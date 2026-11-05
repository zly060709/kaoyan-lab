# -*- coding: utf-8 -*-
"""2019 数学三 解析 解答题 15-23（原卷 p7-p12，逐字照录）"""

A = {}

A[15] = (r"f(-1)=1-\dfrac{1}{e} 与 f(\dfrac{1}{e})=e^{-\frac{2}{e}} 均为极小值, f(0)=1 为极大值", [
    r"【解析】$x>0$ 时，$f'(x)=(e^{2x\ln x})'=e^{2x\ln x}(2\ln x+2)$；$x<0$ 时，$f'(x)=(x+1)e^{x}$；",
    r"$f'_{+}(0)=\lim\limits_{x\to0^{+}}\dfrac{f(x)-f(0)}{x-0}=\lim\limits_{x\to0^{+}}\dfrac{e^{2x\ln x}-1}{x}"
    r"=\lim\limits_{x\to0^{+}}\dfrac{2x\ln x}{x}=\lim\limits_{x\to0^{+}}2\ln x=-\infty$，",
    r"所以 $f'(0)$ 不存在，因此 $f'(x)=\begin{cases}2x^{2x}(1+\ln x),&x>0,\\ (x+1)e^{x},&x<0.\end{cases}$",
    r"令 $f'(x)=0$，得驻点 $x=-1$ 或 $x=\dfrac{1}{e}$；另外 $f(x)$ 还有一个不可导点 $x=0$；",
    r"又 $(-\infty,-1)$ 为单调递减，$(-1,0)$ 为单调递增，$(0,\dfrac{1}{e})$ 为单调递减，$(\dfrac{1}{e},+\infty)$ 为单调递增；因",
    r"此有极小值 $f(-1)=1-\dfrac{1}{e}$ 和极小值 $f(\dfrac{1}{e})=e^{-\frac{2}{e}}$，极大值 $f(0)=1$",
])

A[16] = (r"1-3f''_{11}-f''_{22}", [
    r"【解析】依题意知，",
    r"$\dfrac{\partial g}{\partial x}=y-f'_{1}(x+y,x-y)-f'_{2}(x+y,x-y)$，",
    r"$\dfrac{\partial g}{\partial y}=x-f'_{1}(x+y,x-y)+f'_{2}(x+y,x-y)$",
    r"因为 $f(u,v)$ 具有二阶连续偏导数，故 $f''_{12}=f''_{21}$，因此，",
    r"$\dfrac{\partial^{2}g}{\partial x^{2}}=-(f''_{11}+f''_{12})-(f''_{21}+f''_{22})=-f''_{11}-2f''_{12}-f''_{22}$，",
    r"$\dfrac{\partial^{2}g}{\partial x\partial y}=1-(f''_{11}-f''_{12})-(f''_{21}-f''_{22})=1-f''_{11}+f''_{22}$，",
    r"$\dfrac{\partial^{2}g}{\partial y^{2}}=-(f''_{11}-f''_{12})+(f''_{21}-f''_{22})=-f''_{11}+2f''_{12}-f''_{22}$.",
    r"所以，$\dfrac{\partial^{2}g}{\partial x^{2}}+\dfrac{\partial^{2}g}{\partial x\partial y}+\dfrac{\partial^{2}g}{\partial y^{2}}=1-3f''_{11}-f''_{22}$，",
])

