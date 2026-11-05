# -*- coding: utf-8 -*-
"""2023 数学三 解析 第 12 页：题 21"""

A = {}

A[21] = (r"A=\begin{pmatrix}1&1&1\\ 2&-1&1\\ 0&1&-1\end{pmatrix},\ P=\begin{pmatrix}0&-1&4\\ -1&0&3\\ 1&2&1\end{pmatrix},\ \Lambda=\begin{pmatrix}-2&&\\ &-1&\\ &&2\end{pmatrix}", [
    r"【答案】(1) $A=\begin{pmatrix}1&1&1\\ 2&-1&1\\ 0&1&-1\end{pmatrix}$",
    r"(2) 可逆矩阵 $P=\begin{pmatrix}0&-1&4\\ -1&0&3\\ 1&2&1\end{pmatrix}$，对角阵 $\Lambda=\begin{pmatrix}-2&&\\ &-1&\\ &&2\end{pmatrix}$。",
    r"【解析】(1) 由题设 $A\begin{pmatrix}x_1\\ x_2\\ x_3\end{pmatrix}=\begin{pmatrix}x_1+x_2+x_3\\ 2x_1-x_2+x_3\\ x_2-x_3\end{pmatrix}=\begin{pmatrix}1&1&1\\ 2&-1&1\\ 0&1&-1\end{pmatrix}\begin{pmatrix}x_1\\ x_2\\ x_3\end{pmatrix}$",
    r"故 $A=\begin{pmatrix}1&1&1\\ 2&-1&1\\ 0&1&-1\end{pmatrix}$。",
    r"(2) 由 $|A-\lambda E|=\begin{vmatrix}1-\lambda&1&1\\ 2&-1-\lambda&1\\ 0&1&-1-\lambda\end{vmatrix}=(\lambda+2)(\lambda+1)(2-\lambda)=0$ 得：",
    r"$\lambda_1=-2,\ \lambda_2=-1,\ \lambda_3=2$；",
    r"当 $\lambda_1=-2$ 时，解方程组 $(A-\lambda_1 E)x=0$ 得特征向量 $\boldsymbol{\xi}_1=(0,-1,1)^{\mathrm{T}}$；",
    r"当 $\lambda_2=-1$ 时，解方程组 $(A-\lambda_2 E)x=0$ 得特征向量 $\boldsymbol{\xi}_2=(-1,0,2)^{\mathrm{T}}$；",
    r"当 $\lambda_3=2$ 时，解方程组 $(A-\lambda_3 E)x=0$ 得特征向量 $\boldsymbol{\xi}_3=(4,3,1)^{\mathrm{T}}$；",
    r"则存在可逆矩阵 $P=(\boldsymbol{\xi}_1,\boldsymbol{\xi}_2,\boldsymbol{\xi}_3)=\begin{pmatrix}0&-1&4\\ -1&0&3\\ 1&2&1\end{pmatrix}$，使得 $P^{-1}AP=\Lambda=\begin{pmatrix}-2&&\\ &-1&\\ &&2\end{pmatrix}$。",
])
