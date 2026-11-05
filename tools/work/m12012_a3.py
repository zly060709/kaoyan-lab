# -*- coding: utf-8 -*-
"""2012 数学一 解析 解答题 15-23（原卷 p8-p13，逐字照录；本卷解析标签：15【证明】、16/19-23【详解】、17/18【解】）"""

A = {}

A[15] = ("证明见解析", [
    r"【证明】令 $f(x)=x\ln\dfrac{1+x}{1-x}+\cos x-1-\dfrac{x^{2}}{2}$，则 $f(0)=0$",
    r"$f(x)$ 为偶函数，我们只需证明 $0<x<1, f(x)=x\ln\dfrac{1+x}{1-x}+\cos x-1-\dfrac{x^{2}}{2}>0$.",
    r"$f'(x)=\ln\dfrac{1+x}{1-x}+x\left(\dfrac{1}{1+x}+\dfrac{1}{1-x}\right)-\sin x-x$,",
    r"$f''(x)=2\left(\dfrac{1}{1+x}+\dfrac{1}{1-x}\right)+x\left(-\dfrac{1}{(1+x)^{2}}+\dfrac{1}{(1-x)^{2}}\right)-\cos x-1$",
    r"$=\dfrac{4}{1-x^{2}}+x\left(-\dfrac{1}{(1+x)^{2}}+\dfrac{1}{(1-x)^{2}}\right)-\cos x-1$",
    r"由 $0<x<1$ 可得，$\dfrac{4}{1-x^{2}}>4$，$x\left(-\dfrac{1}{(1+x)^{2}}+\dfrac{1}{(1-x)^{2}}\right)>0$，$-2\leqslant-\cos x-1\leqslant-1$；",
    r"所以当 $0<x<1$，$f''(x)>0$.",
    r"因此，当 $0<x<1$ 时 $f'(x)$ 单调递增．而 $f'(0)=0$，所以 $f'(x)>f'(0)=0$.",
    r"得出 $f(x)$ 为增函数，又由 $f(0)=0$，得出 当 $0<x<1$，",
    r"$f(x)=x\ln\dfrac{1+x}{1-x}+\cos x-1-\dfrac{x^{2}}{2}>0$，即 $x\ln\dfrac{1+x}{1-x}+\cos x>1+\dfrac{x^{2}}{2}$.",
])

A[16] = ("极大值点(1,0); 极小值点(-1,0)", [
    r"【详解】$\begin{cases}f'_{x}=e^{-\frac{x^{2}+y^{2}}{2}}(1-x^{2})=0\\ f'_{y}=-xye^{-\frac{x^{2}+y^{2}}{2}}=0\end{cases}$，解得 $\begin{cases}x=1,\\y=0,\end{cases}$ $\begin{cases}x=-1.\\y=0.\end{cases}$",
    r"$A=f''_{xx}=-xe^{-\frac{x^{2}+y^{2}}{2}}(1-x^{2})-2xe^{-\frac{x^{2}+y^{2}}{2}}$，$B=f''_{xy}=-ye^{-\frac{x^{2}+y^{2}}{2}}(1-x^{2})$，",
    r"$C=f''_{yy}=xe^{-\frac{x^{2}+y^{2}}{2}}(-1+y^{2})$",
    r"代入 $\begin{cases}x=1,\\y=0,\end{cases}$ 可得 $AC-B^{2}=\dfrac{2}{e}>0, A=-\dfrac{2}{\sqrt{e}}<0$，则可知 $\begin{cases}x=1,\\y=0,\end{cases}$ 为函数的极大值点；",
    r"代入 $\begin{cases}x=-1.\\y=0.\end{cases}$ 可得 $AC-B^{2}=\dfrac{2}{e}>0, A=\dfrac{2}{\sqrt{e}}>0$，则可知 $\begin{cases}x=-1,\\y=0,\end{cases}$ 是函数极小值点.",
])

