# -*- coding: utf-8 -*-
"""2021 数学三 题干视觉转录（照录 data/math3/pages/2021/p1-p4.png）"""

ITEMS = []

def add(**kw):
    ITEMS.append(kw)

# ---------- 一、选择题 1-10（每小题 5 分，共 50 分） ----------
add(num=1, type="single", score=5, pages=[1], anchor="第(1)题",
    stem=r"当 $x\to0$ 时，$\displaystyle\int_{0}^{x^{2}}\left(e^{t^{3}}-1\right)dt$ 是 $x^{7}$ 的（ ）",
    options=[r"低阶无穷小", r"等价无穷小", r"高阶无穷小", r"同阶但非等价无穷小"])

add(num=2, type="single", score=5, pages=[1], anchor="第(2)题",
    stem=r"$f(x)=\begin{cases}\dfrac{e^{x}-1}{x},&x\neq0,\\ 1,&x=0\end{cases}$ 在 $x=0$ 处（ ）",
    options=[r"连续且取得极大值", r"连续且取得极小值",
             r"可导且导数为零", r"可导且导数不为零"])

add(num=3, type="single", score=5, pages=[1], anchor="第(3)题",
    stem=r"函数 $f(x)=ax-b\ln x\,(a>0)$ 有 2 个零点，则 $\dfrac{b}{a}$ 的取值范围是（ ）",
    options=[r"$(e,+\infty)$", r"$(0,e)$",
             r"$\left(0,\dfrac{1}{e}\right)$", r"$\left(\dfrac{1}{e},+\infty\right)$"])

add(num=4, type="single", score=5, pages=[1], anchor="第(4)题",
    stem=r"设函数 $f(x,y)$ 可微且 $f(x+1,e^{x})=x(x+1)^{2}$，$f(x,x^{2})=2x^{2}\ln x$，"
         r"则 $df(1,1)=$（ ）",
    options=[r"$dx+dy$", r"$dx-dy$", r"$dy$", r"$-dy$"])

add(num=5, type="single", score=5, pages=[1], anchor="第(5)题",
    stem=r"二次型 $f(x_{1},x_{2},x_{3})=(x_{1}+x_{2})^{2}+(x_{2}+x_{3})^{2}-(x_{3}-x_{1})^{2}$"
         r"的正惯性指数和负惯性指数分别为（ ）",
    options=[r"$2,0$", r"$1,1$", r"$2,1$", r"$1,2$"])

add(num=6, type="single", score=5, pages=[1], anchor="第(6)题",
    stem=r"设 $A=(\boldsymbol{a}_{1},\boldsymbol{a}_{2},\boldsymbol{a}_{3},\boldsymbol{a}_{4})$ 为 4 阶正交矩阵，"
         r"若矩阵 $B=\begin{pmatrix}\boldsymbol{a}_{1}^{\mathrm{T}}\\ \boldsymbol{a}_{2}^{\mathrm{T}}\\ "
         r"\boldsymbol{a}_{3}^{\mathrm{T}}\end{pmatrix}$，$\boldsymbol{\beta}=\begin{pmatrix}1\\ 1\\ 1\end{pmatrix}$，"
         r"$k$ 表示任意常数，则线性方程组 $B\boldsymbol{x}=\boldsymbol{\beta}$ 的通解为 $\boldsymbol{x}=$（ ）",
    options=[
        r"$\boldsymbol{a}_{2}+\boldsymbol{a}_{3}+\boldsymbol{a}_{4}+k\boldsymbol{a}_{1}$",
        r"$\boldsymbol{a}_{1}+\boldsymbol{a}_{3}+\boldsymbol{a}_{4}+k\boldsymbol{a}_{2}$",
        r"$\boldsymbol{a}_{1}+\boldsymbol{a}_{2}+\boldsymbol{a}_{4}+k\boldsymbol{a}_{3}$",
        r"$\boldsymbol{a}_{1}+\boldsymbol{a}_{2}+\boldsymbol{a}_{3}+k\boldsymbol{a}_{4}$",
    ])

