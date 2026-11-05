# -*- coding: utf-8 -*-
"""2020 数学三 解析 选择题 1-8（原卷 p5-p7，逐字照录）"""

A = {}

A[1] = ("B", [
    r"【答案】（B）",
    r"【解析】∵ $\lim\limits_{x\to a}\dfrac{f(x)-a}{x-a}=b$ ∴ $\lim\limits_{x\to a}f(x)=a$，",
    r"设 $f(x)=u$，则 $\lim\limits_{x\to a}\dfrac{\sin f(x)-\sin a}{f(x)-a}=\lim\limits_{u\to a}\dfrac{\sin u-\sin a}{u-a}=\cos a$，",
    r"则 $\lim\limits_{x\to a}\dfrac{\sin f(x)-\sin a}{x-a}=\lim\limits_{x\to a}\dfrac{\sin f(x)-\sin a}{f(x)-a}\cdot\lim\limits_{x\to a}\dfrac{f(x)-a}{x-a}=b\cos a$.",
])

A[2] = ("C", [
    r"【答案】（C）",
    r"【解析】本题考查的是第一类间断点与第二类间断点的定义，判断间断点及类型的一般步骤"
    r"为：①找出无定义的点（无意义的点）；②求该点的左右极限；③按照间断点的定义判定.",
    r"第二类间断点的定义为 $f_{-}(x_{0}),f_{+}(x_{0})$ 至少有一个不存在，很显然 $f(x)$ 不存在的点为"
    r"$x=-1,x=0,x=1,x=2$.",
    r"在 $x=-1$ 处，$\lim\limits_{x\to-1^{-}}f(x)=-\infty$, $\lim\limits_{x\to-1^{+}}f(x)=-\infty$；",
    r"在 $x=0$ 处，$\lim\limits_{x\to0^{-}}f(x)=\lim\limits_{x\to0^{+}}f(x)=-\dfrac{1}{2e}$；",
    r"在 $x=1$ 处，$\lim\limits_{x\to1^{-}}e^{\frac{1}{x-1}}=0$ ， $\lim\limits_{x\to1^{+}}e^{\frac{1}{x-1}}=+\infty$，"
    r"$\lim\limits_{x\to1^{-}}f(x)=0$，$\lim\limits_{x\to1^{+}}f(x)=-\infty$；",
    r"在 $x=2$ 处，$\lim\limits_{x\to2^{-}}f(x)=-\infty$，$\lim\limits_{x\to2^{+}}f(x)=+\infty$；",
    r"所以，第二类间断点为 3 个.",
])

A[3] = ("A", [
    r"【答案】（A）",
    r"【解析】$f(x)$ 为奇函数，则其导数 $f'(x)$ 为偶函数，又 $\cos x$ 为偶函数，则"
    r"$\cos f(x)=\cos f(-x)$，则 $\cos f(x)$ 为偶函数，故 $\cos f(x)+f'(x)$ 为偶函数，以 0 为下"
    r"限、被积函数为偶函数的变限积分函数为奇函数. 所以，本题选 $A$;对于 $C$ 和 $D$ 选项，$f'(x)$"
    r"为偶函数，则 $\cos f'(x)=\cos f'(-x)$ 为偶函数，$f(x)$ 为奇函数，则 $\cos f'(x)+f(x)$ 既"
    r"非奇函数又非偶函数.",
])

A[4] = ("B", [
    r"【答案】（B）",
    r"【解析】由比值法可知，幂级数收敛时，"
    r"$\lim\limits_{n\to\infty}\left|\dfrac{a_{n+1}(x+1)^{2n+2}}{a_{n}(x+1)^{2n}}\right|=\lim\limits_{n\to\infty}\left|\dfrac{a_{n+1}}{a_{n}}\right|(x+1)^{2}<1$，",
    r"则要求 $\sum\limits_{n=1}^{\infty}a_{n}(x+2)^{2n}$ 的收敛区间，只需要求出 $\lim\limits_{n\to\infty}\left|\dfrac{a_{n+1}}{a_{n}}\right|$ 的值即可，",
    r"而条件告诉我们幂级数 $\sum\limits_{n=1}^{\infty}na_{n}(x-2)^{n}$ 的收敛区间为 $(-2,6)$，即收敛半径为 4，",
    r"$\lim\limits_{n\to\infty}\left|\dfrac{(n+1)a_{n+1}}{na_{n}}\right|=\lim\limits_{n\to\infty}\dfrac{n+1}{n}\left|\dfrac{a_{n+1}}{a_{n}}\right|=\lim\limits_{n\to\infty}\left|\dfrac{a_{n+1}}{a_{n}}\right|=\dfrac{1}{4}$，",
    r"则 $\lim\limits_{n\to\infty}\left|\dfrac{a_{n+1}}{a_{n}}\right|(x+1)^{2n}=\dfrac{1}{4}(x+1)^{2}<1$，即 $-3<x<1$.",
    r"所以本题选（B）.",
])

