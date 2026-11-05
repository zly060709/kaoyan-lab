# -*- coding: utf-8 -*-
"""2012 数学一 题干视觉转录（照录 data/math1.pages/pages/2012/p1-p4.png，解析卷 p5-p13 另见 a1-a3）
原卷解答题 15~23 题干均无"（本题满分 x 分）"行，分值按说明行口径分配（15-19 各 10 分、20-23 各 11 分）."""

ITEMS = []

def add(**kw):
    ITEMS.append(kw)

# ---------- 一、选择题：1～8 小题，每小题 4 分，共 32 分．下列每题给出的四个选项中，只有一个选项是符合题目要求的．请将所选项前的字母填在答题纸指定位置上. ----------

add(num=1, type="single", score=4, pages=[1], anchor="第(1)题",
    stem=r"曲线 $y=\dfrac{x^{2}+x}{x^{2}-1}$ 的渐近线条数为（　　）.",
    options=[r"0", r"1", r"2", r"3"])

add(num=2, type="single", score=4, pages=[1], anchor="第(2)题",
    stem=r"设函数 $f(x)=(e^{x}-1)(e^{2x}-2)\cdots(e^{nx}-n)$，其中 $n$ 为正整数，则 $f'(0)=$（　　）",
    options=[r"$(-1)^{n-1}(n-1)!$", r"$(-1)^{n}(n-1)!$",
             r"$(-1)^{n-1}n!$", r"$(-1)^{n}n!$"])

add(num=3, type="single", score=4, pages=[1], anchor="第(3)题",
    stem=r"如果函数 $f(x,y)$ 在 $(0,0)$ 处连续，那么下列命题正确的是（　　）.",
    options=[r"$\lim\limits_{x\to0\atop y\to0}\dfrac{f(x,y)}{|x|+|y|}$ 存在，则 $f(x,y)$ 在 $(0,0)$ 处可微",
             r"若极限 $\lim\limits_{x\to0\atop y\to0}\dfrac{f(x,y)}{x^{2}+y^{2}}$ 存在，则 $f(x,y)$ 在 $(0,0)$ 处可微",
             r"若 $f(x,y)$ 在 $(0,0)$ 处可微，则极限 $\lim\limits_{x\to0\atop y\to0}\dfrac{f(x,y)}{|x|+|y|}$ 存在",
             r"若 $f(x,y)$ 在 $(0,0)$ 处可微，则极限 $\lim\limits_{x\to0\atop y\to0}\dfrac{f(x,y)}{x^{2}+y^{2}}$ 存在"])

add(num=4, type="single", score=4, pages=[1], anchor="第(4)题",
    stem=r"设 $I_{k}=\int_{0}^{k\pi}e^{x^{2}}\sin xdx, (k=1,2,3)$，则有（　　）.",
    options=[r"$I_{1}<I_{2}<I_{3}$", r"$I_{3}<I_{2}<I_{1}$",
             r"$I_{2}<I_{3}<I_{1}$", r"$I_{2}<I_{1}<I_{3}$"])

add(num=5, type="single", score=4, pages=[1], anchor="第(5)题",
    stem=r"设 $\boldsymbol{\alpha}_{1}=\begin{pmatrix}0\\0\\c_{1}\end{pmatrix}, \boldsymbol{\alpha}_{2}=\begin{pmatrix}0\\1\\c_{2}\end{pmatrix}, \boldsymbol{\alpha}_{3}=\begin{pmatrix}1\\-1\\c_{3}\end{pmatrix}, \boldsymbol{\alpha}_{4}=\begin{pmatrix}-1\\1\\c_{4}\end{pmatrix}$，"
         r"其中 $c_{1},c_{2},c_{3},c_{4}$ 为任意常数，则下列向量组线性相关的是（　　）.",
    options=[r"$\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}$",
             r"$\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{4}$",
             r"$\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}$",
             r"$\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}$"])

