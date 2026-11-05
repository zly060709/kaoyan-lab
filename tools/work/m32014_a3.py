# -*- coding: utf-8 -*-
"""2014 数学三 解析 解答题 15-23（原卷 p8-p13，逐字照录）"""

A = {}

A[15] = (r"\dfrac{1}{2}", [
    r"【答案】$\dfrac{1}{2}$",
    r"【解析】",
    r"$\lim\limits_{x\to+\infty}\dfrac{\displaystyle\int_{1}^{x}[t^{2}(e^{\frac{1}{t}}-1)-t]dt}"
    r"{x^{2}\ln(1+\dfrac{1}{x})}=\lim\limits_{x\to+\infty}\dfrac{\displaystyle\int_{1}^{x}[t^{2}(e^{\frac{1}{t}}-1)-t]dt}{x}"
    r"=\lim\limits_{x\to+\infty}\Bigl[x^{2}(e^{\frac{1}{x}}-1)-x\Bigr]$，令 $t=\dfrac{1}{x}$",
    r"$=\lim\limits_{t\to0^{+}}\Bigl[\left(\dfrac{1}{t}\right)^{2}(e^{t}-1)-\dfrac{1}{t}\Bigr]"
    r"=\lim\limits_{t\to0^{+}}\Bigl[\dfrac{(e^{t}-1)-t}{t^{2}}\Bigr]=\dfrac{1}{2}$.",
])

A[16] = (r"-\dfrac{3}{4}", [
    r"【答案】$-\dfrac{3}{4}$",
    r"【解析】由轮换对称性得，",
    r"$\displaystyle\iint\limits_{D}\dfrac{x\sin(\pi\sqrt{x^{2}+y^{2}})}{x+y}dxdy"
    r"=\dfrac{1}{2}\iint\limits_{D}\sin\left(\pi\sqrt{x^{2}+y^{2}}\right)dxdy"
    r"=\dfrac{1}{2}\int_{0}^{\frac{\pi}{2}}d\theta\int_{1}^{2}\sin\left(\pi r\right)rdr=-\dfrac{3}{4}$.",
])

A[17] = (r"f(u)=\dfrac{1}{16}(e^{4u}-4u-1)", [
    r"【答案】$f(u)=\dfrac{1}{16}(e^{4u}-4u-1)$.",
    r"【解析】由于 $\dfrac{\partial z}{\partial x}=f'(e^{x}\cos y)e^{x}\cos y$，"
    r"$\dfrac{\partial z}{\partial y}=-f'(e^{x}\cos y)e^{x}\sin y$，",
    r"所以",
    r"$\cos y\dfrac{\partial z}{\partial x}-\sin y\dfrac{\partial z}{\partial y}"
    r"=f'(e^{x}\cos y)e^{x}\cos^{2}y+f'(e^{x}\cos y)e^{x}\sin^{2}y$",
    r"$=f'(e^{x}\cos y)e^{x}=(4z+e^{x}\cos y)e^{x}$",
    r"即 $f'(e^{x}\cos y)e^{x}=[4f(e^{x}\cos y)+e^{x}\cos y]e^{x}$，",
    r"所以 $f'(e^{x}\cos y)=4f(e^{x}\cos y)+e^{x}\cos y$.",
    r"所以 $f'(u)=4f(u)+u$，对应的微分方程为 $y'-4y=x$，为一阶线性微分方程，",
    r"$y=e^{\int4dx}\left(\int xe^{-\int4dx}dx+C\right)$，计算得 "
    r"$y=e^{4x}\left(\int xe^{-4x}dx+C\right)=-\dfrac{1}{16}(4x+1)+Ce^{4x}$，又由",
    r"$f(0)=0$ 得 $C=\dfrac{1}{16}$，所以 $y=\dfrac{1}{16}(e^{4x}-4x-1)$，得 $f(u)=\dfrac{1}{16}(e^{4u}-4u-1)$.",
])

A[18] = (r"S(x)=\dfrac{3-x}{(1-x)^{3}},x\in(-1,1)", [
    r"【答案】$S(x)=\dfrac{3-x}{(1-x)^{3}},x\in(-1,1)$",
    r"【解析】$\displaystyle\sum\limits_{n=0}^{\infty}(n+1)(n+3)x^{n}$ 收敛域为 $(-1,1)$. 设和函数为 $S(x)$，则",
    r"$S(x)=\left(\displaystyle\sum\limits_{n=0}^{\infty}(n+3)x^{n+1}\right)'$",
    r"$=\left(\dfrac{1}{x}\displaystyle\sum\limits_{n=0}^{\infty}(n+3)x^{n+2}\right)'"
    r"=\left(\dfrac{1}{x}\left(\displaystyle\sum\limits_{n=0}^{\infty}x^{n+3}\right)'\right)'"
    r"=\left(\dfrac{1}{x}\left(\dfrac{x^{3}}{1-x}\right)'\right)'$",
    r"$=\dfrac{3-x}{(1-x)^{3}}$",
    r"则 $S(x)=\dfrac{3-x}{(1-x)^{3}},x\in(-1,1)$.",
])

