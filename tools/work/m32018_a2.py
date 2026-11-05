# -*- coding: utf-8 -*-
"""2018 数学三 解析 填空题 9-14（原卷 p7-p9，逐字照录）"""

A = {}

A[9] = (r"y=4x-3", [
    r"【答案】$y=4x-3$.",
    r"【解析】由题可知，$y'=2x+\dfrac{2}{x}$，$y''=2+\dfrac{-2}{x^{2}}$.",
    r"令$y''=2+\dfrac{-2}{x^{2}}=0$，解得$x=1$，所以曲线的拐点为$(1,1)$.",
    r"又$y'(1)=4$即为切线斜率，所以切线方程为$y=4x-3$.",
])

A[10] = (r"e^{x}\arcsin\sqrt{1-e^{2x}}-\sqrt{1-e^{2x}}+C", [
    r"【答案】$e^{x}\arcsin\sqrt{1-e^{2x}}-\sqrt{1-e^{2x}}+C$. 其中$C$为任意常数.",
    r"【解析】$\int e^{x}\arcsin\sqrt{1-e^{2x}}\mathrm{d}x=\int\arcsin\sqrt{1-e^{2x}}\ \mathrm{d}e^{x}$",
    r"$=e^{x}\arcsin\sqrt{1-e^{2x}}-\int\dfrac{e^{x}}{\sqrt{1-(1-e^{2x})}}\cdot\dfrac{1}{2\sqrt{1-e^{2x}}}\cdot(-2e^{2x})\mathrm{d}x$",
    r"$=e^{x}\arcsin\sqrt{1-e^{2x}}+\int\dfrac{e^{2x}}{\sqrt{1-e^{2x}}}\mathrm{d}x$",
    r"$=e^{x}\arcsin\sqrt{1-e^{2x}}-\dfrac{1}{2}\int\dfrac{1}{\sqrt{1-e^{2x}}}\mathrm{d}(1-e^{2x})$",
    r"$=e^{x}\arcsin\sqrt{1-e^{2x}}-\sqrt{1-e^{2x}}+C$. 其中$C$为任意常数.",
])

A[11] = (r"y_{x}=C\cdot2^{x}-5", [
    r"【答案】$y_{x}=C\cdot2^{x}-5$. 其中$C$为任意常数.",
    r"【解析】$\Delta^{2}y_{x}=\Delta(\Delta y_{x})=\Delta y_{x+1}-\Delta y_{x}"
    r"=(y_{x+2}-y_{x+1})-(y_{x+1}-y_{x})=y_{x+2}-2y_{x+1}+y_{x}$，所"
    r"以原方程可化为$y_{x+2}-2y_{x+1}=5$. 易知，对应齐次方程$y_{x+2}-2y_{x+1}=0$的通解为$y_{x}=C\cdot2^{x}$.",
    r"设原方程的特解为$y_{x}^{*}=A$，代入原方程中得$A=-5$. 所以原方程的通解为",
    r"$y_{x}=C\cdot2^{x}-5$. 其中$C$为任意常数.",
])

A[12] = ("2e", [
    r"【答案】$2e$.",
    r"【解析】由$f(x+\Delta x)-f(x)=2xf(x)\Delta x+o(\Delta x)\ (\Delta x\to0)$，可得",
    r"$\dfrac{f(x+\Delta x)-f(x)}{\Delta x}=2xf(x)+\Delta x$.",
    r"等式两边取极限可得微分方程$f'(x)=2xf(x)$，解得$f(x)=Ce^{x^{2}}$，",
    r"再由$f(0)=2$得$C=2$，所以 $f(x)=2e^{x^{2}}$，所以 $f(1)=2e$.",
])

A[13] = ("2", [
    r"【答案】$2$",
    r"【解析】由$A\boldsymbol{\alpha}_{1}=\boldsymbol{\alpha}_{1}+\boldsymbol{\alpha}_{2}$，"
    r"$A\boldsymbol{\alpha}_{2}=\boldsymbol{\alpha}_{2}+\boldsymbol{\alpha}_{3}$，"
    r"$A\boldsymbol{\alpha}_{3}=\boldsymbol{\alpha}_{1}+\boldsymbol{\alpha}_{3}$，可得",
    r"$A(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3})"
    r"=(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3})"
    r"\begin{pmatrix}1&0&1\\ 1&1&0\\ 0&1&1\end{pmatrix}$. "
    r"由于$\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}$线性无关，"
    r"故$P=(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3})$可逆，",
    r"$A\sim\begin{pmatrix}1&0&1\\ 1&1&0\\ 0&1&1\end{pmatrix}=B$，从而有相同的行列式，$|A|=|B|=2$.",
])

A[14] = (r"\dfrac{1}{3}", [
    r"【答案】$\dfrac{1}{3}$.",
    r"【解析】由$A,B,C$相互独立可得，",
    r"$P(AB)=P(A)P(B)$，$P(AC)=P(A)P(C)$.",
    r"而，$P(AC|A\cup B)=\dfrac{P(AC(A\cup B))}{P(A\cup B)}"
    r"=\dfrac{P((ACA)\cup(ACB))}{P(A)+P(B)-P(AB)}$",
    r"$=\dfrac{P(AC)}{P(A)+P(B)-P(A)P(B)}$，",
    r"又因为$P(A)=P(B)=P(C)=\dfrac{1}{2}$，"
    r"所以$P(AC|A\cup B)=\dfrac{\dfrac{1}{2}\cdot\dfrac{1}{2}}{\dfrac{1}{2}+\dfrac{1}{2}-\dfrac{1}{2}\cdot\dfrac{1}{2}}=\dfrac{1}{3}$.",
])
