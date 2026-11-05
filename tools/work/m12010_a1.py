# -*- coding: utf-8 -*-
"""2010 数学一 解析 选择题 1-8（原卷 p5-p7，逐字照录【答案】【详解】）"""

A = {}

A[1] = ("C", [
    r"【答案】C.",
    r"【详解】方法一：",
    r"$\lim\limits_{x\to\infty}\left(\dfrac{x^{2}}{(x-a)(x+b)}\right)^{x}=\lim\limits_{x\to\infty}e^{\ln\left(\dfrac{x^{2}}{(x-a)(x+b)}\right)^{x}}"
    r"=\lim\limits_{x\to\infty}e^{x\ln\left(\dfrac{x^{2}}{(x-a)(x+b)}\right)}$",
    r"$=\lim\limits_{x\to\infty}e^{x\ln\left(1+\dfrac{x^{2}}{(x-a)(x+b)}-1\right)}=\lim\limits_{x\to\infty}e^{x\left(\dfrac{x^{2}}{(x-a)(x+b)}-1\right)}$",
    r"$=\lim\limits_{x\to\infty}e^{x\left(\dfrac{(a-b)x+ab}{(x-a)(x+b)}\right)}=\lim\limits_{x\to\infty}e^{\dfrac{(a-b)x^{2}+abx}{(x-a)(x+b)}}$",
    r"$=e^{a-b}$",
    r"方法二：本题是 $1^{\infty}$ 型极限",
    r"$\lim\limits_{x\to\infty}\left(\dfrac{x^{2}}{(x-a)(x+b)}\right)^{x}=\lim\limits_{x\to\infty}e^{x\left(\dfrac{x^{2}}{(x-a)(x+b)}-1\right)}"
    r"=\lim\limits_{x\to\infty}e^{\dfrac{(a-b)x^{2}+abx}{(x-a)(x+b)}}=e^{a-b}.$",
])

A[2] = ("B", [
    r"【答案】B.",
    r"$F\left(\dfrac{y}{x},\dfrac{z}{x}\right)=0.$",
    r"等式两边对 $x$ 求偏导，得 $F_{1}'\cdot\left(-\dfrac{y}{x^{2}}\right)+F_{2}'\cdot\left(-\dfrac{z}{x^{2}}+\dfrac{1}{x}\dfrac{\partial z}{\partial x}\right)=0$  (1)",
    r"等式两边对 $y$ 求偏导，得 $F_{1}'\cdot\dfrac{1}{x}+F_{2}'\cdot\dfrac{1}{x}\dfrac{\partial z}{\partial y}=0$  (2)",
    r"$(1)\times x^{2}+(2)\times xy$ 得 $\left(x\dfrac{\partial z}{\partial x}+y\dfrac{\partial z}{\partial y}\right)F_{2}'=zF_{2}'$，"
    r"所以 $x\dfrac{\partial z}{\partial x}+y\dfrac{\partial z}{\partial y}=z.$",
])

A[3] = ("D", [
    r"【答案】D.",
    r"【详解】显然 $x=0, x=1$ 是两个瑕点，有",
    r"$\int_{0}^{1}\dfrac{\sqrt[m]{\ln^{2}(1-x)}}{\sqrt[n]{x}}dx=\int_{0}^{\frac{1}{2}}\dfrac{\sqrt[m]{\ln^{2}(1-x)}}{\sqrt[n]{x}}dx+\int_{\frac{1}{2}}^{1}\dfrac{\sqrt[m]{\ln^{2}(1-x)}}{\sqrt[n]{x}}dx$, "
    r"对于 $\int_{0}^{\frac{1}{2}}\dfrac{\sqrt[m]{\ln^{2}(1-x)}}{\sqrt[n]{x}}dx$ 的瑕点",
    r"$x=0$，当 $x\to0^{+}$ 时 $\dfrac{\sqrt[m]{\ln^{2}(1-x)}}{\sqrt[n]{x}}=\ln^{\frac{2}{m}}(1-x)x^{-\frac{1}{n}}$ "
    r"等价于 $(-1)^{\frac{2}{m}}x^{\frac{2}{m}-\frac{1}{n}}$，而 $\int_{0}^{\frac{1}{2}}x^{\frac{2}{m}-\frac{1}{n}}dx$ 收",
    r"敛(因对任意正整数 $m,n$ 有 $\dfrac{1}{n}-\dfrac{2}{m}<1$)，故 $\int_{0}^{\frac{1}{2}}\dfrac{\sqrt[m]{\ln^{2}(1-x)}}{\sqrt[n]{x}}dx$ 收敛；对 $\int_{\frac{1}{2}}^{1}\dfrac{\sqrt[m]{\ln^{2}(1-x)}}{\sqrt[n]{x}}dx$",
    r"的瑕点 $x=1$，$x\in(1-\delta,1)\left(0<\delta<\dfrac{1}{2}\right)$ 时, $\dfrac{\sqrt[m]{\ln^{2}(1-x)}}{\sqrt[n]{x}}<2^{\frac{1}{n}}\ln^{\frac{2}{m}}(1-x)<2^{\frac{1}{n}}(1-x)^{\frac{2}{m}}$,",
    r"而 $\int_{\frac{1}{2}}^{1}(1-x)^{\frac{2}{m}}dx$ 显然收敛，故 $\int_{\frac{1}{2}}^{1}\dfrac{\sqrt[m]{\ln^{2}(1-x)}}{\sqrt[n]{x}}dx$ 收敛. 所以选择 D.",
])

