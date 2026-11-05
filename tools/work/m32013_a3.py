# -*- coding: utf-8 -*-
"""2013 数学三 解析 解答题 15-23（原卷 p9-p12，逐字照录；解答题原卷无【答案】行，直接【解析】）"""

A = {}

A[15] = ("a=7, n=2", [
    r"【解析】",
    r"利用泰勒公式有：",
    r"$\cos x=1-\dfrac{1}{2}x^{2}+o(x^{2})$，",
    r"$\cos 2x=1-\dfrac{1}{2}(2x)^{2}+o(x^{2})=1-2x^{2}+o(x^{2})$，",
    r"$\cos 3x=1-\dfrac{1}{2}(3x)^{2}+o(x^{2})=1-\dfrac{9}{2}x^{2}+o(x^{2})$，",
    r"所以",
    r"$1-\cos x\cdot\cos 2x\cdot\cos 3x"
    r"=1-\Bigl[1-\dfrac{1}{2}x^{2}+o(x^{2})\Bigr]\cdot\Bigl[1-2x^{2}+o(x^{2})\Bigr]\cdot\Bigl[1-\dfrac{9}{2}x^{2}+o(x^{2})\Bigr]$",
    r"$=1-\Bigl[1-\dfrac{1}{2}x^{2}-2x^{2}-\dfrac{9}{2}x^{2}+o(x^{2})\Bigr]=7x^{2}+o(x^{2})$",
    r"可得，当 $x\to0$ 时，$1-\cos x\cdot\cos 2x\cdot\cos 3x\sim7x^{2}$，所以有 $a=7,n=2$.",
])

A[16] = (r"a=7\sqrt{7}", [
    r"【解析】",
    r"由旋转体的体积公式：$V_{x}=\pi\displaystyle\int_{a}^{b}[f(x)]^{2}dx$，得 $D$ 绕 $x$ 轴旋转体的体积",
    r"$V_{x}=\pi\displaystyle\int_{0}^{a}\bigl(x^{\frac{1}{3}}\bigr)^{2}dx=\dfrac{3\pi}{5}a^{\frac{5}{3}}$，",
    r"又因为 $D$ 绕 $y$ 轴旋转体的体积，可以由整个圆柱体体积减去 $D_{1}$ 绕 $y$ 轴旋转体的体积得到，",
    r"其中 $D_{1}$ 是由 $x=y^{3},y=a^{\frac{1}{3}},x=0$ 所围成.",
    r"所以 $V_{y}=\pi a^{2}a^{\frac{1}{3}}-\pi\displaystyle\int_{0}^{a^{\frac{1}{3}}}\bigl(y^{3}\bigr)^{2}dy=\dfrac{6\pi}{7}a^{\frac{7}{3}}$，"
    r"又由 $V_{y}=10V_{x}$，所以 $\dfrac{6\pi}{7}a^{\frac{7}{3}}=10\dfrac{3\pi}{5}a^{\frac{5}{3}}$，",
    r"所以 $a=7\sqrt{7}$.",
])

A[17] = (r"\dfrac{416}{3}", [
    r"【解析】",
    r"由于区域 $D$ 为非 $X$ 非 $Y$ 型区域，将其分成两个 $X$ 型区域 $D_{1},D_{2}$，所以",
    r"$\displaystyle\iint\limits_{D}x^{2}dxdy=\iint\limits_{D_{1}}x^{2}dxdy+\iint\limits_{D_{2}}x^{2}dxdy$，",
    r"而 $\displaystyle\iint\limits_{D_{2}}x^{2}dxdy=\int_{2}^{6}dx\int_{\frac{x}{3}}^{8-x}x^{2}dy=128$,"
    r"所以 $\displaystyle\iint\limits_{D}x^{2}dxdy=\dfrac{416}{3}$.",
])

