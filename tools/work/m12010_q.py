# -*- coding: utf-8 -*-
"""2010 数学一 题干视觉转录（照录 data/math1.pages/pages/2010/p1-p4.png，解析卷 p5-p12 另见 a1-a3）"""

ITEMS = []

def add(**kw):
    ITEMS.append(kw)

# ---------- 一、选择题：1～8 小题，每小题 4 分，共 32 分。下列每题给出的四个选项中，只有一个选项是符合题目要求的。请将所选项前的字母填在答题纸指定位置上. ----------

add(num=1, type="single", score=4, pages=[1], anchor="第(1)题",
    stem=r"极限 $\lim\limits_{x\to\infty}\left(\dfrac{x^{2}}{(x-a)(x+b)}\right)^{x}=$",
    options=[r"$1$", r"$e$", r"$e^{a-b}$", r"$e^{b-a}$"])

add(num=2, type="single", score=4, pages=[1], anchor="第(2)题",
    stem=r"设函数 $z=z(x,y)$，由方程 $F\left(\dfrac{y}{x},\dfrac{z}{x}\right)=0$ 确定，其中 $F$ 为可微函数，且 $F_{2}'\neq0$，"
         r"则 $x\dfrac{\partial z}{\partial x}+y\dfrac{\partial z}{\partial y}=$",
    options=[r"$x$", r"$z$", r"$-x$", r"$-z$"])

add(num=3, type="single", score=4, pages=[1], anchor="第(3)题",
    stem=r"设 $m,n$ 是正整数, 则反常积分 $\displaystyle\int_{0}^{1}\dfrac{\sqrt[m]{\ln^{2}(1-x)}}{\sqrt[n]{x}}dx$ 的敛散性.",
    options=[r"仅与 $m$ 的取值有关", r"仅与 $n$ 的取值有关",
             r"与 $m,n$ 的取值有关", r"与 $m,n$ 的取值无关"])

add(num=4, type="single", score=4, pages=[1], anchor="第(4)题",
    stem=r"$\lim\limits_{n\to\infty}\sum\limits_{i=1}^{n}\sum\limits_{j=1}^{n}\dfrac{n}{(n+i)(n^{2}+j^{2})}=$",
    options=[
        r"$\int_{0}^{1}dx\int_{0}^{x}\dfrac{1}{(1+x)(1+y^{2})}dy$",
        r"$\int_{0}^{1}dx\int_{0}^{x}\dfrac{1}{(1+x)(1+y)}dy$",
        r"$\int_{0}^{1}dx\int_{0}^{1}\dfrac{1}{(1+x)(1+y)}dy$",
        r"$\int_{0}^{1}dx\int_{0}^{1}\dfrac{1}{(1+x)(1+y^{2})}dy$",
    ])

add(num=5, type="single", score=4, pages=[1], anchor="第(5)题",
    stem=r"设 $\boldsymbol{A}$ 为 $m\times n$ 型矩阵，$\boldsymbol{B}$ 为 $n\times m$ 型矩阵，$\boldsymbol{E}$ 为 $m$ 阶单位矩阵，若 $\boldsymbol{AB}=\boldsymbol{E}$，则.",
    options=[
        r"秩 $r(\boldsymbol{A})=m$，秩 $r(\boldsymbol{B})=m$",
        r"秩 $r(\boldsymbol{A})=m$，秩 $r(\boldsymbol{B})=n$",
        r"秩 $r(\boldsymbol{A})=n$，秩 $r(\boldsymbol{B})=m$",
        r"秩 $r(\boldsymbol{A})=n$，秩 $r(\boldsymbol{B})=n$",
    ])

add(num=6, type="single", score=4, pages=[1, 2], anchor="第(6)题",
    stem=r"设 $\boldsymbol{A}$ 为 4 阶实对称矩阵，且 $\boldsymbol{A}^{2}+\boldsymbol{A}=\boldsymbol{0}$，若 $\boldsymbol{A}$ 的秩为 3，则 $\boldsymbol{A}$ 相似于.",
    options=[
        r"$\begin{pmatrix}1&&&\\&1&&\\&&1&\\&&&0\end{pmatrix}$",
        r"$\begin{pmatrix}1&&&\\&1&&\\&&-1&\\&&&0\end{pmatrix}$",
        r"$\begin{pmatrix}1&&&\\&-1&&\\&&-1&\\&&&0\end{pmatrix}$",
        r"$\begin{pmatrix}-1&&&\\&-1&&\\&&-1&\\&&&0\end{pmatrix}$",
    ])