add(num=6, type="single", score=4, pages=[2], anchor="第(6)题",
    stem=r"设 $\boldsymbol{A}$ 为三阶矩阵，$\boldsymbol{P}$ 为三阶可逆矩阵，且 $\boldsymbol{P}^{-1}\boldsymbol{A}\boldsymbol{P}=\begin{pmatrix}1&0&0\\0&1&0\\0&0&2\end{pmatrix}$，"
         r"若 $\boldsymbol{P}=(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3})$，$\boldsymbol{Q}=(\boldsymbol{\alpha}_{1}+\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3})$，则 $\boldsymbol{Q}^{-1}\boldsymbol{A}\boldsymbol{Q}=$（　　）.",
    options=[r"$\begin{pmatrix}1&0&0\\0&2&0\\0&0&1\end{pmatrix}$", r"$\begin{pmatrix}1&0&0\\0&1&0\\0&0&2\end{pmatrix}$",
             r"$\begin{pmatrix}2&0&0\\0&1&0\\0&0&2\end{pmatrix}$", r"$\begin{pmatrix}2&0&0\\0&2&0\\0&0&1\end{pmatrix}$"])

add(num=7, type="single", score=4, pages=[2], anchor="第(7)题",
    stem=r"设随机变量 $X$ 和 $Y$ 相互独立，且分别服从参数为 1 和参数为 4 的指数分布，则 $P(X<Y)=$（　　）",
    options=[r"$\dfrac{1}{5}$", r"$\dfrac{1}{3}$", r"$\dfrac{2}{5}$", r"$\dfrac{4}{5}$"])

add(num=8, type="single", score=4, pages=[2], anchor="第(8)题",
    stem=r"将长度为 1 的木棒随机地截成两段，则两段长度的相关系数为（　　）.",
    options=[r"1", r"$\dfrac{1}{2}$", r"$-\dfrac{1}{2}$", r"$-1$"])

# ---------- 二、填空题：9～14 小题，每小题 4 分，共 24 分．请将答案写在答题纸指定位置上. ----------

add(num=9, type="blank", score=4, pages=[2], anchor="第(9)题",
    stem=r"已知函数 $f(x)$ 满足方程 $f''(x)+f'(x)-2f(x)=0$ 及 $f''(x)+f(x)=2e^{x}$，则 $f(x)=$________.",
    options=[])

add(num=10, type="blank", score=4, pages=[2], anchor="第(10)题",
    stem=r"$\int_{0}^{2}x\sqrt{2x-x^{2}}dx=$________.",
    options=[])

add(num=11, type="blank", score=4, pages=[2], anchor="第(11)题",
    stem=r"$grad\left(xy+\dfrac{z}{y}\right)\Big|_{(2,1,1)}=$________.",
    options=[])

add(num=12, type="blank", score=4, pages=[2], anchor="第(12)题",
    stem=r"设 $\Sigma=\{(x,y,z)|x+y+z=1,x\geqslant0,y\geqslant0,z\geqslant0\}$，则 $\iint\limits_{\Sigma}y^{2}dS=$________.",
    options=[])

add(num=13, type="blank", score=4, pages=[2], anchor="第(13)题",
    stem=r"设 $\boldsymbol{\alpha}$ 为三维单位向量，$\boldsymbol{E}$ 为三阶单位矩阵，则 $\boldsymbol{E}-\boldsymbol{\alpha}\boldsymbol{\alpha}^{T}$ 的秩为________.",
    options=[])

add(num=14, type="blank", score=4, pages=[2], anchor="第(14)题",
    stem=r"设 $A,B,C$ 为三个随机事件，$A$ 与 $C$ 互不相容，$P(AB)=\dfrac{1}{2}$，$P(C)=\dfrac{1}{3}$，"
         r"则 $P(AB|\overline{C})=$________.",
    options=[])

# ---------- 三、解答题：15～23 小题，共 94 分．解答应写出文字说明、证明过程或演算步骤．请将答案写在答题纸指定位置上. ----------

add(num=15, type="essay", score=10, pages=[3], anchor="第(15)题",
    stem=r"证明：$x\ln\dfrac{1+x}{1-x}+\cos x>1+\dfrac{x^{2}}{2}$，$-1<x<1$.",
    options=[])

add(num=16, type="essay", score=10, pages=[3], anchor="第(16)题",
    stem=r"求函数 $f(x,y)=xe^{-\frac{x^{2}+y^{2}}{2}}$ 的极值.",
    options=[])

