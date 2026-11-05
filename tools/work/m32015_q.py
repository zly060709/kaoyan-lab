# -*- coding: utf-8 -*-
"""2015 数学三 题干视觉转录（照录 data/math3/pages/2015/p1-p4.png）"""

ITEMS = []

def add(**kw):
    ITEMS.append(kw)

# ---------- 一、选择题 1-8（每小题 4 分，共 32 分） ----------
add(num=1, type="single", score=4, pages=[1], anchor="第(1)题",
    stem=r"设 $\{x_{n}\}$ 是数列,下列命题中不正确的是（　）",
    options=[
        r"若 $\lim\limits_{n\to\infty}x_{n}=a$ ,则 $\lim\limits_{n\to\infty}x_{2n}=\lim\limits_{n\to\infty}x_{2n+1}=a$",
        r"若 $\lim\limits_{n\to\infty}x_{2n}=\lim\limits_{n\to\infty}x_{2n+1}=a$，则 $\lim\limits_{n\to\infty}x_{n}=a$",
        r"若 $\lim\limits_{n\to\infty}x_{n}=a$ ,则 $\lim\limits_{n\to\infty}x_{3n}=\lim\limits_{n\to\infty}x_{3n+1}=a$",
        r"若 $\lim\limits_{n\to\infty}x_{3n}=\lim\limits_{n\to\infty}x_{3n+1}=a$ ,则 $\lim\limits_{n\to\infty}x_{n}=a$",
    ])

add(num=2, type="single", score=4, pages=[1], anchor="第(2)题",
    stem=r"设函数 $f(x)$ 在 $(-\infty,+\infty)$ 内连续,其 2 阶导函数 $f''(x)$ 的图形如右图所示,"
         r"则曲线 $y=f(x)$ 的拐点个数为（　）",
    options=[r"$0$", r"$1$", r"$2$", r"$3$"])

add(num=3, type="single", score=4, pages=[1], anchor="第(3)题",
    stem=r"设 $D=\left\{(x,y)\middle|x^{2}+y^{2}\leq2x,x^{2}+y^{2}\leq2y\right\}$,函数 $f(x,y)$ 在 $D$ 上连续,则"
         r"$\iint\limits_{D}f(x,y)\mathrm{d}x\mathrm{d}y=$（　）",
    options=[
        r"$\int_{0}^{\frac{\pi}{4}}\mathrm{d}\theta\int_{0}^{2\cos\theta}f\left(r\cos\theta,r\sin\theta\right)r\mathrm{d}r"
        r"+\int_{\frac{\pi}{4}}^{\frac{\pi}{2}}\mathrm{d}\theta\int_{0}^{2\sin\theta}f\left(r\cos\theta,r\sin\theta\right)r\mathrm{d}r$",
        r"$\int_{0}^{\frac{\pi}{4}}\mathrm{d}\theta\int_{0}^{2\sin\theta}f\left(r\cos\theta,r\sin\theta\right)r\mathrm{d}r"
        r"+\int_{\frac{\pi}{4}}^{\frac{\pi}{2}}\mathrm{d}\theta\int_{0}^{2\cos\theta}f\left(r\cos\theta,r\sin\theta\right)r\mathrm{d}r$",
        r"$2\int_{0}^{1}\mathrm{d}x\int_{1-\sqrt{1-x^{2}}}^{x}f\left(x,y\right)\mathrm{d}y$",
        r"$2\int_{0}^{1}\mathrm{d}x\int_{x}^{\sqrt{2x-x^{2}}}f\left(x,y\right)\mathrm{d}y$",
    ])

add(num=4, type="single", score=4, pages=[1], anchor="第(4)题",
    stem=r"下列级数中发散的是（　）",
    options=[
        r"$\sum\limits_{n=1}^{\infty}\dfrac{n}{3^{n}}$",
        r"$\sum\limits_{n=1}^{\infty}\dfrac{1}{\sqrt{n}}\ln(1+\dfrac{1}{n})$",
        r"$\sum\limits_{n=2}^{\infty}\dfrac{\left(-1\right)^{n}+1}{\ln n}$",
        r"$\sum\limits_{n=1}^{\infty}\dfrac{n!}{n^{n}}$",
    ])

add(num=5, type="single", score=4, pages=[2], anchor="第(5)题",
    stem=r"设矩阵 $\boldsymbol{A}=\begin{pmatrix}1&1&1\\ 1&2&a\\ 1&4&a^{2}\end{pmatrix}$，"
         r"$\boldsymbol{b}=\begin{pmatrix}1\\ d\\ d^{2}\end{pmatrix}$，若集合 $\Omega=\{1,2\}$，则线性方程组"
         r"$\boldsymbol{Ax}=\boldsymbol{b}$ 有无穷多解的充分必要条件为（　）",
    options=[
        r"$a\notin\Omega,d\notin\Omega$", r"$a\notin\Omega,d\in\Omega$",
        r"$a\in\Omega,d\notin\Omega$", r"$a\in\Omega,d\in\Omega$",
    ])

