"""把政治客观题缺失的 answer 从 source_blocks[role=answer] 原文照录提升回 answer 字段。

只读原文、不生成任何新内容：区块文本形如 "B" / "ACD" 才提升，其他形态一律跳过并报告。
"""
import glob
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LETTERS = re.compile(r"^[A-E]{1,5}$")

changed, skipped, files = 0, [], []
for path in sorted(glob.glob(os.path.join(ROOT, "data", "politics", "*.json"))):
    if re.search(r"\.p\d+\.json$|\.analysis\.json$|\.media\.json$", os.path.basename(path)):
        continue
    data = json.load(open(path, encoding="utf-8"))
    touched = 0
    for q in data.get("questions", []):
        if q.get("answer") or q.get("type") not in ("single", "multi"):
            continue
        blocks = [b for b in q.get("source_blocks", [])
                  if isinstance(b, dict) and b.get("role") == "answer"]
        text = (blocks[0].get("text") or "").strip() if blocks else ""
        if not LETTERS.match(text):
            skipped.append("%s: %r" % (q.get("id"), text[:40]))
            continue
        q["answer"] = text
        touched += 1
    if touched:
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
        os.replace(tmp, path)
        changed += touched
        files.append("%s(+%d)" % (os.path.basename(path), touched))

print("提升 %d 题：%s" % (changed, ", ".join(files)))
print("跳过 %d 题（原文无单字母答案区块）：%s" % (len(skipped), "; ".join(skipped[:10])))
