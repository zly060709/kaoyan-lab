# -*- coding: utf-8 -*-
"""2011 数学一 题干视觉转录（照录 data/math1.pages/pages/2011/p1-p4.png，解析卷 p5-p13 另见 a1-a3）"""

ITEMS = []

def add(**kw):
    ITEMS.append(kw)

# ---------- 一、选择题：1～8 小题，每小题 4 分，共 32 分。下列每题给出的四个选项中，只有一个选项是符合题目要求的．请将所选项前的字母填在答题纸指定位置上. ----------

add(num=1, type="single", score=4, pages=[1], anchor="第(1)题",
    stem=r"曲线 $y=(x-1)(x-2)^{2}(x-3)^{3}(x-4)^{4}$ 的一个拐点是（　　）",
    options=[r"$(1,0)$", r"$(2,0)$", r"$(3,0)$", r"$(4,0)$"])

add(num=2, type="single", score=4, pages=[1], anchor="第(2)题",
    stem=r"设数列 $\{a_{n}\}$ 单调减少，$\lim\limits_{n\to\infty}a_{n}=0$, $S_{n}=\sum\limits_{k=1}^{n}a_{k}$ $(n=1,2,\cdots)$ 无界，"
         r"则幂级数 $\sum\limits_{k=1}^{\infty}a_{k}(x-1)^{k}$ 的收敛域是（　　）",
    options=[r"$(-1,1]$", r"$[-1,1)$", r"$[0,2)$", r"$(0,2]$"])

add(num=3, type="single", score=4, pages=[1], anchor="第(3)题",
    stem=r"设函数 $f(x)$ 具有二阶连续导数，且 $f(x)>0, f'(0)=0$，则函数 $z=f(x)\ln f(y)$ 在"
         r"点 $(0,0)$ 处取得极小值的一个充分条件是（　　）",
    options=[r"$f(0)>1,f''(0)>0$", r"$f(0)>1,f''(0)<0$",
             r"$f(0)<1,f''(0)>0$", r"$f(0)<1,f''(0)<0$"])

add(num=4, type="single", score=4, pages=[1], anchor="第(4)题",
    stem=r"设 $I=\int_{0}^{\frac{\pi}{4}}\ln(\sin x)dx, J=\int_{0}^{\frac{\pi}{4}}\ln(\cot x)dx, K=\int_{0}^{\frac{\pi}{4}}\ln(\cos x)dx$，则 $I,J,K$ 的大小关系是（　　）",
    options=[r"$I<J<K$", r"$I<K<J$", r"$J<I<K$", r"$K<J<I$"])

add(num=5, type="single", score=4, pages=[1], anchor="第(5)题",
    stem=r"$\boldsymbol{A}$ 为三阶矩阵，将 $\boldsymbol{A}$ 的第二列加到第一列得到矩阵 $\boldsymbol{B}$，再交换 $\boldsymbol{B}$ 的第二行与第三行"
         r"得到单位矩阵，记 $\boldsymbol{P}_{1}=\begin{pmatrix}1&0&0\\1&1&0\\0&0&1\end{pmatrix}$, $\boldsymbol{P}_{2}=\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}$，则 $\boldsymbol{A}=$（　　）",
    options=[r"$\boldsymbol{P}_{1}\boldsymbol{P}_{2}$", r"$\boldsymbol{P}_{1}^{-1}\boldsymbol{P}_{2}$",
             r"$\boldsymbol{P}_{2}\boldsymbol{P}_{1}$", r"$\boldsymbol{P}_{2}\boldsymbol{P}_{1}^{-1}$"])

add(num=6, type="single", score=4, pages=[1], anchor="第(6)题",
    stem=r"设 $\boldsymbol{A}=(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4})$，$\boldsymbol{A}^{*}$ 是 $\boldsymbol{A}$ 的伴随矩阵，若 $(1,0,1,0)^{T}$ 是方程组 $\boldsymbol{Ax}=\boldsymbol{0}$ 的一个"
         r"基础解系，则 $\boldsymbol{A}^{*}\boldsymbol{x}=\boldsymbol{0}$ 的基础解系可为（　　）",
    options=[r"$\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2}$", r"$\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{3}$",
             r"$\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}$", r"$\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}$"])