add(num=7, type="single", score=4, pages=[2], anchor="第(7)题",
    stem=r"设随机变量 $X$ 的分布函数 $F(x)=\begin{cases}0,&x<0\\ \dfrac{1}{2},&0\leqslant x<1\\ 1-e^{-x},&x\geqslant1\end{cases}$，则 $P\{x=1\}=$",
    options=[r"$0$", r"$\dfrac{1}{2}$", r"$\dfrac{1}{2}-e^{-1}$", r"$1-e^{-1}$"])

add(num=8, type="single", score=4, pages=[2], anchor="第(8)题",
    stem=r"设 $f_{1}(x)$ 为标准正态分布的概率密度，$f_{2}(x)$ 为 $[-1,3]$ 上的均匀分布的概率密度，若 "
         r"$f(x)=\begin{cases}af_{1}(x),&x\leqslant0\\ bf_{2}(x),&x>0\end{cases}(a>0,b>0)$ 为概率密度，则 $a,b$ 应满足",
    options=[r"$2a+3b=4$", r"$3a+2b=4$", r"$a+b=1$", r"$a+b=2$"])

# ---------- 二、填空题：9-14 小题，每小题 4 分，共 24 分，请将答案写在答题纸指定位置上. ----------

add(num=9, type="blank", score=4, pages=[2], anchor="第(9)题",
    stem=r"设 $\begin{cases}x=e^{-t}\\ y=\displaystyle\int_{0}^{t}\ln(1+u^{2})du\end{cases}$，求 $\dfrac{d^{2}y}{dx^{2}}\Big|_{t=0}=.$",
    options=[])

add(num=10, type="blank", score=4, pages=[2], anchor="第(10)题",
    stem=r"$\displaystyle\int_{0}^{\pi^{2}}\sqrt{x}\cos\sqrt{x}dx=$________.",
    options=[])

add(num=11, type="blank", score=4, pages=[2], anchor="第(11)题",
    stem=r"已知曲线 $L$ 的方程为 $y=1-|x|,x\in[-1,1]$ 起点是 $(-1,0)$, 终点是 $(1,0)$, 则曲线积分 "
         r"$\displaystyle\int_{L}xy\,dx+x^{2}dy=$________.",
    options=[])

add(num=12, type="blank", score=4, pages=[2], anchor="第(12)题",
    stem=r"设 $\Omega=\{(x,y,z)\,|\,x^{2}+y^{2}\leqslant z\leqslant1\}$, 则 $\Omega$ 的形心的竖坐标 $\bar{z}=$________.",
    options=[])

add(num=13, type="blank", score=4, pages=[2], anchor="第(13)题",
    stem=r"设 $\boldsymbol{\alpha}_{1}=(1,2,-1,0)^{T}$, $\boldsymbol{\alpha}_{2}=(1,1,0,2)^{T}$, $\boldsymbol{\alpha}_{3}=(2,1,1,a)^{T}$ 若由 $\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}$ 生成的向量空间维"
         r"数是 2，则 $a=$________.",
    options=[])

add(num=14, type="blank", score=4, pages=[3], anchor="第(14)题",
    stem=r"设随机变量 $X$ 概率分布为 $p\{X=k\}=\dfrac{C}{k!}, k=0,1,2,\cdots$，则 $EX^{2}=$________.",
    options=[])

# ---------- 三、解答题：15-23 小题，共 94 分.请将解答写在答题纸指定的位置上.解答应写出文字说明、证明过程或演算步骤. ----------

add(num=15, type="essay", score=10, pages=[3], anchor="第(15)题",
    stem=r"（本题满分 10 分）求微分方程 $y''-3y'+2y=2xe^{x}$ 的通解.",
    options=[])

add(num=16, type="essay", score=10, pages=[3], anchor="第(16)题",
    stem=r"（本题满分 10 分）求函数 $f(x)=\displaystyle\int_{1}^{x^{2}}(x^{2}-t)e^{-t^{2}}dt$ 的单调区间与极值.",
    options=[])

