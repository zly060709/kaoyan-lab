# -*- coding: utf-8 -*-
"""2010 数学三 解析 选择题 1-8（原卷 p5-p6，逐字照录）"""

A = {}

A[1] = ("C", [
    r"【答案】C",
    r"【详解】$\lim\limits_{x\to0}\left[\dfrac{1}{x}-\left(\dfrac{1}{x}-a\right)e^{x}\right]"
    r"=\lim\limits_{x\to0}\dfrac{1-e^{x}+axe^{x}}{x}=\lim\limits_{x\to0}-e^{x}+axe^{x}+ae^{x}$",
    r"$=-1+a=1\therefore a=2$",
])

A[2] = ("A", [
    r"【答案】A",
    r"【详解】由题意知 $\begin{cases}y_{1}'+p(x)y_{1}=q(x)&(1)\\ y_{2}'+p(x)y_{2}=q(x)&(2)\end{cases}$.",
    r"由 $\lambda y_{1}+\mu y_{2}$ 是微分方程的解，将其带入微分方程得",
    r"$(\lambda y_{1}'+\mu y_{2}')+p(x)(\lambda y_{1}+\mu y_{2})=(\lambda+\mu)q(x)$，从而得，$\lambda+\mu=1$",
    r"同理将 $\lambda y_{1}-\mu y_{2}$ 带入微分方程得，$(\lambda y_{1}'-\mu y_{2}')+p(x)(\lambda y_{1}-\mu y_{2})=(\lambda-\mu)q(x)$",
    r"由 $\lambda y_{1}-\mu y_{2}$ 是对应齐次方程的解得 $\lambda-\mu=0$. 联立，"
    r"$\begin{cases}\lambda+\mu=1\\ \lambda-\mu=0\end{cases}$ 解得 $\lambda=\dfrac{1}{2},\mu=\dfrac{1}{2}$.",
])

A[3] = ("B", [
    r"【答案】B",
    r"【详解】由题意知 $g'(x_{0})=0$. 因为 $\left[f(g(x))\right]''=f''(g(x))[g'(x)]^{2}+f'(g(x))g''(x)$, 所以",
    r"$f(g(x))$ 在 $x_{0}$ 取得极值的充分条件为",
    r"$f''(g(x_{0}))=f''(a)[g'(x_{0})]^{2}+f'(a)g''(x_{0})<0$",
    r"由 $g'(x_{0})=0$，$g''(x_{0})<0$, 知 $f'(a)>0$.",
])

A[4] = ("C", [
    r"【答案】C",
    r"【详解】$\lim\limits_{x\to+\infty}\dfrac{f(x)}{g(x)}=\lim\limits_{x\to+\infty}\dfrac{\ln^{10}x}{x}=0<1\therefore f(x)<g(x)$",
    r"$\lim\limits_{x\to+\infty}\dfrac{g(x)}{h(x)}=\lim\limits_{x\to+\infty}\dfrac{x}{e^{\frac{x}{10}}}=0<1\therefore g(x)<h(x)$",
    r"即 $f(x)<g(x)<h(x)$.",
])

A[5] = ("A", [
    r"【答案】A",
    r"【详解】由向量组 I 线性无关知，$r(I)=r$，又向量组 II 的秩 $r(II)\leqslant s$, 且 I 可由 II 表示，",
    r"则 $r=r(I)\leqslant r(II)\leqslant s$，即 $r\leqslant s$.",
])

A[6] = ("D", [
    r"【答案】D",
    r"【详解】设 $A$ 的特征值为 $\lambda$，则由 $A^{2}+A=0$ 可得 $\lambda$ 满足关系式 $\lambda^{2}+\lambda=0$",
    r"即 $\lambda(\lambda+1)=0\Rightarrow\lambda=0$ 或 $\lambda=-1$, 且 $A$ 为实对称矩阵，必可相似对角化.",
    r"又因为 $R(A)=3$, 对角阵的秩也是 3. 所以 $\lambda=-1$ 是三重特征根，",
    r"故 $A\sim\begin{pmatrix}-1&&&\\&-1&&\\&&-1&\\&&&0\end{pmatrix}$，所以正确答案为（D）.",
])

A[7] = ("C", [
    r"【答案】C",
    r"【详解】",
    r"$P\{X=1\}=P\{X\leqslant1\}-P\{X<1\}=F(1)-F(1-0)=1-e^{-1}-\dfrac{1}{2}=\dfrac{1}{2}-e^{-1}$. 所以选 C.",
])

A[8] = ("A", [
    r"【答案】A",
    r"【详解】由概率密度的性质 $\int_{-\infty}^{+\infty}f(x)dx=1$，有",
    r"$a\int_{-\infty}^{0}f_{1}(x)dx+b\int_{0}^{3}f_{2}(x)dx=1\Rightarrow\dfrac{1}{2}a+\dfrac{3}{4}b=1\Rightarrow 2a+3b=4$. 所以选 A.",
])
