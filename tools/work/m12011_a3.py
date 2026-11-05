# -*- coding: utf-8 -*-
"""2011 数学一 解析 解答题 15-23（原卷 p8-p13，逐字照录【解析】/【证明】；本段原卷无单独【答案】行）"""

A = {}

A[15] = (r"e^{-\frac{1}{2}}", [
    r"【解析】这是个 $1^{\infty}$ 型极限",
    r"$I=\lim\limits_{x\to0}\left[\dfrac{\ln(1+x)}{x}\right]^{\frac{1}{e^{x}-1}}=\lim\limits_{x\to0}e^{\frac{1}{e^{x}-1}\ln\left[\frac{\ln(1+x)}{x}\right]}$",
    r"$=e^{\lim\limits_{x\to0}\frac{1}{e^{x}-1}\left(\frac{\ln(1+x)}{x}-1\right)}=e^{\lim\limits_{x\to0}\frac{\ln(1+x)-x}{x^{2}}}$",
    r"$=e^{\lim\limits_{x\to0}\frac{\frac{1}{1+x}-1}{2x}}=e^{\lim\limits_{x\to0}\frac{-x}{2x(1+x)}}$",
    r"$=e^{-\frac{1}{2}}$",
])

A[16] = (r"f''_{11}(1,1)+f''_{12}(1,1)+f'_{1}(1,1)", [
    r"【解析】由于 $g(x)$ 可导且在 $x=1$ 处取得极值，故必有 $g'(1)=0$.",
    r"由题又知 $\dfrac{\partial z}{\partial x}=f'_{1}\cdot y+f'_{2}\cdot yg'(x)$，所以 $\dfrac{\partial z}{\partial x}\Big|_{x=1}=f'_{1}(y,y)\cdot y$. 所以",
    r"$\dfrac{\partial^{2}z}{\partial x\partial y}\Big|_{\substack{x=1\\ y=1}}=\dfrac{d}{dy}\left(\dfrac{\partial z}{\partial x}\Big|_{x=1}\right)\Bigg|_{y=1}=\dfrac{d}{dy}\left(f'_{1}(y,y)\cdot y\right)\Bigg|_{y=1}$",
    r"$=\left[f''_{11}(y,y)+f''_{12}(y,y)\right]y+f'_{1}(y,y)\Big|_{y=1}.$",
    r"$=f''_{11}(1,1)+f''_{12}(1,1)+f'_{1}(1,1)$",
])

A[17] = (r"k\leqslant1 时原方程有一个实根; k>1 时原方程有三个实根", [
    r"【解析】令 $F(x)=k\arctan x-x$，则 $F(x)$ 为奇函数，故只需考虑 $x\in[0,+\infty)$ 部分.",
    r"又 $F(0)=0$，求得 $F'(x)=\dfrac{k}{1+x^{2}}-1=\dfrac{k-1-x^{2}}{1+x^{2}}$",
    r"（1）当 $k-1\leqslant0$，即 $k\leqslant1$，$F'(x)<0(x>0)$，$F(x)$ 在 $(0,+\infty)$ 上无零点；",
    r"（2）当 $k-1>0$，即 $k>1$ 时，$F(x)$ 在 $\left(0,\sqrt{k-1}\right)$ 单调增加，在 $\left(\sqrt{k-1},+\infty\right)$ 单调减少.",
    r"在 $x=\sqrt{k-1}$ 时，函数 $F(x)$ 取得最大值，且",
    r"$F\left(\sqrt{k-1}\right)>F(0)=0$，$\lim\limits_{x\to+\infty}F(x)=\lim\limits_{x\to+\infty}x\left(\dfrac{k\arctan x}{x}-1\right)=-\infty$",
    r"则 $F(x)$ 在 $\left(\sqrt{k-1},+\infty\right)$ 内有一个零点",
    r"综上所述：当 $k\leqslant1$ 时，原方程有一个实根；当 $k>1$ 时，原方程有三个实根.",
])

