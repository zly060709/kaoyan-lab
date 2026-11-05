# -*- coding: utf-8 -*-
"""2023 数学三 解析 第 9 页：题 15-16"""

A = {}

A[15] = ("8", [
    r"【答案】8。",
    r"【解析】由 $\begin{vmatrix}a&0&1\\ 1&a&1\\ 1&2&a\end{vmatrix}=4$ 可得 $a=-1,a=2$",
    r"当 $a=-1$，由方程有解可得 $b=\dfrac{7}{2}$，进而可得 $\begin{vmatrix}1&a&1\\ 1&2&a\\ a&b&0\end{vmatrix}=\begin{vmatrix}1&-1&1\\ 1&2&-1\\ -1&\dfrac{7}{2}&0\end{vmatrix}=8$，",
    r"当 $a=2$，由方程有解可得 $b=-4$，进而可得 $\begin{vmatrix}1&a&1\\ 1&2&a\\ a&b&0\end{vmatrix}=\begin{vmatrix}1&2&1\\ 1&2&2\\ 2&-4&0\end{vmatrix}=8$。",
])

A[16] = (r"-\dfrac{1}{3}", [
    r"【答案】$-\dfrac{1}{3}$。",
    r"【解析】根据相关系数的计算公式知 $\rho=\dfrac{\mathrm{Cov}(X+Y,X-Y)}{\sqrt{D(X+Y)}\sqrt{D(X-Y)}}$，",
    r"其中 $\mathrm{Cov}(X+Y,X-Y)=\mathrm{Cov}(X,X)-\mathrm{Cov}(Y,Y)=D(X)-D(Y)=-p(1-p)$，",
    r"$D(X+Y)=D(X-Y)=D(X)+D(Y)=3p(1-p)$。",
    r"代入 $\rho=\dfrac{\mathrm{Cov}(X+Y,X-Y)}{\sqrt{D(X+Y)}\sqrt{D(X-Y)}}$ 中得，$\rho=-\dfrac{1}{3}$。",
])
