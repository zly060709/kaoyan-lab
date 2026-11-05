# -*- coding: utf-8 -*-
"""装配 2009–2020 数学三：题干(m3YYYY_q) + 解析(m3YYYY_a1..a3) + 知识点(m3YYYY_meta)
-> data/math3/YYYY.json。与 build_m32021.py 同口径，只是把年份做成参数。

用法：python tools/work/build_m3legacy.py 2019 [2018 ...]
"""
import hashlib
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# 逐题分值来源：print=卷面印有「（本题满分 X 分）」；derive=卷面只印总分 94，按惯例折算
SCORE_ORIGIN = {
    2009: "print", 2010: "print", 2011: "print", 2012: "print",
    2013: "print", 2014: "derive", 2015: "print", 2016: "print",
    2017: "print", 2018: "print", 2019: "derive", 2020: "print",
}
LABEL = {"gaoshu": "高等数学", "xiandai": "线性代数", "gailv": "概率论"}
REG = json.load(io.open(os.path.join(ROOT, "data", "meta", "source_pdfs.json"), encoding="utf-8"))


def strip_dollar(s):
    s = s.strip()
    if s.startswith("$") and s.endswith("$") and s.count("$") == 2:
        s = s[1:-1]
    return s.replace("$", "")


def build(year):
    qmod = __import__(f"m3{year}_q")
    mods = [f"m3{year}_a{i}" for i in (1, 2, 3)]
    ana = {}
    for name in mods:
        p = os.path.join(HERE, name + ".py")
        if os.path.exists(p):
            ana.update(__import__(name).A)
    meta = {}
    if os.path.exists(os.path.join(HERE, f"m3{year}_meta.py")):
        meta = __import__(f"m3{year}_meta").META

    missing_ana = [i["num"] for i in qmod.ITEMS if i["num"] not in ana]
    missing_meta = [i["num"] for i in qmod.ITEMS if i["num"] not in meta]
    if missing_ana or missing_meta:
        print(f"{year} 跳过：缺解析 {missing_ana} 缺知识点 {missing_meta}")
        return None

    entry = REG[f"math3:{year}"]
    pdf, sha, npages = entry["pdf"], entry["sha256"], entry["pages"]
    notes = os.path.join(HERE, f"m3{year}_notes.md")
    n_lines = 0
    if os.path.exists(notes):
        txt = io.open(notes, encoding="utf-8").read()
        n_lines = len(re.findall(r"^\s*\d+\.\s", txt, re.M))

    score_note = (
        "解答题逐题分值照卷面题号后的「（本题满分 X 分）」印刷。"
        if SCORE_ORIGIN[year] == "print"
        else "解答题逐题分值：卷面只印「三、解答题：15～23 小题，共 94 分」，未印逐题分值，"
             "按 15–19 题各 10 分、20–23 题各 11 分折算（50+44=94），系推定值而非卷面原文。"
    )

    media_note = ""
    mpath = os.path.join(ROOT, "data", "math3", f"{year}.media.json")
    if os.path.exists(mpath):
        mdoc = json.load(io.open(mpath, encoding="utf-8"))
        nm = sum(len(v) for v in (mdoc.get("items") or {}).values())
        media_note = (f"本卷另有 {nm} 幅原卷图形，为页面影像直接裁图（data/math3/{year}.media.json），未重绘、未派生。")

    questions = []
    for it in qmod.ITEMS:
        num = it["num"]
        ans, lines = ana[num]
        ans = "证明见解析" if ans is None else strip_dollar(ans)
        kps, diff, cat = meta[num]
        blocks = [{"role": "analysis", "origin": "source", "text": "\n\n".join(lines)}]
        q = {
            "id": f"math3-{year}-{num}",
            "subject": "math3",
            "year": year,
            "num": num,
            "type": it["type"],
            "score": it["score"],
            "stem": it["stem"],
            "options": it.get("options", []),
            "answer": ans,
            "source_blocks": blocks,
            "knowledge_points": kps,
            "difficulty": diff,
            "category": {"key": cat, "label": LABEL[cat]},
            "tags": ["math3", LABEL[cat]],
            "media": [],
            "related_ids": [],
            "variants": [],
            "origin": "source",
            "source_hash": f"sha256pdf:{sha}",
            "source_ref": {"pdf": pdf, "sha256": sha, "pages": it["pages"], "anchor": it["anchor"]},
            "schema_version": "1.0.0",
            "content_hash": "",
        }
        core = {k: q[k] for k in ("id", "year", "num", "type", "stem", "options", "answer", "score")}
        core["blocks"] = [{"role": b["role"], "origin": b["origin"], "text": b["text"]} for b in blocks]
        q["content_hash"] = "sha256:" + hashlib.sha256(
            json.dumps(core, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
        questions.append(q)

    assert sum(q["score"] for q in questions) == 150, f"{year} 分数合计 != 150"
    doc = {
        "subject": "math3",
        "year": year,
        "paper": "数学（三）",
        "schema_version": "1.0.0",
        "question_count": len(questions),
        "source_note": (
            f"视觉转录自《{pdf}》（data/math3/pages/{year}/，{npages} 页）。"
            "2009–2020 年数学三结构：选择题 8×4=32 分、填空题 6×4=24 分、解答题 15–23 共 94 分，合计 150 分。"
            + score_note +
            "题干/选项/答案/解析逐字照录，原卷的疑似排版或笔误（错字、漏字、半全角混用、"
            "上下标排版不一致）一律不改，逐条登记在 tools/work/" + f"m3{year}_notes.md" +
            (f"（{n_lines} 条编号记录）。" if os.path.exists(notes) else "（本卷尚无复核记录，待补）。")
            + media_note
        ),
        "questions": questions,
    }
    out = os.path.join(ROOT, "data", "math3", f"{year}.json")
    json.dump(doc, io.open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    miss = [q["id"] for q in questions if not q["stem"] or not q["answer"]]
    print(f"写出 {out} {len(questions)} 题 {os.path.getsize(out) // 1024}KB "
          f"分数合计 {sum(q['score'] for q in questions)} 空题干/空答案 {miss or '无'}")
    return doc


if __name__ == "__main__":
    for y in [int(a) for a in sys.argv[1:]] or list(range(2009, 2021)):
        build(y)
