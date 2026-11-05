# -*- coding: utf-8 -*-
"""2022 数学三 题干视觉转录（照录 data/math3/pages/2022/p1-p4.png）"""

ITEMS = []

def add(**kw):
    ITEMS.append(kw)

# ---------- 一、选择题 1-10（每小题 5 分，共 50 分） ----------
add(num=1, type="single", score=5, pages=[1], anchor="第(1)题",
    stem=r"$x\to0$ 时，$\alpha(x)$，$\beta(x)$ 是非零无穷小量，给出以下 4 个命题：（ ）"
         r"①若 $\alpha(x)\sim\beta(x)$，则 $\alpha^{2}(x)\sim\beta^{2}(x)$；"
         r"②若 $\alpha^{2}(x)\sim\beta^{2}(x)$，则 $\alpha(x)\sim\beta(x)$；"
         r"③若 $\alpha(x)\sim\beta(x)$，则 $\alpha(x)-\beta(x)=o(\alpha(x))$；"
         r"④若 $\alpha(x)-\beta(x)=o(\alpha(x))$，则 $\alpha(x)\sim\beta(x)$；"
         r"其中真命题是：（ ）",
    options=[r"①③", r"①④", r"①③④", r"②③④"])

add(num=2, type="single", score=5, pages=[1], anchor="第(2)题",
    stem=r"已知 $a_n=\sqrt[n]{n}-\dfrac{(-1)^{n}}{n}$，$(n=1,2,\cdots,n)$，则（ ）",
    options=[r"有最大值，有最小值.", r"有最大值，没有最小值.",
             r"没有最大值，有最小值.", r"没有最大值，没有最小值."])

add(num=3, type="single", score=5, pages=[1], anchor="第(3)题",
    stem=r"$f(t)$ 连续，$F(x,y)=\displaystyle\int_{0}^{x-y}(x-y-t)f(t)\mathrm{d}t$，则（ ）",
    options=[
        r"$F_{x}^{\prime}(x,y)=F_{y}^{\prime}(x,y),F_{xx}^{\prime\prime}(x,y)=F_{yy}^{\prime\prime}(x,y)$.",
        r"$F_{x}^{\prime}(x,y)=F_{y}^{\prime}(x,y),F_{xx}^{\prime\prime}(x,y)=-F_{yy}^{\prime\prime}(x,y)$.",
        r"$F_{x}^{\prime}(x,y)=-F_{y}^{\prime}(x,y),F_{xx}^{\prime\prime}(x,y)=F_{yy}^{\prime\prime}(x,y)$",
        r"$F_{x}^{\prime}(x,y)=-F_{y}^{\prime}(x,y),F_{xx}^{\prime\prime}(x,y)=-F_{yy}^{\prime\prime}(x,y)$",
    ])

add(num=4, type="single", score=5, pages=[1], anchor="第(4)题",
    stem=r"$I_1=\displaystyle\int_{0}^{1}\dfrac{x}{2(1+\cos x)}\mathrm{d}x$，"
         r"$I_2=\displaystyle\int_{0}^{1}\dfrac{\ln(1+x)}{1+\cos x}\mathrm{d}x$，"
         r"$I_3=\displaystyle\int_{0}^{1}\dfrac{2x}{1+\sin x}\mathrm{d}x$，则（ ）",
    options=[r"$I_1<I_2<I_3$.", r"$I_2<I_1<I_3$.",
             r"$I_1<I_3<I_2$", r"$I_3<I_2<I_1$"])

add(num=5, type="single", score=5, pages=[2], anchor="第(5)题",
    stem=r"设 $A$ 为 3 阶矩阵，$A=\begin{pmatrix}1&0&0\\ 0&-1&0\\ 0&0&0\end{pmatrix}$，"
         r"则 $A$ 的特征值为 $1,-1,0$ 的充分必要条件是（ ）",
    options=[
        r"存在可逆矩阵 $P,Q$，使得 $A=P\Lambda Q$",
        r"存在可逆矩阵 $P$，使得 $A=P\Lambda P^{-1}$",
        r"存在正交矩阵 $Q$，使得 $A=Q\Lambda Q^{-1}$",
        r"存在可逆矩阵 $P$，使得 $A=P\Lambda P^{\mathrm{T}}$",
    ])

