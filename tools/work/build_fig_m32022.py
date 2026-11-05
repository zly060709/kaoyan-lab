# -*- coding: utf-8 -*-
"""生成 2022 数学三 4 幅派生示意图（origin=derived，非原卷插图）"""
import io
import json
import math
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "data", "math3", "figures", "2022.json")

figs = []

# 第 2 题：数列 a_n = n^(1/n) - (-1)^n/n 的散点（最大值 a1=2、最小值 a2≈0.914）
pts = []
for n in range(1, 15):
    a = n ** (1.0 / n) - ((-1) ** n) / n
    pts.append({"kind": "point", "x": n, "y": round(a, 4),
                "label": ("a₁=2 最大值" if n == 1 else ("a₂≈0.914 最小值" if n == 2 else ""))})
figs.append({
    "qid": "math3-2022-2", "origin": "derived",
    "title": "第2题 数列 $a_n=\\sqrt[n]{n}-\\dfrac{(-1)^n}{n}$ 前 14 项（示意）",
    "xlim": [0, 15], "ylim": [0.8, 2.2],
    "items": pts + [
        {"kind": "hline", "y": 1, "style": "dashed", "label": "极限 1"},
        {"kind": "label", "x": 5.2, "y": 2.06, "text": "a₁=2 为最大值"},
        {"kind": "label", "x": 5.2, "y": 0.86, "text": "a₂≈0.914 为最小值"},
    ],
    "caption": "原卷解法：n^(1/n)→1 且有界，x<e 单增、x>e 单减，故只需比较前几项；n≥3 时 n^(1/n)−1/n>1，最小值只在 n=2 取到，最大值在 n=1 取到，选（A）。散点为按通项公式计算，非原卷插图。",
})

# 第 17 题：解曲线与斜渐近线
figs.append({
    "qid": "math3-2022-17", "origin": "derived",
    "title": "第17题 解曲线 $y=2x+\\mathrm{e}^{1-\\sqrt{x}}$ 与斜渐近线 $y=2x$",
    "xlim": [0, 8], "ylim": [0, 17],
    "items": [
        {"kind": "graph", "f": "2*x+exp(1-sqrt(x))", "domain": [0.01, 8], "color": "#1D4ED8",
         "label": "y=2x+e^(1−√x)"},
        {"kind": "graph", "f": "2*x", "domain": [0, 8], "color": "#B8324A", "label": "y=2x"},
        {"kind": "point", "x": 1, "y": 3, "label": "y(1)=3"},
        {"kind": "label", "x": 4.2, "y": 13.2, "text": "斜渐近线 y=2x（红）"},
    ],
    "caption": "原卷解法：一阶线性方程通解 y=2x+Ce^(−√x)，由 y(1)=3 得 C=e；垂直/水平渐近线均不存在，k=lim y/x=2、b=lim(y−2x)=0，故斜渐近线 y=2x。曲线由通解绘制，非原卷插图。",
})

# 第 19 题：积分区域 D = D1(1/4 圆) ∪ D2(第二象限三角形)
arc = [[round(2 * math.cos(t * math.pi / 2 / 24), 4),
        round(2 * math.sin(t * math.pi / 2 / 24), 4)] for t in range(25)]
figs.append({
    "qid": "math3-2022-19", "origin": "derived",
    "title": "第19题 区域 $D:\\ y-2\\leqslant x\\leqslant\\sqrt{4-y^2},\\ 0\\leqslant y\\leqslant2$",
    "xlim": [-2.6, 2.6], "ylim": [-0.4, 2.6],
    "items": [
        {"kind": "polygon", "pts": [[0, 0]] + arc + [[0, 0]], "color": "rgba(29,78,216,.28)"},
        {"kind": "polygon", "pts": [[0, 0], [0, 2], [-2, 0], [0, 0]], "color": "rgba(201,169,97,.45)"},
        {"kind": "parametric", "fx": "2*cos(t)", "fy": "2*sin(t)", "tmin": 0, "tmax": 1.5708,
         "color": "#1D4ED8", "label": "x²+y²=4"},
        {"kind": "graph", "f": "x+2", "domain": [-2, 0], "color": "#B8324A", "label": "x=y−2"},
        {"kind": "vline", "x": 0, "style": "dashed"},
        {"kind": "hline", "y": 0, "style": "dashed"},
        {"kind": "label", "x": 0.55, "y": 1.0, "text": "D₁: r≤2, 0≤θ≤π/2"},
        {"kind": "label", "x": -1.7, "y": 0.55, "text": "D₂: π/2≤θ≤π"},
    ],
    "caption": "原卷解法：极坐标下 D₁={0≤r≤2, 0≤θ≤π/2}、D₂={0≤r≤2/(sinθ−cosθ), π/2≤θ≤π}；I=2∫₀^{π/2}(1−2sinθcosθ)dθ+∫_{π/2}^{π}2dθ=2π−2。区域按原卷分区绘制，非原卷插图。",
})

# 第 20 题：和函数 S(x)
S = "atan(x)/x+(1/x)*ln((2+x)/(2-x))"
figs.append({
    "qid": "math3-2022-20", "origin": "derived",
    "title": "第20题 和函数 $S(x)$ 在收敛域 $[-1,1]$ 上（示意）",
    "xlim": [-1.1, 1.1], "ylim": [1.6, 2.15],
    "items": [
        {"kind": "graph", "f": S, "domain": [-1, -0.02], "color": "#1D4ED8"},
        {"kind": "graph", "f": S, "domain": [0.02, 1], "color": "#1D4ED8"},
        {"kind": "point", "x": 0, "y": 2, "label": "S(0)=2"},
        {"kind": "vline", "x": -1, "style": "dashed", "label": "x=−1"},
        {"kind": "vline", "x": 1, "style": "dashed", "label": "x=1"},
        {"kind": "label", "x": 0.3, "y": 2.09, "text": "S(x)=arctan x / x + (1/x)ln((2+x)/(2−x))"},
    ],
    "caption": "原卷解法：收敛域 [−1,1]；拆成 S₁(x)=arctan x/x（x≠0）与 S₂(x)=(1/x)ln((2+x)/(2−x))（x≠0），x=0 时各为 1，故 S(0)=2。曲线由和函数表达式绘制，非原卷插图。",
})

json.dump(figs, io.open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("写出", OUT, len(figs), "幅", os.path.getsize(OUT) // 1024, "KB")
