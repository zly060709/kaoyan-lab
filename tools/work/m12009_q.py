# -*- coding: utf-8 -*-
"""2009 数学一 题干视觉转录（照录 data/math1.pages/pages/2009/p1-p5.png，解析卷 p6-p13 另见 a1-a3）"""

ITEMS = []

def add(**kw):
    ITEMS.append(kw)

# ---------- 一、选择题：1～8 小题，每小题 4 分，共 32 分。下列每题给出的四个选项中，只有一个选项是符合题目要求的。请将所选项前的字母填在答题纸指定位置上. ----------

add(num=1, type="single", score=4, pages=[1], anchor="第(1)题",
    stem=r"当 $x\to0$ 时，$f(x)=x-\sin ax$ 与 $g(x)=x^{2}\ln(1-bx)$ 等价无穷小，则（ ）",
    options=[
        r"$a=1,b=-\dfrac{1}{6}$",
        r"$a=1,b=\dfrac{1}{6}$",
        r"$a=-1,b=-\dfrac{1}{6}$",
        r"$a=-1,b=\dfrac{1}{6}$",
    ])

add(num=2, type="single", score=4, pages=[1], anchor="第(2)题",
    stem=r"如图，正方形 $\{(x,y)\,|\,|x|\leqslant1,|y|\leqslant1\}$ 被其对角线划分为四个区域 $D_{k}(k=1,2,3,4)$，"
         r"$I_{k}=\iint\limits_{D_{k}}y\cos xdxdy$，则 $\max\limits_{1\leqslant k\leqslant4}\{I_{k}\}=$（ ）"
         r" @@M:math1-2009-2:0@@",
    options=[r"$I_{1}$", r"$I_{2}$", r"$I_{3}$", r"$I_{4}$"])

add(num=3, type="single", score=4, pages=[1, 2], anchor="第(3)题",
    stem=r"设函数 $y=f(x)$ 在区间 $[-1,3]$ 上的图形如图所示，则函数 $F(x)=\displaystyle\int_{0}^{x}f(t)dt$ 为（ ）"
         r" @@M:math1-2009-3:0@@",
    options=[
        r"@@M:math1-2009-3:1@@",
        r"@@M:math1-2009-3:2@@",
        r"@@M:math1-2009-3:3@@",
        r"@@M:math1-2009-3:4@@",
    ])

add(num=4, type="single", score=4, pages=[2], anchor="第(4)题",
    stem=r"设有两个数列 $\{a_{n}\},\{b_{n}\}$，若 $\lim\limits_{n\to\infty}a_{n}=0$，则（ ）",
    options=[
        r"当 $\sum\limits_{n=1}^{\infty}b_{n}$ 收敛时，$\sum\limits_{n=1}^{\infty}a_{n}b_{n}$ 收敛",
        r"$\sum\limits_{n=1}^{\infty}b_{n}$ 发散时，$\sum\limits_{n=1}^{\infty}a_{n}b_{n}$ 发散",
        r"当 $\sum\limits_{n=1}^{\infty}|b_{n}|$ 收敛时，$\sum\limits_{n=1}^{\infty}a_{n}^{2}b_{n}^{2}$ 收敛",
        r"$\sum\limits_{n=1}^{\infty}|b_{n}|$ 发散时，$\sum\limits_{n=1}^{\infty}a_{n}^{2}b_{n}^{2}$ 发散",
    ])

