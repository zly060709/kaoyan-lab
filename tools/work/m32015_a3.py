# -*- coding: utf-8 -*-
"""2015 数学三 解析 解答题 15-23（原卷 p8-p12，逐字照录）"""

A = {}

A[15] = ("a=-1, b=-1/2, k=-1/3", [
    r"【答案】$a=-1,b=-\dfrac{1}{2},k=-\dfrac{1}{3}$",
    r"【解析】因为 $\ln(1+x)=x-\dfrac{x^{2}}{2}+\dfrac{x^{3}}{3}+o(x^{3}),\sin x=x-\dfrac{x^{3}}{3!}+o(x^{3})$，那么，",
    r"$1=\lim\limits_{x\to0}\dfrac{f(x)}{g(x)}=\lim\limits_{x\to0}\dfrac{x+a\ln(1+x)+bx\sin x}{kx^{3}}"
    r"=\lim\limits_{x\to0}\dfrac{(1+a)x+(b-\dfrac{a}{2})x^{2}+\dfrac{a}{3}x^{3}+o(x^{3})}{kx^{3}}$,",
    r"可得：$\begin{cases}1+a=0\\ b-\dfrac{a}{2}=0\\ \dfrac{a}{3k}=1\end{cases}$，所以，$\begin{cases}a=-1\\ b=-\dfrac{1}{2}\\ k=-\dfrac{1}{3}\end{cases}$.",
])

A[16] = (r"\dfrac{\pi}{4}-\dfrac{2}{5}", [
    r"【答案】$\dfrac{\pi}{4}-\dfrac{2}{5}$",
    r"【解析】由于被积区域关于 $y$ 轴对阵且 $xy$ 是关于 $x$ 的奇函数，则 $\iint\limits_{D}xydxdy=0$；故：",
    r"$\iint\limits_{D}x(x+y)dxdy=\iint\limits_{D}x^{2}dxdy$",
    r"$=2\int_{0}^{1}dx\int_{x^{2}}^{\sqrt{2-x^{2}}}x^{2}dy=2\int_{0}^{1}x^{2}\left(\sqrt{2-x^{2}}-x^{2}\right)dx$",
    r"$=2\int_{0}^{1}x^{2}\sqrt{2-x^{2}}\,dx-\dfrac{2}{5}\stackrel{x=\sqrt{2}\sin t}{=}2\int_{0}^{\frac{\pi}{4}}2\sin^{2}t\,2\cos^{2}t\,dt-\dfrac{2}{5}$",
    r"$=2\int_{0}^{\frac{\pi}{4}}\sin^{2}2t\,dt-\dfrac{2}{5}=\dfrac{\pi}{4}-\dfrac{2}{5}$.",
])

A[17] = ("(I)略; (II)P=30", [
    r"【答案】(I) 略（II）$P=30$.",
    r"【解析】(I) 由于利润函数 $L(Q)=R(Q)-C(Q)=PQ-C(Q)$,两边对 $Q$ 求导，得",
    r"$\dfrac{dL}{dQ}=P+Q\dfrac{dP}{dQ}-C'(Q)=P+Q\dfrac{dP}{dQ}-MC$.",
    r"当且仅当 $\dfrac{dL}{dQ}=0$ 时，利润 $L(Q)$ 最大，又由于 $\eta=-\dfrac{P}{Q}\dfrac{dP}{dQ}$,所以 $\dfrac{dP}{dQ}=-\dfrac{1}{\eta}\dfrac{P}{Q}$,",
    r"故当 $P=\dfrac{MC}{1-\dfrac{1}{\eta}}$ 时，利润最大.",
    r"(II) 由于 $MC=C'(Q)=2Q=2(40-P)$,则 $\eta=-\dfrac{P}{Q}\dfrac{dQ}{dP}=\dfrac{P}{40-P}$ 代入(I)中的定价模型,",
    r"得 $P=\dfrac{2(40-P)}{1-\dfrac{40-P}{P}}$,从而解得 $P=30$.",
])