A[19] = ("证明见解析", [
    r"【解析】",
    r"（1）由 $g(x)$ 在闭区间 $[0,1]$ 上连续，且 $0\leqslant g(x)\leqslant1$，由积分的性质可得",
    r"$\displaystyle\int_{a}^{x}0dt\leqslant\int_{a}^{x}g(t)dt\leqslant\int_{a}^{x}1dt$.",
    r"所以",
    r"$0\leqslant\displaystyle\int_{a}^{x}g(t)dt\leqslant x-a$；",
    r"（2）令 $F(t)=\displaystyle\int_{a}^{a+\int_{a}^{t}g(x)dx}f(x)dx-\int_{a}^{t}f(x)g(x)dx$ 则 $F(a)=0$，",
    r"$F'(t)=f\left(\displaystyle\int_{a}^{t}g(x)dx\right)g(t)-f(t)g(t)$，",
    r"由 $f(x)$ 在区间 $[0,1]$ 单调增，且 $0\leqslant g(x)\leqslant1$，可得",
    r"$F'(t)=f\left(a+\displaystyle\int_{a}^{t}g(x)dx\right)g(t)-f(t)g(t)\leqslant f(a+t-a)g(t)-f(t)g(t)=0$.",
    r"所以，$F(t)$ 为减函数. 因此 $F(b)=\displaystyle\int_{a}^{a+\int_{a}^{b}g(x)dx}f(x)dx-\int_{a}^{b}f(x)g(x)dx\leqslant F(a)=0$.",
    r"即 $\displaystyle\int_{a}^{a+\int_{a}^{b}g(t)dt}f(x)dx\leqslant\int_{a}^{b}f(x)g(x)dx$.",
])

A[20] = (r"(I)\ \alpha=(-1,2,3,1)^{T};\ (II)\ B=(\alpha_{1}+k_{1}\alpha,\alpha_{2}+k_{2}\alpha,"
         r"\alpha_{3}+k_{3}\alpha),\ k_{1},k_{2},k_{3}\in R", [
    r"【详解】（I）$\boldsymbol{A}=\begin{pmatrix}1&-2&3&-4\\ 0&1&-1&1\\ 1&2&0&-3\end{pmatrix}"
    r"\to\begin{pmatrix}1&0&0&1\\ 0&1&0&-2\\ 0&0&1&-3\end{pmatrix}$.",
    r"从而同解方程组为",
    r"$\begin{cases}x_{1}=-x_{4},\\ x_{2}=2x_{4},\\ x_{3}=3x_{4}\end{cases}$",
    r"所以方程组 $\boldsymbol{Ax}=\boldsymbol{0}$ 的一个基础解系为 "
    r"$\boldsymbol{\alpha}=\begin{pmatrix}-1\\ 2\\ 3\\ 1\end{pmatrix}$.",
    r"（II）令 $\boldsymbol{\beta}_{1}=\begin{pmatrix}1\\ 0\\ 0\end{pmatrix},"
    r"\boldsymbol{\beta}_{2}=\begin{pmatrix}0\\ 1\\ 0\end{pmatrix},"
    r"\boldsymbol{\beta}_{3}=\begin{pmatrix}0\\ 0\\ 1\end{pmatrix}$，则",
    r"$(\boldsymbol{A}|\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3})"
    r"=\begin{pmatrix}1&-2&3&-4&\vdots&1&0&0\\ 0&1&-1&1&\vdots&0&1&0\\ 1&2&0&-3&\vdots&0&0&1\end{pmatrix}$",
    r"$\to\begin{pmatrix}1&0&0&1&\vdots&2&6&-1\\ 0&1&0&-2&\vdots&-1&-3&1\\ 0&0&1&-3&\vdots&-1&-4&1\end{pmatrix}$，",
    r"所以 $\boldsymbol{Ax}=\boldsymbol{\beta}_{1}$ 的一个特解为 "
    r"$\boldsymbol{\alpha}_{1}=\begin{pmatrix}2\\ -1\\ -1\\ 0\end{pmatrix}$，",
    r"$\boldsymbol{Ax}=\boldsymbol{\beta}_{2}$ 的一个特解为 "
    r"$\boldsymbol{\alpha}_{2}=\begin{pmatrix}6\\ -3\\ -4\\ 0\end{pmatrix}$，",
    r"$\boldsymbol{Ax}=\boldsymbol{\beta}_{3}$ 的一个特解为 "
    r"$\boldsymbol{\alpha}_{3}=\begin{pmatrix}-1\\ 1\\ 1\\ 0\end{pmatrix}$，",
    r"所以",
    r"$\boldsymbol{B}=\begin{pmatrix}-k_{1}+2&-k_{2}+6&-k_{3}-1\\ 2k_{1}-1&2k_{2}-3&2k_{3}+1\\ "
    r"3k_{1}-1&3k_{2}-4&3k_{3}+1\\ k_{1}&k_{2}&k_{3}\end{pmatrix},\left(k_{1},k_{2},k_{3}\in R\right)$.",
])