add(num=7, type="single", score=4, pages=[2], anchor="第(7)题",
    stem=r"设 $F_{1}(x),F_{2}(x)$ 为两个分布函数，其相应的概率密度 $f_{1}(x),f_{2}(x)$ 是连续函数，则必为"
         r"概率密度的是（　　）",
    options=[r"$f_{1}(x)f_{2}(x)$", r"$2f_{2}(x)F_{1}(x)$",
             r"$f_{1}(x)F_{2}(x)$", r"$f_{1}(x)F_{2}(x)+f_{2}(x)F_{1}(x)$"])

add(num=8, type="single", score=4, pages=[2], anchor="第(8)题",
    stem=r"设随机变量 $X$ 与 $Y$ 相互独立，且 $EX$ 与 $EY$ 存在. 记 $U=\max\{X,Y\}$，"
         r"$V=\min\{X,Y\}$，则 $EUV$ 等于（　　）",
    options=[r"$EU\cdot EV$", r"$EX\cdot EY$", r"$EU\cdot EY$", r"$EX\cdot EV$"])

# ---------- 二、填空题：9～14 小题，每小题 4 分，共 24 分. 请将答案写在答题纸指定位置上. ----------

add(num=9, type="blank", score=4, pages=[2], anchor="第(9)题",
    stem=r"曲线 $y=\int_{0}^{x}\tan tdt$ $(0\leqslant x\leqslant\dfrac{\pi}{4})$ 的弧长 $s=$________.",
    options=[])

add(num=10, type="blank", score=4, pages=[2], anchor="第(10)题",
    stem=r"微分方程 $y'+y=e^{-x}\cos x$ 满足条件 $y(0)=0$ 的解为 $y=$________.",
    options=[])

add(num=11, type="blank", score=4, pages=[2], anchor="第(11)题",
    stem=r"设函数 $F(x,y)=\int_{0}^{xy}\dfrac{\sin t}{1+t^{2}}dt$，则 $\dfrac{\partial^{2}F}{\partial x^{2}}\Big|_{x=0,y=2}=$________.",
    options=[])

add(num=12, type="blank", score=4, pages=[2], anchor="第(12)题",
    stem=r"设 $L$ 是柱面方程 $x^{2}+y^{2}=1$ 与平面 $z=x+y$ 的交线，从 $z$ 轴正向往 $z$ 轴负"
         r"向看去为逆时针方向，则曲线积分 $\oint_{L}xz\,dx+x\,dy+\dfrac{y^{2}}{2}dz=$__________.",
    options=[])

add(num=13, type="blank", score=4, pages=[2], anchor="第(13)题",
    stem=r"若二次曲面的方程 $x^{2}+3y^{2}+z^{2}+2axy+2xz+2yz=4$，经过正交变换化为"
         r"$y_{1}^{2}+4z_{1}^{2}=4$，则 $a=$________.",
    options=[])

add(num=14, type="blank", score=4, pages=[2], anchor="第(14)题",
    stem=r"设二维随机变量 $(X,Y)$ 服从 $N(\mu,\mu,\sigma^{2},\sigma^{2},0)$，则 $E(XY^{2})=$________.",
    options=[])

# ---------- 三、解答题：15～23 小题，共 94 分. 解答应写出文字说明、证明过程或演算步骤. 请将答案写在答题纸指定位置上. ----------

add(num=15, type="essay", score=10, pages=[2], anchor="第(15)题",
    stem=r"（本题满分 10 分）求极限 $\lim\limits_{x\to0}\left[\dfrac{\ln(1+x)}{x}\right]^{\frac{1}{e^{x}-1}}$.",
    options=[])

add(num=16, type="essay", score=10, pages=[2, 3], anchor="第(16)题",
    stem=r"（本题满分 10 分）设函数 $z=f(xy,yg(x))$，其中函数 $f$ 具有二阶连续偏导数，函数"
         r"$g(x)$ 可导且在 $x=1$ 处取得极值 $g(1)=1$，求 $\dfrac{\partial^{2}z}{\partial x\partial y}\Big|_{\substack{x=1\\ y=1}}$.",
    options=[])