A[18] = (r"f(x)=\dfrac{8}{4-x}", [
    r"【答案】$f(x)=\dfrac{8}{4-x}$",
    r"【解析】曲线的切线方程为 $y-f(x_{0})=f'(x_{0})(x-x_{0})$，切线与 $x$ 轴的交点为",
    r"$\left(x_{0}-\dfrac{f(x_{0})}{f'(x_{0})},0\right)$. 故面积为：$s=\dfrac{1}{2}\dfrac{f^{2}(x_{0})}{f'(x_{0})}=4$.",
    r"故 $f(x)$ 满足的方程为 $f^{2}(x)=8f'(x)$,此为可分离变量的微分方程,",
    r"解得 $f(x)=\dfrac{-8}{x+C}$，又由于 $f(0)=2$，带入可得 $C=-4$，从而 $f(x)=\dfrac{8}{4-x}$.",
])

A[19] = (r"f'(x)=u_{1}'(x)u_{2}(x)\cdots u_{n}(x)+u_{1}(x)u_{2}'(x)\cdots u_{n}(x)"
         r"+\cdots+u_{1}(x)u_{2}(x)\cdots u_{n}'(x)", [
    r"【答案】$f'(x)=\left[u_{1}(x)u_{2}(x)\cdots u_{n}(x)\right]'$",
    r"$=u_{1}'(x)u_{2}(x)\cdots u_{n}(x)+u_{1}(x)u_{2}'(x)\cdots u_{n}(x)+\cdots+u_{1}(x)u_{2}(x)\cdots u_{n}'(x)$",
    r"【解析】(I) $\left[u(x)v(x)\right]'=\lim\limits_{h\to0}\dfrac{u(x+h)v(x+h)-u(x)v(x)}{h}$",
    r"$=\lim\limits_{h\to0}\dfrac{u(x+h)v(x+h)-u(x+h)v(x)+u(x+h)v(x)-u(x)v(x)}{h}$",
    r"$=\lim\limits_{h\to0}u(x+h)\dfrac{v(x+h)-v(x)}{h}+\lim\limits_{h\to0}\dfrac{u(x+h)-u(x)}{h}v(x)$",
    r"$=u(x)v'(x)+u'(x)v(x)$.",
    r"(II) 由题意得",
    r"$f'(x)=\left[u_{1}(x)u_{2}(x)\cdots u_{n}(x)\right]'$",
    r"$=u_{1}'(x)u_{2}(x)\cdots u_{n}(x)+u_{1}(x)u_{2}'(x)\cdots u_{n}(x)+\cdots+u_{1}(x)u_{2}(x)\cdots u_{n}'(x)$.",
])

A[20] = (r"a=0,\ X=\begin{pmatrix}3&1&-2\\ 1&1&-1\\ 2&1&-1\end{pmatrix}", [
    r"【答案】$a=0,\boldsymbol{X}=\begin{pmatrix}3&1&-2\\ 1&1&-1\\ 2&1&-1\end{pmatrix}$",
    r"【解析】(I) $\boldsymbol{A}^{3}=\boldsymbol{O}\Rightarrow\left|\boldsymbol{A}\right|=0\Rightarrow"
    r"\begin{vmatrix}a&1&0\\ 1&a&-1\\ 0&1&a\end{vmatrix}=\begin{vmatrix}0&1&0\\ 1-a^{2}&a&-1\\ -a&1&a\end{vmatrix}"
    r"=a^{3}=0\Rightarrow a=0$.",
    r"(II) 由题意知",
    r"$\boldsymbol{X}-\boldsymbol{XA}^{2}-\boldsymbol{AX}+\boldsymbol{AXA}^{2}=\boldsymbol{E}\Rightarrow"
    r"\boldsymbol{X}\left(\boldsymbol{E}-\boldsymbol{A}^{2}\right)-\boldsymbol{AX}\left(\boldsymbol{E}-\boldsymbol{A}^{2}\right)=\boldsymbol{E}$",
    r"$\Rightarrow\left(\boldsymbol{E}-\boldsymbol{A}\right)\boldsymbol{X}\left(\boldsymbol{E}-\boldsymbol{A}^{2}\right)=\boldsymbol{E}"
    r"\Rightarrow\boldsymbol{X}=\left(\boldsymbol{E}-\boldsymbol{A}\right)^{-1}\left(\boldsymbol{E}-\boldsymbol{A}^{2}\right)^{-1}"
    r"=\left[\left(\boldsymbol{E}-\boldsymbol{A}^{2}\right)\left(\boldsymbol{E}-\boldsymbol{A}\right)\right]^{-1}$ 且",
    r"$\Rightarrow\boldsymbol{X}=\left(\boldsymbol{E}-\boldsymbol{A}^{2}-\boldsymbol{A}\right)^{-1}$",
    r"$\boldsymbol{E}-\boldsymbol{A}^{2}-\boldsymbol{A}=\begin{pmatrix}0&-1&1\\ -1&1&1\\ -1&-1&2\end{pmatrix}$,",
    r"$\left(\begin{array}{ccc:ccc}0&-1&1&1&0&0\\ -1&1&1&0&1&0\\ -1&-1&2&0&0&1\end{array}\right)"
    r"\to\left(\begin{array}{ccc:ccc}1&-1&-1&0&-1&0\\ 0&-1&1&1&0&0\\ -1&-1&2&0&0&1\end{array}\right)$",
    r"$\to\left(\begin{array}{ccc:ccc}1&-1&-1&0&-1&0\\ 0&1&-1&-1&0&0\\ 0&-2&1&0&-1&1\end{array}\right)"
    r"\to\left(\begin{array}{ccc:ccc}1&-1&-1&0&-1&0\\ 0&1&-1&-1&0&0\\ 0&0&-1&-2&-1&1\end{array}\right)$",
    r"$\to\left(\begin{array}{ccc:ccc}1&-1&0&2&0&-1\\ 0&1&0&1&1&-1\\ 0&0&1&2&1&-1\end{array}\right)"
    r"\to\left(\begin{array}{ccc:ccc}1&0&0&3&1&-2\\ 0&1&0&1&1&-1\\ 0&0&1&2&1&-1\end{array}\right)$",
    r"$\therefore\boldsymbol{X}=\begin{pmatrix}3&1&-2\\ 1&1&-1\\ 2&1&-1\end{pmatrix}$.",
])

