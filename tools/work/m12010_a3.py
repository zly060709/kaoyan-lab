# -*- coding: utf-8 -*-
"""2010 数学一 解析 解答题 15-23（原卷 p8-p12，逐字照录【详解】；原卷本段无单独【答案】行）"""

A = {}

A[15] = (r"y=C_{1}e^{2x}+C_{2}e^{x}+(-x^{2}-2x)e^{x}", [
    r"【详解】齐次方程 $y''-3y'+2y=0$ 的特征方程为 $\lambda^{2}-3\lambda+2=0$ 由此得",
    r"$\lambda_{1}=2,\lambda_{2}=1$. 齐次方程的通解为 $y=C_{1}e^{2x}+C_{2}e^{x}$，设非齐次方程的特解为",
    r"$y=(Ax+B)xe^{x}$，代入原方程可得，$A=-1,B=-2$. 因此原方程的通解为",
    r"$y=C_{1}e^{2x}+C_{2}e^{x}+(-x^{2}-2x)e^{x}$ ($C_{1},C_{2}$ 为任意常数).",
])

A[16] = (r"增区间 (-1,0),(1,+\infty), 减区间 (-\infty,-1),(0,1); 极小值 f(1)=f(-1)=0; 极大值 f(0)=\dfrac{1}{2}\left(1-\dfrac{1}{e}\right)", [
    r"【详解】$f(x)=x^{2}\int_{1}^{x^{2}}e^{-t^{2}}dt-\int_{1}^{x^{2}}te^{-t^{2}}dt$, $f'(x)=2x\int_{1}^{x^{2}}e^{-t^{2}}dt$. 令 $f'(x)=2x\int_{1}^{x^{2}}e^{-t^{2}}dt=0$,",
    r"解得 $x=0$，$\pm1$. 在区间 $(-1,0)$，$(1,+\infty)$，$f'(x)\geqslant0$，函数 $f(x)$ 单调递增，在区间",
    r"$(-\infty,-1)$，$(0,1)$，$f'(x)\leqslant0$，函数 $f(x)$ 单调递减. 所以在 $x=1,x=-1$ 处取得极",
    r"小值：$f(1)=f(-1)=0$；在 $x=0$ 取得极大值：$f(0)=\dfrac{1}{2}(1-\dfrac{1}{e})$.",
])

A[17] = (r"(I)\ \int_{0}^{1}|\ln t|[\ln(1+t)]^{n}dt<\int_{0}^{1}t^{n}|\ln t|dt; (II)\ \lim\limits_{n\to\infty}M_{n}=0", [
    r"【详解】",
    r"（I）令 $f(t)=\ln(1+t)-t$，当 $0\leqslant t\leqslant1$ 时，$f'(t)=\dfrac{1}{1+t}-1\leqslant0$",
    r"故当 $0\leqslant t\leqslant1$ 时 $f(t)\leqslant f(0)=0$，即 $0\leqslant t\leqslant1$ 时，$0\leqslant\ln(1+t)\leqslant t$,",
    r"从而 $\left(\ln(1+t)\right)^{n}\leqslant t^{n}(n=1,2,\cdots)$ 又由 $|\ln t|\geqslant0$,",
    r"得 $\int_{0}^{1}|\ln t|\left[\ln(1+t)\right]^{n}dt<\int_{0}^{1}t^{n}|\ln t|dt (n=1,2,\cdots).$",
    r"（II）$\int_{0}^{1}|\ln t|t^{n}dt=-\int_{0}^{1}(\ln t)t^{n}dt=-\left.(\ln t)\dfrac{1}{n+1}t^{n+1}\right|_{0}^{1}+\int_{0}^{1}\dfrac{1}{n+1}t^{n}dt=\dfrac{1}{(n+1)^{2}}$",
    r"$\lim\limits_{n\to\infty}\int_{0}^{1}|\ln t|t^{n}dt=0$, 又 $M_{n}\geqslant0$, 所以由夹逼准则得 $\lim\limits_{n\to\infty}\int_{0}^{1}|\ln t|\left[\ln(1+t)\right]^{n}dt=0.$",
])