A[17] = (r"(I)\ y(x)=\sqrt{x}e^{\frac{x^{2}}{2}};\ (II)\ V=\dfrac{\pi}{2}(e^{4}-e)", [
    r"【解析】(I)",
    r"$y(x)=e^{\int x\mathrm{d}x}\Bigl(\int e^{-\int x\mathrm{d}x}\cdot\dfrac{1}{2\sqrt{x}}e^{\frac{x^{2}}{2}}\mathrm{d}x+C\Bigr)"
    r"=e^{\frac{x^{2}}{2}}\Bigl(\int\dfrac{1}{2\sqrt{x}}\mathrm{d}x+C\Bigr)=e^{\frac{x^{2}}{2}}(\sqrt{x}+C)$；",
    r"又由 $y(1)=\sqrt{e}$ 得 $C=0$，最终有 $y(x)=\sqrt{x}e^{\frac{x^{2}}{2}}$",
    r"(II) 所求体积为",
    r"$V=\displaystyle\int_{1}^{2}\pi(\sqrt{x}e^{\frac{x^{2}}{2}})^{2}\mathrm{d}x=\pi\int_{1}^{2}xe^{x^{2}}\mathrm{d}x"
    r"=\dfrac{\pi}{2}e^{x^{2}}\Bigl|_{1}^{2}=\dfrac{\pi}{2}(e^{4}-e)$",
])

A[18] = (r"\dfrac{1}{2}+\dfrac{1}{e^{\pi}-1}", [
    r"【解析】设在区间 $[n\pi,(n+1)\pi]$（$n=0,1,2,\cdots$）上所围的面积记为 $u_{n}$，则",
    r"$u_{n}=\displaystyle\int_{n\pi}^{(n+1)\pi}e^{-x}|\sin x|\,\mathrm{d}x=(-1)^{n}\int_{n\pi}^{(n+1)\pi}e^{-x}\sin x\mathrm{d}x$；",
    r"记 $I=\displaystyle\int e^{-x}\sin x\mathrm{d}x$，则 $I=-\int e^{-x}\mathrm{d}\cos x=-(e^{-x}\cos x-\int\cos x\mathrm{d}e^{-x})$",
    r"$=-e^{-x}\cos x-\int e^{-x}\mathrm{d}\sin x=-e^{-x}\cos x-(e^{-x}\sin x-\int\sin x\mathrm{d}e^{-x})$",
    r"$=-e^{-x}(\cos x+\sin x)-I$，",
    r"所以 $I=-\dfrac{1}{2}e^{-x}(\cos x+\sin x)+C$；",
    r"因此 $u_{n}=(-1)^{n}(-\dfrac{1}{2})e^{-x}(\cos x+\sin x)\Bigl|_{n\pi}^{(n+1)\pi}=\dfrac{1}{2}(e^{-(n+1)\pi}+e^{-n\pi})$；",
    r"（这里需要注意 $\cos n\pi=(-1)^{n}$）",
    r"因此所求面积为 $\displaystyle\sum\limits_{n=0}^{\infty}u_{n}=\dfrac{1}{2}+\sum\limits_{n=1}^{\infty}e^{-n\pi}"
    r"=\dfrac{1}{2}+\dfrac{e^{-\pi}}{1-e^{-\pi}}=\dfrac{1}{2}+\dfrac{1}{e^{\pi}-1}$",
])

A[19] = (r"(I) 证明见解析; (II) \lim\limits_{n\to\infty}\dfrac{a_{n}}{a_{n-1}}=1", [
    r"【解析】(I) $a_{n+1}-a_{n}=\displaystyle\int_{0}^{1}x^{n}(x-1)\sqrt{1-x^{2}}\mathrm{d}x\leqslant0$ 且不恒等于 0，"
    r"所以 $\{a_{n}\}$ 单调递减.",
    r"$a_{n}=-\dfrac{1}{3}\displaystyle\int_{0}^{1}x^{n-1}d(1-x^{2})^{\frac{3}{2}}"
    r"=-\dfrac{1}{3}\Bigl[x^{n-1}(1-x^{2})^{\frac{3}{2}}\Bigr|_{0}^{1}-\int_{0}^{1}(1-x^{2})^{\frac{3}{2}}dx^{n-1}\Bigr]$",
    r"$=\dfrac{n-1}{3}\displaystyle\int_{0}^{1}x^{n-2}(1-x^{2})\sqrt{1-x^{2}}\mathrm{d}x"
    r"=\dfrac{n-1}{3}\bigl(\int_{0}^{1}x^{n-2}\sqrt{1-x^{2}}\mathrm{d}x-\int_{0}^{1}x^{n}\sqrt{1-x^{2}}\mathrm{d}x\bigr)$",
    r"$=\dfrac{n-1}{3}(a_{n-2}-a_{n})$，",
    r"从而有 $a_{n}=\dfrac{n-1}{n+2}a_{n-2}$（$n=2,3,\cdots$）；",
    r"(II) 因为 $\dfrac{a_{n}}{a_{n-2}}<\dfrac{a_{n}}{a_{n-1}}<\dfrac{a_{n}}{a_{n}}=1$，"
    r"而 $\lim\limits_{n\to\infty}\dfrac{a_{n}}{a_{n-2}}=\lim\limits_{n\to\infty}\dfrac{n-1}{n+2}=1$，"
    r"由夹逼准则知 $\lim\limits_{n\to\infty}\dfrac{a_{n}}{a_{n-1}}=1$",
])

