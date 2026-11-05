# -*- coding: utf-8 -*-
"""2010 数学三 解析 解答题 15-23（原卷 p7-p12，逐字照录）"""

A = {}

A[15] = (r"e^{-1}", [
    r"【详解】",
    r"原式等于 $\lim\limits_{x\to+\infty}e^{\frac{1}{\ln x}\ln(x^{\frac{1}{x}}-1)}"
    r"=e^{\lim\limits_{x\to+\infty}\frac{\ln(e^{\frac{\ln x}{x}}-1)}{\ln x}}=e^{A}$，",
    r"其中 $A=\lim\limits_{x\to+\infty}\dfrac{\ln(e^{\frac{\ln x}{x}}-1)}{\ln x}"
    r"=\lim\limits_{x\to+\infty}\dfrac{\dfrac{1}{e^{\frac{\ln x}{x}}-1}\cdot e^{\frac{\ln x}{x}}\cdot\dfrac{1-\ln x}{x^{2}}}{\dfrac{1}{x}}"
    r"=\lim\limits_{x\to+\infty}\dfrac{1}{e^{\frac{\ln x}{x}}-1}\cdot e^{\frac{\ln x}{x}}\cdot\dfrac{1-\ln x}{x}$",
    r"$=\lim\limits_{x\to+\infty}\dfrac{1}{\ln x}\cdot\dfrac{1-\ln x}{x}=\lim\limits_{x\to+\infty}\dfrac{1-\ln x}{\ln x}=-1$",
    r"所以原极限 $=e^{-1}$.",
])

A[16] = (r"\dfrac{14}{15}", [
    r"【详解】积分区域 $D=D_{1}\bigcup D_{2}$, 其中"
    r"$D_{1}=\left\{(x,y)\middle|0\leqslant y\leqslant1,\sqrt{2}y\leqslant x\leqslant\sqrt{1+y^{2}}\right\}$,",
    r"$D_{2}=\left\{(x,y)\middle|-1\leqslant y\leqslant0,-\sqrt{2}y\leqslant x\leqslant\sqrt{1+y^{2}}\right\}$.",
    r"$\iint\limits_{D}(x+y)^{3}dxdy=\iint\limits_{D}\left(x^{3}+3x^{2}y+3xy^{2}+y^{3}\right)dxdy$,",
    r"因为区域 $D$ 关于 $x$ 轴对称，被积函数 $3x^{2}y+y^{3}$ 是 $y$ 的奇函数，所以",
    r"$\iint\limits_{D}\left(3x^{2}y+y^{3}\right)dxdy=0$.",
    r"$\iint\limits_{D}(x+y)^{3}dxdy=\iint\limits_{D}\left(x^{3}+3xy^{2}\right)dxdy"
    r"=2\iint\limits_{D_{1}}\left(x^{3}+3xy^{2}\right)dxdy"
    r"=2\left[\int_{0}^{1}dy\int_{\sqrt{2}y}^{\sqrt{1+y^{2}}}\left(x^{3}+3xy^{2}\right)dx\right]$",
    r"$=2\int_{0}^{1}\left(\dfrac{1}{4}x^{4}+\dfrac{3}{2}x^{2}y^{2}\right)\Big|_{\sqrt{2}y}^{\sqrt{1+y^{2}}}dy"
    r"=2\int_{0}^{1}\left(-\dfrac{9}{4}y^{4}+2y^{2}+\dfrac{1}{4}\right)dy=\dfrac{14}{15}$.",
])

A[17] = (r"M_{\max}=5\sqrt{5},\ M_{\min}=-5\sqrt{5}", [
    r"【详解】条件极值，构造拉格朗日函数.",
    r"$L(x,y,z,\lambda)=xy+2yz+\lambda(x^{2}+y^{2}+z^{2}-10)$.",
    r"$\begin{cases}L_{x}=y+2\lambda x=0\\ L_{y}=x+2z+2\lambda y=0\\ L_{z}=2y+2\lambda z=0\\ "
    r"L_{\lambda}=x^{2}+y^{2}+z^{2}-10=0\end{cases}$",
    r"求解方程组得 $\begin{cases}x_{1}=-1\\ y_{1}=\sqrt{5}\\ z_{1}=-2\end{cases}$，$\begin{cases}x_{2}=-1\\ y_{2}=-\sqrt{5}\\ z_{2}=-2\end{cases}$，"
    r"$\begin{cases}x_{3}=1\\ y_{3}=\sqrt{5}\\ z_{3}=2\end{cases}$，$\begin{cases}x_{4}=1\\ y_{4}=-\sqrt{5}\\ z_{4}=2\end{cases}$，"
    r"$\begin{cases}x_{5}=2\sqrt{2}\\ y_{5}=0\\ z_{5}=-\sqrt{2}\end{cases}$，$\begin{cases}x_{6}=-2\sqrt{2}\\ y_{6}=0\\ z_{6}=\sqrt{2}\end{cases}$，",
    r"代入得，$M_{\max}=1\cdot\sqrt{5}+2\cdot\sqrt{5}\cdot2=5\sqrt{5}$，"
    r"$M_{\min}=-1\cdot\sqrt{5}-2\cdot\sqrt{5}\cdot2=-5\sqrt{5}$",
])