add(num=5, type="single", score=4, pages=[2], anchor="第(5)题",
    stem=r"设 $\boldsymbol{a}_{1},\boldsymbol{a}_{2},\boldsymbol{a}_{3}$ 是 3 维向量空间 $R^{3}$ 的一组基，则由基 $\boldsymbol{a}_{1},\dfrac{1}{2}\boldsymbol{a}_{2},\dfrac{1}{3}\boldsymbol{a}_{3}$ 到基 "
         r"$\boldsymbol{a}_{1}+\boldsymbol{a}_{2},\boldsymbol{a}_{2}+\boldsymbol{a}_{3},\boldsymbol{a}_{3}+\boldsymbol{a}_{1}$ 的过渡矩阵为（ ）",
    options=[
        r"$\begin{pmatrix}1&0&1\\2&2&0\\0&3&3\end{pmatrix}$",
        r"$\begin{pmatrix}1&2&0\\0&2&3\\1&0&3\end{pmatrix}$",
        r"$\begin{pmatrix}\dfrac{1}{2}&\dfrac{1}{4}&-\dfrac{1}{6}\\-\dfrac{1}{2}&\dfrac{1}{4}&\dfrac{1}{6}\\\dfrac{1}{2}&-\dfrac{1}{4}&\dfrac{1}{6}\end{pmatrix}$",
        r"$\begin{pmatrix}\dfrac{1}{2}&-\dfrac{1}{2}&\dfrac{1}{2}\\\dfrac{1}{4}&\dfrac{1}{4}&-\dfrac{1}{4}\\-\dfrac{1}{6}&\dfrac{1}{6}&\dfrac{1}{6}\end{pmatrix}$",
    ])

add(num=6, type="single", score=4, pages=[3], anchor="第(6)题",
    stem=r"设 $\boldsymbol{A},\boldsymbol{B}$ 均为 2 阶矩阵，$\boldsymbol{A}^{*},\boldsymbol{B}^{*}$ 分别为 $\boldsymbol{A},\boldsymbol{B}$ 的伴随矩阵，若 $|\boldsymbol{A}|=2,|\boldsymbol{B}|=3$,则分块矩阵 "
         r"$\begin{pmatrix}\boldsymbol{O}&\boldsymbol{A}\\\boldsymbol{B}&\boldsymbol{O}\end{pmatrix}$ 的伴随矩阵为（ ）",
    options=[
        r"$\begin{pmatrix}\boldsymbol{O}&3\boldsymbol{B}^{*}\\2\boldsymbol{A}^{*}&\boldsymbol{O}\end{pmatrix}$",
        r"$\begin{pmatrix}\boldsymbol{O}&2\boldsymbol{B}^{*}\\3\boldsymbol{A}^{*}&\boldsymbol{O}\end{pmatrix}$",
        r"$\begin{pmatrix}\boldsymbol{O}&3\boldsymbol{A}^{*}\\2\boldsymbol{B}^{*}&\boldsymbol{O}\end{pmatrix}$",
        r"$\begin{pmatrix}\boldsymbol{O}&2\boldsymbol{A}^{*}\\3\boldsymbol{B}^{*}&\boldsymbol{O}\end{pmatrix}$",
    ])

add(num=7, type="single", score=4, pages=[3], anchor="第(7)题",
    stem=r"设随机变量 $X$ 的分布函数为 $F(x)=0.3\Phi(x)+0.7\Phi\left(\dfrac{x-1}{2}\right)$,其中 $\Phi(x)$ 为标准正态分"
         r"布函数，则 $E(X)=$（ ）",
    options=[r"$0$", r"$0.3$", r"$0.7$", r"$1$"])

add(num=8, type="single", score=4, pages=[3], anchor="第(8)题",
    stem=r"设随机变量 $X$ 与 $Y$ 相互独立，且 $X$ 服从标准正态分布 $N(0,1)$,$Y$ 的概率分布为 "
         r"$P\{Y=0\}=P\{Y=1\}=\dfrac{1}{2}$，记 $F_{z}(z)$ 为随机变量 $Z=XY$ 的分布函数，则函数 $F_{z}(z)$ 的"
         r"间断点个数为（ ）",
    options=[r"$0$", r"$1$", r"$2$", r"$3$"])

# ---------- 二、填空题：9～14 小题，每小题 4 分，共 24 分. 请将答案写在答题纸指定位置上. ----------

