# -*- coding: utf-8 -*-
"""2013 数学三 解析 选择题 1-8（原卷 p5-p7，逐字照录）"""

A = {}

A[1] = ("D", [
    r"【答案】(D)",
    r"【解析】",
    r"(A) $\lim\limits_{x\to0}\dfrac{x\cdot o(x^{2})}{x^{3}}=0$，所以 $x\cdot o(x^{2})=o(x^{3})$；",
    r"(B) $\lim\limits_{x\to0}\dfrac{o(x)\cdot o(x^{2})}{x^{3}}=\lim\limits_{x\to0}\Bigl[\dfrac{o(x)}{x}\cdot\dfrac{o(x^{2})}{x^{2}}\Bigr]=0$，"
    r"所以 $o(x)\cdot o(x^{2})=o(x^{3})$；",
    r"(C) $\lim\limits_{x\to0}\dfrac{o(x^{2})+o(x^{2})}{x^{2}}=\lim\limits_{x\to0}\Bigl[\dfrac{o(x^{2})}{x^{2}}+\dfrac{o(x^{2})}{x^{2}}\Bigr]=0$，"
    r"所以 $o(x^{2})+o(x^{2})=o(x^{2})$；",
    r"(D) $\lim\limits_{x\to0}\dfrac{o(x)+o(x^{2})}{x}=\lim\limits_{x\to0}\Bigl[\dfrac{o(x)}{x}+\dfrac{o(x^{2})}{x}\Bigr]=0$，"
    r"所以 $o(x)+o(x^{2})=o(x)$，D 错误，故选择",
    r"D",
])

A[2] = ("C", [
    r"【答案】（C）",
    r"【解析】",
    r"所有的间断点 $x=-1,x=0,x=1$，",
    r"因为",
    r"$\lim\limits_{x\to-1}\dfrac{|x|^{x}-1}{x(x+1)\ln|x|}=-\lim\limits_{x\to-1}\dfrac{e^{x\ln|x|}-1}{(x+1)\ln|x|}"
    r"=-\lim\limits_{x\to-1}\dfrac{x\ln|x|}{(x+1)\ln|x|}=\infty$",
    r"$\lim\limits_{x\to0}\dfrac{|x|^{x}-1}{x(x+1)\ln|x|}=\lim\limits_{x\to0}\dfrac{e^{x\ln|x|}-1}{x\ln|x|}"
    r"=\lim\limits_{x\to0}\dfrac{x\ln|x|}{x\ln|x|}=1$",
    r"$\lim\limits_{x\to1}\dfrac{|x|^{x}-1}{x(x+1)\ln|x|}=\dfrac{1}{2}\lim\limits_{x\to1}\dfrac{e^{x\ln|x|}-1}{\ln|x|}"
    r"=\dfrac{1}{2}\lim\limits_{x\to1}\dfrac{x\ln|x|}{\ln|x|}=\dfrac{1}{2}$",
    r"所以有两个可去间断点，，故选择 C",
])

A[3] = ("B", [
    r"【答案】（B）",
    r"【解析】由轮换对称性，可知 $k=1,3$ 时，$\iint\limits_{D_{k}}ydxdy=\iint\limits_{D_{k}}xdxdy$，"
    r"所以 $I_{1}=I_{3}=0$.",
    r"第二象限 $y>0,x<0$，即 $y-x>0$；第四象限 $y<0,x>0$，即 $y-x<0$,所以",
    r"$I_{2}>0,\ I_{4}<0.$ 故选 B",
])

A[4] = ("D", [
    r"【答案】（D）",
    r"【解析】(A)要使交错级数 $\sum\limits_{n=1}^{\infty}(-1)^{n-1}a_{n}$ 收敛，"
    r"不仅 $\{a_{n}\}$ 单调递减，还需要 $\lim\limits_{n\to\infty}a_{n}=0$.",
    r"(B) $\{a_{n}\}$ 单调递减，且 $\lim\limits_{n\to\infty}a_{n}=0$ 只是交错级数 "
    r"$\sum\limits_{n=1}^{\infty}(-1)^{n-1}a_{n}$ 收敛的充分条件，非必要条件.",
    r"(C) $\lim\limits_{n\to\infty}n^{p}a_{n}$ 存在，又 $p>1$，是 $\sum\limits_{n=1}^{\infty}a_{n}$ 收敛的充分条件，非必要条件.",
    r"(D) 正项级数的比较审敛法，$\lim\limits_{n\to\infty}\dfrac{a_{n}}{\dfrac{1}{n^{p}}}$ 存在，又 $p>1$，"
    r"所以 $\sum\limits_{n=1}^{\infty}a_{n}$ 与 $\sum\limits_{n=1}^{\infty}\dfrac{1}{n^{p}}$ 相同的敛散性，"
    r"$\sum\limits_{n=1}^{\infty}\dfrac{1}{n^{p}}$ 收敛，所以 $\sum\limits_{n=1}^{\infty}a_{n}$ 收敛. 故选 D",
])

