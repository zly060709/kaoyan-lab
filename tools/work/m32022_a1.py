# -*- coding: utf-8 -*-
"""2022 数学三 解析 选择题 1-10（原卷 p6-p9，逐字照录）"""

A = {}

A[1] = ("C", [
    r"【答案】（C）",
    r"【解析】①若 $\alpha(x)\sim\beta(x)$，则 $\lim\limits_{x\to0}\dfrac{\alpha(x)}{\beta(x)}=1$.因此 $\lim\limits_{x\to0}\dfrac{\alpha^{2}(x)}{\beta^{2}(x)}=\lim\limits_{x\to0}\dfrac{\alpha(x)}{\beta(x)}\cdot\dfrac{\alpha(x)}{\beta(x)}=1\cdot1=1$，",
    r"①正确.",
    r"②错，反例 $\alpha(x)=x,\beta(x)=-x$；",
    r"③若 $\alpha(x)\sim\beta(x)$，则 $\lim\limits_{x\to0}\dfrac{\alpha(x)}{\beta(x)}=1$，则 $\lim\limits_{x\to0}\dfrac{\alpha(x)-\beta(x)}{\alpha(x)}=\lim\limits_{x\to0}\dfrac{\alpha(x)}{\alpha(x)}-\lim\limits_{x\to0}\dfrac{\beta(x)}{\alpha(x)}=1-1=0$，",
    r"因此 $\alpha(x)-\beta(x)=o(\alpha(x))$，③正确.",
    r"④若 $\alpha(x)-\beta(x)=o(\alpha(x))$，则 $\lim\limits_{x\to0}\dfrac{\alpha(x)-\beta(x)}{\alpha(x)}=0$，则",
    r"$\lim\limits_{x\to0}\dfrac{\alpha(x)}{\alpha(x)}-\lim\limits_{x\to0}\dfrac{\beta(x)}{\alpha(x)}=1-\lim\limits_{x\to0}\dfrac{\beta(x)}{\alpha(x)}=0$，则 $\lim\limits_{x\to0}\dfrac{\beta(x)}{\alpha(x)}=1$，即 $\alpha(x)\sim\beta(x)$，④正确.",
    r"因此真命题有①③④，选（C）",
])

A[2] = ("A", [
    r"【答案】（A）",
    r"【解析】$\lim\limits_{n\to\infty}\sqrt[n]{n}=1$，因此 $\sqrt[n]{n}$ 必有界.且根据 $\sqrt{x}$ 的单调性可得 $x<e$ 时单增，$x>e$ 时单减，",
    r"因此下界是 1，$\sqrt[2]{2}$ 和 $\sqrt[3]{3}$ 是最大的两个值，对于数列 $a_n$ 来说，$a_1=1+1=2$，",
    r"$a_2=\sqrt{2}-\dfrac{1}{2}<1$，当 $n>3$ 时，$\sqrt[3]{3}$ 在 $\sqrt[n]{n}$ 中取最大值，$-\dfrac{(-1)^{n}}{n}=\dfrac{1}{3}$ 在 $-\dfrac{(-1)^{n}}{n}$ 中取最大值，",
    r"所以必有最大值，排除（C）（D）.",
    r"再考虑是否有最小值，只有 $n$ 为偶数时才有可能成为最小值，接下来证明当 $n\geqslant3$ 时，",
    r"$\sqrt[n]{n}-\dfrac{1}{n}>1$，即证 $n^{\frac{1}{n}}-1>n$，即证 $n^{n+1}>(n+1)^{n}$.可以利用单调性，证明 $b>a>e$ 时，",
    r"$a^{b}>b^{a}$，因此 $n\geqslant3$，可得 $n^{n+1}>(n+1)^{n}$，即 $n\geqslant3$ 时，$\sqrt[n]{n}-\dfrac{1}{n}>1$ 成立.因此仅当 $n=2$ 时，",
    r"$a_2=\sqrt{2}-\dfrac{1}{2}<1$ 为最小值.",
    r"因此选（A）",
])

A[3] = ("C", [
    r"【答案】（C）",
    r"【解析】$F(x,y)=\int_{0}^{x-y}(x-y-t)f(t)\mathrm{d}t=x\int_{0}^{x-y}f(t)\mathrm{d}t-y\int_{0}^{x-y}f(t)\mathrm{d}t-\int_{0}^{x-y}tf(t)\mathrm{d}t$",
    r"所以 $\dfrac{\partial F}{\partial x}=\int_{0}^{x-y}f(t)\mathrm{d}t+xf(x-y)-yf(x-y)-(x-y)f(x-y)=\int_{0}^{x-y}f(t)\mathrm{d}t$",
    r"$\dfrac{\partial F}{\partial y}=-xf(x-y)\mathrm{d}t-\int_{0}^{x-y}f(t)\mathrm{d}t+yf(x-y)+(x-y)f(x-y)=-\int_{0}^{x-y}f(t)\mathrm{d}t$",
    r"$\dfrac{\partial F}{\partial x}=-\dfrac{\partial F}{\partial y}$",
    r"$\dfrac{\partial^{2}F}{\partial x^{2}}=f(x-y),\dfrac{\partial^{2}F}{\partial y^{2}}=f(x-y)$，所以 $\dfrac{\partial^{2}F}{\partial x^{2}}=\dfrac{\partial^{2}F}{\partial y^{2}}$",
    r"综上，正确选项为（C）",
])

