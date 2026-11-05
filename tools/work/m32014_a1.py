# -*- coding: utf-8 -*-
"""2014 数学三 解析 选择题 1-8（原卷 p4-p6，逐字照录）"""

A = {}

A[1] = ("A", [
    r"【答案】（A）",
    r"【解析】由极限的保号性，即可得到 $|a_{n}|>\dfrac{|a|}{2}$ 正确，（C）反例 $a_{n}=a-\dfrac{2}{n}$，（D）反例 "
    r"$a_{n}=a+\dfrac{2}{n}$.",
])

A[2] = ("C", [
    r"【答案】（C）",
    r"【解析】A. $\lim\limits_{x\to\infty}(x+\sin x)=\infty$，所以 $y=x+\sin x$ 无水平渐近线，又可知 "
    r"$y=x+\sin x$ 无垂直渐近线，又 $\lim\limits_{x\to\infty}\dfrac{x+\sin x}{x}=1$，"
    r"$\lim\limits_{x\to\infty}(x+\sin x-x)=\lim\limits_{x\to\infty}\sin x$ 极限不存在，"
    r"所以 $y=x+\sin x$ 无斜渐近线；",
    r"B. $\lim\limits_{x\to\infty}(x^{2}+\sin x)=\infty$，所以 $y=x^{2}+\sin x$ 无水平渐近线，又可知 "
    r"$y=x^{2}+\sin x$ 无垂直渐近线，又 $\lim\limits_{x\to\infty}\dfrac{x^{2}+\sin x}{x}=\infty$，"
    r"极限不存在，所以 $y=x^{2}+\sin x$ 无斜渐近线；",
    r"C. $\lim\limits_{x\to\infty}(x+\sin\dfrac{1}{x})=\infty$，所以 $y=x+\sin\dfrac{1}{x}$ 无水平渐近线，又可知 "
    r"$y=x+\sin\dfrac{1}{x}$ 无垂直渐近线，又 $\lim\limits_{x\to\infty}\dfrac{x+\sin\dfrac{1}{x}}{x}=1$；"
    r"所以 $y=x+\sin\dfrac{1}{x}$ 有斜渐近线 $y=x$，",
    r"D. $\lim\limits_{x\to\infty}(x^{2}+\sin\dfrac{1}{x})=\infty$，所以 $y=x^{2}+\sin\dfrac{1}{x}$ 无水平渐近线，"
    r"又可知 $y=x^{2}+\sin\dfrac{1}{x}$ 无垂直渐近线，又 $\lim\limits_{x\to\infty}\dfrac{x^{2}+\sin\dfrac{1}{x}}{x}=\infty$，"
    r"极限不存在，所以 $y=x^{2}+\sin\dfrac{1}{x}$ 无斜渐近线.",
])

A[3] = ("D", [
    r"【答案】（D）",
    r"【解析】$\tan x=x+\dfrac{1}{3}x^{3}+o(x^{3})$，所以由 $P(x)-\tan x$ 是比 $x^{3}$ 高阶无穷小，得 "
    r"$\lim\limits_{x\to0}\dfrac{P(x)-\tan x}{x^{3}}=0$，所以",
    r"$\lim\limits_{x\to0}\dfrac{P(x)-\tan x}{x^{3}}=0$, 所以 "
    r"$\lim\limits_{x\to0}\dfrac{a+bx+cx^{2}+dx^{3}-x-\dfrac{1}{3}x^{3}-o(x^{3})}{x^{3}}=0$, 所以 $a=0$",
    r"$b=1$, $c=0$, $d=\dfrac{1}{3}$.",
])

A[4] = ("D", [
    r"【答案】（D）",
    r"【解析】$g(x)=f(0)(1-x)+f(1)x$，$g(0)=f(0),g(1)=f(1)$；故 $g(x)$ 实质为一条连接 $[0,f(0)],[1,f(1)]$ 的直线，"
    r"所以当 $f''(x)\geqslant0$ 时，$f(x)$ 为凹的，由图形知，$f(x)\leqslant g(x)$.",
])

A[5] = ("B", [
    r"【答案】（B）",
    r"【解析】解法一 利用行列式性质把此行列式化为拉普拉斯形式",
    r"$\begin{vmatrix}0&a&b&0\\ a&0&0&b\\ 0&c&d&0\\ c&0&0&d\end{vmatrix}"
    r"=-\begin{vmatrix}a&b&0&0\\ c&d&0&0\\ 0&0&d&c\\ 0&0&b&a\end{vmatrix}=-(ad-bc)^{2}$；",
    r"解法二 按第一列展开",
    r"$\begin{vmatrix}0&a&b&0\\ a&0&0&b\\ 0&c&d&0\\ c&0&0&d\end{vmatrix}"
    r"=-a\begin{vmatrix}a&b&0\\ c&d&0\\ 0&0&d\end{vmatrix}-c\begin{vmatrix}a&b&0\\ 0&0&b\\ c&d&0\end{vmatrix}$",
    r"$=-ad(ad-bc)+bc(ad-bc)$",
    r"$=-(ad-bc)^{2}$",
    r"所以正确答案为(B).",
])

