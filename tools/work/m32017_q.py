# -*- coding: utf-8 -*-
"""2017 数学三 题干视觉转录（照录 data/math3/pages/2017/p1-p4.png）"""

ITEMS = []

def add(**kw):
    ITEMS.append(kw)

# ---------- 一、选择题 1-8（每小题 4 分，共 32 分） ----------
add(num=1, type="single", score=4, pages=[1], anchor="第(1)题",
    stem=r"若函数 $f(x)=\begin{cases}\dfrac{1-\cos\sqrt{x}}{ax},&x>0\\ b,&x\leqslant0\end{cases}$ 在 $x=0$ 连续，则（ ）",
    options=[r"$ab=\dfrac{1}{2}$", r"$ab=-\dfrac{1}{2}$", r"$ab=0$", r"$ab=2$"])

add(num=2, type="single", score=4, pages=[1], anchor="第(2)题",
    stem=r"二元函数 $z=xy(3-x-y)$ 的极值点是（ ）",
    options=[r"$(0,0)$", r"$(0,3)$", r"$(3,0)$", r"$(1,1)$"])

add(num=3, type="single", score=4, pages=[1], anchor="第(3)题",
    stem=r"设函数 $f(x)$ 可导，且 $f(x)f'(x)>0$, 则（ ）",
    options=[r"$f(1)>f(-1)$", r"$f(1)<f(-1)$",
             r"$|f(1)|>|f(-1)|$", r"$|f(1)|<|f(-1)|$"])

add(num=4, type="single", score=4, pages=[1], anchor="第(4)题",
    stem=r"设级数 $\sum\limits_{n=2}^{\infty}\left[\sin\dfrac{1}{n}-k\ln\left(1-\dfrac{1}{n}\right)\right]$ 收敛，则 $k=$（ ）",
    options=[r"$1$", r"$2$", r"$-1$", r"$-2$"])

add(num=5, type="single", score=4, pages=[1], anchor="第(5)题",
    stem=r"设 $\boldsymbol{\alpha}$ 为 $n$ 维单位列向量，$\boldsymbol{E}$ 为 $n$ 阶单位矩阵，则（ ）",
    options=[r"$\boldsymbol{E}-\boldsymbol{\alpha}\boldsymbol{\alpha}^{T}$ 不可逆",
             r"$\boldsymbol{E}+\boldsymbol{\alpha}\boldsymbol{\alpha}^{T}$ 不可逆",
             r"$\boldsymbol{E}+2\boldsymbol{\alpha}\boldsymbol{\alpha}^{T}$ 不可逆",
             r"$\boldsymbol{E}-2\boldsymbol{\alpha}\boldsymbol{\alpha}^{T}$ 不可逆"])

add(num=6, type="single", score=4, pages=[1], anchor="第(6)题",
    stem=r"已知矩阵 $\boldsymbol{A}=\begin{pmatrix}2&0&0\\ 0&2&1\\ 0&0&1\end{pmatrix}$，"
         r"$\boldsymbol{B}=\begin{pmatrix}2&1&0\\ 0&2&0\\ 0&0&1\end{pmatrix}$，"
         r"$\boldsymbol{C}=\begin{pmatrix}1&0&0\\ 0&2&0\\ 0&0&2\end{pmatrix}$,则（ ）",
    options=[r"$\boldsymbol{A}$ 与 $\boldsymbol{C}$ 相似，$\boldsymbol{B}$ 与 $\boldsymbol{C}$ 相似",
             r"$\boldsymbol{A}$ 与 $\boldsymbol{C}$ 相似，$\boldsymbol{B}$ 与 $\boldsymbol{C}$ 不相似",
             r"$\boldsymbol{A}$ 与 $\boldsymbol{C}$ 不相似，$\boldsymbol{B}$ 与 $\boldsymbol{C}$ 相似",
             r"$\boldsymbol{A}$ 与 $\boldsymbol{C}$ 不相似，$\boldsymbol{B}$ 与 $\boldsymbol{C}$ 不相似"])

add(num=7, type="single", score=4, pages=[1, 2], anchor="第(7)题",
    stem=r"设 $\boldsymbol{A},\boldsymbol{B},\boldsymbol{C}$ 为三个随机事件,且 $\boldsymbol{A}$ 与 $\boldsymbol{C}$ 相互独立, "
         r"$\boldsymbol{B}$ 与 $\boldsymbol{C}$ 相互独立,则 $\boldsymbol{A}\cup\boldsymbol{B}$ 与 $\boldsymbol{C}$ 相互独立的充要条件是（ ）",
    options=[r"$\boldsymbol{A}$ 与 $\boldsymbol{B}$ 相互独立",
             r"$\boldsymbol{A}$ 与 $\boldsymbol{B}$ 互不相容",
             r"$\boldsymbol{AB}$ 与 $\boldsymbol{C}$ 相互独立",
             r"$\boldsymbol{AB}$ 与 $\boldsymbol{C}$ 互不相容"])