A[18] = ("证明见解析", [
    r"【证明】①令 $f(x)=\ln x(x>0)$，对任意正整数 $n$，由拉格朗日中值定理得",
    r"$\ln(1+\dfrac{1}{n})=\ln(1+n)-\ln n=\dfrac{1}{\xi}$，其中 $n<\xi<n+1$",
    r"即 $\dfrac{1}{n+1}<\ln(1+\dfrac{1}{n})<\dfrac{1}{n}$.",
    r"②先证数列 $\{a_{n}\}$ 单调递减",
    r"$a_{n+1}-a_{n}=\dfrac{1}{n+1}-\ln(n+1)+\ln n=\dfrac{1}{n+1}-\ln(1+\dfrac{1}{n})<0$",
    r"再证数列 $\{a_{n}\}$ 有下界，",
    r"$a_{n}=1+\dfrac{1}{2}+...+\dfrac{1}{n}-\ln n$",
    r"$>\ln(1+\dfrac{1}{1})+\ln(1+\dfrac{1}{2})+...+\ln(1+\dfrac{1}{n})-\ln n$",
    r"$=\ln(\dfrac{2}{1}\times\dfrac{3}{2}...\times\dfrac{n+1}{n}\times\dfrac{1}{n})$",
    r"$=\ln\dfrac{n+1}{n}>0$",
    r"故数列 $\{a_{n}\}$ 单调减少且有下界，所以数列 $\{a_{n}\}$ 收敛.",
])

A[19] = ("a", [
    r"【解析】根据二重积分的计算 $\iint\limits_{D}xyf''_{xy}(x,y)dxdy=\int_{0}^{1}x\left(\int_{0}^{1}yf''_{xy}(x,y)dy\right)dx$，其中",
    r"$\int_{0}^{1}yf''_{xy}(x,y)dy=\int_{0}^{1}ydf'_{x}(x,y)$",
    r"$=\left(yf'_{x}(x,y)\right)\Big|_{y=0}^{y=1}-\int_{0}^{1}f'_{x}(x,y)dy$",
    r"$=f'_{x}(x,1)-\int_{0}^{1}f'_{x}(x,y)dy$",
    r"$=-\int_{0}^{1}f'_{x}(x,y)dy$",
    r"则原式 $=\int_{0}^{1}x\left(-\int_{0}^{1}f'_{x}(x,y)dy\right)dx=-\int_{0}^{1}\left(\int_{0}^{1}xf'_{x}(x,y)dx\right)dy$",
    r"$=-\int_{0}^{1}\left(\int_{0}^{1}xdf(x,y)\right)dy=-\int_{0}^{1}\left(\left(xf(x,y)\right)\Big|_{x=0}^{x=1}-\int_{0}^{1}f(x,y)dx\right)dy$",
    r"$=-\int_{0}^{1}\left(f(1,y)-\int_{0}^{1}f(x,y)dx\right)dy=\iint\limits_{D}f(x,y)dxdy=a$",
])

A[20] = (r"(I)\ a=5; (II)\ \beta_{1}=2\alpha_{1}+4\alpha_{2}-\alpha_{3}, \beta_{2}=\alpha_{1}+2\alpha_{2}, \beta_{3}=5\alpha_{1}+10\alpha_{2}-2\alpha_{3}", [
    r"【解析】（1）易知 $\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}$ 线性无关，由其不能被 $\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3}$ 线性表出，得到 $\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3}$",
    r"线性相关，从而 $r(\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3})<3$. 由",
    r"$\begin{pmatrix}1&1&3\\1&2&4\\1&3&a\end{pmatrix}\to\begin{pmatrix}1&1&3\\0&1&1\\0&2&a-3\end{pmatrix}\to\begin{pmatrix}1&1&1\\0&1&1\\0&0&a-5\end{pmatrix}$",
    r"得 $a=5$.",
    r"（2）由矩阵的初等变换",
    r"$(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}\vdots\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3})=\begin{pmatrix}1&0&1&1&1&3\\0&1&3&1&2&4\\1&1&5&1&3&5\end{pmatrix}\to\begin{pmatrix}1&0&1&1&1&3\\0&1&3&1&2&4\\0&1&4&0&2&2\end{pmatrix}$",
    r"$\to\begin{pmatrix}1&0&1&1&1&3\\0&1&3&1&2&4\\0&0&1&-1&0&-2\end{pmatrix}\begin{pmatrix}1&0&0&2&1&5\\0&1&0&4&2&10\\0&0&1&-1&0&-2\end{pmatrix}$",
    r"故 $\boldsymbol{\beta}_{1}=2\boldsymbol{\alpha}_{1}+4\boldsymbol{\alpha}_{2}-\boldsymbol{\alpha}_{3}$，$\boldsymbol{\beta}_{2}=\boldsymbol{\alpha}_{1}+2\boldsymbol{\alpha}_{2}$，$\boldsymbol{\beta}_{3}=5\boldsymbol{\alpha}_{1}+10\boldsymbol{\alpha}_{2}-2\boldsymbol{\alpha}_{3}$",
])

