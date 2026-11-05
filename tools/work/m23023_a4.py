# -*- coding: utf-8 -*-
"""2023 数学二 答案解析（视觉转录自 p7-p8）。本文件：第 (10)~(14) 题。"""

A = {}

A[10] = ("D", [
    r"易知，$\alpha_{1}$、$\alpha_{2}$ 线性无关，$\beta_{1}$、$\beta_{2}$ 线性无关，由 $\begin{vmatrix}1&2&1\\ 2&1&5\\ 3&1&8\end{vmatrix}=0,\begin{vmatrix}2&1&1\\ 5&0&5\\ 9&1&8\end{vmatrix}=0$ 可知，",
    r"$\gamma$ 可由 $\alpha_{1}$、$\alpha_{2}$ 线性表示，也可由 $\beta_{1}$、$\beta_{2}$ 线性表示，故选（D）。",
])

A[11] = ("-2", [
    r"由已知 $\lim\limits_{x\to 0}\dfrac{f(x)}{g(x)}=\lim\limits_{x\to 0}\dfrac{ax+bx^{2}+\ln(1+x)}{\mathrm{e}^{x^{2}}-\cos x}=1$",
    r"泰勒展开得 $\lim\limits_{x\to 0}\dfrac{ax+bx^{2}+x-\dfrac{1}{2}x^{2}+o(x^{2})}{1+x^{2}+o(x^{2})-\left[1-\dfrac{1}{2}x^{2}+o(x^{2})\right]}=\lim\limits_{x\to 0}\dfrac{(a+1)x+(b-\dfrac{1}{2})x^{2}+o(x^{2})}{\dfrac{3}{2}x^{2}+o(x^{2})}=1$",
    r"则 $a+1=0$，$b-\dfrac{1}{2}=\dfrac{3}{2}$，即 $a=-1$，$b=2$",
    r"故 $ab=-2$。",
])

A[12] = (r"\dfrac{4\pi}{3}+\sqrt{3}", [
    r"$S=\displaystyle\int_{-\sqrt{3}}^{\sqrt{3}}\sqrt{1+\left[y'(x)\right]^{2}}\mathrm{d}x=2\int_{0}^{\sqrt{3}}\sqrt{1+3-x^{2}}\mathrm{d}x=2\int_{0}^{\sqrt{3}}\sqrt{4-x^{2}}\mathrm{d}x$",
    r"$\xlongequal{x=2\sin u}2\displaystyle\int_{0}^{\frac{\pi}{3}}4\cos^{2}u\mathrm{d}u=4\int_{0}^{\frac{\pi}{3}}(1+\cos 2u)\mathrm{d}u=4\left(u+\dfrac{1}{2}\sin 2u\Big|_{0}^{\frac{\pi}{3}}\right)=\dfrac{4\pi}{3}+\sqrt{3}$。",
])

A[13] = (r"-\dfrac{3}{2}", [
    r"$x=1,y=1$ 时，得到 $z=0$",
    r"等式两边对 $x$ 求偏导，$\mathrm{e}^{z}z_{x}'+z+xz_{x}'=2$，代入 $x=1,y=1$，$z=0$ 得到 $z_{x}'|_{(1,1)}=1$",
    r"等式两边继续对 $x$ 求偏导 $e^{z}(z_{x}')^{2}+e^{z}z_{x}''+z_{x}'+z_{x}'+xz_{x}''=0$",
    r"代入 $x=1,y=1$，$z=0$，$z_{x}'|_{(1,1)}=1$，得到 $\dfrac{\partial^{2}z}{\partial x^{2}}\Big|_{(1,1)}=-\dfrac{3}{2}$。",
])

A[14] = (r"-\dfrac{11}{9}", [
    r"$9x^{2}=6y^{2}y'+5y^{4}y'$，当 $x=1$ 时，$y=1$，所以 $y'=\dfrac{9}{11}$，则法线斜率为 $-\dfrac{11}{9}$。",
])
