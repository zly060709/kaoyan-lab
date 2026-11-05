# -*- coding: utf-8 -*-
"""2009 数学三 解析 选择题 1-8（原卷 p5-p7，逐字照录）"""

A = {}

A[1] = ("C", [
    r"【答案】（C）",
    r"【解析】$f(x)=\dfrac{x-x^{3}}{\sin\pi x}$",
    r"则当 $x$ 取任何整数时，$f(x)$ 均无意义. 故 $f(x)$ 的间断点有无穷多个，但可去间断点为",
    r"极限存在的点，故应是 $x-x^{3}=0$ 的解. $x_{1}=0$，$x_{2}=1,x_{3}=-1$，",
    r"$\lim\limits_{x\to0}\dfrac{x-x^{3}}{\sin\pi x}=\lim\limits_{x\to0}\dfrac{1-3x^{2}}{\pi\cos\pi x}=\dfrac{1}{\pi}$；",
    r"$\lim\limits_{x\to1}\dfrac{x-x^{3}}{\sin\pi x}=\lim\limits_{x\to1}\dfrac{1-3x^{2}}{\pi\cos\pi x}=\dfrac{2}{\pi}$；"
    r"$\lim\limits_{x\to-1}\dfrac{x-x^{3}}{\sin\pi x}=\lim\limits_{x\to-1}\dfrac{1-3x^{2}}{\pi\cos\pi x}=\dfrac{2}{\pi}$.",
    r"故可去间断点为 3 个，即 $x_{1}=0$，$x_{2}=1,x_{3}=-1$. ",
])

A[2] = ("A", [
    r"【答案】（A）",
    r"【解析】$\sin ax=ax-\dfrac{1}{6}(ax)^{3}+o\left(x^{3}\right)$，$\ln(1-bx)\sim-bx$,所以 "
    r"$\lim\limits_{x\to0}\dfrac{x-\sin ax}{x^{2}\ln(1-bx)}=$",
    r"$\lim\limits_{x\to0}\dfrac{x-ax+\dfrac{1}{6}(ax)^{3}+o\left(x^{3}\right)}{x^{2}(-bx)}"
    r"=\lim\limits_{x\to0}\dfrac{x-ax+\dfrac{1}{6}(ax)^{3}+o\left(x^{3}\right)}{-bx^{3}}=1,a=1,\dfrac{a^{3}}{-6}=b$，可以解得",
    r"$a=1,b=-\dfrac{1}{6}$. 所以选（A）",
])

A[3] = ("A", [
    r"【答案】（A）",
    r"【解析】原问题可转化为求",
    r"$f(x)=\displaystyle\int_{1}^{x}\dfrac{\sin t}{t}dt-\ln x=\int_{1}^{x}\dfrac{\sin t}{t}dt-\int_{1}^{x}\dfrac{1}{t}dt"
    r"=\int_{1}^{x}\dfrac{\sin t-1}{t}dt=\int_{x}^{1}\dfrac{1-\sin t}{t}dt>0$ 成立时 $x$ 的取值范围，"
    r"由 $\dfrac{1-\sin t}{t}>0,t\in(0,1)$ 时，知当 $x\in(0,1)$ 时，$f(x)>0$，故应选（A）",
])

A[4] = ("D", [
    r"【答案】（D）",
    r"【解析】$F(x)=\displaystyle\int_{0}^{x}f(t)dt$，$F(x_{0})$ 表示 $y=f(x)$ 与 $x$ 轴、$y$ 轴及 $x=x_{0}$ 所围成的图形的代数"
    r"面积。由 $f(x)$ 的图形可知，$x\in(-1,0)$ 时，$f(x)>0$ 且为常数,应有 $F(x)$ 单调递增且为直"
    r"线函数. $x\in(0,1)$ 时, $f(x)<0,F(x)\leqslant0$,且单调递减. $x\in(1,2)$ 时, $f(x)>0,F(x)$ 单调递增. "
    r"$x\in(2,3)$ 时, $f(x)=0,F(x)$ 为常函数. 正确选项为（D）",
])

