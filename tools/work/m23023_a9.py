# -*- coding: utf-8 -*-
"""2023 数学二 答案解析（视觉转录自 p12-p13）。本文件：第 (22) 题。"""

A = {}

A[22] = (r"(1) $A=\begin{pmatrix}1&1&1\\ 2&-1&1\\ 0&1&-1\end{pmatrix}$ (2) $P=\begin{pmatrix}4&1&0\\ 3&0&1\\ 1&-2&-1\end{pmatrix}$ $\Lambda=\begin{pmatrix}2& &\\ &-1&\\ & &-2\end{pmatrix}$", [
    r"(1) 由矩阵的运算规律可知，$A=\begin{pmatrix}1&1&1\\ 2&-1&1\\ 0&1&-1\end{pmatrix}$；",
    r"(2) 令 $|\lambda E-A|=0$，$\begin{vmatrix}\lambda-1&-1&-1\\ -2&\lambda+1&-1\\ 0&-1&\lambda+1\end{vmatrix}=(\lambda-2)(\lambda+1)(\lambda+2)=0$",
    r"得矩阵 $A$ 的特征值为 $\lambda_{1}=2,\lambda_{2}=-1,\lambda_{3}=-2$。",
    r"解方程 $(\lambda_{i}E-A)\boldsymbol{x}=0$ 得矩阵 $A$ 对应的特征向量为 $\alpha_{1}=(4,3,1)^{\mathrm{T}},\alpha_{2}=(1,0,-2)^{\mathrm{T}},\alpha_{3}=(0,1,-1)^{\mathrm{T}}$。",
    r"可得 $P=\begin{pmatrix}4&1&0\\ 3&0&1\\ 1&-2&-1\end{pmatrix}$，$\Lambda=\begin{pmatrix}2& &\\ &-1&\\ & &-2\end{pmatrix}$，使得 $P^{-1}AP=\Lambda$。",
])
