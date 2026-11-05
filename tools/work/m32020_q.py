# -*- coding: utf-8 -*-
"""2020 数学三 题干视觉转录（照录 data/math3/pages/2020/p1-p4.png）"""

ITEMS = []

def add(**kw):
    ITEMS.append(kw)

# ---------- 一、选择题 1-8（每小题 4 分，共 32 分） ----------
add(num=1, type="single", score=4, pages=[1], anchor="第(1)题",
    stem=r"设 $\lim\limits_{x\to a}\dfrac{f(x)-a}{x-a}=b$，则 $\lim\limits_{x\to a}\dfrac{\sin f(x)-\sin a}{x-a}=$（　）",
    options=[r"$b\sin a$", r"$b\cos a$", r"$b\sin f(a)$", r"$b\cos f(a)$"])

add(num=2, type="single", score=4, pages=[1], anchor="第(2)题",
    stem=r"数 $f(x)=\dfrac{e^{\frac{1}{x-1}}\ln|1+x|}{(e^{x}-1)(x-2)}$，则第二类间断点个数为（　）",
    options=[r"$1$", r"$2$", r"$3$", r"$4$"])

add(num=3, type="single", score=4, pages=[1], anchor="第(3)题",
    stem=r"对奇函数 $f(x)$ 在 $(-\infty,+\infty)$ 上有连续导数，则（　）",
    options=[
        r"$\int_{0}^{x}\left[\cos f(t)+f'(t)\right]dt$ 是奇函数",
        r"$\int_{0}^{x}\left[\cos f(t)+f'(t)\right]dt$ 是偶函数",
        r"$\int_{0}^{x}\left[\cos f'(t)+f(t)\right]dt$ 是奇函数",
        r"$\int_{0}^{x}\left[\cos f'(t)+f(t)\right]dt$ 是偶函数",
    ])

add(num=4, type="single", score=4, pages=[1], anchor="第(4)题",
    stem=r"已知幂级数 $\sum\limits_{n=1}^{\infty}na_{n}(x-2)^{n}$ 的收敛区间为 $(-2,6)$，"
         r"则 $\sum\limits_{n=1}^{\infty}a_{n}(x+1)^{2n}$ 的收敛区间为（　）",
    options=[r"$(-2,6)$", r"$(-3,1)$", r"$(-5,3)$", r"$(-17,15)$"])

add(num=5, type="single", score=4, pages=[1], anchor="第(5)题",
    stem=r"设四阶矩阵 $A=(a_{ij})$ 不可逆，$a_{12}$ 的代数余子式 $A_{12}\neq0$，"
         r"$\boldsymbol{a}_{1},\boldsymbol{a}_{2},\boldsymbol{a}_{3},\boldsymbol{a}_{4}$ 为矩阵 $A$ 的列"
         r"向量组，$A^{*}$ 为 $A$ 的伴随矩阵，则 $A^{*}\boldsymbol{x}=\boldsymbol{0}$ 的通解为（　）",
    options=[
        r"$\boldsymbol{x}=k_{1}\boldsymbol{a}_{1}+k_{2}\boldsymbol{a}_{2}+k_{3}\boldsymbol{a}_{3}$",
        r"$\boldsymbol{x}=k_{1}\boldsymbol{a}_{1}+k_{2}\boldsymbol{a}_{2}+k_{3}\boldsymbol{a}_{4}$",
        r"$\boldsymbol{x}=k_{1}\boldsymbol{a}_{1}+k_{2}\boldsymbol{a}_{3}+k_{3}\boldsymbol{a}_{4}$",
        r"$\boldsymbol{x}=k_{1}\boldsymbol{a}_{2}+k_{2}\boldsymbol{a}_{3}+k_{3}\boldsymbol{a}_{4}$",
    ])

add(num=6, type="single", score=4, pages=[1], anchor="第(6)题",
    stem=r"设 $A$ 为三阶矩阵，$\boldsymbol{a}_{1},\boldsymbol{a}_{2}$ 为 $A$ 的特征值 1 对应的两个线性无关的特征向量，"
         r"$\boldsymbol{a}_{3}$ 为 $A$ 的特征值 $-1$ 的特征向量．若存在可逆矩阵 $P$，"
         r"使得 $P^{-1}AP=\begin{pmatrix}1&0&0\\ 0&-1&0\\ 0&0&1\end{pmatrix}$，则 $P$ 可为（　）",
    options=[
        r"$(\boldsymbol{a}_{1}+\boldsymbol{a}_{3},\boldsymbol{a}_{2},-\boldsymbol{a}_{3})$",
        r"$(\boldsymbol{a}_{1}+\boldsymbol{a}_{2},\boldsymbol{a}_{2},-\boldsymbol{a}_{3})$",
        r"$(\boldsymbol{a}_{1}+\boldsymbol{a}_{3},-\boldsymbol{a}_{3},\boldsymbol{a}_{2})$",
        r"$(\boldsymbol{a}_{1}+\boldsymbol{a}_{2},-\boldsymbol{a}_{3},\boldsymbol{a}_{2})$",
    ])

