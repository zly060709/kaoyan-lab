# -*- coding: utf-8 -*-
"""2009 数学三 题干视觉转录（照录 data/math3/pages/2009/p1-p4.png）"""

ITEMS = []

def add(**kw):
    ITEMS.append(kw)

# ---------- 一、选择题 1-8（每小题 4 分，共 32 分） ----------
add(num=1, type="single", score=4, pages=[1], anchor="第(1)题",
    stem=r"函数 $f(x)=\dfrac{x-x^{3}}{\sin\pi x}$ 的可去间断点的个数为（ ）",
    options=[r"$1$", r"$2$", r"$3$", r"无穷多个"])

add(num=2, type="single", score=4, pages=[1], anchor="第(2)题",
    stem=r"当 $x\to0$ 时，$f(x)=x-\sin ax$ 与 $g(x)=x^{2}\ln(1-bx)$ 等价无穷小，则（ ）",
    options=[
        r"$a=1,b=-\dfrac{1}{6}$",
        r"$a=1,b=\dfrac{1}{6}$",
        r"$a=-1,b=-\dfrac{1}{6}$",
        r"$a=-1,b=\dfrac{1}{6}$",
    ])

add(num=3, type="single", score=4, pages=[1], anchor="第(3)题",
    stem=r"使不等式 $\displaystyle\int_{1}^{x}\dfrac{\sin t}{t}dt>\ln x$ 成立的 $x$ 的范围是（ ）",
    options=[
        r"$(0,1)$",
        r"$\left(1,\dfrac{\pi}{2}\right)$",
        r"$\left(\dfrac{\pi}{2},\pi\right)$",
        r"$(\pi,+\infty)$",
    ])

add(num=4, type="single", score=4, pages=[1, 2], anchor="第(4)题",
    stem=r"设函数 $y=f(x)$ 在区间 $[-1,3]$ 上的图形如图所示，则函数 $F(x)=\displaystyle\int_{0}^{x}f(t)dt$ 为（ ）",
    options=[
        r"【图】选项（A）的 $F(x)$ 图形（原卷 p1，图形描述见转录 notes）",
        r"【图】选项（B）的 $F(x)$ 图形（原卷 p1，图形描述见转录 notes）",
        r"【图】选项（C）的 $F(x)$ 图形（原卷 p2，图形描述见转录 notes）",
        r"【图】选项（D）的 $F(x)$ 图形（原卷 p2，图形描述见转录 notes）",
    ])

add(num=5, type="single", score=4, pages=[2], anchor="第(5)题",
    stem=r"设 $\boldsymbol{A}$、$\boldsymbol{B}$ 均为 2 阶矩阵，$\boldsymbol{A}^{*}$,$\boldsymbol{B}^{*}$ 分别为 $\boldsymbol{A}$、$\boldsymbol{B}$ 的伴随矩阵. "
         r"若 $|\boldsymbol{A}|=2$，$|\boldsymbol{B}|=3$，则分块矩阵 $\begin{pmatrix}\boldsymbol{O}&\boldsymbol{A}\\\boldsymbol{B}&\boldsymbol{O}\end{pmatrix}$ 的伴随矩阵为（ ）",
    options=[
        r"$\begin{pmatrix}\boldsymbol{O}&3\boldsymbol{B}^{*}\\2\boldsymbol{A}^{*}&\boldsymbol{O}\end{pmatrix}$",
        r"$\begin{pmatrix}\boldsymbol{O}&2\boldsymbol{B}^{*}\\3\boldsymbol{A}^{*}&\boldsymbol{O}\end{pmatrix}$",
        r"$\begin{pmatrix}\boldsymbol{O}&3\boldsymbol{A}^{*}\\2\boldsymbol{B}^{*}&\boldsymbol{O}\end{pmatrix}$",
        r"$\begin{pmatrix}\boldsymbol{O}&2\boldsymbol{A}^{*}\\3\boldsymbol{B}^{*}&\boldsymbol{O}\end{pmatrix}$",
    ])