A[17] = ("收敛域(-1,1); S(x)=\\frac{1+x^{2}}{(1-x^{2})^{2}}+\\frac{1}{x}\\ln\\frac{1+x}{1-x}(-1<x<0 or 0<x<1), S(0)=3", [
    r"【解】利用比值法有",
    r"$\lim\limits_{n\to\infty}\left|\dfrac{a_{n+1}x^{2(n+1)}}{a_{n}x^{2n}}\right|$",
    r"$=\lim\limits_{n\to\infty}\left|\dfrac{4(n+1)^{2}+4(n+1)+3}{2(n+1)+1}\times\dfrac{2n+1}{4n^{2}+4n+3}x^{2}\right|$",
    r"$=x^{2}$",
    r"令 $x^{2}<1$ 得 $-1<x<1$，",
    r"当 $x=\pm1$ 时，原级数 $=\sum\limits_{n=0}^{\infty}\dfrac{4n^{2}+4n+3}{2n+1}$，但第 n 项的极限即 $\lim\limits_{n\to\infty}\dfrac{4n^{2}+4n+3}{2n+1}=\infty\neq0$，所",
    r"以当 $x=\pm1$ 时，原级数不收敛，所以原级数的收敛区间为 $(-1,1)$，和函数",
    r"$S(x)=\sum\limits_{n=0}^{\infty}\dfrac{4n^{2}+4n+3}{2n+1}x^{2n}=\sum\limits_{n=0}^{\infty}\dfrac{(2n+1)^{2}+2}{2n+1}x^{2n}=\sum\limits_{n=0}^{\infty}(2n+1)x^{2n}+\sum\limits_{n=0}^{\infty}\dfrac{2}{2n+1}x^{2n}$",
    r"$S_{1}(x)=\sum\limits_{n=0}^{\infty}(2n+1)x^{2n}=\left(\sum\limits_{n=0}^{\infty}x^{2n+1}\right)'=\left(\dfrac{x}{1-x^{2}}\right)'=\dfrac{1+x^{2}}{(1-x^{2})^{2}}$",
    r"令 $S_{2}(x)=\sum\limits_{n=0}^{\infty}\dfrac{2}{2n+1}x^{2n}=\dfrac{1}{x}\sum\limits_{n=0}^{\infty}\dfrac{2}{2n+1}x^{2n+1}$",
    r"其中令 $S_{3}(x)=\sum\limits_{n=0}^{\infty}\dfrac{2}{2n+1}x^{2n+1}$，则 $S_{3}'(x)=\sum\limits_{n=0}^{\infty}2x^{2n}=\dfrac{2}{1-x^{2}}$",
    r"那么 $S_{3}(x)-S_{3}(0)=\int_{0}^{x}\dfrac{2}{1-t^{2}}dt=\ln\dfrac{1+x}{1-x}$，其中 $S_{3}(0)=0$，那么 $S_{3}(x)=\ln\dfrac{1+x}{1-x}$",
    r"则 $S_{2}(x)=\dfrac{1}{x}S_{3}(x)=\dfrac{1}{x}\ln\dfrac{1+x}{1-x}$.",
    r"所以和函数：$S(x)=S_{1}(x)+S_{2}(x)=\begin{cases}\dfrac{1+x^{2}}{(1-x^{2})^{2}}+\dfrac{1}{x}\ln\dfrac{1+x}{1-x},-1<x<0\ or\ 0<x<1\\3,\qquad\qquad\qquad\quad x=0\end{cases}$.",
])

A[18] = ("f(t)=\\ln(\\sec t+\\tan t)-\\sin t; 面积=\\frac{\\pi}{4}", [
    r"【解】设切点坐标为 $(x_{0},y_{0})$，则由已知,切线为：",
    r"$y-y_{0}=k(x-x_{0})$，其中 $k=\dfrac{dy}{dx}=\dfrac{-\sin t}{f'(t)}$，由已知，切点与 $x$ 轴交点为 $(-\dfrac{y_{0}}{k}+x_{0},0)$，于",
    r"是 $\sqrt{(1+\dfrac{1}{k^{2}})y_{0}^{2}}=1$",
    r"$\cos^{2}t(1+\dfrac{f'^{2}(t)}{\sin^{2}t})=1$，$f(t)=\ln|\sec t+\tan t|-\sin t+C$，又 $f(0)=0$，$\Rightarrow C=0$",
    r"于是，$f(t)=\ln(\sec t+\tan t)-\sin t$，",
    r"$\int_{0}^{+\infty}ydx=\int_{0}^{\frac{\pi}{2}}\cos tf'(t)dt=\int_{0}^{\frac{\pi}{2}}\cos t\tan t\sin tdt=\int_{0}^{\frac{\pi}{2}}\sin^{2}tdt=\dfrac{\pi}{4}$.",
])