A[18] = (r"收敛域 [-1,1]; 和函数 s(x)=x\arctan x, x\in[-1,1]", [
    r"【详解】$\lim\limits_{n\to\infty}\left|\dfrac{u_{n+1}(x)}{u_{n}(x)}\right|=\lim\limits_{n\to\infty}\left|\dfrac{x^{2n+2}(2n-1)}{x^{2n}(2n+1)}\right|=x^{2}$，"
    r"所以当 $x^{2}<1$ 即 $-1<x<1$ 时，原幂",
    r"级数绝对收敛；当 $x=\pm1$ 时，级数为 $\sum\limits_{n=1}^{\infty}\dfrac{(-1)^{n-1}}{2n-1}$，根据莱布尼兹判别法知此级数收敛,",
    r"故原幂级数的收敛域为 $[-1,1]$.",
    r"由题意可设 $s(x)=\sum\limits_{n=1}^{\infty}\dfrac{(-1)^{n-1}}{2n-1}x^{2n}$，则 $s(x)=\sum\limits_{n=1}^{\infty}\dfrac{(-1)^{n-1}}{2n-1}x^{2n}"
    r"=x\sum\limits_{n=1}^{\infty}\dfrac{(-1)^{n-1}}{2n-1}x^{2n-1}$，令",
    r"$\sum\limits_{n=1}^{\infty}\dfrac{(-1)^{n-1}}{2n-1}x^{2n-1}=f(x), x\in[-1,1]$，则 $f'(x)=\sum\limits_{n=1}^{\infty}(-1)^{n-1}x^{2(n-1)}=\dfrac{1}{1+x^{2}}$.",
    r"因为 $f(0)=0$，所以 $f(x)=\int_{0}^{x}f'(t)dt+f(0)=\arctan x$，从而可得",
    r"$s(x)=x\arctan x, x\in[-1,1]$, 收敛域 $x\in[-1,1]$, 和函数 $s(x)=x\arctan x$.",
])

A[19] = (r"轨迹 C: 2z-y=0, x^{2}+\dfrac{3}{4}y^{2}=1; I=2\pi", [
    r"【详解】切平面法向量 $F_{x}=2x, F_{y}=2y-z, F_{z}=2z-y$，$xoy$ 面的法向量为 $(0,0,1)$,",
    r"因 $S$ 在点 $P$ 处的切平面与 $xOy$ 面垂直. 所以 $2x\times0+(2y-z)\times0+(2z-y)\times1=0\Rightarrow z=\dfrac{y}{2}.$",
    r"所以轨迹 $C$ 为 $\begin{cases}x^{2}+y^{2}+z^{2}-yz=1\\ y=2z\end{cases}$ 即 $\begin{cases}2z-y=0\\ x^{2}+\dfrac{3}{4}y^{2}=1\end{cases}$ "
    r"取 $D_{xy}=\left\{(x,y)\Big|x^{2}+\dfrac{3}{4}y^{2}\leqslant1\right\}$,",
    r"由于 $dS=\sqrt{1+z_{x}^{2}+z_{y}^{2}}dxdy=\sqrt{1+\left(\dfrac{2x}{y-2z}\right)^{2}+\left(\dfrac{2y-z}{y-2z}\right)^{2}}dxdy$",
    r"$=\dfrac{\sqrt{4x^{2}+5y^{2}+5z^{2}-8yz}}{|y-2z|}dxdy=\dfrac{\sqrt{4+y^{2}+z^{2}-4yz}}{|y-2z|}dxdy$",
    r"所以，原式 $=\iint\limits_{D_{xy}}\dfrac{(x+\sqrt{3})|y-2z|}{\sqrt{4+y^{2}+z^{2}-4yz}}\cdot\dfrac{\sqrt{4+y^{2}+z^{2}-4yz}}{|y-2z|}dxdy"
    r"=\iint\limits_{D_{xy}}\left(x+\sqrt{3}\right)dxdy$",
    r"$=\iint\limits_{D_{xy}}xdxdy+\iint\limits_{D_{xy}}\sqrt{3}dxdy=0+\sqrt{3}\cdot\pi\cdot1\cdot\dfrac{2}{\sqrt{3}}=2\pi$.",
])

