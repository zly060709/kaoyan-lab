# -*- coding: utf-8 -*-
"""装配 2022 数学三：题干(m32022_q) + 解析(m32022_a1..a3) -> data/math3/2022.json"""
import hashlib
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from m32022_q import ITEMS
import m32022_a1, m32022_a2, m32022_a3

ANA = {}
for mod in (m32022_a1, m32022_a2, m32022_a3):
    ANA.update(mod.A)

REG = json.load(io.open(os.path.join(ROOT, "data", "meta", "source_pdfs.json"), encoding="utf-8"))
ENTRY = REG["math3:2022"]
PDF, SHA = ENTRY["pdf"], ENTRY["sha256"]

META = {
    1: (["等价无穷小", "无穷小阶的比较"], 3, "gaoshu"),
    2: (["数列极限", "最大值与最小值"], 4, "gaoshu"),
    3: (["变限积分求偏导", "二阶偏导数"], 4, "gaoshu"),
    4: (["定积分大小比较", "导数与单调性"], 4, "gaoshu"),
    5: (["相似对角化", "特征值的充要条件"], 3, "xiandai"),
    6: (["线性方程组解的判定", "系数矩阵与增广矩阵的秩"], 4, "xiandai"),
    7: (["向量组等价", "向量组的秩"], 4, "xiandai"),
    8: (["方差的线性性质", "二项分布与正态分布"], 3, "gailv"),
    9: (["辛钦大数定律", "连续型随机变量期望"], 3, "gailv"),
    10: (["二维离散型联合分布律", "事件独立性", "协方差"], 4, "gailv"),
    11: ([r"$1^{\infty}$ 型未定式极限", "洛必达法则"], 3, "gaoshu"),
    12: (["有理函数定积分", "反正切原函数"], 3, "gaoshu"),
    13: (["周期函数的奇偶性", "高阶导数"], 3, "gaoshu"),
    14: (["分段函数", "累次积分换序"], 4, "gaoshu"),
    15: (["初等矩阵与初等变换", "逆矩阵", "矩阵的迹"], 5, "xiandai"),
    16: (["条件概率", "事件的互不相容与独立"], 3, "gailv"),
    17: (["一阶线性微分方程", "曲线的渐近线"], 4, "gaoshu"),
    18: (["多元函数条件极值", "经济应用题"], 4, "gaoshu"),
    19: (["二重积分极坐标", "区域分块"], 5, "gaoshu"),
    20: (["幂级数收敛域", "和函数逐项求导"], 5, "gaoshu"),
    21: (["二次型标准型", "正交变换", "瑞利商最小值"], 4, "xiandai"),
    22: (["最大似然估计", "估计量的方差"], 4, "gailv"),
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
        "id": f"math3-2022-{num}",
        "subject": "math3",
        "year": 2022,
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
    "year": 2022,
    "paper": "数学（三）",
    "schema_version": "1.0.0",
    "question_count": len(questions),
    "source_note": f"视觉转录自《{PDF}》（data/math3/pages/2022/，{ENTRY['pages']} 页）："
                   "p1–p4 试题、p5 空白、p6–p15 答案解析；题干/选项/答案/解析逐字照录，"
                   "原卷中疑似排版错误的行（如第 14 题解析第二行、第 2 题 $(n=1,2,\\cdots,n)$）一并不改。"
                   "第 10 题联合分布律表格跨 p2/p3 分页，合并后照录。"
                   "2022 年数学三结构：选择题 10×5 分、填空题 6×5 分、解答题 6 题共 70 分（17 题 10 分，18–22 题各 12 分）。",
    "questions": questions,
}
out = os.path.join(ROOT, "data", "math3", "2022.json")
json.dump(doc, io.open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("写出", out, len(questions), "题", os.path.getsize(out) // 1024, "KB")
miss = [q["id"] for q in questions if not q["stem"] or not q["answer"]]
print("空题干/空答案:", miss or "无")
print("分数合计:", sum(q["score"] for q in questions))
