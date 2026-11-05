# -*- coding: utf-8 -*-
"""2019 数学三 解析 填空题 9-14（原卷 p6-p7，逐字照录）"""

A = {}

A[9] = (r"e^{-1}", [
    r"【答案】$e^{-1}$.",
    r"【解析】$\Bigl[\dfrac{1}{1\times2}+\dfrac{1}{2\times3}+\cdots+\dfrac{1}{n\times(n+1)}\Bigr]^{n}=\Bigl(\dfrac{n}{n+1}\Bigr)^{n}$，"
    r"则 $\lim\limits_{n\to\infty}\Bigl(\dfrac{n}{n+1}\Bigr)^{n}=e^{-1}$.",
])

A[10] = (r"(\pi,-2)", [
    r"【答案】$(\pi,-2)$",
    r"【解析】令 $y''=-x\sin x=0$，可得 $x=0$ 或 $x=\pi$，又 $y'''=-\sin x-x\cos x$，因 $y'''(0)=0$，",
    r"$y'''(\pi)=\pi\neq0$，因此拐点坐标为 $(\pi,-2)$.",
])

A[11] = (r"\dfrac{1}{18}(1-2\sqrt{2})", [
    r"【答案】$\dfrac{1}{18}(1-2\sqrt{2})$",
    r"【解析】$f'(x)=\sqrt{1+x^{4}}$，且 $f(1)=0$.因此",
    r"$\displaystyle\int_{0}^{1}x^{2}f(x)\mathrm{d}x=\dfrac{1}{3}\int_{0}^{1}f(x)\mathrm{d}x^{3}"
    r"=\dfrac{1}{3}\Bigl[x^{3}f(x)\Bigr|_{0}^{1}-\int_{0}^{1}x^{3}\sqrt{1+x^{4}}\mathrm{d}x\Bigr]=\dfrac{1}{18}(1-2\sqrt{2})$.",
])

A[12] = ("0.4", [
    r"【答案】0.4",
    r"【解析】因为 $\eta_{AA}=-\dfrac{p_{A}}{Q_{A}}\cdot\dfrac{\partial Q_{A}}{\partial p_{A}}=-\dfrac{p_{A}}{Q_{A}}\cdot(-2p_{A}-p_{B})$，"
    r"将 $p_{A}=10,p_{B}=20,Q_{A}=1000$ 代入，可得 $\eta_{AA}=0.4$",
])

A[13] = ("1", [
    r"【答案】1",
    r"【解析】因为 $A\boldsymbol{x}=\boldsymbol{b}$ 由无穷多解，故 $r(A)=r(A,b)<3$，对矩阵 $(A,b)$ 作初等行变换，因为",
    r"$(A,b)\to\begin{pmatrix}1&0&-1&0\\ 0&1&0&1\\ 0&0&a^{2}-1&a-1\end{pmatrix}$，",
    r"故 $a^{2}-1=a-1=0$，因此 $a=1$",
])

A[14] = (r"\dfrac{2}{3}", [
    r"【答案】$\dfrac{2}{3}$.",
    r"【解析】由条件可得 $EX=\displaystyle\int_{-\infty}^{+\infty}xf(x)\mathrm{d}x=\int_{0}^{2}\dfrac{x^{2}}{2}\mathrm{d}x=\dfrac{4}{3}$，"
    r"且可求得分布函数",
    r"$F(x)=\begin{cases}0,&x<0,\\ \dfrac{x^{2}}{4},&0\leqslant x<2,\\ 1,&x\geqslant2.\end{cases}$",
    r"故可得",
    r"$P\{F(X)>EX-1\}=P\Bigl\{\dfrac{X^{2}}{4}>\dfrac{1}{3}\Bigr\}=P\Bigl\{X>\dfrac{2}{\sqrt{3}}\Bigr\}+P\Bigl\{X<-\dfrac{2}{\sqrt{3}}\Bigr\}"
    r"=\displaystyle\int_{\frac{2}{\sqrt{3}}}^{2}\dfrac{x}{2}\mathrm{d}x+0=\dfrac{x^{2}}{4}\Bigl|_{\frac{2}{\sqrt{3}}}^{2}=\dfrac{2}{3}.$",
])
