# -*- coding: utf-8 -*-
"""2018 数学三 题干视觉转录（照录 data/math3/pages/2018/p1-p4.png）"""

ITEMS = []

def add(**kw):
    ITEMS.append(kw)

# ---------- 一、选择题 1-8（每小题 4 分，共 32 分） ----------
add(num=1, type="single", score=4, pages=[1], anchor="第(1)题",
    stem=r"下列函数中，在 $x=0$ 处不可导的是（  ）",
    options=[r"$f(x)=|x|\sin|x|$.",
             r"$f(x)=|x|\sin\sqrt{|x|}$.",
             r"$f(x)=\cos|x|$.",
             r"$f(x)=\cos\sqrt{|x|}$."])

add(num=2, type="single", score=4, pages=[1], anchor="第(2)题",
    stem=r"设函数 $f(x)$ 在 $[0,1]$ 上二阶可导，且 $\int_{0}^{1}f(x)\mathrm{d}x=0$，则（  ）",
    options=[r"当 $f'(x)<0$ 时，$f(\dfrac{1}{2})<0$.",
             r"当 $f''(x)<0$ 时，$f(\dfrac{1}{2})<0$.",
             r"当 $f'(x)>0$ 时，$f(\dfrac{1}{2})<0$.",
             r"当 $f''(x)>0$ 时，$f(\dfrac{1}{2})<0$."])

add(num=3, type="single", score=4, pages=[1], anchor="第(3)题",
    stem=r"设 $M=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\dfrac{(1+x)^{2}}{1+x^{2}}\mathrm{d}x$，"
         r"$N=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\dfrac{1+x}{e^{x}}\mathrm{d}x$，"
         r"$K=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}(1+\sqrt{\cos x})\mathrm{d}x$，则（  ）",
    options=[r"$M>N>K$.", r"$M>K>N$.", r"$K>M>N$.", r"$K>N>M$."])

add(num=4, type="single", score=4, pages=[1], anchor="第(4)题",
    stem=r"设某产品的成本函数 $C(Q)$ 可导，其中 $Q$ 为产量.若产量为 $Q_{0}$ 时平均成本最小，则（  ）",
    options=[r"$C'(Q_{0})=0$.",
             r"$C'(Q_{0})=C(Q_{0})$.",
             r"$C'(Q_{0})=Q_{0}C(Q_{0})$.",
             r"$Q_{0}C'(Q_{0})=C(Q_{0})$."])

add(num=5, type="single", score=4, pages=[1], anchor="第(5)题",
    stem=r"下列矩阵中，与矩阵 $\begin{pmatrix}1&1&0\\ 0&1&1\\ 0&0&1\end{pmatrix}$ 相似的为（  ）",
    options=[
        r"$\begin{pmatrix}1&1&-1\\ 0&1&1\\ 0&0&1\end{pmatrix}$.",
        r"$\begin{pmatrix}1&0&-1\\ 0&1&1\\ 0&0&1\end{pmatrix}$.",
        r"$\begin{pmatrix}1&1&-1\\ 0&1&0\\ 0&0&1\end{pmatrix}$.",
        r"$\begin{pmatrix}1&0&-1\\ 0&1&0\\ 0&0&1\end{pmatrix}$.",
    ])

add(num=6, type="single", score=4, pages=[1, 2], anchor="第(6)题",
    stem=r"设 $A,B$ 为 $n$ 矩阵，记 $r(X)$ 为矩阵 $X$ 的秩，$(X\ Y)$ 表示分块矩阵，则（  ）",
    options=[
        r"$r(A\ AB)=r(A)$.",
        r"$r(A\ BA)=r(A)$.",
        r"$r(A\ B)=\max\{r(A),r(B)\}$.",
        r"$r(A\ B)=r(A^{\mathrm{T}}\ B^{\mathrm{T}})$.",
    ])

