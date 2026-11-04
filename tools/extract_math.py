# -*- coding: utf-8 -*-
"""数学一 legacy HTML -> data/math/{year}.json 数据迁移（M1，AGENT_CONTRACT 第 1/2 章）。

用法: python -I -X utf8 tools/extract_math.py
只读 legacy/数学一真题精讲_2013-2023_重制版.html；输出 data/math/2013..2023.json
与 data/meta/migration_math.json。题量基准（验收，缺一不合格）：
2013-2020 每年 23 题、2021-2023 每年 22 题，共 250。

保真铁律：
- $...$ / $$...$$ 逐字保留在 stem/options/answer/source_blocks 的 text/html 中；
- 答案以原文 b-daan 区块为准，不改动；
- 解析不了的区块进 source_blocks 且 role="other"；
- 原文无分值标记的题 score=null，不编造；
- 20 张内嵌 base64 配图解码落盘 data/math/media/（字节=原 base64 解码，
  逐像素一致），html src 改写为相对路径以满足单文件 <=500KB 分片上限。

哈希配方（CI 复算依据）：
- source_hash = sha256(原始题卡 HTML 子串, UTF-8)（legacy 只读，故稳定）；
- content_hash = sha256(canonical JSON{stem,options,blocks[role,label,text]}，
  ensure_ascii=False, sort_keys, 紧凑分隔符)。
"""
import base64
import hashlib
import json
import os
import re
import sys
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "legacy", "数学一真题精讲_2013-2023_重制版.html")
OUT_DIR = os.path.join(ROOT, "data", "math")
MEDIA_DIR = os.path.join(ROOT, "data", "math", "media")
META_PATH = os.path.join(ROOT, "data", "meta", "migration_math.json")
SCHEMA_VERSION = "1.0.0"
SOURCE_FILE = "legacy/数学一真题精讲_2013-2023_重制版.html"
MAX_FILE_BYTES = 500 * 1024

YEARS = list(range(2013, 2024))
EXPECTED = {y: (23 if y <= 2020 else 22) for y in YEARS}
TYPE_MAP = {"选择题": "single", "填空题": "fill", "解答题": "essay"}
ANALYSIS_ROLES = {
    "b-kaodian": "kaodian", "b-silu": "silu", "b-jiefa": "jiefa",
    "b-biaozhun": "biaozhun", "b-qita": "qita", "b-yicuo": "yicuo",
    "b-guina": "guina",
}
BLOCK_TAGS = {"p", "div", "figure", "figcaption", "ul", "ol", "li", "section",
              "article", "h1", "h2", "h3", "h4", "h5", "h6", "table", "tr",
              "blockquote", "pre", "hr"}

IMG_RE = re.compile(r'src="data:image/(\w+);base64,([^"]+)"')
OPT_RE = re.compile(r'<div class="opt">(.*?)</div>', re.S)
OPT_KEY_RE = re.compile(r'<span class="opt-key">(.*?)</span>', re.S)
OPT_TXT_RE = re.compile(r'<span class="opt-txt">(.*?)</span>', re.S)
BTAG_RE = re.compile(r'<div class="b-tag">(.*?)</div>', re.S)
BLOCK_CLS_RE = re.compile(r'<div class="(block [^"]+)">')
PAPER = {}


class _TextExtractor(HTMLParser):
    """HTML -> text：实体解码、\\xa0->空格、段内软换行折叠为单空格、
    块级标签处断行。$...$ / $$...$$ 位于文本节点，逐字保留。"""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.buf = []
        self.skip = 0  # svg/math 内部无文本内容，跳过

    def handle_starttag(self, tag, attrs):
        if tag in ("svg", "math"):
            self.skip += 1
            return
        if self.skip:
            return
        if tag == "br" or tag in BLOCK_TAGS:
            self.buf.append("\n")

    def handle_startendtag(self, tag, attrs):
        if self.skip:
            return
        if tag == "br" or tag in BLOCK_TAGS:
            self.buf.append("\n")

    def handle_endtag(self, tag):
        if tag in ("svg", "math"):
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        if tag in BLOCK_TAGS:
            self.buf.append("\n")

    def handle_data(self, data):
        if self.skip:
            return
        # 段内空白（含源文件软换行）折叠为单空格 —— HTML 渲染语义，非内容改写
        self.buf.append(re.sub(r"\s+", " ", data.replace("\xa0", " ")))


def html_to_text(html):
    p = _TextExtractor()
    p.feed(html)
    p.close()
    lines = ("".join(p.buf)).split("\n")
    return "\n".join(ln.strip() for ln in lines if ln.strip())


DIV_OPEN = re.compile(r"<div\b", re.I)
DIV_CLOSE = re.compile(r"</div\s*>", re.I)