A[19] = ("J=\\frac{\\pi}{2}-4", [
    r"【详解】令 $C:x=0\quad 0\leqslant y\leqslant2$，则在 $C+L$ 上曲线积分（设其内部区域为 $D$）可用格",
    r"林公式，所以",
    r"$J=\int_{L}3x^{2}ydx+\left(x^{3}+x-2y\right)dy=\int_{L+C}3x^{2}ydx+\left(x^{3}+x-2y\right)dy-\int_{C}3x^{2}ydx+\left(x^{3}+x-2y\right)dy$",
    r"$=\iint\limits_{D}dxdy+\int_{0}^{2}(-2y)dy=\dfrac{\pi}{2}-4$.",
])

A[20] = ("|A|=1-a^{4}; a=-1; 通解(0,-1,0,0)^{T}+k(1,1,1,1)^{T}", [
    r"【详解】（1）按照第一列展开，得 $|\boldsymbol{A}|=1+(-1)^{5}a^{4}=1-a^{4}$.",
    r"（2）若 $\boldsymbol{Ax}=\boldsymbol{\beta}$ 有无穷多解，则 $|\boldsymbol{A}|=0$，即 $1-a^{4}=0$，解得 $a=1$ 或 $a=-1$.",
    r"当 $a=1$ 时，",
    r"$\overline{\boldsymbol{A}}=\begin{pmatrix}1&1&0&0&1\\0&1&1&0&-1\\0&0&1&1&0\\1&0&0&1&0\end{pmatrix}\to\begin{pmatrix}1&1&0&0&1\\0&1&1&0&-1\\0&0&1&1&0\\0&0&0&0&-2\end{pmatrix}$",
    r"$r(\boldsymbol{A})<r(\overline{\boldsymbol{A}})$，方程组 $\boldsymbol{Ax}=\boldsymbol{\beta}$ 无解.",
    r"当 $a=-1$ 时，",
    r"$\overline{\boldsymbol{A}}=\begin{pmatrix}1&-1&0&0&1\\0&1&-1&0&-1\\0&0&1&-1&0\\-1&0&0&1&0\end{pmatrix}\to\begin{pmatrix}1&-1&0&0&1\\0&1&-1&0&-1\\0&0&1&-1&0\\0&0&0&0&0\end{pmatrix}$",
    r"方程组 $\boldsymbol{Ax}=\boldsymbol{\beta}$ 有无穷多解，其通解为",
    r"$\begin{pmatrix}0\\-1\\0\\0\end{pmatrix}+k\begin{pmatrix}1\\1\\1\\1\end{pmatrix}$，其中 $k$ 为任意常数.",
])