A[5] = ("B", [
    r"【答案】（B）",
    r"【解析】由已知 $AB=C$，即 $A(\boldsymbol{b}_{1},\boldsymbol{b}_{2},\cdots,\boldsymbol{b}_{n})"
    r"=(\boldsymbol{c}_{1},\boldsymbol{c}_{2},\cdots,\boldsymbol{c}_{n})$，"
    r"得 $A\boldsymbol{b}_{i}=\boldsymbol{c}_{i}(i=1,2,\cdots,n)$，",
    r"即 $C$ 的每一列向量可由 $A$ 的列向量组线性表示.因为 $B$ 为可逆矩阵，从而 $A=CB^{-1}$，",
    r"同理可得 $A$ 的每一列向量可由 $C$ 的列向量组线性表示.故 $A$ 的列向量组与 $C$ 的列向量组等价，正确选项为（B）.",
])

A[6] = ("B", [
    r"【答案】（B）",
    r"【解析】由已知 $A=\begin{pmatrix}1&a&1\\ a&b&a\\ 1&a&1\end{pmatrix}$ 为实对称矩阵，"
    r"$B=\begin{pmatrix}2&0&0\\ 0&b&0\\ 0&0&0\end{pmatrix}$ 为对角矩阵，",
    r"故矩阵 $A$ 与 $B$ 相似的充分必要条件是特征值都相同，即 $\lambda_{1}=2,\lambda_{2}=b,\lambda_{3}=0$，",
    r"由 $|A-\lambda E|=\begin{pmatrix}1-\lambda&a&1\\ a&b-\lambda&a\\ 1&a&1-\lambda\end{pmatrix}"
    r"=\lambda[2a^{2}-(\lambda-2)(\lambda-b)]=0$，",
    r"可得 $2a^{2}=0$，从而 $a=0,b$ 为任意实数，正确选项为（B）.",
])

A[7] = ("A", [
    r"【答案】（A）",
    r"【解析】",
    r"由 $X\sim N(\mu,\sigma^{2})\Rightarrow\dfrac{X-\mu}{\sigma}\sim N(0,1)$，"
    r"当 $X_{1}\sim N(0,1),X_{2}\sim N(0,2^{2}),X_{3}\sim N(5,3^{2})$，",
    r"$p_{1}=P(-2<X_{1}<2)=P\left\{\left|\dfrac{X_{1}-0}{1}\right|<2\right\}=\Phi(2)-\Phi(-2)=2\Phi(2)-1$；",
    r"$p_{2}=P(-2<X_{2}<2)=P\left\{\left|\dfrac{X_{2}-0}{2}\right|<1\right\}=2\Phi(1)-1$；",
    r"$p_{3}=P(-2<X_{3}<2)=P\left\{-\dfrac{7}{3}<\dfrac{X_{3}-5}{3}<-1\right\}"
    r"=\Phi(-1)-\Phi\left(-\dfrac{7}{3}\right)$；",
    r"根据标准正态分布概率密度的函数图图像的对称性可知，$p_{1}>p_{2}>p_{3}$,故选 A",
])

A[8] = ("C", [
    r"【答案】（C）",
    r"【解析】由于 $X,Y$ 相互独立，所以",
    r"$P\{X+Y=2\}=P\{X=1,Y=1\}+P\{X=2,Y=0\}+P\{X=3,Y=-1\}$",
    r"$=P\{X=1\}P\{Y=1\}+P\{X=2\}P\{Y=0\}+P\{X=3\}P\{Y=-1\}=\dfrac{1}{6}$",
    r"故选 C",
])
