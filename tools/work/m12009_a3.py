# -*- coding: utf-8 -*-
"""2009 数学一 解析 解答题 15-23（原卷 p9-p13，逐字照录【解析】；本段原卷无单独【答案】行）"""

A = {}

A[15] = (r"f\left(0,\dfrac{1}{e}\right)=-\dfrac{1}{e}", [
    r"【解析】$f_{x}'(x,y)=2x(2+y^{2})=0$, $f_{y}'(x,y)=2x^{2}y+\ln y+1=0$，驻点为",
    r"$x=0, y=\dfrac{1}{e}$. $f_{xx}''=2(2+y^{2})$, $f_{yy}''=2x^{2}+\dfrac{1}{y}$, $f_{xy}''=4xy$,则",
    r"$f_{xx}''\Big|_{\left(0,\frac{1}{e}\right)}=2\left(2+\dfrac{1}{e^{2}}\right)$, $f_{xy}''\Big|_{\left(0,\frac{1}{e}\right)}=0$, $f_{yy}''\Big|_{\left(0,\frac{1}{e}\right)}=e$ 在驻点，",
    r"$A=f_{xx}''>0$, $AC-B^{2}=f_{xx}''f_{yy}''-(f_{xy}'')^{2}>0$，二元函数存在极小值 $f\left(0,\dfrac{1}{e}\right)=-\dfrac{1}{e}$.",
])

A[16] = (r"S_{1}=\dfrac{1}{2}; S_{2}=1-\ln2", [
    r"【解析】曲线 $y=x^{n}$ 与曲线 $y=x^{n+1}$ 的交点 $(0,0)$ 和 $(1,1)$，",
    r"$a_{n}=\int_{0}^{1}(x^{n}-x^{n+1})dx=\left(\dfrac{1}{n+1}x^{n+1}-\dfrac{1}{n+2}x^{n+2}\right)\Big|_{0}^{1}=\dfrac{1}{n+1}-\dfrac{1}{n+2}$，",
    r"$S_{1}=\sum\limits_{n=1}^{\infty}a_{n}=\lim\limits_{n\to\infty}\sum\limits_{i=1}^{n}a_{n}=\lim\limits_{n\to\infty}(\dfrac{1}{2}-\dfrac{1}{3}+...+\dfrac{1}{n+1}-\dfrac{1}{n+2})=\lim\limits_{n\to\infty}(\dfrac{1}{2}-\dfrac{1}{n+2})=\dfrac{1}{2}$",
    r"$S_{2}=\sum\limits_{n=1}^{\infty}a_{2n-1}=\sum\limits_{n=1}^{\infty}(\dfrac{1}{2n}-\dfrac{1}{2n+1})=\dfrac{1}{2}-\dfrac{1}{3}+...+\dfrac{1}{2n}-\dfrac{1}{2n+1}+...=\sum\limits_{n=1}^{\infty}\dfrac{(-1)^{n}}{n}$",
    r"由 $\ln(1+x)=x-\dfrac{1}{2}x^{2}+...+(-1)^{(n-1)}\dfrac{x^{n}}{n}+...$，令 $x=1$，得",
    r"$\ln(1+1)=\ln2=1-(\dfrac{1}{2}-\dfrac{1}{3}+\dfrac{1}{4}-\dfrac{1}{5}+...+\dfrac{1}{2n}-\dfrac{1}{2n+1}+...)=1-S_{2}$，",
    r"$S_{2}=1-\ln2$.",
])