add(num=7, type="single", score=4, pages=[2], anchor="第(7)题",
    stem=r"设随机变量 $X$ 的概率密度函数 $f(x)$ 满足 $f(1+x)=f(1-x)$，且 $\int_{0}^{2}f(x)\mathrm{d}x=0.6$，"
         r"则 $P\{X<0\}=$（  ）",
    options=[r"$0.2$.", r"$0.3$.", r"$0.4$.", r"$0.5$."])

add(num=8, type="single", score=4, pages=[2], anchor="第(8)题",
    stem=r"设 $X_{1},X_{2},\cdots,X_{n}\ (n\geqslant2)$ 为来自总体 $N(\mu,\sigma^{2})$ 的简单随机样本，"
         r"令 $\overline{X}=\dfrac{1}{n}\sum\limits_{i=1}^{n}X_{i}$，"
         r"$S=\sqrt{\dfrac{1}{n-1}\sum\limits_{i=1}^{n}(X_{i}-\overline{X})^{2}}$，"
         r"$S^{*}=\sqrt{\dfrac{1}{n}\sum\limits_{i=1}^{n}(X_{i}-\mu)^{2}}$，则（  ）",
    options=[
        r"$\dfrac{\sqrt{n}(\overline{X}-\mu)}{S}\sim t(n)$.",
        r"$\dfrac{\sqrt{n}(\overline{X}-\mu)}{S}\sim t(n-1)$.",
        r"$\dfrac{\sqrt{n}(\overline{X}-\mu)}{S^{*}}\sim t(n)$.",
        r"$\dfrac{\sqrt{n}(\overline{X}-\mu)}{S^{*}}\sim t(n-1)$.",
    ])

# ---------- 二、填空题 9-14（每小题 4 分，共 24 分） ----------
add(num=9, type="blank", score=4, pages=[2], anchor="第(9)题",
    stem=r"曲线 $y=x^{2}+2\ln x$ 在其拐点处的切线方程是________.",
    options=[])

add(num=10, type="blank", score=4, pages=[2], anchor="第(10)题",
    stem=r"$\int e^{x}\arcsin\sqrt{1-e^{2x}}\mathrm{d}x=$________.",
    options=[])

add(num=11, type="blank", score=4, pages=[2], anchor="第(11)题",
    stem=r"差分方程 $\Delta^{2}y_{x}-y_{x}=5$ 的通解为________.",
    options=[])

add(num=12, type="blank", score=4, pages=[2], anchor="第(12)题",
    stem=r"设函数 $f(x)$ 满足 $f(x+\Delta x)-f(x)=2xf(x)\Delta x+o(\Delta x)\ (\Delta x\to0)$，且 $f(0)=2$，"
         r"则 $f(1)=$________.",
    options=[])

add(num=13, type="blank", score=4, pages=[2], anchor="第(13)题",
    stem=r"设 $A$ 为 3 阶矩阵，$\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}$ 为线性无关的向量组，"
         r"若 $A\boldsymbol{\alpha}_{1}=\boldsymbol{\alpha}_{1}+\boldsymbol{\alpha}_{2}$，"
         r"$A\boldsymbol{\alpha}_{2}=\boldsymbol{\alpha}_{2}+\boldsymbol{\alpha}_{3}$，"
         r"$A\boldsymbol{\alpha}_{3}=\boldsymbol{\alpha}_{1}+\boldsymbol{\alpha}_{3}$，则$|A|=$________.",
    options=[])

add(num=14, type="blank", score=4, pages=[2], anchor="第(14)题",
    stem=r"设随机事件 $A,B,C$ 相互独立，且 $P(A)=P(B)=P(C)=\dfrac{1}{2}$，则"
         r"$P(AC|A\cup B)=$________.",
    options=[])

# ---------- 三、解答题 15-23（共 94 分） ----------
add(num=15, type="essay", score=10, pages=[3], anchor="第(15)题",
    stem=r"已知实数 $a,b$ 满足 $\lim\limits_{x\to+\infty}[(ax+b)e^{\frac{1}{x}}-x]=2$，求 $a,b$ 的值.",
    options=[])

