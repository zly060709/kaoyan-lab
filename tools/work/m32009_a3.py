# -*- coding: utf-8 -*-
"""2009 数学三 解析 解答题 15-23（原卷 p8-p12，逐字照录）"""

A = {}

A[15] = (r"f(0,1/e)=-1/e", [
    r"【解析】$f'_{x}(x,y)=2x(2+y^{2})=0$, $f'_{y}(x,y)=2x^{2}y+\ln y+1=0$，驻点为",
    r"$x=0,y=\dfrac{1}{e}$. $f''_{xx}=2(2+y^{2}),f''_{yy}=2x^{2}+\dfrac{1}{y},f''_{xy}=4xy$,则",
    r"$f''_{xx}\Big|_{\left(0,\frac{1}{e}\right)}=2\left(2+\dfrac{1}{e^{2}}\right)$, "
    r"$f''_{xy}\Big|_{\left(0,\frac{1}{e}\right)}=0$, $f''_{yy}\Big|_{\left(0,\frac{1}{e}\right)}=e$ 在驻点，",
    r"$A=f''_{xx}>0,AC-B^{2}=f''_{xx}f''_{yy}-(f''_{xy})^{2}>0$，二元函数存在极小值 $f\left(0,\dfrac{1}{e}\right)=-\dfrac{1}{e}$",
])

A[16] = (r"x\ln(1+\sqrt{(1+x)/x})+\frac{1}{2}\ln(\sqrt{1+x}+\sqrt{x})-\frac{1}{2}(\sqrt{x(x+1)}-x)+C", [
    r"【解析】令 $\sqrt{\dfrac{1+x}{x}}=t$ 得 $x=\dfrac{1}{t^{2}-1}$，",
    r"原式 $=\displaystyle\int\ln(1+t)d(\dfrac{1}{t^{2}-1})=\dfrac{\ln(1+t)}{t^{2}-1}-\int\dfrac{1}{t^{2}-1}\cdot\dfrac{1}{t+1}dt$",
    r"$=\dfrac{\ln(1+t)}{t^{2}-1}-\displaystyle\int\left(\dfrac{1}{4(t-1)}+\dfrac{-1}{4(t+1)}+\dfrac{-1}{2(t+1)^{2}}\right)dt"
    r"=\dfrac{\ln(1+t)}{t^{2}-1}+\dfrac{1}{4}\ln\Bigl|\dfrac{t+1}{t-1}\Bigr|-\dfrac{1}{2(t+1)}+C$",
    r"$=x\ln(1+\sqrt{\dfrac{1+x}{x}})+\dfrac{1}{4}\ln\dfrac{\sqrt{\dfrac{1+x}{x}}+1}{\sqrt{\dfrac{1+x}{x}}-1}"
    r"-\dfrac{1}{2(\sqrt{\dfrac{1+x}{x}}+1)}+C$",
    r"$=x\ln(1+\sqrt{\dfrac{1+x}{x}})+\dfrac{1}{2}\ln(\sqrt{1+x}+\sqrt{x})-\dfrac{1}{2}(\sqrt{x(x+1)}-x)+C$. ",
])

A[17] = (r"-8/3", [
    r"【解析】由 $(x-1)^{2}+(y-1)^{2}\leqslant2$ 得 $r\leqslant2(\sin\theta+\cos\theta)$，",
    r"所以 $\displaystyle\iint\limits_{D}(x-y)dxdy"
    r"=\int_{\frac{\pi}{4}}^{\frac{3\pi}{4}}d\theta\int_{0}^{2(\sin\theta+\cos\theta)}(r\cos\theta-r\sin\theta)rdr$",
    r"$=\displaystyle\int_{\frac{\pi}{4}}^{\frac{3\pi}{4}}\left[\dfrac{1}{3}(\cos\theta-\sin\theta)r^{3}\Big|_{0}^{2(\sin\theta+\cos\theta)}\right]d\theta$",
    r"$=\displaystyle\int_{\frac{\pi}{4}}^{\frac{3\pi}{4}}\dfrac{8}{3}(\cos\theta-\sin\theta).(\sin\theta+\cos\theta)^{3}d\theta$",
    r"$=\dfrac{8}{3}\displaystyle\int_{\frac{\pi}{4}}^{\frac{3\pi}{4}}(\sin\theta+\cos\theta)^{3}d(\sin\theta+\cos\theta)"
    r"=\dfrac{8}{3}\times\dfrac{1}{4}(\sin\theta+\cos\theta)^{4}\Big|_{\frac{\pi}{4}}^{\frac{3\pi}{4}}=-\dfrac{8}{3}$. ",
])

