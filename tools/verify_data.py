# -*- coding: utf-8 -*-
"""题量核对（合同第 7 章基准，缺一即不合格）+ 必填字段完整性抽查。
用法: python -I -X utf8 tools/verify_data.py"""
import glob, json, os, sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPECT = {"politics": 456, "math": 250, "english": 675, "cs408": 376}
REQ = ["id", "subject", "year", "num", "type", "stem", "source_blocks", "source_hash", "origin", "content_hash", "schema_version"]

ok = True
summary = {}
for subj, exp in EXPECT.items():
    files = sorted(glob.glob(os.path.join(ROOT, "data", subj, "*.json")))
    total = 0
    per = {}
    bad_fields = 0
    for fp in files:
        try:
            d = json.load(open(fp, encoding="utf-8"))
        except Exception as e:
            per[os.path.basename(fp)] = f"JSON-ERR:{e}"
            ok = False
            continue
        n = d.get("question_count")
        if not isinstance(n, int):
            n = len(d.get("questions", []))
        per[os.path.basename(fp)] = n
        total += n
        for q in d.get("questions", []):
            missing = [k for k in REQ if k not in q or q[k] in ("", None) and k != "options"]
            if missing:
                bad_fields += 1
    status = "PASS" if total == exp and bad_fields == 0 and files else "FAIL"
    if status == "FAIL":
        ok = False
    summary[subj] = {"total": total, "expected": exp, "files": len(files), "bad_field_questions": bad_fields}
    print(f"{subj}: {total}/{exp} [{status}] files={len(files)} bad={bad_fields}")
    print(f"  per-file: {per}")

print("=" * 40)
print("ALL PASS" if ok else "HAS FAIL — 不得进入下一阶段（合同第 7 章）")
sys.exit(0 if ok else 1)