A[18] = (r"(I)\ \int_{0}^{1}|\ln t|[\ln(1+t)]^{n}dt<\int_{0}^{1}t^{n}|\ln t|dt;\ (II)\ \lim\limits_{n\to\infty}M_{n}=0", [
    r"【详解】",
    r"（I）令 $f(t)=\ln(1+t)-t$,",
    r"当 $0\leqslant t\leqslant1$ 时，$f'(t)=\dfrac{1}{1+t}-1\leqslant0$;",
    r"故当 $0\leqslant t\leqslant1$ 时 $f(t)\leqslant f(0)=0$;",
    r"当 $0\leqslant t\leqslant1$ 时 $0\leqslant\ln(1+t)\leqslant t$,",
    r"从而 $\left(\ln(1+t)\right)^{n}\leqslant t^{n}(n=1,2,\cdots)$ 又由 $|\ln t|\geqslant0$.",
    r"得 $\int_{0}^{1}|\ln t|\left[\ln(1+t)\right]^{n}dt<\int_{0}^{1}t^{n}|\ln t|dt(n=1,2,\cdots)$.",
    r"（II）$\int_{0}^{1}|\ln t|t^{n}dt=-\int_{0}^{1}(\ln t)t^{n}dt"
    r"=-(\ln t)\dfrac{1}{n+1}t^{n+1}\Big|_{0}^{1}+\int_{0}^{1}\dfrac{1}{n+1}t^{n}dt=\dfrac{1}{(n+1)^{2}}$",
    r"$\lim\limits_{n\to\infty}\int_{0}^{1}|\ln t|t^{n}dt=0$，又 $M_{n}>0$.",
    r"由夹逼定理得 $\lim\limits_{n\to\infty}\int_{0}^{1}|\ln t|\left[\ln(1+t)\right]^{n}dt=0$.",
])

A[19] = ("证明见解析", [
    r"【详解】（I）设 $F(x)=\int_{0}^{x}f(t)dt(0\leqslant x\leqslant2)$，则 $\int_{0}^{2}f(x)dx=F(2)-F(0)$.",
    r"根据拉格朗日中值定理，存在 $\eta\in(0,2)$，使 $F(2)-F(0)=2F'(\eta)=2f(\eta)$.",
    r"由题设 $\int_{0}^{2}f(x)dx=2f(0)$，从而 $f(\eta)=f(0)$;",
    r"（II）由题可知 $\dfrac{f(2)+f(3)}{2}$ 在 $f(2)$ 到 $f(3)$ 之间，所以由连续函数的介值定理有，存在",
    r"$\xi_{0}\in[2,3]$，使得 $f(\xi_{0})=\dfrac{f(2)+f(3)}{2}$，而 $\dfrac{f(2)+f(3)}{2}=f(0)$,",
    r"又由（1）的结论有 $f(\eta)=f(0), \eta\in(0,2)$，所以 $f(0)=f(\eta)=f(\xi_{0}), 0<\eta<2\leqslant\xi_{0}\leqslant3$",
    r"在区间 $(0,\eta)$ 上，由罗尔定理有，存在 $\xi_{1}\in(0,\eta)$, 使得 $f'(\xi_{1})=0$，",
    r"在区间 $(\eta,\xi_{0})$ 上，由罗尔定理有，存在 $\xi_{2}\in(\eta,\xi_{0})$, 使得 $f'(\xi_{2})=0$.",
    r"由于 $f'(\xi_{1})=f'(\xi_{2})=0$，所以在区间 $(\xi_{1},\xi_{2})$ 上，由罗尔定理有，存在 $\xi\in(\xi_{1},\xi_{2})$, 使得",
    r"$f''(\xi)=0$.",
])