add(num=6, type="single", score=5, pages=[2], anchor="第(6)题",
    stem=r"设矩阵 $A=\begin{pmatrix}1&1&1\\ 1&a&a^{2}\\ 1&b&b^{2}\end{pmatrix},\boldsymbol{b}=\begin{pmatrix}1\\ 2\\ 4\end{pmatrix}$，"
         r"则线性方程组 $A\boldsymbol{x}=\boldsymbol{b}$ 解的情况为（ ）",
    options=[r"无解", r"有解", r"有无穷多解或无解", r"有唯一解或无解"])

add(num=7, type="single", score=5, pages=[2], anchor="第(7)题",
    stem=r"设 $\boldsymbol{\alpha}_1=\begin{pmatrix}\lambda\\ 1\\ 1\end{pmatrix},"
         r"\boldsymbol{\alpha}_2=\begin{pmatrix}1\\ \lambda\\ 1\end{pmatrix},"
         r"\boldsymbol{\alpha}_3=\begin{pmatrix}1\\ 1\\ \lambda\end{pmatrix},"
         r"\boldsymbol{\alpha}_4=\begin{pmatrix}1\\ \lambda\\ \lambda^{2}\end{pmatrix}$，"
         r"若向量组 $\boldsymbol{\alpha}_1,\boldsymbol{\alpha}_2,\boldsymbol{\alpha}_3$ 与 "
         r"$\boldsymbol{\alpha}_1,\boldsymbol{\alpha}_2,\boldsymbol{\alpha}_4$ 等价，则 $\lambda$ 的取值范围是（ ）",
    options=[
        r"$\{0,1\}$",
        r"$\{\lambda\mid\lambda\in R,\lambda\neq-2\}$",
        r"$\{\lambda\mid\lambda\in R,\lambda\neq-1,\lambda\neq-2\}$",
        r"$\{\lambda\mid\lambda\in R,\lambda\neq-1\}$",
    ])

add(num=8, type="single", score=5, pages=[2], anchor="第(8)题",
    stem=r"设随机变量 $X\sim N(0,4),Y\sim B\left(3,\dfrac{1}{3}\right)$，且 $X$ 与 $Y$ 不相关，"
         r"则 $D(X-3Y+1)=$（ ）",
    options=[r"$2$", r"$4$", r"$6$", r"$10$"])

add(num=9, type="single", score=5, pages=[2], anchor="第(9)题",
    stem=r"设随机变量 $X_1,X_2,\cdots,X_n$ 独立同分布，$X_1$ 的概率密度 "
         r"$f(x)=\begin{cases}1-|x|,&|x|<1,\\ 0,&\text{其他},\end{cases}$ 则 "
         r"$\dfrac{1}{n}\displaystyle\sum_{i=1}^{n}X_i^{2}$ 依概率收敛于（ ）",
    options=[r"$\dfrac{1}{8}$", r"$\dfrac{1}{6}$", r"$\dfrac{1}{3}$", r"$\dfrac{1}{2}$"])

add(num=10, type="single", score=5, pages=[2, 3], anchor="第(10)题",
    stem=r"二维随机变量 $(X,Y)$ 的联合分布律为 "
         r"$\begin{array}{|c|ccc|}\hline X\backslash Y&0&1&2\\\hline "
         r"-1&0.1&0.1&b\\ 1&a&0.1&0.1\\\hline\end{array}$ "
         r"已知事件 $\{\max(X,Y)=2\}$ 与事件 $\{\min(X,Y)=1\}$ 相互独立，则 $Cov(X,Y)=$（ ）",
    options=[r"$-0.6$", r"$-0.36$", r"$0$", r"$0.48$"])

# ---------- 二、填空题 11-16（每小题 5 分，共 30 分） ----------
add(num=11, type="blank", score=5, pages=[3], anchor="第(11)题",
    stem=r"$\lim\limits_{x\to0}\left(\dfrac{1+\mathrm{e}^{x}}{2}\right)^{\cot x}=$________.",
    options=[])

add(num=12, type="blank", score=5, pages=[3], anchor="第(12)题",
    stem=r"$\displaystyle\int_{0}^{2}\dfrac{2x-4}{x^{2}+2x+4}\mathrm{d}x=$________.",
    options=[])

add(num=13, type="blank", score=5, pages=[3], anchor="第(13)题",
    stem=r"设 $f(x)=\mathrm{e}^{\sin x}+\mathrm{e}^{-\sin x}$，$f^{\prime\prime\prime}(2\pi)=$________.",
    options=[])

add(num=14, type="blank", score=5, pages=[3], anchor="第(14)题",
    stem=r"$f(x)=\begin{cases}\mathrm{e}^{x},&0\leqslant x\leqslant1,\\ 0,&\text{其他}\end{cases}$，求 "
         r"$\displaystyle\int_{-\infty}^{+\infty}\mathrm{d}x\int_{-\infty}^{+\infty}f(x)f(y-x)\mathrm{d}y=$________.",
    options=[])

