# -*- coding: utf-8 -*-
"""2019 数学三 解析 选择题 1-8（原卷 p5-p6，逐字照录）"""

A = {}

A[1] = ("C", [
    r"【答案】(C)",
    r"【解析】当 $x\to0$ 时，$x-\tan x\sim-\dfrac{x^{3}}{3}$，则 $k=3$，所以选（C）",
])

A[2] = ("D", [
    r"【答案】(D)",
    r"【解析】令 $f(x)=x^{5}-5x+k$，由 $f'(x)=5x^{4}-5=0$ 得 $x=\pm1$，当 $x<-1$ 时，$f'(x)>0$，",
    r"当 $-1<x<1$ 时，$f'(x)<0$，当 $x>1$ 时，$f'(x)>0$，又由于 $\lim\limits_{x\to-\infty}f(x)=-\infty$，",
    r"$\lim\limits_{x\to+\infty}f(x)=+\infty$，方程要有三个不等实根，只需要 $f(-1)=4+k>0$，$f(1)=-4+k<0$，",
    r"因此 $k$ 的取值范围为 $-4<k<4$",
])

A[3] = ("D", [
    r"【答案】(D)",
    r"【解析】由通解形式知，$\lambda_{1}=\lambda_{2}=-1$，故特征方程为 $(\lambda+1)^{2}=\lambda^{2}+2\lambda+1=0$，所以",
    r"$a=2,b=1$，又由于 $y^{*}=e^{x}$ 是 $y''+2y'+y=ce^{x}$ 的特解，代入得 $c=4$",
])

A[4] = ("B", [
    r"【答案】(B)",
    r"【解析】由 $\displaystyle\sum\limits_{n=1}^{\infty}\dfrac{v_{n}}{n}$ 条件收敛知，$\lim\limits_{n\to\infty}\dfrac{v_{n}}{n}=0$，"
    r"故当 $n$ 充分大时，$\Bigl|\dfrac{v_{n}}{n}\Bigr|\leqslant1$.",
    r"所以 $|u_{n}v_{n}|=\Bigl|nu_{n}\cdot\dfrac{v_{n}}{n}\Bigr|\leqslant|nu_{n}|$，由于 $\displaystyle\sum\limits_{n=1}^{\infty}nu_{n}$ 绝对收敛，"
    r"所以 $\displaystyle\sum\limits_{n=1}^{\infty}u_{n}v_{n}$ 绝对收敛.",
    r"由 $\displaystyle\sum\limits_{n=1}^{\infty}nu_{n}$ 绝对收敛，$\lim\limits_{x\to\infty}\dfrac{|u_{n}|}{|nu_{n}|}=0$，"
    r"可知 $\displaystyle\sum\limits_{n=1}^{\infty}u_{n}$ 也对决收敛；而由 $\displaystyle\sum\limits_{n=1}^{\infty}\dfrac{v_{n}}{n}$ 条件收敛时，"
    r"$\displaystyle\sum\limits_{n=1}^{\infty}v_{n}$ 敛散性不确定.",
    r"例如：$v_{n}=(-1)^{n}$，$\displaystyle\sum\limits_{n=1}^{\infty}\dfrac{v_{n}}{n}$ 条件收敛，但是 $\displaystyle\sum\limits_{n=1}^{\infty}v_{n}$ 发散.",
    r"$v_{n}=\dfrac{(-1)^{n}}{\ln(n+1)}$，$\displaystyle\sum\limits_{n=1}^{\infty}\dfrac{v_{n}}{n}$ 条件收敛，但是 $\displaystyle\sum\limits_{n=1}^{\infty}v_{n}$ 收敛.",
])

A[5] = ("A", [
    r"【答案】(A)",
    r"【解析】由于方程组基础解系中只有 2 个向量，则 $r(A)=2<3$，所以 $r(A^{*})=0$",
])

A[6] = ("C", [
    r"【答案】(C)",
    r"【解析】由 $A^{2}+A=2E$，可知矩阵的特征值满足方程 $\lambda^{2}+\lambda-2=0$，解得，$\lambda=1$ 或 $\lambda=-2$.",
    r"再由 $|A|=4$，可知 $\lambda_{1}=1,\lambda_{2}=\lambda_{3}=-2$，所以规范形为 $y_{1}^{2}-y_{2}^{2}-y_{3}^{2}$.故答案选（C）",
])

A[7] = ("C", [
    r"【答案】(C)",
    r"【解析】$P(A\overline{B})=P(B\overline{A})\Leftrightarrow P(A)-P(AB)=P(B)-P(AB)\Leftrightarrow P(A)=P(B)$；故选（C）",
])

A[8] = ("A", [
    r"【答案】(A)",
    r"【解析】",
    r"因为 $X\sim N(\mu,\sigma^{2}),Y\sim N(\mu,\sigma^{2})$，且 $X,Y$ 相互独立，所以 $X-Y\sim N(0,2\sigma^{2})$，所以",
    r"$P\{|X-Y|<1\}=\Phi\Bigl(\dfrac{1-0}{\sqrt{2}\sigma}\Bigr)-\Phi\Bigl(\dfrac{-1-0}{\sqrt{2}\sigma}\Bigr)=2\Phi\Bigl(\dfrac{1}{\sqrt{2}\sigma}\Bigr)-1$；选（A）",
])