add(num=7, type="single", score=5, pages=[2], anchor="第(7)题",
    stem=r"已知矩阵 $A=\begin{pmatrix}1&0&-1\\ 2&-1&1\\ -1&2&-5\end{pmatrix}$，"
         r"若存在下三角可逆矩阵 $P$ 和上三角可逆矩阵 $Q$，使得 $PAQ$ 为对角矩阵，则 $P$、$Q$ 分别取（ ）",
    options=[
        r"$\begin{pmatrix}1&0&0\\ 0&1&0\\ 0&0&1\end{pmatrix}$，$\begin{pmatrix}1&0&1\\ 0&1&3\\ 0&0&1\end{pmatrix}$",
        r"$\begin{pmatrix}1&0&0\\ 2&-1&0\\ -3&2&1\end{pmatrix}$，$\begin{pmatrix}1&0&0\\ 0&1&0\\ 0&0&1\end{pmatrix}$",
        r"$\begin{pmatrix}1&0&0\\ 2&-1&0\\ -3&2&1\end{pmatrix}$，$\begin{pmatrix}1&0&1\\ 0&1&3\\ 0&0&1\end{pmatrix}$",
        r"$\begin{pmatrix}1&0&0\\ 0&1&0\\ 1&3&1\end{pmatrix}$，$\begin{pmatrix}1&2&-3\\ 0&-1&2\\ 0&0&1\end{pmatrix}$",
    ])

add(num=8, type="single", score=5, pages=[2], anchor="第(8)题",
    stem=r"设 $A,B$ 为随机事件，且 $0<P(B)<1$，下列命题中为假命题的是（ ）",
    options=[
        r"若 $P(A|B)=P(A)$，则 $P(A|\overline{B})=P(A)$.",
        r"若 $P(A|B)>P(A)$，则 $P(\overline{A}|\overline{B})>P(\overline{A})$",
        r"若 $P(A|B)>P(A|\overline{B})$，则 $P(A|B)>P(A)$",
        r"若 $P(A|A\cup B)>P(\overline{A}|A\cup B)$，则 $P(A)>P(B)$",
    ])

add(num=9, type="single", score=5, pages=[2], anchor="第(9)题",
    stem=r"设 $(X_{1},Y_{1}),(X_{2},Y_{2}),\cdots,(X_{n},Y_{n})$ 为来自总体 "
         r"$N(\mu_{1},\mu_{2};\sigma_{1}^{2},\sigma_{2}^{2};\rho)$ 的简单随机样本，"
         r"令 $\theta=\mu_{1}-\mu_{2}$，$\overline{X}=\dfrac{1}{n}\sum\limits_{i=1}^{n}X_{i}$，"
         r"$\overline{Y}=\dfrac{1}{n}\sum\limits_{i=1}^{n}Y_{i}$，$\hat{\theta}=\overline{X}-\overline{Y}$，则（ ）",
    options=[
        r"$E(\hat{\theta})=\theta,D(\hat{\theta})=\dfrac{\sigma_{1}^{2}+\sigma_{2}^{2}}{n}$",
        r"$E(\hat{\theta})=\theta,D(\hat{\theta})=\dfrac{\sigma_{1}^{2}+\sigma_{2}^{2}-2\rho\sigma_{1}\sigma_{2}}{n}$",
        r"$E(\hat{\theta})\neq\theta,D(\hat{\theta})=\dfrac{\sigma_{1}^{2}+\sigma_{2}^{2}}{n}$",
        r"$E(\hat{\theta})\neq\theta,D(\hat{\theta})=\dfrac{\sigma_{1}^{2}+\sigma_{2}^{2}-2\rho\sigma_{1}\sigma_{2}}{n}$",
    ])

add(num=10, type="single", score=5, pages=[2], anchor="第(10)题",
    stem=r"总体 $X$ 的概率分布为 $P\{X=1\}=\dfrac{1-\theta}{2}$，$P\{X=2\}=P\{X=3\}=\dfrac{1+\theta}{4}$，"
         r"利用来自总体 $X$ 的样本观察值 $1,3,2,2,1,3,1,2$ 可得 $\theta$ 的最大似然估计值为（ ）",
    options=[r"$\dfrac{1}{4}$", r"$\dfrac{3}{8}$", r"$\dfrac{1}{2}$", r"$\dfrac{5}{8}$"])

# ---------- 二、填空题 11-16（每小题 5 分，共 30 分） ----------
add(num=11, type="blank", score=5, pages=[3], anchor="第(11)题",
    stem=r"若 $y=\cos e^{-\sqrt{x}}$，$\dfrac{dy}{dx}\Big|_{x=1}=$________.",
    options=[])

