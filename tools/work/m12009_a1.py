# -*- coding: utf-8 -*-
"""2009 数学一 解析 选择题 1-8（原卷 p6-p8，逐字照录【答案】【解析】）"""

A = {}

A[1] = ("A", [
    r"【答案】（A）",
    r"【解析】",
    r"$\sin ax=ax-\dfrac{1}{6}(ax)^{3}+o\left(x^{3}\right),\ln(1-bx)\sim-bx$，所以 $\lim\limits_{x\to0}\dfrac{x-\sin ax}{x^{2}\ln(1-bx)}=$",
    r"$\lim\limits_{x\to0}\dfrac{x-ax+\dfrac{1}{6}(ax)^{3}+o\left(x^{3}\right)}{x^{2}(-bx)}=\lim\limits_{x\to0}\dfrac{(1-a)x+\dfrac{1}{6}(ax)^{3}+o\left(x^{3}\right)}{-bx^{3}}=1,a=1,\dfrac{a^{3}}{-6}=b$，",
    r"解得 $a=1,b=-\dfrac{1}{6}$，所以选（A）",
])

A[2] = ("A", [
    r"【答案】（A）",
    r"【解析】",
    r"$D_{2},D_{4}$ 关于 $x$ 轴对称,而被积函数 $y\cos x$ 是关于 $y$ 的奇函数,所以 $I_{2}=I_{4}=0$; $D_{1},D_{3}$",
    r"两区域关于 $y$ 轴对称，被积函数 $y\cos x$ 是关于 $x$ 的偶函数，由积分对称性和定积分",
    r"的性质可知 $I_{1}=2\iint\limits_{\{(x,y)|y\geqslant x,0\leqslant x\leqslant1\}}y\cos xdxdy>0$, $I_{3}=2\iint\limits_{\{(x,y)|y\leqslant-x,0\leqslant x\leqslant1\}}y\cos xdxdy<0$",
    r"所以正确答案为（A）",
])

A[3] = ("D", [
    r"【答案】（D）",
    r"【解析】$F(x)=\displaystyle\int_{0}^{x}f(t)dt$, $F(x_{0})$ 表示 $y=f(x)$ 与 $x$ 轴、$y$ 轴及 $x=x_{0}$ 所围成的图形的",
    r"代数面积. 由 $f(x)$ 的图形可知，$x\in(-1,0)$ 时，$f(x)>0$ 且为常数,应有 $F(x)$ 单调递增且",
    r"为直线函数. $x\in(0,1)$ 时, $f(x)<0$, $F(x)\leqslant0$,且单调递减. $x\in(1,2)$ 时, $f(x)>0$, $F(x)$ 单调",
    r"递增. $x\in(2,3)$ 时, $f(x)=0$, $F(x)$ 为常函数.正确选项为（D）",
])

A[4] = ("C", [
    r"【答案】（C）",
    r"【解析】（方法 1）$\displaystyle\sum_{n=1}^{\infty}|b_{n}|$ 收敛，则 $\lim\limits_{n\to\infty}|b_{n}|=0$，又 $\lim\limits_{n\to\infty}|a_{n}|=0$，必存在 $N$，使当 $n>N$",
    r"时 $|b_{n}|<1$ 且 $|a_{n}|<1$（极限的有界性）, $0\leqslant a_{n}^{2}b_{n}^{2}<|b_{n}|$,立即由正项级数的比较判别法得到：",
    r"当 $\displaystyle\sum_{n=1}^{\infty}|b_{n}|$ 收敛时，$\displaystyle\sum_{n=1}^{\infty}|a_{n}^{2}b_{n}^{2}|$ 收敛.应选（C）.",
    r"（方法 2）反例：对 A 取 $a_{n}=b_{n}=(-1)^{n}\dfrac{1}{\sqrt{n}}$，对 B 取 $a_{n}=b_{n}=\dfrac{1}{n}$，对 D 取 $a_{n}=b_{n}=\dfrac{1}{n}$.",
])

A[5] = ("A", [
    r"【答案】（A）",
    r"【解析】由基 $\boldsymbol{a}_{1},\dfrac{1}{2}\boldsymbol{a}_{2},\dfrac{1}{3}\boldsymbol{a}_{3}$ 到 $\boldsymbol{a}_{1}+\boldsymbol{a}_{2},\boldsymbol{a}_{2}+\boldsymbol{a}_{3},\boldsymbol{a}_{3}+\boldsymbol{a}_{1}$ 的过渡矩阵满足",
    r"$(\boldsymbol{a}_{1}+\boldsymbol{a}_{2},\boldsymbol{a}_{2}+\boldsymbol{a}_{3},\boldsymbol{a}_{3}+\boldsymbol{a}_{1})=\left(\boldsymbol{a}_{1},\dfrac{1}{2}\boldsymbol{a}_{2},\dfrac{1}{3}\boldsymbol{a}_{3}\right)\begin{pmatrix}1&0&1\\2&2&0\\0&3&3\end{pmatrix}$,所以此题选（A）.",
])