A[20] = (r"(I)\ \lambda=-1, a=-2; (II)\ x=k(1,0,1)^{T}+(3/2,-1/2,0)^{T} (k 为任意常数)", [
    r"【详解】（I）由 $\boldsymbol{Ax}=\boldsymbol{b}$ 存在 2 个不同的解，可知 $R(\boldsymbol{A})=R(\boldsymbol{A}\!\vdots\,\boldsymbol{b})<3$",
    r"对 $\boldsymbol{Ax}=\boldsymbol{b}$ 的增广矩阵做初等行变换,",
    r"$\bar{\boldsymbol{A}}=(\boldsymbol{A}\!\vdots\,\boldsymbol{b})=\begin{pmatrix}\lambda&1&1&\vdots&a\\ 0&\lambda-1&0&\vdots&1\\ 1&1&\lambda&\vdots&1\end{pmatrix}"
    r"\xrightarrow{\;r_{1}\leftrightarrow r_{3}\;}"
    r"\begin{pmatrix}1&1&\lambda&\vdots&1\\ 0&\lambda-1&0&\vdots&1\\ \lambda&1&1&\vdots&a\end{pmatrix}$",
    r"$\xrightarrow{\;r_{3}-\lambda r_{1}\;}"
    r"\begin{pmatrix}1&1&\lambda&\vdots&1\\ 0&\lambda-1&0&\vdots&1\\ 0&1-\lambda&1-\lambda^{2}&\vdots&a-\lambda\end{pmatrix}"
    r"\xrightarrow{\;r_{3}+r_{2}\;}"
    r"\begin{pmatrix}1&1&\lambda&\vdots&1\\ 0&\lambda-1&0&\vdots&1\\ 0&0&1-\lambda^{2}&\vdots&a+1-\lambda\end{pmatrix}$",
    r"所以 $\begin{cases}1-\lambda^{2}=0\\ a+1-\lambda=0\end{cases}$，解得 $\lambda=1,a=0$ （舍去）；$\lambda=-1,a=-2$.",
    r"（II）由（I）知，$\bar{\boldsymbol{A}}=\begin{pmatrix}1&1&-1&\vdots&1\\ 0&-2&0&\vdots&1\\ 0&0&0&\vdots&0\end{pmatrix}"
    r"\to\begin{pmatrix}1&0&-1&\vdots&1.5\\ 0&1&0&\vdots&-0.5\\ 0&0&0&\vdots&0\end{pmatrix}$,",
    r"$R(\boldsymbol{A})=R(\bar{\boldsymbol{A}})=2$, 对应齐次线性方程组 $\boldsymbol{Ax}=\boldsymbol{0}$ 的基础解系含 1 个解向量，"
    r"即 $\boldsymbol{\alpha}=\begin{pmatrix}1\\ 0\\ 1\end{pmatrix}$,",
    r"$\boldsymbol{Ax}=\boldsymbol{b}$ 的一个特解为 $\boldsymbol{\beta}=\begin{pmatrix}\dfrac{3}{2}\\ -\dfrac{1}{2}\\ 0\end{pmatrix}$, "
    r"$\boldsymbol{Ax}=\boldsymbol{b}$ 的通解为 $k\begin{pmatrix}1\\ 0\\ 1\end{pmatrix}+\begin{pmatrix}\dfrac{3}{2}\\ -\dfrac{1}{2}\\ 0\end{pmatrix}$（其中 $k$ 为任意常数）.",
])

A[21] = (r"(I)\ A=\begin{pmatrix}1/2&0&-1/2\\ 0&1&0\\ -1/2&0&1/2\end{pmatrix}; (II)\ 证明见解析", [
    r"【详解】",
    r"（I）由题意知矩阵 $\boldsymbol{A}$ 的特征值为 1,1,0, 且特征值 0 对应的特征向量为 $\left(\dfrac{\sqrt{2}}{2},0,\dfrac{\sqrt{2}}{2}\right)^{T}$,",
    r"$\boldsymbol{Q}^{T}\boldsymbol{AQ}=\begin{pmatrix}1&&\\ &1&\\ &&0\end{pmatrix}$, 设特征值 1 对应的特征向量为 $(x_{1},x_{2},x_{3})^{T}$，则",
    r"$\dfrac{\sqrt{2}}{2}\cdot x_{1}+0\cdot x_{2}+\dfrac{\sqrt{2}}{2}\cdot x_{3}=0$，求解得特征值 1 对应的特征向量为",
    r"$(0,1,0)^{T},(1,0,-1)^{T}$，将其单位化得 $(0,1,0)^{T},\left(\dfrac{1}{\sqrt{2}},0,-\dfrac{1}{\sqrt{2}}\right)^{T}.$",
    r"$\boldsymbol{Q}=\begin{pmatrix}0&\dfrac{\sqrt{2}}{2}&\dfrac{\sqrt{2}}{2}\\ 1&0&0\\ 0&-\dfrac{\sqrt{2}}{2}&\dfrac{\sqrt{2}}{2}\end{pmatrix}$, "
    r"$\boldsymbol{Q}^{T}=\boldsymbol{Q}^{-1}=\begin{pmatrix}0&1&0\\ \dfrac{\sqrt{2}}{2}&0&-\dfrac{\sqrt{2}}{2}\\ \dfrac{\sqrt{2}}{2}&0&\dfrac{\sqrt{2}}{2}\end{pmatrix}$,",
    r"$\boldsymbol{A}=\boldsymbol{Q}\Lambda\boldsymbol{Q}^{T}=\begin{pmatrix}0&\dfrac{\sqrt{2}}{2}&\dfrac{\sqrt{2}}{2}\\ 1&0&0\\ 0&-\dfrac{\sqrt{2}}{2}&\dfrac{\sqrt{2}}{2}\end{pmatrix}"
    r"\begin{pmatrix}1&&\\ &1&\\ &&0\end{pmatrix}"
    r"\begin{pmatrix}0&1&0\\ \dfrac{\sqrt{2}}{2}&0&-\dfrac{\sqrt{2}}{2}\\ \dfrac{\sqrt{2}}{2}&0&\dfrac{\sqrt{2}}{2}\end{pmatrix}"
    r"=\begin{pmatrix}\dfrac{1}{2}&0&-\dfrac{1}{2}\\ 0&1&0\\ -\dfrac{1}{2}&0&\dfrac{1}{2}\end{pmatrix}.$",
    r"（II）证明：$\left(\boldsymbol{A}+\boldsymbol{E}\right)^{T}=\boldsymbol{A}^{T}+\boldsymbol{E}=\boldsymbol{A}+\boldsymbol{E}$, , "
    r"$\boldsymbol{A}+\boldsymbol{E}$ 为实对称矩阵. 又 $\boldsymbol{A}$ 的特征值为 1,1,0,",
    r"$\boldsymbol{A}+\boldsymbol{E}$ 的特征值为 2,2,1，都大于 0，$\boldsymbol{A}+\boldsymbol{E}$ 为正定矩阵.",
])

