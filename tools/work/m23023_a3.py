# -*- coding: utf-8 -*-
"""2023 数学二 答案解析（视觉转录自 p6-p7）。本文件：第 (6)(7)(8)(9) 题。"""

A = {}

A[6] = ("A", [
    r"$f(\alpha)=\displaystyle\int_{2}^{+\infty}\dfrac{1}{x(\ln x)^{\alpha+1}}\mathrm{d}x$ 收敛，则 $\alpha>0$。",
    r"$f(\alpha)=\displaystyle\int_{2}^{+\infty}\dfrac{1}{x(\ln x)^{\alpha+1}}\mathrm{d}x=-\dfrac{1}{\alpha}(\ln x)^{-\alpha}\Big|_{2}^{+\infty}=\dfrac{1}{\alpha}(\ln 2)^{-\alpha}$。",
    r"$f'(\alpha)=-\dfrac{1}{\alpha^{2}}(\ln 2)^{-\alpha}-\dfrac{1}{\alpha}\ln\ln 2\,(\ln 2)^{-\alpha}$。",
    r"令 $f'(\alpha)=0$，则有唯一驻点 $\alpha=-\dfrac{1}{\ln\ln 2}$，即 $\alpha_{0}=-\dfrac{1}{\ln\ln 2}$，选（A）。",
])

A[7] = ("C", [
    r"$f'(x)=(x^{2}+2x+a)\mathrm{e}^{x}$，$f''(x)=(x^{2}+4x+2+a)\mathrm{e}^{x}$。由于 $f(x)$ 无极值点，所以 $f'(x)\geqslant 0$，即 $x^{2}+2x+a\geqslant 0$，判别式 $\Delta=4-4a\leqslant 0$，解得 $a\geqslant 1$；",
    r"又 $y=f(x)$ 有拐点，所以 $f''(x)$ 有零点，即 $x^{2}+4x+2+a=0$ 有零点，判别式 $\Delta=16-4(a+2)\geqslant 0$，解得 $a\leqslant 2$。",
    r"当 $a=2$ 时，$f''(x)=(x^{2}+4x+4)\mathrm{e}^{x}$ 有唯一零点 $x=-2$，计算得到 $f^{(4)}(-2)=2$，故此时无拐点。",
    r"综上 $a$ 的取值范围是：$[1,2)$，选（C）。",
])

A[8] = ("D", [
    r"由于 $\begin{pmatrix}A&E\\ O&B\end{pmatrix}^{*}=\begin{vmatrix}A&E\\ O&B\end{vmatrix}\begin{pmatrix}A&E\\ O&B\end{pmatrix}^{-1}$，",
    r"而 $\begin{vmatrix}A&E\\ O&B\end{vmatrix}=|A||B|$，$\begin{pmatrix}A&E\\ O&B\end{pmatrix}^{-1}=\begin{pmatrix}A^{-1}&-A^{-1}B^{-1}\\ O&B^{-1}\end{pmatrix}$，$|A|A^{-1}=A^{*}$，$|B|B^{-1}=B^{*}$",
    r"所以 $\begin{pmatrix}A&E\\ O&B\end{pmatrix}^{*}=|A||B|\begin{pmatrix}A^{-1}&-A^{-1}B^{-1}\\ O&B^{-1}\end{pmatrix}=\begin{pmatrix}|A||B|A^{-1}&-|A||B|A^{-1}B^{-1}\\ O&|A||B|B^{-1}\end{pmatrix}=\begin{pmatrix}|B|A^{*}&-A^{*}B^{*}\\ O&|A|B^{*}\end{pmatrix}$，选（D）。",
])

A[9] = ("B", [
    r"$f(x_{1},x_{2},x_{3})=(x_{1}+x_{2})^{2}+(x_{1}+x_{3})^{2}-4(x_{2}-x_{3})^{2}=2x_{1}^{2}-3x_{2}^{2}-3x_{3}^{2}+2x_{1}x_{2}+2x_{1}x_{3}+8x_{2}x_{3}$",
    r"$=2\left(x_{1}+\dfrac{1}{2}x_{2}+\dfrac{1}{2}x_{3}\right)^{2}-\dfrac{7}{2}(x_{2}-x_{3})^{2}$",
    r"由上述配方法可知，该二次型的正、负惯性指数分别为 1，1，所以选（B）。",
])
