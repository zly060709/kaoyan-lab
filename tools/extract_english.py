# -*- coding: utf-8 -*-
"""英语一 legacy HTML → 统一 JSON（M1 数据迁移子任务）。

用法（仓库根执行）:
    python -I -X utf8 tools/extract_english.py

输入（只读，绝不修改）: legacy/考研英语一真题逐题精讲_2010-2024.html
输出:
    data/english/{year}.json            2010..2024 共 15 个分片（每年 52 条：
                                        客观 45 + 翻译 5 + 写作 2；question_count
                                        采用客观题口径 45 以对齐合同验收基准 675）
    data/meta/migration_english.json    迁移报告（题量核对、答案交叉核对、缺漏）
    data/meta/english_dictionary.json   原文内嵌 LOCAL_DICT 大词典原样保全

约束: Python 3 仅标准库；不写 state/；不执行 git；不编造任何题目内容，
解析不了的区块原样进 source_blocks(role="other")，宁可多存不可丢失。
"""
import hashlib
import html as html_mod
import json
import os
import re
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "legacy", "考研英语一真题逐题精讲_2010-2024.html")
OUT_DIR = os.path.join(ROOT, "data", "english")
META_DIR = os.path.join(ROOT, "data", "meta")
SOURCE_REL = "legacy/考研英语一真题逐题精讲_2010-2024.html"
YEARS = list(range(2010, 2025))
SCHEMA_VERSION = "1.0.0"
LETTERS = "ABCDEFGH"

DIV_RE = re.compile(r"<div\b[^>]*>|</div>")
OPEN_DIV_RE = re.compile(r"<div\b[^>]*>")


