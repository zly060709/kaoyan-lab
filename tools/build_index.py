# -*- coding: utf-8 -*-
"""构建跨科搜索索引：data/index/{sid}.json（题干+选项+解析文本前段）。
用法: python -I -X utf8 tools/build_index.py
幂等：可重复运行；subjects.json 为科目清单来源。"""
import glob, json, os, re, sys, hashlib, datetime

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, "data", "meta", "subjects.json")
reg = json.load(open(REG, encoding="utf-8"))
SNIP = 600

def norm(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    return re.sub(r"\s+", " ", s).strip()

total = 0
for s in reg["subjects"]:
    sid, dd = s["id"], s.get("dataDir") or s["id"]
    files = sorted(glob.glob(os.path.join(ROOT, "data", dd, "[12]*.json")))
    files = [f for f in files if re.match(r"^\d{4}\.json$", os.path.basename(f))]
    if not files:
        continue
    entries = []
    for fp in files:
        try:
            d = json.load(open(fp, encoding="utf-8"))
        except Exception:
            continue
        year = d.get("year") or int(os.path.basename(fp)[:4])
        for q in d.get("questions", []):
            text_parts = [norm(q.get("stem"))]
            for o in (q.get("options") or [])[:6]:
                text_parts.append(norm(o if isinstance(o, str) else json.dumps(o, ensure_ascii=False)))
            for b in (q.get("source_blocks") or []):
                t = norm(b.get("text"))
                if t:
                    text_parts.append(t[:SNIP])
            text = " ".join(p for p in text_parts if p)[:1800]
            entries.append({
                "id": q.get("id"), "sid": sid, "year": year, "num": q.get("num"),
                "type": q.get("type"), "title": norm(q.get("title") or q.get("stem"))[:80],
                "tags": (q.get("tags") or [])[:4], "text": text,
            })
    if not entries:
        continue
    # 按年分片（合同：单文件 ≤500KB）；{sid}.manifest.json 记清单
    by_year = {}
    for e in entries:
        by_year.setdefault(e["year"], []).append(e)
    shards = {}
    for y, es in sorted(by_year.items()):
        fp = os.path.join(ROOT, "data", "index", sid, f"{y}.json")
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        json.dump({"sid": sid, "year": y, "count": len(es), "entries": es},
                  open(fp, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
        size = os.path.getsize(fp)
        flag = "" if size <= 500 * 1024 else " [>500KB!]"
        shards[str(y)] = {"count": len(es), "kb": size // 1024, "flag": flag}
        print(f"  {sid}/{y}.json: {len(es)} 条 {size//1024}KB{flag}")
        total += len(es)
    mf = {"sid": sid, "updated_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
          "count": len(entries), "shards": shards}
    json.dump(mf, open(os.path.join(ROOT, "data", "index", f"{sid}.manifest.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

print(f"index total: {total} 条")
