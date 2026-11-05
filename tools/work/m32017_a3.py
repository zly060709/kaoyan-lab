# -*- coding: utf-8 -*-
"""2017 数学三 解析 解答题 15-23（原卷 p8-p13，逐字照录）"""

A = {}

A[15] = (r"\dfrac{2}{3}", [
    r"【解析】$\displaystyle\int_{0}^{x}\sqrt{x-t}e^{t}dt\xlongequal{x-t=u}\int_{0}^{x}\sqrt{u}e^{x-u}du=e^{x}\int_{0}^{x}\sqrt{u}e^{-u}du$",
    r"则 $\lim\limits_{x\to0^{+}}\dfrac{\displaystyle\int_{0}^{x}\sqrt{x-t}e^{t}dt}{\sqrt{x^{3}}}"
    r"=\lim\limits_{x\to0^{+}}\dfrac{e^{x}\displaystyle\int_{0}^{x}\sqrt{u}e^{-u}du}{\sqrt{x^{3}}}"
    r"=\lim\limits_{x\to0^{+}}\dfrac{\displaystyle\int_{0}^{x}\sqrt{u}e^{-u}du}{\sqrt{x^{3}}}$",
    r"$=\lim\limits_{x\to0^{+}}\dfrac{\sqrt{x}e^{-x}}{\dfrac{3}{2}\sqrt{x}}=\dfrac{2}{3}.$",
])

A[16] = (r"\dfrac{2-\sqrt{2}}{16}\pi", [
    r"【解析】",
    r"$\displaystyle\iint\limits_{D}\dfrac{y^{3}}{\left(1+x^{2}+y^{4}\right)^{2}}dxdy"
    r"=\int_{0}^{+\infty}dx\int_{0}^{\sqrt{x}}\dfrac{y^{3}}{\left(1+x^{2}+y^{4}\right)^{2}}dy$",
    r"$=\displaystyle\int_{0}^{+\infty}dx\int_{0}^{\sqrt{x}}\dfrac{1}{4}\dfrac{1}{\left(1+x^{2}+y^{4}\right)^{2}}d\left(1+x^{2}+y^{4}\right)"
    r"=\int_{0}^{+\infty}\dfrac{1}{4}(-1)\dfrac{1}{\left(1+x^{2}+y^{4}\right)}\Big|_{0}^{\sqrt{x}}dx$",
    r"$=\dfrac{-1}{4}\displaystyle\int_{0}^{+\infty}\left(\dfrac{1}{1+x^{2}+x^{2}}-\dfrac{1}{1+x^{2}}\right)dx"
    r"=\dfrac{1}{4}\int_{0}^{+\infty}\left(\dfrac{1}{1+x^{2}}-\dfrac{1}{1+2x^{2}}\right)dx$",
    r"$=\dfrac{1}{4}\left[\arctan(x)-\dfrac{1}{\sqrt{2}}\arctan\left(\sqrt{2}x\right)\right]\Big|_{0}^{+\infty}"
    r"=\dfrac{1}{4}\left[\dfrac{\pi}{2}-\dfrac{1}{\sqrt{2}}\dfrac{\pi}{2}\right]$",
    r"$=\dfrac{2-\sqrt{2}}{16}\pi$",
])

A[17] = (r"\dfrac{1}{4}", [
    r"【解析】$\lim\limits_{n\to\infty}\sum\limits_{k=1}^{n}\dfrac{k}{n^{2}}\ln\left(1+\dfrac{k}{n}\right)"
    r"=\lim\limits_{n\to\infty}\dfrac{1}{n}\sum\limits_{k=1}^{n}\dfrac{k}{n}\ln\left(1+\dfrac{k}{n}\right)=\int_{0}^{1}x\ln(1+x)dx$",
    r"$=\dfrac{1}{2}\displaystyle\int_{0}^{1}\ln(1+x)d\left(x^{2}\right)"
    r"=\dfrac{1}{2}x^{2}\ln(1+x)\Big|_{0}^{1}-\dfrac{1}{2}\int_{0}^{1}\dfrac{\left(x^{2}-1\right)+1}{1+x}dx$",
    r"$=\dfrac{1}{2}\ln 2-\dfrac{1}{2}\displaystyle\int_{0}^{1}\left(x-1+\dfrac{1}{1+x}\right)dx"
    r"=\dfrac{1}{2}\ln 2-\dfrac{1}{4}+\dfrac{1}{2}-\dfrac{1}{2}\ln 2=\dfrac{1}{4}.$",
])

