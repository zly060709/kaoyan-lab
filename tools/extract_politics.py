# -*- coding: utf-8 -*-
"""考研政治真题迁移：legacy HTML -> data/politics/{year}.json
保真：原文区块（题干/答案/思路/解析/背景/问答/框架/材料）全量进 source_blocks，不改写。
用法: python -I -X utf8 tools/extract_politics.py"""
import hashlib, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "legacy", "考研政治真题逐题精讲_修复版.html")
OUTD = os.path.join(ROOT, "data", "politics")
METAD = os.path.join(ROOT, "data", "meta")
os.makedirs(OUTD, exist_ok=True); os.makedirs(METAD, exist_ok=True)
raw = open(SRC, encoding="utf-8", errors="replace").read()

ROLES = [
    ("stem",      ("q-text", "q-stem", "b-question", "stem-block", "question-block", "q-question", "question-text")),
    ("answer",    ("q-answer", "answer-block", "b-answer")),
    ("approach",  ("q-approach", "approach-block", "b-approach")),
    ("analysis",  ("q-analysis", "analysis-block", "b-analysis")),
    ("background",("q-background", "background-block", "b-background", "q-bg")),
    ("qa",        ("q-qa", "qa-block", "b-qa")),
    ("frame",     ("frame", "framework")),
    ("material",  ("material",)),
]

def role_of(cls):
    toks = set(cls.split())
    for role, keys in ROLES:
        if toks & set(keys):
            return role
    return "other" if "block" in toks else None

DIV_RE = re.compile(r"<div\b[^>]*>", re.I)
CLS_RE = re.compile(r'class="([^"]*)"')
CLOSE_RE = re.compile(r"</div\s*>", re.I)

def block_end(h, i):
    depth = 1; pos = i
    while depth:
        mo = DIV_RE.search(h, pos); mc = CLOSE_RE.search(h, pos)
        if not mc:
            return len(h)
        if mo and mo.start() < mc.start():
            depth += 1; pos = mo.end()
        else:
            depth -= 1
            if depth == 0:
                return mc.start()
            pos = mc.end()
    return len(h)

