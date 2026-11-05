# -*- coding: utf-8 -*-
"""2014 数学三 题干视觉转录（照录 data/math3/pages/2014/p1-p3.png）"""

ITEMS = []

def add(**kw):
    ITEMS.append(kw)

# ---------- 一、选择题 1~8 小题，每小题 4 分，共 32 分 ----------
add(num=1, type="single", score=4, pages=[1], anchor="第1题",
    stem=r"$\lim\limits_{n\to\infty}a_{n}=a$，且 $a\neq0$，则 $n$ 充分大时.",
    options=[
        r"$|a_{n}|>\dfrac{|a|}{2}$",
        r"$|a_{n}|<\dfrac{|a|}{2}$",
        r"$a_{n}>a-\dfrac{1}{n}$",
        r"$a_{n}<a+\dfrac{1}{n}$",
    ])

add(num=2, type="single", score=4, pages=[1], anchor="第2题",
    stem=r"下列曲线中，具有渐近线的是.",
    options=[
        r"$y=x+\sin x$",
        r"$y=x^{2}+\sin x$",
        r"$y=x+\sin\dfrac{1}{x}$",
        r"$y=x^{2}+\sin\dfrac{1}{x}$",
    ])

add(num=3, type="single", score=4, pages=[1], anchor="第3题",
    stem=r"设 $P(x)=a+bx+cx^{2}+dx^{3}$，当 $x\to0$ 时，若 $P(x)-\tan x$ 是比 $x^{3}$ 高阶无穷小，"
         r"则下列选项错误的是.",
    options=[
        r"$a=0$", r"$b=1$", r"$c=0$", r"$d=\dfrac{1}{6}$",
    ])

add(num=4, type="single", score=4, pages=[1], anchor="第4题",
    stem=r"设函数 $f(x)$ 具有二阶导数，$g(x)=f(0)(1-x)+f(1)x$，则在区间 $[0,1]$ 上.",
    options=[
        r"当 $f'(x)\geqslant0$ 时，$f(x)\geqslant g(x)$",
        r"当 $f'(x)\geqslant0$ 时，$f(x)\leqslant g(x)$",
        r"当 $f''(x)\geqslant0$ 时，$f(x)\geqslant g(x)$",
        r"当 $f''(x)\geqslant0$ 时，$f(x)\leqslant g(x)$",
    ])

add(num=5, type="single", score=4, pages=[1], anchor="第5题",
    stem=r"四阶行列式 $\begin{vmatrix}0&a&b&0\\ a&0&0&b\\ 0&c&d&0\\ c&0&0&d\end{vmatrix}=$.",
    options=[
        r"$(ad-bc)^{2}$",
        r"$-(ad-bc)^{2}$",
        r"$a^{2}d^{2}-b^{2}c^{2}$",
        r"$b^{2}c^{2}-a^{2}d^{2}$",
    ])

add(num=6, type="single", score=4, pages=[1], anchor="第6题",
    stem=r"设 $\boldsymbol{a}_{1},\boldsymbol{a}_{2},\boldsymbol{a}_{3}$ 均为三维向量，则任意常数 $k,l$，"
         r"向量组 $\boldsymbol{a}_{1}+k\boldsymbol{a}_{3},\boldsymbol{a}_{2}+l\boldsymbol{a}_{3}$ 线性无关是向量组"
         r"$\boldsymbol{a}_{1},\boldsymbol{a}_{2},\boldsymbol{a}_{3}$ 线性无关.",
    options=[
        r"必要非充分条件",
        r"充分非必要条件",
        r"充分必要条件",
        r"既非充分又非必要条件",
    ])

add(num=7, type="single", score=4, pages=[1], anchor="第7题",
    stem=r"设随机事件 $A$ 与 $B$ 相互独立，且 $P(B)=0.5$，$P(A-B)=0.3$，则 $P(B-A)=$ .",
    options=[r"$0.1$", r"$0.2$", r"$0.3$", r"$0.4$"])

add(num=8, type="single", score=4, pages=[1, 2], anchor="第8题",
    stem=r"设 $X_{1},X_{2},X_{3}$ 为来自正态总体 $N(0,\sigma^{2})$ 的简单随机样本，"
         r"则统计量 $S=\dfrac{X_{1}-X_{2}}{\sqrt{2}|X_{3}|}$ 服从.",
    options=[
        r"$F(1,1)$", r"$F(2,1)$", r"$t(1)$", r"$t(2)$",
    ])

# ---------- 二、填空题 9~14 小题，每小题 4 分，共 24 分 ----------
add(num=9, type="blank", score=4, pages=[2], anchor="第9题",
    stem=r"设的需求函数为 $Q=40-2p$（$p$ 为商品的价格），则该商品的边际收益为________.",
    options=[])

add(num=10, type="blank", score=4, pages=[2], anchor="第10题",
    stem=r"设 $D$ 是由曲线 $xy+1=0$ 与直线 $y+x=0$ 及 $y=2$ 围成的有界区域，"
         r"则 $D$ 的面积为________.",
    options=[])

add(num=11, type="blank", score=4, pages=[2], anchor="第11题",
    stem=r"设 $\displaystyle\int_{0}^{a}xe^{2x}dx=\dfrac{1}{4}$，则 $a=$________.",
    options=[])

add(num=12, type="blank", score=4, pages=[2], anchor="第12题",
    stem=r"$\displaystyle\int_{0}^{1}dy\int_{y}^{1}\left(\dfrac{e^{x^{2}}}{x}-e^{y^{2}}\right)dx=$________.",
    options=[])