A[18] = (r"\dfrac{1}{\ln 2}-1<k<\dfrac{1}{2}", [
    r"【解析】令 $f(x)=\dfrac{1}{\ln(1+x)}-\dfrac{1}{x}$，",
    r"$f'(x)=-\dfrac{1}{\ln^{2}(1+x)}\cdot\dfrac{1}{1+x}+\dfrac{1}{x^{2}}"
    r"=\dfrac{(1+x)\ln^{2}(1+x)-x^{2}}{x^{2}(1+x)\ln^{2}(1+x)}$，",
    r"令 $g(x)=(1+x)\ln^{2}(1+x)-x^{2}$，可得 $g'(x)=\ln^{2}(1+x)+2\ln(1+x)-2x$，",
    r"$g''(x)=2\dfrac{\ln(1+x)-x}{1+x}<0$，$x\in(0,1)$，",
    r"故 $g'(x)$ 在 $[0,1]$ 上单调递减，从而 $x\in(0,1)$ 时 $g'(x)<g'(0)=0$，",
    r"故 $g(x)$ 在 $[0,1]$ 上单调递减，从而 $x\in(0,1)$ 时 $g(x)<g(0)=0$.",
    r"因此有 $f'(x)<0$，可知 $f(x)$ 在 $(0,1]$ 上单调递减，"
    r"从而 $f(1)<f(x)<\lim\limits_{x\to0^{+}}f(x)$，又",
    r"$f(1)=\dfrac{1}{\ln 2}-1$，"
    r"$\lim\limits_{x\to0^{+}}f(x)=\lim\limits_{x\to0^{+}}\left(\dfrac{1}{\ln(1+x)}-\dfrac{1}{x}\right)=\dfrac{1}{2}$，"
    r"则要使得 $f(x)=k$ 在 $(0,1)$ 内有实根，必有 $\dfrac{1}{\ln 2}-1<k<\dfrac{1}{2}$.",
])

A[19] = (r"(1)\ R\geqslant 1;\ (2)\ S(x)=\dfrac{e^{-x}}{1-x}", [
    r"【解析】",
    r"（1）$a_{0}=1,a_{1}=0$, $a_{n+1}=\dfrac{1}{n+1}\left(na_{n}+a_{n-1}\right)$，所以 $0\leqslant a_{n+1}\leqslant 1$；"
    r"记 R 为 $\sum\limits_{n=0}^{\infty}a_{n}x^{n}$ 的收敛半径；当 $|x|<1$ 时，"
    r"因为 $\left|a_{n}x^{n}\right|\leqslant|x|^{n}$ 且 $\sum\limits_{n=0}^{\infty}x^{n}$ 收敛，"
    r"所以 $\sum\limits_{n=0}^{\infty}a_{n}x^{n}$ 绝对收敛，于是",
    r"$(-1,1)\in(-R,R)$, 故 $\mathrm{R}\geqslant 1$",
    r"（2）由逐项求导定理可知 $S'(x)=\sum\limits_{n=1}^{\infty}na_{n}x^{n-1}$",
    r"故 $(1-x)S'(x)=(1-x)\displaystyle\sum_{n=1}^{\infty}na_{n}x^{n-1}"
    r"=\sum_{n=1}^{\infty}na_{n}x^{n-1}-\sum_{n=1}^{\infty}na_{n}x^{n}$",
    r"$=\displaystyle\sum_{n=0}^{\infty}(n+1)a_{n+1}x^{n}-\sum_{n=1}^{\infty}na_{n}x^{n}"
    r"=\sum_{n=1}^{\infty}\left[(n+1)a_{n+1}-na_{n}\right]x^{n}+a_{1}$，",
    r"$xS(x)=\displaystyle\sum_{n=0}^{\infty}a_{n}x^{n+1}=\sum_{n=1}^{\infty}a_{n-1}x^{n}$，",
    r"则 $(1-x)S'(x)-xS(x)=\displaystyle\sum_{n=1}^{\infty}\left[(n+1)a_{n+1}-na_{n}-a_{n-1}\right]x^{n}+a_{1}$，",
    r"由 $a_{n+1}=\dfrac{1}{n+1}\left(na_{n}+a_{n-1}\right)$ 可知 $(n+1)a_{n+1}-na_{n}-a_{n-1}=0$，",
    r"又由于 $a_{1}=0$，故 $(1-x)S'(x)-xS(x)=0$,",
    r"解此微分方程可得 $S(x)=\dfrac{ce^{-x}}{1-x}$.",
    r"又由于 $S(0)=a_{0}=1$，可知 $c=1$，从而 $S(x)=\dfrac{e^{-x}}{1-x}$.",
])