A[21] = (r"a=4,\ b=5,\ P=\begin{pmatrix}2&-3&-1\\ 1&0&-1\\ 0&1&1\end{pmatrix}", [
    r"【解析】(I) $\boldsymbol{A}\sim\boldsymbol{B}\Rightarrow tr(\boldsymbol{A})=tr(\boldsymbol{B})\Rightarrow3+a=1+b+1$.",
    r"$\left|\boldsymbol{A}\right|=\left|\boldsymbol{B}\right|\Rightarrow\begin{vmatrix}0&2&-3\\ -1&3&-3\\ 1&-2&a\end{vmatrix}"
    r"=\begin{vmatrix}1&-2&0\\ 0&b&0\\ 0&3&1\end{vmatrix}$,",
    r"$\begin{cases}a-b=-1\\ 2a-b=3\end{cases}\Rightarrow\begin{cases}a=4\\ b=5\end{cases}$.",
    r"(II) 结合(I)，$\left|\lambda\boldsymbol{E}-\boldsymbol{B}\right|=\begin{vmatrix}\lambda-1&-2&0\\ 0&\lambda-5&0\\ 0&3&\lambda-1\end{vmatrix}"
    r"=\left(\lambda-1\right)^{2}\left(\lambda-5\right)=0$,",
    r"$\boldsymbol{B}$ 的特征值 $\lambda_{1}=\lambda_{2}=1,\lambda_{3}=5$；",
    r"且 $\boldsymbol{A}$ 与 $\boldsymbol{B}$ 相似，则有 $\boldsymbol{A}$ 的特征值 $\lambda_{1}=\lambda_{2}=1,\lambda_{3}=5$；",
    r"$\lambda_{1}=\lambda_{2}=1$ 时 $\left(\boldsymbol{E}-\boldsymbol{A}\right)\boldsymbol{x}=\boldsymbol{0}$ 的基础解系为"
    r"$\boldsymbol{\xi}_{1}=(2,1,0)^{T};\boldsymbol{\xi}_{2}=(-3,0,1)^{T}$;",
    r"$\lambda_{3}=5$ 时 $(5\boldsymbol{E}-\boldsymbol{A})\boldsymbol{x}=\boldsymbol{0}$ 的基础解系为 $\boldsymbol{\xi}_{3}=(-1,-1,1)^{T}$.",
    r"令 $\boldsymbol{P}=(\boldsymbol{\xi}_{1},\boldsymbol{\xi}_{2},\boldsymbol{\xi}_{3})=\begin{pmatrix}2&-3&-1\\ 1&0&-1\\ 0&1&1\end{pmatrix}$，"
    r"则可逆矩阵 $\boldsymbol{P}$，使 $\boldsymbol{P}^{-1}\boldsymbol{AP}$ 为对角矩阵.即",
    r"$\boldsymbol{P}^{-1}\boldsymbol{AP}=\begin{pmatrix}1& &\\ &1&\\ & &5\end{pmatrix}$.",
])

