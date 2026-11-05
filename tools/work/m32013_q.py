# -*- coding: utf-8 -*-
"""2013 数学三 题干视觉转录（照录 data/math3/pages/2013/p1-p4.png）"""

ITEMS = []

def add(**kw):
    ITEMS.append(kw)

# ---------- 一、选择题 1-8（每小题 4 分，共 32 分） ----------
add(num=1, type="single", score=4, pages=[1], anchor="第(1)题",
    stem=r"当 $x\to0$ 时，用“$o(x)$”表示比 $x$ 高阶的无穷小，则下列式子中错误的是.",
    options=[
        r"$x\cdot o(x^{2})=o(x^{3})$",
        r"$o(x)\cdot o(x^{2})=o(x^{3})$",
        r"$o(x^{2})+o(x^{2})=o(x^{2})$",
        r"$o(x)+o(x^{2})=o(x^{2})$",
    ])

add(num=2, type="single", score=4, pages=[1], anchor="第(2)题",
    stem=r"函数 $f(x)=\dfrac{|x|^{x}-1}{x(x+1)\ln|x|}$ 的可去间断点的个数为.",
    options=[r"$0$", r"$1$", r"$2$", r"$3$"])

add(num=3, type="single", score=4, pages=[1], anchor="第(3)题",
    stem=r"设 $D_{k}$ 是圆域 $D=\left\{(x,y)\,|\,x^{2}+y^{2}\leqslant1\right\}$ 位于第 $k$ 象限的部分，"
         r"记 $I_{k}=\iint\limits_{D_{k}}(y-x)dxdy$ $(k=1,2,3,4)$，则.",
    options=[r"$I_{1}>0$", r"$I_{2}>0$", r"$I_{3}>0$", r"$I_{4}>0$"])

add(num=4, type="single", score=4, pages=[1], anchor="第(4)题",
    stem=r"设 $\{a_{n}\}$ 为正项数列，下列选项正确的是.",
    options=[
        r"若 $a_{n}>a_{n+1}$，则 $\sum\limits_{n=1}^{\infty}(-1)^{n-1}a_{n}$ 收敛",
        r"若 $\sum\limits_{n=1}^{\infty}(-1)^{n-1}a_{n}$ 收敛，则 $a_{n}>a_{n+1}$",
        r"若 $\sum\limits_{n=1}^{\infty}a_{n}$ 收敛，则存在常数 $p>1$，使 $\lim\limits_{x\to\infty}n^{p}a_{n}$ 存在",
        r"若存在常数 $P>1$，使 $\lim\limits_{n\to\infty}n^{P}a_{n}$ 存在，则 $\sum\limits_{n=1}^{\infty}a_{n}$ 收敛",
    ])

add(num=5, type="single", score=4, pages=[1, 2], anchor="第(5)题",
    stem=r"设 $A,B,C$ 均为 $n$ 阶矩阵，若 $AB=C$，且 $B$ 可逆，则",
    options=[
        r"矩阵 $C$ 行向量组与 $A$ 的行向量组等价",
        r"矩阵 $C$ 列向量组与 $A$ 的列向量组等价",
        r"矩阵 $C$ 行向量组与 $B$ 的行向量组等价",
        r"矩阵 $C$ 列向量组与 $B$ 的列向量组等价",
    ])

add(num=6, type="single", score=4, pages=[2], anchor="第(6)题",
    stem=r"矩阵 $\begin{pmatrix}1&a&1\\ a&b&a\\ 1&a&1\end{pmatrix}$ 与 $\begin{pmatrix}2&0&0\\ 0&b&0\\ 0&0&0\end{pmatrix}$"
         r"相似的充分必要条件为:",
    options=[
        r"$a=0,b=2$",
        r"$a=0,b$ 为任意实数",
        r"$a=2,b=0$",
        r"$b=0,a$ 为任意实数",
    ])

add(num=7, type="single", score=4, pages=[2], anchor="第(7)题",
    stem=r"设 $X_{1},X_{2},X_{3}$ 是随机变量，且 $X_{1}\sim N(0,1)$, $X_{2}\sim N(0,2^{2})$, $X_{3}\sim N(5,3^{2})$，"
         r"$p_{i}=P(-2\leqslant X_{i}\leqslant2)(i=1,2,3)$，则.",
    options=[
        r"$p_{1}>p_{2}>p_{3}$",
        r"$p_{2}>p_{1}>p_{3}$",
        r"$p_{3}>p_{1}>p_{2}$",
        r"$p_{1}>p_{3}>p_{2}$",
    ])

