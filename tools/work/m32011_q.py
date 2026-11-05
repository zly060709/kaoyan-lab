# -*- coding: utf-8 -*-
"""2011 数学三 题干视觉转录（照录 data/math3/pages/2011/p1-p4.png）"""

ITEMS = []

def add(**kw):
    ITEMS.append(kw)

# ---------- 一、选择题 1-8（每小题 4 分，共 32 分） ----------
add(num=1, type="single", score=4, pages=[1], anchor="第(1)题",
    stem=r"已知当 $x\to0$ 时，函数 $f(x)=3\sin x-\sin 3x$ 与 $cx^{k}$ 是等价无穷小，则.",
    options=[r"$k=1,c=4$", r"$k=1,c=-4$", r"$k=3,c=4$", r"$k=3,c=-4$"])

add(num=2, type="single", score=4, pages=[1], anchor="第(2)题",
    stem=r"已知 $f(x)$ 在 $x=0$ 处可导，且 $f(0)=0$，则 $\lim\limits_{x\to0}\dfrac{x^{2}f(x)-2f(x^{3})}{x^{3}}$ 等于.",
    options=[r"$-2f'(0)$", r"$-f'(0)$", r"$f'(0)$", r"$0$"])

add(num=3, type="single", score=4, pages=[1], anchor="第(3)题",
    stem=r"设 $\{u_{n}\}$ 是数列，则下列命题正确的是.",
    options=[
        r"若 $\sum\limits_{n=1}^{\infty}u_{n}$ 收敛，则 $\sum\limits_{n=1}^{\infty}(u_{2n-1}+u_{2n})$ 收敛",
        r"若 $\sum\limits_{n=1}^{\infty}(u_{2n-1}+u_{2n})$ 收敛，则 $\sum\limits_{n=1}^{\infty}u_{n}$ 收敛",
        r"若 $\sum\limits_{n=1}^{\infty}u_{n}$ 收敛，则 $\sum\limits_{n=1}^{\infty}(u_{2n-1}-u_{2n})$ 收敛",
        r"若 $\sum\limits_{n=1}^{\infty}(u_{2n-1}-u_{2n})$ 收敛，则 $\sum\limits_{n=1}^{\infty}u_{n}$ 收敛",
    ])

add(num=4, type="single", score=4, pages=[1], anchor="第(4)题",
    stem=r"设 $I=\int_{0}^{\frac{\pi}{4}}\ln(\sin x)\mathrm{d}x$，$J=\int_{0}^{\frac{\pi}{4}}\ln(\cot x)\mathrm{d}x$，"
         r"$K=\int_{0}^{\frac{\pi}{4}}\ln(\cos x)\mathrm{d}x$，则 $I,J,K$ 的大小关系是.",
    options=[r"$I<J<K$", r"$I<K<J$", r"$J<I<K$", r"$K<J<I$"])

add(num=5, type="single", score=4, pages=[1], anchor="第(5)题",
    stem=r"设 $\boldsymbol{A}$ 为三阶矩阵，将 $\boldsymbol{A}$ 的第二列加到第一列得到矩阵 $\boldsymbol{B}$，"
         r"再交换 $\boldsymbol{B}$ 的第二行与第三行得到单位矩阵，记 "
         r"$\boldsymbol{P}_{1}=\begin{pmatrix}1&0&0\\1&1&0\\0&0&1\end{pmatrix}$，"
         r"$\boldsymbol{P}_{2}=\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}$，则 $\boldsymbol{A}=$（　　）",
    options=[
        r"$\boldsymbol{P}_{1}\boldsymbol{P}_{2}$",
        r"$\boldsymbol{P}_{1}^{-1}\boldsymbol{P}_{2}$",
        r"$\boldsymbol{P}_{2}\boldsymbol{P}_{1}$",
        r"$\boldsymbol{P}_{2}\boldsymbol{P}_{1}^{-1}$",
    ])

