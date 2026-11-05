# -*- coding: utf-8 -*-
"""2015 数学三 解析 选择题 1-8（原卷 p5-p7，逐字照录）"""

A = {}

A[1] = ("D", [
    r"【答案】(D)",
    r"【解析】考查数列极限与子列极限的关系.数列收敛，那么它的任何无穷子列均收敛.所以(A)"
    r"与（C）正确；一个数列存在多个无穷子列并集包含原数列所有项，且这些子列均收敛于同"
    r"一个值，则原数列是收敛的.(B)正确，(D) 错误，故选（D）",
])

A[2] = ("C", [
    r"【答案】(C)",
    r"【解析】根据拐点的必要条件，拐点可能是 $f''(x)$ 不存在的点或 $f''(x)=0$ 的点处产生.所以"
    r"$y=f(x)$ 有三个点可能是拐点，根据拐点的定义，即凹凸性改变的点；二阶导函数 $f''(x)$ 符"
    r"号发生改变的点即为拐点.所以从图可知，拐点个数为 2，故选（C）",
])

A[3] = ("B", [
    r"【答案】(B)",
    r"【解析】根据图可得，在极坐标系下该二重积分要分成两个积分区域",
    r"$D_{1}=\left\{(r,\theta)\middle|0\leq\theta\leq\dfrac{\pi}{4},0\leq r\leq2\sin\theta\right\}$,"
    r"$D_{2}=\left\{(r,\theta)\middle|\dfrac{\pi}{4}\leq\theta\leq\dfrac{\pi}{2},0\leq r\leq2\cos\theta\right\}$",
    r"所以",
    r"$\iint\limits_{D}f\left(x,y\right)\mathrm{d}x\mathrm{d}y=\int_{0}^{\frac{\pi}{4}}\mathrm{d}\theta\int_{0}^{2\sin\theta}f\left(r\cos\theta,r\sin\theta\right)r\mathrm{d}r"
    r"+\int_{\frac{\pi}{4}}^{\frac{\pi}{2}}\mathrm{d}\theta\int_{0}^{2\cos\theta}f\left(r\cos\theta,r\sin\theta\right)r\mathrm{d}r$,",
    r"选（B）",
])

A[4] = ("C", [
    r"【答案】(C)",
    r"【解析】(A)为正项级数，因为 $\lim\limits_{n\to\infty}\dfrac{\dfrac{n+1}{3^{n+1}}}{\dfrac{n}{3^{n}}}"
    r"=\lim\limits_{n\to\infty}\dfrac{n+1}{3n}=\dfrac{1}{3}=<1$，所以根据正项级数的比值判",
    r"别法$\sum\limits_{n=1}^{\infty}\dfrac{n}{3^{n}}$ 收敛；(B)为正项级数，因为 $\dfrac{1}{\sqrt{n}}\ln(1+\dfrac{1}{n})\sim\dfrac{1}{n^{\frac{3}{2}}}$，根据 $P$ 级数收敛准则, 知",
    r"$\sum\limits_{n=1}^{\infty}\dfrac{1}{\sqrt{n}}\ln(1+\dfrac{1}{n})$ 收敛；(C) $\sum\limits_{n=1}^{\infty}\dfrac{\left(-1\right)^{n}+1}{\ln n}"
    r"=\sum\limits_{n=1}^{\infty}\dfrac{\left(-1\right)^{n}}{\ln n}+\sum\limits_{n=1}^{\infty}\dfrac{1}{\ln n}$，根据莱布尼茨判别法知",
    r"$\sum\limits_{n=1}^{\infty}\dfrac{\left(-1\right)^{n}}{\ln n}$ 收敛，$\sum\limits_{n=1}^{\infty}\dfrac{1}{\ln n}$ 发散, 所以根据级数收敛定义知, $\sum\limits_{n=1}^{\infty}\dfrac{\left(-1\right)^{n}+1}{\ln n}$ 发散；(D)为正项",
    r"级数, 因为 $\lim\limits_{n\to\infty}\dfrac{\dfrac{(n+1)!}{(n+1)^{n+1}}}{\dfrac{n!}{n^{n}}}"
    r"=\lim\limits_{n\to\infty}\dfrac{(n+1)!}{n!}\dfrac{n^{n}}{(n+1)^{n+1}}"
    r"=\lim\limits_{n\to\infty}\left(\dfrac{n}{n+1}\right)^{n}=\dfrac{1}{e}<1$，所以根据正项级",
    r"数的比值判别法$\sum\limits_{n=1}^{\infty}\dfrac{n!}{n^{n}}$收敛, 所以选（C）",
])

