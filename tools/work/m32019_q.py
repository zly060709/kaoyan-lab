# -*- coding: utf-8 -*-
"""2019 数学三 题干视觉转录（照录 data/math3/pages/2019/p1-p4.png）"""

ITEMS = []

def add(**kw):
    ITEMS.append(kw)

# ---------- 一、选择题 1-8（每小题 4 分，共 32 分） ----------
add(num=1, type="single", score=4, pages=[1], anchor="第(1)题",
    stem=r"当 $x\to0$ 时，若 $x-\tan x$ 与 $x^{k}$ 是同阶无穷小，则 $k=$（ ）",
    options=[r"$1$", r"$2$", r"$3$", r"$4$"])

add(num=2, type="single", score=4, pages=[1], anchor="第(2)题",
    stem=r"已知方程 $x^{5}-5x+k=0$ 有 3 个不同的实根，则 $k$ 的取值范围为（ ）",
    options=[r"$(-\infty,-4)$", r"$(4,+\infty)$", r"$\{-4,4\}$", r"$(-4,4)$"])

add(num=3, type="single", score=4, pages=[1], anchor="第(3)题",
    stem=r"已知微分方程 $y''+ay'+by=ce^{x}$ 的通解为 $y=(C_{1}+C_{2}x)e^{-x}+e^{x}$，则 $a,b,c$ 依次为（ ）",
    options=[r"$1,0,1.$", r"$1,0,2.$", r"$2,1,3.$", r"$2,1,4.$"])

add(num=4, type="single", score=4, pages=[1], anchor="第(4)题",
    stem=r"若 $\displaystyle\sum\limits_{n=1}^{\infty}nu_{n}$ 绝对收敛，$\displaystyle\sum\limits_{n=1}^{\infty}\dfrac{v_{n}}{n}$ 条件收敛，则（ ）",
    options=[
        r"$\displaystyle\sum\limits_{n=1}^{\infty}u_{n}v_{n}$ 条件收敛",
        r"$\displaystyle\sum\limits_{n=1}^{\infty}u_{n}v_{n}$ 绝对收敛",
        r"$\displaystyle\sum\limits_{n=1}^{\infty}(u_{n}+v_{n})$ 收敛",
        r"$\displaystyle\sum\limits_{n=1}^{\infty}(u_{n}+v_{n})$ 发散",
    ])

add(num=5, type="single", score=4, pages=[1], anchor="第(5)题",
    stem=r"设 $A$ 是四阶矩阵，$A^{*}$ 是 $A$ 的伴随矩阵，若线性方程组 $A\boldsymbol{x}=\boldsymbol{0}$ 的基础解系中只有 2 个向量，"
         r"则 $A^{*}$ 的秩是（ ）",
    options=[r"$0$", r"$1$", r"$2$", r"$3$"])

add(num=6, type="single", score=4, pages=[1], anchor="第(6)题",
    stem=r"设 $A$ 是 3 阶实对称矩阵，$E$ 是阶单位矩阵.若 $A^{2}+A=2E$，且 $|A|=4$，则二次型 $x^{\mathrm{T}}Ax$ 规范形为（ ）",
    options=[
        r"$y_{1}^{2}+y_{2}^{2}+y_{3}^{2}$",
        r"$y_{1}^{2}+y_{2}^{2}-y_{3}^{2}$",
        r"$y_{1}^{2}-y_{2}^{2}-y_{3}^{2}$",
        r"$-y_{1}^{2}-y_{2}^{2}-y_{3}^{2}$",
    ])

add(num=7, type="single", score=4, pages=[1, 2], anchor="第(7)题",
    stem=r"设 $A,B$ 为随机事件，则 $P(A)=P(B)$ 充分必要条件是（ ）",
    options=[
        r"$P(A\cup B)=P(A)+P(B)$",
        r"$P(AB)=P(A)P(B)$",
        r"$P(A\overline{B})=P(B\overline{A})$",
        r"$P(AB)=P(A\overline{B})$",
    ])