add(num=6, type="single", score=4, pages=[2], anchor="第(6)题",
    stem=r"设 $\boldsymbol{A}$，$\boldsymbol{P}$ 均为 3 阶矩阵，$\boldsymbol{P}^{T}$ 为 $\boldsymbol{P}$ 的转置矩阵，"
         r"且 $\boldsymbol{P}^{T}\boldsymbol{A}\boldsymbol{P}=\begin{pmatrix}1&0&0\\0&1&0\\0&0&2\end{pmatrix}$，若 "
         r"$\boldsymbol{P}=(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}),"
         r"\boldsymbol{Q}=(\boldsymbol{\alpha}_{1}+\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3})$，"
         r"则 $\boldsymbol{Q}^{T}\boldsymbol{A}\boldsymbol{Q}$ 为（ ）",
    options=[
        r"$\begin{pmatrix}2&1&0\\1&1&0\\0&0&2\end{pmatrix}$",
        r"$\begin{pmatrix}1&1&0\\1&2&0\\0&0&2\end{pmatrix}$",
        r"$\begin{pmatrix}2&0&0\\0&1&0\\0&0&2\end{pmatrix}$",
        r"$\begin{pmatrix}1&0&0\\0&2&0\\0&0&2\end{pmatrix}$",
    ])

add(num=7, type="single", score=4, pages=[2], anchor="第(7)题",
    stem=r"设事件 $A$ 与事件 $B$ 互不相容，则（ ）",
    options=[
        r"$P(\overline{A}\,\overline{B})=0$",
        r"$P(AB)=P(A)P(B)$",
        r"$P(A)=1-P(B)$",
        r"$P(\overline{A}\cup\overline{B})=1$",
    ])

add(num=8, type="single", score=4, pages=[2], anchor="第(8)题",
    stem=r"设随机变量 $X$ 与 $Y$ 相互独立，且 $X$ 服从标准正态分布 $N(0,1)$,$Y$ 的概率分布为 "
         r"$P\{Y=0\}=P\{Y=1\}=\dfrac{1}{2}$，记 $F_{z}(z)$ 为随机变量 $Z=XY$ 的分布函数，"
         r"则函数 $F_{z}(z)$ 的间断点个数为（ ）",
    options=[r"$0$", r"$1$", r"$2$", r"$3$"])

# ---------- 二、填空题 9-14（每小题 4 分，共 24 分） ----------
add(num=9, type="blank", score=4, pages=[3], anchor="第(9)题",
    stem=r"$\lim\limits_{x\to0}\dfrac{e-e^{\cos x}}{\sqrt[3]{1+x^{2}}-1}=$________.",
    options=[])

add(num=10, type="blank", score=4, pages=[3], anchor="第(10)题",
    stem=r"设 $z=(x+e^{y})^{x}$，则 $\dfrac{\partial z}{\partial x}\Big|_{(1,0)}=$________.",
    options=[])

add(num=11, type="blank", score=4, pages=[3], anchor="第(11)题",
    stem=r"幂级数 $\displaystyle\sum_{n=1}^{\infty}\dfrac{e^{n}-(-1)^{n}}{n^{2}}x^{n}$ 的收敛半径为________.",
    options=[])

add(num=12, type="blank", score=4, pages=[3], anchor="第(12)题",
    stem=r"设某产品的需求函数为 $Q=Q(P)$，其对应价格 $P$ 的弹性 $\varepsilon=0.2$，则当需求量为 10000 "
         r"件时，价格增加 1 元会使产品收益增加________元.",
    options=[])

add(num=13, type="blank", score=4, pages=[3], anchor="第(13)题",
    stem=r"设 $\boldsymbol{\alpha}=(1,1,1)^{T}$,$\boldsymbol{\beta}=(1,0,k)^{T}$，若矩阵 $\boldsymbol{\alpha}\boldsymbol{\beta}^{T}$ "
         r"相似于 $\begin{pmatrix}3&0&0\\0&0&0\\0&0&0\end{pmatrix}$，则 $k=$________.",
    options=[])

add(num=14, type="blank", score=4, pages=[3], anchor="第(14)题",
    stem=r"设 $X_{1},X_{2},\cdots,X_{m}$ 为来自二项分布总体 $B(n,p)$ 的简单随机样本，$\overline{X}$ 和 $S^{2}$ 分别为样本 "
         r"均值和样本方差. 记统计量 $T=\overline{X}-S^{2}$，则 $ET=$________.",
    options=[])

# ---------- 三、解答题 15-23（共 94 分） ----------
add(num=15, type="essay", score=9, pages=[3], anchor="第(15)题",
    stem=r"（本题满分为 9 分）求二元函数 $f(x,y)=x^{2}(2+y^{2})+y\ln y$ 极值.",
    options=[])

add(num=16, type="essay", score=10, pages=[3], anchor="第(16)题",
    stem=r"（本题满分 10 分）计算不定积分 $\displaystyle\int\ln\Bigl(1+\sqrt{\dfrac{1+x}{x}}\Bigr)dx\,(x>0)$.",
    options=[])

