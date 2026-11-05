# -*- coding: utf-8 -*-
"""2021 卷 LaTeX 静态检查：$ 奇偶、花括号、\\begin/\\end 配对"""
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
d = json.load(io.open(os.path.join(ROOT, "data", "math3", "2021.json"), encoding="utf-8"))

errs = []
for q in d["questions"]:
    texts = [("stem", q["stem"])] + [("opt%d" % (i + 1), o) for i, o in enumerate(q["options"])] \
        + [("answer", q["answer"])]
    for b in q["source_blocks"]:
        texts.append(("block", b["text"]))
    for name, t in texts:
        if t.count("$") % 2 != 0:
            errs.append(f"{q['id']} {name}: $ 奇偶 {t.count('$')}")
        for ch_open, ch_close, tag in (("{", "}", "brace"),):
            if t.count(ch_open) != t.count(ch_close):
                errs.append(f"{q['id']} {name}: {tag} 不配对 {t.count(ch_open)}/{t.count(ch_close)}")
        for env in re.findall(r"\\begin\{(\w+\*?)\}", t):
            if t.count(f"\\begin{{{env}}}") != t.count(f"\\end{{{env}}}"):
                errs.append(f"{q['id']} {name}: \\begin/{env} 不配对")

print("检查", d["question_count"], "题:", "0 错误" if not errs else f"{len(errs)} 处错误")
for e in errs[:20]:
    print("  -", e)
sys.exit(1 if errs else 0)