add(num=8, type="single", score=4, pages=[2], anchor="第(8)题",
    stem=r"设随机变量 $X$ 和 $Y$ 相互独立，且都服从正态分布 $N(\mu,\sigma^{2})$，则 $P\{|X-Y|<1\}=$（ ）",
    options=[
        r"与 $\mu$ 无关，而与 $\sigma^{2}$ 有关",
        r"与 $\mu$ 有关，而与 $\sigma^{2}$ 无关",
        r"与 $\mu$，$\sigma^{2}$ 都有关",
        r"与 $\mu$，$\sigma^{2}$ 都无关",
    ])

# ---------- 二、填空题 9-14（每小题 4 分，共 24 分） ----------
add(num=9, type="blank", score=4, pages=[2], anchor="第(9)题",
    stem=r"$\lim\limits_{n\to\infty}\Bigl[\dfrac{1}{1\cdot2}+\dfrac{1}{2\cdot3}+\cdots+\dfrac{1}{n(n+1)}\Bigr]^{n}=$________.",
    options=[])

add(num=10, type="blank", score=4, pages=[2], anchor="第(10)题",
    stem=r"曲线 $y=x\sin x+2\cos x\,(-\dfrac{\pi}{2}<x<\dfrac{3\pi}{2})$ 的拐点坐标为________.",
    options=[])

add(num=11, type="blank", score=4, pages=[2], anchor="第(11)题",
    stem=r"已知 $f(x)=\displaystyle\int_{1}^{x}\sqrt{1+t^{4}}\,\mathrm{d}t$，则 $\displaystyle\int_{0}^{1}x^{2}f(x)\mathrm{d}x=$________.",
    options=[])

add(num=12, type="blank", score=4, pages=[2], anchor="第(12)题",
    stem=r"$p_{A},p_{B}$ 分别表示 $A,B$ 两商品的价格，商品 $A$ 需求函数 $Q_{A}=500-p_{A}^{2}-p_{A}p_{B}+2p_{B}^{2}$，"
         r"当 $p_{A}=10$，$p_{B}=20$ 时，求商品 $A$ 对自身价格的需求弹性 $\eta_{AA}(\eta_{AA}>0)=$________.",
    options=[])

add(num=13, type="blank", score=4, pages=[2], anchor="第(13)题",
    stem=r"$A=\begin{pmatrix}1&0&-1\\ 1&1&-1\\ 0&1&a^{2}-1\end{pmatrix}$，$\boldsymbol{b}=\begin{pmatrix}0\\ 1\\ a\end{pmatrix}$，"
         r"$A\boldsymbol{x}=\boldsymbol{b}$ 有无穷多解，求 $a=$________.",
    options=[])

add(num=14, type="blank", score=4, pages=[2], anchor="第(14)题",
    stem=r"设随机变量 $X$ 的概率密度为 $f(x)=\begin{cases}\dfrac{x}{2},&0<x<2,\\ 0,&\text{其他},\end{cases}$ "
         r"$F(x)$ 为 $X$ 的分布函数，$EX$ 为 $X$ 的数学期望，则 $P\{F(X)>EX-1\}=$________.",
    options=[])

# ---------- 三、解答题 15-23（共 94 分） ----------
add(num=15, type="essay", score=10, pages=[2], anchor="第(15)题",
    stem=r"已知 $f(x)=\begin{cases}x^{2x},&x>0,\\ xe^{x}+1,&x\leqslant0,\end{cases}$ 求 $f'(x)$，并求 $f(x)$ 的极值.",
    options=[])

add(num=16, type="essay", score=10, pages=[2], anchor="第(16)题",
    stem=r"已知 $f(u,v)$ 具有二阶连续偏导数，且 $g(x,y)=xy-f(x+y,x-y)$，"
         r"求 $\dfrac{\partial^{2}g}{\partial x^{2}}+\dfrac{\partial^{2}g}{\partial x\partial y}+\dfrac{\partial^{2}g}{\partial y^{2}}$.",
    options=[])

add(num=17, type="essay", score=10, pages=[2, 3], anchor="第(17)题",
    stem=r"$y=y(x)$ 是微分方程 $y'-xy=\dfrac{1}{2\sqrt{x}}e^{\frac{x^{2}}{2}}$ 满足条件 $y(1)=\sqrt{e}$ 的特解."
         r"（I）求 $y(x)$；"
         r"（II）设平面区域 $D=\{(x,y)|1\leqslant x\leqslant2,0\leqslant y\leqslant y(x)\}$，求 $D$ 绕 $x$ 轴旋转所得旋转体的体积.",
    options=[])