A[18] = (r"(I)\ -\dfrac{Q}{500}+40;\ (II)\ 20;\ (III)\ P=40", [
    r"【解析】设利润为 $f(Q)$,则 $f(Q)=PQ-(20Q+6000)=-\dfrac{Q^{2}}{1000}+40Q-6000$",
    r"（I）边际利润为 $f'=-\dfrac{Q}{500}+40$；",
    r"（II）当 $P=50$ 时 $Q=10000$，此时的边际利润为 $f'(10000)=20$；"
    r"其经济意义：此时销量每增加一个，利润就会增加20；",
    r"（III）令 $f'=-\dfrac{Q}{500}+40=0$ 得 $Q=20000$，此时 $P=40$.",
])

A[19] = ("证明见解析", [
    r"【解析】",
    r"（I）因 $\lim\limits_{x\to+\infty}f(x)=2$，由极限的保号性知，$\exists X>0$，当 $x>X$ 时 $f(x)>1$，"
    r"不防取 $x=\eta$ 满足 $x>X$，且 $f(\eta)=\dfrac{4}{3}$，则 $f(x)$ 在 $[0,\eta]$ 上连续，"
    r"由闭区间连续函数的介值定理得 $\exists a\in[0,\eta]$, 使得 $f(a)=1$，"
    r"又因为 $f(0)=0$，所以 $\exists a>0$, 使得 $f(a)=1$.",
    r"（II）构造辅助函数 $F(x)=f(x)-\dfrac{1}{a}x$，则 $F(0)=0$，$F(a)=0$，又 $F(x)$ 在 $[0,a]$ 可导，",
    r"由罗尔定理知，$\exists\xi\in(0,a)$，使得 $F'(\xi)=f'(\xi)-\dfrac{1}{a}=0$，即 $f'(\xi)=\dfrac{1}{a}$.",
])

A[20] = (r"a=-1,\ b=0;\ C=\begin{pmatrix}c_{1}+c_{2}+1&-c_{1}\\ c_{1}&c_{2}\end{pmatrix}", [
    r"【解析】设矩阵 $C=\begin{pmatrix}x_{1}&x_{2}\\ x_{3}&x_{4}\end{pmatrix}$，则",
    r"$AC=\begin{pmatrix}1&a\\ 1&0\end{pmatrix}\begin{pmatrix}x_{1}&x_{2}\\ x_{3}&x_{4}\end{pmatrix}"
    r"=\begin{pmatrix}x_{1}+ax_{3}&x_{2}+ax_{4}\\ x_{1}&x_{2}\end{pmatrix}$",
    r"$CA=\begin{pmatrix}x_{1}&x_{2}\\ x_{3}&x_{4}\end{pmatrix}\begin{pmatrix}1&a\\ 1&0\end{pmatrix}"
    r"=\begin{pmatrix}x_{1}+x_{2}&ax_{1}\\ x_{3}+x_{4}&ax_{3}\end{pmatrix}$",
    r"$AC-CA=\begin{pmatrix}x_{1}+ax_{3}&x_{2}+ax_{4}\\ x_{1}&x_{2}\end{pmatrix}"
    r"-\begin{pmatrix}x_{1}+x_{2}&ax_{1}\\ x_{3}+x_{4}&ax_{3}\end{pmatrix}"
    r"=\begin{pmatrix}-x_{2}+ax_{3}&-ax_{1}+x_{2}+ax_{4}\\ x_{1}-x_{3}-x_{4}&x_{2}-ax_{3}\end{pmatrix}$",
    r"由 $AC-CA=B$，得",
    r"$\begin{cases}-x_{2}+ax_{3}=0\\ -ax_{1}+x_{2}+ax_{4}=1\\ x_{1}-x_{3}-x_{4}=1\\ x_{2}-ax_{3}=b\end{cases}$",
    r"此为 4 元非齐次线性方程组，欲使得矩阵 $C$ 存在，则此非齐次线性方程组必有解，从而增广矩阵",
    r"$\overline{A}=\begin{pmatrix}0&-1&a&0&0\\ -a&1&0&a&1\\ 1&0&-1&-1&1\\ 0&1&-a&0&b\end{pmatrix}"
    r"\to\begin{pmatrix}1&0&-1&-1&1\\ 0&1&-a&0&0\\ 0&0&0&0&b\\ 0&0&0&0&1+a\end{pmatrix}$",
    r"所以当 $1+a=0,b=0$，即 $a=-1,b=0$ 时，非齐次线性方程组有解，存在矩阵 $C$，使得 $AC-CA=B$.",
    r"又 $\overline{A}\to\begin{pmatrix}1&0&-1&-1&1\\ 0&1&1&0&0\\ 0&0&0&0&0\\ 0&0&0&0&0\end{pmatrix}$",
    r"所以",
    r"$X=\begin{pmatrix}x_{1}\\ x_{2}\\ x_{3}\\ x_{4}\end{pmatrix}"
    r"=c_{1}\begin{pmatrix}1\\ -1\\ 1\\ 0\end{pmatrix}+c_{2}\begin{pmatrix}1\\ 0\\ 0\\ 1\end{pmatrix}"
    r"+\begin{pmatrix}1\\ 0\\ 0\\ 0\end{pmatrix}=\begin{pmatrix}c_{1}+c_{2}+1\\ -c_{1}\\ c_{1}\\ c_{2}\end{pmatrix}$",
    r"所以",
    r"$C=\begin{pmatrix}c_{1}+c_{2}+1&-c_{1}\\ c_{1}&c_{2}\end{pmatrix}$($c_{1},c_{2}$为任意实数）.",
])

