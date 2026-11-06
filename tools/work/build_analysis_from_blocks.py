# -*- coding: utf-8 -*-
"""由 data/{科目}/{年}.json 的 source_blocks 生成 {年}.analysis.json（九段式分步揭示）。

零编造：只把题库里**已经存在**的精讲原文区块换成 nodes，不改写、不新增任何文字；
每题写出 coveredRoles，前端据此把已纳入九段的区块从「原文/扩展」区移除，避免重复显示。

用法: python -I -X utf8 tools/work/build_analysis_from_blocks.py [--dry-run]
输出: data/{科目}/{年}.analysis.json
"""
import glob
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 每科参与九段揭示的 role（其余一律留在原文区，不搬动）
EXPLAIN_ROLES = {
    "politics": ["background", "frame", "approach", "analysis", "qa"],
    "english":  ["vocab", "grammar", "think", "detail", "warn"],
    "math":     ["kaodian", "silu", "jiefa", "biaozhun", "qita", "yicuo", "guina", "analysis"],
    "math2":    ["analysis", "approach", "warn"],
    "math3":    ["analysis"],
    "law498":   ["analysis", "analysis2", "note"],
}

# 无 label 的区块用标准九段名补标签（只是展示分组，不碰正文）
ROLE_LABEL = {
    "politics": {"background": "先补基础", "frame": "审题抓条件", "approach": "思路引导",
                 "analysis": "为什么不选其他", "qa": "举一反三"},
    "english":  {"vocab": "先补基础", "grammar": "先补基础", "think": "思路引导",
                 "detail": "完整推导", "warn": "易错深挖"},
    "math":     {"kaodian": "考点定位", "silu": "思路引导", "jiefa": "关键一步",
                 "biaozhun": "完整推导", "qita": "举一反三", "yicuo": "易错深挖",
                 "guina": "方法归纳", "analysis": "完整推导"},
    "math2":    {"analysis": "完整推导", "approach": "思路引导", "warn": "易错深挖"},
    "math3":    {"analysis": "完整推导"},
    "law498":   {"analysis": "完整推导", "analysis2": "完整推导", "note": "先补基础"},
}

# 原文 label 里少数不在前端 STEPS/ALIAS 表内的，规范成可识别的标签（只改标签）
LABEL_NORM = {
    "其他解法 · 举一反三": "其他解法",
    "易错点与陷阱": "易错提醒",
    "💡 考场思路": "思路引导",
}


def lines_of(block):
    txt = block.get("text")
    if not isinstance(txt, str) or not txt.strip():
        return []
    out = [l.strip() for l in txt.split("\n") if l.strip()]
    # 单段过长时按句号切成多行，便于分步阅读（不增删字符，仅在换行处切分）
    res = []
    for l in out:
        if len(l) <= 400:
            res.append(l)
        else:
            parts = re.split(r"(?<=[。；！？])", l)
            buf = ""
            for p in parts:
                if not p:
                    continue
                if len(buf) + len(p) > 400 and buf:
                    res.append(buf)
                    buf = p
                else:
                    buf += p
            if buf:
                res.append(buf)
    return res


def build_year(subj, path, dry=False):
    year = int(re.match(r"^(\d{4})\.json$", os.path.basename(path)).group(1))
    d = json.load(open(path, encoding="utf-8"))
    roles = EXPLAIN_ROLES[subj]
    items, covered_total, skipped = [], 0, 0
    for q in d.get("questions", []):
        nodes, covered = [], []
        for b in q.get("source_blocks", []):
            role = b.get("role")
            if role not in roles or role in covered:
                continue
            lines = lines_of(b)
            if not lines:
                continue
            label = b.get("label") or ROLE_LABEL[subj].get(role, "完整推导")
            label = LABEL_NORM.get(str(label).strip(), str(label).strip())
            nodes.append({"type": "text", "label": label, "lines": lines})
            covered.append(role)
        if not nodes:
            skipped += 1
            continue
        origins = {(b.get("origin") or "source") for b in q.get("source_blocks", [])
                   if b.get("role") in covered}
        kp = q.get("knowledge_points") or []
        desc = kp[0] if isinstance(kp, list) and kp and isinstance(kp[0], str) else ""
        src = q.get("source_ref") or {}
        items.append({
            "id": q.get("id"),
            "num": q.get("num"),
            "desc": desc,
            "origin": "source" if origins <= {"source"} else "extended",
            "coveredRoles": covered,
            "source": src.get("file") or src.get("pdf") or "",
            "nodes": nodes,
        })
        covered_total += len(covered)
    payload = {
        "subject": subj,
        "year": year,
        "count": len(items),
        "origin": "source",
        "generator": "tools/work/build_analysis_from_blocks.py（source_blocks 原文照录，零编造）",
        "analysis": items,
    }
    out = os.path.join(ROOT, "data", subj, "%d.analysis.json" % year)
    blob = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    if not dry:
        with open(out, "wb") as f:
            f.write(blob)
    return year, len(items), covered_total, skipped, len(blob), os.path.basename(out)


def main():
    dry = "--dry-run" in sys.argv
    total_files = total_items = total_blocks = total_bytes = 0
    oversized = []
    for subj in EXPLAIN_ROLES:
        files = sorted(glob.glob(os.path.join(ROOT, "data", subj, "[0-9][0-9][0-9][0-9].json")))
        sy = si = sb = sz = 0
        for f in files:
            year, items, blocks, skipped, size, name = build_year(subj, f, dry)
            sy += 1; si += items; sb += blocks; sz += size
            if size > 500 * 1024:
                oversized.append("%s/%s %dKB" % (subj, name, size // 1024))
            if skipped:
                print("  %s/%d 无精讲区块题数=%d" % (subj, year, skipped))
        print("%-10s 年份=%2d 生成题目=%4d 区块=%5d 体积=%5dKB" %
              (subj, sy, si, sb, sz // 1024))
        total_files += sy; total_items += si; total_blocks += sb; total_bytes += sz
    print("-" * 60)
    print("合计: %d 个 analysis.json / %d 题 / %d 个原文区块 / %dKB%s" %
          (total_files, total_items, total_blocks, total_bytes // 1024,
           "  [DRY-RUN 未写盘]" if dry else ""))
    if oversized:
        print("超过 500KB 门禁的文件:", oversized)
        sys.exit(1)


if __name__ == "__main__":
    main()