A[20] = (r"(I)\ \lambda=-1,\ a=-2;\ (II)\ \boldsymbol{x}=k\begin{pmatrix}1\\0\\1\end{pmatrix}"
         r"+\begin{pmatrix}\frac{3}{2}\\-\frac{1}{2}\\0\end{pmatrix}", [
    r"【详解】（I）由 $A\boldsymbol{x}=\boldsymbol{b}$ 存在 2 个不同的解，可知 $R(A)=R(A\!:\!\boldsymbol{b})<3$.",
    r"对 $A\boldsymbol{x}=\boldsymbol{b}$ 的增广矩阵做初等行变换，",
    r"$\overline{A}=(A\!:\!\boldsymbol{b})="
    r"\left(\begin{array}{cccc}\lambda&1&1\!:&a\\ 0&\lambda-1&0\!:&1\\ 1&1&\lambda\!:&1\end{array}\right)"
    r"\xrightarrow{r_{1}\leftrightarrow r_{3}}"
    r"\left(\begin{array}{cccc}1&1&\lambda\!:&1\\ 0&\lambda-1&0\!:&1\\ \lambda&1&1\!:&a\end{array}\right)$",
    r"$\xrightarrow{r_{3}-\lambda r_{1}}"
    r"\left(\begin{array}{ccccc}1&1&\lambda&:&1\\ 0&\lambda-1&0&:&1\\ 0&1-\lambda&1-\lambda^{2}&:&a-\lambda\end{array}\right)"
    r"\xrightarrow{r_{3}+r_{2}}"
    r"\left(\begin{array}{ccccc}1&1&\lambda&:&1\\ 0&\lambda-1&0&:&1\\ 0&0&1-\lambda^{2}&:&a+1-\lambda\end{array}\right)$",
    r"所以 $\begin{cases}1-\lambda^{2}=0\\ a+1-\lambda=0\end{cases}$，解得 $\lambda=1, a=0$ （舍去）；$\lambda=-1, a=-2$.",
    r"（II）由（I）知，$\overline{A}="
    r"\left(\begin{array}{cccc}1&1&-1\!:&1\\ 0&-2&0\!:&1\\ 0&0&0\!:&0\end{array}\right)"
    r"\to\left(\begin{array}{cccc}1&0&-1\!:&1.5\\ 0&1&0\!:&-0.5\\ 0&0&0\!:&0\end{array}\right)$.",
    r"$R(A)=R(\overline{A})=2$, 对应齐次线性方程组 $A\boldsymbol{x}=\boldsymbol{0}$ 的基础解系含 1 个解向量, "
    r"即 $\boldsymbol{\alpha}=\begin{pmatrix}1\\ 0\\ 1\end{pmatrix}$,",
    r"$A\boldsymbol{x}=\boldsymbol{b}$ 的一个特解为 $\boldsymbol{\beta}=\begin{pmatrix}\dfrac{3}{2}\\ -\dfrac{1}{2}\\ 0\end{pmatrix}$, "
    r"$A\boldsymbol{x}=\boldsymbol{b}$ 的通解为 $k\begin{pmatrix}1\\ 0\\ 1\end{pmatrix}+\begin{pmatrix}\dfrac{3}{2}\\ -\dfrac{1}{2}\\ 0\end{pmatrix}$"
    r"（其中 $k$ 为任意常数）.",
])