A[21] = (r"(I)\ A=2\alpha\alpha^{T}+\beta\beta^{T};\ (II)\ 2y_{1}^{2}+y_{2}^{2}", [
    r"【解析】（I）证明：",
    r"$f(x_{1},x_{2},x_{3})=2\bigl(a_{1}x_{1}+a_{2}x_{2}+a_{3}x_{3}\bigr)^{2}"
    r"+\bigl(b_{1}x_{1}+b_{2}x_{2}+b_{3}x_{3}\bigr)^{2}$",
    r"$=2\Biggl[\bigl(x_{1},x_{2},x_{3}\bigr)\begin{pmatrix}a_{1}\\ a_{2}\\ a_{3}\end{pmatrix}"
    r"\bigl(a_{1},a_{2},a_{3}\bigr)\begin{pmatrix}x_{1}\\ x_{2}\\ x_{3}\end{pmatrix}\Biggr]"
    r"+\Biggl[\bigl(x_{1},x_{2},x_{3}\bigr)\begin{pmatrix}b_{1}\\ b_{2}\\ b_{3}\end{pmatrix}"
    r"\bigl(b_{1},b_{2},b_{3}\bigr)\begin{pmatrix}x_{1}\\ x_{2}\\ x_{3}\end{pmatrix}\Biggr]$",
    r"$=X^{T}\bigl(2\boldsymbol{\alpha}\boldsymbol{\alpha}^{T}\bigr)X+X^{T}\bigl(\boldsymbol{\beta}\boldsymbol{\beta}^{T}\bigr)X$",
    r"$=X^{T}\bigl(2\boldsymbol{\alpha}\boldsymbol{\alpha}^{T}+\boldsymbol{\beta}\boldsymbol{\beta}^{T}\bigr)X$",
    r"又 $2\boldsymbol{\alpha}\boldsymbol{\alpha}^{T}+\boldsymbol{\beta}\boldsymbol{\beta}^{T}$ 为实对称矩阵，"
    r"故二次型 $f$ 对应的矩阵 $A=2\boldsymbol{\alpha}\boldsymbol{\alpha}^{T}+\boldsymbol{\beta}\boldsymbol{\beta}^{T}$",
    r"（II）因为 $\boldsymbol{\alpha},\boldsymbol{\beta}$ 正交且都为单位向量，"
    r"即 $\boldsymbol{\beta}^{T}\boldsymbol{\alpha}=0,\boldsymbol{\alpha}^{T}\boldsymbol{\beta}=0,"
    r"\boldsymbol{\alpha}^{T}\boldsymbol{\alpha}=1,\boldsymbol{\beta}^{T}\boldsymbol{\beta}=1$",
    r"故 $A\boldsymbol{\alpha}=\bigl(2\boldsymbol{\alpha}\boldsymbol{\alpha}^{T}+\boldsymbol{\beta}\boldsymbol{\beta}^{T}\bigr)\boldsymbol{\alpha}=2\boldsymbol{\alpha}$，"
    r"从而矩阵 $A$ 的其中一个特征值为 $\lambda_{1}=2$，",
    r"同理可得 $A\boldsymbol{\beta}=\bigl(2\boldsymbol{\alpha}\boldsymbol{\alpha}^{T}+\boldsymbol{\beta}\boldsymbol{\beta}^{T}\bigr)\boldsymbol{\beta}=\boldsymbol{\beta}$，"
    r"即矩阵 $A$ 的其中一个特征值为 $\lambda_{2}=1$，",
    r"又因为 $r\bigl(\boldsymbol{\alpha}\boldsymbol{\alpha}^{T}\bigr)=1,r\bigl(\boldsymbol{\beta}\boldsymbol{\beta}^{T}\bigr)=1$，"
    r"所以 $r(A)=r\bigl(2\boldsymbol{\alpha}\boldsymbol{\alpha}^{T}+\boldsymbol{\beta}\boldsymbol{\beta}^{T}\bigr)\leqslant2$.",
    r"从而矩阵 $A$ 的其中一个特征值为 $\lambda_{3}=0$,二次型 $f$ 经正交变换后的标准形为 $2y_{1}^{2}+y_{2}^{2}$.",
])