def strip_tags(s):
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    for a, b in [("&nbsp;", " "), ("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'),
                 ("&#39;", "'"), ("&ldquo;", "“"), ("&rdquo;", "”"), ("&mdash;", "—"), ("&hellip;", "…")]:
        s = s.replace(a, b)
    s = re.sub(r"&[a-zA-Z#0-9]+;", " ", s)
    return re.sub(r"\s+", " ", s).strip()

TAGMAP = [("马原", "马原"), ("毛中特", "毛中特"), ("毛泽东思想", "毛中特"), ("史纲", "史纲"),
          ("思修", "思修法基"), ("思想道德", "思修法基"), ("时政", "时政当代"),
          ("当代世界经济", "时政当代"), ("形势与政策", "时政当代")]

def parse_article(year, num, art):
    tm = re.search(r"(?s)<h2[^>]*>(.*?)</h2>", art)
    title = strip_tags(tm.group(1)) if tm else f"第{num}题"
    if "多项选择题" in title: qtype = "multi"
    elif "单项选择题" in title: qtype = "single"
    elif num >= 34: qtype = "essay"
    else: qtype = "other"
    score = {"single": 1, "multi": 2, "essay": 10}.get(qtype, None)

    blocks = []
    for m in DIV_RE.finditer(art):
        cm = CLS_RE.search(m.group(0))
        if not cm: continue
        cls = cm.group(1)
        role = role_of(cls)
        if not role: continue
        inner = art[m.end():block_end(art, m.end())]
        inner = re.sub(r"(?s)<h4[^>]*>.*?</h4>", "", inner, count=1).strip()
        if blocks and blocks[-1]["_s"] <= m.start() < blocks[-1]["_e"] and blocks[-1]["role"] == role:
            blocks[-1]["_e"] = block_end(art, m.end())  # 嵌套同类块合并
            continue
        blocks.append({"role": role, "class": cls, "html": inner, "text": strip_tags(inner), "_s": m.start(), "_e": block_end(art, m.end())})
    for b in blocks:
        b.pop("_s"); b.pop("_e")

    answer = ""
    for b in blocks:
        if b["role"] == "answer":
            am = re.search(r'badge[^"]*"[^>]*>\s*([A-D]{1,4})\s*<', b["html"])
            if am:
                answer = am.group(1); break

    stem, options = "", []
    sb = next((b for b in blocks if b["role"] == "stem"), None)
    if sb:
        h = re.sub(r"(?s)<h4[^>]*>.*?</h4>", "", sb["html"])
        om = re.search(r'<div class="opts[^"]*"[^>]*>', h)
        if om:
            gt = h.index(">", om.start()) + 1
            oend = block_end(h, gt)
            oinner = h[gt:oend]
            options = [strip_tags(x) for x in re.findall(r"(?s)<(?:div|li)[^>]*>(.*?)</(?:div|li)>", oinner)]
            stem = strip_tags(h[:om.start()])
        else:
            stem = strip_tags(h)

    km = re.search(r"（([^（）]*(?:（[^（）]*）[^（）]*)*)）\s*$", title)
    kp_raw = km.group(1) if km else ""
    segs = [s.strip() for s in re.split(r"[·•]", kp_raw) if s.strip()]
    tags = []
    for key, tag in TAGMAP:
        if key in title or any(key in s for s in segs):
            if tag not in tags: tags.append(tag)
    if qtype == "essay" and "分析题" not in tags: tags.append("分析题")
    knowledge_points = [s for s in segs[1:]] if segs else ([kp_raw] if kp_raw else [])

    media = [mm.group(1) for mm in re.finditer(r'<img[^>]*?src="([^"]+)"', art)]
    art_text = strip_tags(art)
    source_hash = "sha256:" + hashlib.sha256(art_text.encode("utf-8")).hexdigest()
    q = {
        "id": f"pol-{year}-{num:02d}", "subject": "politics", "year": year, "paper": "politics",
        "num": num, "type": qtype, "title": title, "stem": stem, "options": options,
        "answer": answer, "score": score,
        "source_blocks": [{k: b[k] for k in ("role", "class", "html", "text")} for b in blocks],
        "source_hash": source_hash, "knowledge_points": knowledge_points, "difficulty": None,
        "tags": tags, "media": media, "related_ids": [], "variants": [], "origin": "source",
        "content_hash": "", "schema_version": "1.0.0",
        "source_ref": {"file": "legacy/考研政治真题逐题精讲_修复版.html", "anchor": f"q-{year}-{num}", "year": year, "num": num},
    }
    q["content_hash"] = "sha256:" + hashlib.sha256(
        json.dumps(q, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    return q

sec_it = list(re.finditer(r'<section\b[^>]*class="[^"]*year-section[^"]*"[^>]*>', raw))
per_year, errors = {}, []
for si, sm in enumerate(sec_it):
    tag = sm.group(0)
    ym = re.search(r'data-year="(\d{4})"', tag) or re.search(r'y(\d{4})', tag)
    if not ym: continue
    year = int(ym.group(1))
    end = sec_it[si + 1].start() if si + 1 < len(sec_it) else len(raw)
    sec = raw[sm.end():end]
    qs = []
    for am in re.finditer(r'<article\b[^>]*class="[^"]*question[^"]*"[^>]*>', sec):
        astart = am.end()
        aend = sec.find("</article>", astart)
        art = sec[astart:aend if aend != -1 else len(sec)]
        nm = re.search(r'data-n="(\d+)"', am.group(0))
        num = int(nm.group(1)) if nm else 0
        if not num:
            t = re.search(r"第\s*(\d+)\s*题", strip_tags(art[:300]))
            num = int(t.group(1)) if t else len(qs) + 1
        try:
            qs.append(parse_article(year, num, art))
        except Exception as e:
            errors.append(f"{year} Q{num}: {type(e).__name__} {e}")
    per_year[year] = qs
    json.dump({"subject": "politics", "year": year, "question_count": len(qs), "questions": qs},
              open(os.path.join(OUTD, f"{year}.json"), "w", encoding="utf-8"), ensure_ascii=False)
    print(f"  {year}: {len(qs)} 题")

total = sum(len(v) for v in per_year.values())
missing = {y: sorted(set(range(1, 39)) - {q["num"] for q in qs}) for y, qs in per_year.items()}
missing = {y: m for y, m in missing.items() if m}
meta = {"expected_total": 456, "actual_total": total, "per_year": {y: len(q) for y, q in sorted(per_year.items())},
        "missing_nums": missing, "errors": errors, "ok": total == 456 and not missing}
json.dump(meta, open(os.path.join(METAD, "migration_politics.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"TOTAL: {total}/456 -> {'OK' if total == 456 else 'MISMATCH'}")
if missing: print("missing:", missing)
if errors: print("errors:", errors[:5])