A[20] = (r"(1)\ 证明见解析;\ (2)\ x=k(1,2,-1)^{T}+(1,1,1)^{T}", [
    r"【解析】(1) 证明：设 $\boldsymbol{A}$ 的特征值为 $\lambda_{1},\lambda_{2},\lambda_{3}$，",
    r"因为 $\boldsymbol{A}$ 有三个不同的特征值，所以 $\boldsymbol{A}$ 可以相似对角化，"
    r"即存在可逆矩阵 $\boldsymbol{P}$，使得",
    r"$\boldsymbol{P}^{-1}\boldsymbol{AP}=\begin{pmatrix}\lambda_{1}& &\\ &\lambda_{2}&\\ & &\lambda_{3}\end{pmatrix}$，",
    r"因为 $\lambda_{1},\lambda_{2},\lambda_{3}$ 两两不同，所以 $\mathrm{R}(\boldsymbol{A})\geqslant 2$，",
    r"又因为 $\boldsymbol{\alpha}_{3}=\boldsymbol{\alpha}_{1}+2\boldsymbol{\alpha}_{2}$，"
    r"所以 $\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}$ 线性相关，"
    r"从而 $\mathrm{R}(\boldsymbol{A})<3$，于是 $\mathrm{R}(\boldsymbol{A})=2$.",
    r"（2）因为 $\mathrm{R}(\boldsymbol{A})=2$，所以 $\boldsymbol{Ax}=\boldsymbol{0}$ 基础解系中有一个线性无关的解向量，由",
    r"$\begin{cases}\boldsymbol{\alpha}_{1}+2\boldsymbol{\alpha}_{2}-\boldsymbol{\alpha}_{3}=\boldsymbol{0}\\ "
    r"\boldsymbol{\alpha}_{1}+\boldsymbol{\alpha}_{2}+\boldsymbol{\alpha}_{3}=\boldsymbol{\beta}\end{cases}$ "
    r"得 $\boldsymbol{Ax}=\boldsymbol{\beta}$ 的通解为 "
    r"$\boldsymbol{x}=\mathrm{k}\begin{pmatrix}1\\ 2\\ -1\end{pmatrix}+\begin{pmatrix}1\\ 1\\ 1\end{pmatrix}$（k 为任意常数）.",
])

A[21] = (r"a=2,\ Q=(\gamma_{1},\gamma_{2},\gamma_{3})", [
    r"【解析】",
    r"$\boldsymbol{A}=\begin{pmatrix}2&1&-4\\ 1&-1&1\\ -4&1&a\end{pmatrix}$，"
    r"$\boldsymbol{x}=\begin{pmatrix}x_{1}\\ x_{2}\\ x_{3}\end{pmatrix}$，$f(x_{1},x_{2},x_{3})=\boldsymbol{x}^{T}\boldsymbol{Ax}$.",
    r"因为 $\lambda_{3}=0$，所以 $\left|\boldsymbol{A}\right|=0$.",
    r"由 $\left|\boldsymbol{A}\right|=\begin{vmatrix}2&1&-4\\ 1&-1&1\\ -4&1&a\end{vmatrix}=-3(a-2)=0$ 得 $a=2$.",
    r"由 $\left|\lambda\boldsymbol{E}-\boldsymbol{A}\right|=\begin{vmatrix}\lambda-2&-1&4\\ -1&\lambda+1&-1\\ 4&-1&\lambda-2\end{vmatrix}"
    r"=\lambda(\lambda+3)(\lambda-6)=0$ 得 $\lambda_{1}=-3,\lambda_{2}=6,\lambda_{3}=0$.",
    r"由 $-3\boldsymbol{E}-\boldsymbol{A}=\begin{pmatrix}-5&-1&4\\ -1&-2&-1\\ 4&-1&-5\end{pmatrix}"
    r"\to\begin{pmatrix}1&0&-1\\ 0&1&1\\ 0&0&0\end{pmatrix}$ 得",
    r"$\lambda_{1}=-3$ 对应的线性无关的特征向量为 $\boldsymbol{\alpha}_{1}=\begin{pmatrix}1\\ -1\\ 1\end{pmatrix}$；",
    r"由 $6\boldsymbol{E}-\boldsymbol{A}=\begin{pmatrix}4&-1&4\\ -1&7&-1\\ 4&-1&4\end{pmatrix}"
    r"\to\begin{pmatrix}1&0&1\\ 0&1&0\\ 0&0&0\end{pmatrix}$ 得",
    r"$\lambda_{2}=6$ 对应的线性无关的特征向量为 $\boldsymbol{\alpha}_{2}=\begin{pmatrix}-1\\ 0\\ 1\end{pmatrix}$；",
    r"由 $0\boldsymbol{E}-\boldsymbol{A}=\begin{pmatrix}-2&-1&4\\ -1&1&-1\\ 4&-1&-2\end{pmatrix}"
    r"\to\begin{pmatrix}1&0&-1\\ 0&1&-2\\ 0&0&0\end{pmatrix}$ 得",
    r"$\lambda_{3}=0$ 对应的线性无关的特征向量为 $\boldsymbol{\alpha}_{3}=\begin{pmatrix}1\\ 2\\ 1\end{pmatrix}$，",
    r"单位正交化得 $\boldsymbol{\gamma}_{1}=\dfrac{1}{\sqrt{3}}\begin{pmatrix}1\\ -1\\ 1\end{pmatrix},"
    r"\boldsymbol{\gamma}_{2}=\dfrac{1}{\sqrt{2}}\begin{pmatrix}-1\\ 0\\ 1\end{pmatrix},"
    r"\boldsymbol{\gamma}_{3}=\dfrac{1}{\sqrt{6}}\begin{pmatrix}1\\ 2\\ 1\end{pmatrix}$，",
    r"故正交矩阵为 $\boldsymbol{Q}=\begin{pmatrix}\dfrac{1}{\sqrt{3}}&-\dfrac{1}{\sqrt{2}}&\dfrac{1}{\sqrt{6}}\\ "
    r"-\dfrac{1}{\sqrt{3}}&0&\dfrac{2}{\sqrt{6}}\\ \dfrac{1}{\sqrt{3}}&\dfrac{1}{\sqrt{2}}&\dfrac{1}{\sqrt{6}}\end{pmatrix}$.",
])