add(num=16, type="essay", score=10, pages=[3], anchor="第(16)题",
    stem=r"设平面区域 $D$ 由曲线 $y=\sqrt{3(1-x^{2})}$ 与直线 $y=\sqrt{3}x$ 及 $y$ 轴围成，"
         r"计算二重积分 $\iint\limits_{D}x^{2}\mathrm{d}x\mathrm{d}y$.",
    options=[])

add(num=17, type="essay", score=10, pages=[3], anchor="第(17)题",
    stem=r"将长为 2 m 的铁丝分成三段，依次围成圆、正方形与正三角形. 三个图形的面积之和"
         r"是否存在最小值？若存在，求出最小值.",
    options=[])

add(num=18, type="essay", score=10, pages=[3], anchor="第(18)题",
    stem=r"已知 $\cos2x-\dfrac{1}{(1+x)^{2}}=\sum\limits_{n=0}^{\infty}a_{n}x^{n}\ (-1<x<1)$，求 $a_{n}$.",
    options=[])

add(num=19, type="essay", score=10, pages=[3], anchor="第(19)题",
    stem=r"设数列 $\{x_{n}\}$ 满足：$x_{1}>0$，$x_{n}e^{x_{n+1}}=e^{x_{n}}-1\ (n=1,2,\cdots)$. "
         r"证明 $\{x_{n}\}$ 收敛，并求 $\lim\limits_{n\to\infty}x_{n}$.",
    options=[])

add(num=20, type="essay", score=11, pages=[3], anchor="第(20)题",
    stem=r"设实二次型 $f(x_{1},x_{2},x_{3})=(x_{1}-x_{2}+x_{3})^{2}+(x_{2}+x_{3})^{2}+(x_{1}+ax_{3})^{2}$，"
         r"其中 $a$ 是参数."
         r"（I）求 $f(x_{1},x_{2},x_{3})=0$ 的解；"
         r"（II）求 $f(x_{1},x_{2},x_{3})$ 的规范形.",
    options=[])

add(num=21, type="essay", score=11, pages=[3], anchor="第(21)题",
    stem=r"已知 $a$ 常数，且矩阵 $A=\begin{pmatrix}1&2&a\\ 1&3&0\\ 2&7&-a\end{pmatrix}$ "
         r"可经初等列变换化为矩阵 $B=\begin{pmatrix}1&a&2\\ 0&1&1\\ -1&1&1\end{pmatrix}$."
         r"（I）求 $a$；"
         r"（II）求满足 $AP=B$ 的可逆矩阵 $P$.",
    options=[])

add(num=22, type="essay", score=11, pages=[3, 4], anchor="第(22)题",
    stem=r"设随机变量 $X$ 与 $Y$ 相互独立，$X$ 的概率分为为 $P\{X=1\}=P\{X=-1\}=\dfrac{1}{2}$. $Y$ 服"
         r"从参数为 $\lambda$ 的泊松分布. 令 $Z=XY$."
         r"（I）求 $Cov(X,Z)$；"
         r"（II）求 $Z$ 的概率分布.",
    options=[])

add(num=23, type="essay", score=11, pages=[4], anchor="第(23)题",
    stem=r"设总体 $X$ 的概率密度为 $f(x;\sigma)=\dfrac{1}{2\sigma}e^{-\frac{|x|}{\sigma}}$，$-\infty<x<+\infty$，"
         r"其中 $\sigma\in(0,+\infty)$ 为未知参数. $X_{1},X_{2},\cdots,X_{n}$ 为来自总体 $X$ 的简单随机样本，"
         r"记 $\sigma$ 的最大似然估计量为 $\hat{\sigma}$."
         r"（I）求 $\hat{\sigma}$"
         r"（II）求 $E(\hat{\sigma})$ 和 $D(\hat{\sigma})$.",
    options=[])
