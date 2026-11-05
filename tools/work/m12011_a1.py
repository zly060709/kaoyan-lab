# -*- coding: utf-8 -*-
"""2011 数学一 解析 选择题 1-8（原卷 p5-p6，逐字照录【答案】【解析】；本卷解析标签为【解析】）"""

A = {}

A[1] = ("C", [
    r"【答案】(C)",
    r"【解析】法一：在区间[1,2]上，$\dfrac{f(1)+f(2)}{2}=0, f\left(\dfrac{1+2}{2}\right)<0$，$f(x)$ 为凹函数；",
    r"在区间[2,3]上，$\dfrac{f(2)+f(3)}{2}=0, f\left(\dfrac{2+3}{2}\right)<0$，$f(x)$ 为凹函数；",
    r"在区间[3,4]上，$\dfrac{f(3)+f(4)}{2}=0, f\left(\dfrac{3+4}{2}\right)>0$，$f(x)$ 为凸函数.",
    r"在点 $(3,0)$ 左右函数凹凸性发生改变，所以点 $(3,0)$ 为拐点.",
    r"法二：原函数可看成 $y=p(x)(x-3)^{3}$. 经计算可得 $y''(3)=0,y'''(3)\neq0$，所以 $(3,0)$ 是曲线"
    r"的拐点. 其他点不能满足充分条件.",
])

A[2] = ("C", [
    r"【答案】(C)",
    r"【解析】根据部分和数列无界，所以级数 $\sum\limits_{k=1}^{\infty}a_{k}$ 发散，可知 $\sum\limits_{k=1}^{\infty}a_{k}x^{k}$ 在 $x=1$ 发散；$x=-1$ 时"
    r"为交错级数，根据题意收敛，所以可判断收敛半径为 $R=1$，收敛域是 $[-1,1)$. 所以",
    r"$\sum\limits_{k=1}^{\infty}a_{k}(x-1)^{k}$ 的收敛域为 $\sum\limits_{k=1}^{\infty}a_{k}x^{k}$ 即 $x\in[0,2)$.",
])

A[3] = ("A", [
    r"【答案】(A)",
    r"【解析】由于 $\begin{cases}z'_{x}=f'(x)g(y)=0\\ z'_{y}=f(x)g'(y)=0\end{cases}$，满足",
    r"$z''_{xx}=f''(x)g(y)$, $z''_{yy}=f(x)g''(y)$, $z''_{xy}=f'(x)g'(y)$",
    r"对于点 $(0,0)$",
    r"$A=z''_{xx}(0,0)=f''(0)g(0)$, $B=z''_{xy}=f'(0)g'(0)$, $C=z''_{yy}=f(0)g''(0)$",
    r"已知 $f(0)>0,g(0)<0$，$f'(0)=g'(0)=0$.",
    r"当 $f''(0)<0,g''(0)>0$ 时，$AC-B^{2}>0$ 且 $A>0$，此时 $f(0,0)$ 是极小值.",
])

A[4] = ("B", [
    r"【答案】(B)",
    r"【解析】在区间 $\left(0,\dfrac{\pi}{4}\right)$ 上，$\sin x<\cos x<\cot x$，且 $\ln x$ 是增函数，所以",
    r"$\ln(\sin x)<\ln(\cos x)<\ln(\cot x)$",
    r"由定积分比较大小的性质可知，应选 (B).",
])

A[5] = ("D", [
    r"【答案】(D).",
    r"【解析】由初等变换及初等矩阵的性质易知 $\boldsymbol{P}_{2}\boldsymbol{A}\boldsymbol{P}_{1}=\boldsymbol{E}$，从而 $\boldsymbol{A}=\boldsymbol{P}_{2}^{-1}\boldsymbol{P}_{1}^{-1}=\boldsymbol{P}_{2}\boldsymbol{P}_{1}^{-1}$，选 (D).",
])

A[6] = ("D", [
    r"【答案】(D).",
    r"【解析】由于 $(1,0,1,0)^{T}$ 是方程组 $\boldsymbol{Ax}=\boldsymbol{0}$ 的一个基础解析. 故",
    r"$\boldsymbol{A}\begin{pmatrix}1\\0\\1\\0\end{pmatrix}=(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4})\begin{pmatrix}1\\0\\1\\0\end{pmatrix}=\boldsymbol{\alpha}_{1}+\boldsymbol{\alpha}_{3}=0$",
    r"即 $\boldsymbol{\alpha}_{1}$ 与 $\boldsymbol{\alpha}_{3}$ 线性相关，排除 (A)、(C)",
    r"又由于 $r(\boldsymbol{A}^{*})=\begin{cases}4,&r(\boldsymbol{A})=4\\1,&r(\boldsymbol{A})=3\\0,&r(\boldsymbol{A})<3\end{cases}$，知道 $r(\boldsymbol{A}^{*})$ 不可能为 2，排除 (B)",
    r"选 (D)",
])

A[7] = ("D", [
    r"【答案】(D).",
    r"【解析】由概率密度的性质知，概率密度必须满足 $\int_{-\infty}^{+\infty}f(x)dx=1$，故由题知",
    r"$\int_{-\infty}^{+\infty}\left[f_{1}(x)F_{2}(x)+f_{2}(x)F_{1}(x)\right]dx=\int_{-\infty}^{+\infty}dF_{1}(x)F_{2}(x)=F_{1}(x)F_{2}(x)\Big|_{-\infty}^{+\infty}=1$",
    r"故选择 (D)",
])

A[8] = ("B", [
    r"【答案】(B).",
    r"【解析】由题知 $UV=XY$，且 $X,Y$ 独立，故有",
    r"$E(UV)=E(XY)=EX\cdot EY$",
    r"故选择 (B).",
])