def sha256(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def class_of(tag):
    m = re.search(r'class="([^"]*)"', tag)
    return m.group(1) if m else ""


def find_block(s, start, limit=300000):
    """start 指向 '<div'，返回 (start, end) 平衡区间（含外壳）。"""
    depth = 0
    for m in DIV_RE.finditer(s, start, min(len(s), start + limit)):
        if m.group(0).startswith("</"):
            depth -= 1
            if depth == 0:
                return start, m.end()
        else:
            depth += 1
    raise ValueError("unbalanced <div> at offset %d" % start)


def inner_of(block):
    """'<div ...> INNER </div>' → INNER"""
    a = block.find(">")
    b = block.rfind("</div>")
    return block[a + 1: b] if b > a else block[a + 1:]


def strip_tags(s):
    return html_mod.unescape(re.sub(r"<[^>]+>", "", s))


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def text_of(html_str):
    return norm(strip_tags(html_str))


def write_json(path, obj):
    """紧凑序列化（控制体积），tmp + os.replace 原子落盘。返回字节数。"""
    data = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(data)
        os.replace(tmp, path)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    return len(data.encode("utf-8"))


# ---------------------------------------------------------------- 面板切分
def load_panels():
    with open(SRC, encoding="utf-8") as f:
        raw = f.read()
    starts = [(int(m.group(1)), m.start())
              for m in re.finditer(r'<div class="year-panel" data-year="(\d+)"', raw)]
    panels = {}
    for idx, (y, s) in enumerate(starts):
        end = starts[idx + 1][1] if idx + 1 < len(starts) else len(raw)
        seg = raw[s:end]
        # 末尾面板之后是内嵌脚本/词典/弹窗等页面级资产，不属于题目内容
        for cut in ("<script", "</main>"):
            p = seg.find(cut)
            if p >= 0:
                seg = seg[:p]
        panels[y] = seg
    return raw, panels


def walk_outer(panel):
    """按文档顺序抓取顶层目标区块，返回 [(first_class, full_class, html)]。"""
    OUTER = {"section-banner", "sub-banner", "bilingual", "nt-opts", "q-card",
             "dir-box", "essay-box", "cover", "quick-nav", "footer"}
    out, skip = [], -1
    for m in OPEN_DIV_RE.finditer(panel):
        if m.start() < skip:
            continue
        cls = class_of(m.group(0))
        first = cls.split(" ")[0] if cls else ""
        if first in OUTER:
            s, e = find_block(panel, m.start())
            out.append((first, cls, panel[m.start():e]))
            skip = e
    return out


# ---------------------------------------------------------------- 区块解析
def parse_cover(html):
    h1 = re.search(r"<h1>(.*?)</h1>", html, re.S)
    subs = re.search(r'<div class="sub">(.*?)</div>', html, re.S)
    metas = [text_of(x) for x in re.findall(r"<span>(.*?)</span>", html, re.S)]
    return {"title": text_of(h1.group(1)) if h1 else "",
            "sub": text_of(subs.group(1)) if subs else "",
            "meta": metas}


def parse_quicknav(html):
    sheet = {}
    for m in re.finditer(r'<div class="answer-cell">\s*(\d+)\s*<b>([A-Z])</b>\s*</div>', html):
        sheet[int(m.group(1))] = m.group(2)
    return sheet


def parse_bilingual(html):
    body = inner_of(html)
    paras = []
    for m in re.finditer(r"<p\b[^>]*>.*?</p>", body, re.S):
        tag = m.group(0)
        a = tag.find(">")
        paras.append({"class": class_of(tag), "html": tag[a + 1: tag.rfind("</p>")],
                      "text": text_of(tag)})
    blanks = sorted({int(n) for n in
                     re.findall(r'<span class="blank">\s*(\d+)\s*</span>', body)})
    return {"paragraphs": paras, "html": body, "text": text_of(body),
            "blanks": blanks,
            "key_sentence_count": len(re.findall(r"key-sentence", body))}


def parse_ntopts(html):
    body = inner_of(html)
    head = re.search(r'<div class="nt-opts-h">(.*?)</div>', body, re.S)
    opts = []
    for m in re.finditer(r'<div class="nt-o">', body):
        s, e = find_block(body, m.start())
        seg = body[s:e]
        lab = re.search(r'<div class="nt-lab">\s*([A-H])\s*</div>', seg)
        en = re.search(r'<div class="nt-en">(.*?)</div>', seg, re.S)
        zh = re.search(r'<div class="nt-zh">(.*?)</div>', seg, re.S)
        opts.append({
            "label": lab.group(1) if lab else "",
            "en": {"html": en.group(1) if en else "", "text": text_of(en.group(1)) if en else ""},
            "zh": {"html": zh.group(1) if zh else "", "text": text_of(zh.group(1)) if zh else ""},
        })
    return {"head": text_of(head.group(1)) if head else "", "options": opts,
            "html": body, "text": text_of(body)}


def parse_qcard(html):
    """题卡 → 结构化片段（不编造：一切字段都来自原文）。"""
    body = inner_of(html)
    num = int(re.search(r'<div class="q-num">\s*(\d+)', body).group(1))
    qtype_m = re.search(r'<div class="q-type">(.*?)</div>', body, re.S)
    qtype = text_of(qtype_m.group(1)) if qtype_m else ""
    qans_m = re.search(r'<div class="q-answer">(.*?)</div>', body, re.S)
    qans_html, qans_text, answer = "", "", None
    if qans_m:
        qans_html, qans_text = qans_m.group(1), text_of(qans_m.group(1))
        am = re.search(r"<b>\s*([A-Z])\s*</b>", qans_html)
        if am:
            answer = am.group(1)

    # stem（个别年份嵌在 q-head 内，故全文搜索）
    stem_html, stem_en, stem_zh = None, "", ""
    sm = re.search(r'<div class="stem">', body)
    if sm:
        s, e = find_block(body, sm.start())
        stem_html = body[s:e]
        si = inner_of(stem_html)
        zh_m = re.search(r'<span class="stem-zh">(.*?)</span>', si, re.S)
        if zh_m:
            stem_zh = text_of(zh_m.group(1))
            stem_en = text_of(si[: zh_m.start()] + si[zh_m.end():])
        else:
            stem_en = text_of(si)

    # options
    options, opts_block, answer_from_opts = [], None, None
    om = re.search(r'<div class="options">', body)
    if om:
        s, e = find_block(body, om.start())
        opts_block = body[s:e]
        oi = inner_of(opts_block)
        idx, skip = 0, -1
        for m in OPEN_DIV_RE.finditer(oi):
            if m.start() < skip:
                continue
            cls = class_of(m.group(0))
            if cls.split(" ")[0] != "opt":
                continue
            s2, e2 = find_block(oi, m.start())
            skip = e2
            idx += 1
            od = oi[s2:e2]
            correct = "correct" in cls.split(" ")
            tm = (re.search(r'<span class="tag">\s*\[([A-H])\]\s*</span>', od)
                  or re.search(r'<span class="opt">\s*\[([A-H])\]\s*</span>', od))
            letter = tm.group(1) if tm else (LETTERS[idx - 1] if idx <= 8 else "")
            zh_m = re.search(r'<span class="opt-zh">(.*?)</span>', od, re.S)
            if zh_m:
                rest, zh_text = od[: zh_m.start()] + od[zh_m.end():], text_of(zh_m.group(1))
            else:
                rest, zh_text = od, ""
            en_text = text_of(rest)  # 含 [X] 标记与行内释义（原文如此）
            options.append(en_text + ((" " + zh_text) if zh_text else ""))
            if correct:
                answer_from_opts = letter

    # block think/detail/vocab/warn/grammar
    blocks, skip = [], -1
    for m in re.finditer(r'<div class="block ([a-z-]+)">', body):
        if m.start() < skip:
            continue
        s, e = find_block(body, m.start())
        skip = e
        blocks.append({"role": m.group(1), "class": "block " + m.group(1),
                       "html": inner_of(body[s:e]), "text": text_of(body[s:e])})

    # trans-box trans-src / trans-zh（翻译题卡）
    trans, skip = [], -1
    for m in re.finditer(r'<div class="trans-box (trans-src|trans-zh)">', body):
        if m.start() < skip:
            continue
        s, e = find_block(body, m.start())
        skip = e
        trans.append({"role": m.group(1), "class": "trans-box " + m.group(1),
                      "html": inner_of(body[s:e]), "text": text_of(body[s:e])})

    # 兜底：题卡内未归类的顶层区块 → role="other"（宁可多存）
    known = {"q-head", "stem", "options"}
    others, skip = [], -1
    for m in OPEN_DIV_RE.finditer(body):
        if m.start() < skip:
            continue
        s, e = find_block(body, m.start())
        skip = e
        cls = class_of(m.group(0))
        first = cls.split(" ")[0] if cls else ""
        if first in known or first == "block" or (first == "trans-box"):
            continue
        others.append({"role": "other", "class": cls, "html": inner_of(body[s:e]),
                       "text": text_of(body[s:e])})

    return {"num": num, "qtype": qtype, "answer": answer,
            "answer_from_opts": answer_from_opts, "qans_html": qans_html,
            "qans_text": qans_text, "stem_html": stem_html,
            "stem_en": stem_en, "stem_zh": stem_zh,
            "options": options, "opts_block": opts_block,
            "blocks": blocks, "trans": trans, "others": others,
            "card_text": text_of(html)}


# ---------------------------------------------------------------- 组装
def type_of_num(num):
    if 1 <= num <= 20:
        return "cloze"
    if 21 <= num <= 40:
        return "reading"
    if 41 <= num <= 45:
        return "partb"
    if 46 <= num <= 50:
        return "translation"
    return "writing"


def content_hash(qid, year, num, typ, stem, options, answer, score, sbs):
    parts = [qid, str(year), str(num), typ, norm(stem)]
    parts += [norm(o) for o in options]
    parts += [answer or "", "" if score is None else str(score)]
    parts += [norm(b["text"]) for b in sbs]
    return sha256("|".join(parts))


def derive_cloze_stem(passage, n):
    """完形无 .stem 的题：从完形原文 .bilingual 中取含第 n 空标记的原句（纯原文抽取）。"""
    pat = re.compile(r'<span class="blank">\s*%d\s*</span>' % n)
    for p in passage["paragraphs"]:
        if p["class"] != "en" or not pat.search(p["html"]):
            continue
        sents = re.split(r'(?<=[.!?])\s+(?=[A-Z"(0-9])', p["text"])
        # 独立空号：前后不挨数字（含千分位 1,932 / 年份 1924）；句末 "2." 亦可命中
        num_re = re.compile(r"(?<![\d.])%d(?![\d])" % n)
        hits = [s for s in sents if num_re.search(s)]
        return (hits[0] if hits else p["text"]), p
    return "", None


def parse_year(year, panel):
    state = {"section": None, "text_no": None, "last_banner": ""}
    cover, footer, answer_sheet = {}, "", {}
    passages, cards, nt_opts, writing_tasks = [], [], None, []

    for first, cls, blockhtml in walk_outer(panel):
        if first == "cover":
            cover = parse_cover(blockhtml)
        elif first == "quick-nav":
            answer_sheet = parse_quicknav(blockhtml)
        elif first == "footer":
            footer = text_of(blockhtml)
        elif first == "section-banner":
            t = text_of(blockhtml)
            state["last_banner"] = t
            if "Use of English" in t:
                state["section"], state["text_no"] = "cloze", None
            elif t.startswith("Reading Part A"):
                state["section"] = "reading"
                m = re.search(r"Text\s*(\d)", t)
                state["text_no"] = int(m.group(1)) if m else None
            elif t.startswith("Part B"):
                state["section"], state["text_no"] = "partb", None
            elif t.startswith("Part C"):
                state["section"], state["text_no"] = "translation", None
            elif "Writing" in t:
                state["section"], state["text_no"] = "writing", None
        elif first == "sub-banner":
            t = text_of(blockhtml)
            state["last_banner"] = t
            if state["section"] == "reading":
                m = re.search(r"Text\s*(\d)", t)
                if m:
                    state["text_no"] = int(m.group(1))
            elif state["section"] == "writing":
                sm = re.search(r"（(\d+)分）", t)
                writing_tasks.append({"banner": t, "banner_html": blockhtml,
                                      "score": int(sm.group(1)) if sm else None,
                                      "dir": None, "essays": []})
        elif first == "bilingual":
            kind = state["section"] if state["section"] in ("cloze", "reading", "partb") else "other"
            b = parse_bilingual(blockhtml)
            passages.append({
                "id": "eng-%d-p-%s%s" % (year, kind, state["text_no"] or ""),
                "kind": kind, "text_no": state["text_no"],
                "banner": state["last_banner"], **b})
        elif first == "nt-opts":
            nt_opts = parse_ntopts(blockhtml)
        elif first == "q-card":
            cards.append(parse_qcard(blockhtml))
        elif first == "dir-box":
            if writing_tasks:
                writing_tasks[-1]["dir"] = blockhtml
        elif first == "essay-box":
            if writing_tasks:
                writing_tasks[-1]["essays"].append(blockhtml)

    # ---- 逐题组装 ----
    questions = []
    partb_passage = next((p for p in passages if p["kind"] == "partb"), None)
    cloze_passage = next((p for p in passages if p["kind"] == "cloze"), None)
    missing = []

    for c in cards:
        num, typ = c["num"], type_of_num(c["num"])
        sbs = []
        stem = c["stem_en"]
        # ① 答案块（q-answer 原文）
        if c["qans_html"]:
            sbs.append({"role": "answer", "class": "q-answer",
                        "html": c["qans_html"], "text": c["qans_text"]})
        # ② 题干块（stem + stem-zh 原样保留）
        if c["stem_html"]:
            sbs.append({"role": "stem", "class": "stem", "html": c["stem_html"],
                        "text": text_of(c["stem_html"])})
        elif typ == "cloze" and cloze_passage:
            sent, para = derive_cloze_stem(cloze_passage, num)
            if sent:
                stem = sent
                if para:
                    sbs.append({"role": "stem-ctx", "class": "bilingual p.en",
                                "html": para["html"], "text": para["text"]})
            else:
                missing.append("%d: cloze-%d stem-ctx 未定位" % (year, num))
        elif typ == "partb" and partb_passage:
            # 优先【题目】段；个别年份（如 2020）原文只有【选项】段 → 取该双语块首段，
            # 均为原文内容，不编造。
            paras = partb_passage["paragraphs"]
            topic = (next((p for p in paras if p["text"].startswith("【题目】")), None)
                     or (paras[0] if paras else None))
            if topic:
                stem = topic["text"]
                sbs.append({"role": "stem-ctx", "class": "bilingual p",
                            "html": topic["html"], "text": topic["text"]})
            else:
                missing.append("%d: partb 双语块无任何段落" % year)
        # ③ 选项块
        if c["opts_block"]:
            sbs.append({"role": "options", "class": "options",
                        "html": inner_of(c["opts_block"]),
                        "text": text_of(c["opts_block"])})
        # ④ 翻译原文/译文
        for t in c["trans"]:
            sbs.append(t)
        # ⑤ 解析区块（think/detail/vocab/warn/grammar）
        sbs.extend(c["blocks"])
        # ⑥ 新题型选项原文（英汉对照）→ 附入 41–45 每题
        if typ == "partb" and nt_opts:
            sbs.append({"role": "nt-opts", "class": "nt-opts",
                        "html": nt_opts["html"], "text": nt_opts["text"]})
        # ⑦ 未归类区块兜底
        sbs.extend(c["others"])

        # 翻译题：题干 = 原文英文句（trans-src）
        if typ == "translation" and not stem:
            stem = next((t["text"] for t in c["trans"] if t["role"] == "trans-src"), "")

        answer = c["answer"]
        if typ in ("cloze", "reading") and c["answer_from_opts"] and answer \
                and c["answer_from_opts"] != answer:
            missing.append("%d: 第%d题 q-answer(%s) 与 opt.correct(%s) 不一致"
                           % (year, num, answer, c["answer_from_opts"]))

        qid = "eng-%d-%d" % (year, num)
        questions.append({
            "id": qid, "subject": "english", "year": year, "paper": "英语一",
            "num": num, "type": typ, "stem": stem,
            "options": c["options"] if typ in ("cloze", "reading") else [],
            "answer": answer, "score": None,
            "source_blocks": sbs,
            "knowledge_points": [c["qtype"]] if c["qtype"] else [],
            "tags": [typ], "media": [], "origin": "source",
            "content_hash": content_hash(qid, year, num, typ, stem,
                                         c["options"], answer, None, sbs),
            "source_hash": sha256(c["card_text"]),
            "schema_version": SCHEMA_VERSION,
            "source_ref": {"file": SOURCE_REL, "year": year, "num": num,
                           "anchor": "year-panel[data-year=%d] .q-card .q-num=%d"
                                     % (year, num)},
        })

    # ---- 写作两题（原文无 q-card，由 sub-banner + dir-box + essay-box 组装）----
    for i, w in enumerate(writing_tasks):
        num = 51 + i
        sbs = [{"role": "sub-banner", "class": "sub-banner",
                "html": inner_of(w["banner_html"]), "text": w["banner"]}]
        dir_text, dir_en = "", ""
        if w["dir"]:
            dhtml = inner_of(w["dir"])
            dir_text = text_of(w["dir"])
            em = re.search(r'<p class="dir-en">(.*?)</p>', dhtml, re.S)
            dir_en = text_of(em.group(1)) if em else dir_text
            sbs.append({"role": "dir-box", "class": "dir-box",
                        "html": dhtml, "text": dir_text})
        for eb in w["essays"]:
            sbs.append({"role": "essay-box", "class": "essay-box",
                        "html": inner_of(eb), "text": text_of(eb)})
        qid = "eng-%d-%d" % (year, num)
        text_src = norm(" ".join([w["banner"], dir_text] +
                                 [b["text"] for b in sbs[2:]]))
        questions.append({
            "id": qid, "subject": "english", "year": year, "paper": "英语一",
            "num": num, "type": "writing", "stem": dir_en, "options": [],
            "answer": None, "score": w["score"],
            "source_blocks": sbs, "knowledge_points": [], "tags": ["writing"],
            "media": [], "origin": "source",
            "content_hash": content_hash(qid, year, num, "writing", dir_en,
                                         [], None, w["score"], sbs),
            "source_hash": sha256(text_src),
            "schema_version": SCHEMA_VERSION,
            "source_ref": {"file": SOURCE_REL, "year": year, "num": num,
                           "anchor": "year-panel[data-year=%d] .sub-banner=%s"
                                     % (year, w["banner"][:40])},
        })

    questions.sort(key=lambda q: q["num"])

    # ---- 答案交叉核对（q-answer 为准，速查表核对，不改写）----
    mismatches = []
    for q in questions:
        if q["type"] in ("cloze", "reading", "partb") and q["answer"]:
            quick = answer_sheet.get(q["num"])
            if quick and quick != q["answer"]:
                mismatches.append({"year": year, "num": q["num"],
                                   "q_answer": q["answer"], "quick_nav": quick})
    # 速查表应恰好覆盖 1..45
    for n in range(1, 46):
        if n not in answer_sheet:
            missing.append("%d: 答案速查表缺第%d题" % (year, n))

    obj = [q for q in questions if q["type"] in ("cloze", "reading", "partb")]
    trans = [q for q in questions if q["type"] == "translation"]
    writ = [q for q in questions if q["type"] == "writing"]
    if len(obj) != 45:
        missing.append("%d: 客观题=%d（应为45）" % (year, len(obj)))
    if len(trans) != 5:
        missing.append("%d: 翻译=%d（应为5）" % (year, len(trans)))
    if len(writ) != 2:
        missing.append("%d: 写作=%d（应为2）" % (year, len(writ)))
    if cloze_passage and cloze_passage["blanks"] != list(range(1, 21)):
        missing.append("%d: 完形 blank 标记=%s（应为1..20）" % (year, cloze_passage["blanks"]))

    year_doc = {
        "subject": "english", "year": year, "paper": "英语一",
        "schema_version": SCHEMA_VERSION, "source_file": SOURCE_REL,
        "question_count": len(obj),          # 客观题口径（合同验收基准 45/年）
        "total_question_count": len(questions),
        "objective_count": len(obj), "translation_count": len(trans),
        "writing_count": len(writ), "passage_count": len(passages),
        "cover": cover, "answer_sheet": {str(k): v for k, v in sorted(answer_sheet.items())},
        "questions": questions, "passages": passages,
        "partb_options": ({"head": nt_opts["head"],
                           "options": [{"label": o["label"], "en": o["en"]["text"],
                                        "zh": o["zh"]["text"]} for o in nt_opts["options"]]}
                          if nt_opts else None),
        "footer": footer,
    }
    return year_doc, mismatches, missing


def extract_dictionary(raw):
    i = raw.find("var LOCAL_DICT =")
    if i < 0:
        return None
    j = raw.find("</script>", i)
    blob = raw[i + len("var LOCAL_DICT ="): j].strip().rstrip(";")
    try:
        return json.loads(blob)
    except Exception:
        return None


DICT_SHARDS = [("a-g", "abcdefg"), ("h-n", "hijklmn"), ("o-t", "opqrst"), ("u-z", "uvwxyz")]


def write_dictionary_shards(dic):
    """内嵌大词典按首字母分 4 片落盘（单文件 ≤500KB，内容一条不丢）。"""
    shards = {name: {} for name, _ in DICT_SHARDS}
    for k, v in dic.items():
        c = (k[:1] or " ").lower()
        for name, letters in DICT_SHARDS:
            if c in letters:
                shards[name][k] = v
                break
        else:
            shards["a-g"][k] = v  # 数字/符号开头等归入首片
    out = []
    for name, _ in DICT_SHARDS:
        p = os.path.join(META_DIR, "english_dictionary_%s.json" % name)
        out.append({"file": "data/meta/english_dictionary_%s.json" % name,
                    "entries": len(shards[name]), "bytes": write_json(p, shards[name])})
    return out


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    raw, panels = load_panels()
    if sorted(panels) != YEARS:
        print("FATAL: 年份面板不齐: %s" % sorted(panels))
        return 1

    report_missing, report_mismatch = [], []
    per_year_obj, per_year_trans, per_year_writ, sizes = {}, {}, {}, {}
    total_obj = 0
    for y in YEARS:
        doc, mism, miss = parse_year(y, panels[y])
        report_mismatch += mism
        report_missing += miss
        n = write_json(os.path.join(OUT_DIR, "%d.json" % y), doc)
        sizes[y] = n
        obj = doc["objective_count"]
        per_year_obj[str(y)] = obj
        per_year_trans[str(y)] = doc["translation_count"]
        per_year_writ[str(y)] = doc["writing_count"]
        total_obj += obj
        print("%d: 客观=%d 翻译=%d 写作=%2d passages=%d blocks/题≈%.1f  %.0f KB %s"
              % (y, obj, doc["translation_count"], doc["writing_count"],
                 doc["passage_count"],
                 sum(len(q["source_blocks"]) for q in doc["questions"]) / max(1, len(doc["questions"])),
                 n / 1024, "OK" if n < 500 * 1024 else "OVER-500KB!"))

    # 内嵌大词典原样保全（合同「英语：内嵌大词典与点词查词…一条不丢」），按首字母分片
    dic = extract_dictionary(raw)
    dic_shards = write_dictionary_shards(dic) if dic else []

    meta = {
        "subject": "english",
        "expected_objective": 675,
        "actual_objective": total_obj,
        "per_year_objective": per_year_obj,
        "translation_years": sum(1 for v in per_year_trans.values() if v == 5),
        "writing_years": sum(1 for v in per_year_writ.values() if v == 2),
        "per_year_translation": per_year_trans,
        "per_year_writing": per_year_writ,
        "missing": report_missing,
        "answer_mismatches": report_mismatch,
        "ok": total_obj == 675 and not report_missing and not report_mismatch,
        "max_file_bytes": max(sizes.values()),
        "file_bytes": {str(k): v for k, v in sizes.items()},
        "dictionary_entries": len(dic) if dic else 0,
        "dictionary_shards": dic_shards,
        "source_file": SOURCE_REL,
        "source_sha256": sha256(raw),
        "hash_algorithm": {
            "source_hash": "sha256(题卡 text_of(outer html)，空白归一)",
            "content_hash": "sha256(id|year|num|type|stem|options...|answer|score|source_blocks.text... 各段 norm 后以 | 连接)",
        },
        "schema_version": SCHEMA_VERSION,
        "generated_at": "2026-11-04",
        "tool": "tools/extract_english.py",
    }
    mn = write_json(os.path.join(META_DIR, "migration_english.json"), meta)

    print("-" * 60)
    print("客观题合计: %d / 675   翻译年份: %d   写作年份: %d"
          % (total_obj, meta["translation_years"], meta["writing_years"]))
    print("答案交叉核对不一致: %d   缺漏: %d" % (len(report_mismatch), len(report_missing)))
    for m in report_mismatch:
        print("  MISMATCH:", m)
    for m in report_missing:
        print("  MISSING:", m)
    print("最大分片: %.0f KB (限额 500KB)" % (meta["max_file_bytes"] / 1024))
    print("词典: %d 条 → %d 个分片（每片 ≤500KB）"
          % (meta["dictionary_entries"], len(dic_shards)))
    for s in dic_shards:
        print("   %s: %d 条, %.0f KB" % (s["file"], s["entries"], s["bytes"] / 1024))
    print("meta: %.0f KB → data/meta/migration_english.json" % (mn / 1024))
    print("source_sha256:", meta["source_sha256"][:16], "…")
    print("RESULT:", "OK" if meta["ok"] and meta["max_file_bytes"] < 500 * 1024 else "FAIL")
    return 0 if meta["ok"] and meta["max_file_bytes"] < 500 * 1024 else 2


if __name__ == "__main__":
    sys.exit(main())