A[22] = (r"A=\dfrac{1}{\pi}, f_{Y|X}(y|x)=\dfrac{1}{\sqrt{\pi}}e^{-(x-y)^{2}}", [
    r"【详解】由概率密度的性质 $\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}f(x,y)dxdy=1$，可知",
    r"$\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}Ae^{-2x^{2}+2xy-y^{2}}dxdy=A\int_{-\infty}^{+\infty}e^{-x^{2}}dx\int_{-\infty}^{+\infty}e^{-(x-y)^{2}}dy=1.$",
    r"又知 $\int_{-\infty}^{+\infty}e^{-x^{2}}dx=\sqrt{\pi}$，有 $\int_{-\infty}^{+\infty}e^{-x^{2}}dx\int_{-\infty}^{+\infty}e^{-(x-y)^{2}}dy=\pi$，所以 $A=\dfrac{1}{\pi}$，即",
    r"$f(x,y)=\dfrac{1}{\pi}e^{-2x^{2}+2xy-y^{2}}$，$X$ 的边缘概率密度为",
    r"$f_{X}(x)=\dfrac{1}{\pi}e^{-x^{2}}\int_{-\infty}^{+\infty}e^{-(x-y)^{2}}dy=\dfrac{1}{\pi}e^{-x^{2}}\cdot\sqrt{\pi}=\dfrac{1}{\sqrt{\pi}}e^{-x^{2}}, -\infty<x<+\infty$,",
    r"$f_{Y|X}(y|x)=\dfrac{f(x,y)}{f_{X}(x)}=\dfrac{\dfrac{1}{\pi}e^{-2x^{2}+2xy-y^{2}}}{\dfrac{1}{\sqrt{\pi}}e^{-x^{2}}}"
    r"=\dfrac{1}{\sqrt{\pi}}e^{-(x-y)^{2}}, -\infty<x<+\infty, -\infty<y<+\infty$.",
])

A[23] = (r"a_{1}=0, a_{2}=a_{3}=\dfrac{1}{n}; DT=\dfrac{(1-\theta)\theta}{n}", [
    r"【详解】由题知 $N_{1},N_{2},N_{3}$ 分别服从二项分布 $B(n,1-\theta), B(n,\theta-\theta^{2}), B(n,\theta^{2})$，则有",
    r"$EN_{1}=n(1-\theta), EN_{2}=n(\theta-\theta^{2}), EN_{3}=n\theta^{2}$,",
    r"$ET=E(\sum\limits_{i=1}^{3}a_{i}N_{i})=\sum\limits_{i=1}^{3}a_{i}EN_{i}=a_{1}n(1-\theta)+a_{2}n(\theta-\theta^{2})+a_{3}n\theta^{2}=\theta$",
    r"$\Rightarrow\begin{cases}a_{1}n=0\\ a_{2}n-a_{1}n=1\\ a_{3}n-a_{2}n=0\end{cases}\Rightarrow\begin{cases}a_{1}=0\\ a_{2}=\dfrac{1}{n}\\ a_{3}=\dfrac{1}{n}\end{cases}$",
    r"即 $T=\sum\limits_{i=1}^{3}a_{i}N_{i}=\dfrac{N_{2}+N_{3}}{n}=\dfrac{n-N_{1}}{n}=1-\dfrac{N_{1}}{n}$,",
    r"$DT=D(1-\dfrac{N_{1}}{n})=\dfrac{1}{n^{2}}DN_{1}=\dfrac{1}{n^{2}}\times n(1-\theta)\theta=\dfrac{(1-\theta)\theta}{n}$.",
])
