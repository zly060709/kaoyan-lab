# -*- coding: utf-8 -*-
"""2012 数学三 题干视觉转录（照录 data/math3/pages/2012/p1-p4.png）"""

ITEMS = []

def add(**kw):
    ITEMS.append(kw)

# ---------- 一、选择题 1-8（每小题 4 分，共 32 分） ----------
add(num=1, type="single", score=4, pages=[1], anchor="第(1)题",
    stem=r"曲线 $y=\dfrac{x^{2}+x}{x^{2}-1}$ 的渐近线条数为（ ）.",
    options=[r"0", r"1", r"2", r"3"])

add(num=2, type="single", score=4, pages=[1], anchor="第(2)题",
    stem=r"设函数 $f(x)=\left(e^{x}-1\right)\left(e^{2x}-2\right)\cdots\left(e^{nx}-n\right)$，其中 $n$ 为正整数，则 $f'(0)=$.",
    options=[r"$(-1)^{n-1}(n-1)!$", r"$(-1)^{n}(n-1)!$",
             r"$(-1)^{n-1}n!$", r"$(-1)^{n}n!$"])

add(num=3, type="single", score=4, pages=[1], anchor="第(3)题",
    stem=r"设函数 $f(t)$ 连续，则二次积分 $\int_{0}^{\frac{\pi}{2}}d\theta\int_{2\cos\theta}^{2}f\left(r^{2}\right)rdr=$（ ）.",
    options=[
        r"$\int_{0}^{2}dx\int_{\sqrt{2x-x^{2}}}^{\sqrt{4-x^{2}}}\sqrt{x^{2}+y^{2}}f\left(x^{2}+y^{2}\right)dy$",
        r"$\int_{0}^{2}dx\int_{\sqrt{2x-x^{2}}}^{\sqrt{4-x^{2}}}f\left(x^{2}+y^{2}\right)dy$",
        r"$\int_{0}^{2}dy\int_{1+\sqrt{1+y^{2}}}^{\sqrt{1-y^{2}}}\sqrt{x^{2}+y^{2}}f\left(x^{2}+y^{2}\right)dx$",
        r"$\int_{0}^{2}dy\int_{1+\sqrt{1+y^{2}}}^{\sqrt{1-y^{2}}}f\left(x^{2}+y^{2}\right)dx$",
    ])

add(num=4, type="single", score=4, pages=[1], anchor="第(4)题",
    stem=r"已知级数 $\sum\limits_{n=1}^{\infty}(-1)^{n}\sqrt{n}\sin\dfrac{1}{n^{a}}$ 绝对收敛，"
         r"级数 $\sum\limits_{n=1}^{\infty}\dfrac{(-1)^{n}}{n^{2-a}}$ 条件收敛，则（ ）.",
    options=[r"$0<a\leqslant\dfrac{1}{2}$", r"$\dfrac{1}{2}<a\leqslant1$",
             r"$1<a\leqslant\dfrac{3}{2}$", r"$\dfrac{3}{2}<a<2$"])

add(num=5, type="single", score=4, pages=[1], anchor="第(5)题",
    stem=r"设 $\boldsymbol{\alpha}_{1}=\begin{pmatrix}0\\ 0\\ c_{1}\end{pmatrix},"
         r"\boldsymbol{\alpha}_{2}=\begin{pmatrix}0\\ 1\\ c_{2}\end{pmatrix},"
         r"\boldsymbol{\alpha}_{3}=\begin{pmatrix}1\\ -1\\ c_{3}\end{pmatrix},"
         r"\boldsymbol{\alpha}_{4}=\begin{pmatrix}-1\\ 1\\ c_{4}\end{pmatrix}$，"
         r"其中 $c_{1},c_{2},c_{3},c_{4}$ 为任意常数，则下列向量组线性相关的是（ ）.",
    options=[r"$\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}$",
             r"$\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{4}$",
             r"$\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}$",
             r"$\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}$"])