A[6] = ("B", [
    r"【答案】（B）",
    r"【解析】由于分块矩阵 $\begin{pmatrix}\boldsymbol{O}&\boldsymbol{A}\\\boldsymbol{B}&\boldsymbol{O}\end{pmatrix}$ 的行列式 $\begin{vmatrix}\boldsymbol{O}&\boldsymbol{A}\\\boldsymbol{B}&\boldsymbol{O}\end{vmatrix}=(-1)^{2\times2}|\boldsymbol{A}||\boldsymbol{B}|=2\times3=6$，即分",
    r"块矩阵可逆，那么根据公式 $\boldsymbol{C}^{*}=|\boldsymbol{C}|\boldsymbol{C}^{-1}$ 可得 $\begin{pmatrix}\boldsymbol{O}&\boldsymbol{A}\\\boldsymbol{B}&\boldsymbol{O}\end{pmatrix}^{*}=\begin{vmatrix}\boldsymbol{O}&\boldsymbol{A}\\\boldsymbol{B}&\boldsymbol{O}\end{vmatrix}\begin{pmatrix}\boldsymbol{O}&\boldsymbol{A}\\\boldsymbol{B}&\boldsymbol{O}\end{pmatrix}^{-1}$",
    r"$=6\begin{pmatrix}\boldsymbol{O}&\boldsymbol{B}^{-1}\\\boldsymbol{A}^{-1}&\boldsymbol{O}\end{pmatrix}=6\begin{pmatrix}\boldsymbol{O}&\dfrac{1}{|\boldsymbol{B}|}\boldsymbol{B}^{*}\\\dfrac{1}{|\boldsymbol{A}|}\boldsymbol{A}^{*}&\boldsymbol{O}\end{pmatrix}=6\begin{pmatrix}\boldsymbol{O}&\dfrac{1}{3}\boldsymbol{B}^{*}\\\dfrac{1}{2}\boldsymbol{A}^{*}&\boldsymbol{O}\end{pmatrix}=\begin{pmatrix}\boldsymbol{O}&2\boldsymbol{B}^{*}\\3\boldsymbol{A}^{*}&\boldsymbol{O}\end{pmatrix}$，故",
    r"答案为（B）",
])

A[7] = ("C", [
    r"【答案】（C）",
    r"【解析】因为 $F(x)=0.3\Phi(x)+0.7\Phi\left(\dfrac{x-1}{2}\right)$,求导数可得",
    r"$F'(x)=0.3\varphi(x)+\dfrac{0.7}{2}\varphi\left(\dfrac{x-1}{2}\right)=0.3\dfrac{1}{\sqrt{2\pi}}e^{-\frac{x^{2}}{2}}+0.7\dfrac{1}{2\sqrt{2\pi}}e^{-\frac{(x-1)^{2}}{2\times2^{2}}}$，由于",
    r"$\dfrac{1}{\sqrt{2\pi}}e^{-\frac{x^{2}}{2}}$ 是 $N(0,1)$ 的密度函数，故其期望值为 0，$\dfrac{1}{2\sqrt{2\pi}}e^{-\frac{(x-1)^{2}}{2\times2^{2}}}$ 是 $N(1,2^{2})$ 的密度",
    r"函数，而且其期望值为 1，所以 $E(X)=0.3\times0+0.7\times1=0.7$.",
])

A[8] = ("B", [
    r"【答案】（B）",
    r"【解析】$F_{z}(z)=P(XY\leqslant z)$",
    r"$=P(XY\leqslant z|Y=0)P(Y=0)+P(XY\leqslant z|Y=1)P(Y=1)$",
    r"$=\dfrac{1}{2}[P(XY\leqslant z|Y=0)+P(XY\leqslant z|Y=1)]$",
    r"$=\dfrac{1}{2}[P(X\cdot0\leqslant z|Y=0)+P(X\cdot1\leqslant z|Y=1)]$",
    r"由于 $X$，$Y$ 独立，所以 $F_{z}(z)=\dfrac{1}{2}[P(X\cdot0\leqslant z)+P(X\leqslant z)]$.",
    r"（1）若 $z<0$，则 $F_{z}(z)=\dfrac{1}{2}\Phi(z)$，（2）若 $z\geqslant0$，则 $F_{z}(z)=\dfrac{1}{2}(1+\Phi(z))$，故",
    r"$z=0$ 为间断点，本题选（B）.",
])