A[22] = (r"(1)\ \dfrac{4}{9};\ (2)\ f_{Z}(z)=z\ (0\leqslant z<1),\ z-2\ (2\leqslant z<3),\ 0\ (\text{其他})", [
    r"【解析】",
    r"(1)$E(Y)=\displaystyle\int_{-\infty}^{+\infty}yf_{Y}(y)dy=\int_{0}^{1}y\cdot 2ydy=2\cdot\dfrac{1}{3}=\dfrac{2}{3}$",
    r"$P\left[Y\leqslant E(Y)\right]=P\left(Y\leqslant\dfrac{2}{3}\right)"
    r"=\displaystyle\int_{-\infty}^{\frac{2}{3}}f_{Y}(y)dy=\int_{0}^{\frac{2}{3}}2ydy=\dfrac{4}{9}.$",
    r"(2)求 $Z$ 的分布函数",
    r"$F_{Z}(z)=P(Z\leqslant z)=P(X+Y\leqslant z)$",
    r"$=P(x=0)P\left(X+Y\leqslant z|X=0\right)+P(x=2)P\left(X+Y\leqslant z|X=2\right)$",
    r"$=\dfrac{1}{2}\left[P(Y\leqslant z)+P(Y\leqslant z-2)\right]$",
    r"当 $Z<0$ 时, $F_{Z}(z)=0$",
    r"当 $0\leqslant Z<1$ 时, $F_{Z}(z)=\dfrac{1}{2}\displaystyle\int_{0}^{z}2ydy=\dfrac{1}{2}z^{2}$",
    r"当 $1\leqslant Z<2$ 时, $F_{Z}(z)=\dfrac{1}{2}$",
    r"当 $2\leqslant Z<3$ 时, $F_{Z}(z)=\dfrac{1}{2}\left(\displaystyle\int_{0}^{z-2}2ydy+1\right)"
    r"=\dfrac{1}{2}\left(z^{2}-4z+5\right)$",
    r"当 $z\geqslant 3$ 时, $F_{Z}(z)=1$",
    r"故 $F_{Z}(z)=\begin{cases}0, z<0\\ \dfrac{1}{2}z^{2}, 0\leqslant z<1\\ \dfrac{1}{2}, 1\leqslant z<2\\ "
    r"\dfrac{1}{2}\left(z^{2}-4z+5\right), 2\leqslant z<3\\ 1, z\geqslant 3\end{cases}$，"
    r"则 $f_{z}(z)=\begin{cases}0, z<0\\ z, 0\leqslant z<1\\ 0, 1\leqslant z<2\\ z-2, 2\leqslant z<3\\ 0, z\geqslant 3\end{cases}$",
    r"整理得：$f_{z}(z)=\begin{cases}z, 0\leqslant z<1\\ z-2, 2\leqslant z<3\\ 0, \text{其他}\end{cases}$.",
])

