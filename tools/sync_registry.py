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
    "law498": "law498",
}

# 客观题题型白名单，用于反推 objectiveTotal（首页「其中客观题 N」此前是硬编码 675）。
# 必须与 tools/gates.py G1 的英语白名单保持一致，否则首页数字与门禁基准会各说各话。
OBJECTIVE_TYPES = {
    "english": {"cloze", "reading", "partb", "single", "multi"},
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


def objective_total(data_dir, types):
    """按题型白名单反推客观题总数；科目没有白名单则返回 None（不猜）。"""
    if not types:
        return None
    base = os.path.join(ROOT, "data", data_dir)
    if not os.path.isdir(base):
        return 0
    n = 0
    for fn in sorted(os.listdir(base)):
        if not YEAR_RE.match(fn):
            continue
        try:
            d = load(os.path.join(base, fn))
        except Exception:
            continue
        qs = d.get("questions") if isinstance(d, dict) else d
        for q in qs or []:
            if isinstance(q, dict) and q.get("type") in types:
                n += 1
    return n


def paper_years():
    """返回 {subject_id: {year: 页数}}，来自逐页影像清单 `data/meta/source_pdfs.json`。

    页数取清单里声明的 `page_files`，**不再要求文件在本机存在**。原因：本仓的工作副本可能是
    稀疏物化（影像只在远端 main 上），按本地存在性过滤会把「远端确实有」的年份静默判成无，
    注册表随之删掉数一 2009–2012 与数二 2009–2023 的影像年份——线上科目页的原卷入口消失，
    而科目页与 QUALITY_REPORT 的文字仍在承诺它们（收敛⑪ 起踩到，收敛⑭ 修正）。
    「声明的文件是否真的在仓库里」这条真值检查交给 CI（全量检出）：`tools/verify_pages.py`。
    """
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
        n = len(files) or int(info.get("pages") or 0)
        if n <= 0:
            continue
        out.setdefault(sid, {})[int(m.group(2))] = n
    return out


def analysis_years(data_dir):
    """列出真正有精讲文件的年份（{年}.analysis.json 或 {年}.analysis.p1.json 且 analysis 非空）。"""
    base = os.path.join(ROOT, "data", data_dir)
    out = []
    if not os.path.isdir(base):
        return out
    for fn in sorted(os.listdir(base)):
        m = re.match(r"^(\d{4})\.analysis(\.p\d+)?\.json$", fn)
        if not m:
            continue
        y = int(m.group(1))
        if y in out:
            continue
        try:
            d = load(os.path.join(base, fn))
        except Exception:
            continue
        if isinstance(d, dict) and (d.get("analysis") or []):
            out.append(y)
    return sorted(out)


def figure_years(data_dir):
    """列出真正有 DSL 图形文件的年份（data/{科}/figures/{年}.json 且是非空数组）。

    与 analysisYears 同因：前端无条件请求会在缺图年份的每个题页留下 404，
    被 try/catch 吞掉但浏览器 console 仍报错，合同「console 报错 = 0」成假通过。
    """
    base = os.path.join(ROOT, "data", data_dir, "figures")
    out = []
    if not os.path.isdir(base):
        return out
    for fn in sorted(os.listdir(base)):
        m = re.match(r"^(\d{4})\.json$", fn)
        if not m:
            continue
        try:
            d = load(os.path.join(base, fn))
        except Exception:
            continue
        if isinstance(d, list) and d:
            out.append(int(m.group(1)))
    return sorted(out)


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
        s["analysisYears"] = analysis_years(data_dir)
        s["figureYears"] = figure_years(data_dir)
        total = sum(per_year.values())
        s["questionTotal"] = total
        obj = objective_total(data_dir, OBJECTIVE_TYPES.get(s["id"]))
        if obj is None:
            s.pop("objectiveTotal", None)
        else:
            s["objectiveTotal"] = obj
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
                   "dataYears/paperYears/questionTotal/objectiveTotal 由 tools/sync_registry.py 依真实数据反推；"
                   "paperYears 取影像清单声明的页数（本机缺文件不代表仓库缺，真值由 CI 的 verify_pages.py 校）。")
    dump(spath, reg)
    dump(os.path.join(ROOT, "data", "meta", "coverage.json"), coverage)
    for sid, c in coverage.items():
        print("%-10s %-9s %5d 题  数据年 %s  影像年 %s" % (
            sid, c["status"], c["questions"],
            fmt_years(c["dataYears"]), fmt_years(c["paperYears"])))
    for s in reg["subjects"]:
        if s.get("objectiveTotal") is not None:
            print("%-10s 客观题 %d / 全量 %d（按 %s 题型白名单）" % (
                s["id"], s["objectiveTotal"], s.get("questionTotal", 0),
                ",".join(sorted(OBJECTIVE_TYPES.get(s["id"], ())))))


def fmt_years(ys):
    if not ys:
        return "—"
    return "%d–%d(%d)" % (ys[0], ys[-1], len(ys)) if len(ys) > 1 else str(ys[0])


if __name__ == "__main__":
    main()