A[4] = ("A", [
    r"【答案】（A）",
    r"【解析】比较 $I_1,I_2$，令 $f(x)=\dfrac{x}{2}-\ln(1+x),x\in(0,1)$ 则",
    r"$f^{\prime}(x)=\dfrac{1}{2}-\dfrac{1}{1+x}=\dfrac{x-1}{2(1+x)}<0,x\in(0,1)$，又 $f(0)=0$，所以 $f(x)<f(0)=0,I_1<I_2$；",
    r"再比较 $I_2,I_3$，令",
    r"$g(x)=\dfrac{\ln(1+x)}{1+\cos x}-\dfrac{2x}{1+\sin x}=\dfrac{\ln(1+x)(1+\sin x)-2x(1+\cos x)}{(1+\cos x)(1+\sin x)}$，",
    r"$h(x)=\ln(1+x)(1+\sin x)-2x(1+\cos x)$",
    r"$=\ln(1+x)+x\sin x\cdot\ln(1+x)-x-2x\cos x,x\in(0,1)$",
    r"其中 $\ln(1+x)-x<0,\ \sin x\cdot\ln(1+x)-x<0,\ -2x\cos x<0$，则 $I_2<I_3$，故选（A）",
])

A[5] = ("B", [
    r"【答案】（B）",
    r"【解析】$A$ 有 3 个不同特征值，故 $A$ 一定可以对角化 $\Leftrightarrow$ 存在可逆矩阵 $P$，使得",
    r"$A=P\Lambda P^{-1}$.",
])

A[6] = ("D", [
    r"【答案】（D）",
    r"【解析】根据非齐次方程组 $A\boldsymbol{x}=\boldsymbol{b}$ 解判别的充要条件：系数矩阵秩与增广矩阵秩的关系",
    r"当 $r(A)=r(A,\boldsymbol{b})=n$ 时，$A\boldsymbol{x}=\boldsymbol{b}$ 有唯一解；",
    r"当 $r(A)=r(A,\boldsymbol{b})<n$ 时，$A\boldsymbol{x}=\boldsymbol{b}$ 有无穷多解；",
    r"当 $r(A)<r(A,\boldsymbol{b})$ 时，$A\boldsymbol{x}=\boldsymbol{b}$ 无解；",
    r"$(A,\boldsymbol{b})=\begin{pmatrix}1&1&1&1\\ 1&a&a^{2}&2\\ 1&b&b^{2}&4\end{pmatrix}\Rightarrow\begin{pmatrix}1&1&1&1\\ 0&a-1&a^{2}-1&1\\ 0&b-1&b^{2}-1&3\end{pmatrix}$",
    r"当 $a=1$ 或 $b=1$ 时，此时方程组无解；",
    r"当 $a\neq1$ 且 $b\neq1$ 时，原式化简为 $\begin{pmatrix}1&1&1&1\\ 0&1&a+1&\dfrac{1}{a-1}\\ 0&0&b-a&\dfrac{3}{b-1}-\dfrac{1}{a-1}\end{pmatrix}$",
    r"当 $a=b$ 时，$\dfrac{3}{b-1}-\dfrac{1}{a-1}\neq0$，$r(A)<r(A,\boldsymbol{b})$，此时方程组无解；",
    r"当 $a\neq b$ 时，$r(A)=r(A,\boldsymbol{b})=3$，此时 $A\boldsymbol{x}=\boldsymbol{b}$ 有唯一解，",
    r"故答案选（D）",
])

