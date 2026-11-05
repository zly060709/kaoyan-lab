# -*- coding: utf-8 -*-
"""2016 数学三 题干视觉转录（照录 data/math3/pages/2016/p1-p4.png）"""

ITEMS = []

def add(**kw):
    ITEMS.append(kw)

# ---------- 一、选择题 1-8（每小题 4 分，共 32 分） ----------
add(num=1, type="single", score=4, pages=[1], anchor="第(1)题",
    stem=r"设函数 $y=f(x)$ 在 $(-\infty,+\infty)$ 内连续，其导函数的图形如图所示，则.",
    options=[r"函数 $f(x)$ 有 2 个极值点，曲线 $y=f(x)$ 有 2 个拐点",
             r"函数 $f(x)$ 有 2 个极值点，曲线 $y=f(x)$ 有 3 个拐点",
             r"函数 $f(x)$ 有 3 个极值点，曲线 $y=f(x)$ 有 1 个拐点",
             r"函数 $f(x)$ 有 3 个极值点，曲线 $y=f(x)$ 有 2 个拐点"])

add(num=2, type="single", score=4, pages=[1], anchor="第(2)题",
    stem=r"已知函数 $f(x,y)=\dfrac{e^{x}}{x-y}$，则.",
    options=[r"$f_{x}'-f_{y}'=0$", r"$f_{x}'+f_{y}'=0$",
             r"$f_{x}'-f_{y}'=f$", r"$f_{x}'+f_{y}'=f$"])

add(num=3, type="single", score=4, pages=[1], anchor="第(3)题",
    stem=r"设 $J_{i}=\displaystyle\iint\limits_{D_{i}}\sqrt[3]{x-y}dxdy(i=1,2,3)$，其中 "
         r"$D_{1}=\left\{(x,y)\middle|0\leqslant x\leqslant1,0\leqslant y\leqslant1\right\}$，"
         r"$D_{2}=\left\{(x,y)\middle|0\leqslant x\leqslant1,0\leqslant y\leqslant\sqrt{x}\right\}$,"
         r"$D_{3}=\left\{(x,y)\middle|0\leqslant x\leqslant1,x^{2}\leqslant y\leqslant1\right\}$,则.",
    options=[r"$J_{1}<J_{2}<J_{3}$", r"$J_{3}<J_{1}<J_{2}$",
             r"$J_{2}<J_{3}<J_{1}$", r"$J_{2}<J_{1}<J_{3}$"])

add(num=4, type="single", score=4, pages=[1], anchor="第(4)题",
    stem=r"级数为 $\displaystyle\sum_{n=1}^{\infty}\Bigl(\dfrac{1}{\sqrt{n}}-\dfrac{1}{\sqrt{n+1}}\Bigr)\sin(n+k)$"
         r"（$k$ 为常数）.",
    options=[r"绝对收敛", r"条件收敛", r"发散", r"收敛性与 $k$ 有关"])

add(num=5, type="single", score=4, pages=[1], anchor="第(5)题",
    stem=r"设 $A$，$B$ 是可逆矩阵，且 $A$ 与 $B$ 相似，则下列结论错误的是.",
    options=[r"$A^{\mathrm{T}}$ 与 $B^{\mathrm{T}}$ 相似", r"$A^{-1}$ 与 $B^{-1}$ 相似",
             r"$A+A^{\mathrm{T}}$ 与 $B+B^{\mathrm{T}}$ 相似", r"$A+A^{-1}$ 与 $B+B^{-1}$ 相似"])

add(num=6, type="single", score=4, pages=[1], anchor="第(6)题",
    stem=r"设二次型 $f(x_{1},x_{2},x_{3})=a(x_{1}^{2}+x_{2}^{2}+x_{3}^{2})+2x_{1}x_{2}+2x_{2}x_{3}+2x_{1}x_{3}$"
         r"的正负惯性指数分别为$1,2$，则.",
    options=[r"$a>1$", r"$a<-2$", r"$-2<a<1$", r"$a=1$或 $a=-2$"])

add(num=7, type="single", score=4, pages=[1, 2], anchor="第(7)题",
    stem=r"设 $A,B$ 为两个随机事件，且 $0<P(A)<1,0<P(B)<1$，如果 $P(A|B)=1$，则.",
    options=[r"$P(\overline{B}|\overline{A})=1$", r"$P(A|\overline{B})=0$",
             r"$P(A\cup B)=1$", r"$P(B|A)=1$"])

add(num=8, type="single", score=4, pages=[2], anchor="第(8)题",
    stem=r"设随机变量 $X$ 与 $Y$ 相互独立，且 $X\sim N(1,2),Y\sim N(1,4)$，则 $D(XY)=$.",
    options=[r"$6$", r"$8$", r"$14$", r"$15$"])

# ---------- 二、填空题 9-14（每小题 4 分，共 24 分） ----------
add(num=9, type="blank", score=4, pages=[2], anchor="第(9)题",
    stem=r"已知函数 $f(x)$ 满足 $\lim\limits_{x\to0}\dfrac{\sqrt{1+f(x)\sin2x}-1}{e^{3x}-1}=2$，"
         r"则 $\lim\limits_{x\to0}f(x)=$________.",
    options=[])

add(num=10, type="blank", score=4, pages=[2], anchor="第(10)题",
    stem=r"极限 $\lim\limits_{n\to\infty}\dfrac{1}{n^{2}}\Bigl(\sin\dfrac{1}{n}+2\sin\dfrac{2}{n}+\cdots+n\sin\dfrac{n}{n}\Bigr)=$________.",
    options=[])