A[18] = ("证明见解析", [
    r"【解析】(I) 过 $(a,f(a))$ 与 $(b,f(b))$ 的直线方程为 $f(x)=f(a)+\dfrac{f(b)-f(a)}{b-a}(x-a)$，",
    r"取辅助函数 $F(x)=f(x)-f(a)-\dfrac{f(b)-f(a)}{b-a}(x-a)$，则 $F(a)=F(b)$；",
    r"$F(x)$ 在 $[a,b]$ 上连续，在 $(a,b)$ 内可导，且 $F'(x)=f'(x)-\dfrac{f(b)-f(a)}{b-a}$. ",
    r"由罗尔定理，存在 $\zeta\in(a,b)$，使 $F'(\zeta)=0$，即",
    r"$f'(\zeta)-\dfrac{f(b)-f(a)}{b-a}=0$，或 $f(b)-f(a)=f'(\zeta)(b-a)$. ",
    r"（II）任取 $x\in(0,\delta)$，则函数 $f(x)$ 满足：",
    r"在闭区间 $[0,x]$ 上连续，开区间 $(0,x)$ 内可导，由拉格朗日中值定理可得：",
    r"$\exists\eta\in(0,x)\subset(0,\delta)$，使得 $f'(\eta)=\dfrac{f(x)-f(0)}{x-0}$，",
    r"两边取 $x\to0^{+}$ 时的极限，注意到 $\lim\limits_{x\to0^{+}}f'(x)=A$，可得",
    r"$f'_{+}(0)=\lim\limits_{x\to0^{+}}\dfrac{f(x)-f(0)}{x-0}=\lim\limits_{x\to0^{+}}f'(\eta)=A$，",
    r"于是 $f'_{+}(0)$ 存在，且 $f'_{+}(0)=A$. ",
])

A[19] = (r"2y+1/\sqrt{y}-3x=0", [
    r"【解析】旋转体的体积为 $V=\displaystyle\int_{1}^{t}\pi f(x)^{2}dx=\pi\int_{1}^{t}f(x)^{2}dx$，",
    r"曲边梯形的面积为：$s=\displaystyle\int_{1}^{t}f(x)dx$，则由题可知",
    r"$V=\pi ts\Rightarrow\pi\int_{1}^{t}f(x)^{2}dx=\pi t\int_{1}^{t}f(x)dx\Rightarrow\int_{1}^{t}f(x)^{2}dx=t\int_{1}^{t}f(x)dx$. ",
    r"两边对 $t$ 求导可得 $f(x)^{2}=\int_{1}^{t}f(x)dx+tf(t)\Rightarrow f(t)^{2}-tf(t)=\int_{1}^{t}f(x)dx$",
    r"继续求导可得 $2f(t)f'(t)-f(t)-tf'(t)=f(t)$，化简可得",
    r"$(2f(t)-t)f'(t)=2f(t)$ 记 $f(t)=y$，则 $\dfrac{dt}{dy}+\dfrac{1}{2y}t=1$，解之得 $t=Cy^{-\frac{1}{2}}+\dfrac{2}{3}y$. ",
    r"在（V）式中令 $t=1$，则 $f^{2}(1)-f(1)=0$,且 $f(t)>0,\therefore f(1)=1$，代入 $t=Cy^{-\frac{1}{2}}+\dfrac{2}{3}y$ 得",
    r"$C=\dfrac{1}{3}$, $\therefore t=\dfrac{1}{3}\left(\dfrac{1}{\sqrt{y}}+2y\right)$. 所以该曲线方程为：$2y+\dfrac{1}{\sqrt{y}}-3x=0$. ",
])