A[22] = (r"(I)\ f(x,y)=9y^{2}/x\ (0<y<x<1);\ (II)\ f_{Y}(y)=-9y^{2}\ln y\ (0<y<1);\ (III)\ 1/8", [
    r"【解析】（I）$\bigl(X,Y\bigr)$ 的概率密度为 "
    r"$f(x,y)=f_{X}(x)f_{Y|X}(y|x)=\begin{cases}\dfrac{9y^{2}}{x},&0<y<x<1\\ 0,&\text{其他}\end{cases}$",
    r"（II）根据 $f_{Y}(y)=\displaystyle\int_{-\infty}^{+\infty}f(x,y)dx$，可以求得",
    r"$f_{Y}(y)=\begin{cases}-9y^{2}\ln y,&0<y<1\\ 0,&\text{其他}\end{cases}$",
    r"（III）",
    r"$P\{X>2Y\}=\displaystyle\iint\limits_{x>2y}f(x,y)dxdy"
    r"=\iint\limits_{\substack{x>2y\\ 0<y<x<1}}\dfrac{9y^{2}}{x}dxdy"
    r"=\int_{0}^{1}dx\int_{0}^{\frac{x}{2}}\dfrac{9y^{2}}{x}dy=\dfrac{1}{8}$.",
])

A[23] = (r"(I)\ \bar{X};\ (II)\ \dfrac{2n}{\sum\limits_{i=1}^{n}\dfrac{1}{X_{i}}}", [
    r"【解析】（I）令 $EX=\displaystyle\int_{-\infty}^{+\infty}xf(x;\theta)dx"
    r"=\int_{0}^{+\infty}\dfrac{\theta^{2}}{x^{2}}e^{-\frac{\theta}{x}}dx=\theta=\overline{X}$，"
    r"$\theta$ 矩估计量为 $\overline{X}$.",
    r"（II）似然函数",
    r"$L((\theta)=\displaystyle\prod_{i=1}^{n}f(x_{i};\theta)"
    r"=\begin{cases}\dfrac{\theta^{2n}}{\bigl(x_{1}x_{2}...x_{n}\bigr)^{3}}e^{-\theta\sum\limits_{i=1}^{n}\frac{1}{x_{i}}},&x_{i}>0\\ 0,&\text{else}\end{cases}$",
    r"当 $x_{i}>0$,令 $\dfrac{d\ln L(\theta)}{d\theta}=0$,得 $\theta=\dfrac{2n}{\sum\limits_{i=1}^{n}\dfrac{1}{x_{i}}}$,"
    r"所以 $\theta$ 得最大似然估计量为 $\dfrac{2n}{\sum\limits_{i=1}^{n}\dfrac{1}{X_{i}}}$.",
])
