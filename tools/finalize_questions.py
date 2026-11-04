# -*- coding: utf-8 -*-
"""为题目 JSON 补齐 content_hash（幂等：已有则跳过）+ 校验结构。
用法: python -I -X utf8 tools/finalize_questions.py math2 2009"""
import hashlib, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
subj, year = sys.argv[1], sys.argv[2]
fp = os.path.join(ROOT, "data", subj, f"{year}.json")
d = json.load(open(fp, encoding="utf-8"))

def chash(q):
    core = {k: q.get(k) for k in ("id", "year", "num", "type", "stem", "options", "answer", "score") if k in q}
    for b in q.get("source_blocks", []):
        core.setdefault("blocks", []).append({"role": b.get("role"), "origin": b.get("origin"), "text": b.get("text")})
    return "sha256:" + hashlib.sha256(json.dumps(core, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()

REQ = ["id", "subject", "year", "num", "type", "stem", "answer", "source_blocks", "source_hash", "origin", "content_hash", "schema_version"]
errs, filled = [], 0
for q in d.get("questions", []):
    if not q.get("content_hash"):
        q["content_hash"] = chash(q)
        filled += 1
    miss = [k for k in REQ if k not in q]
    if miss:
        errs.append(f"{q.get('id')}: 缺 {miss}")
json.dump(d, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{subj}/{year}: {len(d['questions'])} 题, content_hash 补 {filled}, 错误 {len(errs)}")
for e in errs[:5]:
    print(" -", e)
sys.exit(1 if errs else 0)