A[6] = ("A", [
    r"【答案】(A)",
    r"【解析】①充分性",
    r"若向量组 $\boldsymbol{a}_{1}+k\boldsymbol{a}_{3},\boldsymbol{a}_{2}+l\boldsymbol{a}_{3}$ 线性无关，"
    r"令 $k=0,l=0$，得 $\boldsymbol{a}_{1},\boldsymbol{a}_{2}$ 线性无关.",
    r"但 $\boldsymbol{a}_{1},\boldsymbol{a}_{2},\boldsymbol{a}_{3}$ 不一定线性无关，比如若 $\boldsymbol{a}_{3}=\boldsymbol{0}$ 时，"
    r"$\boldsymbol{a}_{1},\boldsymbol{a}_{2},\boldsymbol{a}_{3}$ 线性相关.",
    r"从而任意常数 $k,l$，向量组 $\boldsymbol{a}_{1}+k\boldsymbol{a}_{3},\boldsymbol{a}_{2}+l\boldsymbol{a}_{3}$ 线性无关"
    r"不是向量组 $\boldsymbol{a}_{1},\boldsymbol{a}_{2},\boldsymbol{a}_{3}$ 线性无关的充分条件.",
    r"②必要性",
    r"$(\boldsymbol{a}_{1}+k\boldsymbol{a}_{3},\boldsymbol{a}_{2}+l\boldsymbol{a}_{3})"
    r"=(\boldsymbol{a}_{1},\boldsymbol{a}_{2},\boldsymbol{a}_{3})\begin{pmatrix}1&0\\ 0&1\\ k&l\end{pmatrix}$",
    r"令",
    r"$\boldsymbol{C}=(\boldsymbol{a}_{1}+k\boldsymbol{a}_{3},\boldsymbol{a}_{2}+l\boldsymbol{a}_{3}),"
    r"\boldsymbol{A}=(\boldsymbol{a}_{1},\boldsymbol{a}_{2},\boldsymbol{a}_{3}),"
    r"\boldsymbol{B}=\begin{pmatrix}1&0\\ 0&1\\ k&l\end{pmatrix}$,",
    r"从而 $\boldsymbol{C}=\boldsymbol{AB}$. $\because$向量组 $\boldsymbol{a}_{1},\boldsymbol{a}_{2},\boldsymbol{a}_{3}$ 线性无关，"
    r"$\therefore r(\boldsymbol{A})=3$",
    r"$\therefore r(\boldsymbol{C})=r(\boldsymbol{AB})=r(\boldsymbol{B})=2$. $\therefore$对于任意常数 $k,l$，"
    r"向量组 $\boldsymbol{a}_{1}+k\boldsymbol{a}_{3},\boldsymbol{a}_{2}+l\boldsymbol{a}_{3}$ 线性无关. 正确答案为(A).",
])

A[7] = ("B", [
    r"【答案】（B）",
    r"【解析】$\because$随机事件 $A$ 与 $B$ 相互独立",
    r"$\therefore P(A-B)=P(A)-P(AB)=P(A)-P(A)P(B)=0.3$",
    r"$\Rightarrow P(A)=0.6$",
    r"$\therefore P(B-A)=P(B)-P(AB)=P(B)-P(A)P(B)=0.2$",
])

A[8] = ("C", [
    r"【答案】（C）",
    r"【解析】$\because X_{1},X_{2}$ 相互独立且均服从 $N(0,\sigma^{2})$，"
    r"$\therefore\dfrac{X_{1}-X_{2}}{\sqrt{2}\sigma}\sim N(0,1)$，",
    r"又 $\because\left(\dfrac{X_{3}}{\sigma}\right)^{2}\sim\chi^{2}(1)$，"
    r"$\dfrac{X_{1}-X_{2}}{\sqrt{2}\sigma}$ 与 $\left(\dfrac{X_{3}}{\sigma}\right)^{2}$ 相互独立.",
    r"$\therefore S=\dfrac{\dfrac{X_{1}-X_{2}}{\sqrt{2}\sigma}}{\sqrt{\dfrac{\left(\dfrac{X_{3}}{\sigma}\right)^{2}}{1}}}"
    r"=\dfrac{X_{1}-X_{2}}{\sqrt{2}|X_{3}|}\sim t(1)$.",
])
