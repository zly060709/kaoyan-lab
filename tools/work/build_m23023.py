# -*- coding: utf-8 -*-
"""装配 2023 数学二：题干(m23023_q) + 解析(m23023_a1..a9) -> data/math2/2023.json"""
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from m23023_q import ITEMS
from m23023_a1 import A as A1
from m23023_a2 import A as A2
from m23023_a3 import A as A3
from m23023_a4 import A as A4
from m23023_a5 import A as A5
from m23023_a6 import A as A6
from m23023_a7 import A as A7
from m23023_a8 import A as A8
from m23023_a9 import A as A9

ANA = {}
for src in (A1, A2, A3, A4, A5, A6, A7, A8, A9):
    ANA.update(src)

PDF = "2023数学二真题及解析.pdf"
SHA = "4e7dc8a080d2a6ac5c2b6623f4ee451f84f2edcf510d841d6a125142b71cccae"

# 派生元数据（知识点/难度/板块），不改原文内容
META = {
    1: (["斜渐近线方程", "极限计算"], 2, "gaoshu"),
    2: (["分段函数原函数", "不定积分与连续性"], 3, "gaoshu"),
    3: (["数列极限", "无穷小阶比较"], 4, "gaoshu"),
    4: (["二阶常系数线性微分方程", "解的有界性"], 3, "gaoshu"),
    5: (["参数方程求导", "导数定义与连续性"], 4, "gaoshu"),
    6: (["反常积分", "含参积分最值"], 4, "gaoshu"),
    7: (["极值点判定", "拐点与高阶导数"], 4, "gaoshu"),
    8: (["分块矩阵伴随矩阵", "逆矩阵"], 3, "xiandai"),
    9: (["二次型规范形", "惯性指数与配方法"], 2, "xiandai"),
    10: (["向量组线性表示", "生成子空间的交"], 3, "xiandai"),
    11: (["等价无穷小", "泰勒展开求参数"], 3, "gaoshu"),
    12: (["变限积分求导", "平面曲线弧长"], 3, "gaoshu"),
    13: (["隐函数求偏导", "二阶偏导数"], 3, "gaoshu"),
    14: (["隐函数求导", "法线斜率"], 2, "gaoshu"),
    15: (["定积分换元", "函数方程积分"], 3, "gaoshu"),
    16: (["含参线性方程组有解", "行列式计算"], 4, "xiandai"),
    17: (["一阶微分方程几何应用", "导数求最值"], 4, "gaoshu"),
    18: (["二元函数极值", "二阶充分条件"], 3, "gaoshu"),
    19: (["反常积分", "平面图形面积与旋转体体积"], 4, "gaoshu"),
    20: (["二重积分极坐标", "变量替换"], 4, "gaoshu"),
    21: (["泰勒公式", "中值定理证明"], 5, "gaoshu"),
    22: (["矩阵对角化", "特征值与特征向量"], 2, "xiandai"),
}
LABEL = {"gaoshu": "高等数学", "xiandai": "线性代数"}


def strip_dollar(s):
    s = s.strip()
    if s.startswith("$") and s.endswith("$") and s.count("$") == 2:
        s = s[1:-1]
    return s.replace("$", "")


questions = []
for it in ITEMS:
    num = it["num"]
    ans, lines = ANA[num]
    if ans is None:
        ans = "证明见解析"
    ans = strip_dollar(ans)
    kps, diff, cat = META[num]
    blocks = [{"role": "analysis", "origin": "source", "text": "\n\n".join(lines)}]
    q = {
        "id": f"math2-2023-{num}",
        "subject": "math2",
        "year": 2023,
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
        "tags": ["math2", LABEL[cat]],
        "media": [],
        "related_ids": [],
        "variants": [],
        "origin": "source",
        "source_hash": f"sha256pdf:{SHA}",
        "source_ref": {"pdf": PDF, "sha256": SHA, "pages": it["pages"], "anchor": it["anchor"]},
        "schema_version": "1.0.0",
        "content_hash": "",
    }
    core = {k: q[k] for k in ("id", "year", "num", "type", "stem", "options", "answer", "score")}
    core["blocks"] = [{"role": b["role"], "origin": b["origin"], "text": b["text"]} for b in blocks]
    q["content_hash"] = "sha256:" + hashlib.sha256(
        json.dumps(core, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    questions.append(q)

doc = {
    "subject": "math2",
    "year": 2023,
    "paper": "数学（二）",
    "schema_version": "1.0.0",
    "question_count": len(questions),
    "source_note": "视觉转录自《2023数学二真题及解析.pdf》（data/math2/pages/2023/，13 页）："
                   "p1–p4 试题、p5–p13 答案解析，题干/选项/答案/解析逐字照录。"
                   "2023 年结构：选择题 10×5 分、填空题 6×5 分、解答题 6 题共 70 分。",
    "questions": questions,
}
out = os.path.join(ROOT, "data", "math2", "2023.json")
json.dump(doc, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("写出", out, len(questions), "题", os.path.getsize(out) // 1024, "KB")
miss = [q["id"] for q in questions if not q["stem"] or not q["answer"]]
print("空题干/空答案:", miss or "无")
have = sorted(ANA)
print("解析覆盖:", have)