add(num=17, type="essay", score=10, pages=[3], anchor="第(17)题",
    stem=r"求幂级数 $\sum\limits_{n=0}^{\infty}\dfrac{4n^{2}+4n+3}{2n+1}x^{2n}$ 的收敛域及和函数.",
    options=[])

add(num=18, type="essay", score=10, pages=[3], anchor="第(18)题",
    stem=r"已知曲线 $L:\begin{cases}x=f(t)\\y=\cos t\end{cases}(0\leqslant t\leqslant\dfrac{\pi}{2})$，其中函数 $f(t)$ 具有连续导数，且 $f(0)=0$，"
         r"$f'(t)>0(0<t<\dfrac{\pi}{2})$．若曲线 $L$ 的切线与 $x$ 轴交点到切点的距离恒为 1，求函数 $f(t)$ 的表达式，"
         r"并求此曲线 $L$ 与 $x$ 轴与 $y$ 轴无边界的区域的面积.",
    options=[])

add(num=19, type="essay", score=10, pages=[3], anchor="第(19)题",
    stem=r"已知 $L$ 是第一象限中从点 $(0,0)$ 沿圆周 $x^{2}+y^{2}=2x$ 到点 $(2,0)$，再沿圆周"
         r"$x^{2}+y^{2}=4$ 到点 $(0,2)$ 的曲线段，计算曲线积分 $J=\int_{L}3x^{2}ydx+\left(x^{3}+x-2y\right)dy$.",
    options=[])

add(num=20, type="essay", score=11, pages=[3], anchor="第(20)题",
    stem=r"设 $\boldsymbol{A}=\begin{pmatrix}1&a&0&0\\0&1&a&0\\0&0&1&a\\a&0&0&1\end{pmatrix}, \boldsymbol{\beta}=\begin{pmatrix}1\\-1\\0\\0\end{pmatrix}$."
         r"（1）计算 $|\boldsymbol{A}|$；"
         r"（2）当实数 $a$ 取何值时，$\boldsymbol{Ax}=\boldsymbol{\beta}$ 有无穷多解，并求其通解.",
    options=[])

add(num=21, type="essay", score=11, pages=[3], anchor="第(21)题",
    stem=r"已知 $\boldsymbol{A}=\begin{pmatrix}1&0&1\\0&1&1\\-1&0&a\\0&a&-1\end{pmatrix}$，二次型 $f(x_{1},x_{2},x_{3})=\boldsymbol{x}^{T}(\boldsymbol{A}^{T}\boldsymbol{A})\boldsymbol{x}$ 的秩为 2."
         r"（1）求实数 $a$ 的值；"
         r"（2）求正交变换 $\boldsymbol{x}=\boldsymbol{Qy}$ 将 $f$ 化为标准形.",
    options=[])

add(num=22, type="essay", score=11, pages=[3, 4], anchor="第(22)题",
    stem=r"设二维离散型随机变量 $X$ 与 $Y$ 的概率分布为"
         r"$\begin{array}{c|ccc} X\backslash Y & 0 & 1 & 2\\ \hline 0 & \dfrac{1}{4} & 0 & \dfrac{1}{4}\\ 1 & 0 & \dfrac{1}{3} & 0\\ 2 & \dfrac{1}{12} & 0 & \dfrac{1}{12} \end{array}$"
         r"求：（1）$P(X=2Y)$；"
         r"（2）$\mathrm{cov}(X-Y,Y)$.",
    options=[])

add(num=23, type="essay", score=11, pages=[4], anchor="第(23)题",
    stem=r"设随机变量 $X$ 与 $Y$ 相互独立且分别服从正态分布 $N(\mu,\sigma^{2})$ 与 $N(\mu,2\sigma^{2})$，其中 $\sigma$ 是未"
         r"知参数且 $\sigma>0$．设 $Z=X-Y$."
         r"（1）求 $Z$ 的概率密度 $f_{Z}(z)$；"
         r"（2）设 $Z_{1},Z_{2},\cdots,Z_{n}$ 为来自总体 $Z$ 的简单随机样本，求 $\sigma^{2}$ 的最大似然估计量 $\hat{\sigma}^{2}$；"
         r"（3）证明 $\sigma^{2}$ 为 $\hat{\sigma}^{2}$ 的无偏估计量.",
    options=[])
