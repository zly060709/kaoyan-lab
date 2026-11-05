# -*- coding: utf-8 -*-
"""2022 数学二 答案解析 填空题（p7-p8）。"""

A = {}

A[11] = (r"$\mathrm{e}^{\frac{1}{2}}$", [
    r"【解析】$\displaystyle\lim_{x\to 0}\left(\dfrac{1+\mathrm{e}^{x}}{2}\right)^{\cot x}=\lim_{x\to 0}\left(1+\dfrac{\mathrm{e}^{x}-1}{2}\right)^{\cot x}=\mathrm{e}^{\lim\limits_{x\to 0}\dfrac{\cos x(\mathrm{e}^{x}-1)}{2\sin x}}=\mathrm{e}^{\frac{1}{2}}$。",
])

A[12] = (r"$-\dfrac{31}{32}$", [
    r"【解析】同时对原等式两端求导：$2x+y+xy'+3y^{2}y'=0$；",
    r"再次求导：$2+2y'+xy''+6y(y')^{2}+3y^{2}y''=0$，",
    r"当 $x=1$ 时 $y=1$，$y'=-\dfrac{3}{4}$，$y''(1)=-\dfrac{31}{32}$。",
])

A[13] = (r"$\dfrac{8\sqrt{3}\pi}{9}$", [
    r"【解析】$\displaystyle\int_{0}^{1}\dfrac{2x+3}{x^{2}-x+1}\mathrm{d}x=\int_{0}^{1}\dfrac{2x-1}{x^{2}-x+1}\mathrm{d}x+4\int_{0}^{1}\dfrac{1}{x^{2}-x+1}\mathrm{d}x$",
    r"$=\ln\left|x^{2}-x+1\right|\big|_{0}^{1}+4\displaystyle\int_{0}^{1}\dfrac{1}{\left(x-\dfrac{1}{2}\right)^{2}+\dfrac{3}{4}}\mathrm{d}x=\dfrac{8}{\sqrt{3}}\arctan\dfrac{2x-1}{\sqrt{3}}\big|_{0}^{1}=\dfrac{8\sqrt{3}\pi}{9}$。",
])

A[14] = (r"$y=C_{1}+\mathrm{e}^{x}\left(C_{2}\sin 2x+C_{3}\cos 2x\right)$，$C_{1},C_{2},C_{3}$ 为任意常数", [
    r"【解析】微分方程对应特征方程为：$\lambda^{3}-2\lambda^{2}+5\lambda=0$。可得特征值为 $\lambda_{1}=0,\lambda_{2,3}=1\pm 2i$。",
    r"所以原方程的通解为：$y=C_{1}+\mathrm{e}^{x}\left(C_{2}\sin 2x+C_{3}\cos 2x\right)$，$C_{1},C_{2},C_{3}$ 为任意常数。",
])

A[15] = (r"$\dfrac{\pi}{12}$", [
    r"【解析】$S=\dfrac{1}{2}\displaystyle\int_{0}^{\frac{\pi}{3}}\sin^{2}3\theta\mathrm{d}\theta=\dfrac{1}{2}\cdot\dfrac{1}{3}\int_{0}^{\pi}\sin^{2}\theta\mathrm{d}\theta=\dfrac{\pi}{12}$。",
])

A[16] = ("$-1$", [
    r"【解析】$\begin{pmatrix}1&0&0\\ 0&0&1\\ 0&1&0\end{pmatrix}\boldsymbol{A}\begin{pmatrix}1&0&0\\ -1&1&0\\ 0&0&1\end{pmatrix}=\begin{pmatrix}-2&1&-1\\ 1&-1&0\\ -1&0&0\end{pmatrix}$，",
    r"则 $\boldsymbol{A}^{-1}=\begin{pmatrix}1&0&0\\ -1&1&0\\ 0&0&1\end{pmatrix}\begin{pmatrix}-2&1&-1\\ 1&-1&0\\ -1&0&0\end{pmatrix}^{-1}\begin{pmatrix}1&0&0\\ 0&0&1\\ 0&1&0\end{pmatrix}=\begin{pmatrix}0&-1&0\\ 0&0&-1\\ -1&1&-1\end{pmatrix}$",
    r"故 $\mathrm{tr}(\boldsymbol{A}^{-1})=-1$",
])