add(num=18, type="essay", score=10, pages=[3], anchor="第(18)题",
    stem=r"求曲线 $y=e^{-x}\sin x\,(x\geqslant0)$ 与 $x$ 轴之间图形的面积.",
    options=[])

add(num=19, type="essay", score=10, pages=[3], anchor="第(19)题",
    stem=r"设 $a_{n}=\displaystyle\int_{0}^{1}x^{n}\sqrt{1-x^{2}}\,\mathrm{d}x\,(n=0,1,2,\cdots)$."
         r"（I）证明：数列 $\{a_{n}\}$ 单调递减，且 $a_{n}=\dfrac{n-1}{n+2}a_{n-2}\,(n=2,3,\cdots)$."
         r"（II）求 $\lim\limits_{n\to\infty}\dfrac{a_{n}}{a_{n-1}}$",
    options=[])

add(num=20, type="essay", score=11, pages=[3], anchor="第(20)题",
    stem=r"已知向量组 "
         r"$\mathrm{I}:\boldsymbol{\alpha}_{1}=\begin{pmatrix}1\\ 1\\ 4\end{pmatrix}$，"
         r"$\boldsymbol{\alpha}_{2}=\begin{pmatrix}1\\ 0\\ 4\end{pmatrix}$，"
         r"$\boldsymbol{\alpha}_{3}=\begin{pmatrix}1\\ 2\\ a^{2}+3\end{pmatrix}$，"
         r"$\mathrm{II}:\boldsymbol{\beta}_{1}=\begin{pmatrix}1\\ 1\\ a+3\end{pmatrix}$，"
         r"$\boldsymbol{\beta}_{2}=\begin{pmatrix}0\\ 2\\ 1-a\end{pmatrix}$，"
         r"$\boldsymbol{\beta}_{3}=\begin{pmatrix}1\\ 3\\ a^{2}+3\end{pmatrix}$，若向量组 $\mathrm{I}$ 和向量组 $\mathrm{II}$ 等价，"
         r"求 $a$ 的取值，并将 $\boldsymbol{\beta}_{3}$ 用 $\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}$ 线性表示.",
    options=[])

add(num=21, type="essay", score=11, pages=[3], anchor="第(21)题",
    stem=r"已知矩阵 $A=\begin{pmatrix}-2&-2&1\\ 2&x&-2\\ 0&0&-2\end{pmatrix}$ 与 $B=\begin{pmatrix}2&1&0\\ 0&-1&0\\ 0&0&y\end{pmatrix}$ 相似，"
         r"（I）求 $x,y$；"
         r"（II）求可逆矩阵 $P$,使得 $P^{-1}AP=B$",
    options=[])

add(num=22, type="essay", score=11, pages=[3], anchor="第(22)题",
    stem=r"设随机变量 $X$ 与 $Y$ 相互独立，$X$ 服从参数为 1 的指数分布，$Y$ 的概率分布为 "
         r"$P(Y=-1)=p$，$P(Y=1)=1-p$，$(0<p<1)$，令 $Z=XY$."
         r"（I）求 $Z$ 的概率密度；"
         r"（II）$p$ 为何值时，$X$ 与 $Z$ 不相关？"
         r"（III）$X$ 与 $Z$ 是否相互独立？",
    options=[])

add(num=23, type="essay", score=11, pages=[3, 4], anchor="第(23)题",
    stem=r"设总体 $X$ 的概率密度为 "
         r"$f(x;\sigma^{2})=\begin{cases}\dfrac{A}{\sigma}e^{-\frac{(x-\mu)^{2}}{2\sigma^{2}}},&x\geqslant\mu\\ 0,&x<\mu\end{cases}$ "
         r"$\mu$ 是已知参数，$\sigma>0$ 是未知参数，$A$ 是常数.$X_{1},X_{2},\cdots,X_{n}$ 是来自总体 $X$ 简单随机样本."
         r"（I）求 $A$；"
         r"（II）求 $\sigma^{2}$ 的最大似然估计量.",
    options=[])