A[21] = (r"(I)\ 特征值 -1,1,0, 特征向量 k_{1}(1,0,-1)^{T}, k_{2}(1,0,1)^{T}, k_{3}(0,1,0)^{T}; (II)\ A=\begin{pmatrix}0&0&1\\0&0&0\\1&0&0\end{pmatrix}", [
    r"【解析】（1）根据题意，$\boldsymbol{A}\begin{pmatrix}1\\0\\-1\end{pmatrix}=-1\times\begin{pmatrix}1\\0\\-1\end{pmatrix}$，$\boldsymbol{A}\begin{pmatrix}1\\0\\1\end{pmatrix}=1\times\begin{pmatrix}1\\0\\1\end{pmatrix}$",
    r"所以特征值 $-1$ 对应的特征向量为 $k_{1}\begin{pmatrix}1\\0\\-1\end{pmatrix}$，特征值 1 对应的特征向量为 $k_{2}\begin{pmatrix}1\\0\\1\end{pmatrix}$.",
    r"由 $r(\boldsymbol{A})=2$ 知 $\boldsymbol{A}$ 的另一个特征值为 0，设特征值为 0 对应的特征向量为 $k_{3}\begin{pmatrix}x_{1}\\x_{2}\\x_{3}\end{pmatrix}$.",
    r"因为实对称矩阵不同特征值得特征向量正交，得到 $\begin{cases}x_{1}-x_{3}=0\\ x_{1}+x_{3}=0\end{cases}$",
    r"从而特征值 0 对应的特征向量为 $k_{3}\begin{pmatrix}0\\1\\0\end{pmatrix}$，其中 $k_{1},k_{2},k_{3}$ 为不为零的任意常数.",
    r"（2）令 $\boldsymbol{P}=\begin{pmatrix}1&1&0\\0&0&1\\-1&1&0\end{pmatrix}$，则 $\boldsymbol{P}^{-1}=\begin{pmatrix}1&1&0\\0&0&1\\-1&1&0\end{pmatrix}^{-1}=\begin{pmatrix}\dfrac{1}{2}&0&-\dfrac{1}{2}\\\dfrac{1}{2}&0&\dfrac{1}{2}\\0&1&0\end{pmatrix}$",
    r"由 $\boldsymbol{P}^{-1}\boldsymbol{A}\boldsymbol{P}=\boldsymbol{\Lambda}$，知",
    r"$\boldsymbol{A}=\boldsymbol{P}\boldsymbol{\Lambda}\boldsymbol{P}^{-1}=\begin{pmatrix}1&1&0\\0&0&1\\-1&1&0\end{pmatrix}\begin{pmatrix}-1&0&0\\0&1&0\\0&0&0\end{pmatrix}\begin{pmatrix}1&1&0\\0&0&1\\-1&1&0\end{pmatrix}^{-1}=\begin{pmatrix}0&0&1\\0&0&0\\1&0&0\end{pmatrix}$",
])

A[22] = (r"(I)\ P\{X=0,Y=0\}=P\{X=1,Y=-1\}=P\{X=1,Y=1\}=1/3, 其余为 0; (II)\ P\{Z=-1\}=P\{Z=0\}=P\{Z=1\}=1/3; (III)\ \rho_{XY}=0", [
    r"【解析】（I）由于 $P\left\{X^{2}=Y^{2}\right\}=1$，即",
    r"$P\left\{X=0,Y=0\right\}+P\left\{X=1,Y=-1\right\}+P\left\{X=1,Y=1\right\}=1$",
    r"则有",
    r"$P\left\{X=1,Y=0\right\}=P\left\{X=0,Y=-\right\}1=P\left\{X=0,Y=1\right\}=0$",
    r"$P\left\{X=0,Y=0\right\}=P\left\{Y=0\right\}-P\left\{X=1,Y=0\right\}=\dfrac{1}{3}$",
    r"$P\left\{X=1,Y=-1\right\}=P\left\{Y=-1\right\}-P\left\{X=0,Y=-1\right\}=\dfrac{1}{3}$",
    r"$P\left\{X=1,Y=1\right\}=P\left\{Y=1\right\}-P\left\{X=0,Y=1\right\}=\dfrac{1}{3}$",
    r"所以 $(X,Y)$ 的概率分布为",
    r"$\begin{array}{c|ccc} X\backslash Y & -1 & 0 & 1\\ \hline 0 & 0 & 1/3 & 0\\ 1 & 1/3 & 0 & 1/3 \end{array}$",
    r"（II）易知随机变量 $Z$ 的可能取值为 $-1,0,1$，则有",
    r"$P\left\{Z=1\right\}=P\left\{X=1,Y=1\right\}=\dfrac{1}{3}$",
    r"$P\left\{Z=-1\right\}=P\left\{X=1,Y=-1\right\}=\dfrac{1}{3}$",
    r"$P\left\{Z=0\right\}=1-P\left\{Z=1\right\}-P\left\{Z=-1\right\}=\dfrac{1}{3}$",
    r"故 $Z=XY$ 的概率分布为",
    r"$\begin{array}{c|ccc} Z & -1 & 0 & 1\\ \hline P & 1/3 & 1/3 & 1/3 \end{array}$",
    r"（III）由（I）和（II）知",
    r"$E(XY)=EZ=(-1)\times\dfrac{1}{3}+1\times\dfrac{1}{3}=0$",
    r"$EX=\dfrac{2}{3}$，$EY=(-1)\times\dfrac{1}{3}+1\times\dfrac{1}{3}=0$",
    r"故有 $Cov(X,Y)=E(XY)-EXEY=0$，所以 $\rho_{XY}=0$.",
])

