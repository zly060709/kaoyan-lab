# -*- coding: utf-8 -*-
"""装配 2021 数学三：题干(m32021_q) + 解析(m32021_a1..a3) -> data/math3/2021.json"""
import hashlib
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from m32021_q import ITEMS
import m32021_a1, m32021_a2, m32021_a3

ANA = {}
for mod in (m32021_a1, m32021_a2, m32021_a3):
    ANA.update(mod.A)

REG = json.load(io.open(os.path.join(ROOT, "data", "meta", "source_pdfs.json"), encoding="utf-8"))
ENTRY = REG["math3:2021"]
PDF, SHA = ENTRY["pdf"], ENTRY["sha256"]

META = {
    1: (["变限积分求导", "无穷小阶的比较"], 3, "gaoshu"),
    2: (["分段函数的连续性", "导数定义与极值"], 3, "gaoshu"),
    3: (["函数零点个数", "单调性与最值"], 4, "gaoshu"),
    4: (["多元复合函数求导", "全微分"], 4, "gaoshu"),
    5: (["二次型", "惯性指数"], 3, "xiandai"),
    6: (["正交矩阵", "非齐次线性方程组的通解"], 4, "xiandai"),
    7: (["矩阵的三角分解", "初等变换"], 4, "xiandai"),
    8: (["条件概率", "事件独立性"], 4, "gailv"),
    9: (["估计量的期望与方差", "样本均值的协方差"], 3, "gailv"),
    10: (["最大似然估计"], 3, "gailv"),
    11: (["复合函数求导", "链式法则"], 3, "gaoshu"),
    12: (["含绝对值的定积分", "凑微分"], 3, "gaoshu"),
    13: (["旋转体体积", "定积分换元与对称性"], 3, "gaoshu"),
    14: (["一阶线性差分方程"], 3, "gaoshu"),
    15: (["行列式的定义", "行列式按行展开"], 4, "xiandai"),
    16: (["条件概率", "相关系数"], 4, "gailv"),
    17: (["单侧极限", "极限存在的充要条件"], 4, "gaoshu"),
    18: (["二元函数极值", "极值充分条件"], 4, "gaoshu"),
    19: (["二重积分极坐标", "交换积分次序"], 5, "gaoshu"),
    20: (["可分离变量微分方程", "幂级数求和函数"], 5, "gaoshu"),
    21: (["特征值与特征向量", "相似对角化"], 4, "xiandai"),
    22: (["均匀分布", "随机变量函数的分布", "期望"], 4, "gailv"),
}
LABEL = {"gaoshu": "高等数学", "xiandai": "线性代数", "gailv": "概率论"}


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
        "id": f"math3-2021-{num}",
        "subject": "math3",
        "year": 2021,
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
    "subject": "math3",
    "year": 2021,
    "paper": "数学（三）",
    "schema_version": "1.0.0",
    "question_count": len(questions),
    "source_note": f"视觉转录自《{PDF}》（data/math3/pages/2021/，{ENTRY['pages']} 页）："
                   "p1–p4 试题、p5–p12 答案解析；题干/选项/答案/解析逐字照录，"
                   "原卷中疑似排版问题的行（如第 17 题解析用拉丁字母 a 指代题干中的 $\\alpha$、"
                   "第 21 题 (3E−A) 行变换结果的第一行）一并不改。"
                   "第 5 题解析 $|\\lambda E-A|$ 第二个等号一步为原文照录。"
                   "2021 年数学三结构：选择题 10×5 分、填空题 6×5 分、解答题 6 题共 70 分"
                   "（原卷未逐题印分值，按 17 题 10 分、18–22 题各 12 分计）。",
    "questions": questions,
}
out = os.path.join(ROOT, "data", "math3", "2021.json")
json.dump(doc, io.open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("写出", out, len(questions), "题", os.path.getsize(out) // 1024, "KB")
miss = [q["id"] for q in questions if not q["stem"] or not q["answer"]]
print("空题干/空答案:", miss or "无")
print("分数合计:", sum(q["score"] for q in questions))