add(num=7, type="single", score=4, pages=[2], anchor="第(7)题",
    stem=r"设 $A,B,C$ 为三个随机事件，且"
         r"$P(A)=P(B)=P(C)=\dfrac{1}{4}$,$P(AB)=0$,$P(AC)=P(BC)=\dfrac{1}{12}$，"
         r"则 $A,B,C$ 中恰有一个事件发生的概率为（　）",
    options=[r"$\dfrac{3}{4}$", r"$\dfrac{2}{3}$", r"$\dfrac{1}{2}$", r"$\dfrac{5}{12}$"])

add(num=8, type="single", score=4, pages=[2], anchor="第(8)题",
    stem=r"若二维随机变量 $(X,Y)$ 服从 $N(0;0;1,4;-\dfrac{1}{2})$，则下列服从标准正态分布且与 $X$ 独立"
         r"的是（　）",
    options=[r"$\dfrac{\sqrt{5}}{5}(X+Y)$", r"$\dfrac{\sqrt{5}}{5}(X-Y)$",
             r"$\dfrac{\sqrt{3}}{3}(X+Y)$", r"$\dfrac{\sqrt{3}}{3}(X-Y)$"])

# ---------- 二、填空题 9-14（每小题 4 分，共 24 分） ----------
add(num=9, type="blank", score=4, pages=[2], anchor="第(9)题",
    stem=r"设函数 $z=\arctan[xy+\sin(x+y)]$,则 $\mathrm{d}z\big|_{(0,\pi)}=$________.",
    options=[])

add(num=10, type="blank", score=4, pages=[2], anchor="第(10)题",
    stem=r"曲线 $x+y+\mathrm{e}^{2xy}=0$ 在点 $(0,-1)$ 处的切线方程为________.",
    options=[])

add(num=11, type="blank", score=4, pages=[2], anchor="第(11)题",
    stem=r"设某厂家生产某产品的产量为 $Q$,已知成本函数 $C(Q)=100+13Q$,设该产品的单价为"
         r"$p$，需求量关于价格的函数为 $Q(p)=\dfrac{800}{p+3}-2$,则利润取得最大值时的产量为________.",
    options=[])

add(num=12, type="blank", score=4, pages=[2], anchor="第(12)题",
    stem=r"设平面区域 $D=\left\{(x,y)\mid\dfrac{x}{2}\leqslant y\leqslant\dfrac{1}{1+x^{2}},0\leqslant x\leqslant1\right\}$,"
         r"$D$ 绕 $y$ 轴旋转所得旋转体的体积为________.",
    options=[])

add(num=13, type="blank", score=4, pages=[2], anchor="第(13)题",
    stem=r"行列式 $\begin{vmatrix}a&0&-1&1\\ 0&a&1&-1\\ -1&1&a&0\\ 1&-1&0&a\end{vmatrix}=$________.",
    options=[])

add(num=14, type="blank", score=4, pages=[2], anchor="第(14)题",
    stem=r"随机变量 $X$ 的分布律为 $P(X=k)=\dfrac{1}{2^{k}}$,$k=1,2,...$,$Y$ 为 $X$ 被 3 除的余数,则 $EY=$",
    options=[])

# ---------- 三、解答题 15-23（共 94 分：15~19 每题 10 分，20~23 每题 11 分，以各题"（本题满分 X 分）"行为准） ----------
add(num=15, type="essay", score=10, pages=[2, 3], anchor="第(15)题",
    stem=r"设 $a,b$ 为常数，且当 $n\to\infty$ 时，$\left(1+\dfrac{1}{n}\right)^{n}-e$ 与 $\dfrac{b}{n^{a}}$ 为等价无穷小，求 $a,b$ 的值.",
    options=[])

add(num=16, type="essay", score=10, pages=[3], anchor="第(16)题",
    stem=r"求函数 $f(x,y)=x^{3}+8y^{3}-xy$ 的极值.",
    options=[])