add(num=6, type="single", score=4, pages=[2], anchor="第(6)题",
    stem=r"设 $A$ 为三阶矩阵，$P$ 为三阶可逆矩阵，且 $P^{-1}AP=\begin{pmatrix}1&0&0\\ 0&1&0\\ 0&0&2\end{pmatrix}$，"
         r"若 $P=\left(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}\right)$，"
         r"$Q=\left(\boldsymbol{\alpha}_{1}+\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}\right)$，则 $Q^{-1}AQ=$（ ）.",
    options=[
        r"$\begin{pmatrix}1&0&0\\ 0&2&0\\ 0&0&1\end{pmatrix}$",
        r"$\begin{pmatrix}1&0&0\\ 0&1&0\\ 0&0&2\end{pmatrix}$",
        r"$\begin{pmatrix}2&0&0\\ 0&1&0\\ 0&0&2\end{pmatrix}$",
        r"$\begin{pmatrix}2&0&0\\ 0&2&0\\ 0&0&1\end{pmatrix}$",
    ])

add(num=7, type="single", score=4, pages=[2], anchor="第(7)题",
    stem=r"设随机变量 $X$ 和 $Y$ 相互独立，且均服从 $(0,1)$ 上的均匀分布，则 $P\left(x^{2}+y^{2}\leqslant1\right)=$.",
    options=[r"$\dfrac{1}{4}$", r"$\dfrac{1}{2}$", r"$\dfrac{\pi}{8}$", r"$\dfrac{\pi}{4}$"])

add(num=8, type="single", score=4, pages=[2], anchor="第(8)题",
    stem=r"设 $X_{1},X_{2},X_{3},X_{4}$ 为来自总体为 $N\left(1,\sigma^{2}\right)(\sigma>0)$ 的简单随机样本，"
         r"则统计量 $\dfrac{X_{1}-X_{2}}{\left|X_{3}+X_{4}-2\right|}$ 的分布为（ ）.",
    options=[r"$N(0,1)$", r"$t(1)$", r"$\chi^{2}(1)$", r"$F(1,1)$"])

# ---------- 二、填空题 9-14（每小题 4 分，共 24 分） ----------
add(num=9, type="blank", score=4, pages=[2], anchor="第(9)题",
    stem=r"$\lim\limits_{x\to\frac{\pi}{4}}(\tan x)^{\frac{1}{\cos x-\sin x}}=$________.",
    options=[])

add(num=10, type="blank", score=4, pages=[2], anchor="第(10)题",
    stem=r"设函数 $f(x)=\begin{cases}\ln\sqrt{x},&x\geqslant1,\\ 2x-1,&x<1\end{cases}$，$y=f(f(x))$，"
         r"则 $\dfrac{dy}{dx}\Big|_{x=e}=$________.",
    options=[])

add(num=11, type="blank", score=4, pages=[2], anchor="第(11)题",
    stem=r"设连续函数 $z=f(x,y)$ 满足 $\lim\limits_{x\to0\atop y\to1}\dfrac{f(x,y)-2x+y-2}{\sqrt{x^{2}+(y-1)^{2}}}=0$，"
         r"则 $dz\big|_{(0,1)}=$________.",
    options=[])

add(num=12, type="blank", score=4, pages=[2], anchor="第(12)题",
    stem=r"由曲线 $y=\dfrac{4}{x}$ 和直线 $y=x$ 及 $y=4x$ 在第一象限中围成的平面图形的面积为____.",
    options=[])

add(num=13, type="blank", score=4, pages=[2], anchor="第(13)题",
    stem=r"设 $A$ 为三阶矩阵，$|A|=3$，$A^{*}$ 为 $A$ 的伴随矩阵，若交换 $A$ 的第一行与第二行得到"
         r"矩阵 $B$，则 $\left|BA^{*}\right|=$________.",
    options=[])

add(num=14, type="blank", score=4, pages=[2], anchor="第(14)题",
    stem=r"设 $A,B,C$ 为三个随机事件，$A$ 与 $C$ 互不相容，$P(AB)=\dfrac{1}{2},P(C)=\dfrac{1}{3}$，"
         r"则$P\left(AB\big|\overline{C}\right)=$____.",
    options=[])

# ---------- 三、解答题 15-23（共 94 分） ----------
add(num=15, type="essay", score=10, pages=[3], anchor="第(15)题",
    stem=r"计算 $\lim\limits_{x\to0}\dfrac{e^{x^{2}}-e^{2-2\cos x}}{x^{4}}$.",
    options=[])

