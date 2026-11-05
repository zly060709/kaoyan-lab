# -*- coding: utf-8 -*-
"""2010 数学三 题干视觉转录（照录 data/math3/pages/2010/p1-p3.png）"""

ITEMS = []

def add(**kw):
    ITEMS.append(kw)

# ---------- 一、选择题：1～8 小题，每小题 4 分，共 32 分（原卷 p1-p2 说明行原文，逐字） ----------
# 一、选择题：1～8 小题，每小题 4 分，共 32 分。下列每题给出的四个选项中，只有一个选项是符合题目要求的。
# 请将所选项前的字母填在答题纸指定位置上.

add(num=1, type="single", score=4, pages=[1], anchor="第(1)题",
    stem=r"若 $\lim\limits_{x\to0}\left[\dfrac{1}{x}-\left(\dfrac{1}{x}-a\right)e^{x}\right]=1$，则 $a$ 等于.",
    options=[r"$0$", r"$1$", r"$2$", r"$3$"])

add(num=2, type="single", score=4, pages=[1], anchor="第(2)题",
    stem=r"设 $y_{1},y_{2}$ 是一阶线性非齐次微分方程 $y'+p(x)y=q(x)$ 的两个特解，若常数 $\lambda,\mu$ 使"
         r"$\lambda y_{1}+\mu y_{2}$ 是该方程的解，$\lambda y_{1}-\mu y_{2}$ 是该方程对应的齐次方程的解，则.",
    options=[
        r"$\lambda=\dfrac{1}{2},\mu=\dfrac{1}{2}$",
        r"$\lambda=-\dfrac{1}{2},\mu=-\dfrac{1}{2}$",
        r"$\lambda=\dfrac{2}{3},\mu=\dfrac{1}{3}$",
        r"$\lambda=\dfrac{2}{3},\mu=\dfrac{2}{3}$",
    ])

add(num=3, type="single", score=4, pages=[1], anchor="第(3)题",
    stem=r"设函数 $f(x),g(x)$ 具有二阶导数，且 $g''(x)<0$，若 $g(x_{0})=a$ 是 $g(x)$ 的极值，则"
         r"$f(g(x))$ 在 $x_{0}$ 取极大值的一个充分条件是.",
    options=[r"$f'(a)<0$", r"$f'(a)>0$", r"$f''(a)<0$", r"$f''(a)>0$"])

add(num=4, type="single", score=4, pages=[1], anchor="第(4)题",
    stem=r"设 $f(x)=\ln^{10}x$, $g(x)=x$, $h(x)=e^{\frac{x}{10}}$，则当 $x$ 充分大时有.",
    options=[
        r"$g(x)<h(x)<f(x)$",
        r"$h(x)<g(x)<f(x)$",
        r"$f(x)<g(x)<h(x)$",
        r"$g(x)<f(x)<h(x)$",
    ])

add(num=5, type="single", score=4, pages=[1], anchor="第(5)题",
    stem=r"设向量组 $I:\boldsymbol{a}_{1},\boldsymbol{a}_{2},\cdots,\boldsymbol{a}_{r}$ 可由向量组"
         r"$II:\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\cdots,\boldsymbol{\beta}_{s}$ 线性表示. 下列命题正确的是.",
    options=[
        r"若向量组 I 线性无关，则 $r\leqslant s$",
        r"若向量组 I 线性相关，则 $r>s$",
        r"若向量组 II 线性无关，则 $r\leqslant s$",
        r"若向量组 II 线性相关，则 $r>s$",
    ])

add(num=6, type="single", score=4, pages=[1], anchor="第(6)题",
    stem=r"设 $A$ 为 4 阶实对称矩阵，且 $A^{2}+A=0$ 若 $A$ 的秩为 3，则 $A$ 相似于.",
    options=[
        r"$\begin{pmatrix}1&&&\\&1&&\\&&1&\\&&&0\end{pmatrix}$",
        r"$\begin{pmatrix}1&&&\\&1&&\\&&-1&\\&&&0\end{pmatrix}$",
        r"$\begin{pmatrix}1&&&\\&-1&&\\&&-1&\\&&&0\end{pmatrix}$",
        r"$\begin{pmatrix}-1&&&\\&-1&&\\&&-1&\\&&&0\end{pmatrix}$",
    ])