add(num=13, type="blank", score=4, pages=[2], anchor="第13题",
    stem=r"设 $f\left(x_{1},x_{2},x_{3}\right)=x_{1}^{2}-x_{2}^{2}+2ax_{1}x_{3}+4x_{2}x_{3}$ 的负惯性指数为 1，"
         r"则 $a$ 的取值范围为________.",
    options=[])

add(num=14, type="blank", score=4, pages=[2], anchor="第14题",
    stem=r"设总体 $X$ 的概率密度为 $f\left(x,\theta\right)="
         r"\begin{cases}\dfrac{2x}{3\theta^{2}},&\theta<x<2\theta,\\ \theta,&\text{其他}\end{cases}$"
         r"其中 $\theta$ 为未知参数，$X_{1},X_{2},\cdots,X_{n}$ 为来自总体 $X$ 的简单随机变量，"
         r"若 $E\Bigl[c\displaystyle\sum\limits_{n=1}^{\infty}X_{i}^{2}\Bigr]=\theta^{2}$，则 $c=$________.",
    options=[])

# ---------- 三、解答题 15~23 小题，共 94 分（原卷未印逐题分值，按 15-19 各 10 分、20-23 各 11 分计） ----------
add(num=15, type="essay", score=10, pages=[2], anchor="第15题",
    stem=r"求极限 $\lim\limits_{x\to+\infty}\dfrac{\displaystyle\int_{1}^{x}\bigl[t^{2}(e^{\frac{1}{t}}-1)-t\bigr]dt}"
         r"{x^{2}\ln(1+\dfrac{1}{x})}$ .",
    options=[])

add(num=16, type="essay", score=10, pages=[2], anchor="第16题",
    stem=r"设平面区域 $D=\left\{(x,y)\bigr|1\leqslant x^{2}+y^{2}\leqslant4,x\geqslant0,y\geqslant0\right\}$，"
         r"计算 $\displaystyle\iint\limits_{D}\dfrac{x\sin(\pi\sqrt{x^{2}+y^{2}})}{x+y}dxdy$ .",
    options=[])

add(num=17, type="essay", score=10, pages=[2], anchor="第17题",
    stem=r"设 $f(u)$ 具有连续导数，且 $z=f(e^{x}\cos y)$ 满足 "
         r"$\cos y\dfrac{\partial z}{\partial x}-\sin y\dfrac{\partial z}{\partial y}=(4z+e^{x}\cos y)e^{x}$，"
         r"若 $f(0)=0$，求 $f(u)$ 的表达式.",
    options=[])

add(num=18, type="essay", score=10, pages=[2], anchor="第18题",
    stem=r"求 $\displaystyle\sum\limits_{n=0}^{\infty}(n+1)(n+3)x^{n}$ 的收敛域及和函数.",
    options=[])

add(num=19, type="essay", score=10, pages=[2, 3], anchor="第19题",
    stem=r"设函数 $f(x),g(x)$ 在区间 $[a,b]$ 上连续，且 $f(x)$ 单调增加，$0\leqslant g(x)\leqslant1$，证明："
         r"（1）$0\leqslant\displaystyle\int_{a}^{x}g(t)dt\leqslant x-a,x\in[a,b]$."
         r"（2）$\displaystyle\int_{a}^{a+\int_{a}^{b}g(t)dt}f(x)dx\leqslant\int_{a}^{b}f(x)g(x)dx$ .",
    options=[])

add(num=20, type="essay", score=11, pages=[3], anchor="第20题",
    stem=r"设矩阵 $\boldsymbol{A}=\begin{pmatrix}1&-2&3&-4\\ 0&1&-1&1\\ 1&2&0&-3\end{pmatrix}$,"
         r"$\boldsymbol{E}$ 为三阶单位矩阵"
         r"（I）求 $\boldsymbol{Ax}=\boldsymbol{0}$ 的一个基础解系；"
         r"（II）求满足 $\boldsymbol{AB}=\boldsymbol{E}$ 的所有的矩阵 $\boldsymbol{B}$ .",
    options=[])

add(num=21, type="essay", score=11, pages=[3], anchor="第21题",
    stem=r"证明 $n$ 阶矩阵 $\begin{pmatrix}1&1&\cdots&1\\ 1&1&\cdots&1\\ \vdots&\vdots&&\vdots\\ 1&1&\cdots&1\end{pmatrix}$"
         r"与 $\begin{pmatrix}0&0&\cdots&1\\ 0&0&\cdots&2\\ \vdots&\vdots&&\vdots\\ 0&0&\cdots&n\end{pmatrix}$ 相似.",
    options=[])

add(num=22, type="essay", score=11, pages=[3], anchor="第22题",
    stem=r"设随机变量 $X$ 的概率分布为 $P\left\{X=1\right\}=P\left\{X=2\right\}=\dfrac{1}{2}$,"
         r"在给定 $X=i$ 的条件下，随机变量 $Y$ 服从均匀分布 $u\left(0,i\right)\left(i=1,2\right)$，"
         r"（I）求 $Y$ 的分布函数 $F_{Y}\left(y\right)$；"
         r"（II）求 $E\left(Y\right)$.",
    options=[])

add(num=23, type="essay", score=11, pages=[3], anchor="第23题",
    stem=r"设随机变量 $X,Y$ 的概率分布相同，$X$ 的概率分布为 $P\left\{X=0\right\}=\dfrac{1}{3},"
         r"P\left\{X=1\right\}=\dfrac{2}{3}$，且 $X$ 与 $Y$ 的相关系数 $\rho_{XY}=\dfrac{1}{2}$ ."
         r"（I）求 $\left(X,Y\right)$ 的概率分布；"
         r"（II）求 $P\left\{X+Y\leqslant1\right\}$ .",
    options=[])