A[21] = ("a=-1; f=2y_{1}^{2}+6y_{2}^{2}", [
    r"【详解】（1）对 $\boldsymbol{A}$ 初等行变换，",
    r"$\boldsymbol{A}=\begin{pmatrix}1&0&1\\0&1&1\\-1&0&a\\0&a&-1\end{pmatrix}\to\begin{pmatrix}1&0&1\\0&1&1\\0&0&a+1\\0&0&0\end{pmatrix}$",
    r"由 $r(\boldsymbol{A})=r(\boldsymbol{A}^{T}\boldsymbol{A})=2$，得 $a=-1$.",
    r"（2）",
    r"$\boldsymbol{A}^{T}\boldsymbol{A}=\begin{pmatrix}1&1&-1&-1\\0&1&0&-1\\1&0&-1&0\end{pmatrix}\begin{pmatrix}1&0&1\\0&1&1\\-1&0&-1\\0&-1&-1\end{pmatrix}=\begin{pmatrix}2&0&2\\0&2&2\\2&2&4\end{pmatrix}$",
    r"由 $\boldsymbol{A}^{T}\boldsymbol{A}$ 的特征多项式",
    r"$|\lambda\boldsymbol{E}-\boldsymbol{A}^{T}\boldsymbol{A}|=\begin{vmatrix}\lambda-2&0&-2\\0&\lambda-2&-2\\-2&-2&\lambda-4\end{vmatrix}=\begin{vmatrix}\lambda-2&0&-2\\-(\lambda-2)&\lambda-2&-2\\0&-2&\lambda-4\end{vmatrix}$",
    r"$=(\lambda-2)\begin{vmatrix}1&0&-2\\-1&\lambda-2&-2\\0&-2&\lambda-4\end{vmatrix}=(\lambda-2)\begin{vmatrix}1&0&-2\\0&\lambda-2&-4\\0&-2&\lambda-4\end{vmatrix}=\lambda(\lambda-2)(\lambda-6)$",
    r"得矩阵 $\boldsymbol{A}^{T}\boldsymbol{A}$ 的特征值 $\lambda_{1}=2$，$\lambda_{2}=6$，$\lambda_{3}=0$.",
    r"当 $\lambda_{1}=2$ 时，解得 $(2\boldsymbol{E}-\boldsymbol{A}^{T}\boldsymbol{A})\boldsymbol{x}=0$ 的基础解系 $\boldsymbol{\alpha}_{1}=(1,-1,0)^{T}$；",
    r"当 $\lambda_{2}=6$ 时，解得 $(6\boldsymbol{E}-\boldsymbol{A}^{T}\boldsymbol{A})\boldsymbol{x}=0$ 的基础解系 $\boldsymbol{\alpha}_{2}=(1,1,2)^{T}$；",
    r"当 $\lambda_{3}=0$ 时，解得 $(0\boldsymbol{E}-\boldsymbol{A}^{T}\boldsymbol{A})\boldsymbol{x}=0$ 的基础解系 $\boldsymbol{\alpha}_{3}=(1,1,-1)^{T}$；",
    r"由于 $\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}$ 已是正交向量组，只需单位化，",
    r"$\boldsymbol{\gamma}_{1}=\dfrac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\\0\end{pmatrix}, \boldsymbol{\gamma}_{2}=\dfrac{1}{\sqrt{6}}\begin{pmatrix}1\\1\\2\end{pmatrix}, \boldsymbol{\gamma}_{3}=\dfrac{1}{\sqrt{3}}\begin{pmatrix}1\\1\\-1\end{pmatrix}$",
    r"令 $\boldsymbol{Q}=(\boldsymbol{\gamma}_{1},\boldsymbol{\gamma}_{2},\boldsymbol{\gamma}_{3})$，经过正交变换 $\boldsymbol{x}=\boldsymbol{Qy}$，二次型 $f(x_{1},x_{2},x_{3})=\boldsymbol{x}^{T}(\boldsymbol{A}^{T}\boldsymbol{A})\boldsymbol{x}$ 化成标",
    r"准形 $f(x_{1},x_{2},x_{3})=2y_{1}^{2}+6y_{2}^{2}$.",
])

A[22] = ("P(X=2Y)=\\frac{1}{4}; cov(X-Y,Y)=-\\frac{2}{3}", [
    r"【详解】",
    r"(1)$P(X=2Y)=P(X=0,Y=0)+P(X=2,Y=1)$",
    r"由 $X$ 与 $Y$ 的联合概率分布可知：$P(X=0,Y=0)=\dfrac{1}{4}$，$P(X=2,Y=1)=0$，",
    r"所以 $P(X=2Y)=P(X=0,Y=0)+P(X=2,Y=1)=\dfrac{1}{4}+0=\dfrac{1}{4}$.",
    r"(2)由 $X$ 与 $Y$ 的联合概率分布可知：",
    r"随机变量 $X$,$Y$ 以及 $XY$ 的分布律如下表所示：",
    r"$\begin{array}{c|ccc} X & 0 & 1 & 2\\ \hline P & \dfrac{1}{2} & \dfrac{1}{3} & \dfrac{1}{6} \end{array}$",
    r"$\begin{array}{c|ccc} Y & 0 & 1 & 2\\ \hline P & \dfrac{1}{3} & \dfrac{1}{3} & \dfrac{1}{3} \end{array}$",
    r"$\begin{array}{c|cccc} XY & 0 & 1 & 2 & 4\\ \hline P & \dfrac{7}{12} & \dfrac{1}{3} & 0 & \dfrac{1}{12} \end{array}$",
    r"所以",
    r"$EX=0\times\dfrac{1}{2}+1\times\dfrac{1}{3}+2\times\dfrac{1}{6}=\dfrac{2}{3}$; $EX^{2}=0^{2}\times\dfrac{1}{2}+1^{2}\times\dfrac{1}{3}+2^{2}\times\dfrac{1}{6}=1$",
    r"$EY=0\times\dfrac{1}{3}+1\times\dfrac{1}{3}+2\times\dfrac{1}{3}=1$; $EY^{2}=0^{2}\times\dfrac{1}{3}+1^{2}\times\dfrac{1}{3}+2^{2}\times\dfrac{1}{3}=\dfrac{5}{3}$",
    r"$EXY=0\times\dfrac{7}{12}+1\times\dfrac{1}{3}+2\times0+4\times\dfrac{1}{12}=\dfrac{2}{3}$",
    r"则",
    r"$DX=EX^{2}-(EX)^{2}=1-\left(\dfrac{2}{3}\right)^{2}=\dfrac{5}{9}$, $DY=EY^{2}-(EY)^{2}=\dfrac{5}{3}-1^{2}=\dfrac{2}{3}$",
    r"$\mathrm{cov}(X-Y,Y)=\mathrm{cov}(X,Y)-\mathrm{cov}(Y,Y)$",
    r"$=(EXY-EX\cdot EY)-(EY^{2}-EY\cdot EY)$",
    r"$=\left(\dfrac{2}{3}-\dfrac{2}{3}\times1\right)-\left(\dfrac{5}{3}-1\times1\right)$",
    r"$=-\dfrac{2}{3}$",
])