A[20] = (r"a\neq-1; a=1 时 \beta_{3}=(3-2k)\alpha_{1}+(k-2)\alpha_{2}+k\alpha_{3}; "
         r"a\neq\pm1 时 \beta_{3}=\alpha_{1}-\alpha_{2}+\alpha_{3}", [
    r"【解析】令 $A=(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3})$，"
    r"$B=(\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3})$,因向量组（I）与（II）等价，故",
    r"$r(A)=r(B)=r(A,B)$，对矩阵 $(A,B)$ 作初等行变换.",
    r"$(A,B)=\begin{pmatrix}1&1&1&1&0&1\\ 1&0&2&1&2&3\\ 4&4&a^{2}+3&a+3&1-a&a^{2}+3\end{pmatrix}"
    r"\to\begin{pmatrix}1&1&1&1&0&1\\ 0&-1&1&0&2&2\\ 0&0&a^{2}-1&a-1&1-a&a^{2}-1\end{pmatrix}$",
    r"当 $a=1$ 时，$r(A)=r(B)=r(A,B)=2$；当 $a=-1$ 时，$r(A)=r(B)=2$，但 $r(A,B)=3$；",
    r"当 $a\neq\pm1$ 时，$r(A)=r(B)=r(A,B)=3$.综上，只需 $a\neq-1$ 即可.",
    r"(I) 当 $a=1$ 时，$(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3},\boldsymbol{\beta}_{3})"
    r"\to\begin{pmatrix}1&0&2&3\\ 0&1&-1&-2\\ 0&0&0&0\end{pmatrix}$，"
    r"故 $\boldsymbol{\beta}_{3}=x_{1}\boldsymbol{\alpha}_{1}+x_{2}\boldsymbol{\alpha}_{2}+x_{3}\boldsymbol{\alpha}_{3}$ 的等价方",
    r"程组为 $\begin{cases}x_{1}=3-2x_{3},\\ x_{2}=-2+x_{3},\end{cases}$ "
    r"得通解为 $\boldsymbol{x}=k\begin{pmatrix}-2\\ 1\\ 1\end{pmatrix}+\begin{pmatrix}3\\ -2\\ 0\end{pmatrix}$"
    r"（$k$ 为任意常数），",
    r"从而 $\boldsymbol{\beta}_{3}=(3-2k)\boldsymbol{\alpha}_{1}+(k-2)\boldsymbol{\alpha}_{2}+k\boldsymbol{\alpha}_{3}$"
    r"（$k$ 为任意常数）；",
    r"(II) 当 $a\neq\pm1$ 时，$(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3},\boldsymbol{\beta}_{3})"
    r"\to\begin{pmatrix}1&0&0&1\\ 0&1&0&-1\\ 0&0&1&1\end{pmatrix}$，得 $\boldsymbol{x}=\begin{pmatrix}1\\ -1\\ 1\end{pmatrix}$，",
    r"所以 $\boldsymbol{\beta}_{3}=\boldsymbol{\alpha}_{1}-\boldsymbol{\alpha}_{2}+\boldsymbol{\alpha}_{3}$",
])

