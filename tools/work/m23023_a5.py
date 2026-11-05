# -*- coding: utf-8 -*-
"""2023 数学二 答案解析（视觉转录自 p9）。本文件：第 (15)(16) 题。"""

A = {}

A[15] = (r"\dfrac{1}{2}", [
    r"$\displaystyle\int_{1}^{3}f(x)\mathrm{d}x=\int_{1}^{2}f(x)\mathrm{d}x+\int_{2}^{3}f(x)\mathrm{d}x=\int_{1}^{2}f(x)\mathrm{d}x+\int_{0}^{1}f(x+2)\mathrm{d}(x+2)$",
    r"$=\displaystyle\int_{1}^{2}f(x)\mathrm{d}x+\int_{0}^{1}f(x+2)\mathrm{d}(x)=\int_{1}^{2}f(x)\mathrm{d}x+\int_{0}^{1}f(x)+x\mathrm{d}x$",
    r"$=\displaystyle\int_{0}^{2}f(x)\mathrm{d}x+\int_{0}^{1}x\mathrm{d}x=\dfrac{1}{2}$",
])

A[16] = ("8", [
    r"已知 $\begin{vmatrix}a&0&1\\ 1&a&1\\ 1&2&a\end{vmatrix}=a^{3}+2-a-2a=4$，即 $a^{3}-3a-2=0$，解得 $a=2$ 或 $a=-1$",
    r"(1) 当 $a=2$ 时，对增广矩阵作初等行变换：",
    r"$\overline{A}=\begin{pmatrix}2&0&1&1\\ 1&2&1&0\\ 1&2&2&0\\ 2&b&0&2\end{pmatrix}\rightarrow\begin{pmatrix}1&2&1&0\\ 0&-4&-1&1\\ 0&0&1&0\\ 0&b&-1&1\end{pmatrix}\rightarrow\begin{pmatrix}1&2&1&0\\ 0&1&\dfrac{1}{4}&-\dfrac{1}{4}\\ 0&0&1&0\\ 0&0&-1-\dfrac{1}{4}b&1+\dfrac{1}{4}b\end{pmatrix}$",
    r"方程组有解，$r(\overline{A})=r(A)$，$b=-4$，则 $\begin{vmatrix}1&a&1\\ 1&2&a\\ a&b&0\end{vmatrix}=a^{3}+b-2a-ab=8$；",
    r"(2) 当 $a=-1$ 时，对增广矩阵作初等行变换：",
    r"$\overline{A}=\begin{pmatrix}-1&0&1&1\\ 1&-1&1&0\\ 1&2&-1&0\\ -1&b&0&2\end{pmatrix}\rightarrow\begin{pmatrix}1&0&-1&-1\\ 0&-1&2&1\\ 0&2&0&1\\ 0&b&-1&1\end{pmatrix}\rightarrow\begin{pmatrix}1&0&-1&-1\\ 0&1&-2&-1\\ 0&0&4&3\\ 0&0&2b-1&b+1\end{pmatrix}$",
    r"方程组有解，$r(\overline{A})=r(A)$，$b=\dfrac{7}{2}$，则 $\begin{vmatrix}1&a&1\\ 1&2&a\\ a&b&0\end{vmatrix}=a^{3}+b-2a-ab=8$；",
    r"综上所述，行列式 $\begin{vmatrix}1&a&1\\ 1&2&a\\ a&b&0\end{vmatrix}=8$。",
])
