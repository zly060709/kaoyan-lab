# -*- coding: utf-8 -*-
"""2021 数学三 解析 解答题 17-22（原卷 p10-p12，逐字照录）"""

A = {}

A[17] = (r"\alpha=\dfrac{e^{-1}-e}{\pi}", [
    r"【解析】$\lim\limits_{x\to0^{+}}\bigl[a\arctan\dfrac{1}{x}+(1+x)^{\frac{1}{x}}\bigr]=\dfrac{\pi}{2}a+\mathrm{e}$；",
    r"$\lim\limits_{x\to0^{-}}\bigl[a\arctan\dfrac{1}{x}+(1-x)^{\frac{1}{x}}\bigr]=-\dfrac{\pi}{2}a+\mathrm{e}^{-1}$；",
    r"则其左极限等于右极限：$\dfrac{\pi}{2}a+\mathrm{e}=-\dfrac{\pi}{2}a+\mathrm{e}^{-1}$，解得 $a=\dfrac{\mathrm{e}^{-1}-\mathrm{e}}{\pi}$.",
])

A[18] = ("f(-1,0)=2 与 f(1/2,0)=1/2-2ln2 均为极小值", [
    r"【解析】令 $\begin{cases}f_{x}'(x,y)=\dfrac{2x^{2}+x-1-y^{2}}{x^{3}}=0,\\ f_{y}'(x,y)=\dfrac{y}{x^{2}}=0,\end{cases}$ "
    r"得驻点 $(-1,0)$ 和 $\left(\dfrac{1}{2},0\right)$.",
    r"$\begin{cases}f_{xx}''(x,y)=\dfrac{-2x^{2}-2x+3+3y^{2}}{x^{4}},\\ f_{yx}''(x,y)=-\dfrac{2y}{x^{3}},\\ "
    r"f_{yy}''(x,y)=\dfrac{1}{x^{2}},\end{cases}$",
    r"在 $(-1,0)$ 处，$A=3>0,B=0,C=1>0,AC-B^{2}>0$，所以有极小值 $f(-1,0)=2$；",
    r"在 $\left(\dfrac{1}{2},0\right)$ 处，$A=24>0,B=0,C=4>0,AC-B^{2}>0$,"
    r"所以有极小值 $f\left(\dfrac{1}{2},0\right)=\dfrac{1}{2}-2\ln2$.",
])

A[19] = (r"\dfrac{1}{8}(e-1)^{2}", [
    r"【解析】$\displaystyle\iint\limits_{D}e^{(x+y)^{2}}(x^{2}-y^{2})\mathrm{d}x\mathrm{d}y"
    r"=\int_{0}^{\frac{\pi}{4}}d\theta\int_{0}^{1}e^{r^{2}+2r^{2}\cos\theta\sin\theta}"
    r"(r^{2}\cos^{2}\theta-r^{2}\sin^{2}\theta)rdr$",
    r"$=\displaystyle\int_{0}^{1}dr\int_{0}^{\frac{\pi}{4}}e^{r^{2}(1+\sin2\theta)}r^{3}\cos2\theta d\theta$"
    r"$\qquad=\displaystyle\int_{0}^{1}\dfrac{r}{2}e^{r^{2}(1+\sin2\theta)}\Big|_{0}^{\frac{\pi}{4}}dr"
    r"=\dfrac{1}{2}\int_{0}^{1}r(e^{2r^{2}}-e^{r^{2}})dr$",
    r"$=\dfrac{1}{2}\Bigl(\dfrac{1}{4}e^{2r^{2}}-\dfrac{1}{2}e^{r^{2}}\Bigr)\Big|_{0}^{1}=\dfrac{1}{8}(e-1)^{2}$",
])

A[20] = (r"(I)\ y_{n}(x)=\dfrac{x^{n+1}}{n(n+1)};\ (II)\ [-1,1],\ "
         r"S(x)=x+(1-x)\ln(1-x)\ (-1\leqslant x<1),\ S(1)=1", [
    r"【解析】（I）$xy'-(n+1)y=0$,化简得 $\dfrac{dy}{y}=(n+1)\dfrac{dx}{x}$，两边积分，得",
    r"$\ln|y|=(n+1)\ln|x|+C_{0}$，化简得 $y=Cx^{n+1}$.",
    r"因为 $y_{n}(1)=\dfrac{1}{n(n+1)}$,所以 $C=\dfrac{1}{n(n+1)}$,所以 $y_{n}(x)=\dfrac{1}{n(n+1)}x^{n+1}$.",
    r"（II）令 $\lim\limits_{n\to\infty}\left|\dfrac{\dfrac{1}{(n+1)(n+2)}x^{n+2}}{\dfrac{1}{n(n+1)}x^{n+1}}\right|<1$，"
    r"得 $-1<x<1$.",
    r"$x=1$ 时，$\sum\limits_{n=1}^{\infty}\dfrac{1}{n(n+1)}$ 收敛；$x=-1$ 时，"
    r"$\sum\limits_{n=1}^{\infty}\dfrac{(-1)^{n+1}}{n(n+1)}$ 收敛；收敛域为 $[-1,1]$.",
    r"$S(x)=\displaystyle\sum_{n=1}^{\infty}\dfrac{x^{n+1}}{n(n+1)}=x\sum_{n=1}^{\infty}\dfrac{x^{n}}{n}-\sum_{n=1}^{\infty}\dfrac{x^{n+1}}{n+1}$",
    r"$=x\displaystyle\int_{0}^{x}\Bigl(\sum_{n=1}^{\infty}\dfrac{x^{n}}{n}\Bigr)'dx-\int_{0}^{x}\Bigl(\sum_{n=1}^{\infty}\dfrac{x^{n+1}}{n+1}\Bigr)'dx$",
    r"$=x\displaystyle\int_{0}^{x}\dfrac{1}{1-x}dx-\int_{0}^{x}\dfrac{x}{1-x}dx$",
    r"$=(1-x)\ln(1-x)+x$ $\qquad x\in[-1,1)$. ",
    r"$S(1)=\lim\limits_{x\to1^{-}}[(1-x)\ln(1-x)+x]=1$，",
    r"所以 $S(x)=\begin{cases}x+(1-x)\ln(1-x),&-1\leqslant x<1\\ 1,&x=1\end{cases}$. ",
])