A[5] = ("B", [
    r"【答案】（B）",
    r"【解析】由于分块矩阵 $\begin{pmatrix}\boldsymbol{O}&\boldsymbol{A}\\\boldsymbol{B}&\boldsymbol{O}\end{pmatrix}$ 的行列式"
    r"$\left|\begin{matrix}\boldsymbol{O}&\boldsymbol{A}\\\boldsymbol{B}&\boldsymbol{O}\end{matrix}\right|=(-1)^{2\times2}\left|\boldsymbol{A}\right|\left|\boldsymbol{B}\right|=2\times3=6$，即分块矩"
    r"阵可逆，根据公式 $\boldsymbol{C}^{*}=\left|\boldsymbol{C}\right|\boldsymbol{C}^{-1}$ 可得"
    r"$\begin{pmatrix}\boldsymbol{O}&\boldsymbol{A}\\\boldsymbol{B}&\boldsymbol{O}\end{pmatrix}^{*}="
    r"\left|\begin{matrix}\boldsymbol{O}&\boldsymbol{A}\\\boldsymbol{B}&\boldsymbol{O}\end{matrix}\right|"
    r"\begin{pmatrix}\boldsymbol{O}&\boldsymbol{A}\\\boldsymbol{B}&\boldsymbol{O}\end{pmatrix}^{-1}$",
    r"$=6\begin{pmatrix}\boldsymbol{O}&\boldsymbol{B}^{-1}\\\boldsymbol{A}^{-1}&\boldsymbol{O}\end{pmatrix}"
    r"=6\begin{pmatrix}\boldsymbol{O}&\dfrac{1}{|\boldsymbol{B}|}\boldsymbol{B}^{*}\\[2mm]"
    r"\dfrac{1}{|\boldsymbol{A}|}\boldsymbol{A}^{*}&\boldsymbol{O}\end{pmatrix}"
    r"=6\begin{pmatrix}\boldsymbol{O}&\dfrac{1}{3}\boldsymbol{B}^{*}\\[2mm]"
    r"\dfrac{1}{2}\boldsymbol{A}^{*}&\boldsymbol{O}\end{pmatrix}"
    r"=\begin{pmatrix}\boldsymbol{O}&2\boldsymbol{B}^{*}\\3\boldsymbol{A}^{*}&\boldsymbol{O}\end{pmatrix}$，故答案为",
    r"（B）",
])

A[6] = ("A", [
    r"【答案】（A）",
    r"【解析】$\boldsymbol{Q}=(\boldsymbol{\alpha}_{1}+\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3})"
    r"=(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3})\begin{pmatrix}1&0&0\\1&1&0\\0&0&1\end{pmatrix}"
    r"=(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3})\boldsymbol{E}_{12}(1)$，即：",
    r"$\boldsymbol{Q}=\boldsymbol{P}\boldsymbol{E}_{12}(1)$，"
    r"$\boldsymbol{Q}^{T}\boldsymbol{A}\boldsymbol{Q}=[\boldsymbol{P}\boldsymbol{E}_{12}(1)]^{T}\boldsymbol{A}[\boldsymbol{P}\boldsymbol{E}_{12}(1)]"
    r"=\boldsymbol{E}_{12}^{T}(1)[\boldsymbol{P}^{T}\boldsymbol{A}\boldsymbol{P}]\boldsymbol{E}_{12}(1)$",
    r"$=\boldsymbol{E}_{12}^{T}(1)\begin{pmatrix}1&0&0\\1&1&0\\0&0&1\end{pmatrix}\boldsymbol{E}_{12}(1)"
    r"=\begin{pmatrix}1&1&0\\0&1&0\\0&0&1\end{pmatrix}\begin{pmatrix}1&0&0\\0&1&0\\0&0&2\end{pmatrix}"
    r"\begin{pmatrix}1&1&0\\0&1&0\\0&0&1\end{pmatrix}=\begin{pmatrix}2&1&0\\1&1&0\\0&0&2\end{pmatrix}$. ",
])

A[7] = ("D", [
    r"【答案】（D）",
    r"【解析】因为 $A,B$ 互不相容，所以 $P(AB)=0$. ",
    r"（A）$P=(\overline{A}\,\overline{B})=P(\overline{A\cup B})=1-P(A\cup B)$，因为 $P(A\cup B)$ 不一定等于 1，所以（A）不"
    r"正确；（B）当 $P(A),P(B)$ 不为 0 时，（B）不成立，故排除；（C）只有当 $A,B$ 互为对立事"
    r"件的时候才成立，故排除；（D）$P=(\overline{A}\cup\overline{B})=P(\overline{AB})=1-P(AB)=1$，故（D）正确.",
])

A[8] = ("B", [
    r"【答案】（B）",
    r"【解析】$F_{z}(z)=P(XY\leqslant z)=P(XY\leqslant z|Y=0)P(Y=0)+P(XY\leqslant z|y=1)P(Y=1)$",
    r"$=\dfrac{1}{2}[P(XY\leqslant z|Y=0)+P(XY\leqslant z|Y=1)]$",
    r"$=\dfrac{1}{2}[P(X\cdot0\leqslant z|Y=0)+P(XY\leqslant z|Y=1)]$",
    r"由于 $X$，$Y$ 独立：得 $F_{z}(z)=\dfrac{1}{2}[P(X\cdot0\leqslant z)+P(X\leqslant z)]$. ",
    r"（1）若 $z<0$，则 $F_{z}(z)=\dfrac{1}{2}\Phi(z)$. （2）若 $z\geqslant0$，则 $F_{z}(z)=\dfrac{1}{2}(1+\Phi(z))$. ",
    r"因此，$z=0$ 为间断点，故选（B）.",
])
