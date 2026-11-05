# -*- coding: utf-8 -*-
"""注册表真实化：用磁盘上的真实数据反推 dataYears / paperYears / counts 写回 subjects.json。

首页与科目页一律以本脚本产出的真实覆盖为准，避免「声称年份」与「实际数据」不一致。
用法: python -I -X utf8 tools/sync_registry.py
"""
import json
import os
import re
import sys
from datetime import datetime, timezone

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YEAR_RE = re.compile(r"^(\d{4})\.json$")
PAGE_KEY_RE = re.compile(r"^(.+):(\d{4})$")

# source_pdfs.json 的输出目录 id -> 科目 id
PAGES_DIR_TO_SUBJECT = {
    "math1.pages": "math1",
    "math2": "math2",
    "math3": "math3",
}


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def dump(path, obj):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(json.dumps(obj, ensure_ascii=False, indent=2))
    os.replace(tmp, path)


def subject_data(data_dir):
    """返回 {year: 题目数}，只统计真正含题目的年文件。"""
    base = os.path.join(ROOT, "data", data_dir)
    per_year = {}
    if not os.path.isdir(base):
        return per_year
    for fn in sorted(os.listdir(base)):
        m = YEAR_RE.match(fn)
        if not m:
            continue
        try:
            d = load(os.path.join(base, fn))
        except Exception:
            per_year[int(m.group(1))] = -1
            continue
        if isinstance(d, dict):
            qs = d.get("questions") or []
            per_year[int(m.group(1))] = len(qs)
        elif isinstance(d, list):
            per_year[int(m.group(1))] = len(d)
    return {y: n for y, n in per_year.items() if n and n > 0}


def paper_years():
    """返回 {subject_id: {year: 页数}}，来自逐页影像清单（真实存在才计）。"""
    out = {}
    src = os.path.join(ROOT, "data", "meta", "source_pdfs.json")
    if not os.path.exists(src):
        return out
    manifest = load(src)
    for key, info in manifest.items():
        m = PAGE_KEY_RE.match(key)
        if not m:
            continue
        sid = PAGES_DIR_TO_SUBJECT.get(m.group(1))
        if not sid:
            continue
        files = info.get("page_files") or []
        real = [f for f in files if os.path.exists(os.path.join(ROOT, f.replace("\\", "/")))]
        if not real:
            continue
        out.setdefault(sid, {})[int(m.group(2))] = len(real)
    return out


def main():
    spath = os.path.join(ROOT, "data", "meta", "subjects.json")
    reg = load(spath)
    papers = paper_years()
    coverage = {}
    for s in reg["subjects"]:
        data_dir = s.get("dataDir") or s["id"]
        per_year = subject_data(data_dir)
        py = papers.get(s["id"], {})
        s["dataYears"] = sorted(per_year.keys())
        s["yearCounts"] = {str(y): n for y, n in sorted(per_year.items())}
        s["paperYears"] = sorted(py.keys())
        s["paperPages"] = {str(y): n for y, n in sorted(py.items())}
        total = sum(per_year.values())
        s["questionTotal"] = total
        if total > 0:
            s["status"] = "active"
        elif py:
            s["status"] = "imaging"
        else:
            s["status"] = "pending"
        if s.get("years") and s["dataYears"]:
            s["years"] = [s["dataYears"][0], s["dataYears"][-1]]
        coverage[s["id"]] = {
            "status": s["status"],
            "dataYears": s["dataYears"],
            "questions": total,
            "paperYears": s["paperYears"],
        }
    reg["updated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    reg["note"] = ("20 科全国统考/联考框架。status: active=已上线 | imaging=仅有原卷影像（题目转录中） | "
                   "pending=待用户提供资料（合同禁止编造真题）。dataDir 为数据目录别名。"
                   "dataYears/paperYears/questionTotal 由 tools/sync_registry.py 依真实数据反推。")
    dump(spath, reg)
    dump(os.path.join(ROOT, "data", "meta", "coverage.json"), coverage)
    for sid, c in coverage.items():
        print("%-10s %-9s %5d 题  数据年 %s  影像年 %s" % (
            sid, c["status"], c["questions"],
            fmt_years(c["dataYears"]), fmt_years(c["paperYears"])))


def fmt_years(ys):
    if not ys:
        return "—"
    return "%d–%d(%d)" % (ys[0], ys[-1], len(ys)) if len(ys) > 1 else str(ys[0])


if __name__ == "__main__":
    main()
