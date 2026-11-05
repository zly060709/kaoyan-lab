# -*- coding: utf-8 -*-
"""装配 2023 数学三：题干(m32023_q) + 解析(m32023_a1..a10) -> data/math3/2023.json"""
import hashlib
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from m32023_q import ITEMS
import m32023_a1, m32023_a2, m32023_a3, m32023_a4, m32023_a5
import m32023_a6, m32023_a7, m32023_a8, m32023_a9, m32023_a10

ANA = {}
for mod in (m32023_a1, m32023_a2, m32023_a3, m32023_a4, m32023_a5,
            m32023_a6, m32023_a7, m32023_a8, m32023_a9, m32023_a10):
    ANA.update(mod.A)

REG = json.load(io.open(os.path.join(ROOT, "data", "meta", "source_pdfs.json"), encoding="utf-8"))
ENTRY = REG["math3:2023"]
PDF, SHA = ENTRY["pdf"], ENTRY["sha256"]

META = {
    1: (["偏导数定义", "极限存在性"], 3, "gaoshu"),
    2: (["分段函数不定积分", "原函数连续性"], 3, "gaoshu"),
    3: (["二阶常系数线性微分方程", "解的有界性"], 4, "gaoshu"),
    4: (["级数绝对收敛", "正项级数比较"], 4, "gaoshu"),
    5: (["分块矩阵", "伴随矩阵"], 4, "xiandai"),
    6: (["二次型规范型", "特征值"], 3, "xiandai"),
    7: (["向量组的线性表示", "公共解"], 4, "xiandai"),
    8: (["泊松分布", "离散型随机变量期望"], 3, "gailv"),
    9: (["抽样分布", "F分布"], 3, "gailv"),
    10: (["正态总体", "无偏估计"], 4, "gailv"),
    11: (["未定式极限", "倒代换与洛必达法则"], 3, "gaoshu"),
    12: (["全微分反求函数", "偏积分"], 4, "gaoshu"),
    13: (["幂级数求和", "微分方程"], 4, "gaoshu"),
    14: (["变限积分方程", "一阶线性微分方程"], 4, "gaoshu"),
    15: (["行列式计算", "线性方程组有解判定"], 4, "xiandai"),
    16: (["二项分布", "相关系数"], 3, "gailv"),
    17: (["隐函数求导", "极值第二充分条件"], 3, "gaoshu"),
    18: (["反常积分", "平面图形面积", "旋转体体积"], 4, "gaoshu"),
    19: (["二重积分极坐标", "区域分块与对称性"], 4, "gaoshu"),
    20: (["泰勒公式", "中值定理证明"], 5, "gaoshu"),
    21: (["矩阵对角化", "特征值与特征向量"], 3, "xiandai"),
    22: (["分布函数", "随机变量函数的密度", "数学期望存在性"], 3, "gailv"),
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
        "id": f"math3-2023-{num}",
        "subject": "math3",
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
    "year": 2023,
    "paper": "数学（三）",
    "schema_version": "1.0.0",
    "question_count": len(questions),
    "source_note": f"视觉转录自《{PDF}》（data/math3/pages/2023/，{ENTRY['pages']} 页）："
                   "p1–p4 试题、p5–p13 答案解析，题干/选项/答案/解析逐字照录。"
                   "2023 年数学三结构：选择题 10×5 分、填空题 6×5 分、解答题 6 题共 70 分。"
                   "其中第 18 题与数学二 2023 第 19 题、第 21 题与数学二 2023 第 22 题同题。",
    "questions": questions,
}
out = os.path.join(ROOT, "data", "math3", "2023.json")
json.dump(doc, io.open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("写出", out, len(questions), "题", os.path.getsize(out) // 1024, "KB")
miss = [q["id"] for q in questions if not q["stem"] or not q["answer"]]
print("空题干/空答案:", miss or "无")
print("分数合计:", sum(q["score"] for q in questions))