add(num=7, type="single", score=4, pages=[2], anchor="第(7)题",
    stem=r"设随机变量 $X$ 的分布函数"
         r"$F(x)=\begin{cases}0,&x<0\\ \dfrac{1}{2},&0\leqslant x<1\\ 1-e^{-x},&x\geqslant1\end{cases}$，"
         r"则 $P\{X=1\}=$.",
    options=[r"$0$", r"$\dfrac{1}{2}$", r"$\dfrac{1}{2}-e^{1}$", r"$1-e^{-1}$"])

add(num=8, type="single", score=4, pages=[2], anchor="第(8)题",
    stem=r"设 $f_{1}(x)$ 为标准正态分布的概率密度，$f_{2}(x)$ 为 $[-1,3]$ 上的均匀分布的概率密度，若"
         r"$f(x)=\begin{cases}af_{1}(x),&x\leqslant0\\ bf_{2}(x),&x>0\end{cases}$ $(a>0,b>0)$ 为概率密度，则 $a,b$ 应满足:",
    options=[r"$2a+3b=4$", r"$3a+2b=4$", r"$a+b=1$", r"$a+b=2$"])

# ---------- 二、填空题：9～14 小题，每小题 4 分，共 24 分（原卷 p2 说明行原文，逐字） ----------
# 二、填空题：9～14 小题，每小题 4 分，共 24 分。请将答案写在答题纸指定位置上.

add(num=9, type="blank", score=4, pages=[2], anchor="第(9)题",
    stem=r"设可导函数 $y=y(x)$ 由方程 $\int_{0}^{x+y}e^{-t^{2}}dt=\int_{0}^{x}x\sin t^{2}dt$ 确定，"
         r"则 $\dfrac{dy}{dx}\Big|_{x=0}=$______.",
    options=[])

add(num=10, type="blank", score=4, pages=[2], anchor="第(10)题",
    stem=r"设位于曲线 $y=\dfrac{1}{\sqrt{x(1+\ln^{2}x)}}$ $(e\leqslant x<+\infty)$ 下方，$x$ 轴上方的无界区域为 $G$，"
         r"则 $G$ 绕 $x$ 轴旋转一周所得空间区域的体积为________.",
    options=[])

add(num=11, type="blank", score=4, pages=[2], anchor="第(11)题",
    stem=r"设某商品的收益函数为 $R(p)$，收益弹性为 $1+p^{3}$，其中 $p$ 为价格，且 $R(1)=1$，则 $R(p)=$______.",
    options=[])

add(num=12, type="blank", score=4, pages=[2], anchor="第(12)题",
    stem=r"若曲线 $y=x^{3}+ax^{2}+bx+1$ 有拐点 $(-1,0)$，则 $b=$______.",
    options=[])

add(num=13, type="blank", score=4, pages=[2], anchor="第(13)题",
    stem=r"设 $A,B$ 为 3 阶方阵，且 $|A|=3,|B|=2,|A^{-1}+B|=2,$，则 $|A+B^{-1}|=$______.",
    options=[])

add(num=14, type="blank", score=4, pages=[2], anchor="第(14)题",
    stem=r"设 $X_{1},X_{2},\cdots,X_{n}$ 是来自总体 $N(\mu,\sigma^{2})$ $(\sigma>0)$ 的简单随机样本，记统计量"
         r"$T=\dfrac{1}{n}\sum\limits_{i=1}^{n}X_{i}^{2}$，则 $ET=$______.",
    options=[])

# ---------- 三、解答题：15～23 小题，共 94 分（原卷 p2 说明行原文，逐字） ----------
# 三、解答题：15～23 小题，共 94 分。解答应写出文字说明、证明过程或演算步骤。请将答案写在答题纸指定位置上.
# 各题分值以卷面"（本题满分 X 分）"为准：15-19 各 10 分，20-23 各 11 分.

add(num=15, type="essay", score=10, pages=[2], anchor="第(15)题",
    stem=r"（本题满分 10 分）求极限 $\lim\limits_{x\to+\infty}(x^{\frac{1}{x}}-1)^{\frac{1}{\ln x}}$.",
    options=[])