add(num=8, type="single", score=4, pages=[2], anchor="第(8)题",
    stem=r"设 $\boldsymbol{X}_{1},\boldsymbol{X}_{2}\cdots\boldsymbol{X}_{n}\,(n\geqslant2)$ 为来自总体 $N(\mu,1)$ 的简单随机样本，"
         r"记 $\overline{\boldsymbol{X}}=\dfrac{1}{n}\sum\limits_{i=1}^{n}\boldsymbol{X}_{i}$，则下列结论中不正确的是（ ）",
    options=[r"$\sum\limits_{i=1}^{n}(\boldsymbol{X}_{i}-\mu)^{2}$ 服从 $\chi^{2}$ 分布",
             r"$2(\boldsymbol{X}_{n}-\boldsymbol{X}_{1})^{2}$ 服从 $\chi^{2}$ 分布",
             r"$\sum\limits_{i=1}^{n}(\boldsymbol{X}_{i}-\overline{\boldsymbol{X}})^{2}$ 服从 $\chi^{2}$ 分布",
             r"$n(\overline{\boldsymbol{X}}-\mu)^{2}$ 服从 $\chi^{2}$ 分布"])

# ---------- 二、填空题 9-14（每小题 4 分，共 24 分） ----------
add(num=9, type="blank", score=4, pages=[2], anchor="第(9)题",
    stem=r"$\displaystyle\int_{-\pi}^{\pi}\left(\sin^{3}x+\sqrt{\pi^{2}-x^{2}}\right)dx=$________.",
    options=[])

add(num=10, type="blank", score=4, pages=[2], anchor="第(10)题",
    stem=r"差分方程 $y_{t+1}-2y_{t}=2^{t}$ 的通解为 $y_{t}=$________.",
    options=[])

add(num=11, type="blank", score=4, pages=[2], anchor="第(11)题",
    stem=r"设生产某产品的平均成本 $\overline{C}(Q)=1+e^{-Q}$，其中 $Q$ 为产量,则边际成本为________.",
    options=[])

add(num=12, type="blank", score=4, pages=[2], anchor="第(12)题",
    stem=r"设函数 $f(x,y)$ 具有一阶连续偏导数，且 $df(x,y)=ye^{y}dx+x(1+y)e^{y}dy$，$f(0,0)=0$，"
         r"则 $f(x,y)=$________.",
    options=[])

add(num=13, type="blank", score=4, pages=[2], anchor="第(13)题",
    stem=r"设矩阵 $\boldsymbol{A}=\begin{pmatrix}1&0&1\\ 1&1&2\\ 0&1&1\end{pmatrix}$，"
         r"$\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}$ 为线性无关的三维列向量，"
         r"则向量组 $\boldsymbol{A\alpha}_{1},\boldsymbol{A\alpha}_{2},\boldsymbol{A\alpha}_{3}$ 的秩为________.",
    options=[])

add(num=14, type="blank", score=4, pages=[2], anchor="第(14)题",
    stem=r"设随机变量 $\boldsymbol{X}$ 的概率分布为 $P\{\boldsymbol{X}=-2\}=\dfrac{1}{2}$，"
         r"$P\{\boldsymbol{X}=1\}=a$，$P\{\boldsymbol{X}=3\}=b$，若 $EX=0$，则 $DX=$________.",
    options=[])

# ---------- 三、解答题 15-23（共 94 分：15-19 各 10 分，20-23 各 11 分） ----------
add(num=15, type="essay", score=10, pages=[2], anchor="第(15)题",
    stem=r"(本题满分 10 分) 求 $\lim\limits_{x\to0^{+}}\dfrac{\displaystyle\int_{0}^{x}\sqrt{x-t}e^{t}dt}{\sqrt{x^{3}}}$.",
    options=[])

add(num=16, type="essay", score=10, pages=[3], anchor="第(16)题",
    stem=r"(本题满分 10 分) 计算积分 $\displaystyle\iint\limits_{D}\dfrac{y^{3}}{\left(1+x^{2}+y^{4}\right)^{2}}dxdy$，"
         r"其中 $D$ 是第一象限中以曲线 $y=\sqrt{x}$ 与 $x$ 轴为边界的无界区域.",
    options=[])

add(num=17, type="essay", score=10, pages=[3], anchor="第(17)题",
    stem=r"(本题满分 10 分) 求 $\lim\limits_{n\to\infty}\sum\limits_{k=1}^{n}\dfrac{k}{n^{2}}\ln\left(1+\dfrac{k}{n}\right)$.",
    options=[])