A[17] = (r"(I)\ S_{1}:\dfrac{x^{2}}{4}+\dfrac{y^{2}+z^{2}}{3}=1, S_{2}:\dfrac{y^{2}+z^{2}}{4}=\left(\dfrac{1}{4}x-1\right)^{2}; (II)\ V=\pi", [
    r"【解析】(I) $S_{1}$ 的方程为 $\dfrac{x^{2}}{4}+\dfrac{y^{2}+z^{2}}{3}=1$，设切点 $\left(x_{0},y_{0}\right)$，则 $\dfrac{x^{2}}{4}+\dfrac{y^{2}}{3}=1$ 在 $\left(x_{0},y_{0}\right)$",
    r"处的切线为 $\dfrac{xx_{0}}{4}+\dfrac{yy_{0}}{3}=1$，代入 $x=4, y=0$，解得 $x_{0}=1, y_{0}=\pm\dfrac{3}{2}$，所以切线",
    r"方程 $\dfrac{x}{4}\pm\dfrac{y}{2}=1$. 得到 $S_{2}$ 的方程为 $\dfrac{y^{2}+z^{2}}{4}=\left(\dfrac{1}{4}x-1\right)^{2}$.",
    r"(II) $S_{1}$ 与 $S_{2}$ 之间的立体体积 $V$ 等于 $V_{1}-V_{2}$，其中 $V_{1}$ 是一个底面半径为 $\dfrac{3}{2}$，高为",
    r"3 的圆锥，$V_{2}$ 是椭球体 $\dfrac{x^{2}}{4}+\dfrac{y^{2}+z^{2}}{3}\leqslant1$ 在 $x=1$ 和 $x=2$ 平面之间的部分的",
    r"体积，所以 $V=\dfrac{1}{3}\pi r^{2}h-\pi\int_{1}^{2}\dfrac{3\left(4-x^{2}\right)}{4}dx=\dfrac{9}{4}\pi-\dfrac{5}{4}\pi=\pi$.",
])

A[18] = ("证明见解析", [
    r"【解析】(I) 过 $(a,f(a))$ 与 $(b,f(b))$ 的直线方程为 $y(x)=f(a)+\dfrac{f(b)-f(a)}{b-a}(x-a)$",
    r"取辅助函数 $F(x)=f(x)-f(a)-\dfrac{f(b)-f(a)}{b-a}(x-a)$，则 $F(a)=F(b)$；",
    r"$F(x)$ 在 $[a,b]$ 上连续，在 $(a,b)$ 内可导，且 $F'(x)=f'(x)-\dfrac{f(b)-f(a)}{b-a}$.",
    r"由罗尔定理，存在 $\zeta\in(a,b)$，使 $F'(\zeta)=0$，即",
    r"$f'(\zeta)-\dfrac{f(b)-f(a)}{b-a}=0$，或 $f(b)-f(a)=f'(\zeta)(b-a)$.",
    r"(II) 任取 $x\in(0,\delta)$，则函数 $f(x)$ 满足：在闭区间 $[0,x]$ 上连续，开区间 $(0,x_{0})$ 内",
    r"可导，由拉格朗日中值定理可得：$\exists\zeta\in(0,x)\subset(0,\delta)$，使得 $f'(\zeta)=\dfrac{f(x)-f(0)}{x-0}$，",
    r"两边取 $x\to0^{+}$ 时的极限,注意到 $\lim\limits_{x\to0^{+}}f'(x)=A$,可得",
    r"$f_{+}'(0)=\lim\limits_{x\to0^{+}}\dfrac{f(x)-f(0)}{x-0}=\lim\limits_{x\to0^{+}}f'(\zeta)=A$,于是 $f_{+}'(0)$ 存在，且 $f_{+}'(0)=A$.",
])

