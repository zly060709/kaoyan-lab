# -*- coding: utf-8 -*-
"""2022 数学二 答案解析 续（p7）。"""

A = {}

A[7] = ("A", [
    r"【解析】比较 $I_{1},I_{2}$，令 $f(x)=\dfrac{x}{2}-\ln(1+x),x\in(0,1)$，则",
    r"$f'(x)=\dfrac{1}{2}-\dfrac{1}{1+x}=\dfrac{x-1}{2(1+x)}<0,x\in(0,1)$",
    r"又 $f(0)=0$，所以 $f(x)<f(0)=0$，$I_{1}<I_{2}$；再比较 $I_{2},I_{3}$，",
    r"令 $g(x)=\dfrac{\ln(1+x)}{1+\cos x}-\dfrac{2x}{1+\sin x}=\dfrac{\ln(1+x)(1+\sin x)-2x(1+\cos x)}{(1+\cos x)(1+\sin x)}$，",
    r"$h(x)=\ln(1+x)(1+\sin x)-2x(1+\cos x)=\ln(1+x)-x+\sin x\cdot\ln(1+x)-x-2x\cos x,x\in(0,1)$",
    r"其中 $\ln(1+x)-x<0$，$\sin x\cdot\ln(1+x)-x<0$，$-2x\cos x<0$，则 $I_{2}<I_{3}$，故选（A）",
])

A[8] = ("B", [
    r"【解析】$\boldsymbol{A}$ 有 3 个不同特征值，故 $\boldsymbol{A}$ 一定可以对角化 $\Leftrightarrow$ 存在可逆矩阵 $\boldsymbol{P}$，使得 $\boldsymbol{A}=\boldsymbol{P}\boldsymbol{\Lambda}\boldsymbol{P}^{-1}$。",
])

A[9] = ("D", [
    r"【解析】$|\boldsymbol{A}|=(b-1)(b-a)(a-1)$。当 $b\neq 1$ 且 $a\neq 1$ 且 $b\neq a$ 时，$r(\boldsymbol{A})=r\big(\boldsymbol{A}\big|\boldsymbol{b}\big)=3$ 有唯一解；当 $b=1\big(b\neq 1\big)$ 或 $a=1\big(b\neq 1\big)$ 或 $a=b=1$ 时均有 $r(\boldsymbol{A})<r\big(\boldsymbol{A}\big|\boldsymbol{b}\big)$ 无解。",
])

A[10] = ("C", [
    r"【解析】",
    r"$\big(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}\big)=\begin{pmatrix}\lambda&1&1&1\\ 1&\lambda&1&\lambda\\ 1&1&\lambda&\lambda^{2}\end{pmatrix}\to\begin{pmatrix}1&1&\lambda&\lambda^{2}\\ 0&\lambda-1&1-\lambda&\lambda-\lambda^{2}\\ 0&1-\lambda&1-\lambda^{2}&1-\lambda^{3}\end{pmatrix}$",
    r"$\to\begin{pmatrix}1&1&\lambda&\lambda^{2}\\ 0&\lambda-1&1-\lambda&\lambda-\lambda^{2}\\ 0&0&2-\lambda-\lambda^{2}&1+\lambda-\lambda^{2}-\lambda^{3}\end{pmatrix}$",
    r"已知 $\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}$ 与 $\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{4}$ 等价，则 $r\big(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}\big)=r\big(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{4}\big)=r\big(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}\big)$",
    r"当 $\lambda=-1$ 时，$r\big(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}\big)=3,r\big(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{4}\big)=2$ 与向量组等价矛盾，故 $\lambda\neq-1$",
    r"当 $\lambda=-2$ 时，$r\big(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}\big)=2,r\big(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{4}\big)=3$ 与向量组等价矛盾，故 $\lambda\neq-2$",
    r"故排除（B）（D）；当 $\lambda=2$，$r\big(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}\big)=r\big(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{4}\big)=3$，故排除（A），于是该题选（C）。",
])
