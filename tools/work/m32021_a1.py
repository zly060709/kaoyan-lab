# -*- coding: utf-8 -*-
"""2021 数学三 解析 选择题 1-10（原卷 p5-p8，逐字照录）"""

A = {}

A[1] = ("C", [
    r"【答案】（C）",
    r"【解析】$\lim\limits_{x\to0}\dfrac{\displaystyle\int_{0}^{x^{2}}\left(e^{t^{3}}-1\right)dt}{x^{7}}"
    r"=\lim\limits_{x\to0}\dfrac{2x\cdot\left(e^{x^{6}}-1\right)}{7x^{6}}=\lim\limits_{x\to0}\dfrac{2x^{7}}{7x^{6}}=0$，"
    r"故 $\displaystyle\int_{0}^{x^{2}}\left(e^{t^{3}}-1\right)dt$ 是 $x^{7}$ 的高阶无穷小，故选（C）",
])

A[2] = ("D", [
    r"【答案】（D）",
    r"【解析】由于 $\lim\limits_{x\to0}f(x)=\lim\limits_{x\to0}\dfrac{e^{x}-1}{x}=1=f(0)$，故在 $x=0$ 处连续.",
    r"又 $f'(0)=\lim\limits_{x\to0}\dfrac{f(x)-f(0)}{x}=\lim\limits_{x\to0}\dfrac{\dfrac{e^{x}-1}{x}-1}{x}"
    r"=\lim\limits_{x\to0}\dfrac{e^{x}-1-x}{x^{2}}=\dfrac{1}{2}$，故可导，选（D）",
])

A[3] = ("A", [
    r"【答案】（A）",
    r"【解析】由 $f(x)=ax-b\ln x(a>0)$，当 $x>0$ 时，$f'(x)=a-\dfrac{b}{x}$.",
    r"当 $b\leqslant0$ 时，$f'(x)>0$，$f(x)$ 单调递增，与题意矛盾.",
    r"当 $b>0$ 时，令 $f'(x)=0$，则 $x=\dfrac{b}{a}$，",
    r"则当 $x\in\left(0,\dfrac{b}{a}\right)$ 时，$f'(x)<0$，当 $x\in\left(\dfrac{b}{a},+\infty\right)$ 时，$f'(x)>0$.",
    r"又 $\lim\limits_{x\to0^{+}}f(x)=+\infty$，$\lim\limits_{x\to+\infty}f(x)=+\infty$，"
    r"故令 $f\left(\dfrac{b}{a}\right)=b\left(1-\ln\dfrac{b}{a}\right)<0$，即 $\dfrac{b}{a}>e$ 时与 $x$ 轴有两个交点，故选（A）",
])

A[4] = ("C", [
    r"【答案】（C）",
    r"【解析】$f(x+1,e^{x})=x(x+1)^{2}$ 两边对 $x$ 求导：",
    r"$f_{1}'(x+1,e^{x})+f_{2}'(x+1,e^{x})\cdot e^{x}=(x+1)^{2}+2x(x+1)$",
    r"将 $x=0$ 带入，得 $f_{1}'(1,1)+f_{2}'(1,1)=1$；①",
    r"$f(x,x^{2})=2x^{2}\ln x$ 两边对 $x$ 求导：",
    r"$f_{1}'(x,x^{2})+f_{2}'(x,x^{2})\cdot2x=4x\ln x+2x$",
    r"将 $x=1$ 带入，得 $f_{1}'(1,1)+2f_{2}'(1,1)=2$ ②",
    r"联立①、②，解得 $f_{1}'(1,1)=0$，$f_{2}'(1,1)=1$，故选（C）",
])

A[5] = ("B", [
    r"【答案】（B）",
    r"【解析】解法一：",
    r"$f(x_{1},x_{2},x_{3})=2x_{2}^{2}+2x_{1}x_{2}+2x_{2}x_{3}+2x_{1}x_{3}$",
    r"$=2(x_{2}^{2}+x_{1}x_{2}+x_{2}x_{3})+2x_{1}x_{3}$",
    r"$=2\Bigl[x_{2}^{2}+x_{2}(x_{1}+x_{3})+\dfrac{1}{4}(x_{1}+x_{3})^{2}\Bigr]-\dfrac{1}{2}(x_{1}+x_{3})^{2}+2x_{1}x_{3}$",
    r"$=2\Bigl[x_{2}+\dfrac{1}{2}(x_{1}+x_{3})\Bigr]^{2}-\dfrac{1}{2}(x_{1}-x_{3})^{2}$",
    r"故二次型 $f(x_{1},x_{2},x_{3})$ 的正负惯性指数为 1，1.",
    r"解法二：$f(x_{1},x_{2},x_{3})=2x_{1}x_{2}+2x_{2}^{2}+2x_{2}x_{3}+2x_{1}x_{3}$ "
    r"可得二次型矩阵为 $\begin{pmatrix}0&1&1\\ 1&2&1\\ 1&1&0\end{pmatrix}$，",
    r"$|\lambda E-A|=\begin{vmatrix}\lambda&-1&-1\\ -1&\lambda-2&-1\\ -1&-1&\lambda\end{vmatrix}"
    r"=\begin{vmatrix}\lambda+1&0&-\lambda-1\\ -1&\lambda-2&-1\\ -1&-1&\lambda\end{vmatrix}"
    r"=\begin{vmatrix}\lambda+1&0&0\\ -1&\lambda-2&-2\\ -1&-1&\lambda-1\end{vmatrix}=(\lambda+1)(\lambda^{2}-3\lambda)$",
    r"$=\lambda(\lambda+1)(\lambda-3)$",
    r"故二次型特征值为 $0,-1,3$，二次型 $f(x_{1},x_{2},x_{3})$ 的正负惯性指数为 1,1．",
])