A[21] = ("证明见解析", [
    r"【证明】令",
    r"$\boldsymbol{A}=\begin{pmatrix}1&1&\cdots&1\\ 1&1&\cdots&1\\ \vdots&\vdots&&\vdots\\ 1&1&\cdots&1\end{pmatrix},"
    r"\boldsymbol{B}=\begin{pmatrix}0&0&\cdots&1\\ 0&0&\cdots&2\\ \vdots&\vdots&&\vdots\\ 0&0&\cdots&n\end{pmatrix}$",
    r"则",
    r"$|\lambda\boldsymbol{E}-\boldsymbol{A}|=\begin{vmatrix}\lambda-1&-1&\cdots&-1\\ -1&\lambda-1&\cdots&-1\\ "
    r"\vdots&\vdots&&\vdots\\ -1&-1&\cdots&\lambda-1\end{vmatrix}"
    r"=(\lambda-n)\begin{vmatrix}1&1&\cdots&1\\ 0&\lambda&\cdots&0\\ \vdots&\vdots&&\vdots\\ 0&0&\cdots&\lambda\end{vmatrix}"
    r"=\lambda^{n-1}(\lambda-n)=0$",
    r"$\Rightarrow\lambda_{1}=\lambda_{2}=\cdots=\lambda_{n-1}=0,\lambda_{n}=n$，",
    r"因为 $\boldsymbol{A}^{T}=\boldsymbol{A}$，即 $\boldsymbol{A}$ 为实对称矩阵，",
    r"所以 $\boldsymbol{A}$ 可相似对角化，即 $\boldsymbol{A}\sim\boldsymbol{\Lambda}$，其中 "
    r"$\boldsymbol{\Lambda}=\begin{pmatrix}n&&&\\ &0&&\\ &&\ddots&\\ &&&0\end{pmatrix}$，",
    r"$|\lambda\boldsymbol{E}-\boldsymbol{B}|=\begin{vmatrix}\lambda&0&\cdots&-1\\ 0&\lambda&\cdots&-2\\ "
    r"\vdots&\vdots&&\vdots\\ 0&0&\cdots&\lambda-n\end{vmatrix}"
    r"=\lambda^{n-1}(\lambda-n)=0\Rightarrow\lambda_{1}=\lambda_{2}=\cdots=\lambda_{n-1}=0,\lambda_{n}=n$.",
    r"当 $\lambda_{1}=\lambda_{2}=\cdots=\lambda_{n-1}=0$ 时，"
    r"$0\boldsymbol{E}-\boldsymbol{B}=\begin{pmatrix}0&0&\cdots&-1\\ 0&0&\cdots&-2\\ \vdots&\vdots&&\vdots\\ "
    r"0&0&\cdots&-n\end{pmatrix}\to\begin{pmatrix}0&0&\cdots&1\\ 0&0&\cdots&0\\ \vdots&\vdots&&\vdots\\ "
    r"0&0&\cdots&0\end{pmatrix}$，",
    r"即 $r(-\boldsymbol{B})=1$，则 $r(\boldsymbol{B})=1$，",
    r"所以 $\lambda_{1}=\lambda_{2}=\cdots=\lambda_{n-1}=0$ 对应 $n-1$ 个线性无关的特征向量，",
    r"从而 $\boldsymbol{B}$ 可相似对角化，即 $\boldsymbol{B}\sim\boldsymbol{\Lambda}$，其中 "
    r"$\boldsymbol{\Lambda}=\begin{pmatrix}n&&&\\ &0&&\\ &&\ddots&\\ &&&0\end{pmatrix}$，"
    r"所以 $\boldsymbol{A}$ 与 $\boldsymbol{B}$ 相似.",
])

