# -*- coding: utf-8 -*-
"""2012 数学三 解析 选择题 1-8（原卷 p5-p7，逐字照录）"""

A = {}

A[1] = ("C", [
    r"(1)【答案】（C）",
    r"【详解】$\lim\limits_{x\to1}\dfrac{x^{2}+x}{x^{2}-1}=\lim\limits_{x\to1}\dfrac{x}{x-1}=\infty$，有 1 条垂直渐近线；",
    r"$\lim\limits_{x\to\infty}\dfrac{x^{2}+x}{x^{2}-1}=\lim\limits_{x\to\infty}\dfrac{x}{x-1}=1$，有 1 条水平渐近线；",
])

A[2] = ("A", [
    r"(2)【答案】（A）",
    r"【详解】由已知 $f(0)=0$，则",
    r"$f'(0)=\lim\limits_{x\to0}\dfrac{f(x)-f(0)}{x}=\lim\limits_{x\to0}\dfrac{\left(e^{x}-1\right)\left(e^{2x}-2\right)\cdots\left(e^{nx}-n\right)}{x}$",
    r"$=\lim\limits_{x\to0}\left(e^{2x}-2\right)\cdots\left(e^{nx}-n\right)=(-1)^{n-1}(n-1)!$",
])

A[3] = ("B", [
    r"(3)【答案】（B）",
    r"【解析】由已知，被积函数为 $f\left(x^{2}+y^{2}\right)$，而积分区域为",
    r"$D=\left\{(x,y)\left|\sqrt{2x-x^{2}}\leqslant y\leqslant\sqrt{4-x^{2}},0\leqslant x\leqslant2\right.\right\}$，故应选 B",
])

A[4] = ("D", [
    r"(4)【答案】（D）",
    r"【详解】$\sqrt{n}\sin\dfrac{1}{n^{a}}\sim\dfrac{1}{n^{a-\frac{1}{2}}}\Rightarrow a-\dfrac{1}{2}>1,a>\dfrac{3}{2},$",
    r"级数 $\sum\limits_{n=1}^{\infty}\dfrac{(-1)^{n}}{n^{2-a}}$ 条件收敛，则 $0<2-a\leqslant1\Rightarrow2>a\geqslant1$，于是，选择 D.",
])

A[5] = ("C", [
    r"(5)【答案】（C）.",
    r"【详解】$\left|\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}\right|=-c_{1}$，"
    r"若 $c_{1}\neq0$ 则 $\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}$ 线性无关；"
    r"$\left|\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{4}\right|=c_{1}$，"
    r"若 $c_{1}\neq0$ 则 $\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{4}$ 线性无关；",
    r"$\left|\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}\right|=0$，"
    r"则 $\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}$ 线性相关；"
    r"$\left|\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}\right|=-c_{4}-c_{3}$，当 $-c_{4}\neq c_{3}$ 时，"
    r"则 $\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}$ 线性无关；综上所述，故应选（C）.",
])

A[6] = ("B", [
    r"（6）【详解】解法一：由题设，",
    r"$Q=\left(\boldsymbol{\alpha}_{1}+\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}\right)"
    r"=\left(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}\right)"
    r"\begin{pmatrix}1&0&0\\ 1&1&0\\ 0&0&1\end{pmatrix},$",
    r"从而",
    r"$Q^{-1}AQ=\begin{pmatrix}1&0&0\\ 1&1&0\\ 0&0&1\end{pmatrix}^{-1}P^{-1}AP"
    r"\begin{pmatrix}1&0&0\\ 1&1&0\\ 0&0&1\end{pmatrix}$",
    r"$=\begin{pmatrix}1&0&0\\ 1&1&0\\ 0&0&1\end{pmatrix}^{-1}"
    r"\begin{pmatrix}1&0&0\\ 0&1&0\\ 0&0&2\end{pmatrix}"
    r"\begin{pmatrix}1&0&0\\ 1&1&0\\ 0&0&1\end{pmatrix}"
    r"=\begin{pmatrix}1&0&0\\ 0&1&0\\ 0&0&2\end{pmatrix}$",
    r"故应选（B）.",
    r"解法二：由题设 $P^{-1}AP=\begin{pmatrix}1&0&0\\ 0&1&0\\ 0&0&2\end{pmatrix}$ 可知，矩阵 $A$ 是可相似对角化的矩阵，"
    r"因而其相似变换矩阵 $P$ 的列向量 $\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}$ "
    r"是 $A$ 的分别属于特征值 1,1,2 的特征向量. 由于 1,1 是二重特征值，故 $\boldsymbol{\alpha}_{1}+\boldsymbol{\alpha}_{2}$ "
    r"仍属于特征值 1 的特征向量，故 $Q^{-1}AQ=\begin{pmatrix}1&0&0\\ 0&1&0\\ 0&0&2\end{pmatrix}$.",
])

A[7] = ("D", [
    r"(7)【答案】（D）",
    r"【详解】因为随机变量 $X$ 和 $Y$ 相互独立，且均服从 $(0,1)$ 上的均匀分布，",
    r"所以 $X$ 和 $Y$ 的联合概率分布为：$f(x,y)=\begin{cases}1,&0<x<1,0<y<1\\ 0,&\text{其他}\end{cases},$",
    r"则 $P\left(x^{2}+y^{2}\leqslant1\right)=\int_{0}^{\frac{\pi}{2}}d\theta\int_{0}^{1}rdr=\dfrac{\pi}{4}$.",
])

A[8] = ("B", [
    r"(8)【答案】（B）",
    r"【详解】排除法：从统计量 $\dfrac{X_{1}-X_{2}}{\left|X_{3}+X_{4}-2\right|}$ 的形式中含有绝对值，"
    r"就可以排除掉（A）,(C)和（D）,只能选（B）",
    r"直接法：因为 $X_{1},X_{2},X_{3},X_{4}$ 为来自总体为 $N\left(1,\sigma^{2}\right)(\sigma>0)$ 的简单随机样本",
    r"所以 $X_{1},X_{2},X_{3},X_{4}$ 相互独立且都服从 $N\left(1,\sigma^{2}\right)(\sigma>0)$.",
    r"则 $\left(X_{1}-X_{2}\right)$ 服从 $N\left(0,2\sigma^{2}\right)$，"
    r"即 $\dfrac{X_{1}-X_{2}}{\sqrt{2}\sigma}$ 服从 $N(0,1)$；",
    r"$\left(X_{3}+X_{4}-2\right)$ 服从 $N\left(0,2\sigma^{2}\right)$，"
    r"即 $\dfrac{X_{3}+X_{4}-2}{\sqrt{2}\sigma}$ 服从 $N(0,1)$，"
    r"$\left(\dfrac{X_{3}+X_{4}-2}{\sqrt{2}\sigma}\right)^{2}$ 服从 $\chi^{2}(1)$.",
    r"从而 $\dfrac{X_{1}-X_{2}}{\left|X_{3}+X_{4}-2\right|}"
    r"=\dfrac{\dfrac{X_{1}-X_{2}}{\sqrt{2}\sigma}}{\left|\dfrac{X_{3}+X_{4}-2}{\sqrt{2}\sigma}\right|}$ 服从 $t(1)$.",
])