A[6] = ("D", [
    r"【答案】（D）",
    r"【解析】由 $A=(\boldsymbol{a}_{1},\boldsymbol{a}_{2},\boldsymbol{a}_{3},\boldsymbol{a}_{4})$ 为 4 阶正交矩阵，"
    r"$\boldsymbol{a}_{1},\boldsymbol{a}_{2},\boldsymbol{a}_{3},\boldsymbol{a}_{4}$ 均为单位向量，且两两正交，",
    r"故 $r(B)=3$，且 $\begin{pmatrix}\boldsymbol{a}_{1}^{\mathrm{T}}\\ \boldsymbol{a}_{2}^{\mathrm{T}}\\ "
    r"\boldsymbol{a}_{3}^{\mathrm{T}}\end{pmatrix}\boldsymbol{a}_{4}=0$ 故 $B\boldsymbol{x}=0$ 的基础解系为 $\boldsymbol{a}_{4}$，",
    r"$B(\boldsymbol{a}_{1}+\boldsymbol{a}_{2}+\boldsymbol{a}_{3})=\begin{pmatrix}\boldsymbol{a}_{1}^{\mathrm{T}}\\ "
    r"\boldsymbol{a}_{2}^{\mathrm{T}}\\ \boldsymbol{a}_{3}^{\mathrm{T}}\end{pmatrix}"
    r"(\boldsymbol{a}_{1}+\boldsymbol{a}_{2}+\boldsymbol{a}_{3})=\begin{pmatrix}1\\ 1\\ 1\end{pmatrix}$",
    r"故 $B\boldsymbol{x}=\boldsymbol{\beta}$ 的通解为 $\boldsymbol{x}=\boldsymbol{a}_{1}+\boldsymbol{a}_{2}+\boldsymbol{a}_{3}+k\boldsymbol{a}_{4}$．",
])

A[7] = ("C", [
    r"【答案】（C）",
    r"【解析】本题（A），（B）选项中均有单位矩阵 $E$，经矩阵相乘运算验证，$PAQ$ 结果并不是对角矩阵.",
    r"（C）选项验算 $PAQ=\begin{pmatrix}1&0&0\\ 2&-1&0\\ -3&2&1\end{pmatrix}"
    r"\begin{pmatrix}1&0&-1\\ 2&-1&1\\ -1&2&-5\end{pmatrix}"
    r"\begin{pmatrix}1&0&1\\ 0&1&3\\ 0&0&1\end{pmatrix}=\begin{pmatrix}1&0&0\\ 0&1&0\\ 0&0&0\end{pmatrix}$，故选（C）.",
    r"（D）选项经矩阵相乘运算验证，$PAQ$ 结果也不是对角矩阵.",
])

A[8] = ("D", [
    r"【答案】（D）",
    r"【解析】（A）选项正确：由 $P(A|B)=P(A)$ 知，$A$ 与 $B$ 独立，所以 $P(A|\overline{B})=P(A)$ 成立.",
    r"（B）选项正确：由 $P(A|B)>P(A)$ 知，$P(AB)>P(A)P(B)$",
    r"$P(\overline{A}|\overline{B})=\dfrac{P(\overline{A}\overline{B})}{P(\overline{B})}"
    r"=\dfrac{1-P(A)-P(B)+P(AB)}{1-P(B)}$",
    r"$>\dfrac{1-P(A)-P(B)+P(A)P(B)}{1-P(B)}$",
    r"$=\dfrac{[1-P(A)][1-P(B)]}{1-P(B)}=1-P(A)=P(\overline{A})$ 成立.",
    r"（C）选项正确：$P(A|B)>P(A|\overline{B})$ 知，$P(AB)>P(A)P(B)$",
    r"故 $P(A|B)=\dfrac{P(AB)}{P(B)}>P(A)$ 成立.",
    r"（D）选项错误：$P(A|A\cup B)=\dfrac{P[A\cap(A\cup B)]}{P(A\cup B)}=\dfrac{P(A)}{P(A\cup B)}$",
    r"$P(\overline{A}|A\cup B)=\dfrac{P(\overline{A}\cap(A\cup B))}{P(A\cup B)}=\dfrac{P(\overline{A}B)}{P(A\cup B)}"
    r"=\dfrac{P(B)-P(AB)}{P(A\cup B)}$",
    r"由 $P(A|A\cup B)>P(\overline{A}|A\cup B)$ 知，$P(A)>P(B)-P(AB)$，无法说明 $P(A)>P(B)$.",
    r"选（D）．",
])

A[9] = ("B", [
    r"【答案】（B）",
    r"【解析】$E(\hat{\theta})=E(\overline{X}-\overline{Y})=EX-EY=\mu_{1}-\mu_{2}$",
    r"$D(\hat{\theta})=D(\overline{X}-\overline{Y})=D(\overline{X})+D(\overline{Y})-2\mathrm{cov}(\overline{X},\overline{Y})"
    r"=\dfrac{\sigma_{1}^{2}+\sigma_{2}^{2}-2\rho\sigma_{1}\sigma_{2}}{n}$. 选（B）.",
])

A[10] = ("A", [
    r"【答案】（A）",
    r"【解析】$L(\theta)=\left(\dfrac{1-\theta}{2}\right)^{3}\left(\dfrac{1+\theta}{4}\right)^{5}$",
    r"$\ln L(\theta)=3\ln\left(\dfrac{1-\theta}{2}\right)+5\ln\left(\dfrac{1+\theta}{4}\right)$，",
    r"令 $\dfrac{d\ln L(\theta)}{d\theta}=\dfrac{-3}{1-\theta}+\dfrac{5}{1+\theta}=0$，得 $\hat{\theta}=\dfrac{1}{4}$. 选（A）",
])
