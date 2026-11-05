# -*- coding: utf-8 -*-
"""2011 数学三 解析 填空题 9-14（原卷 p7-p8，逐字照录）"""

A = {}

A[9] = (r"(1+3x)e^{3x}", [
    r"【答案】$(1+3x)e^{3x}$",
    r"【解析】$f(x)=\lim\limits_{t\to0}x(1+3t)^{\frac{x}{t}}"
    r"=x\lim\limits_{t\to0}\left[(1+3t)^{\frac{1}{3t}}\right]^{3x}=xe^{3x}$，"
    r"则 $f'(x)=(1+3x)e^{3x}$",
])

A[10] = (r"(2\ln2+1)dx+(-2\ln2-1)dy", [
    r"【答案】$(2\ln2+1)\mathrm{d}x+(-2\ln2-1)\mathrm{d}y$",
    r"【解析】$\mathrm{d}z=\dfrac{\partial z}{\partial x}\mathrm{d}x+\dfrac{\partial z}{\partial y}\mathrm{d}y"
    r"=(2\ln2+1)\mathrm{d}x-(2\ln2+1)\mathrm{d}y$",
    r"$\dfrac{\partial z}{\partial x}\Big|_{\substack{x=1\\y=1}}"
    r"=\left(1+\dfrac{x}{y}\right)^{\frac{x}{y}}\left[\dfrac{1}{y}\ln\left(1+\dfrac{x}{y}\right)"
    r"+\dfrac{x}{y}\cdot\dfrac{1}{1+\dfrac{x}{y}}\cdot\dfrac{1}{y}\right]\Bigg|_{\substack{x=1\\y=1}}"
    r"=2\ln2+1$，",
    r"$\dfrac{\partial z}{\partial y}\Big|_{\substack{x=1\\y=1}}"
    r"=\left(1+\dfrac{x}{y}\right)^{\frac{x}{y}}\left[-\dfrac{x}{y^{2}}\ln\left(1+\dfrac{x}{y}\right)"
    r"+\dfrac{x}{y}\cdot\dfrac{1}{1+\dfrac{x}{y}}\cdot\left(-\dfrac{x}{y^{2}}\right)\right]\Bigg|_{\substack{x=1\\y=1}}"
    r"=-1-2\ln2$.",
])

A[11] = (r"y=-2x", [
    r"【答案】$y=-2x$",
    r"【解析】等式两边同时求导数，$\sec^{2}\left(x+y+\dfrac{\pi}{4}\right)(1+y')=e^{y}y'$，"
    r"代入 $(0,0)$ 得到 $y'(0)=-2$，",
    r"所以切线方程为 $y=-2x$.",
])

A[12] = (r"\dfrac{4}{3}\pi", [
    r"【答案】$\dfrac{4}{3}\pi$",
    r"【解析】$V=\int_{1}^{2}\pi y^{2}dx=\int_{1}^{2}\pi(x-1)^{2}dx=\dfrac{4}{3}\pi$.",
])

A[13] = (r"3y_1^2", [
    r"【答案】$3y_{1}^{2}$.",
    r"【解析】由 $\boldsymbol{A}$ 的各行元素之和为 3，得 "
    r"$\boldsymbol{A}\begin{pmatrix}1\\1\\1\end{pmatrix}=3\begin{pmatrix}1\\1\\1\end{pmatrix}$，"
    r"从而 3 为其特征值.",
    r"因为 $r(\boldsymbol{A})=1$，故 $\boldsymbol{A}$ 的特征值为 0、0、1.",
    r"因此 $f$ 在正交变换 $\boldsymbol{x}=\boldsymbol{Qy}$ 下的标准形为 $3y_{1}^{2}$.",
])

A[14] = (r"\mu(\mu^2+\sigma^2)", [
    r"【答案】$\mu(\mu^{2}+\sigma^{2})$",
    r"【解析】由题知 $X$ 与 $Y$ 的相关系数 $\rho_{XY}=0$，即 $X$ 与 $Y$ 不相关.",
    r"当 $(X,Y)$ 服从二维正态分布，$X$ 与 $Y$ 不相关 $\Leftrightarrow$ $X$ 与 $Y$ 独立",
    r"所以 $X$ 与 $Y$ 独立，则有",
    r"$EX=EY=\mu,DX=DY=\sigma^{2}$",
    r"$EY^{2}=DY+(EY)^{2}=\mu^{2}+\sigma^{2}$",
    r"$E\left(XY^{2}\right)=EXEY^{2}=\mu\left(\mu^{2}+\sigma^{2}\right)$.",
])