A[5] = ("C", [
    r"【答案】（C）",
    r"【解析】$A=(a_{ij})$ 不可逆知，$|A|=0$ 及 $r(A)<4$；由 $A_{12}\neq0$ 知 $A^{*}\neq O$ 且 $\boldsymbol{a}_{1},\boldsymbol{a}_{3},\boldsymbol{a}_{4}$ 线性无"
    r"关（无关组的延长组仍无关），故 $r(A)=3$ 及 $r(A^{*})=1$，故 $A^{*}\boldsymbol{x}=\boldsymbol{0}$ 的基础解系含有 3 个"
    r"向量. 由 $A^{*}A=|A|E=O$ 知，$A$ 的列向量均为 $A^{*}\boldsymbol{x}=\boldsymbol{0}$ 的解,故通解 $\boldsymbol{x}=k_{1}\boldsymbol{a}_{1}+k_{2}\boldsymbol{a}_{3}+k_{3}\boldsymbol{a}_{4}$.",
])

A[6] = ("D", [
    r"【答案】（D）",
    r"【解析】因为 $\boldsymbol{a}_{1},\boldsymbol{a}_{2}$ 为 $A$ 的特征值 1 对应的两个线性无关的特征向量，故 $\boldsymbol{a}_{1}+\boldsymbol{a}_{2},\boldsymbol{a}_{2}$ 仍为特"
    r"征值 1 的两个线性无关的特征向量；因为 $\boldsymbol{a}_{3}$ 为 $A$ 的特征值 $-1$ 的特征向量，故 $-\boldsymbol{a}_{3}$ 仍为特征"
    r"值 $-1$ 的特征向量，因为特征向量与特征值的排序一一对应，故只需 $P=(\boldsymbol{a}_{1}+\boldsymbol{a}_{2},-\boldsymbol{a}_{3},\boldsymbol{a}_{2})$，",
    r"就有 $P^{-1}AP=\begin{pmatrix}1&0&0\\ 0&-1&0\\ 0&0&1\end{pmatrix}$.",
])

A[7] = ("D", [
    r"【答案】（D）",
    r"【解析】",
    r"$P(A\bar{B}\bar{C})+P(\bar{A}B\bar{C})+P(\bar{A}\bar{B}C)$",
    r"$=P(A\cap\overline{B\cup C})+P(B\cap\overline{A\cup C})+P(C\cap\overline{A\cup B})$",
    r"$=P(A)-P(AB)-P(AC)+P(ABC)+P(B)-P(AB)-P(BC)+P(ABC)$",
    r"$+P(C)-P(AC)-P(BC)+P(ABC)$",
    r"又 $ABC\subset AB$，$P(ABC)\leqslant P(AB)=0,P(ABC)=0$，",
    r"原式$=\dfrac{1}{4}-\dfrac{1}{12}+\dfrac{1}{4}-\dfrac{1}{12}+\dfrac{1}{4}-\dfrac{1}{12}-\dfrac{1}{12}=\dfrac{5}{12}$.",
])

A[8] = ("C", [
    r"【答案】（C）",
    r"【解析】由二维正态分布可知 $X\sim N(0,1)$， $Y\sim N(0,4)$， $\rho_{XY}=-\dfrac{1}{2}$",
    r"$D(X+Y)=DX+DY+2\rho_{XY}\sqrt{DX}\sqrt{DY}=3$，",
    r"所以 $X+Y\sim N(0,3)$，$\dfrac{\sqrt{3}}{3}(X+Y)\sim N(0,1)$.",
    r"又 $\mathrm{cov}(X,X+Y)=\mathrm{cov}(X,X)+\mathrm{cov}(X,Y)=DX+\rho_{XY}\sqrt{DX}\sqrt{DY}=0$，",
    r"所以 $X$ 与 $\dfrac{\sqrt{3}}{3}(X+Y)$ 独立.",
])
