# -*- coding: utf-8 -*-
"""2012 数学一 解析 选择题 1-8（原卷 p5-p7，逐字照录【答案】【解析】；本卷解析标签为【解析】）"""

A = {}

A[1] = ("C", [
    r"【答案】(C)",
    r"【解析】$\lim\limits_{x\to1}\dfrac{x^{2}+x}{x^{2}-1}=\lim\limits_{x\to1}\dfrac{x}{x-1}=\infty$，有 1 条垂直渐近线 $x=1$；",
    r"$\lim\limits_{x\to\infty}\dfrac{x^{2}+x}{x^{2}-1}=\lim\limits_{x\to\infty}\dfrac{x}{x-1}=1$，有 1 条水平渐近线 $y=1$.",
])

A[2] = ("A", [
    r"【答案】（A）",
    r"【解析】方法一：由已知 $f(0)=0$，则",
    r"$f'(0)=\lim\limits_{x\to0}\dfrac{f(x)-f(0)}{x}=\lim\limits_{x\to0}\dfrac{(e^{x}-1)(e^{2x}-2)\cdots(e^{nx}-n)}{x}$.",
    r"$=\lim\limits_{x\to0}(e^{2x}-2)\cdots(e^{nx}-n)=(-1)^{n-1}(n-1)!$",
])

A[3] = ("B", [
    r"【答案】（B）",
    r"【解析】由已知 $\lim\limits_{x\to0\atop y\to0}\dfrac{f(x,y)}{x^{2}+y^{2}}$ 存在，又连续，则 $f(0,0)=0$；且 $\lim\limits_{x\to0\atop y=0}\dfrac{f(x,0)-f(0,0)}{x^{2}}$ 存在,",
    r"于是 $\lim\limits_{x\to0\atop y=0}\dfrac{f(x,0)-f(0,0)}{x}=0$，$f_{x}(0,0)=0$，同理可得 $f_{y}(0,0)=0$，于是由可微定",
    r"义 $\lim\limits_{x\to0\atop y\to0}\dfrac{f(x,y)-f(0,0)-f_{x}(0,0)x-f_{y}(0,0)y}{\sqrt{x^{2}+y^{2}}}=\lim\limits_{x\to0\atop y\to0}\dfrac{f(x,y)}{\sqrt{x^{2}+y^{2}}}=0$,于是，可微．应",
    r"选（B）.",
])

A[4] = ("D", [
    r"【答案】（D）.",
    r"【解析】$I_{1}=\int_{0}^{\pi}e^{x^{2}}\sin xdx>0$,",
    r"$I_{2}=\int_{0}^{2\pi}e^{x^{2}}\sin xdx=\int_{0}^{\pi}e^{x^{2}}\sin xdx-\int_{0}^{\pi}e^{(x+\pi)^{2}}\sin xdx=I_{1}-\int_{0}^{\pi}e^{(x+\pi)^{2}}\sin xdx<I_{1}$",
    r"$I_{3}=\int_{0}^{3\pi}e^{x^{2}}\sin xdx=I_{2}+\int_{2\pi}^{3\pi}e^{x^{2}}\sin xdx=\int_{0}^{\pi}e^{x^{2}}\sin xdx-\int_{0}^{\pi}e^{(x+\pi)^{2}}\sin xdx+\int_{0}^{\pi}e^{(x+2\pi)^{2}}\sin xdx$",
    r"$=I_{1}+\int_{0}^{\pi}\left(e^{(x+2\pi)^{2}}-e^{(x+\pi)^{2}}\right)\sin xdx>I_{1}$.",
])

A[5] = ("C", [
    r"【答案】(C)．",
    r"【解析】由 $\boldsymbol{\alpha}_{3}+\boldsymbol{\alpha}_{4}=\begin{pmatrix}0\\0\\c_{5}\end{pmatrix}$ 必与 $\boldsymbol{\alpha}_{1}$ 线性相关，从而 $\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}$ 线性相关，故应选（C）.",
])

A[6] = ("B", [
    r"【答案】(B)．",
    r"【解析】解法一：由题设，",
    r"$\boldsymbol{Q}=(\boldsymbol{\alpha}_{1}+\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3})=(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3})\begin{pmatrix}1&0&0\\1&1&0\\0&0&1\end{pmatrix}$",
    r"从而",
    r"$\boldsymbol{Q}^{-1}\boldsymbol{A}\boldsymbol{Q}=\begin{pmatrix}1&0&0\\1&1&0\\0&0&1\end{pmatrix}^{-1}\boldsymbol{P}^{-1}\boldsymbol{A}\boldsymbol{P}\begin{pmatrix}1&0&0\\1&1&0\\0&0&1\end{pmatrix}$",
    r"$=\begin{pmatrix}1&0&0\\1&1&0\\0&0&1\end{pmatrix}^{-1}\begin{pmatrix}1&0&0\\0&1&0\\0&0&2\end{pmatrix}\begin{pmatrix}1&0&0\\1&1&0\\0&0&1\end{pmatrix}=\begin{pmatrix}1&0&0\\0&1&0\\0&0&2\end{pmatrix}$",
    r"解法二：由题设 $\boldsymbol{P}^{-1}\boldsymbol{A}\boldsymbol{P}=\begin{pmatrix}1&0&0\\0&1&0\\0&0&2\end{pmatrix}$ 可知，矩阵 $\boldsymbol{A}$ 是可相似对角化的矩阵，因而",
    r"其相似变换矩阵 $\boldsymbol{P}$ 的列向量 $\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}$ 是 $\boldsymbol{A}$ 的分别属于特征值 1,1,2 的特征向量．由",
    r"于 1,1 是二重特征值，故 $\boldsymbol{\alpha}_{1}+\boldsymbol{\alpha}_{2}$ 仍属于特征值 1 的特征向量，故 $\boldsymbol{Q}^{-1}\boldsymbol{A}\boldsymbol{Q}=\begin{pmatrix}1&0&0\\0&1&0\\0&0&2\end{pmatrix}$，",
    r"故应选（B）．",
])

A[7] = ("A", [
    r"【答案】(A)",
    r"【解析】因为随机变量 $X$ 和 $Y$ 相互独立，且分别服从参数为 1 和参数为 4 的指数分布，即",
    r"$f_{x}(x)=\begin{cases}e^{-x}, x\geqslant0\\0, \text{其他}\end{cases}$   $f_{y}(y)=\begin{cases}4e^{-4y}, y\geqslant0\\0, \text{其他}\end{cases}$",
    r"所以 $X$ 和 $Y$ 的联合概率分布为：$f(x,y)=\begin{cases}4e^{-x-4y}, x,y\geqslant0\\0, \text{其他}\end{cases}$",
    r"则 $P(x<y)=\int_{0}^{+\infty}dx\int_{x}^{+\infty}4e^{-x-4y}dy=\dfrac{1}{5}$.",
])

A[8] = ("D", [
    r"【答案】(D)",
    r"【解析】设截成两段的长度分别为 $X$ 与 $Y$,则 $X+Y=1$,即 $Y=1-X$，也就是说 $X$ 与 $Y$ 存在",
    r"确定的线性关系，所以 $X$ 与 $Y$ 的相关系数的绝对值为 1，而 $X$ 的系数小于 0，则 $X$ 与 $Y$",
    r"的相关系数为 $-1$.",
])