add(num=12, type="blank", score=5, pages=[3], anchor="第(12)题",
    stem=r"$\displaystyle\int_{\sqrt{5}}^{5}\dfrac{x}{\sqrt{|x^{2}-9|}}dx=$________.",
    options=[])

add(num=13, type="blank", score=5, pages=[3], anchor="第(13)题",
    stem=r"设 $D$ 由 $y=\sqrt{x}\sin\pi x\,(0\leqslant x\leqslant1)$ 与 $x$ 轴围成，"
         r"则 $D$ 绕 $x$ 轴旋转的旋转体体积为________.",
    options=[])

add(num=14, type="blank", score=5, pages=[3], anchor="第(14)题",
    stem=r"差分方程 $\Delta y_{t}=t$ 的通解为 $y_{t}=$________.",
    options=[])

add(num=15, type="blank", score=5, pages=[3], anchor="第(15)题",
    stem=r"多项式 $f(x)=\begin{vmatrix}x&x&1&2x\\ 1&x&2&-1\\ 2&1&x&1\\ 2&-1&1&x\end{vmatrix}$"
         r"的 $x^{3}$ 项的系数为________.",
    options=[])

add(num=16, type="blank", score=5, pages=[3], anchor="第(16)题",
    stem=r"甲乙两个盒子中各装 2 个红球 2 个白球，先从甲盒中任取一球，观察颜色放入乙盒，"
         r"再从乙盒中任取一球，令 $X,Y$ 分别表示从甲乙两盒中取得红球的个数，"
         r"则 $X,Y$ 的相关系数 $\rho_{XY}=$________.",
    options=[])

# ---------- 三、解答题 17-22（共 70 分） ----------
add(num=17, type="essay", score=10, pages=[3], anchor="第(17)题",
    stem=r"已知 $\lim\limits_{x\to0}\Bigl[\alpha\arctan\dfrac{1}{x}+(1+|x|)^{\frac{1}{x}}\Bigr]$ 存在，求 $\alpha$ 的值.",
    options=[])

add(num=18, type="essay", score=12, pages=[3], anchor="第(18)题",
    stem=r"求函数 $f(x,y)=2\ln|x|+\dfrac{(x-1)^{2}+y^{2}}{2x^{2}}$ 的极值.",
    options=[])

add(num=19, type="essay", score=12, pages=[3], anchor="第(19)题",
    stem=r"设有界区域 $D$ 是圆 $x^{2}+y^{2}=1$ 和直线 $y=x$ 以及 $x$ 轴在第一象限围成的部分，"
         r"计算二重积分 $\displaystyle\iint\limits_{D}e^{(x+y)^{2}}(x^{2}-y^{2})\mathrm{d}x\mathrm{d}y$.",
    options=[])

add(num=20, type="essay", score=12, pages=[3], anchor="第(20)题",
    stem=r"设 $n$ 为正整数，$y=y_{n}(x)$ 是微分方程 $xy'-(n+1)y=0$ 满足条件 "
         r"$y_{n}(1)=\dfrac{1}{n(n+1)}$ 的解."
         r"（I）求 $y_{n}(x)$；"
         r"（II）求级数 $\displaystyle\sum_{n=1}^{\infty}y_{n}(x)$ 的收敛域及和函数.",
    options=[])

add(num=21, type="essay", score=12, pages=[4], anchor="第(21)题",
    stem=r"设矩阵 $A=\begin{pmatrix}2&1&0\\ 1&2&0\\ 1&a&b\end{pmatrix}$ 仅有两个不同的特征值，"
         r"若 $A$ 相似于对角矩阵，求 $a,b$ 的值."
         r"求逆矩阵 $P$，使得 $P^{-1}AP=\Lambda$.",
    options=[])

add(num=22, type="essay", score=12, pages=[4], anchor="第(22)题",
    stem=r"在区间 $(0,2)$ 上随机取一点，将该区间分成两段，较短一段的长度记为 $X$，"
         r"较长一段的长度记为 $Y$，令 $Z=\dfrac{Y}{X}$."
         r"（I）求 $X$ 的概率密度;"
         r"（II）求 $Z$ 的概率密度;"
         r"（III）求 $E\Bigl(\dfrac{X}{Y}\Bigr)$.",
    options=[])