A[7] = ("C", [
    r"【答案】（C）",
    r"【解析】$(\boldsymbol{\alpha}_1,\boldsymbol{\alpha}_2,\boldsymbol{\alpha}_3,\boldsymbol{\alpha}_4)=\begin{pmatrix}\lambda&1&1&1\\ 1&\lambda&1&\lambda\\ 1&1&\lambda&\lambda^{2}\end{pmatrix}\sim\begin{pmatrix}1&1&\lambda&\lambda^{2}\\ 0&\lambda-1&1-\lambda&\lambda-\lambda^{2}\\ 0&1-\lambda&1-\lambda^{2}&1-\lambda^{3}\end{pmatrix}$",
    r"$\sim\begin{pmatrix}1&1&\lambda&\lambda^{2}\\ 0&\lambda-1&1-\lambda&\lambda-\lambda^{2}\\ 0&0&2-\lambda-\lambda^{2}&1+\lambda-\lambda^{2}-\lambda^{3}\end{pmatrix}$",
    r"已知 $\boldsymbol{\alpha}_1,\boldsymbol{\alpha}_2,\boldsymbol{\alpha}_3$ 与 $\boldsymbol{\alpha}_1,\boldsymbol{\alpha}_2,\boldsymbol{\alpha}_4$ 等价，则 $r(\boldsymbol{\alpha}_1,\boldsymbol{\alpha}_2,\boldsymbol{\alpha}_3)=r(\boldsymbol{\alpha}_1,\boldsymbol{\alpha}_2,\boldsymbol{\alpha}_4)=r(\boldsymbol{\alpha}_1,\boldsymbol{\alpha}_2,\boldsymbol{\alpha}_3,\boldsymbol{\alpha}_4)$",
    r"当 $\lambda=-1$ 时，$r(\boldsymbol{\alpha}_1,\boldsymbol{\alpha}_2,\boldsymbol{\alpha}_3)=3,r(\boldsymbol{\alpha}_1,\boldsymbol{\alpha}_2,\boldsymbol{\alpha}_4)=2$ 与向量组等价矛盾，故 $\lambda\neq-1$",
    r"当 $\lambda=-2$ 时，$r(\boldsymbol{\alpha}_1,\boldsymbol{\alpha}_2,\boldsymbol{\alpha}_3)=2,r(\boldsymbol{\alpha}_1,\boldsymbol{\alpha}_2,\boldsymbol{\alpha}_4)=3$ 与向量组等价矛盾，故 $\lambda\neq-2$",
    r"故排除（B）（D）；当 $\lambda=2$，$r(\boldsymbol{\alpha}_1,\boldsymbol{\alpha}_2,\boldsymbol{\alpha}_3)=r(\boldsymbol{\alpha}_1,\boldsymbol{\alpha}_2,\boldsymbol{\alpha}_4)=3$，故排除 A，于是该题选择（C）",
])

A[8] = ("D", [
    r"【答案】（D）",
    r"【解析】$D(X-3Y+1)=D(X)+9D(Y)$",
    r"由 $X\sim N(0,4),Y\sim B\left(3,\dfrac{1}{3}\right)$ 知，$D(X)=4,D(Y)=\dfrac{2}{3}$，故 $D(X-3Y+1)=10$，故选（D）",
])

A[9] = ("B", [
    r"【答案】（B）",
    r"【解析】由辛钦大数定律知，$\dfrac{1}{n}\sum\limits_{i=1}^{n}X_i^{2}$ 依概率收敛于 $E(X^{2})$",
    r"由于 $E(X^{2})=\int_{-\infty}^{+\infty}x^{2}f(x)\mathrm{d}x=\int_{-1}^{1}x^{2}(1-|x|)\mathrm{d}x=\dfrac{1}{6}$，故选（B）",
])

A[10] = ("B", [
    r"【答案】（B）",
    r"【解析】令事件 $A=\{\max(X,Y)=2\},B=\{\min(X,Y)=1\}$，则",
    r"$P(A)=P\{X=-1,Y=2\}+P\{X=1,Y=2\}=b+0.1$",
    r"$P(B)=P\{X=1,Y=1\}+P\{X=1,Y=2\}=0.2$，",
    r"$P(AB)=P\{X=1,Y=2\}=0.1$",
    r"因为事件 $A,B$ 独立，所以 $P(AB)=P(A)P(B)$，即",
    r"$(b+0.1)\times0.2=0.1$，又由规范性知 $a+b=0.6$，则可得 $a=0.2,b=0.4$，",
    r"所以 $X$ 的边缘分布律为 $\begin{array}{|c|cc|}\hline X&-1&1\\\hline P&0.6&0.4\\\hline\end{array}$",
    r"$Y$ 的边缘分布律为 $\begin{array}{|c|ccc|}\hline Y&0&1&2\\\hline P&0.3&0.2&0.5\\\hline\end{array}$",
    r"则 $E(X)=-1\times0.6+1\times0.4=-0.2\ E(Y)=0\times0.3+1\times0.2+2\times0.5=1.2$",
    r"$E(XY)=-1\times0.1+(-2)\times0.4+1\times0.1+2\times0.1=-0.6$",
    r"所以 $Cov(X,Y)=E(XY)-E(X)E(Y)=-0.36$",
])
