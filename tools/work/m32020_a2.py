# -*- coding: utf-8 -*-
"""2020 数学三 解析 填空题 9-14（原卷 p7-p8，逐字照录）"""

A = {}

A[9] = (r"dz|_{(0,\pi)}=(\pi-1)dx-dy", [
    r"（9）【答案】$\left.dz\right|_{(0,\pi)}=(\pi-1)dx-dy$",
    r"【解析】$\dfrac{\partial z}{\partial x}=\dfrac{y+\cos(x+y)}{1+\left[xy+\sin(x+y)\right]^{2}},"
    r"\dfrac{\partial z}{\partial y}=\dfrac{x+\cos(x+y)}{1+\left[xy+\sin(x+y)\right]^{2}}$，"
    r"将 $x=0,y=\pi$ 带入可知，",
    r"$\left.dz\right|_{(0,\pi)}=(\pi-1)dx-dy$",
])

A[10] = (r"y=x-1", [
    r"（10）【答案】$y=x-1$",
    r"【解析】在 $x+y+e^{2xy}=0$ 两侧同时对 $x$ 求导有$1+\dfrac{dy}{dx}+e^{2xy}"
    r"\left(2y+2x\dfrac{dy}{dx}\right)=0$，将",
    r"$x=0,y=-1$ 带入可知$\dfrac{dy}{dx}=1$，所以切线方程为 $y=x-1.$",
])

A[11] = (r"Q=8", [
    r"（11）【答案】$Q=8$",
    r"【解析】由 $Q(p)=\dfrac{800}{P+3}-2$ 可知 $p=\dfrac{800}{Q+2}-3$，则利润函数为",
    r"$L(Q)=\left(\dfrac{800}{Q+2}-3\right)Q-(100+13Q),\quad"
    r"\dfrac{dL(Q)}{dQ}=\dfrac{1600}{\left(Q+2\right)^{2}}-16$，"
    r"令$\dfrac{dL(Q)}{dQ}=0$可得，$Q=8$，",
    r"此时$\dfrac{d^{2}L(Q)}{dQ^{2}}=-\dfrac{3200}{\left(Q+2\right)^{3}}<0$，故取得最大利润.",
])

A[12] = (r"\pi(\ln 2-\dfrac{1}{3})", [
    r"（12）【答案】$\pi(\ln 2-\dfrac{1}{3})$",
    r"【解析】由题意列式得$V=\int_{0}^{1}2\pi x\left(\dfrac{1}{1+x^{2}}-\dfrac{x}{2}\right)dx"
    r"=\pi\left(\ln(1+x^{2})-\dfrac{1}{3}x^{3}\right)\left|\right._{0}^{1}"
    r"=\ \pi(\ln 2-\dfrac{1}{3})\ .$",
])

A[13] = (r"a^{2}(a^{2}-4)", [
    r"（13）【答案】$a^{2}(a^{2}-4).$",
    r"【解析】",
    r"原式$=a\begin{vmatrix}1&1&1&1\\ 0&a&1&-1\\ -1&1&a&0\\ 1&-1&0&a\end{vmatrix}"
    r"=a\begin{vmatrix}1&1&1&1\\ 0&a&1&-1\\ 0&2&a+1&1\\ 0&0&a&a\end{vmatrix}"
    r"=a\begin{vmatrix}a&1&-1\\ 2&a+1&1\\ 0&a&a\end{vmatrix}"
    r"=a^{2}\begin{vmatrix}a&2&-1\\ 2&a&1\\ 0&0&1\end{vmatrix}=a^{2}(a^{2}-4).$",
])

A[14] = (r"\dfrac{8}{7}", [
    r"（14）【答案】$\dfrac{8}{7}$",
    r"【解析】$P\left\{Y=0\right\}=\sum_{n=1}^{\infty}P\left\{X=3n\right\}"
    r"=\sum_{n=1}^{\infty}\dfrac{1}{8^{n}}=\dfrac{1}{7}$",
    r"$P\left\{Y=1\right\}=\sum_{n=0}^{\infty}P\left\{X=3n+1\right\}"
    r"=\sum_{n=0}^{\infty}\dfrac{1}{2}\dfrac{1}{8^{n}}=\dfrac{4}{7}$",
    r"$P\left\{Y=2\right\}=\sum_{n=0}^{\infty}P\left\{X=3n+2\right\}"
    r"=\sum_{n=0}^{\infty}\dfrac{1}{4}\dfrac{1}{8^{n}}=\dfrac{2}{7}$",
    r"所以 $EY=0\times\dfrac{1}{7}+1\times\dfrac{4}{7}+2\times\dfrac{2}{7}=\dfrac{8}{7}.$",
])
