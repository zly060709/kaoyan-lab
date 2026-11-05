# -*- coding: utf-8 -*-
"""2017 数学三 解析 选择题 1-8（原卷 p5-p7，逐字照录）"""

A = {}

A[1] = ("A", [
    r"【答案】A",
    r"【解析】$f(0+0)=\lim\limits_{x\to0^{+}}\dfrac{1-\cos\sqrt{x}}{ax}=\dfrac{1}{2a}$，$f(0)=f(0-0)=b$，",
    r"因为 $f(x)$ 在 $x=0$ 处连续，所以 $f(0+0)=f(0)=f(0-0)$，从而 $ab=\dfrac{1}{2}$，应选（A）",
])

A[2] = ("D", [
    r"【答案】D",
    r"【解析】由 $\begin{cases}z'_{x}=3y-2xy-y^{2}=0\\ z'_{y}=3x-2xy-x^{2}=0\end{cases}$，"
    r"得 $\begin{cases}x=0\\ y=0\end{cases}$，$\begin{cases}x=1\\ y=1\end{cases}$，$\begin{cases}x=0\\ y=3\end{cases}$，$\begin{cases}x=3\\ y=0\end{cases}$，",
    r"$z''_{xx}=-2y$，$z''_{xy}=3-2x-2y$，$z''_{yy}=-2x$，",
    r"当 $(x,y)=(0,0),(0,3),(3,0)$ 时，$AC-B^{2}<0$ 成立，则都不是极值点；",
    r"当 $(x,y)=(1,1)$ 时，$AC-B^{2}=3>0$ 且 $A=-2<0$，则 $(1,1)$ 为极值点，应选（D）.",
])

A[3] = ("C", [
    r"【答案】C",
    r"【解析】若 $f(x)>0$，则 $f'(x)>0$，从而 $f(1)>f(-1)>0$；",
    r"若 $f(x)<0$，则 $f'(x)<0$，从而 $f(1)<f(-1)<0$，故 $|f(1)|>|f(-1)|$，应选（C）",
    r"方法二：令 $F(x)=f^{2}(x)$，则 $F'(x)=2f(x)f'(x)>0$，所以 $F(x)$ 单调递增.",
    r"故 $F(1)>F(-1)$，即 $f^{2}(1)>f^{2}(-1)$，可得 $|f(1)|>|f(-1)|$，选 C.",
])

A[4] = ("C", [
    r"【答案】C",
    r"【解析】$\sin x=x-\dfrac{1}{6}x^{3}+o\left(x^{3}\right)$ 得 $\sin\dfrac{1}{n}=\dfrac{1}{n}-\dfrac{1}{6n^{3}}+o\left(\dfrac{1}{n^{3}}\right)$，",
    r"由 $\ln(1+x)=x-\dfrac{x^{2}}{2}+o\left(x^{2}\right)$ 得 $\ln\left(1-\dfrac{1}{n}\right)=-\dfrac{1}{n}-\dfrac{1}{2n^{2}}+o\left(\dfrac{1}{n^{2}}\right)$，",
    r"于是 $\sin\dfrac{1}{n}-k\ln\left(1-\dfrac{1}{n}\right)=(k+1)\dfrac{1}{n}+\dfrac{k}{2n^{2}}+o\left(\dfrac{1}{n^{2}}\right)$，",
    r"由 $\sum\limits_{n=2}^{\infty}\left[\sin\dfrac{1}{n}-k\ln\left(1-\dfrac{1}{n}\right)\right]$ 收敛得 $k=-1$，应选（C）",
])