A[23] = (r"(1)\ f(z)=\dfrac{2}{\sqrt{2\pi}\sigma}e^{-\frac{z^{2}}{2\sigma^{2}}}\ (z\geqslant 0);\ "
         r"(2)\ \hat{\sigma}=\sqrt{\dfrac{\pi}{2}}\ \overline{Z};\ (3)\ \hat{\sigma}=\sqrt{\dfrac{1}{n}\sum\limits_{i=1}^{n}Z_{i}^{2}}", [
    r"【解析】",
    r"(1)因为 $X_{i}$ 服从 $N\left(\mu,\sigma^{2}\right)$,$Y_{i}=X_{i}-\mu$ 服从 $N\left(0,\sigma^{2}\right)$,对应的概率密度为",
    r"$f_{Y}(y)=\dfrac{1}{\sqrt{2\pi}\sigma}e^{-\frac{y^{2}}{2\sigma^{2}}}$,设 $Z_{i}$ 的分布函数为 $F(z)$；",
    r"当 $z<0$ 时, $F(z)=0$；",
    r"当 $z\geqslant 0$ 时, $F(z)=P\left\{Z_{i}\leqslant z\right\}=P\left\{\left|Y_{i}\right|\leqslant z\right\}"
    r"=P\left\{-z\leqslant Y_{i}\leqslant z\right\}=\displaystyle\int_{-z}^{z}\dfrac{1}{\sqrt{2\pi}\sigma}e^{-\frac{y^{2}}{2\sigma^{2}}}dy$；",
    r"则 $Z_{i}$ 的概率密度为 $f(z)=F'(z)=\begin{cases}\dfrac{2}{\sqrt{2\pi}\sigma}e^{-\frac{z^{2}}{2\sigma^{2}}}, z\geqslant 0\\ "
    r"0, z<0\end{cases}$；",
    r"(2)因为 $EZ_{i}=\displaystyle\int_{0}^{+\infty}z\dfrac{2}{\sqrt{2\pi}\sigma}e^{-\frac{z^{2}}{2\sigma^{2}}}dz=\dfrac{2\sigma}{\sqrt{2\pi}}$,"
    r"所以 $\sigma=\sqrt{\dfrac{\pi}{2}}EZ_{i}$,令 $\overline{Z}=\dfrac{1}{n}\sum\limits_{i=1}^{n}Z_{i}$，则 $\sigma$ 的矩估计量为",
    r"$\hat{\sigma}=\sqrt{\dfrac{\pi}{2}}\displaystyle\sum_{i=1}^{n}Z_{i}=\sqrt{\dfrac{\pi}{2}}\overline{Z}$",
    r"由题知对应的似然函数为 $L\left(z_{1},z_{2},\cdots z_{n};\sigma\right)=\displaystyle\prod_{i=1}^{n}\sqrt{\dfrac{2}{\pi}}\dfrac{1}{\sigma}"
    r"e^{-\frac{z_{i}^{2}}{2\sigma^{2}}}=\left(\sqrt{\dfrac{2}{\pi}}\right)^{n}\left(\dfrac{1}{\sigma}\right)^{n}"
    r"e^{-\frac{1}{2\sigma^{2}}\sum\limits_{i=1}^{n}z_{i}^{2}}$,取对数得: "
    r"$\ln L=n\ln\sqrt{\dfrac{2}{\pi}}-n\ln\sigma-\dfrac{1}{2\sigma^{2}}\sum\limits_{i=1}^{n}\left(z_{i}^{2}\right)$,",
    r"令 $\dfrac{d\ln L(\sigma)}{d\sigma}=-\dfrac{n}{\sigma}+\dfrac{\sum\limits_{i=1}^{n}\left(z_{i}^{2}\right)}{\sigma^{3}}=0$，",
    r"得 $\sigma=\sqrt{\dfrac{1}{n}\sum\limits_{i=1}^{n}z_{i}^{2}}$,所以 $\sigma$ 的最大似然估计量为 "
    r"$\hat{\sigma}=\sqrt{\dfrac{1}{n}\sum\limits_{i=1}^{n}Z_{i}^{2}}$.",
])