add(num=6, type="single", score=4, pages=[2], anchor="第(6)题",
    stem=r"设 $\boldsymbol{A}$ 为 4×3 矩阵，$\boldsymbol{\eta}_{1},\boldsymbol{\eta}_{2},\boldsymbol{\eta}_{3}$ "
         r"是非齐次线性方程组 $\boldsymbol{AX}=\boldsymbol{\beta}$ 的三个线性无关的解，"
         r"$k_{1},k_{2}$ 为任意实数，则 $\boldsymbol{AX}=\boldsymbol{\beta}$ 的通解为.",
    options=[
        r"$\dfrac{\boldsymbol{\eta}_{2}+\boldsymbol{\eta}_{3}}{2}+k_{1}(\boldsymbol{\eta}_{2}-\boldsymbol{\eta}_{1})$",
        r"$\dfrac{\boldsymbol{\eta}_{2}-\boldsymbol{\eta}_{3}}{2}+k_{2}(\boldsymbol{\eta}_{2}-\boldsymbol{\eta}_{1})$",
        r"$\dfrac{\boldsymbol{\eta}_{2}+\boldsymbol{\eta}_{3}}{2}+k_{1}(\boldsymbol{\eta}_{3}-\boldsymbol{\eta}_{1})+k_{2}(\boldsymbol{\eta}_{2}-\boldsymbol{\eta}_{1})$",
        r"$\dfrac{\boldsymbol{\eta}_{2}-\boldsymbol{\eta}_{3}}{2}+k_{1}(\boldsymbol{\eta}_{3}-\boldsymbol{\eta}_{1})+k_{2}(\boldsymbol{\eta}_{2}-\boldsymbol{\eta}_{1})$",
    ])

add(num=7, type="single", score=4, pages=[2], anchor="第(7)题",
    stem=r"设 $F_{1}(x),F_{2}(x)$ 为两个分布函数，其相应的概率密度 $f_{1}(x),f_{2}(x)$ 是连续函数，"
         r"则必为概率密度的是.",
    options=[
        r"$f_{1}(x)f_{2}(x)$",
        r"$2f_{2}(x)F_{1}(x)$",
        r"$f_{1}(x)F_{2}(x)$",
        r"$f_{1}(x)F_{2}(x)+f_{2}(x)F_{1}(x)$",
    ])

add(num=8, type="single", score=4, pages=[2], anchor="第(8)题",
    stem=r"设总体 $X$ 服从参数为 $\lambda(\lambda>0)$ 的泊松分布，$X_{1},X_{2},\cdots,X_{n}(n\geqslant2)$ "
         r"为来自该总体的简单随机样本，则对应的统计量 $T_{1}=\dfrac{1}{n}\sum\limits_{i=1}^{n}X_{i}$，"
         r"$T_{2}=\dfrac{1}{n-1}\sum\limits_{i=1}^{n-1}X_{i}+\dfrac{1}{n}X_{n}$ 满足.",
    options=[
        r"$ET_{1}>ET_{2},DT_{1}>DT_{2}$",
        r"$ET_{1}>ET_{2},DT_{1}<DT_{2}$",
        r"$ET_{1}<ET_{2},DT_{1}>DT_{2}$",
        r"$ET_{1}<ET_{2},DT_{1}<DT_{2}$",
    ])

# ---------- 二、填空题 9-14（每小题 4 分，共 24 分） ----------
add(num=9, type="blank", score=4, pages=[2], anchor="第(9)题",
    stem=r"设 $f(x)=\lim\limits_{t\to0}x(1+3t)^{\frac{x}{t}}$，则 $f'(x)=$______.",
    options=[])

add(num=10, type="blank", score=4, pages=[2], anchor="第(10)题",
    stem=r"设函数 $z=\left(1+\dfrac{x}{y}\right)^{\frac{x}{y}}$，则 $\mathrm{d}z\big|_{(1,1)}=$______.",
    options=[])

add(num=11, type="blank", score=4, pages=[2], anchor="第(11)题",
    stem=r"曲线 $\tan\left(x+y+\dfrac{\pi}{4}\right)=e^{y}$ 在点 $(0,0)$ 处的切线方程为______.",
    options=[])

add(num=12, type="blank", score=4, pages=[2], anchor="第(12)题",
    stem=r"曲线 $y=\sqrt{x^{2}-1}$，直线 $x=2$ 及 $x$ 轴所围成的平面图形绕 $x$ 轴旋转所成的旋转体的"
         r"体积为______.",
    options=[])

add(num=13, type="blank", score=4, pages=[2], anchor="第(13)题",
    stem=r"设二次型 $f(x_{1},x_{2},x_{3})=\boldsymbol{x}^{\mathrm{T}}\boldsymbol{Ax}$ 的秩为 1，"
         r"$\boldsymbol{A}$ 的各行元素之和为 3，则 $f$ 在正交变换 $\boldsymbol{x}=\boldsymbol{Qy}$ 下的"
         r"标准形为______.",
    options=[])

add(num=14, type="blank", score=4, pages=[3], anchor="第(14)题",
    stem=r"设二维随机变量 $(X,Y)$ 服从 $N(\mu,\mu,\sigma^{2},\sigma^{2},0)$，则 $E(XY^{2})=$______.",
    options=[])

