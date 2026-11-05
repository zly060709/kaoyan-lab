# -*- coding: utf-8 -*-
"""参数化数学卷装配器：按 math_batch_config.json 批量生成 data/<subj>/<year>.json

用法: python -I -X utf8 tools/work/build_math_batch.py math3:2020 math3:2019 ...
配置 tools/work/math_batch_config.json:
{
  "math3:2020": {"prefix": "m32020", "source_key": "math3:2020",
                 "paper": "数学（三）", "note": "……source_note 全文……"}
}
模块约定（仓库 tools/work/）：{prefix}_q.py(ITEMS) / {prefix}_a1..a3.py(A) / {prefix}_meta.py(META)
META[num] = ([知识点...], 难度1-5, 板块key)，板块 label 在 LABELS。
"""
import hashlib
import importlib
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

CONFIG = json.load(io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                        "math_batch_config.json"), encoding="utf-8"))
LABELS = {"gaoshu": "高等数学", "xiandai": "线性代数", "gailv": "概率论"}


def strip_dollar(s):
    s = s.strip()
    if s.startswith("$") and s.endswith("$") and s.count("$") == 2:
        s = s[1:-1]
    return s.replace("$", "")


def build_one(key):
    cfg = CONFIG[key]
    subj, year = key.split(":")
    year = int(year)
    pfx = cfg["prefix"]
    q = importlib.import_module(f"{pfx}_q")
    a1 = importlib.import_module(f"{pfx}_a1")
    a2 = importlib.import_module(f"{pfx}_a2")
    a3 = importlib.import_module(f"{pfx}_a3")
    meta = importlib.import_module(f"{pfx}_meta")
    ANA = {}
    for m in (a1, a2, a3):
        ANA.update(m.A)
    META = meta.META

    reg = json.load(io.open(os.path.join(ROOT, "data", "meta", "source_pdfs.json"), encoding="utf-8"))
    entry = reg[cfg.get("source_key", key)]
    pdf, sha = entry["pdf"], entry["sha256"]
    subj_out = cfg.get("out_subject", subj)  # math1 的存量数据目录/subject 均为 "math"
    out_dir = cfg.get("out_dir", subj)

    questions = []
    for it in q.ITEMS:
        num = it["num"]
        ans, lines = ANA[num]
        if ans is None:
            ans = "证明见解析"
        ans = strip_dollar(ans)
        kps, diff, cat = META[num]
        blocks = [{"role": "analysis", "origin": "source", "text": "\n\n".join(lines)}]
        qd = {
            "id": f"{subj_out}-{year}-{num}",
            "subject": subj_out,
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
            "category": {"key": cat, "label": LABELS[cat]},
            "tags": [subj_out, LABELS[cat]],
            "media": [],
            "related_ids": [],
            "variants": [],
            "origin": "source",
            "source_hash": f"sha256pdf:{sha}",
            "source_ref": {"pdf": pdf, "sha256": sha, "pages": it["pages"], "anchor": it["anchor"]},
            "schema_version": "1.0.0",
            "content_hash": "",
        }
        core = {k: qd[k] for k in ("id", "year", "num", "type", "stem", "options", "answer", "score")}
        core["blocks"] = [{"role": b["role"], "origin": b["origin"], "text": b["text"]} for b in blocks]
        qd["content_hash"] = "sha256:" + hashlib.sha256(
            json.dumps(core, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
        questions.append(qd)

    doc = {
        "subject": subj,
        "year": year,
        "paper": cfg.get("paper", "数学"),
        "schema_version": "1.0.0",
        "question_count": len(questions),
        "source_note": cfg["note"],
        "questions": questions,
    }
    out = os.path.join(ROOT, "data", out_dir, f"{year}.json")
    json.dump(doc, io.open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    miss = [qd["id"] for qd in questions if not qd["stem"] or (not qd["answer"] and qd["type"] == "single")]
    print("写出", os.path.relpath(out, ROOT), len(questions), "题",
          os.path.getsize(out) // 1024, "KB | 分数", sum(qd["score"] for qd in questions),
          "| 空题干/客观空答案:", miss or "无")


for key in sys.argv[1:]:
    build_one(key)