add(num=17, type="essay", score=10, pages=[3], anchor="第(17)题",
    stem=r"（本题满分 10 分）求方程 $k\arctan x-x=0$ 不同实根的个数，其中 $k$ 为参数.",
    options=[])

add(num=18, type="essay", score=10, pages=[3], anchor="第(18)题",
    stem=r"（本题满分 10 分）①证明对任意正整数 $f(x)$，都有 $\dfrac{1}{n+1}<\ln(1+\dfrac{1}{n})<\dfrac{1}{n}$ 成立；"
         r"②$a_{n}=1+\dfrac{1}{2}+\cdots\dfrac{1}{n}-\ln n(n=1,2,\cdots)$，证明数列 $\{a_{n}\}$ 收敛.",
    options=[])

add(num=19, type="essay", score=10, pages=[3], anchor="第(19)题",
    stem=r"（本题满分 11 分）已知函数 $f(x,y)$ 具有二阶连续偏导数，且"
         r"$f(1,y)=0$, $f(x,1)=0$, $\iint\limits_{D}f(x,y)dxdy=a$."
         r"其中 $D=\{(x,y)|0\leqslant x\leqslant1,0\leqslant y\leqslant1\}$，计算二重积分 $\iint\limits_{D}xyf''_{xy}(x,y)dxdy$.",
    options=[])

add(num=20, type="essay", score=11, pages=[3], anchor="第(20)题",
    stem=r"（本小题满 11 分）设向量组 $\boldsymbol{\alpha}_{1}=(1,0,1)^{T},\boldsymbol{\alpha}_{2}=(0,1,1)^{T},\boldsymbol{\alpha}_{3}=(1,3,5)^{T}$，不能由向量"
         r"组 $\boldsymbol{\beta}_{1}=(1,1,1)^{T},\boldsymbol{\beta}_{2}=(1,2,3)^{T},\boldsymbol{\beta}_{3}=(3,4,a)^{T}$ 线性表出."
         r"（I）求 $a$ 的值."
         r"（II）将 $\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3}$ 由 $\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}$ 线性表出.",
    options=[])

add(num=21, type="essay", score=11, pages=[3], anchor="第(21)题",
    stem=r"（本小题满分 11 分）$\boldsymbol{A}$ 为三阶实对称矩阵，$\boldsymbol{A}$ 的秩为 2，且"
         r"$\boldsymbol{A}\begin{pmatrix}1&1\\0&0\\-1&1\end{pmatrix}=\begin{pmatrix}-1&1\\0&0\\1&1\end{pmatrix}$."
         r"（I）求 $\boldsymbol{A}$ 的特征值与特征向量."
         r"（II）求矩阵 $\boldsymbol{A}$.",
    options=[])

add(num=22, type="essay", score=11, pages=[3], anchor="第(22)题",
    stem=r"（本题满分 11 分）设随机变量 $X$ 与 $Y$ 的概率分布分别为"
         r"$\begin{array}{c|cc} X & 0 & 1\\ \hline P & 1/3 & 2/3 \end{array}$ 与 "
         r"$\begin{array}{c|ccc} Y & -1 & 0 & 1\\ \hline P & 1/3 & 1/3 & 1/3 \end{array}$"
         r"且 $P\left\{X^{2}=Y^{2}\right\}=1$."
         r"（I）求二维随机变量 $(X,Y)$ 的概率分布；"
         r"（II）求 $Z=XY$ 的概率分布；"
         r"（III）求 $X$ 与 $Y$ 的相关系数 $\rho_{XY}$.",
    options=[])

add(num=23, type="essay", score=11, pages=[4], anchor="第(23)题",
    stem=r"（本题满分 11 分）设 $X_{1},X_{2},\cdots,X_{n}$ 为来自正态总体 $N(\mu_{0},\sigma^{2})$ 的简单随机样本，其中"
         r"$\mu_{0}$ 已知，$\sigma^{2}>0$ 未知. $\overline{X}$ 和 $S^{2}$ 分别表示样本均值和样本方差."
         r"（I）求参数 $\sigma^{2}$ 的最大似然估计 $\hat{\sigma}^{2}$；"
         r"（II）计算 $E\hat{\sigma}^{2}$ 和 $D\hat{\sigma}^{2}$.",
    options=[])