A[5] = ("D", [
    r"【答案】(D)",
    r"【解析】$(\boldsymbol{A},\boldsymbol{b})=\left(\begin{array}{cccc}1&1&1&1\\ 1&2&a&d\\ 1&4&a^{2}&d^{2}\end{array}\right)"
    r"\to\left(\begin{array}{cccc}1&1&1&1\\ 0&1&a-1&d-1\\ 0&0&(a-1)(a-2)&(d-1)(d-2)\end{array}\right)$,",
    r"由 $r(\boldsymbol{A})=r(\boldsymbol{A},\boldsymbol{b})<3$，故 $a=1$ 或 $a=2$，同时 $d=1$ 或 $d=2$. 故选（D）．",
])

A[6] = ("A", [
    r"【答案】(A)",
    r"【解析】解法一：由 $\boldsymbol{x}=\boldsymbol{Py}$，故 $f=\boldsymbol{x}^{T}\boldsymbol{Ax}=\boldsymbol{y}^{T}\left(\boldsymbol{P}^{T}\boldsymbol{AP}\right)\boldsymbol{y}=2y_{1}^{2}-y_{2}^{2}+y_{3}^{2}$.且",
    r"$\boldsymbol{P}^{T}\boldsymbol{AP}=\begin{pmatrix}2&0&0\\ 0&1&0\\ 0&0&-1\end{pmatrix}$,",
    r"$\boldsymbol{Q}=\boldsymbol{P}\begin{pmatrix}1&0&0\\ 0&0&1\\ 0&-1&0\end{pmatrix}=\boldsymbol{PC}$,",
    r"$\boldsymbol{Q}^{T}\boldsymbol{AQ}=\boldsymbol{C}^{T}\left(\boldsymbol{P}^{T}\boldsymbol{AP}\right)\boldsymbol{C}=\begin{pmatrix}2&0&0\\ 0&-1&0\\ 0&0&1\end{pmatrix}$.",
    r"所以 $f=\boldsymbol{x}^{T}\boldsymbol{Ax}=\boldsymbol{y}^{T}\left(\boldsymbol{P}^{T}\boldsymbol{AP}\right)\boldsymbol{y}=2y_{1}^{2}-y_{2}^{2}+y_{3}^{2}$. 选（A）.",
    r"解法二：设二次型的矩阵为 $\boldsymbol{A}$，则",
    r"$\boldsymbol{P}^{-1}\boldsymbol{AP}=\boldsymbol{P}^{T}\boldsymbol{AP}=\begin{pmatrix}2&0&0\\ 0&1&0\\ 0&0&-1\end{pmatrix}$",
    r"可见 $\boldsymbol{e}_{1},\boldsymbol{e}_{2},\boldsymbol{e}_{3}$ 都是 $\boldsymbol{A}$ 的特征向量，特征值依次为 $2,1,-1$；于是 $\boldsymbol{e}_{1},-\boldsymbol{e}_{3},\boldsymbol{e}_{2}$ 也是 $\boldsymbol{A}$ 的特征向",
    r"量，特征值分别是 $1,-1,1$从而正交变换 $\boldsymbol{x}=\boldsymbol{Qy}$ 下的标准形为 $2y_{1}^{2}-y_{2}^{2}+y_{3}^{2}$.",
])

A[7] = ("C", [
    r"【答案】(C)",
    r"【解析】由于 $AB\subset A,AB\subset B$，按概率的基本性质，我们有 $P\left(AB\right)\leq P\left(A\right)$ 且",
    r"$P\left(AB\right)\leq P\left(B\right)$，从而 $P\left(AB\right)\leq\dfrac{P\left(A\right)+P\left(B\right)}{2}$，选（C）．",
])

A[8] = ("B", [
    r"【答案】(B)",
    r"【解析】根据样本方差 $S^{2}=\dfrac{1}{n-1}\sum\limits_{i=1}^{n}\left(X_{i}-\overline{X}\right)^{2}$ 的性质 $E(S^{2})=D(X)$，而",
    r"$D(X)=m\theta(1-\theta)$，从而 $E\bigl[\sum\limits_{i=1}^{n}\left(X_{i}-\overline{X}\right)^{2}\bigr]=(n-1)E(S^{2})=m(n-1)\theta(1-\theta)$，选（B）．",
])