add(num=18, type="essay", score=10, pages=[3], anchor="第(18)题",
    stem=r"(本题满分 10 分) 已知方程 $\dfrac{1}{\ln(1+x)}-\dfrac{1}{x}=k$ 在区间 $(0,1)$ 内有实根,确定常数 $k$ 的取值范围.",
    options=[])

add(num=19, type="essay", score=10, pages=[3], anchor="第(19)题",
    stem=r"(本题满分 10 分) 设 $a_{0}=1,a_{1}=0$, $a_{n+1}=\dfrac{1}{n+1}\left(na_{n}+a_{n-1}\right)$ $(n=1,2,\cdots)$, "
         r"$S(x)$ 为幂级数 $\sum\limits_{n=0}^{\infty}a_{n}x^{n}$ 的和函数，"
         r"(1)证明幂级数 $\sum\limits_{n=0}^{\infty}a_{n}x^{n}$ 的收敛半径不小于 1."
         r"(2)证明 $(1-x)S'(x)-xS(x)=0$ $(x\in(-1,1))$,并求 $S(x)$ 的表达式.",
    options=[])

add(num=20, type="essay", score=11, pages=[3], anchor="第(20)题",
    stem=r"(本题满分 11 分) 三阶矩阵 $\boldsymbol{A}=(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3})$ "
         r"有 3 个不同的特征值，且 $\boldsymbol{\alpha}_{3}=\boldsymbol{\alpha}_{1}+2\boldsymbol{\alpha}_{2}$"
         r"(1) 证明 $r(\boldsymbol{A})=2$."
         r"(2) 如果 $\boldsymbol{\beta}=\boldsymbol{\alpha}_{1}+\boldsymbol{\alpha}_{2}+\boldsymbol{\alpha}_{3}$，"
         r"求方程组 $\boldsymbol{Ax}=\boldsymbol{\beta}$ 的通解.",
    options=[])

add(num=21, type="essay", score=11, pages=[3], anchor="第(21)题",
    stem=r"(本题满分 11 分) 设二次型 $f(x_{1},x_{2},x_{3})=2x_{1}^{2}-x_{2}^{2}+ax_{3}^{2}+2x_{1}x_{2}-8x_{1}x_{3}+2x_{2}x_{3}$ "
         r"在正交变换 $\boldsymbol{x}=\boldsymbol{Qy}$ 下标准形为 $\lambda_{1}y_{1}^{2}+\lambda_{2}y_{2}^{2}$，"
         r"求 $a$ 的值及一个正交矩阵 $\boldsymbol{Q}$.",
    options=[])

add(num=22, type="essay", score=11, pages=[3], anchor="第(22)题",
    stem=r"(本题满分 11 分) 设随机变量 $\boldsymbol{X}$ 与 $\boldsymbol{Y}$ 相互独立，"
         r"且 $\boldsymbol{X}$ 的概率分布为 $P\{\boldsymbol{X}=0\}=P\{\boldsymbol{X}=2\}=\dfrac{1}{2}$,"
         r"$\boldsymbol{Y}$ 的概率密度为 $f(y)=\begin{cases}2y,&0<y<1\\ 0,&\text{其他}\end{cases}$."
         r"(1) 求 $P\{\boldsymbol{Y}\leqslant E\boldsymbol{Y}\}$."
         r"(2) 求 $\boldsymbol{Z}=\boldsymbol{X}+\boldsymbol{Y}$ 的概率密度.",
    options=[])

add(num=23, type="essay", score=11, pages=[4], anchor="第(23)题",
    stem=r"(本题满分 11 分) 某工程师为了了解一台天平的精度，用该天平对一物体的质量做 $n$ 次测量，"
         r"该物体的质量 $\mu$ 是已知的，设 $n$ 次测量的结果 $\boldsymbol{X}_{1},\boldsymbol{X}_{2},\cdots,\boldsymbol{X}_{n}$ 相互独立，"
         r"且均服从正态分布 $N\left(\mu,\sigma^{2}\right)$，该工程师记录的是 $n$ 次测量的绝对误差 "
         r"$\boldsymbol{Z}_{i}=\left|\boldsymbol{X}_{i}-\mu\right|,(i=1,2,\cdots,n)$，"
         r"利用 $\boldsymbol{Z}_{1},\boldsymbol{Z}_{2},\cdots,\boldsymbol{Z}_{n}$ 估计 $\sigma$."
         r"(1) 求 $\boldsymbol{Z}_{i}$ 的概率密度."
         r"(2) 利用一阶矩求 $\sigma$ 的矩估计量."
         r"(3) 求 $\sigma$ 的最大似然估计.",
    options=[])