A[22] = (r"(I)\ P\{Y=n\}=C_{n-1}^{1}p(1-p)^{n-2}p=(n-1)\left(\dfrac{1}{8}\right)^{2}\left(\dfrac{7}{8}\right)^{n-2},\ n=2,3,\cdots;\ "
         r"(II)\ E(Y)=16", [
    r"【答案】(I) $P\{Y=n\}=C_{n-1}^{1}p(1-p)^{n-2}p=(n-1)(\dfrac{1}{8})^{2}(\dfrac{7}{8})^{n-2}$，$n=2,3,\cdots$；",
    r"(II) $E(Y)=16$.",
    r"【解析】(I) 记 $p$ 为观测值大于 3 的概率，则 $p=P(X>3)=\int_{3}^{+\infty}2^{-x}ln2dx=\dfrac{1}{8}$,",
    r"从而 $P\{Y=n\}=C_{n-1}^{1}p(1-p)^{n-2}p=(n-1)(\dfrac{1}{8})^{2}(\dfrac{7}{8})^{n-2}$，$n=2,3,\cdots$",
    r"为 $Y$ 的概率分布；",
    r"(II) $E(Y)=\sum\limits_{n=2}^{\infty}n\cdot P\{Y=n\}=\sum\limits_{n=2}^{\infty}n\cdot(n-1)(\dfrac{1}{8})^{2}(\dfrac{7}{8})^{n-2}$",
    r"记 $S(x)=\sum\limits_{n=2}^{\infty}n\cdot(n-1)x^{n-2}$ $-1<x<1$，则 $E(Y)=(\dfrac{1}{8})^{2}S(\dfrac{7}{8})$",
    r"$S(x)=\sum\limits_{n=2}^{\infty}n\cdot(n-1)x^{n-2}=(\sum\limits_{n=2}^{\infty}n\cdot x^{n-1})'=(\sum\limits_{n=2}^{\infty}x^{n})''"
    r"=\dfrac{2}{\left(1-x\right)^{3}}$，所以 $E(Y)=(\dfrac{1}{8})^{2}S(\dfrac{7}{8})=16$.",
])

A[23] = (r"(I)\ \hat{\theta}=2\overline{X}-1;\ (II)\ \hat{\theta}=\min\{X_{1},X_{2},\cdots,X_{n}\}", [
    r"【答案】(I) $\hat{\theta}=2\overline{X}-1$，$\overline{X}=\dfrac{1}{n}\sum\limits_{i=1}^{n}X_{i}$；",
    r"(II) $\hat{\theta}=\min\{X_{1},X_{2},\cdots,X_{n}\}$.",
    r"【解析】(I) $E(X)=\int_{-\infty}^{+\infty}xf(x;\theta)dx=\int_{\theta}^{1}x\cdot\dfrac{1}{1-\theta}dx=\dfrac{1+\theta}{2}$，",
    r"令 $E(X)=\overline{X}$，即 $\dfrac{1+\theta}{2}=\overline{X}$，解得 $\hat{\theta}=2\overline{X}-1$, $\overline{X}=\dfrac{1}{n}\sum\limits_{i=1}^{n}X_{i}$ 为 $\theta$ 的矩估计量 ；",
    r"(II) 似然函数 $L(\theta)=\prod\limits_{i=1}^{n}f(x_{i};\theta)$，",
    r"当 $\theta\leq x_{i}\leq1$ 时，$L(\theta)=\prod\limits_{i=1}^{n}\dfrac{1}{1-\theta}=(\dfrac{1}{1-\theta})^{n}$，则 $\ln L(\theta)=-n\ln(1-\theta)$.",
    r"从而 $\dfrac{d\ln L(\theta)}{d\theta}=\dfrac{n}{1-\theta}$，关于 $\theta$ 单调增加,",
    r"所以 $\hat{\theta}=\min\{X_{1},X_{2},\cdots,X_{n}\}$ 为 $\theta$ 的最大似然估计.",
])
