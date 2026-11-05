# -*- coding: utf-8 -*-
"""生成 2021 数学三 3 幅派生示意图（origin=derived，非原卷插图）"""
import io
import json
import math
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "data", "math3", "figures", "2021.json")

figs = []

# 第 13 题：D 的边界曲线 y = √x·sin(πx)（旋转体母线）
figs.append({
    "qid": "math3-2021-13", "origin": "derived",
    "title": "第13题 曲线 $y=\\\\sqrt{x}\\\\sin\\\\pi x\\\\ (0\\\\leqslant x\\\\leqslant1)$（旋转体母线，示意）",
    "xlim": [0, 1.05], "ylim": [-1.1, 1.1],
    "items": [
        {"kind": "graph", "f": "sqrt(x)*sin(pi*x)", "domain": [0, 1], "color": "#1D4ED8",
         "label": "y=√x·sinπx"},
        {"kind": "hline", "y": 0, "style": "dashed"},
        {"kind": "point", "x": 0.5, "y": 0.7071, "label": "y(1/2)≈0.707"},
        {"kind": "label", "x": 0.52, "y": 0.93, "text": "V=π∫₀¹ x·sin²πx dx = π/4"},
    ],
    "caption": "原卷解法：V=π∫₀¹ y²dx=π∫₀¹ x·sin²πx dx，换元 x=t/π 后用对称性 (1/π)·(π/2)∫₀^π sin²t dt=π/4。曲线按题设函数绘制，非原卷插图。",
})

# 第 19 题：积分区域 D（单位圆内 0≤θ≤π/4 的扇形）
arc = [[round(math.cos(t * math.pi / 4 / 24), 4),
        round(math.sin(t * math.pi / 4 / 24), 4)] for t in range(25)]
figs.append({
    "qid": "math3-2021-19", "origin": "derived",
    "title": "第19题 区域 $D$：$x^{2}+y^{2}\\\\leqslant1$，$0\\\\leqslant y\\\\leqslant x$（第一象限扇形）",
    "xlim": [-0.12, 1.12], "ylim": [-0.12, 0.88],
    "items": [
        {"kind": "polygon", "pts": [[0, 0]] + arc + [[0, 0]], "color": "rgba(29,78,216,.28)"},
        {"kind": "parametric", "fx": "cos(t)", "fy": "sin(t)", "tmin": 0, "tmax": 0.7854,
         "color": "#1D4ED8", "label": "x²+y²=1"},
        {"kind": "graph", "f": "x", "domain": [0, 0.72], "color": "#B8324A", "label": "y=x"},
        {"kind": "hline", "y": 0, "style": "dashed"},
        {"kind": "label", "x": 0.38, "y": 0.18, "text": "D: 0≤r≤1, 0≤θ≤π/4"},
    ],
    "caption": "原卷解法：极坐标 x²−y²=r²cos2θ、(x+y)²=r²(1+sin2θ)，D={0≤r≤1, 0≤θ≤π/4}；先对 θ 积分 ∫e^{r²(1+sin2θ)}r³cos2θdθ=(r/2)(e^{2r²}−e^{r²})，再对 r 积分得 (e−1)²/8。区域按题设绘制，非原卷插图。",
})

# 第 20 题：和函数 S(x)=x+(1-x)ln(1-x)，S(1)=1
S = "x+(1-x)*ln(1-x)"
figs.append({
    "qid": "math3-2021-20", "origin": "derived",
    "title": "第20题 和函数 $S(x)=x+(1-x)\\\\ln(1-x)$ 在收敛域 $[-1,1]$ 上（示意）",
    "xlim": [-1.1, 1.1], "ylim": [-0.06, 1.12],
    "items": [
        {"kind": "graph", "f": S, "domain": [-1, 0.99], "color": "#1D4ED8"},
        {"kind": "point", "x": 1, "y": 1, "label": "S(1)=1"},
        {"kind": "vline", "x": -1, "style": "dashed", "label": "x=−1"},
        {"kind": "vline", "x": 1, "style": "dashed", "label": "x=1"},
        {"kind": "label", "x": 0.1, "y": 0.55, "text": "S(x)=x+(1−x)ln(1−x)"},
    ],
    "caption": "原卷解法：收敛域 [−1,1]；S(x)=x∑xⁿ/n−∑x^{n+1}/(n+1)=x∫₀ˣdt/(1−t)−∫₀ˣ t/(1−t)dt=(1−x)ln(1−x)+x（x<1），S(1)=lim_{x→1⁻}=1。曲线由和函数表达式绘制，非原卷插图。",
})

json.dump(figs, io.open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("写出", OUT, len(figs), "幅", os.path.getsize(OUT) // 1024, "KB")