A[21] = (r"(I)\ x=3,\ y=-2;\ (II)\ P=P_{1}P_{2}^{-1}=\begin{pmatrix}1&-\dfrac{1}{3}&1\\ -2&-\dfrac{1}{3}&-2\\ 0&0&-4\end{pmatrix}", [
    r"【解析】(I) 方法一：相似矩阵有相同的行列式值和迹，因此有 $\begin{cases}-2+x-2=2-1+y\\ |A|=|B|\end{cases}$，",
    r"又 $|A|=-2(4-2x)$，$|B|=-2y$，所以 $x=3,y=-2$.",
    r"方法二：观察得 $A$ 必有一个特征值为 $-2$，$B$ 的特征值为 $2,-1,y$，因此由 $A$，$B$ 相似得",
    r"两个矩阵特征值相等得 $y=-2$，再由 $-2+x-2=2-1+y$，得 $x=3$",
    r"(II) 易知 $B$ 的特征值为 $2,-1,-2$；因此",
    r"$A-2E\xrightarrow{r}\begin{pmatrix}2&1&0\\ 0&0&1\\ 0&0&0\end{pmatrix}$，取 $\boldsymbol{\xi}_{1}=(1,-2,0)^{\mathrm{T}}$，",
    r"$A+E\xrightarrow{r}\begin{pmatrix}1&2&0\\ 0&0&1\\ 0&0&0\end{pmatrix}$，取 $\boldsymbol{\xi}_{2}=(-2,1,0)^{\mathrm{T}}$，",
    r"$A+2E\xrightarrow{r}\begin{pmatrix}4&0&1\\ 0&2&-1\\ 0&0&0\end{pmatrix}$，取 $\boldsymbol{\xi}_{3}=(1,-2,-4)^{\mathrm{T}}$",
    r"令 $P_{1}=\begin{pmatrix}1&-2&1\\ -2&1&-2\\ 0&0&-4\end{pmatrix}$，则有 $P_{1}^{-1}AP_{1}=\begin{pmatrix}2&0&0\\ 0&-1&0\\ 0&0&-2\end{pmatrix}$；",
    r"同理可得，对于矩阵 $B$，有矩阵 $P_{2}=\begin{pmatrix}1&-1&0\\ 0&3&0\\ 0&0&1\end{pmatrix}$，"
    r"$P_{2}^{-1}BP_{2}=\begin{pmatrix}2&0&0\\ 0&-1&0\\ 0&0&-2\end{pmatrix}$，所以",
    r"$P_{1}^{-1}AP_{1}=P_{2}^{-1}BP_{2}$，即 $B=P_{2}P_{1}^{-1}AP_{1}P_{2}^{-1}$，所以",
    r"令 $P=P_{1}P_{2}^{-1}=\begin{pmatrix}1&-\dfrac{1}{3}&1\\ -2&-\dfrac{1}{3}&-2\\ 0&0&-4\end{pmatrix}$",
])