A[4] = ("D", [
    r"【答案】D.",
    r"【详解】",
    r"$\lim\limits_{x\to\infty}\sum\limits_{i=1}^{n}\sum\limits_{j=1}^{n}\dfrac{n}{(n+i)(n^{2}+j^{2})}=\lim\limits_{n\to\infty}\sum\limits_{i=1}^{n}\dfrac{1}{\left(1+\dfrac{i}{n}\right)}\dfrac{1}{n}\sum\limits_{j=1}^{n}\dfrac{1}{\left(1+\left(\dfrac{j}{n}\right)^{2}\right)}\dfrac{1}{n}=$",
    r"$\int_{0}^{1}dx\int_{0}^{1}\dfrac{1}{(1+x)(1+y^{2})}dy.$",
])

A[5] = ("A", [
    r"【答案】A",
    r"【详解】由于 $\boldsymbol{AB}=\boldsymbol{E}$ 所以 $R(\boldsymbol{AB})=m$,",
    r"又 $R(\boldsymbol{AB})=m\leqslant\min(R(\boldsymbol{A}),R(\boldsymbol{B}))$ 即 $R(\boldsymbol{A})\geqslant m, R(\boldsymbol{B})\geqslant m$,",
    r"$R(\boldsymbol{A})\leqslant m, R(\boldsymbol{B})\leqslant m, R(\boldsymbol{A})=m, R(\boldsymbol{B})=m$.",
])

A[6] = ("D", [
    r"【答案】D.",
    r"【详解】设 $\boldsymbol{A}$ 的特征值为 $\lambda$，则由 $\boldsymbol{A}^{2}+\boldsymbol{A}=\boldsymbol{0}$ 可得 $\lambda$ 满足关系式 $\lambda^{2}+\lambda=0$",
    r"即 $\lambda(\lambda+1)=0\Rightarrow\lambda=0$ 或 $\lambda=-1$, 且 $\boldsymbol{A}$ 为实对称矩阵，必可相似对角化.",
    r"又因为 $R(\boldsymbol{A})=3$, 对角阵的秩也是 3. 所以 $\lambda=-1$ 是三重特征根，",
    r"故 $\boldsymbol{A}\sim\begin{pmatrix}-1&&&\\&-1&&\\&&-1&\\&&&0\end{pmatrix}$，所以正确答案为（D）.",
])

A[7] = ("C", [
    r"【答案】C.",
    r"【详解】$P\{x=1\}=P\{x\leqslant1\}-P\{x<1\}=F(1)-F(1-0)=1-e^{-1}-\dfrac{1}{2}=\dfrac{1}{2}-e^{-1}$",
    r"所以选 C.",
])

A[8] = ("A", [
    r"【答案】A.",
    r"【详解】由概率密度的性质 $\int_{-\infty}^{+\infty}f(x)dx=1$，有",
    r"$a\int_{-\infty}^{0}f_{1}(x)dx+b\int_{0}^{3}f_{2}(x)dx=1\Rightarrow\dfrac{1}{2}a+\dfrac{3}{4}b=1\Rightarrow2a+3b=4$",
    r"所以选 A.",
])
