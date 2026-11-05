# -*- coding: utf-8 -*-
"""2009 数学三 解析 填空题 9-14（原卷 p7-p8，逐字照录）"""

A = {}

A[9] = (r"\dfrac{3e}{2}", [
    r"【答案】$\dfrac{3e}{2}$. ",
    r"【解析】$\lim\limits_{x\to0}\dfrac{e-e^{\cos x}}{\sqrt[3]{1+x^{2}}-1}"
    r"=\lim\limits_{x\to0}\dfrac{e\left(1-e^{\cos x-1}\right)}{\sqrt[3]{1+x^{2}}-1}"
    r"=\lim\limits_{x\to0}\dfrac{-e(\cos x-1)}{\dfrac{x^{2}}{3}}"
    r"=\lim\limits_{x\to0}\dfrac{e\cdot\dfrac{x^{2}}{2}}{\dfrac{x^{2}}{3}}=\dfrac{3e}{2}$",
])

A[10] = ("2\\ln 2+1", [
    r"【答案】$2\ln2+1$. ",
    r"【解析】由 $z=(x+e^{y})^{x}$，故 $z(x,0)=(x+1)^{x}$",
    r"$\dfrac{\partial z}{\partial x}\Big|_{y=0}=[(x+1)^{x}]'=[e^{x\ln(1+x)}]'"
    r"=e^{x\ln(1+x)}\left[\ln(1+x)+\dfrac{x}{1+x}\right]$",
    r"代入 $x=1$ 得，$\dfrac{\partial z}{\partial x}\Big|_{(1,0)}=e^{\ln2}\left(\ln2+\dfrac{1}{2}\right)=2\ln2+1$. ",
])

A[11] = (r"\dfrac{1}{e}", [
    r"【答案】$\dfrac{1}{e}$",
    r"【解析】由题意知，$a_{n}=\dfrac{e^{n}-(-1)^{n}}{n^{2}}>0$",
    r"$\left|\dfrac{a_{n+1}}{a_{n}}\right|=\dfrac{e^{n+1}-(-1)^{n+1}}{(n+1)^{2}}\cdot\dfrac{n^{2}}{e^{n}-(-1)^{n}}"
    r"=\dfrac{n^{2}}{(n+1)^{2}}\cdot\dfrac{e^{n+1}\left[1-\left(-\dfrac{1}{e}\right)^{n+1}\right]}"
    r"{e^{n}\left[1-\left(-\dfrac{1}{e}\right)^{n+1}\right]}\to e\,(n\to\infty)$",
    r"所以，该幂级数的收敛半径为 $\dfrac{1}{e}$. ",
])

A[12] = ("8000", [
    r"【答案】8000",
    r"【解析】由题意知 $\varepsilon=-\dfrac{P}{Q}\dfrac{dQ}{dP}=0.2$，收益函数为 $R=PQ(P)$，收益微分为",
    r"$dR=PdQ+QdP=Q(1-\varepsilon)dP$ 代入得 $dR=8000$. ",
])

A[13] = ("2", [
    r"【答案】2. ",
    r"【解析】$\boldsymbol{\alpha}\boldsymbol{\beta}^{T}$ 相似于 $\begin{pmatrix}3&0&0\\0&0&0\\0&0&0\end{pmatrix}$，"
    r"根据相似矩阵有相同的特征值，得到 $\boldsymbol{\alpha}\boldsymbol{\beta}^{T}$ 的特征值为 $3,0,0$. ",
    r"而 $\boldsymbol{\alpha}^{T}\boldsymbol{\beta}$ 为矩阵 $\boldsymbol{\alpha}\boldsymbol{\beta}^{T}$ 的对角元素之和，"
    r"所以 $1+k=3+0+0,\therefore k=2$. ",
])

A[14] = ("np^2", [
    r"【答案】$np^{2}$. ",
    r"【解析】由 $ET=E(\overline{X}-S^{2})=E\overline{X}-ES^{2}=np-np(1-p)=np^{2}$. ",
])