add(num=16, type="essay", score=10, pages=[2], anchor="第(16)题",
    stem=r"（本题满分 10 分）计算二重积分 $\iint\limits_{D}(x+y)^{3}\mathrm{d}x\mathrm{d}y$，"
         r"其中 $D$ 由曲线 $x=\sqrt{1+y^{2}}$ 与直线 $x+\sqrt{2}\,y=0$ 及 $x-\sqrt{2}\,y=0$ 围成.",
    options=[])

add(num=17, type="essay", score=10, pages=[3], anchor="第(17)题",
    stem=r"（本题满分 10 分）求函数 $M=xy+2yz$ 在约束条件 $x^{2}+y^{2}+z^{2}=10$ 下的最大值和最小值.",
    options=[])

add(num=18, type="essay", score=10, pages=[3], anchor="第(18)题",
    stem=r"（本题满分 10 分）"
         r"（I）比较 $\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}dt$ 与 $\int_{0}^{1}|\ln t|t^{n}dt$, $n=1,2,\cdots$ 的大小，说明理由"
         r"（II）设 $M_{n}=\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}dt(n=1,2,\cdots)$，求极限 $\lim\limits_{n\to\infty}M_{n}$.",
    options=[])

add(num=19, type="essay", score=10, pages=[3], anchor="第(19)题",
    stem=r"（本题满分 10 分）设函数 $f(x)$ 在 $[0,3]$ 上连续，在 $(0,3)$ 内存在二阶导数，且"
         r"$2f(0)=\int_{0}^{2}f(x)dx=f(2)+f(3)$,"
         r"（I）证明：存在 $\eta\in(0,2)$ 使 $f(\eta)=f(0)$;"
         r"（II）证明：存在 $\xi\in(0,3)$, 使得 $f''(\xi)=0$.",
    options=[])

add(num=20, type="essay", score=11, pages=[3], anchor="第(20)题",
    stem=r"（本题满分 11 分）设"
         r"$A=\begin{pmatrix}\lambda&1&1\\ 0&\lambda-1&0\\ 1&1&\lambda\end{pmatrix}$, "
         r"$\boldsymbol{b}=\begin{pmatrix}a\\ 1\\ 1\end{pmatrix}.$"
         r"已知线性方程组 $A\boldsymbol{x}=\boldsymbol{b}$ 存在 2 个不同的解,"
         r"（I）求 $\lambda$，$a$;"
         r"（II）求方程组的 $A\boldsymbol{x}=\boldsymbol{b}$ 通解.",
    options=[])

add(num=21, type="essay", score=11, pages=[3], anchor="第(21)题",
    stem=r"（本题满分 11 分）设 $A=\begin{pmatrix}0&-1&4\\ -1&3&a\\ 4&a&0\end{pmatrix}$，"
         r"正交矩阵 $Q$ 使得 $Q^{T}AQ$ 为对角矩阵，若 $Q$ 的第一列为 $\dfrac{1}{\sqrt{6}}\begin{pmatrix}1\\ 2\\ 1\end{pmatrix}$，"
         r"求 $a$，$Q$.",
    options=[])

add(num=22, type="essay", score=11, pages=[3], anchor="第(22)题",
    stem=r"（本题满分 11 分）设二维随机变量 $(X,Y)$ 的概率密度为"
         r"$f(x,y)=Ae^{-2x^{2}+2xy-y^{2}}$, $-\infty<x<+\infty$，"
         r"求常数 $A$ 及条件概率密度 $f_{Y|X}(y|x)$.",
    options=[])

add(num=23, type="essay", score=11, pages=[3], anchor="第(23)题",
    stem=r"（本题满分 11 分）箱内有 6 个球，其中红，白，黑球的个数分别为 1,2,3 个，现从箱中随机的取出 2 个球，"
         r"设 $X$ 为取出的红球个数，$Y$ 为取出的白球个数"
         r"（I）求随机变量 $(X,Y)$ 的概率分布;（II）求 $\operatorname{cov}(X,Y)$.",
    options=[])