add(num=16, type="essay", score=10, pages=[3], anchor="第(16)题",
    stem=r"计算二重积分 $\iint\limits_{D}e^{x}xydxdy$，其中 D 是以曲线 $y=\sqrt{x},y=\dfrac{1}{\sqrt{x}}$ "
         r"及 y 轴为边界的无界区域.",
    options=[])

add(num=17, type="essay", score=10, pages=[3], anchor="第(17)题",
    stem=r"某企业为生产甲、乙两种型号的产品，投入的固定成本为 $10000$（万元），设该企业"
         r"生产甲、乙两种产品的产量分别为 x 件和 y 件，且两种产品的边际成本分别为 $20+\dfrac{x}{2}$（万"
         r"元/件）与 $6+y$（万元/件）"
         r"（1）求生产甲乙两种产品的总成本函数 $C(x,y)$（万元）."
         r"（2）当生产总量为 $50$ 件时，甲乙两种的产量各为多少时可使总成本最小？并求出最小成本."
         r"（3）求总产量为 $50$ 件且总成本最小时，甲产品的边际成本，并解释其经济意义.",
    options=[])

add(num=18, type="essay", score=10, pages=[3], anchor="第(18)题",
    stem=r"证明：$x\ln\dfrac{1+x}{1-x}+\cos x>1+\dfrac{x^{2}}{2},\ -1<x<1$.",
    options=[])

add(num=19, type="essay", score=12, pages=[3], anchor="第(19)题",
    stem=r"已知函数 $f(x)$ 满足方程 $f''(x)+f'(x)-2f(x)=0$ 及 $f''(x)+f(x)=2e^{x}$."
         r"（1）求 $f(x)$ 的表达式；"
         r"（2）求曲线 $y=f\left(x^{2}\right)\int_{0}^{x}f\left(-t^{2}\right)dt$ 的拐点.",
    options=[])

add(num=20, type="essay", score=11, pages=[3], anchor="第(20)题",
    stem=r"设 $A=\begin{pmatrix}1&a&0&0\\ 0&1&a&0\\ 0&0&1&a\\ a&0&0&1\end{pmatrix},"
         r"\boldsymbol{\beta}=\begin{pmatrix}1\\ -1\\ 0\\ 0\end{pmatrix}$."
         r"（1）计算$|A|$；"
         r"（2）当实数 $a$ 取何值时，$Ax=\boldsymbol{\beta}$ 有无穷多解，并求其通解.",
    options=[])

add(num=21, type="essay", score=11, pages=[3, 4], anchor="第(21)题",
    stem=r"已知 $A=\begin{pmatrix}1&0&1\\ 0&1&1\\ -1&0&a\\ 0&a&-1\end{pmatrix}$，"
         r"二次型 $f\left(x_{1},x_{2},x_{3}\right)=\boldsymbol{x}^{T}\left(A^{T}A\right)\boldsymbol{x}$ 的秩为 2."
         r"（1）求实数 $a$ 的值；"
         r"（2）求正交变换 $\boldsymbol{x}=\boldsymbol{Qy}$ 将 $f$ 化为标准形.",
    options=[])

add(num=22, type="essay", score=10, pages=[4], anchor="第(22)题",
    stem=r"设二维离散型随机变量 $X$ 与 $Y$ 的概率分布为"
         r"$\begin{array}{c|ccc} X\backslash Y & 0 & 1 & 2\\ \hline"
         r" 0 & \dfrac{1}{4} & 0 & \dfrac{1}{4}\\"
         r" 1 & 0 & \dfrac{1}{3} & 0\\"
         r" 2 & \dfrac{1}{12} & 0 & \dfrac{1}{12}\\"
         r"\end{array}$"
         r"求：（1）$P(X=2Y)$"
         r"（2）$\mathrm{cov}(X-Y,Y)$",
    options=[])

add(num=23, type="essay", score=10, pages=[4], anchor="第(23)题",
    stem=r"设随机变量 $X$ 和 $Y$ 相互独立，且均服从参数为 1 的指数分布，"
         r"$V=\min(X,Y),U=\max(X,Y)$."
         r"求：（1）随机变量 $V$ 的概率密度；"
         r"（2）$E(U+V)$.",
    options=[])