A[20] = (r"(I) \zeta_2=(-1/2,1/2,0)^T+k_1(-1/2,-1/2,1)^T, \zeta_3=(-1/2,0,0)^T+k_2(-1,1,0)^T+k_3(0,0,1)^T (k_i 为任意常数); (II) 证明见解析", [
    r"【解析】(I) 解方程 $\boldsymbol{A}\boldsymbol{\zeta}_{2}=\boldsymbol{\zeta}_{1}$，对增广矩阵 $\left(\boldsymbol{A},\boldsymbol{\zeta}_{1}\right)$ 做初等行变换，",
    r"$\left(\boldsymbol{A},\boldsymbol{\zeta}_{1}\right)\to\begin{pmatrix}1&-1&-1&-1\\-1&1&1&1\\0&-4&-2&-2\end{pmatrix}"
    r"\to\begin{pmatrix}1&-1&-1&-1\\0&1&\frac{1}{2}&\frac{1}{2}\\0&0&0&0\end{pmatrix}"
    r"\to\begin{pmatrix}1&0&-\frac{1}{2}&-\frac{1}{2}\\0&1&\frac{1}{2}&\frac{1}{2}\\0&0&0&0\end{pmatrix}$",
    r"解得，$\boldsymbol{\zeta}_{2}=\begin{pmatrix}-\frac{1}{2}\\\frac{1}{2}\\0\end{pmatrix}"
    r"+k_{1}\begin{pmatrix}-\frac{1}{2}\\-\frac{1}{2}\\1\end{pmatrix}$，其中 $k_{1}$ 为任意常数. 解方程 $\boldsymbol{A}^{2}\boldsymbol{\zeta}_{3}=\boldsymbol{\zeta}_{1}$，",
    r"$\boldsymbol{A}^{2}=\begin{pmatrix}2&2&0\\-2&-2&0\\4&4&0\end{pmatrix}$，对增广矩阵 $\left(\boldsymbol{A}^{2},\boldsymbol{\zeta}_{1}\right)$ 做初等行变换，",
    r"$\left(\boldsymbol{A}^{2},\boldsymbol{\zeta}_{1}\right)\to\begin{pmatrix}2&2&0&-1\\-2&-2&0&1\\4&4&0&-2\end{pmatrix}"
    r"\to\begin{pmatrix}1&1&0&-\frac{1}{2}\\0&0&0&0\\0&0&0&0\end{pmatrix}$",
    r"解得，$\boldsymbol{\zeta}_{3}=\begin{pmatrix}-\frac{1}{2}\\0\\0\end{pmatrix}"
    r"+k_{2}\begin{pmatrix}-1\\1\\0\end{pmatrix}+k_{3}\begin{pmatrix}0\\0\\1\end{pmatrix}$，其中 $k_{2},k_{3}$ 为任意常数.",
    r"（II）证明：由于",
    r"$\left|\begin{matrix}-1&-\frac{1}{2}+\frac{1}{2}k_{1}&-\frac{1}{2}-k_{2}\\ 1&\frac{1}{2}-\frac{1}{2}k_{1}&k_{2}\\ -2&k_{1}&k_{3}\end{matrix}\right|"
    r"=\left|\begin{matrix}0&0&-\frac{1}{2}\\ 1&\frac{1}{2}-\frac{1}{2}k_{1}&k_{2}\\ -2&k_{1}&k_{3}\end{matrix}\right|"
    r"=-\dfrac{1}{2}(k_{1}+1-k_{1})=-\dfrac{1}{2}\neq0$. ",
    r"故 $\boldsymbol{\zeta}_{1},\boldsymbol{\zeta}_{2},\boldsymbol{\zeta}_{3}$ 线性无关.",
])

A[21] = (r"(I) 特征值为 a-2, a, a+1; (II) a=2", [
    r"【解析】(I) $\boldsymbol{A}=\begin{pmatrix}a&0&1\\0&a&-1\\1&-1&a-1\end{pmatrix}$. ",
    r"$|\lambda\boldsymbol{E}-\boldsymbol{A}|=\left|\begin{matrix}\lambda-a&0&-1\\0&\lambda-a&1\\-1&1&\lambda-a+1\end{matrix}\right|"
    r"=\left|\begin{matrix}\lambda-a&\lambda-a&0\\0&\lambda-a&1\\-1&1&\lambda-a+1\end{matrix}\right|"
    r"=\left|\begin{matrix}\lambda-a&0&0\\0&\lambda-a&1\\-1&2&\lambda-a+1\end{matrix}\right|$",
    r"$=(\lambda-a)\left((\lambda-a)^{2}+(\lambda-a)-2\right)=(\lambda-a)(\lambda-a-1)(\lambda-a+2)$. ",
    r"所以二次型的矩阵 $\boldsymbol{A}$ 的特征值为 $a-2,a,a+1$. ",
    r"（II）若规范形为 $y_{1}^{2}+y_{2}^{2}$，说明有两个特征值为正，一个为 0，当 $a=2$ 时，三个特征值为",
    r"$0,2,3$，得二次型的规范形为 $y_{1}^{2}+y_{2}^{2}$. ",
])