A[5] = ("A", [
    r"【答案】A",
    r"【解析】令 $\boldsymbol{A}=\boldsymbol{\alpha}\boldsymbol{\alpha}^{T}$，$\boldsymbol{A}^{2}=\boldsymbol{A}$，",
    r"令 $\boldsymbol{AX}=\lambda\boldsymbol{X}$，由 $(\boldsymbol{A}^{2}-\boldsymbol{A})\boldsymbol{X}=(\lambda^{2}-\lambda)\boldsymbol{X}=\boldsymbol{0}$ "
    r"得 $\lambda^{2}-\lambda=0$，$\lambda=0$ 或 $\lambda=1$，",
    r"因为 $tr(\boldsymbol{A})=\boldsymbol{\alpha}^{T}\boldsymbol{\alpha}=1=\lambda_{1}+\cdots+\lambda_{n}$ 得 "
    r"$\boldsymbol{A}$ 的特征值为 $\lambda_{1}=\cdots=\lambda_{n-1}=0,\lambda_{n}=1$",
    r"$\boldsymbol{E}-\boldsymbol{\alpha}\boldsymbol{\alpha}^{T}$ 的特征值为 $\lambda_{1}=\cdots=\lambda_{n-1}=1$，"
    r"$\lambda_{n}=0$,从而 $\left|\boldsymbol{E}-\boldsymbol{\alpha}\boldsymbol{\alpha}^{T}\right|=0$，",
    r"即 $\boldsymbol{E}-\boldsymbol{\alpha}\boldsymbol{\alpha}^{T}$ 不可逆，应选（A）.",
])

A[6] = ("B", [
    r"【答案】B",
    r"【解析】$\boldsymbol{A},\boldsymbol{B},\boldsymbol{C}$ 的特征值为 $\lambda_{1}=\lambda_{2}=2,\lambda_{3}=1$，",
    r"由 $2\boldsymbol{E}-\boldsymbol{A}=\begin{pmatrix}0&0&0\\ 0&0&-1\\ 0&0&1\end{pmatrix}$ 得 $r(2\boldsymbol{E}-\boldsymbol{A})=1$，"
    r"则 $\boldsymbol{A}$ 可相似对角化，从而 $\boldsymbol{A}$ 与 $\boldsymbol{C}$ 相似；",
    r"由 $2\boldsymbol{E}-\boldsymbol{B}=\begin{pmatrix}0&-1&0\\ 0&0&0\\ 0&0&1\end{pmatrix}$ 得 $r(2\boldsymbol{E}-\boldsymbol{B})=2$，"
    r"则 $\boldsymbol{B}$ 不可相似对角化，从而 $\boldsymbol{B}$ 与 $\boldsymbol{A},\boldsymbol{C}$ 不相似；应选（B）.",
])

A[7] = ("C", [
    r"【答案】C",
    r"【解析】",
    r"$P\left[(A+B)C\right]=P\left[AC+BC\right]=P(AC)+P(BC)-P(ABC)$",
    r"$=P(A)P(C)+P(B)P(C)-P(ABC)$，",
    r"$P(A+B)P(C)=\left[P(A)+P(B)-P(AB)\right]P(C)$",
    r"$=P(A)P(C)+P(B)P(C)-P(AB)P(C)$",
    r"$A\cup B$ 与 $C$ 独立即 $P\left[(A+B)C\right]=P(A+B)P(C)$ 的充分必要条件为",
    r"$P(A)P(C)+P(B)P(C)-P(ABC)=P(A)P(C)+P(B)P(C)-P(AB)P(C)$，",
    r"$P(ABC)=P(AB)P(C)$，即 $AB$ 与 $C$ 独立，应选（C）",
])

A[8] = ("B", [
    r"【答案】B",
    r"【解析】若总体 $X\sim N(\mu,\sigma^{2})$，则 $\dfrac{1}{\sigma^{2}}\sum\limits_{i=1}^{n}(X_{i}-\mu)^{2}\sim\chi^{2}(n)$，",
    r"$\dfrac{1}{\sigma^{2}}\sum\limits_{i=1}^{n}(X_{i}-\overline{X})^{2}\sim\chi^{2}(n-1)$，"
    r"因为总体 $X\sim N(\mu,1)$，所以 $\sum\limits_{i=1}^{n}(X_{i}-\mu)^{2}\sim\chi^{2}(n)$",
    r"$\sum\limits_{i=1}^{n}(X_{i}-\overline{X})^{2}\sim\chi^{2}(n-1)$，再由 $\overline{X}\sim N\left(\mu,\dfrac{1}{n}\right)$ 得 "
    r"$\dfrac{\overline{X}-\mu}{\dfrac{1}{\sqrt{n}}}=\sqrt{n}(\overline{X}-\mu)\sim N(0,1)$",
    r"从而 $n(\overline{X}-\mu)^{2}\sim\chi^{2}(1)$，不正确的是（B），应选（B）",
])