add(num=6, type="single", score=4, pages=[2], anchor="第(6)题",
    stem=r"设二次型 $f=(x_{1},x_{2},x_{3})$ 在正交变换 $\boldsymbol{x}=\boldsymbol{Py}$ 下的标准形为 $2y_{1}^{2}+y_{2}^{2}-y_{3}^{2}$，其"
         r"中 $\boldsymbol{P}=(\boldsymbol{e}_{1},\boldsymbol{e}_{2},\boldsymbol{e}_{3})$，若 $\boldsymbol{Q}=(\boldsymbol{e}_{1},-\boldsymbol{e}_{3},\boldsymbol{e}_{2})$ 则 $f=(x_{1},x_{2},x_{3})$ 在正交变换 $\boldsymbol{x}=\boldsymbol{Qy}$ 下的"
         r"标准形为（　）",
    options=[
        r"$2y_{1}^{2}-y_{2}^{2}+y_{3}^{2}$", r"$2y_{1}^{2}+y_{2}^{2}-y_{3}^{2}$",
        r"$2y_{1}^{2}-y_{2}^{2}-y_{3}^{2}$", r"$2y_{1}^{2}+y_{2}^{2}+y_{3}^{2}$",
    ])

add(num=7, type="single", score=4, pages=[2], anchor="第(7)题",
    stem=r"若 $A,B$ 为任意两个随机事件,则（　）",
    options=[
        r"$P\left(AB\right)\leq P\left(A\right)P\left(B\right)$",
        r"$P\left(AB\right)\geq P\left(A\right)P\left(B\right)$",
        r"$P\left(AB\right)\leq\dfrac{P\left(A\right)+P\left(B\right)}{2}$",
        r"$P\left(AB\right)\geq\dfrac{P\left(A\right)+P\left(B\right)}{2}$",
    ])

add(num=8, type="single", score=4, pages=[2], anchor="第(8)题",
    stem=r"设总体 $X\sim B\left(m,\theta\right)$, $X_{1},X_{2},\ldots,X_{n}$ 为来自该总体的简单随机样本, $\overline{X}$ 为样本均值,"
         r"则 $E\left[\sum\limits_{i=1}^{n}\left(X_{i}-\overline{X}\right)^{2}\right]=$（　）",
    options=[
        r"$(m-1)n\theta\left(1-\theta\right)$", r"$m\left(n-1\right)\theta\left(1-\theta\right)$",
        r"$(m-1)\left(n-1\right)\theta\left(1-\theta\right)$", r"$mn\theta\left(1-\theta\right)$",
    ])

# ---------- 二、填空题 9-14（每小题 4 分，共 24 分） ----------
add(num=9, type="blank", score=4, pages=[2], anchor="第(9)题",
    stem=r"$\lim\limits_{x\to0}\dfrac{\ln(\cos x)}{x^{2}}=$________.",
    options=[])

add(num=10, type="blank", score=4, pages=[2], anchor="第(10)题",
    stem=r"设函数 $f(x)$ 连续, $\varphi(x)=\int_{0}^{x^{2}}xf(t)\mathrm{d}t$,若 $\varphi(1)=1$,$\varphi'(1)=5$,则 $f(1)=$________.",
    options=[])

add(num=11, type="blank", score=4, pages=[2], anchor="第(11)题",
    stem=r"若函数 $z=z(x,y)$ 由方程 $\mathrm{e}^{x+2y+3z}+xyz=1$ 确定,则 $\mathrm{d}z\Big|_{(0,0)}=$________.",
    options=[])

add(num=12, type="blank", score=4, pages=[3], anchor="第(12)题",
    stem=r"设函数 $y=y(x)$ 是微分方程 $y''+y'-2y=0$ 的解,且在 $x=0$ 处 $y(x)$ 取得极值 3,"
         r"则 $y(x)=$________.",
    options=[])

add(num=13, type="blank", score=4, pages=[3], anchor="第(13)题",
    stem=r"设 3 阶矩阵 $\boldsymbol{A}$ 的特征值为 $2,-2,1$, $\boldsymbol{B}=\boldsymbol{A}^{2}-\boldsymbol{A}+\boldsymbol{E}$,其中 $\boldsymbol{E}$ 为 3 阶单位矩阵,则行"
         r"列式$\left|\boldsymbol{B}\right|=$________.",
    options=[])

add(num=14, type="blank", score=4, pages=[3], anchor="第(14)题",
    stem=r"设二维随机变量 $(X,Y)$ 服从正态分布 $N(1,0;1,1;0)$，则 $P\{XY-Y<0\}=$____.",
    options=[])