A[21] = (r"(I)\ a=b=1,\ P_{1}=(a_{1},a_{2},a_{3});\ (II)\ a=-1,b=3,\ P_{2}=(\beta_{1},\beta_{2},\beta_{3})", [
    r"【解析】（I）$|\lambda E-A|=\begin{vmatrix}\lambda-2&-1&0\\ -1&\lambda-2&0\\ -1&-a&\lambda-b\end{vmatrix}$",
    r"$=(\lambda-b)\Bigl[(\lambda-2)^{2}-1\Bigr]=(\lambda-b)(\lambda-3)(\lambda-1)=0$",
    r"当 $b=1$ 时，$\lambda_{1}=\lambda_{2}=1,\lambda_{3}=3$，$A$ 相似于对角矩阵，则 $r(E-A)=1$，$a=1$.",
    r"$(E-A)=\begin{pmatrix}-1&-1&0\\ -1&-1&0\\ -1&-a&0\end{pmatrix}\to\begin{pmatrix}-1&-1&0\\ 0&0&0\\ 0&0&0\end{pmatrix}$，"
    r"$\boldsymbol{a}_{1}=\begin{pmatrix}-1\\ 1\\ 0\end{pmatrix},\boldsymbol{a}_{2}=\begin{pmatrix}0\\ 0\\ 1\end{pmatrix}$",
    r"$(3E-A)=\begin{pmatrix}1&-1&0\\ -1&1&0\\ -1&-1&2\end{pmatrix}\to\begin{pmatrix}1&1&-2\\ 0&1&-1\\ 0&0&0\end{pmatrix}$，"
    r"$\boldsymbol{a}_{3}=\begin{pmatrix}1\\ 1\\ 1\end{pmatrix}$",
    r"令可逆矩阵 $P_{1}=(\boldsymbol{a}_{1},\boldsymbol{a}_{2},\boldsymbol{a}_{3})$，使得 "
    r"$P_{1}^{-1}AP_{1}=\Lambda=\begin{pmatrix}1& &\\ &1&\\ & &3\end{pmatrix}$. ",
    r"（II）当 $b=3$ 时，$\lambda_{1}=\lambda_{2}=3,\lambda_{3}=1$，$A$ 相似于对角矩阵，则 $r(3E-A)=1$，$a=-1$",
    r"$(3E-A)=\begin{pmatrix}1&-1&0\\ -1&1&0\\ -1&-a&0\end{pmatrix}\to\begin{pmatrix}1&-1&0\\ 0&0&0\\ 0&0&0\end{pmatrix}$，"
    r"$\boldsymbol{\beta}_{1}=\begin{pmatrix}1\\ 1\\ 0\end{pmatrix},\boldsymbol{\beta}_{2}=\begin{pmatrix}0\\ 0\\ 1\end{pmatrix}$，",
    r"$(E-A)=\begin{pmatrix}-1&-1&0\\ -1&-1&0\\ -1&1&-2\end{pmatrix}\to\begin{pmatrix}1&-1&2\\ 0&1&-1\\ 0&0&0\end{pmatrix}$，"
    r"$\boldsymbol{\beta}_{3}=\begin{pmatrix}-1\\ 1\\ 1\end{pmatrix}$，",
    r"令可逆矩阵 $P_{2}=(\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3})$，使得 "
    r"$P_{2}^{-1}AP_{2}=\Lambda=\begin{pmatrix}3& &\\ &3&\\ & &1\end{pmatrix}$. ",
])

A[22] = (r"(I)\ f_{X}(x)=1\ (0<x<1);\ (II)\ f_{Z}(z)=\dfrac{2}{(z+1)^{2}}\ (z\geqslant1);\ "
         r"(III)\ E(X/Y)=2\ln 2-1", [
    r"【解析】易知 $X+Y=2,Y>X>0$，且 $X$ 在 $(0,1)$ 上服从均匀分布;",
    r"（I）$X$ 的概率密度 $f_{X}(x)=\begin{cases}1,&0<x<1\\ 0,&\text{其他}\end{cases}$. ",
    r"（II）$Z$ 的分布函数 $F_{Z}(z)=P\{Z\leqslant z\}=P\left\{\dfrac{2-X}{X}\leqslant z\right\}$；",
    r"$z<1$ 时，$F_{Z}(z)=0$；$z\geqslant1$ 时，$F_{Z}(z)=\displaystyle\int_{\frac{2}{z+1}}^{1}1dx=1-\dfrac{2}{z+1}$；",
    r"$Z$ 的概率密度为 $f_{Z}(z)=\begin{cases}\dfrac{2}{(z+1)^{2}},&z\geqslant1\\ 0,&z<1\end{cases}$. ",
    r"（III）$E\Bigl(\dfrac{X}{Y}\Bigr)=E\Bigl(\dfrac{X}{2-X}\Bigr)=\displaystyle\int_{0}^{1}\dfrac{x}{2-x}dx"
    r"=\int_{0}^{1}\Bigl(\dfrac{2}{2-x}-1\Bigr)dx$",
    r"$=-2\ln|2-x|\Big|_{0}^{1}-1=2\ln2-1$. ",
])