add(num=8, type="single", score=4, pages=[2], anchor="第(8)题",
    stem=r"设随机变量 $X$ 和 $Y$ 相互独立，则 $X$ 和 $Y$ 的概率分布分别为"
         r"$\begin{array}{|c|cccc|}\hline X&0&1&2&3\\\hline P&\dfrac{1}{2}&\dfrac{1}{4}&\dfrac{1}{8}&\dfrac{1}{8}\\\hline\end{array}$"
         r"$\begin{array}{|c|ccc|}\hline Y&-1&0&1\\\hline P&\dfrac{1}{3}&\dfrac{1}{3}&\dfrac{1}{3}\\\hline\end{array}$"
         r"则 $P\{X+Y=2\}=$",
    options=[
        r"$\dfrac{1}{12}$",
        r"$\dfrac{1}{8}$",
        r"$\dfrac{1}{6}$",
        r"$-\dfrac{1}{2}$",
    ])

# ---------- 二、填空题 9-14（每小题 4 分，共 24 分） ----------
add(num=9, type="blank", score=4, pages=[2], anchor="第(9)题",
    stem=r"设曲线 $y=f(x)$ 与 $y=x^{2}-x$ 在点 $(1,0)$ 处有公共切线，"
         r"则 $\lim\limits_{n\to\infty}nf\left(\dfrac{n}{n+2}\right)=$________.",
    options=[])

add(num=10, type="blank", score=4, pages=[2], anchor="第(10)题",
    stem=r"设函数 $z=z(x,y)$ 由方程 $(z+y)^{x}=xy$ 确定，"
         r"则 $\dfrac{\partial z}{\partial x}\Big|_{(1,2)}=$________.",
    options=[])

add(num=11, type="blank", score=4, pages=[2], anchor="第(11)题",
    stem=r"$\displaystyle\int_{1}^{+\infty}\dfrac{\ln x}{(1+x)^{2}}dx=$________.",
    options=[])

add(num=12, type="blank", score=4, pages=[2], anchor="第(12)题",
    stem=r"微分方程 $y''-y'+\dfrac{1}{4}y=0$ 的通解为 $y=$________.",
    options=[])

add(num=13, type="blank", score=4, pages=[3], anchor="第(13)题",
    stem=r"设 $A=(a_{ij})$ 是 3 阶非零矩阵，$|A|$ 为 $A$ 的行列式，$A_{ij}$ 为 $a_{ij}$ 的代数余子式，"
         r"若 $a_{ij}+A_{ij}=0(i,j=1,2,3)$，则 $|A|=$________.",
    options=[])

add(num=14, type="blank", score=4, pages=[3], anchor="第(14)题",
    stem=r"设随机变量 $X$ 服从标准正态分布 $N(0,1)$，则 $E\left(Xe^{2X}\right)=$________.",
    options=[])

# ---------- 三、解答题 15-23（共 94 分，每题括注“本题满分 X 分”） ----------
add(num=15, type="essay", score=10, pages=[3], anchor="第(15)题",
    stem=r"当 $x\to0$ 时，$1-\cos x\cos 2x\cos 3x$ 与 $ax^{n}$ 为等价无穷小，求 $n$ 与 $a$ 的值.",
    options=[])

add(num=16, type="essay", score=10, pages=[3], anchor="第(16)题",
    stem=r"设 D 是由曲线 $y=x^{\frac{1}{3}}$，直线 $x=a(a>0)$ 及 $x$ 轴所围成的平面图形，"
         r"$V_{x},V_{y}$ 分别是 D 绕 $x$ 轴，$y$ 轴旋转一周所得旋转体的体积. 若 $V_{y}=10V_{x}$，求 $a$ 的值.",
    options=[])

add(num=17, type="essay", score=10, pages=[3], anchor="第(17)题",
    stem=r"设平面区域 $D$ 由直线 $x=3y$，$y=3x$ 及 $x+y=8$ 围成，计算 $\iint\limits_{D}x^{2}dxdy$.",
    options=[])