add(num=17, type="essay", score=10, pages=[3], anchor="第(17)题",
    stem=r"（本题满分 10 分）"
         r"（I）比较 $\displaystyle\int_{0}^{1}|\ln t|\left[\ln(1+t)\right]^{n}dt$ 与 $\displaystyle\int_{0}^{1}|\ln t|t^{n}dt, n=1,2,\cdots$ 的大小，说明理由；"
         r"（II）设 $M_{n}=\displaystyle\int_{0}^{1}|\ln t|\left[\ln(1+t)\right]^{n}dt (n=1,2,\cdots)$，求极限 $\lim\limits_{n\to\infty}M_{n}$.",
    options=[])

add(num=18, type="essay", score=10, pages=[3], anchor="第(18)题",
    stem=r"（本题满分 10 分）求幂级数 $\sum\limits_{n=1}^{\infty}\dfrac{(-1)^{n-1}}{2n-1}x^{2n}$ 的收敛域及和函数.",
    options=[])

add(num=19, type="essay", score=10, pages=[3], anchor="第(19)题",
    stem=r"（本题满分 10 分）设 $P$ 为椭球面 $S:x^{2}+y^{2}+z^{2}-yz=1$ 上的动点，若 $S$ 在点 $P$ 处的"
         r"切平面与 $xOy$ 面垂直，求点 $P$ 的轨迹 $C$，并计算曲面积分 "
         r"$I=\iint\limits_{\Sigma}\dfrac{(x+\sqrt{3})|y-2z|}{\sqrt{4+y^{2}+z^{2}-4yz}}dS$，其中 $\Sigma$ 是椭球面 $S$ 位于曲线 $C$ 上方的部分.",
    options=[])

add(num=20, type="essay", score=11, pages=[3], anchor="第(20)题",
    stem=r"（本题满分 11 分）设 $\boldsymbol{A}=\begin{pmatrix}\lambda&1&1\\ 0&\lambda-1&0\\ 1&1&\lambda\end{pmatrix}$，$\boldsymbol{b}=\begin{pmatrix}a\\1\\1\end{pmatrix}$，已知线性方程组 $\boldsymbol{Ax}=\boldsymbol{b}$ 存在 2"
         r"个不同的解，"
         r"（I）求 $\lambda$，$a$；（II）求方程组的 $\boldsymbol{Ax}=\boldsymbol{b}$ 通解.",
    options=[])

add(num=21, type="essay", score=11, pages=[3], anchor="第(21)题",
    stem=r"（本题满分 11 分）已知二次型 $f(x_{1},x_{2},x_{3})=\boldsymbol{x}^{T}\boldsymbol{Ax}$ 在正交变换 $\boldsymbol{x}=\boldsymbol{Qy}$ 下的标准形"
         r"为 $y_{1}^{2}+y_{2}^{2}$，且 $\boldsymbol{Q}$ 的第 3 列为 $\left(\dfrac{\sqrt{2}}{2},0,\dfrac{\sqrt{2}}{2}\right)^{T}$"
         r"（I）求矩阵 $\boldsymbol{A}$；"
         r"（II）证明 $\boldsymbol{A}+\boldsymbol{E}$ 为正定矩阵，其中 $\boldsymbol{E}$ 为 3 阶单位矩阵.",
    options=[])

add(num=22, type="essay", score=11, pages=[3, 4], anchor="第(22)题",
    stem=r"（本题满分 11 分）设二维随机变量 $(X,Y)$ 的概率密度为 "
         r"$f(x,y)=Ae^{-2x^{2}+2xy-y^{2}}, -\infty<x<+\infty$，$-\infty<y<+\infty$ "
         r"求常数 A 及条件概率密度 $f_{Y|X}(y|x)$.",
    options=[])

add(num=23, type="essay", score=11, pages=[4], anchor="第(23)题",
    stem=r"（本题满分 11 分设总体 $X$ 的概率分布为 "
         r"$\begin{array}{c|ccc} X & 1 & 2 & 3\\ \hline P & 1-\theta & \theta-\theta^{2} & \theta^{2}\end{array}$ "
         r"其中参数 $\theta\in(0,1)$ 未知，以 $N_{i}$ 表示来自总体 $X$ 的简单随机样本（样本容量为 $n$）中等于 $i$"
         r"的个数 $(i=1,2,3)$. 试求常数 $a_{1},a_{2},a_{3}$，使 $T=\sum\limits_{i=1}^{3}a_{i}N_{i}$ 为 $\theta$ 的无偏估计量，并求 $T$ 的方差.",
    options=[])
