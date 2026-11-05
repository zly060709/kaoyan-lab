# -*- coding: utf-8 -*-
"""2016 数学三 解析 选择题 1-8（原卷 p5-p7，逐字照录）"""

A = {}

A[1] = ("B", [
    r"【答案】B.",
    r"【解析】对图像进行标记，可知 $x_{1},x_{3},x_{5}$ 为驻点，而在 $x_{1}$ 和 $x_{3}$ 两侧 $f'(x)$ 变号，则为极值点，",
    r"$x_{5}$ 两侧 $f'(x)$ 不变号，则不是极值点，在 $x_{2}$ 处一阶导数不存在，但在 $x_{2}$ 两侧 $f'(x)$ 不变号，",
    r"则不是极值点，在 $x_{2}$ 处二阶导数不存在，在 $x_{4}$ 和 $x_{5}$ 处二阶导数为零，在这三个点两侧一阶",
    r"导函数增减性发生变化，则都为拐点，故应选（B）.",
])

A[2] = ("D", [
    r"【答案】D.",
    r"【解析】$f_{x}'=\dfrac{e^{x}(x-y)-e^{x}}{(x-y)^{2}},f_{y}'=\dfrac{e^{x}}{(x-y)^{2}}$, 因而 $f_{x}'+f_{y}'=\dfrac{e^{x}}{x-y}=f$.",
])

A[3] = ("B", [
    r"【答案】B.",
    r"【解析】$D_{1}$ 关于直线 $y=x$ 对称，$J_{1}=\dfrac{1}{2}\displaystyle\iint\limits_{D_{1}}(\sqrt[3]{x-y}+\sqrt[3]{y-x})dxdy=0.$",
    r"$D_{1}$ 被直线 $y=x$ 对分成的两个积分区域记为 $D_{11}$ 及 $D_{12}$，则",
    r"$\displaystyle\iint\limits_{D_{11}}\sqrt[3]{x-y}dxdy=-\displaystyle\iint\limits_{D_{12}}\sqrt[3]{x-y}dxdy$，"
    r"$\displaystyle\iint\limits_{D_{11}}\sqrt[3]{x-y}dxdy<0,\displaystyle\iint\limits_{D_{12}}\sqrt[3]{x-y}dxdy>0$",
    r"如图所示,",
    r"$J_{2}=\displaystyle\iint\limits_{D_{2}}\sqrt[3]{x-y}dxdy=\displaystyle\iint\limits_{D_{21}}\sqrt[3]{x-y}dxdy"
    r"+\displaystyle\iint\limits_{D_{22}}\sqrt[3]{x-y}dxdy+\displaystyle\iint\limits_{D_{23}}\sqrt[3]{x-y}dxdy$,",
    r"$J_{3}=\displaystyle\iint\limits_{D_{3}}\sqrt[3]{x-y}dxdy=\displaystyle\iint\limits_{D_{31}}\sqrt[3]{x-y}dxdy"
    r"+\displaystyle\iint\limits_{D_{32}}\sqrt[3]{x-y}dxdy+\displaystyle\iint\limits_{D_{33}}\sqrt[3]{x-y}dxdy$,",
    r"由轮换对称性可知：$\displaystyle\iint\limits_{D_{31}}\sqrt[3]{x-y}dxdy=-\displaystyle\iint\limits_{D_{32}}\sqrt[3]{x-y}dxdy$；",
    r"故 $J_{2}=\displaystyle\iint\limits_{D_{2}}\sqrt[3]{x-y}dxdy=\displaystyle\iint\limits_{D_{23}}\sqrt[3]{x-y}dxdy>0$，",
    r"$J_{3}=\displaystyle\iint\limits_{D_{3}}\sqrt[3]{x-y}dxdy=\displaystyle\iint\limits_{D_{33}}\sqrt[3]{x-y}dxdy<0$,",
    r"故 $J_{3}<J_{1}<J_{2}$，选（B）.",
])

A[4] = ("A", [
    r"【答案】A.",
    r"【解析】$\Bigl|\Bigl(\dfrac{1}{\sqrt{n}}-\dfrac{1}{\sqrt{n+1}}\Bigr)\sin(n+k)\Bigr|\leqslant\dfrac{1}{\sqrt{n}}-\dfrac{1}{\sqrt{n+1}}$",
    r"$=\dfrac{\sqrt{n+1}-\sqrt{n}}{\sqrt{n(n+1)}}=\dfrac{1}{\sqrt{n(n+1)}(\sqrt{n+1}+\sqrt{n})}\leqslant\dfrac{1}{n^{\frac{3}{2}}}$"
    r" 因而级数绝对收敛，选（A）.",
])

A[5] = ("C", [
    r"【答案】C.",
    r"【解析】由已知条件，存在可逆矩阵 $P$ 使得 $P^{-1}AP=B.$",
    r"那么 $B^{\mathrm{T}}=(P^{-1}AP)^{\mathrm{T}}=P^{\mathrm{T}}A^{\mathrm{T}}(P^{-1})^{\mathrm{T}}=P_{1}^{-1}A^{\mathrm{T}}P_{1}$，"
    r"其中 $P_{1}=(P^{\mathrm{T}})^{-1}$，即 $A^{\mathrm{T}}$ 和 $B^{\mathrm{T}}$ 相似，（A）正确.",
    r"$B^{-1}=(P^{-1}AP)^{-1}=P^{-1}A^{-1}(P^{-1})^{-1}=P^{-1}A^{-1}P$，即 $A^{-1}$ 和 $B^{-1}$ 相似，（B）正确.",
    r"又 $P^{-1}(A+A^{-1})P=P^{-1}AP+P^{-1}A^{-1}P=B+B^{-1}$，即 $A+A^{-1}$ 和 $B+B^{-1}$ 相似，（D）正确，",
    r"故选 C.",
])

A[6] = ("C", [
    r"【答案】C.",
    r"【解析】二次型矩阵 $A=\begin{pmatrix}a&1&1\\ 1&a&1\\ 1&1&a\end{pmatrix}$",
    r"由特征多项式 $|\lambda E-A|=\begin{vmatrix}\lambda-a&-1&-1\\ -1&\lambda-a&-1\\ -1&-1&\lambda-a\end{vmatrix}"
    r"=(\lambda-a-2)(\lambda-a+1)^{2}$,",
    r"矩阵 $A$ 的特征值，$a+2,a-1,a-1.$ 由 $p=1,q=2$，$\begin{cases}a+2>0\\ a-1<0\end{cases}\therefore-2<a<1.$",
])

A[7] = ("A", [
    r"【答案】A.",
    r"【解析】$P(A|B)=1,$ 则 $P(\overline{A}|B)=0$ 也就有 $P(\overline{A}B)=0$，",
    r"$P(B|\overline{A})=0$ 得 $P(\overline{B}|\overline{A})=1.$",
])

A[8] = ("C", [
    r"【答案】C.",
    r"【解析】$D(XY)=E(XY)^{2}-(EXY)^{2}=EX^{2}EY^{2}-(EXEY)^{2}$",
    r"$=\Bigl[DX+(EX)^{2}\Bigr]\Bigl[DY+(EY)^{2}\Bigr]-1^{2}=14.$",
])