A[23] = (r"(I)\ \hat{\sigma}^{2}=\dfrac{1}{n}\sum\limits_{i=1}^{n}(X_{i}-\mu_{0})^{2}; (II)\ E\hat{\sigma}^{2}=\sigma^{2}, D\hat{\sigma}^{2}=\dfrac{2\sigma^{4}}{n}", [
    r"【解析】（I）设 $x_{1},x_{2},...,x_{n}$ 为对应样本观测值，故最大似然函数为",
    r"$L(\sigma^{2})=\prod\limits_{i=1}^{n}\dfrac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x_{i}-\mu_{0})^{2}}{2\sigma^{2}}}=(2\pi)^{-\frac{n}{2}}\cdot(\sigma^{2})^{-\frac{n}{2}}\cdot e^{-\frac{1}{2\sigma^{2}}\sum\limits_{i=1}^{n}(x_{i}-\mu_{0})^{2}}$",
    r"两边同时取对数，有",
    r"$\ln L(\sigma^{2})=-\dfrac{n}{2}\ln(2\pi)-\dfrac{n}{2}\ln(\sigma^{2})-\dfrac{1}{2\sigma^{2}}\sum\limits_{i=1}^{n}(x_{i}-\mu_{0})^{2}$",
    r"令 $\dfrac{d\ln L(\sigma^{2})}{d(\sigma^{2})}=-\dfrac{n}{2}\cdot\dfrac{1}{\sigma^{2}}+\dfrac{1}{2(\sigma^{2})^{2}}\sum\limits_{i=1}^{n}(x_{i}-\mu_{0})^{2}=0$，可得 $\sigma^{2}=\dfrac{1}{n}\sum\limits_{i=1}^{n}(x_{i}-\mu_{0})^{2}$.",
    r"所以 $Y$ 的最大似然估计为 $\hat{\sigma}^{2}=\dfrac{1}{n}\sum\limits_{i=1}^{n}(X_{i}-\mu_{0})^{2}$.",
    r"（II）由（I）知，由于 $X_{i}\sim N(\mu_{0},\sigma^{2})(i=1,2,\cdots,n)$，则有 $\dfrac{X_{i}-\mu_{0}}{\sigma}\sim N(0,1)(i=1,2,\cdots,n)$，",
    r"所以 $\sum\limits_{i=1}^{n}\left(\dfrac{X_{i}-\mu_{0}}{\sigma}\right)^{2}\sim\chi^{2}(n)$，所以有",
    r"$E\left(\sum\limits_{i=1}^{n}\left(\dfrac{X_{i}-\mu_{0}}{\sigma}\right)^{2}\right)=n$, $D\left(\sum\limits_{i=1}^{n}\left(\dfrac{X_{i}-\mu_{0}}{\sigma}\right)^{2}\right)=2n$",
    r"故",
    r"$E\hat{\sigma}^{2}=\dfrac{1}{n}\sum\limits_{i=1}^{n}E(X_{i}-\mu_{0})^{2}=\sigma^{2}$,",
    r"$D\hat{\sigma}^{2}=D\left(\dfrac{\sigma^{2}}{n}\sum\limits_{i=1}^{n}\left(\dfrac{X_{i}-\mu_{0}}{\sigma}\right)^{2}\right)=\dfrac{\sigma^{4}}{n^{2}}D\left(\sum\limits_{i=1}^{n}\left(\dfrac{X_{i}-\mu_{0}}{\sigma}\right)^{2}\right)=\dfrac{2\sigma^{4}}{n}$.",
])