add(num=9, type="blank", score=4, pages=[3], anchor="第(9)题",
    stem=r"设函数 $f(u,v)$ 具有二阶连续偏导数, $z=f(x,xy)$,则 $\dfrac{\partial^{2}z}{\partial x\partial y}=$________.",
    options=[])

add(num=10, type="blank", score=4, pages=[3], anchor="第(10)题",
    stem=r"若二阶常系数线性齐次微分方程 $y''+ay'+by=0$ 的通解为 $y=(C_{1}+C_{2}x)e^{x}$,则非齐"
         r"次方程 $y''+ay'+by=x$ 满足条件 $y(0)=2,y'(0)=0$ 的通解为 y=________.",
    options=[])

add(num=11, type="blank", score=4, pages=[3], anchor="第(11)题",
    stem=r"已知曲线 $L:y=x^{2}(0\leqslant x\leqslant\sqrt{2})$，则 $\int_{L}xds=$________.",
    options=[])

add(num=12, type="blank", score=4, pages=[3], anchor="第(12)题",
    stem=r"设 $\Omega=\{(x,y,z)\,|\,x^{2}+y^{2}+z^{2}\leqslant1\}$，则 $\iiint\limits_{\Omega}z^{2}dxdydz=$________.",
    options=[])

add(num=13, type="blank", score=4, pages=[3], anchor="第(13)题",
    stem=r"若 3 维向量 $\boldsymbol{\alpha},\boldsymbol{\beta}$ 满足 $\boldsymbol{\alpha}^{T}\boldsymbol{\beta}=2$，其中 $\boldsymbol{\alpha}^{T}$ 为 $\boldsymbol{\alpha}$ 的转置，则矩阵 $\boldsymbol{\beta}\boldsymbol{\alpha}^{T}$ 的非零特征值为"
         r"________.",
    options=[])

add(num=14, type="blank", score=4, pages=[3], anchor="第(14)题",
    stem=r"设 $X_{1},X_{2},...,X_{m}$ 为来自二项分布总体 $B(n,p)$ 的简单随机样本，$\overline{X}$ 和 $S^{2}$ 分别为样本"
         r"均值和样本方差. 若 $\overline{X}+kS^{2}$ 为 $np^{2}$ 的无偏估计量，则 $k=$________.",
    options=[])

# ---------- 三、解答题：15～23 小题，共 94 分. 解答应写出文字说明、证明过程或演算步骤. 请将答案写在答题纸指定位置上. ----------

add(num=15, type="essay", score=9, pages=[4], anchor="第(15)题",
    stem=r"（本题满分 9 分）求二元函数 $f(x,y)=x^{2}(2+y^{2})+y\ln y$ 极值.",
    options=[])

add(num=16, type="essay", score=9, pages=[4], anchor="第(16)题",
    stem=r"（本题满分 9 分）设 $a_{n}$ 为曲线 $y=x^{n}$ 与 $y=x^{n+1}(n=1,2,...)$ 所围成区域的面积，记 "
         r"$S_{1}=\sum\limits_{n=1}^{\infty}a_{n},S_{2}=\sum\limits_{n=1}^{\infty}a_{2n-1}$ ，求 $S_{1}$ 与 $S_{2}$ 的值.",
    options=[])

add(num=17, type="essay", score=11, pages=[4], anchor="第(17)题",
    stem=r"（本题满分 11 分）椭球面 $S_{1}$ 是椭圆 $\dfrac{x^{2}}{4}+\dfrac{y^{2}}{3}=1$ 绕 $x$ 轴旋转而成，圆锥面 $S_{2}$ 是过点 "
         r"$(4,0)$ 且与椭圆 $\dfrac{x^{2}}{4}+\dfrac{y^{2}}{3}=1$ 相切的直线绕 $x$ 轴旋转而成. "
         r"（I）求 $S_{1}$ 及 $S_{2}$ 的方程；"
         r"（II）求 $S_{1}$ 与 $S_{2}$ 之间的立体的体积.",
    options=[])