A[19] = (r"4\pi", [
    r"【解析】$I=\oiint\limits_{\Sigma}\dfrac{xdydz+ydzdx+zdxdy}{\left(x^{2}+y^{2}+z^{2}\right)^{\frac{3}{2}}}$，其中 $2x^{2}+2y^{2}+z^{2}=4$",
    r"记 $P=\dfrac{x}{\left(x^{2}+y^{2}+z^{2}\right)^{\frac{3}{2}}},Q=\dfrac{y}{\left(x^{2}+y^{2}+z^{2}\right)^{\frac{3}{2}}},R=\dfrac{z}{\left(x^{2}+y^{2}+z^{2}\right)^{\frac{3}{2}}}$，则",
    r"$\dfrac{\partial P}{\partial x}=\dfrac{y^{2}+z^{2}-2x^{2}}{\left(x^{2}+y^{2}+z^{2}\right)^{\frac{5}{2}}},\dfrac{\partial Q}{\partial y}=\dfrac{x^{2}+z^{2}-2y^{2}}{\left(x^{2}+y^{2}+z^{2}\right)^{\frac{5}{2}}},\dfrac{\partial R}{\partial z}=\dfrac{x^{2}+y^{2}-2z^{2}}{\left(x^{2}+y^{2}+z^{2}\right)^{\frac{5}{2}}}$",
    r"记 $\Sigma_{1}:x^{2}+y^{2}+z^{2}=\varepsilon^{2}\left(0<\varepsilon<\sqrt{2}\right)$，取 $\Sigma_{1}$ 外侧，并记 $\Sigma_{1},\Sigma$ 之间的区域为 $\Omega$，则",
    r"由高斯公式有，$\oiint\limits_{\Sigma-\Sigma_{1}}\dfrac{xdydz+ydxdz+zdxdy}{\left(x^{2}+y^{2}+z^{2}\right)^{\frac{3}{2}}}=\iiint\limits_{\Omega}\left(\dfrac{\partial P}{\partial x}+\dfrac{\partial Q}{\partial y}+\dfrac{\partial R}{\partial z}\right)dV=0$",
    r"$\oiint\limits_{\Sigma}\dfrac{xdydz+ydzdx+zdxdy}{\left(x^{2}+y^{2}+z^{2}\right)^{\frac{3}{2}}}=\oiint\limits_{\Sigma_{1}}\dfrac{xdydz+ydzdx+zdxdy}{\left(x^{2}+y^{2}+z^{2}\right)^{\frac{3}{2}}}=$",
    r"$\dfrac{1}{\varepsilon^{3}}\oiint\limits_{\Sigma_{1}}xdydz+ydxdz+zdxdy=\dfrac{1}{\varepsilon^{3}}\iiint\limits_{\Omega}3dV=4\pi$",
])