add(num=17, type="essay", score=10, pages=[3], anchor="第(17)题",
    stem=r"设函数 $y=f(x)$ 满足 $y''+2y'+5y=0$，且有 $f(0)=1$,$f'(0)=-1$."
         r"（I）求 $f(x)$；"
         r"（II）设 $a_{n}=\int_{n\pi}^{+\infty}f(x)dx$，求 $\sum\limits_{n=1}^{\infty}a_{n}$.",
    options=[])

add(num=18, type="essay", score=10, pages=[3], anchor="第(18)题",
    stem=r"区域 $D=\left\{(x,y)\mid x^{2}+y^{2}\leqslant1,y\geqslant0\right\}$,连续函数满足 "
         r"$f(x,y)=y\sqrt{1-x^{2}}+x\iint\limits_{D}f(x,y)dxdy$，"
         r"计算 $\iint\limits_{D}xf(x,y)dxdy$.",
    options=[])

add(num=19, type="essay", score=10, pages=[3], anchor="第(19)题",
    stem=r"设函数 $f(x)$ 在 $[0,2]$ 上具有连续导数. $f(0)=f(2)=0$，"
         r"$M=\max\limits_{x\in[0,2]}\left\{\left|f(x)\right|\right\}$. 证:"
         r"（I）存在 $\xi\in(0,2)$ 使 $\left|f'(\xi)\right|\geqslant M$；"
         r"（II）若对任意 $x\in(0,2)$,$\left|f'(x)\right|\leqslant M$,则 $M=0$.",
    options=[])

add(num=20, type="essay", score=11, pages=[3], anchor="第(20)题",
    stem=r"设二次型 $f(x_{1},x_{2})=x_{1}^{2}-4x_{1}x_{2}+4x_{2}^{2}$ 经正交变换 "
         r"$\begin{pmatrix}x_{1}\\ x_{2}\end{pmatrix}=Q\begin{pmatrix}y_{1}\\ y_{2}\end{pmatrix}$ 化为二次型"
         r"$g(y_{1},y_{2})=ay_{1}^{2}+4y_{1}y_{2}+by_{2}^{2}$，其中 $a\geqslant b$．求:"
         r"（I）求 $a,b$ 的值；"
         r"（II）求正交矩阵 $Q$.",
    options=[])

add(num=21, type="essay", score=11, pages=[3, 4], anchor="第(21)题",
    stem=r"设 $A$ 为二阶矩阵，$P=(\boldsymbol{\alpha},A\boldsymbol{\alpha})$，"
         r"$\boldsymbol{\alpha}$ 是非零向量且不是 $A$ 的特征向量."
         r"（I）证明矩阵 $P$ 可逆；"
         r"（II）若 $A^{2}\boldsymbol{\alpha}+A\boldsymbol{\alpha}-6\boldsymbol{\alpha}=\boldsymbol{0}$，"
         r"求 $P^{-1}AP$ 并判断 $A$ 是否相似于对角矩阵.",
    options=[])

add(num=22, type="essay", score=11, pages=[4], anchor="第(22)题",
    stem=r"二维随机变量 $(X,Y)$ 在区域 $D=\left\{(x,y)\middle|0<y<\sqrt{1-x^{2}}\right\}$ 上服从均匀分布，且"
         r"$Z_{1}=\begin{cases}1,&X-Y>0\\ 0,&X-Y\leqslant0\end{cases}$，"
         r"$Z_{2}=\begin{cases}1,&X+Y>0\\ 0,&X+Y\leqslant0\end{cases}$. 求:"
         r"（I）二维随机变量 $(Z_{1},Z_{2})$ 的概率分布；"
         r"（II）求 $Z_{1},Z_{2}$ 得相关系数.",
    options=[])

add(num=23, type="essay", score=11, pages=[4], anchor="第(23)题",
    stem=r"设某元件的使用寿命 $T$ 的分布函数为 $F(t)=\begin{cases}1-e^{-\left(\frac{t}{\theta}\right)^{m}},&t\geqslant0\\ 0,&t<0\end{cases}$，"
         r"其中 $\theta,m$ 为参数且大于零."
         r"（I）计算概率 $P\left\{T>t\right\}$ 与 $P(T>s+t|T>s)$，其中 $s>0,t>0$；"
         r"（II）任取 $\boldsymbol{n}$ 个元件试验，其寿命分别为 $t_{1},t_{2},...,t_{n}$，"
         r"若 $\boldsymbol{m}$ 已知，求 $\theta$ 得最大似然估计值 $\hat{\theta}$.",
    options=[])