A[22] = (r"(I)\ f_{Z}(z)=\begin{cases}pe^{z},&z<0\\ (1-p)e^{-z},&z\geqslant0\end{cases};\ (II)\ p=\dfrac{1}{2};\ (III)\ 不独立", [
    r"【解析】(I) $Z$ 的分布函数为",
    r"$F_{Z}(z)=P(Z\leqslant z)=P(XY\leqslant z)=P(X\geqslant-z)P(Y=-1)+P(X\leqslant z)P(Y=1)$",
    r"因为 $X$ 与 $Y$ 相互独立，且 $X$ 的分布函数为 $F_{X}(x)=\begin{cases}1-e^{-x},&x>0,\\ 0,&x\leqslant0.\end{cases}$",
    r"因此，$F_{Z}(z)=p[1-F_{X}(-z)]+(1-p)F_{X}(z)=\begin{cases}pe^{z},&z<0,\\ p+(1-p)(1-e^{-z}),&z\geqslant0.\end{cases}$",
    r"所以，$Z$ 的概率密度为 $f_{Z}(z)=F'_{Z}(z)=\begin{cases}pe^{z},&z<0,\\ (1-p)e^{-z},&z\geqslant0.\end{cases}$",
    r"(II) 当 $Cov(X,Z)=EXZ-EX\cdot EZ=EX^{2}\cdot EY-(EX)^{2}\cdot EY=DX\cdot EY=0$ 时，$X$ 与 $Z$",
    r"不相关.因为 $DX=1$，$EY=1-2p$，故 $p=\dfrac{1}{2}$.",
    r"(III) 不独立.",
    r"因为 $P(X\leqslant1,Z\leqslant-1)=P(X\leqslant1,XY\leqslant-1)=0,P(X\leqslant1)>0,P(Z\leqslant-1)>0$，",
    r"所以 $P(X\leqslant1,Z\leqslant1)\neq P(X\leqslant1)P(Z\leqslant-1)$，",
    r"所以 $X$ 与 $Z$ 不独立.",
])

A[23] = (r"(I)\ A=\sqrt{\dfrac{2}{\pi}};\ (II)\ \hat{\sigma}^{2}=\dfrac{1}{n}\sum\limits_{i=1}^{n}(X_{i}-\mu)^{2}", [
    r"【解析】(I) 由密度函数的规范性可知 $\displaystyle\int_{-\infty}^{+\infty}f(x)\mathrm{d}x=1$，即",
    r"$\displaystyle\int_{\mu}^{+\infty}\dfrac{A}{\sigma}e^{-\frac{(x-\mu)^{2}}{2\sigma^{2}}}\mathrm{d}x"
    r"=\dfrac{A}{\sigma}\int_{0}^{+\infty}e^{-\frac{t^{2}}{2\sigma^{2}}}\mathrm{d}t"
    r"=\dfrac{\sqrt{2\pi}A}{2}\int_{-\infty}^{+\infty}\dfrac{1}{\sqrt{2\pi}\sigma}e^{-\frac{t^{2}}{2\sigma^{2}}}\mathrm{d}t"
    r"=A\sqrt{\dfrac{\pi}{2}}=1$，",
    r"得 $A=\sqrt{\dfrac{2}{\pi}}$.",
    r"(II) 设似然函数",
    r"$L(\sigma^{2})=\displaystyle\prod_{i=1}^{n}f(x_{i},\sigma^{2})=\begin{cases}\Bigl(\dfrac{2}{\pi}\Bigr)^{\frac{n}{2}}\cdot\sigma^{-n}"
    r"\cdot e^{-\frac{1}{2\sigma^{2}}\sum\limits_{i=1}^{n}(x_{i}-\mu)^{2}},&x_{i}\geqslant\mu\\ 0,&\text{其他}\end{cases}$",
    r"取对数，$\ln L(\sigma^{2})=\dfrac{n}{2}\ln\Bigl(\dfrac{2}{\pi}\Bigr)-\dfrac{n}{2}\ln\sigma^{2}"
    r"-\dfrac{1}{2\sigma^{2}}\displaystyle\sum_{i=1}^{n}(x_{i}-\mu)^{2}$；",
    r"对 $\sigma^{2}$ 求导，$\dfrac{\mathrm{d}\ln L(\sigma^{2})}{\mathrm{d}\sigma^{2}}=-\dfrac{n}{2\sigma^{2}}"
    r"+\dfrac{\sum\limits_{i=1}^{n}(x_{i}-\mu)^{2}}{2\sigma^{4}}$，",
    r"令导数为零，解得 $\sigma^{2}=\dfrac{1}{n}\displaystyle\sum_{i=1}^{n}(x_{i}-\mu)^{2}$，",
    r"故 $\sigma^{2}$ 的最大似然估计量为 $\hat{\sigma}^{2}=\dfrac{1}{n}\displaystyle\sum_{i=1}^{n}(X_{i}-\mu)^{2}$.",
])
