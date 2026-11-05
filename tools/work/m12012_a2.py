# -*- coding: utf-8 -*-
"""2012 数学一 解析 填空题 9-14（原卷 p7-p8，逐字照录【答案】【解析】；本卷解析标签为【解析】）"""

A = {}

A[9] = ("e^{x}", [
    r"【答案】$e^{x}$",
    r"【解析】$f''(x)+f'(x)-2f(x)=0$ 的通解为 $C_{1}e^{-2x}+C_{2}e^{x}$；",
    r"将 $f(x)=C_{1}e^{-2x}+C_{2}e^{x}$ 和 $f''(x)=4C_{1}e^{-2x}+C_{2}e^{x}$ 代入 $f''(x)+f(x)=2e^{x}$，于是，可得：",
    r"$C_{1}=0, C_{2}=1$，故函数为 $f(x)=e^{x}$.",
])

A[10] = (r"\frac{\pi}{2}", [
    r"【答案】$\dfrac{\pi}{2}$",
    r"【解析】令 $t=x-1$，易得 $\int_{0}^{2}x\sqrt{2x-x^{2}}dx=\int_{-1}^{1}(t+1)\sqrt{1-t^{2}}dt$",
    r"由于 $t\sqrt{1-t^{2}}$ 为奇函数，所以 $\int_{-1}^{1}t\sqrt{1-t^{2}}dt=0$，故原积分变为 $\int_{-1}^{1}\sqrt{1-t^{2}}dt=\dfrac{\pi}{2}$.",
])

A[11] = ("(1,1,1)", [
    r"【答案】$(1,1,1)$",
    r"【解析】$\dfrac{\partial\left(xy+\dfrac{z}{y}\right)}{\partial x}=y$，$\dfrac{\partial\left(xy+\dfrac{z}{y}\right)}{\partial y}=x-\dfrac{z}{y^{2}}$，$\dfrac{\partial\left(xy+\dfrac{z}{y}\right)}{\partial z}=\dfrac{1}{y}$，梯度公式代入点 $(2,1,1)$",
    r"可得出答案.",
])

A[12] = (r"\frac{\sqrt{3}}{12}", [
    r"【答案】$\dfrac{\sqrt{3}}{12}$",
    r"【解析】投影到 $xoy$ 平面上，$\iint\limits_{\Sigma}y^{2}dS=\iint\limits_{D}y^{2}\sqrt{3}dxdy=\sqrt{3}\int_{0}^{1}dy\int_{0}^{1-y}y^{2}dx=\dfrac{\sqrt{3}}{12}$.",
])

A[13] = ("2", [
    r"【答案】2.",
    r"【解析】",
    r"由 $\boldsymbol{\alpha}$ 为三维单位向量，知矩阵 $\boldsymbol{\alpha}\boldsymbol{\alpha}^{T}$ 的秩为 1，特征值为 1,0,0，从而 $\boldsymbol{E}-\boldsymbol{\alpha}\boldsymbol{\alpha}^{T}$ 特征值为 0,1,1.",
    r"由于 $\boldsymbol{E}-\boldsymbol{\alpha}\boldsymbol{\alpha}^{T}$ 为实对称矩阵，又实对称矩阵的秩等于非零特征值的个数，故 $\boldsymbol{E}-\boldsymbol{\alpha}\boldsymbol{\alpha}^{T}$ 的秩",
    r"为 2.",
])

A[14] = (r"\frac{3}{4}", [
    r"【答案】$\dfrac{3}{4}$",
    r"【解析】因为 $A$ 与 $C$ 互不相容，即 $AC=\phi$，又因为 $A=AC+A\overline{C}$，所以 $A\overline{C}=A$",
    r"从而 $AB\overline{C}=AB$，则 $P(AB|\overline{C})=\dfrac{P(AB\overline{C})}{P(\overline{C})}=\dfrac{P(AB)}{1-P(C)}=\dfrac{3}{4}$.",
])