add(num=11, type="blank", score=4, pages=[2], anchor="第(11)题",
    stem=r"设函数 $f(u,v)$ 可微，$z=z(x,y)$ 由方程 $(x+1)z-y^{2}=x^{2}f(x-z,y)$ 确定，则 "
         r"$dz\big|_{(0,1)}=$________.",
    options=[])

add(num=12, type="blank", score=4, pages=[2], anchor="第(12)题",
    stem=r"设 $D=\left\{(x,y)\ \middle|\ \ |x|\leqslant y\leqslant1,-1\leqslant x\leqslant1\right\}$，"
         r"则 $\displaystyle\iint\limits_{D}x^{2}e^{-y^{2}}dxdy=$________.",
    options=[])

add(num=13, type="blank", score=4, pages=[2], anchor="第(13)题",
    stem=r"行列式$\begin{vmatrix}\lambda&-1&0&0\\ 0&\lambda&-1&0\\ 0&0&\lambda&-1\\ 4&3&2&\lambda+1\end{vmatrix}=$_______.",
    options=[])

add(num=14, type="blank", score=4, pages=[2], anchor="第(14)题",
    stem=r"设袋中有红、白、黑球各 1 个，从中有放回地取球，每次取 1 个，直到三种颜色的球"
         r"都取到时停止，则取球次数恰好为 4 的概率为________.",
    options=[])

# ---------- 三、解答题 15-23（共 94 分：15-19 每题 10 分，20-23 每题 11 分） ----------
add(num=15, type="essay", score=10, pages=[2], anchor="第(15)题",
    stem=r"求极限 $\lim\limits_{x\to0}\left(\cos2x+2x\sin x\right)^{\frac{1}{x^{4}}}.$",
    options=[])

add(num=16, type="essay", score=10, pages=[2, 3], anchor="第(16)题",
    stem=r"设某商品的最大需求量为 1200 件，该商品的需求函数 $Q=Q(p)$，需求弹性"
         r"$\eta=\dfrac{p}{120-p}\,(\eta>0)$，$p$ 为单价（万元）."
         r"（I）求需求函数的表达式；"
         r"（II）求 $p=100$ 万元时的边际收益，并说明其经济意义.",
    options=[])

add(num=17, type="essay", score=10, pages=[3], anchor="第(17)题",
    stem=r"设函数 $f(x)=\displaystyle\int_{0}^{1}\left|t^{2}-x^{2}\right|dt(x>0)$，"
         r"求 $f'(x)$ 并求 $f(x)$ 的最小值.",
    options=[])

add(num=18, type="essay", score=10, pages=[3], anchor="第(18)题",
    stem=r"设函数 $f(x)$ 连续，且满足 $\displaystyle\int_{0}^{x}f(x-t)dt=\int_{0}^{x}(x-t)f(t)dt+e^{-x}-1$，"
         r"求 $f(x)$.",
    options=[])

add(num=19, type="essay", score=10, pages=[3], anchor="第(19)题",
    stem=r"求幂级数 $\displaystyle\sum_{n=0}^{\infty}\dfrac{x^{2n+2}}{(n+1)(2n+1)}$ 的收敛域及和函数.",
    options=[])

add(num=20, type="essay", score=11, pages=[3], anchor="第(20)题",
    stem=r"设矩阵 $A=\begin{pmatrix}1&1&1-a\\ 1&0&a\\ a+1&1&a+1\end{pmatrix}$，"
         r"$\boldsymbol{\beta}=\begin{pmatrix}0\\ 1\\ 2a-2\end{pmatrix}$，且方程组 $A\boldsymbol{x}=\boldsymbol{\beta}$ 无解."
         r"（I）求 $a$ 的值；"
         r"（II）求方程组 $A^{\mathrm{T}}A\boldsymbol{x}=A^{\mathrm{T}}\boldsymbol{\beta}$ 的通解.",
    options=[])

add(num=21, type="essay", score=11, pages=[3], anchor="第(21)题",
    stem=r"已知矩阵 $A=\begin{pmatrix}0&-1&1\\ 2&-3&0\\ 0&0&0\end{pmatrix}.$"
         r"（I）求 $A^{99}.$"
         r"（II）设 3 阶矩阵 $B=(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3})$ "
         r"满足 $B^{2}=BA.$ 记 $B^{100}=(\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3}),$"
         r"将 $\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3}$ 分别表示"
         r"为 $\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}$ 的线性组合.",
    options=[])

add(num=22, type="essay", score=11, pages=[3], anchor="第(22)题",
    stem=r"设二维随机变量 $(X,Y)$ 在区域 $D=\left\{(x,y)\middle|0<x<1,x^{2}<y<\sqrt{x}\right\}$ "
         r"上服从均匀分布，令"
         r"$U=\begin{cases}1,&X\leqslant Y.\\ 0,&X>Y.\end{cases}$"
         r"（I）写出 $(X,Y)$ 的概率密度;"
         r"（II）问 $U$ 与 $X$ 是否相互独立？并说明理由;"
         r"（III）求 $Z=U+X$ 的分布函数 $F(z)$.",
    options=[])

add(num=23, type="essay", score=11, pages=[3, 4], anchor="第(23)题",
    stem=r"设总体 $X$ 的概率密度为 $f(x,\theta)=\begin{cases}\dfrac{3x^{2}}{\theta^{3}},&0<x<\theta\\ 0,&\text{其他}\end{cases}$"
         r"其中 $\theta\in(0,+\infty)$ 为未知参数，"
         r"$X_{1},X_{2},X_{3}$ 为来自总体 $X$ 的简单随机样本，令 $T=\max(X_{1},X_{2},X_{3}).$"
         r"（I）求 $T$ 的概率密度;"
         r"（II）确定 $a$，使得 $E(aT)=\theta$.",
    options=[])
