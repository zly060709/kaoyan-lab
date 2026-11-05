# -*- coding: utf-8 -*-
"""math3 各年 JSON 的公式静态检查：$ 奇偶、花括号、\\begin/\\end 配对、疑似裸命令。
用法：python tools/work/check_m3years.py [2019 2018 ...]   （默认全部年份文件）
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIR = os.path.join(ROOT, "data", "math3")

def check(path):
    doc = json.load(io.open(path, encoding="utf-8"))
    errs = []
    for q in doc["questions"]:
        texts = [("stem", q["stem"]), ("answer", q["answer"])]
        texts += [("opt%d" % (i + 1), o) for i, o in enumerate(q.get("options") or [])]
        texts += [("block%d" % i, b["text"]) for i, b in enumerate(q.get("source_blocks") or [])]
        for name, t in texts:
            if not isinstance(t, str):
                continue
            if t.count("$") % 2:
                errs.append(f"{q['id']} {name}: $ 不配对（{t.count('$')} 个）| {t[:70]}")
            if t.count("{") != t.count("}"):
                errs.append(f"{q['id']} {name}: 花括号不配对 {t.count('{')}/{t.count('}')}")
            for env in set(re.findall(r"\\(?:begin|end)\{(\w+\*?)\}", t)):
                if t.count(f"\\begin{{{env}}}") != t.count(f"\\end{{{env}}}"):
                    errs.append(f"{q['id']} {name}: \\begin/{env} 不配对")
    return doc["question_count"], errs

if __name__ == "__main__":
    years = [int(a) for a in sys.argv[1:]] if len(sys.argv) > 1 else None
    total_err = 0
    for f in sorted(os.listdir(DIR)):
        if not (f.endswith(".json") and f[0].isdigit()):
            continue
        y = int(f.split(".")[0])
        if years and y not in years:
            continue
        n, errs = check(os.path.join(DIR, f))
        total_err += len(errs)
        print(f"{y}: {n} 题，静态检查 {'0 错误' if not errs else str(len(errs)) + ' 处'}")
        for e in errs[:6]:
            print("   ", e)
    print("合计错误", total_err)
    sys.exit(1 if total_err else 0)