# ---------- 三、解答题 15-23（共 94 分：15-19 每题 10 分，20-23 每题 11 分） ----------
add(num=15, type="essay", score=10, pages=[3], anchor="第(15)题",
    stem=r"（本题满分 10 分）求极限 $\lim\limits_{x\to0}\dfrac{\sqrt{1+2\sin x}-x-1}{x\ln(1+x)}$.",
    options=[])

add(num=16, type="essay", score=10, pages=[3], anchor="第(16)题",
    stem=r"（本题满分 10 分）已知函数 $f(u,v)$ 具有二阶连续偏导数，$f(1,1)=2$ 是 $f(u,v)$ 的极"
         r"值，$z=f\left((x+y),f(x,y)\right)$，求 $\dfrac{\partial^{2}z}{\partial x\partial y}\Big|_{x=1,y=1}$.",
    options=[])

add(num=17, type="essay", score=10, pages=[3], anchor="第(17)题",
    stem=r"（本题满分 10 分）求 $\int\dfrac{\arcsin\sqrt{x}+\ln x}{\sqrt{x}}\mathrm{d}x$.",
    options=[])

add(num=18, type="essay", score=10, pages=[3], anchor="第(18)题",
    stem=r"（本题满分 10 分）证明方程 $4\arctan x-x+\dfrac{4\pi}{3}-\sqrt{3}=0$ 恰有两个实根.",
    options=[])

add(num=19, type="essay", score=10, pages=[3], anchor="第(19)题",
    stem=r"（本题满分 10 分）设函数 $f(x)$ 在 $[0,1]$ 内有连续的导数，$f(0)=1$，且"
         r"$\iint\limits_{D_{t}}f'(x+y)\mathrm{d}x\mathrm{d}y=\iint\limits_{D_{t}}f(t)\mathrm{d}x\mathrm{d}y$，"
         r"其中 $D_{t}=\{(x,y)|0\leqslant x\leqslant t,0\leqslant y\leqslant t-x\}(0<t\leqslant1)$，"
         r"求 $f(x)$ 的表达式.",
    options=[])

add(num=20, type="essay", score=11, pages=[3], anchor="第(20)题",
    stem=r"（本小题满分 11 分）设向量组 $\boldsymbol{\alpha}_{1}=(1,0,1)^{T}$，"
         r"$\boldsymbol{\alpha}_{2}=(0,1,1)^{T}$，$\boldsymbol{\alpha}_{3}=(1,3,5)^{T}$，不能由"
         r"向量组 $\boldsymbol{\beta}_{1}=(1,1,1)^{T}$，$\boldsymbol{\beta}_{2}=(1,2,3)^{T}$，"
         r"$\boldsymbol{\beta}_{3}=(3,4,a)^{T}$ 线性表出."
         r"（1）求 $a$ 的值."
         r"（2）将 $\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3}$ 由 "
         r"$\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}$ 线性表出.",
    options=[])

add(num=21, type="essay", score=11, pages=[3], anchor="第(21)题",
    stem=r"（本小题满分 11 分）$\boldsymbol{A}$ 为三阶实对称矩阵，$r(\boldsymbol{A})=2$ 且 "
         r"$\boldsymbol{A}\begin{pmatrix}1&1\\0&0\\-1&1\end{pmatrix}=\begin{pmatrix}-1&1\\0&0\\1&1\end{pmatrix}$."
         r"（1）求 $\boldsymbol{A}$ 的特征值与特征向量."
         r"（2）求矩阵 $\boldsymbol{A}$.",
    options=[])

add(num=22, type="essay", score=11, pages=[3, 4], anchor="第(22)题",
    stem=r"（本题满分 11 分）设随机变量 $X$ 与 $Y$ 的概率分布分别为"
         r"$X$：$0$，$1$；$P$：$\dfrac{1}{3}$，$\dfrac{2}{3}$；"
         r"$Y$：$-1$，$0$，$1$；$P$：$\dfrac{1}{3}$，$\dfrac{1}{3}$，$\dfrac{1}{3}$；"
         r"且 $P\{X^{2}=Y^{2}\}=1$."
         r"（Ⅰ）求二维随机变量 $(X,Y)$ 的概率分布；"
         r"（Ⅱ）求 $Z=XY$ 的概率分布；"
         r"（Ⅲ）求 $X$ 与 $Y$ 的相关系数 $\rho_{XY}$.",
    options=[])

add(num=23, type="essay", score=11, pages=[4], anchor="第(23)题",
    stem=r"（本题满分 11 分）二维随机变量 $(X,Y)$ 在 $G$ 上服从均匀分布，$G$ 由 $x-y=0$，"
         r"$x+y=2$ 与 $y=0$ 围成."
         r"（Ⅰ）求边缘概率密度 $f_{X}(x)$；"
         r"（Ⅱ）求 $f_{X|Y}(x|y)$.",
    options=[])