A[21] = (r"(I)\ \lambda_{1}=2,\ a=-1;\ (II)\ Q=\begin{pmatrix}\frac{1}{\sqrt{6}}&-\frac{1}{\sqrt{2}}&-\frac{1}{\sqrt{3}}\\"
         r"\frac{2}{\sqrt{6}}&0&\frac{1}{\sqrt{3}}\\\frac{1}{\sqrt{6}}&\frac{1}{\sqrt{2}}&-\frac{1}{\sqrt{3}}\end{pmatrix}", [
    r"【详解】由于 $\dfrac{1}{\sqrt{6}}\begin{pmatrix}1\\ 2\\ 1\end{pmatrix}$ 是 $Q$ 的第一列，所以 $\begin{pmatrix}1\\ 2\\ 1\end{pmatrix}$ "
    r"是 $A$ 的一个特征向量，设其所属特征值为",
    r"$\lambda_{1}$，则 $A\cdot\begin{pmatrix}1\\ 2\\ 1\end{pmatrix}=\lambda_{1}\cdot\begin{pmatrix}1\\ 2\\ 1\end{pmatrix}$，"
    r"即 $\begin{pmatrix}0&-1&4\\ -1&3&a\\ 4&a&0\end{pmatrix}\begin{pmatrix}1\\ 2\\ 1\end{pmatrix}"
    r"=\begin{pmatrix}2\\ 5+a\\ 4+2a\end{pmatrix}=\begin{pmatrix}\lambda_{1}\\ 2\lambda_{1}\\ \lambda_{1}\end{pmatrix}$.",
    r"所以 $\begin{cases}\lambda_{1}=2\\ 2\lambda_{1}=5+a\\ \lambda_{1}=4+2a\end{cases}\Rightarrow\begin{cases}\lambda_{1}=2\\ a=-1\end{cases}$.",
    r"则 $|\lambda E-A|=\begin{vmatrix}\lambda&1&-4\\ 1&\lambda-3&1\\ -4&1&\lambda\end{vmatrix}"
    r"\xrightarrow{r_{3}-r_{1}}\begin{vmatrix}\lambda&1&-4\\ 1&\lambda-3&1\\ -4-\lambda&0&\lambda+4\end{vmatrix}$",
    r"$\xrightarrow{c_{1}+c_{3}}\begin{vmatrix}\lambda-4&1&-4\\ 2&\lambda-3&1\\ 0&0&\lambda+4\end{vmatrix}"
    r"=(\lambda+4)\begin{vmatrix}\lambda-4&1\\ 2&\lambda-3\end{vmatrix}$",
    r"$=(\lambda+4)((\lambda-2)((\lambda-5)=0$",
    r"$\Rightarrow\lambda_{1}=2, \lambda_{2}=-4, \lambda_{3}=5$",
    r"当 $\lambda_{2}=-4$ 时，$-4E-A=\begin{pmatrix}-4&1&-4\\ 1&-7&1\\ -4&1&-4\end{pmatrix}"
    r"\xrightarrow{r_{1}\leftrightarrow r_{2}}\begin{pmatrix}1&-7&1\\ -4&1&-4\\ -4&1&-4\end{pmatrix}"
    r"\xrightarrow[r_{2}+4r_{1}]{r_{3}-r_{2}}\begin{pmatrix}1&-7&1\\ 0&-27&0\\ 0&0&0\end{pmatrix}$,",
    r"其等价方程组为 $\begin{cases}x_{1}-7x_{2}+x_{3}=0\\ -27x_{2}=0\end{cases}$，"
    r"由此得其基础解系含有 1 个解向量，即 $\boldsymbol{a}_{2}=\begin{pmatrix}-1\\ 0\\ 1\end{pmatrix}$.",
    r"当 $\lambda_{3}=5$ 时，$5E-A=\begin{pmatrix}5&1&-4\\ 1&2&1\\ -4&1&5\end{pmatrix}"
    r"\xrightarrow{r_{1}\leftrightarrow r_{2}}\begin{pmatrix}1&2&1\\ 5&1&-4\\ -4&1&5\end{pmatrix}"
    r"\xrightarrow[r_{3}+4r_{1}]{r_{2}-5r_{1}}\begin{pmatrix}1&2&1\\ 0&-9&-9\\ 0&9&9\end{pmatrix}$",
    r"$\xrightarrow{r_{3}-r_{2}}\begin{pmatrix}1&2&1\\ 0&-9&-9\\ 0&0&0\end{pmatrix}"
    r"\xrightarrow{-\frac{1}{9}r_{2}}\begin{pmatrix}1&2&1\\ 0&1&1\\ 0&0&0\end{pmatrix}$",
    r"其等价方程组为 $\begin{cases}x_{1}+2x_{2}+x_{3}=0\\ x_{2}+x_{3}=0\end{cases}$.",
    r"由此得其基础解系含有一个解向量，即 $\boldsymbol{a}_{3}=\begin{pmatrix}-1\\ 1\\ -1\end{pmatrix}$ "
    r"把 $\boldsymbol{a}_{2},\boldsymbol{a}_{3}$ 单位化得:",
    r"$\boldsymbol{\beta}_{2}=\dfrac{1}{\sqrt{2}}\begin{pmatrix}-1\\ 0\\ 1\end{pmatrix}$, "
    r"$\boldsymbol{\beta}_{3}=\dfrac{1}{\sqrt{3}}\begin{pmatrix}-1\\ 1\\ -1\end{pmatrix}$, "
    r"所以 $Q=\begin{pmatrix}\dfrac{1}{\sqrt{6}}&-\dfrac{1}{\sqrt{2}}&-\dfrac{1}{\sqrt{3}}\\ "
    r"\dfrac{2}{\sqrt{6}}&0&\dfrac{1}{\sqrt{3}}\\ "
    r"\dfrac{1}{\sqrt{6}}&\dfrac{1}{\sqrt{2}}&-\dfrac{1}{\sqrt{3}}\end{pmatrix}$.",
])

