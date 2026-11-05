# -*- coding: utf-8 -*-
"""汇总交付报告所需事实：各科题量、影像卷数、图形数、精讲条数、搜索索引规模。"""
import glob
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLASH = "/"


def load(abs_path):
    return json.load(open(abs_path, encoding="utf-8"))


def norm(p):
    return p.replace(chr(92), SLASH)


print("== 题量 / 精讲 / 图形 / 影像 ==")
grand = 0
for d in sorted(glob.glob(os.path.join(ROOT, "data", "*"))):
    if not os.path.isdir(d):
        continue
    name = norm(d).split(SLASH)[-1]
    if name in ("meta", "index"):
        continue
    years, qs = [], 0
    for p in sorted(glob.glob(os.path.join(d, "*.json"))):
        if re.match(r"^\d{4}\.json$", os.path.basename(p)):
            years.append(os.path.basename(p)[:4])
            qs += len(load(p).get("questions") or [])
    ana = 0
    for p in glob.glob(os.path.join(d, "*.analysis.json")):
        if re.search(r"\.p\d+\.json$", os.path.basename(p)):
            continue
        ana += len(load(p).get("analysis") or [])
        for pp in glob.glob(os.path.join(os.path.dirname(p), os.path.basename(p).replace(".json", ".p*.json"))):
            ana += len(load(pp).get("analysis") or [])
    figs = len(glob.glob(os.path.join(d, "figures", "*.json")))
    pages = len(glob.glob(os.path.join(d, "pages", "*", "*.png")))
    grand += qs
    print("%-14s 题=%-5d 年=%s 精讲=%-5d 图形文件=%-3d 影像页=%d" % (
        name, qs, ",".join(years) or "-", ana, figs, pages))
print("总题量", grand)

print("== 搜索索引 ==")
for p in sorted(glob.glob(os.path.join(ROOT, "data", "index", "*.json"))):
    print("  ", os.path.basename(p), os.path.getsize(p) // 1024, "KB")

print("== 注册表 ==")
reg = load(os.path.join(ROOT, "data", "meta", "subjects.json"))
for s in reg.get("subjects", []):
    print("  %-12s %-9s data=%s paper=%s total=%s" % (
        s.get("id"), s.get("status"), s.get("dataYears"),
        s.get("paperYears"), s.get("questionTotal")))
