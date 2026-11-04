# -*- coding: utf-8 -*-
"""导出数学科目各年题目紧凑摘要（供逐题图形化转录工作台）。
用法: python -I -X utf8 tools/dump_math_summary.py math 2013 2023
输出: tools/work/math-{dir}-{y1}-{y2}.txt（每题: 题号|类型|分值|考点|题干前180字）"""
import glob, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
subj = sys.argv[1] if len(sys.argv) > 1 else "math"
y1 = int(sys.argv[2]) if len(sys.argv) > 2 else 0
y2 = int(sys.argv[3]) if len(sys.argv) > 3 else 9999

os.makedirs(os.path.join(ROOT, "tools", "work"), exist_ok=True)
outp = os.path.join(ROOT, "tools", "work", f"math-{subj}-{y1}-{y2}.txt")
lines = []
for fp in sorted(glob.glob(os.path.join(ROOT, "data", subj, "*.json"))):
    if not re.match(r"^\d{4}\.json$", os.path.basename(fp)):
        continue
    year = int(os.path.basename(fp)[:4])
    if not (y1 <= year <= y2):
        continue
    d = json.load(open(fp, encoding="utf-8"))
    lines.append(f"########## {year} ({d.get('paper','')} {d.get('question_count','?')}题) ##########")
    for q in d.get("questions", []):
        stem = re.sub(r"\s+", " ", q.get("stem") or "")[:180]
        kp = ""
        for b in q.get("source_blocks", []):
            if b.get("role") in ("kaodian", "analysis"):
                kp = re.sub(r"\s+", " ", b.get("text") or "")[:70]
                break
        opts = " ".join(re.sub(r"\s+", " ", o)[:40] for o in (q.get("options") or [])[:4] if isinstance(o, str))
        ans = q.get("answer")
        lines.append(f"[{q['num']:>2}|{q.get('type','?'):>6}|{q.get('score') or '-':>3}|答:{ans}] {stem}")
        if opts:
            lines.append(f"      选项: {opts[:200]}")
        if kp:
            lines.append(f"      考点: {kp}")
open(outp, "w", encoding="utf-8").write("\n".join(lines))
print(f"written: {outp} ({len(lines)} lines, {os.path.getsize(outp)//1024}KB)")