add(num=18, type="essay", score=10, pages=[3], anchor="第(18)题",
    stem=r"设生产某产品的固定成本为 60000 元，可变成本为 20 元/件，价格函数为 $p=60-\dfrac{Q}{1000}$"
         r"（$p$ 是单价，单位：元，$Q$ 是销量，单位：件），已知产销平衡，求："
         r"（I）该商品的边际利润."
         r"（II）当 $p=50$ 时的边际利润，并解释其经济意义."
         r"（III）使得利润最大的定价 $p$.",
    options=[])

add(num=19, type="essay", score=10, pages=[3], anchor="第(19)题",
    stem=r"设函数 $f(x)$ 在 $[0,+\infty)$ 上可导，$f(0)=0$ 且 $\lim\limits_{x\to\infty}f(x)=2$，证明"
         r"（I）存在 $a>0$，使得 $f(a)=1$;"
         r"（II）对（I）中的 $a$，存在 $\xi\in(0,a)$，使得 $f'(\xi)=\dfrac{1}{a}$.",
    options=[])

add(num=20, type="essay", score=11, pages=[3, 4], anchor="第(20)题",
    stem=r"设 $A=\begin{pmatrix}1&a\\ 1&0\end{pmatrix}$，$B=\begin{pmatrix}0&1\\ 1&b\end{pmatrix}$，"
         r"当 $a$，$b$ 为何值时，存在矩阵 $C$ 使得 $AC-CA=B$，并求所有矩阵 $C$.",
    options=[])

add(num=21, type="essay", score=11, pages=[4], anchor="第(21)题",
    stem=r"设二次型 $f(x_{1},x_{2},x_{3})=2(a_{1}x_{1}+a_{2}x_{2}+a_{3}x_{3})^{2}+(b_{1}x_{1}+b_{2}x_{2}+b_{3}x_{3})^{2}$，"
         r"记 $\boldsymbol{\alpha}=\begin{pmatrix}a_{1}\\ a_{2}\\ a_{3}\end{pmatrix}$，$\boldsymbol{\beta}=\begin{pmatrix}b_{1}\\ b_{2}\\ b_{3}\end{pmatrix}$."
         r"（I）证明二次型 $f$ 对应的矩阵为 $2\boldsymbol{\alpha}\boldsymbol{\alpha}^{T}+\boldsymbol{\beta}\boldsymbol{\beta}^{T}$."
         r"（II）若 $\boldsymbol{\alpha},\boldsymbol{\beta}$ 正交且均为单位向量，"
         r"证明 $f$ 在正交变换下的标准形为 $2y_{1}^{2}+y_{2}^{2}$.",
    options=[])

add(num=22, type="essay", score=11, pages=[4], anchor="第(22)题",
    stem=r"设 $(X,Y)$ 是二维随机变量，$X$ 的边缘概率密度为 "
         r"$f_{X}(x)=\begin{cases}3x^{2},&0<x<1\\ 0,&\text{其他}\end{cases}$，"
         r"在给定 $X=x(0<x<1)$ 的条件下，$Y$ 的条件概率密度为 "
         r"$f_{Y|X}(y|x)=\begin{cases}\dfrac{3y^{2}}{x^{3}},&0<y<x\\ 0,&\text{其他}\end{cases}$."
         r"（I）求 $(X,Y)$ 的概率密度 $f(x,y)$;"
         r"（II）求 $Y$ 的边缘概率密度 $f_{Y}(y)$;"
         r"（III）求 $P\{X>2Y\}$.",
    options=[])

add(num=23, type="essay", score=11, pages=[4], anchor="第(23)题",
    stem=r"设总体 $X$ 的概率密度为 "
         r"$f(x;\theta)=\begin{cases}\dfrac{\theta^{2}}{x^{3}}e^{-\frac{\theta}{x}},&x>0\\ 0,&\text{其他}\end{cases}$，"
         r"其中 $\theta$ 为位置参数且大于零，$X_{1},X_{2},\cdots X_{n}$ 为来自总体 $X$ 的简单随机样本."
         r"（I）求 $\theta$ 的矩估计量;"
         r"（II）求 $\theta$ 的最大似然估计.",
    options=[])