A[20] = (r"(I)\ \boldsymbol{\zeta}_{2}=\left(-\dfrac{1}{2},\dfrac{1}{2},0\right)^{T}+k_{1}\left(\dfrac{1}{2},-\dfrac{1}{2},1\right)^{T}; \boldsymbol{\zeta}_{3}=\left(-\dfrac{1}{2},0,0\right)^{T}+k_{2}(-1,1,0)^{T}+k_{3}(0,0,1)^{T}; (II)\ 证明见解析", [
    r"【解析】(I) 解方程 $\boldsymbol{A\zeta}_{2}=\boldsymbol{\zeta}_{1}$，对增广矩阵 $\left(\boldsymbol{A},\boldsymbol{\zeta}_{1}\right)$ 做初等行变换，",
    r"$\left(\boldsymbol{A},\boldsymbol{\zeta}_{1}\right)\to\begin{pmatrix}1&-1&-1&-1\\-1&1&1&1\\0&-4&-2&-2\end{pmatrix}\to\begin{pmatrix}1&-1&-1&-1\\0&1&\dfrac{1}{2}&\dfrac{1}{2}\\0&0&0&0\end{pmatrix}\to\begin{pmatrix}1&0&-\dfrac{1}{2}&-\dfrac{1}{2}\\0&1&\dfrac{1}{2}&\dfrac{1}{2}\\0&0&0&0\end{pmatrix}$",
    r"解得，$\boldsymbol{\zeta}_{2}=\begin{pmatrix}-\dfrac{1}{2}\\\dfrac{1}{2}\\0\end{pmatrix}+k_{1}\begin{pmatrix}\dfrac{1}{2}\\-\dfrac{1}{2}\\1\end{pmatrix}$，其中 $k_{1}$ 为任意常数. 解方程 $\boldsymbol{A}^{2}\boldsymbol{\zeta}_{3}=\boldsymbol{\zeta}_{1}$，",
    r"$\boldsymbol{A}^{2}=\begin{pmatrix}2&2&0\\-2&-2&0\\4&4&0\end{pmatrix}$，对增广矩阵 $\left(\boldsymbol{A}^{2},\boldsymbol{\zeta}_{1}\right)$ 做初等行变换，",
    r"$\left(\boldsymbol{A}^{2},\boldsymbol{\zeta}_{1}\right)\to\begin{pmatrix}2&2&0&-1\\-2&-2&0&1\\4&4&0&-2\end{pmatrix}\to\begin{pmatrix}1&1&0&-\dfrac{1}{2}\\0&0&0&0\\0&0&0&0\end{pmatrix}$,那么非齐次方程的解是，",
    r"$\boldsymbol{\zeta}_{3}=\begin{pmatrix}-\dfrac{1}{2}\\0\\0\end{pmatrix}+k_{2}\begin{pmatrix}-1\\1\\0\end{pmatrix}+k_{3}\begin{pmatrix}0\\0\\1\end{pmatrix}$，其中 $k_{2},k_{3}$ 为任意常数.",
    r"(II) 证明：由于",
    r"$\begin{vmatrix}-1&-\dfrac{1}{2}+\dfrac{1}{2}k_{1}&-\dfrac{1}{2}-k_{2}\\1&\dfrac{1}{2}-\dfrac{1}{2}k_{1}&k_{2}\\-2&k_{1}&k_{3}\end{vmatrix}=\begin{vmatrix}0&0&-\dfrac{1}{2}\\1&\dfrac{1}{2}-\dfrac{1}{2}k_{1}&k_{2}\\-2&k_{1}&k_{3}\end{vmatrix}=-\dfrac{1}{2}\left(k_{1}+1-k_{1}\right)=-\dfrac{1}{2}\neq0$.",
    r"故 $\boldsymbol{\zeta}_{1},\boldsymbol{\zeta}_{2},\boldsymbol{\zeta}_{3}$ 线性无关.",
])

A[21] = (r"(I)\ 特征值 a-2,a,a+1; (II)\ a=2", [
    r"【解析】(I) $\boldsymbol{A}=\begin{pmatrix}a&0&1\\0&a&-1\\1&-1&a-1\end{pmatrix}$.",
    r"$|\lambda\boldsymbol{E}-\boldsymbol{A}|=\begin{vmatrix}\lambda-a&0&-1\\0&\lambda-a&1\\-1&1&\lambda-a+1\end{vmatrix}=\begin{vmatrix}\lambda-a&\lambda-a&0\\0&\lambda-a&1\\-1&1&\lambda-a+1\end{vmatrix}=\begin{vmatrix}\lambda-a&0&0\\0&\lambda-a&1\\-1&2&\lambda-a+1\end{vmatrix}$",
    r"$=(\lambda-a)\left((\lambda-a)^{2}+(\lambda-a)-2)\right)=(\lambda-a)(\lambda-a-1)(\lambda-a+2)$.",
    r"所以二次型的矩阵 $\boldsymbol{A}$ 的特征值为 $a-2,a,a+1$.",
    r"(II) 若规范形为 $y_{1}^{2}+y_{2}^{2}$，说明有两个特征值为正，一个为 0，当 $a=2$ 时，三个特",
    r"征值为 0,2,3，这时，二次型的规范形为 $y_{1}^{2}+y_{2}^{2}$.",
])