A[22] = (r"A=\dfrac{1}{\pi};\ f_{Y|X}(y|x)=\dfrac{1}{\sqrt{\pi}}e^{-(x-y)^{2}}", [
    r"【详解】由概率密度的性质 $\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}f(x,y)dxdy=1$，可知",
    r"$\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}Ae^{-2x^{2}+2xy-y^{2}}dxdy"
    r"=A\int_{-\infty}^{+\infty}e^{-x^{2}}dx\int_{-\infty}^{+\infty}e^{-(x-y)^{2}}dy=1$,",
    r"又知 $\int_{-\infty}^{+\infty}e^{-x^{2}}dx=\sqrt{\pi}$，有 "
    r"$\int_{-\infty}^{+\infty}e^{-x^{2}}dx\int_{-\infty}^{+\infty}e^{-(x-y)^{2}}dy=\pi$,",
    r"所以 $A=\dfrac{1}{\pi}$，即 $f(x,y)=\dfrac{1}{\pi}e^{-2x^{2}+2xy-y^{2}}$.",
    r"$X$ 的边缘概率密度为",
    r"$f_{X}(x)=\dfrac{1}{\pi}e^{-x^{2}}\int_{-\infty}^{+\infty}e^{-(x-y)^{2}}dy"
    r"=\dfrac{1}{\pi}e^{-x^{2}}\cdot\sqrt{\pi}=\dfrac{1}{\sqrt{\pi}}e^{-x^{2}}$, $-\infty<x<+\infty$,",
    r"$f_{Y|X}(y|x)=\dfrac{f(x,y)}{f_{X}(x)}"
    r"=\dfrac{\dfrac{1}{\pi}e^{-2x^{2}+2xy-y^{2}}}{\dfrac{1}{\sqrt{\pi}}e^{-x^{2}}}"
    r"=\dfrac{1}{\sqrt{\pi}}e^{-(x-y)^{2}}$, $-\infty<x<+\infty$, $-\infty<y<+\infty$.",
])

A[23] = (r"(I)\ P\{X=0,Y=0\}=\dfrac{1}{5},\ P\{X=0,Y=1\}=\dfrac{2}{5},\ P\{X=0,Y=2\}=\dfrac{1}{15},\ "
         r"P\{X=1,Y=0\}=\dfrac{1}{5},\ P\{X=1,Y=1\}=\dfrac{2}{15},\ P\{X=1,Y=2\}=0;\ (II)\ Cov(X,Y)=-\dfrac{4}{45}", [
    r"【详解】（I）由题知 $X$ 的可能取值为 $0,1$；$Y$ 的可能取值为 $0,1,2$，则有",
    r"$P\{X=0,Y=0\}=\dfrac{C_{3}^{2}}{C_{6}^{2}}=\dfrac{1}{5}$，"
    r"$P\{X=0,Y=1\}=\dfrac{C_{2}^{1}C_{3}^{1}}{C_{6}^{2}}=\dfrac{2}{5}$",
    r"$P\{X=0,Y=2\}=\dfrac{C_{2}^{2}}{C_{6}^{2}}=\dfrac{1}{15}$，"
    r"$P\{X=1,Y=0\}=\dfrac{C_{1}^{1}C_{3}^{1}}{C_{6}^{2}}=\dfrac{1}{5}$",
    r"$P\{X=1,Y=1\}=\dfrac{C_{1}^{1}C_{2}^{1}}{C_{6}^{2}}=\dfrac{2}{15}$，"
    r"$P\{X=1,Y=2\}=0$",
    r"随机变量 $(X,Y)$ 的概率分布为",
    r"$\begin{array}{c|ccc} X\backslash Y & 0 & 1 & 2\\ \hline "
    r"0 & \dfrac{1}{5} & \dfrac{2}{5} & \dfrac{1}{15}\\ "
    r"1 & \dfrac{1}{5} & \dfrac{2}{15} & 0 \end{array}$",
    r"（II）随机变量 $X,Y$ 的分布律分别为",
    r"$\begin{array}{c|cc} X & 0 & 1\\ \hline P & \dfrac{2}{3} & \dfrac{1}{3} \end{array}$",
    r"$\begin{array}{c|ccc} Y & 0 & 1 & 2\\ \hline P & \dfrac{2}{5} & \dfrac{8}{15} & \dfrac{1}{15} \end{array}$",
    r"所以有",
    r"$EX=\dfrac{1}{3}$, $EY=1\times\dfrac{8}{15}+2\times\dfrac{1}{15}=\dfrac{2}{3}$,",
    r"$EXY=1\times1\times\dfrac{2}{15}=\dfrac{2}{15}$",
    r"$\Rightarrow Cov(X,Y)=EXY-EXEY=-\dfrac{4}{45}$",
])