add(num=15, type="blank", score=5, pages=[3], anchor="第(15)题",
    stem=r"已知 $A$ 是 3 阶矩阵，将 $A$ 第 2 行与第 3 行互换，再将第 2 列的 $-1$ 倍加到第 1 列得矩阵 "
         r"$\begin{pmatrix}-2&1&-1\\ 1&-1&0\\ -1&0&0\end{pmatrix}$，$A^{-1}$ 为 $A$ 的逆，"
         r"则 $\mathrm{tr}\left(A^{-1}\right)=$________.",
    options=[])

add(num=16, type="blank", score=5, pages=[3], anchor="第(16)题",
    stem=r"设 $A,B,C$ 为随机事件，且 $A$ 与 $B$ 互不相容，$A$ 与 $C$ 互不相容，$B$ 与 $C$ 相互独立，"
         r"$P(A)=P(B)=P(C)=\dfrac{1}{3}$，则 $P(B\cup C\mid A\cup B\cup C)=$________.",
    options=[])

# ---------- 三、解答题 17-22（共 70 分） ----------
add(num=17, type="essay", score=10, pages=[3], anchor="第(17)题",
    stem=r"（本题满分 10 分）设函数 $y(x)$ 是微分方程 $y^{\prime}+\dfrac{1}{2\sqrt{x}}y=2+\sqrt{x}$ 的"
         r"满足 $y(1)=3$ 的解，求曲线 $y=y(x)$ 的渐近线.",
    options=[])

add(num=18, type="essay", score=12, pages=[3], anchor="第(18)题",
    stem=r"（本题满分 12 分）某单位产品产量 $Q$ 由资本投入量 $x$ 和劳动投入量 $y$ 决定，"
         r"生产函数 $Q=12x^{\frac{1}{2}}y^{\frac{1}{6}}$，销售单价 $p$ 与 $Q$ 的关系 $p=1160-1.5Q$."
         r"若单位资本投入和劳动投入的价格分别为 6 和 8，求利润最大时的产量.",
    options=[])

add(num=19, type="essay", score=12, pages=[3, 4], anchor="第(19)题",
    stem=r"（本题满分 12 分）已知区域 $D$ 为 "
         r"$\left\{(x,y)\mid y-2\leqslant x\leqslant\sqrt{4-y^{2}},0\leqslant y\leqslant2\right\}$，"
         r"计算 $I=\displaystyle\iint_{D}\dfrac{(x-y)^{2}}{x^{2}+y^{2}}\mathrm{d}x\mathrm{d}y$.",
    options=[])

add(num=20, type="essay", score=12, pages=[4], anchor="第(20)题",
    stem=r"（本题满分 12 分）求幂级数 "
         r"$\displaystyle\sum_{n=0}^{\infty}\dfrac{(-4)^{n}+1}{4^{n}(2n+1)}x^{2n}$ 的收敛域及和函数 $S(x)$.",
    options=[])

add(num=21, type="essay", score=12, pages=[4], anchor="第(21)题",
    stem=r"（本题满分 12 分）已知二次型 $f\left(x_1,x_2,x_3\right)=3x_1^{2}+4x_2^{2}+3x_3^{2}+2x_1x_3$，"
         r"(Ⅰ) 求正交变换 $\boldsymbol{x}=Q\boldsymbol{y}$ 化二次型为标准型；"
         r"(Ⅱ) 证明 $\min\limits_{x\neq0}\dfrac{f(x)}{\boldsymbol{x}^{\mathrm{T}}\boldsymbol{x}}=2$.",
    options=[])

add(num=22, type="essay", score=12, pages=[4], anchor="第(22)题",
    stem=r"（本题满分 12 分）设 $X_1,X_2,\cdots,X_n$ 为来自均值为 $\theta$ 的指数分布总体的简单随机样本，"
         r"$Y_1,Y_2,\cdots,Y_m$ 为来自均值为 $2\theta$ 的指数分布总体的简单随机样本，且两样本相互独立，"
         r"其中 $\theta(\theta>0)$ 是未知参数，利用样本 $X_1,X_2,\cdots,X_n$，$Y_1,Y_2,\cdots,Y_m$ 求 "
         r"$\theta$ 的最大似然估计量 $\hat{\theta}$，并求 $D\hat{\theta}$.",
    options=[])