add(num=18, type="essay", score=11, pages=[4], anchor="第(18)题",
    stem=r"（本题满分 11 分）(I) 证明拉格朗日中值定理：若函数 $f(x)$ 在 $[a,b]$ 上连续，在 $(a,b)$ "
         r"可导，则存在 $\zeta\in(a,b)$，使得 $f(b)-f(a)=f'(\zeta)(b-a)$. "
         r"（II）证明：若函数 $f(x)$ 在 x=0 处连续，在 $(0,\delta)(\delta>0)$ 内可导，且 $\lim\limits_{x\to0^{+}}f'(x)=A$ 则"
         r"$f'_{+}(0)$ 存在，且 $f'_{+}(0)=A$. ",
    options=[])

add(num=19, type="essay", score=10, pages=[4], anchor="第(19)题",
    stem=r"（本题满分 10 分）计算曲面积分 $I=\oiint\limits_{\Sigma}\dfrac{xdydz+ydzdx+zdxdy}{(x^{2}+y^{2}+z^{2})^{\frac{3}{2}}}$ 其中 $\Sigma$ 是曲面 "
         r"$2x^{2}+2y^{2}+z^{2}=4$ 的外侧.",
    options=[])

add(num=20, type="essay", score=11, pages=[4], anchor="第(20)题",
    stem=r"（本题满分 11 分）设 $\boldsymbol{A}=\begin{pmatrix}1&-1&-1\\-1&1&1\\0&-4&-2\end{pmatrix}$,"
         r"$\boldsymbol{\zeta}_{1}=\begin{pmatrix}-1\\1\\-2\end{pmatrix}$ "
         r"（I）求满足 $\boldsymbol{A\zeta}_{2}=\boldsymbol{\zeta}_{1},\boldsymbol{A}^{2}\boldsymbol{\zeta}_{3}=\boldsymbol{\zeta}_{1}$ 的所有向量 $\boldsymbol{\zeta}_{2},\boldsymbol{\zeta}_{3}$；"
         r"（II）对（I）中的任一向量 $\boldsymbol{\zeta}_{2},\boldsymbol{\zeta}_{3}$,证明:$\boldsymbol{\zeta}_{1},\boldsymbol{\zeta}_{2},\boldsymbol{\zeta}_{3}$ 线性无关.",
    options=[])

add(num=21, type="essay", score=11, pages=[4, 5], anchor="第(21)题",
    stem=r"（本题满分 11 分）设二次型 $f(x_{1},x_{2},x_{3})=ax_{1}^{2}+ax_{2}^{2}+(a-1)x_{3}^{2}+2x_{1}x_{3}-2x_{2}x_{3}$ "
         r"（I）求二次型 $f$ 的矩阵的所有特征值；"
         r"（II）若二次型 $f$ 的规范形为 $y_{1}^{2}+y_{2}^{2}$，求 $a$ 的值.",
    options=[])

add(num=22, type="essay", score=11, pages=[5], anchor="第(22)题",
    stem=r"（本题满分 11 分）袋中有一个红球，两个黑球，三个白球，现有放回的从袋中取两"
         r"次，每次取一球，以 $X$，$Y$，$Z$ 分别表示两次取球的红、黑、白球的个数. "
         r"（I）求 $P\left\{X=1|Z=0\right\}$. "
         r"（II）求二维随机变量 $(X,Y)$ 的概率分布.",
    options=[])

add(num=23, type="essay", score=11, pages=[5], anchor="第(23)题",
    stem=r"（本题满分 11 分）设总体 $X$ 的概率密度为 "
         r"$f(x)=\begin{cases}\lambda^{2}xe^{-\lambda x}, & x>0\\ 0, & \text{其他}\end{cases}$，其中参数 "
         r"$\lambda(\lambda>0)$ 未知，$X_{1},X_{2},...X_{n}$ 是来自总体 $X$ 的简单随机样本. "
         r"（I）求参数 $\lambda$ 的矩估计量；"
         r"（II）求参数 $\lambda$ 的最大似然估计量.",
    options=[])
