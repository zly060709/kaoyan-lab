# -*- coding: utf-8 -*-
"""2014 数学三 解析 填空题 9-14（原卷 p6-p8，逐字照录）"""

A = {}

A[9] = (r"20-Q", [
    r"【答案】$20-Q$",
    r"【解析】$S(Q)=Qp=Q(20-\dfrac{1}{2}Q)$，所以 $S'(Q)=Qp=20-Q$.",
])

A[10] = (r"\dfrac{3}{2}-\ln 2", [
    r"【答案】$\dfrac{3}{2}-\ln2$",
    r"【解析】实质为由 $y=-x$，$y=2$，$y=-\dfrac{1}{x}$ 围成的 $Y$ 型区域，所以",
    r"$S=\displaystyle\int_{1}^{2}(-\dfrac{1}{y}+y)dy=\dfrac{3}{2}-\ln2$.",
])

A[11] = (r"\dfrac{1}{2}", [
    r"【答案】$\dfrac{1}{2}$",
    r"【解析】利用分部积分得",
    r"$\displaystyle\int_{0}^{a}xe^{2x}dx=\dfrac{1}{2}\int_{0}^{a}xde^{2x}=\dfrac{1}{2}xe^{2x}\Big|_{0}^{a}"
    r"-\dfrac{1}{2}\int_{0}^{a}e^{2x}dx=\dfrac{1}{2}ae^{2a}-\dfrac{1}{4}e^{2x}\Big|_{0}^{a}"
    r"=\dfrac{1}{2}ae^{2a}-\dfrac{1}{4}e^{2a}+\dfrac{1}{4}$,",
    r"$=\left(\dfrac{1}{2}a-\dfrac{1}{4}\right)e^{2a}+\dfrac{1}{4}=\dfrac{1}{4}$；所以 $\dfrac{1}{2}a-\dfrac{1}{4}=0$，"
    r"故 $a=\dfrac{1}{2}$.",
])

A[12] = (r"\dfrac{1}{2}(e-1)", [
    r"【答案】$\dfrac{1}{2}(e-1)$",
    r"【解析】被积函数 $\dfrac{e^{x^{2}}}{x}-e^{y^{2}}$ 分开计算得",
    r"$\displaystyle\int_{0}^{1}dy\int_{y}^{1}\left(\dfrac{e^{x^{2}}}{x}-e^{y^{2}}\right)dx"
    r"=\int_{0}^{1}dy\int_{y}^{1}\dfrac{e^{x^{2}}}{x}dx-\int_{0}^{1}dy\int_{y}^{1}e^{y^{2}}dx"
    r"=\int_{0}^{1}dx\int_{0}^{x}\dfrac{e^{x^{2}}}{x}dy-\int_{0}^{1}dy\int_{y}^{1}e^{y^{2}}dx$",
    r"由于 $\displaystyle\int_{0}^{1}dx\int_{0}^{x}\dfrac{e^{x^{2}}}{x}dy=\int_{0}^{1}e^{x^{2}}dx$，"
    r"$\displaystyle\int_{0}^{1}e^{y^{2}}(y-1)dy=\int_{0}^{1}ye^{y^{2}}dy-\int_{0}^{1}e^{y^{2}}dy$",
    r"所以",
    r"$\displaystyle\int_{0}^{1}dx\int_{0}^{x}\dfrac{e^{x^{2}}}{x}dy-\int_{0}^{1}dy\int_{y}^{1}e^{y^{2}}dx"
    r"=\int_{0}^{1}e^{x^{2}}dx+\int_{0}^{1}ye^{y^{2}}dy-\int_{0}^{1}e^{y^{2}}dy"
    r"=\int_{0}^{1}ye^{y^{2}}dy=\dfrac{1}{2}(e-1)$.",
])

A[13] = (r"[-2,2]", [
    r"【答案】$[-2,2]$",
    r"【解析】解法一：二次型的矩阵",
    r"$\boldsymbol{A}=\begin{pmatrix}1&0&a\\ 0&-1&2\\ a&2&0\end{pmatrix}$",
    r"从而知其三个特征值之和为 0.",
    r"又因为其负惯性指数为 1，所以 $|\boldsymbol{A}|\leqslant0$，即 $|\boldsymbol{A}|=a^{2}-4\leqslant0\Rightarrow-2\leqslant a\leqslant2$.",
    r"解法二：$f\left(x_{1},x_{2},x_{3}\right)=\left(x_{1}-ax_{3}\right)^{2}-\left(x_{2}-2x_{3}\right)^{2}"
    r"+\left(4-a^{2}\right)x_{3}^{2}$，因为负惯性指数为 1，故",
    r"$4-a^{2}\geqslant0$，即 $-2\leqslant a\leqslant2$.",
])

A[14] = (r"\dfrac{2}{5n}", [
    r"【答案】$\dfrac{2}{5n}$",
    r"【解析】$EX_{i}^{2}=\displaystyle\int_{-\infty}^{+\infty}x^{2}f(x)dx=\int_{\theta}^{2\theta}x^{2}\dfrac{2x}{3\theta^{2}}dx=\dfrac{5}{2}\theta^{2}$，",
    r"从而 $E\Bigl[c\displaystyle\sum\limits_{n=1}^{\infty}X_{i}^{2}\Bigr]=cE\Bigl[\sum\limits_{n=1}^{\infty}X_{i}^{2}\Bigr]"
    r"=cn\dfrac{5}{2}\theta^{2}=\theta^{2}$，",
    r"$\Rightarrow c=\dfrac{2}{5n}$.",
])
