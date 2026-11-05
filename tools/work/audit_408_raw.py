# -*- coding: utf-8 -*-
"""一次性体检：legacy 408 RAW_DATA 的 qtype 分布、字段覆盖、stem/stem_nodes 缺口。"""
import collections
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
raw = open(os.path.join(ROOT, "legacy", "408_真题逐题精讲_修复版.html"),
           encoding="utf-8", errors="replace").read()
m = re.search(r"RAW_DATA\s*=\s*", raw)
i = m.end()
while raw[i] in " \t\r\n":
    i += 1

BACKSLASH = chr(92)
QUOTE = chr(34)


def jslice(s, start):
    depth = 0
    instr = False
    esc = False
    for j in range(start, len(s)):
        ch = s[j]
        if instr:
            if esc:
                esc = False
            elif ch == BACKSLASH:
                esc = True
            elif ch == QUOTE:
                instr = False
        else:
            if ch == QUOTE:
                instr = True
            elif ch in "[{":
                depth += 1
            elif ch in "]}":
                depth -= 1
                if depth == 0:
                    return s[start:j + 1]
    raise ValueError("unbalanced")


data = json.loads(jslice(raw, i))


def collect(entry):
    qs = list(entry.get("questions") or [])
    for p in (entry.get("parts") or []):
        if isinstance(p, dict) and isinstance(p.get("questions"), list):
            qs += p["questions"]
    return qs


qt = collections.Counter()
keys = collections.Counter()
total = 0
stem_empty_with_nodes = []
stem_missing_everywhere = []
for entry in data:
    year = entry.get("year")
    for q in collect(entry):
        total += 1
        qt[str(q.get("qtype"))] += 1
        for k in q.keys():
            keys[k] += 1
        st = (q.get("stem") or "").strip() if isinstance(q.get("stem"), str) else ""
        sn = q.get("stem_nodes") or []
        if not st and sn:
            stem_empty_with_nodes.append((year, q.get("num")))
        if not st and not sn:
            stem_missing_everywhere.append((year, q.get("num"), str(q.get("qtype"))))
print("total", total)
print("qtype", dict(qt))
print("keys", dict(keys))
print("stem empty but has stem_nodes:", len(stem_empty_with_nodes), stem_empty_with_nodes[:20])
print("stem empty and no stem_nodes:", len(stem_missing_everywhere), stem_missing_everywhere[:20])