A[22] = (r"(I)\ F_{Y}(y)=\begin{cases}0,&y<0\\ \dfrac{3}{4}y,&0\leqslant y<1\\ \dfrac{1}{2}\left(1+\dfrac{y}{2}\right),&1\leqslant y<2\\ 1,&y\geqslant2\end{cases};\ (II)\ E(Y)=\dfrac{3}{4}", [
    r"【详解】（I）",
    r"$F_{Y}(y)=P\{Y\leqslant y\}=P\{Y\leqslant y,X=1\}+P\{Y\leqslant y,X=2\}$",
    r"$=P\{Y\leqslant y|X=1\}P\{X=1\}+P\{Y\leqslant y|X=2\}P\{X=2\}$",
    r"$=\dfrac{1}{2}\Bigl[P\{Y\leqslant y|X=1\}+P\{Y\leqslant y|X=2\}\Bigr]$",
    r"当 $y<0$ 时，$F_{Y}(y)=0$；",
    r"当 $0\leqslant y<1$ 时，$F_{Y}(y)=\dfrac{1}{2}\left(y+\dfrac{y}{2}\right)=\dfrac{3}{4}y$；",
    r"当 $1\leqslant y<2$ 时，$F_{Y}(y)=\dfrac{1}{2}\left(1+\dfrac{y}{2}\right)$；",
    r"当 $y\geqslant2$ 时，$F_{Y}(y)=1$.",
    r"所以 $F_{Y}(y)=\begin{cases}0,&y<0\\ \dfrac{3}{4}y,&0\leqslant y<1\\ \dfrac{1}{2}\left(1+\dfrac{y}{2}\right),&1\leqslant y<2\\ 1,&y\geqslant2\end{cases}$.",
    r"（II）由 $Y$ 的分布函数 $F_{Y}(y)$ 得到概率密度为",
    r"$f(y)=F_{Y}'(y)=\begin{cases}\dfrac{3}{4},&0<y<1\\ \dfrac{1}{4},&1\leqslant y<2\\ 0,&\text{其他}\end{cases}$，",
    r"则 $E(Y)=\displaystyle\int_{-\infty}^{+\infty}yf(y)dy=\int_{0}^{1}y\dfrac{3}{4}dy+\int_{1}^{2}y\dfrac{1}{4}dy=\dfrac{3}{4}$.",
])

A[23] = (r"(I)\ P\{X=0,Y=0\}=\dfrac{2}{9},P\{X=0,Y=1\}=\dfrac{1}{9},P\{X=1,Y=0\}=\dfrac{1}{9},"
         r"P\{X=1,Y=1\}=\dfrac{5}{9};\ (II)\ \dfrac{4}{9}", [
    r"【详解】（I）由已知得 $EX=EY=\dfrac{2}{3},EX^{2}=EY^{2}=\dfrac{2}{3}$.",
    r"从而 $DX=DY=\dfrac{2}{9}$，$\rho_{XY}=\dfrac{1}{2}=\dfrac{EXY-EXEY}{\sqrt{DX}\sqrt{DY}}$，以 $EXY=\dfrac{5}{9}$，",
    r"从而 $P\{X=1,Y=1\}=\dfrac{5}{9}$.",
    r"$P\{X=1,Y=0\}=P\{X=1\}-P\{X=1,Y=1\}=\dfrac{1}{9}$",
    r"$P\{X=0,Y=0\}=P\{Y=0\}-P\{X=1,Y=0\}=\dfrac{2}{9}$",
    r"$P\{X=0,Y=1\}=P\{Y=1\}-P\{X=1,Y=1\}=\dfrac{1}{9}$",
    r"即 $\left(X,Y\right)$ 的概率分布为",
    r"$\begin{array}{c|cc|c} \boldsymbol{X}\backslash\boldsymbol{Y} & 0 & 1 & \\ \hline "
    r"0 & \dfrac{2}{9} & \dfrac{1}{9} & \dfrac{1}{3} \\ 1 & \dfrac{1}{9} & \dfrac{5}{9} & \dfrac{2}{3} \\ \hline "
    r" & \dfrac{1}{3} & \dfrac{2}{3} & \end{array}$",
    r"（II）$P\{X+Y\leqslant1\}=P\{X=0,Y=0\}+P\{X=0,Y=1\}+P\{X=1,Y=0\}=\dfrac{4}{9}$.",
])