def balanced_div(s, i):
    """s[i] 处为 '<div'。返回 (inner_html, end_after_close_tag, class_attr)。"""
    assert s[i:i + 4].lower() == "<div", "balanced_div 起点必须是 <div"
    depth = 0
    j = i
    cls = None
    while True:
        mo = DIV_OPEN.search(s, j)
        mc = DIV_CLOSE.search(s, j)
        if mc is None:
            raise ValueError("div 未闭合 @%d" % i)
        if mo and mo.start() < mc.start():
            if depth == 0:
                mattr = re.match(r'<div[^>]*class="([^"]*)"', s[mo.start():mo.start() + 300])
                cls = mattr.group(1) if mattr else ""
            depth += 1
            j = mo.end()
        else:
            depth -= 1
            if depth == 0:
                mopen = re.match(r"<div[^>]*>", s[i:])
                open_end = i + mopen.end()
                return s[open_end:mc.start()], mc.end(), cls
            j = mc.end()


def find_exact_div(s, class_attr, start=0):
    m = re.compile(r'<div class="' + re.escape(class_attr) + r'">').search(s, start)
    return m.start() if m else -1


def extract_images(card, media_used):
    """base64 内嵌图 -> data/math/media/img-<sha12>.png（字节=原解码，逐像素一致）。
    html 中 src 改写为相对路径；同内容（同哈希）复用同一文件。"""
    def repl(m):
        ext = m.group(1).lower()
        raw = base64.b64decode(m.group(2).strip())
        h = hashlib.sha256(raw).hexdigest()[:12]
        name = "img-%s.%s" % (h, ext)
        path = os.path.join(MEDIA_DIR, name)
        if not os.path.exists(path):
            with open(path, "wb") as f:
                f.write(raw)
        rel = "data/math/media/" + name
        media_used.append(rel)
        return 'src="%s"' % rel
    return IMG_RE.sub(repl, card)