# ---------- 三、解答题 15-23（共 94 分：15-19 各 10 分，20-23 各 11 分） ----------
add(num=15, type="essay", score=10, pages=[3], anchor="第(15)题",
    stem=r"设函数 $f(x)=x+a\ln(1+x)+bx\sin x,g(x)=kx^{3}$.若 $f(x)$ 与 $g(x)$ 在 $x\to0$ 时是等价"
         r"无穷小,求 $a,b,k$ 的值.",
    options=[])

add(num=16, type="essay", score=10, pages=[3], anchor="第(16)题",
    stem=r"计算二重积分 $\iint\limits_{D}x(x+y)dxdy$，其中 $D=\left\{(x,y)\middle|x^{2}+y^{2}\leq2,y\geq x^{2}\right\}$.",
    options=[])

add(num=17, type="essay", score=10, pages=[3], anchor="第(17)题",
    stem=r"为了实现利润的最大化,厂商需要对某商品确定其定价模型,设 $Q$ 为该商品的需求量,"
         r"$P$ 为价格, $MC$ 为边际成本, $\eta$ 为需求弹性 $\left(\eta>0\right)$."
         r"（I）证明定价模型为 $P=\dfrac{MC}{1-\dfrac{1}{\eta}}$；"
         r"（II）若该商品的成本函数为 $C(Q)=1600+Q^{2}$，需求函数为 $Q=40-P$，试由（I）中的定"
         r"价模型确定此商品的价格.",
    options=[])

add(num=18, type="essay", score=10, pages=[3], anchor="第(18)题",
    stem=r"设函数 $f(x)$ 在定义域 $I$ 上的导数大于零,若对任意的 $x_{0}\in I$，曲线 $y=f(x)$ 在点"
         r"$(x_{0},f(x_{0}))$ 处的切线与直线 $x=x_{0}$ 及 $x$ 轴所围成区域的面积恒为 4,且 $f(0)=2$，求 $f(x)$"
         r"表达式.",
    options=[])

add(num=19, type="essay", score=10, pages=[3, 4], anchor="第(19)题",
    stem=r"（I）设函数 $u(x),v(x)$ 可导,利用导数定义证明 $\left[u(x)v(x)\right]'=u'(x)v(x)+u(x)v'(x)$;"
         r"（II）设函数 $u_{1}(x),u_{2}(x),\cdots,u_{n}(x)$ 可导, $f(x)=u_{1}(x)u_{2}(x)\cdots u_{n}(x)$，写出 $f'(x)$ 的求导公"
         r"式.",
    options=[])

add(num=20, type="essay", score=11, pages=[4], anchor="第(20)题",
    stem=r"设矩阵 $\boldsymbol{A}=\begin{pmatrix}a&1&0\\ 1&a&-1\\ 0&1&a\end{pmatrix}$,且 $\boldsymbol{A}^{3}=\boldsymbol{O}$."
         r"（I）求 $a$ 的值；"
         r"（II）若矩阵 $\boldsymbol{X}$ 满足 $\boldsymbol{X}-\boldsymbol{XA}^{2}-\boldsymbol{AX}+\boldsymbol{AXA}^{2}=\boldsymbol{E}$，其中 $\boldsymbol{E}$ 为 3 阶单位矩阵,求 $\boldsymbol{X}$.",
    options=[])

add(num=21, type="essay", score=11, pages=[4], anchor="第(21)题",
    stem=r"设矩阵 $\boldsymbol{A}=\begin{pmatrix}0&2&-3\\ -1&3&-3\\ 1&-2&a\end{pmatrix}$ 相似于矩阵 $\boldsymbol{B}=\begin{pmatrix}1&-2&0\\ 0&b&0\\ 0&3&1\end{pmatrix}$."
         r"（I）求 $a,b$ 的值；"
         r"（II）求可逆矩阵 $\boldsymbol{P}$,使 $\boldsymbol{P}^{-1}\boldsymbol{AP}$ 为对角矩阵.",
    options=[])

add(num=22, type="essay", score=11, pages=[4], anchor="第(22)题",
    stem=r"设随机变量 $X$ 的概率密度为 $f(x)=\begin{cases}2^{-x}\ln2,&x>0\\ 0,&x\leq0\end{cases}$"
         r"对 $X$ 进行独立重复的观测,直到第 2 个大于 3 的观测值出现时停止,记 $Y$ 为观测次数"
         r"（I）求 $Y$ 的概率分布；"
         r"（II）求 $E(Y)$.",
    options=[])

add(num=23, type="essay", score=11, pages=[4], anchor="第(23)题",
    stem=r"设总体 $X$ 的概率密度为"
         r"$f(x,\theta)=\begin{cases}\dfrac{1}{1-\theta},&\theta\leq x\leq1,\\ 0,&\text{其他},\end{cases}$"
         r"其中 $\theta$ 为未知参数，$X_{1},X_{2},\cdots,X_{n}$ 为来自该总体的简单随机样本."
         r"（I）求 $\theta$ 的矩估计量；"
         r"（II）求 $\theta$ 的最大似然估计.",
    options=[])