add(num=17, type="essay", score=10, pages=[3], anchor="第(17)题",
    stem=r"（本题满分 10 分）计算二重积分 $\displaystyle\iint\limits_{D}(x-y)dxdy$，其中 "
         r"$D=\{(x,y)\,|\,(x-1)^{2}+(y-1)^{2}\leqslant2,\ y\geqslant x\}$. ",
    options=[])

add(num=18, type="essay", score=11, pages=[3], anchor="第(18)题",
    stem=r"（本题满分 11 分）(I) 证明拉格朗日中值定理：若函数 $f(x)$ 在 $[a,b]$ 上连续，在 $(a,b)$ "
         r"可导，则存在 $\zeta\in(a,b)$，使得 $f(b)-f(a)=f'(\zeta)(b-a)$. "
         r"（II)证明：若函数 $f(x)$ 在 $x=0$ 处连续，在 $(0,\delta)(\delta>0)$ 内可导，"
         r"且 $\lim\limits_{x\to0^{+}}f'(x)=A$ 则 $f'_{+}(0)$ 存在，且 $f'_{+}(0)=A$. ",
    options=[])

add(num=19, type="essay", score=10, pages=[4], anchor="第(19)题",
    stem=r"（本题满分 10 分）设曲线 $y=f(x)$，其中 $y=f(x)$ 是可导函数，且 $f(x)>0$，已知 "
         r"曲线 $y=f(x)$ 与直线 $y=0,x=1$ 及 $x=t\,(t>1)$ 所围成的曲边梯形，绕 $x$ 轴旋转一周所得的 "
         r"立体体积值是曲边梯形面积值的 $\pi t$ 倍，求该曲线方程.",
    options=[])

add(num=20, type="essay", score=11, pages=[4], anchor="第(20)题",
    stem=r"（本题满分 11 分）"
         r"设 $\boldsymbol{A}=\begin{pmatrix}1&-1&-1\\-1&1&1\\0&-4&-2\end{pmatrix}$,"
         r"$\boldsymbol{\zeta}_{1}=\begin{pmatrix}-1\\1\\-2\end{pmatrix}$"
         r"（I）求满足 $\boldsymbol{A}\boldsymbol{\zeta}_{2}=\boldsymbol{\zeta}_{1},\boldsymbol{A}^{2}\boldsymbol{\zeta}_{3}=\boldsymbol{\zeta}_{1}$ "
         r"的所有向量 $\boldsymbol{\zeta}_{2},\boldsymbol{\zeta}_{3}$；"
         r"（II）对（I）中的任一向量 $\boldsymbol{\zeta}_{2},\boldsymbol{\zeta}_{3}$，证明："
         r"$\boldsymbol{\zeta}_{1},\boldsymbol{\zeta}_{2},\boldsymbol{\zeta}_{3}$ 线性无关.",
    options=[])

add(num=21, type="essay", score=11, pages=[4], anchor="第(21)题",
    stem=r"（本题满分 11 分）"
         r"设二次型 $f(x_{1},x_{2},x_{3})=ax_{1}^{2}+ax_{2}^{2}+(a-1)x_{3}^{2}+2x_{1}x_{3}-2x_{2}x_{3}$"
         r"（I）求二次型 $f$ 的矩阵的所有特征值；"
         r"（II）若二次型 $f$ 的规范形为 $y_{1}^{2}+y_{2}^{2}$，求 $a$ 的值.",
    options=[])

add(num=22, type="essay", score=11, pages=[4], anchor="第(22)题",
    stem=r"（本题满分 11 分）"
         r"设二维随机变量 $(X,Y)$ 的概率密度为 "
         r"$f(x,y)=\begin{cases}e^{-x}&0<y<x\\ 0&\text{其他}\end{cases}$"
         r"（I）求条件概率密度 $f_{Y|X}(y|x)$. "
         r"（II）求条件概率 $P=[X\leqslant1|Y\leqslant1]$. ",
    options=[])

add(num=23, type="essay", score=11, pages=[4], anchor="第(23)题",
    stem=r"（本题满分 11 分）"
         r"袋中有一个红球，两个黑球，三个白球，现有放回的从袋中取两次，每次取一球，以 $X$，"
         r"$Y$，$Z$ 分别表示两次取球的红、黑、白球的个数. "
         r"（I）求 $P\{X=1|Z=0\}$.（II）求二维随机变量 $(X,Y)$ 的概率分布.",
    options=[])
