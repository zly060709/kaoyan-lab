# -*- coding: utf-8 -*-
"""装配 2022 数学二：题干(m22022_q) + 解析(m22022_a1..a6) -> data/math2/2022.json"""
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from m22022_q import ITEMS
from m22022_a1 import A as A1
from m22022_a2 import A as A2
from m22022_a3 import A as A3
from m22022_a4 import A as A4
from m22022_a5 import A as A5, A20_CONT
from m22022_a6 import A22_CONT

ANA = {}
for src in (A1, A2, A3, A4, A5):
    ANA.update(src)
ANA[20] = (ANA[20][0], ANA[20][1] + A20_CONT)
ANA[22] = (ANA[22][0], ANA[22][1] + A22_CONT)

PDF = "2022数学二真题及解析.pdf"
SHA = "513793a3053aeacecf6159e76414d6888a8e60b2b54e44ea60ddb7a69971847a"

# 派生元数据（知识点/难度/板块），不改原文内容
META = {
    1: (["无穷小比较", "等价无穷小定义"], 2, "gaoshu"),
    2: (["二重积分交换积分次序"], 3, "gaoshu"),
    3: (["导数局部保号性", "单调性与凹凸性判定"], 3, "gaoshu"),
    4: (["变限积分求导", "二元函数偏导数"], 3, "gaoshu"),
    5: (["反常积分敛散性判别"], 4, "gaoshu"),
    6: (["数列极限存在性", "复合函数单调性"], 4, "gaoshu"),
    7: (["定积分大小比较", "构造函数法"], 4, "gaoshu"),
    8: (["矩阵特征值", "相似与对角化"], 2, "xiandai"),
    9: (["线性方程组解的判定", "行列式计算"], 3, "xiandai"),
    10: (["向量组等价", "矩阵的秩"], 4, "xiandai"),
    11: (["幂指函数极限", "重要极限"], 3, "gaoshu"),
    12: (["隐函数求导"], 3, "gaoshu"),
    13: (["有理函数积分", "凑微分与反正切"], 3, "gaoshu"),
    14: (["高阶常系数线性微分方程", "特征方程"], 2, "gaoshu"),
    15: (["极坐标下曲线面积"], 3, "gaoshu"),
    16: (["初等变换与矩阵乘积", "逆矩阵与迹"], 4, "xiandai"),
    17: (["导数定义", "未定式极限"], 3, "gaoshu"),
    18: (["一阶线性微分方程", "平面曲线弧长"], 3, "gaoshu"),
    19: (["二重积分极坐标计算", "区域分块"], 4, "gaoshu"),
    20: (["多元复合函数求偏导", "二元函数极值"], 4, "gaoshu"),
    21: (["泰勒公式", "积分不等式证明"], 5, "gaoshu"),
    22: (["二次型正交变换", "特征值与瑞利商"], 3, "xiandai"),
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
        "id": f"math2-2022-{num}",
        "subject": "math2",
        "year": 2022,
        "num": num,
        "type": it["type"],
        "score": it["score"],
        "stem": it["stem"],
        "options": it["options"],
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
    "year": 2022,
    "paper": "数学（二）",
    "schema_version": "1.0.0",
    "question_count": len(questions),
    "source_note": "视觉转录自《2022数学二真题及解析.pdf》（data/math2/pages/2022/，11 页）："
                   "p1–p4 试题、p5–p11 答案解析，题干/选项/答案/解析逐字照录。"
                   "2022 年结构：选择题 10×5 分、填空题 6×5 分、解答题 6 题共 70 分。",
    "questions": questions,
}
out = os.path.join(ROOT, "data", "math2", "2022.json")
json.dump(doc, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("写出", out, len(questions), "题", os.path.getsize(out) // 1024, "KB")
miss = [q["id"] for q in questions if not q["stem"] or not q["answer"]]
print("空题干/空答案:", miss or "无")