A[22] = (r"(I)\ \dfrac{4}{9}; (II)\ P\{X=0,Y=0\}=\dfrac{1}{4},P\{X=0,Y=1\}=\dfrac{1}{3},P\{X=0,Y=2\}=\dfrac{1}{9},P\{X=1,Y=0\}=\dfrac{1}{6},P\{X=1,Y=1\}=\dfrac{1}{9},P\{X=2,Y=0\}=\dfrac{1}{36},其余为 0", [
    r"【解析】(I) 在没有取白球的情况下取了一次红球，利用样本空间的缩减法，相当于只",
    r"有 1 个红球，2 个黑球放回摸两次，其中摸一个红球的概率，所以 $P\left\{X=1|Z=0\right\}$",
    r"$=\dfrac{C_{2}^{1}\times2}{3^{2}}=\dfrac{4}{9}$.",
    r"(II) $X$，$Y$ 取值范围为 0,1,2,故",
    r"$P(X=0,Y=0)=\dfrac{C_{3}^{1}\times C_{3}^{2}}{6^{2}}=\dfrac{1}{4}$, $P(X=1,Y=0)=\dfrac{C_{2}^{1}\times C_{3}^{1}}{6^{2}}=\dfrac{1}{6}$,",
    r"$P(X=2,Y=0)=\dfrac{1}{6^{2}}=\dfrac{1}{36}$, $P(X=0,Y=1)=\dfrac{C_{2}^{1}\times C_{2}^{1}\times C_{3}^{1}}{6^{2}}=\dfrac{1}{3}$,",
    r"$P(X=1,Y=1)=\dfrac{C_{2}^{1}\times C_{2}^{1}}{6^{2}}=\dfrac{1}{9}$, $P(X=2,Y=1)=0$,",
    r"$P(X=0,Y=2)=\dfrac{C_{2}^{1}\times C_{2}^{1}}{6^{2}}=\dfrac{1}{9}$, $P(X=1,Y=2)=0, P(X=2,Y=2)=0$,",
    r"$\begin{array}{c|ccc} Y & 0 & 1 & 2\\ \hline 0 & 1/4 & 1/3 & 1/9\\ 1 & 1/6 & 1/9 & 0\\ 2 & 1/36 & 0 & 0 \end{array}$",
])

A[23] = (r"(I)\ \hat{\lambda}=\dfrac{2}{\overline{X}}; (II)\ \hat{\lambda}=\dfrac{2}{\overline{X}}", [
    r"【解析】(I) 由 $EX=\int_{-\infty}^{+\infty}xf\left(x\right)dx=\int_{0}^{+\infty}\lambda^{2}x^{2}e^{-\lambda x}dx=\dfrac{2}{\lambda}$，令 $EX=\overline{X}$，可得总体参",
    r"数 $\lambda$ 的矩估计量 $\hat{\lambda}=\dfrac{2}{\overline{X}}$.",
    r"(II) 构造似然函数 $L(x_{1},\cdots\cdots x_{n},\lambda)=\begin{cases}\prod\limits_{i=1}^{n}f\left(x_{i}\right)=\lambda^{2n}\cdot\prod\limits_{i=1}^{n}x_{i}.e^{-\lambda\sum\limits_{i=1}^{n}x_{i}}, & x_{1},....x_{n}>0\\ 0, & \text{其他}\end{cases}$",
    r"当 $x_{1},x_{2}...x_{n}>0$ 时，取对数 $\ln L=2n\ln\lambda+\sum\limits_{i=1}^{n}\ln x_{i}-\lambda\sum\limits_{i=1}^{\pi}x_{i}$",
    r"令 $\dfrac{d\ln L}{d\lambda}=0\Rightarrow\dfrac{2n}{\lambda}-\sum\limits_{i=1}^{n}x_{i}=0$, $\lambda=\dfrac{2n}{\sum\limits_{i=1}^{n}x_{i}}=\dfrac{2}{\dfrac{1}{n}\sum\limits_{i=1}^{n}x_{i}}$，故其最大似然估计量为 $\hat{\lambda}=\dfrac{2}{\overline{X}}$.",
])
