# -*- coding: utf-8 -*-
"""2023 数学三 解析 第 6 页：题 4-6"""

A = {}

A[4] = ("A", [
    r"【答案】（A）",
    r"【解析】因级数 $\sum\limits_{n=1}^{+\infty}a_n$，$\sum\limits_{n=1}^{+\infty}b_n$ 均收敛，且 $a_n<b_n$，则级数 $\sum\limits_{n=1}^{+\infty}(b_n-a_n)$ 也收敛，且 $b_n-a_n>0$，",
    r"故 $\sum\limits_{n=1}^{+\infty}(b_n-a_n)$ 为正项级数，因此 $\sum\limits_{n=1}^{+\infty}(b_n-a_n)$ 绝对收敛，即 $\sum\limits_{n=1}^{+\infty}|b_n-a_n|$ 收敛。",
    r"又因 $|b_n|=|(b_n-a_n)+a_n|\leqslant|b_n-a_n|+|a_n|$，其中 $\sum\limits_{n=1}^{+\infty}|b_n-a_n|$ 已收敛，故当 $\sum\limits_{n=1}^{+\infty}a_n$ 绝对收敛，即 $\sum\limits_{n=1}^{+\infty}|a_n|$ 收敛时，$\sum\limits_{n=1}^{+\infty}|b_n|$ 也收敛，因此，「$\sum\limits_{n=1}^{+\infty}a_n$ 绝对收敛」是「$\sum\limits_{n=1}^{+\infty}b_n$ 绝对收敛」的充分条件。",
    r"同理，$|a_n|=|b_n-(b_n-a_n)|\leqslant|b_n|+|b_n-a_n|$，其中 $\sum\limits_{n=1}^{+\infty}|b_n-a_n|$ 已收敛，故当 $\sum\limits_{n=1}^{+\infty}b_n$ 绝对收敛，即 $\sum\limits_{n=1}^{+\infty}|b_n|$ 收敛时，$\sum\limits_{n=1}^{+\infty}|a_n|$ 也收敛，因此，「$\sum\limits_{n=1}^{+\infty}a_n$ 绝对收敛」是「$\sum\limits_{n=1}^{+\infty}b_n$ 绝对收敛」的必要条件。",
    r"综所述，得出选项（A）。",
])

A[5] = ("B", [
    r"【答案】（B）",
    r"【解析】由伴随矩阵的公式可知：$M^{*}=|M|\cdot M^{-1}$，所以",
    r"$\begin{pmatrix}A&E\\ O&B\end{pmatrix}^{*}=\begin{pmatrix}A&E\\ O&B\end{pmatrix}^{-1}\cdot\begin{vmatrix}A&E\\ O&B\end{vmatrix}=\begin{pmatrix}A^{-1}&-A^{-1}B^{-1}\\ O&B^{-1}\end{pmatrix}\cdot|A||B|=\begin{pmatrix}|B|A^{*}&-A^{*}B^{*}\\ O&|A|B^{*}\end{pmatrix}$",
    r"因此答案选（B）",
])

A[6] = ("B", [
    r"【答案】B",
    r"【解析】$f(x_1,x_2,x_3)=(x_1+x_2)^{2}+(x_1+x_3)^{2}-4(x_2-x_3)^{2}$",
    r"$=2x_1^{2}-3x_2^{2}-3x_3^{2}+2x_1x_2+2x_1x_3+8x_2x_3$",
    r"所以 $A=\begin{pmatrix}2&1&1\\ 1&-3&4\\ 1&4&-3\end{pmatrix}$，$|A-\lambda E|=\begin{vmatrix}2-\lambda&1&1\\ 1&-3-\lambda&4\\ 1&4&-3-\lambda\end{vmatrix}=0$，",
    r"解得：特征值为 $0,3,-7$，所以规范型前系数为 $0,1,-1$，因此选（B）",
])