A[23] = ("f_{Z}(z)=\\frac{1}{\\sqrt{6\\pi}\\sigma}e^{-\\frac{z^{2}}{6\\sigma^{2}}}; \\hat{\\sigma}^{2}=\\frac{1}{3n}\\sum_{i=1}^{n}Z_{i}^{2}; 无偏性证明见解析", [
    r"【详解】（1）因为随机变量 $X$ 与 $Y$ 相互独立且分别服从正态分布 $N(\mu,\sigma^{2})$ 与 $N(\mu,2\sigma^{2})$",
    r"所以 $Z=X-Y$ 也服从正态分布，其中",
    r"$EZ=E(X-Y)=EX-EY=\mu-\mu=0, DZ=D(X-Y)=DX+DY=\sigma^{2}+2\sigma^{2}=3\sigma^{2}$",
    r"从而 $Z$ 服从 $N(0,3\sigma^{2})$. 则 $Z$ 的概率密度 $f_{Z}(z)=\dfrac{1}{\sqrt{6\pi}\sigma}e^{-\frac{z^{2}}{6\sigma^{2}}}$.",
    r"（2）$Z_{1},Z_{2},\cdots,Z_{n}$ 在样本值为 $z_{1},z_{2},\cdots,z_{n}$ 的最大似然函数为：",
    r"$L(z_{1},z_{2},\cdots,z_{n};\sigma^{2})=\prod\limits_{i=1}^{n}\dfrac{1}{\sqrt{6\pi}\sigma}e^{-\frac{z_{i}^{2}}{6\sigma^{2}}}=(6\pi)^{-\frac{n}{2}}\cdot(\sigma^{2})^{-\frac{n}{2}}\cdot e^{-\frac{1}{6\sigma^{2}}\sum\limits_{i=1}^{n}z_{i}^{2}}$",
    r"两边同时取对数，有：$\ln L(\sigma^{2})=-\dfrac{n}{2}\ln(6\pi)-\dfrac{n}{2}\ln(\sigma^{2})-\dfrac{1}{6\sigma^{2}}\sum\limits_{i=1}^{n}z_{i}^{2}$",
    r"令 $\dfrac{d\ln L(\sigma^{2})}{d(\sigma^{2})}=-\dfrac{n}{2}\cdot\dfrac{1}{\sigma^{2}}+\dfrac{1}{6(\sigma^{2})^{2}}\sum\limits_{i=1}^{n}z_{i}^{2}=0$，可得：$\sigma^{2}=\dfrac{1}{3n}\sum\limits_{i=1}^{n}z_{i}^{2}$",
    r"所以 $\sigma^{2}$ 的最大似然估计为：$\hat{\sigma}^{2}=\dfrac{1}{3n}\sum\limits_{i=1}^{n}Z_{i}^{2}$",
    r"（3）由（1）知，$E\hat{\sigma}^{2}=\dfrac{1}{3n}\sum\limits_{i=1}^{n}E(Z_{i}^{2})$，其中 $E(Z_{i}^{2})=\left[E(Z_{i})\right]^{2}+D(Z_{i})=3\sigma^{2}$",
    r"从而 $E\hat{\sigma}^{2}=\dfrac{1}{3n}\sum\limits_{i=1}^{n}E(Z_{i}^{2})=\dfrac{1}{3n}\cdot3\sigma^{2}=\sigma^{2}$，所以 $\sigma^{2}$ 为 $\hat{\sigma}^{2}$ 的无偏估计量.",
])