def sha256_text(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def parse_card(cid_raw, year, num, raw_slice, warn):
    """解析单张题卡。raw_slice=原始（未改图）题卡 HTML 子串。"""
    media_used = []
    card_html = extract_images(raw_slice, media_used)

    cat_key = re.search(r'data-cat="(\w+)"', card_html)
    cat_label = re.search(r'<span class="cat-pill[^"]*">([^<]+)</span>', card_html)
    q_type_zh = re.search(r'<span class="q-type">([^<]+)</span>', card_html)
    q_num_txt = re.search(r'<span class="q-num">([^<]+)</span>', card_html)
    if not (cat_key and cat_label and q_type_zh):
        warn.append("%s: 缺少 card 头部字段" % cid_raw)
    if q_num_txt:
        m = re.search(r"第\s*(\d+)\s*题", q_num_txt.group(1))
        if m and int(m.group(1)) != num:
            warn.append("%s: q-num(%s) 与 id 题号(%d)不一致" % (cid_raw, q_num_txt.group(1), num))

    qtype = TYPE_MAP.get(q_type_zh.group(1).strip())
    if qtype is None:
        warn.append("%s: 未知题型「%s」" % (cid_raw, q_type_zh.group(1)))

    blocks = []
    stem_text = ""
    options = []

    # --- 题干 q-stem（含内联选项/配图/figcaption，原样保留） ---
    i = find_exact_div(card_html, "q-stem")
    if i < 0:
        warn.append("%s: 未找到 q-stem" % cid_raw)
        stem_html = ""
    else:
        stem_html, _, _ = balanced_div(card_html, i)
        stem_text = html_to_text(stem_html)
    blocks.append({"role": "stem", "class": "q-stem", "html": stem_html,
                   "text": stem_text})

    # --- 选项：仅取结构化 div.opt；散落题干内联的选项保留在 stem 原文中 ---
    for mo in OPT_RE.finditer(stem_html):
        mk = OPT_KEY_RE.search(mo.group(1))
        mt = OPT_TXT_RE.search(mo.group(1))
        key = html_to_text(mk.group(1)) if mk else ""
        txt = html_to_text(mt.group(1)) if mt else ""
        options.append(key + txt)

    # --- 答案 b-daan-wrap / ans-body（折叠状态用 hidden 记录） ---
    ans_i = card_html.find('<div class="block b-daan-wrap">')
    ans_text = ""
    if ans_i < 0:
        warn.append("%s: 未找到 b-daan-wrap" % cid_raw)
    else:
        wrap_inner, _, _ = balanced_div(card_html, ans_i)
        mexp = re.search(r'aria-expanded="(\w+)"', wrap_inner)
        mbody = re.compile(r'<div class="(ans-body[^"]*)">').search(wrap_inner)
        if not mbody:
            warn.append("%s: 未找到 ans-body" % cid_raw)
        else:
            ans_html, _, ans_cls = balanced_div(wrap_inner, mbody.start())
            ans_text = html_to_text(ans_html)
            hidden = "show" not in (ans_cls or "") or (mexp and mexp.group(1) == "false")
            blocks.append({"role": "answer", "class": ans_cls, "html": ans_html,
                           "text": ans_text, "hidden": bool(hidden)})

    # --- 七个固定分块 + 未登记块（按文档顺序；未知块 role="other" 全量保留） ---
    for mb in BLOCK_CLS_RE.finditer(card_html):
        cls = mb.group(1)
        second = cls.split()[1] if len(cls.split()) > 1 else ""
        if second == "b-daan-wrap":
            continue
        inner, _, _ = balanced_div(card_html, mb.start())
        if second in ANALYSIS_ROLES:
            role = ANALYSIS_ROLES[second]
            mlbl = BTAG_RE.search(inner)
            label = html_to_text(mlbl.group(1)) if mlbl else None
            body_i = find_exact_div(inner, "b-body")
            if body_i >= 0:
                body_html, _, _ = balanced_div(inner, body_i)
            else:
                warn.append("%s: %s 无 b-body，按整块保留" % (cid_raw, second))
                body_html = inner
            blocks.append({"role": role, "class": cls, "label": label,
                           "html": body_html, "text": html_to_text(body_html)})
        else:
            blocks.append({"role": "other", "class": cls, "html": inner,
                           "text": html_to_text(inner)})

    # --- 分值：仅取题面「（本题满分 N 分）」标记，无则 null，不编造 ---
    mscore = re.search(r"本题满分\s*(\d+)\s*分", stem_text)
    score = int(mscore.group(1)) if mscore else None

    # --- 考点：仅取 b-kaodian「考点定位」原文文字，不拆不改 ---
    kp = next((b["text"] for b in blocks if b["role"] == "kaodian"), None)
    knowledge_points = [kp] if kp else []

    content_payload = json.dumps(
        {"stem": stem_text, "options": options,
         "blocks": [{"role": b["role"], "label": b.get("label"), "text": b["text"]}
                    for b in blocks]},
        ensure_ascii=False, sort_keys=True, separators=(",", ":"))

    q = {
        "id": "math-%d-%d" % (year, num),
        "subject": "math",
        "year": year,
        "paper": PAPER.get(year, "数学（一）真题精讲"),
        "num": num,
        "type": qtype,
        "stem": stem_text,
        "options": options,
        "answer": ans_text or None,
        "score": score,
        "source_blocks": blocks,
        "knowledge_points": knowledge_points,
        "tags": ["math"],
        "media": media_used,
        "category": {"key": cat_key.group(1) if cat_key else None,
                     "label": cat_label.group(1) if cat_label else None},
        "origin": "source",
        "content_hash": sha256_text(content_payload),
        "schema_version": SCHEMA_VERSION,
        "source_hash": sha256_text(raw_slice),
        "source_ref": {"file": SOURCE_FILE, "anchor": cid_raw,
                       "year": year, "num": num},
    }
    # LaTeX 保真证据：原文题卡与产出 text 字段的 $ 数量逐题一致（内部字段，落盘前弹出）
    q["_dollars_raw"] = raw_slice.count("$")
    q["_dollars_json"] = (stem_text + ans_text +
                          "".join(b["text"] for b in blocks
                                  if b["role"] not in ("stem", "answer"))).count("$")
    return q


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    os.makedirs(MEDIA_DIR, exist_ok=True)
    with open(SRC, "rb") as f:
        html = f.read().decode("utf-8")  # 字节解码，不做 EOL 翻译

    for m in re.finditer(
            r'<section class="year-view" data-year="(\d+)"><div class="year-head">'
            r'<div class="yh-title">([^<]+)</div><div class="yh-sub">([^<]+)</div>', html):
        PAPER[int(m.group(1))] = m.group(3).split("·")[0].strip()

    warn = []
    starts = [m.start() for m in re.finditer(r'<article class="card', html)]
    by_year = {y: [] for y in YEARS}
    for a in starts:
        end = html.find("</article>", a)
        raw_slice = html[a:end + len("</article>")]
        if raw_slice.count("<article") != 1:
            warn.append("@%d: 题卡内嵌套 <article>，切分异常" % a)
        mid = re.search(r'id="p(\d+)-(\d+)"', raw_slice)
        if not mid:
            warn.append("@%d: 题卡缺 id" % a)
            continue
        year, num = int(mid.group(1)), int(mid.group(2))
        if year not in by_year:
            warn.append("p%d-%d: 年份不在基准范围" % (year, num))
            continue
        if "\\(" in raw_slice or "\\[" in raw_slice:
            warn.append("p%d-%d: 发现 $ 以外的数学定界符（需人工复核）" % (year, num))
        by_year[year].append(parse_card("p%d-%d" % (year, num), year, num, raw_slice, warn))

    # LaTeX 逐题校验（先算后弹内部字段，避免落盘泄漏）
    all_q = [q for y in YEARS for q in by_year[y]]
    n_dollar_bad = [q["id"] for q in all_q if q["_dollars_raw"] != q["_dollars_json"]]
    for q in all_q:
        q.pop("_dollars_raw")
        q.pop("_dollars_json")

    # ---------- 抽样原文对照（2013/2019/2023 各首末题）----------
    # 方法：对原题卡切片独立跑一遍 tag-aware 文本化（忽略全部空白后），
    # 产出 stem/answer 文本（去空白）必须是原文卡文本的连续子串。
    spot = []
    spot_years = (2013, 2019, 2023)
    for y in spot_years:
        qs = sorted(by_year[y], key=lambda q: q["num"])
        for q in (qs[0], qs[-1]):
            anchor = q["source_ref"]["anchor"]
            a = html.find('id="%s"' % anchor)
            a = html.rfind("<article", 0, a)
            b = html.find("</article>", a) + len("</article>")
            card_flat = re.sub(r"\s+", "", html_to_text(html[a:b]))
            stem_key = re.sub(r"\s+", "", q["stem"])
            ans_key = re.sub(r"\s+", "", q["answer"] or "")
            spot.append({
                "id": q["id"],
                "stem_hit": bool(stem_key) and stem_key in card_flat,
                "answer_hit": bool(ans_key) and ans_key in card_flat,
                "stem_preview": q["stem"][:42].replace("\n", " / "),
                "answer_preview": (q["answer"] or "")[:42].replace("\n", " / "),
            })

    # ---------- 写文件 ----------
    per_year, missing, over_size, latex_ratio = {}, [], [], {}
    for y in YEARS:
        qs = sorted(by_year[y], key=lambda q: q["num"])
        nums = [q["num"] for q in qs]
        for n in range(1, EXPECTED[y] + 1):
            if n not in nums:
                missing.append("math-%d-%d" % (y, n))
        for n in nums:
            if n not in range(1, EXPECTED[y] + 1):
                warn.append("math-%d-%d: 题号超出基准（多出）" % (y, n))
        per_year[y] = len(qs)
        latex_ratio[y] = round(sum(1 for q in qs if "$" in q["stem"]) / len(qs), 4) if qs else 0.0
        doc = {"subject": "math", "year": y, "paper": PAPER.get(y, ""),
               "question_count": len(qs), "questions": qs}
        payload = json.dumps(doc, ensure_ascii=False, indent=2)
        if len(payload.encode("utf-8")) > MAX_FILE_BYTES:
            payload = json.dumps(doc, ensure_ascii=False, separators=(",", ":"))
        fp = os.path.join(OUT_DIR, "%d.json" % y)
        with open(fp, "w", encoding="utf-8", newline="\n") as f:
            f.write(payload)
        size = os.path.getsize(fp)
        if size > MAX_FILE_BYTES:
            over_size.append("%d.json=%dB" % (y, size))
        print("%d.json: %d 题, %.1f KB" % (y, len(qs), size / 1024))

    total = sum(per_year.values())
    ok = (total == 250 and not missing and not over_size
          and not n_dollar_bad and not warn and per_year == EXPECTED
          and all(s["stem_hit"] and s["answer_hit"] for s in spot))
    meta = {
        "expected_total": 250,
        "actual_total": total,
        "per_year": {str(y): per_year[y] for y in YEARS},
        "missing": missing,
        "latex_stem_ratio": {str(y): latex_ratio[y] for y in YEARS},
        "latex_dollar_mismatch": n_dollar_bad,
        "images_extracted": len(os.listdir(MEDIA_DIR)),
        "files_over_500kb": over_size,
        "spot_check": spot,
        "warnings": warn,
        "ok": ok,
    }
    os.makedirs(os.path.dirname(META_PATH), exist_ok=True)
    with open(META_PATH, "w", encoding="utf-8", newline="\n") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    print("-" * 46)
    print("总题数: %d / 250   per_year=%s" % (total, per_year))
    print("LaTeX $ 逐题校验不一致: %s" % (n_dollar_bad or "无"))
    print("stem 含 $ 比例:", latex_ratio)
    for s in spot:
        print("抽样 %s: stem命中=%s answer命中=%s | %s | 答:%s"
              % (s["id"], s["stem_hit"], s["answer_hit"], s["stem_preview"], s["answer_preview"]))
    if warn:
        print("警告:", warn)
    print("迁移结果: %s  (meta -> %s)" % ("OK" if ok else "FAIL", META_PATH))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