A[22] = (r"(I) f_{Y|X}(y|x)=1/x (0<y<x), 其他为 0; (II) (e-2)/(e-1)", [
    r"【解析】(I) $f(x,y)=\begin{cases}e^{-x}&0<y<x\\0&\text{其他}\end{cases}$ 得其边缘密度函数",
    r"$f_{x}(x)=\displaystyle\int_{0}^{x}e^{-x}dy=xe^{-x}\quad x>0$. ",
    r"故 $f_{y|x}(y|x)=\dfrac{f(x,y)}{f_{x}(x)}=\dfrac{1}{x}\quad 0<y<x$,",
    r"即 $f_{y|x}(y|x)=\begin{cases}\dfrac{1}{x}&0<y<x\\0&\text{其他}\end{cases}$. ",
    r"（II）$P[X\leqslant1,Y\leqslant1]=\displaystyle\iint\limits_{x\leqslant1,y\leqslant1}f(x,y)dxdy"
    r"=\int_{0}^{1}dx\int_{0}^{x}e^{-x}dy=\int_{0}^{1}xe^{-x}dx=1-2e^{-1}$,",
    r"$f_{Y}(y)=\displaystyle\int_{y}^{+\infty}e^{-x}dx=-e^{-x}\Big|_{y}^{+\infty}=e^{-y},y>0$,",
    r"所以 $P[Y\leqslant1]=\displaystyle\int_{0}^{1}e^{-y}dy=-e^{-y}\Big|_{0}^{1}=-e^{-1}+1=1-e^{-1}$,",
    r"所以 $P[X\leqslant1,Y\leqslant1]=\dfrac{1-2e^{-1}}{1-e^{-1}}=\dfrac{e-2}{e-1}$. ",
])

A[23] = (r"(I) 4/9; (II) 概率分布表见解析", [
    r"【解析】(I) 在没有取白球的情况下取了一次红球，利用样本空间的缩减法，相当于只有 1 个红球，"
    r"2 个黑球放回摸两次，其中摸一个红球的概率，所以 $P\{X=1|Z=0\}=$",
    r"$\dfrac{C_{2}^{1}\times2}{3^{2}}=\dfrac{4}{9}$. ",
    r"（II）$X$，$Y$ 取值范围为 $0,1,2$，故",
    r"$P(X=0,Y=0)=\dfrac{C_{3}^{1}\times C_{3}^{1}}{6^{2}}=\dfrac{1}{4}$,$P(X=1,Y=0)=\dfrac{C_{2}^{1}\times C_{3}^{1}}{6^{2}}=\dfrac{1}{6}$;",
    r"$P(X=2,Y=0)=\dfrac{1}{6^{2}}=\dfrac{1}{36}$,$P(X=0,Y=1)=\dfrac{C_{2}^{1}\times C_{2}^{1}\times C_{3}^{1}}{6^{2}}=\dfrac{1}{3}$;",
    r"$P(X=1,Y=1)=\dfrac{C_{2}^{1}\times C_{2}^{1}}{6^{2}}=\dfrac{1}{9}$,$P(X=2,Y=1)=0$;",
    r"$P(X=0,Y=2)=\dfrac{C_{2}^{1}\times C_{2}^{1}}{6^{2}}=\dfrac{1}{9}$,$P(X=1,Y=2)=0$,$P(X=2,Y=2)=0$. ",
    r"（原卷为分布表，逐格照录）$X\backslash Y$：0，1，2；$X=0$ 行：1/4，1/3，1/9；$X=1$ 行：1/6，1/9，0；$X=2$ 行：1/36，0，0.",
])
