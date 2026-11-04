# -*- coding: utf-8 -*-
"""408 真题迁移：legacy 内嵌 RAW_DATA JSON -> data/cs408/{year}.json (+ {year}.analysis.json)
保真：RAW_DATA 字段全量保留；题干/选项/答案/desc/nodes 不改写。
用法: python -I -X utf8 tools/extract_408.py"""
import hashlib, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "legacy", "408_真题逐题精讲_修复版.html")
OUTD = os.path.join(ROOT, "data", "cs408")
METAD = os.path.join(ROOT, "data", "meta")
os.makedirs(OUTD, exist_ok=True); os.makedirs(METAD, exist_ok=True)
raw = open(SRC, encoding="utf-8", errors="replace").read()

m = re.search(r"RAW_DATA\s*=\s*", raw)
if not m:
    sys.exit("FATAL: RAW_DATA not found")
i = m.end()
while i < len(raw) and raw[i] in " \t\r\n":
    i += 1
if raw[i] != "[":
    sys.exit(f"FATAL: RAW_DATA does not start with '[' at {i}: {raw[i:i+40]!r}")

def json_slice(s, start):
    depth = 0; instr = False; esc = False
    for j in range(start, len(s)):
        ch = s[j]
        if instr:
            if esc: esc = False
            elif ch == "\\": esc = True
            elif ch == '"': instr = False
        else:
            if ch == '"': instr = True
            elif ch in "[{": depth += 1
            elif ch in "]}":
                depth -= 1
                if depth == 0:
                    return s[start:j + 1]
    raise ValueError("unbalanced JSON")

txt = json_slice(raw, i)
data = json.loads(txt)
print(f"RAW_DATA parsed: {len(data)} year entries")

def norm_text(v):
    if v is None: return ""
    if isinstance(v, (list, dict)): return json.dumps(v, ensure_ascii=False)
    return str(v)

def collect_questions(entry):
    qs = []
    if isinstance(entry.get("questions"), list):
        qs.extend(entry["questions"])
    for p in entry.get("parts", []) or []:
        if isinstance(p, dict):
            if isinstance(p.get("questions"), list):
                qs.extend(p["questions"])
    return qs

def qtype_map(qt):
    s = norm_text(qt)
    if "单" in s: return "single"
    if "多" in s: return "multi"
    return "big"

def img_list(*vals):
    out = []
    for v in vals:
        for mm in re.finditer(r'<img[^>]*?src="([^"]+)"', norm_text(v)):
            out.append(mm.group(1))
    return out

MEDIA_RE = re.compile(r"data:image/[a-zA-Z+]+;base64,[A-Za-z0-9+/=]+")
media_store = {}  # qid -> {idx: dataURI}

def pull_media(node, qid):
    """把 data URI 图片替换为占位符 @@M:qid:idx@@，原图存入 media_store（渲染时回填，原图可达）。"""
    counter = media_store.setdefault(qid, {})

    def walk(v):
        if isinstance(v, str):
            def rep(m):
                idx = len(counter)
                counter[str(idx)] = m.group(0)
                return f"@@M:{qid}:{idx}@@"
            return MEDIA_RE.sub(rep, v)
        if isinstance(v, list):
            return [walk(x) for x in v]
        if isinstance(v, dict):
            return {k: walk(x) for k, x in v.items()}
        return v

    return walk(node)

per_year = {}
all_ids = set()
for entry in data:
    year = entry.get("year")
    if year is None:
        sys.exit("FATAL: entry without year")
    year = int(year)
    qs_in = collect_questions(entry)
    base_qs, analysis = [], []
    for idx, q in enumerate(qs_in):
        num = q.get("num", idx + 1)
        try: num = int(num)
        except Exception: num = idx + 1
        qid = f"cs408-{year}-{num:02d}"
        if qid in all_ids:
            print(f"[warn] duplicate id {qid}")
        all_ids.add(qid)
        qt = q.get("qtype")
        tags = [norm_text(q.get("subject"))] if q.get("subject") else []
        if qt: tags.append(norm_text(qt))
        source_blocks = []
        if q.get("desc") is not None:
            source_blocks.append({"role": "desc", "html": "", "text": norm_text(q["desc"])})
        if q.get("nodes") is not None:
            source_blocks.append({"role": "nodes", "html": "", "text": json.dumps(q["nodes"], ensure_ascii=False)})
        src_hash = "sha256:" + hashlib.sha256(
            json.dumps(q, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
        base = {
            "id": qid, "subject": "cs408", "year": year, "num": num,
            "type": qtype_map(qt), "stem": norm_text(q.get("stem")),
            "options": q.get("options") if isinstance(q.get("options"), list) else [],
            "answer": q.get("answer"), "score": q.get("score"),
            "source_blocks": source_blocks, "source_hash": src_hash,
            "knowledge_points": [], "difficulty": None, "tags": tags,
            "media": img_list(q.get("stem"), q.get("desc"), q.get("nodes")),
            "related_ids": [], "variants": [], "origin": "source",
            "content_hash": "", "schema_version": "1.0.0",
            "source_ref": {"file": "legacy/408_真题逐题精讲_修复版.html", "anchor": f"RAW_DATA[{year}].q[{num}]", "year": year, "num": num},
        }
        base["content_hash"] = "sha256:" + hashlib.sha256(
            json.dumps(base, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
        base = pull_media(base, qid)
        base_qs.append(base)
        # 大块解析独立分片（合同单文件≤500KB）
        if q.get("nodes") is not None or q.get("desc") is not None:
            analysis.append({"id": qid, "num": num, "desc": q.get("desc"), "nodes": q.get("nodes")})
    year_obj = {
        "subject": "cs408", "year": year, "title": entry.get("title"),
        "intro": entry.get("intro"), "question_count": len(base_qs), "questions": base_qs,
    }
    fp = os.path.join(OUTD, f"{year}.json")
    json.dump(year_obj, open(fp, "w", encoding="utf-8"), ensure_ascii=False)
    json.dump({"subject": "cs408", "year": year, "items": {k: v for k, v in media_store.items() if k.startswith(f"cs408-{year}-")}},
              open(os.path.join(OUTD, f"{year}.media.json"), "w", encoding="utf-8"), ensure_ascii=False)
    if analysis:
        json.dump({"subject": "cs408", "year": year, "count": len(analysis), "analysis": analysis},
                  open(os.path.join(OUTD, f"{year}.analysis.json"), "w", encoding="utf-8"), ensure_ascii=False)
    per_year[year] = len(base_qs)
    size = os.path.getsize(fp)
    flag = "" if size <= 500 * 1024 else " [>500KB]"
    print(f"  {year}: {len(base_qs)} 题, base {size//1024}KB{flag}, analysis {len(analysis)}")

total = sum(per_year.values())
expected = 376
missing = {y: sorted(set(range(1, 48)) - {q["num"] for q in []}) for y in []}
meta = {"expected_total": expected, "actual_total": total, "per_year": per_year, "ok": total == expected}
json.dump(meta, open(os.path.join(METAD, "migration_cs408.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"TOTAL: {total}/{expected} -> {'OK' if total == expected else 'MISMATCH'}")
