# -*- coding: utf-8 -*-
"""2022 数学三 解析 填空题 11-16（原卷 p9-p11，逐字照录）"""

A = {}

A[11] = (r"\sqrt{\mathrm{e}}", [
    r"【答案】$\sqrt{\mathrm{e}}$",
    r"【解析】$\lim\limits_{x\to0}\left(\dfrac{1+\mathrm{e}^{x}}{2}\right)^{\cot x}=\mathrm{e}^{\lim\limits_{x\to0}\cot x\cdot\ln\left(\frac{1+\mathrm{e}^{x}}{2}\right)}$，",
    r"$\lim\limits_{x\to0}\cot x\cdot\ln\left(\dfrac{1+\mathrm{e}^{x}}{2}\right)=\lim\limits_{x\to0}\dfrac{\ln\left(\dfrac{1+\mathrm{e}^{x}}{2}\right)}{\tan x}=\lim\limits_{x\to0}\dfrac{\dfrac{1+\mathrm{e}^{x}}{2}-1}{\tan x}=\lim\limits_{x\to0}\dfrac{1+\mathrm{e}^{x}-2}{2x}=\lim\limits_{x\to0}\dfrac{\mathrm{e}^{x}-1}{2x}=\dfrac{1}{2}$",
    r"所以原式 $=\sqrt{\mathrm{e}}$",
])

A[12] = (r"\ln3-\dfrac{\pi}{\sqrt{3}}", [
    r"【答案】$\ln3-\dfrac{\pi}{\sqrt{3}}$",
    r"【解析】$\int_{0}^{2}\dfrac{2x-4}{x^{2}+2x+4}\mathrm{d}x=\int_{0}^{2}\dfrac{2x+2}{x^{2}+2x+4}\mathrm{d}x-\int_{0}^{2}\dfrac{6}{x^{2}+2x+4}\mathrm{d}x$",
    r"$=\ln\left(x^{2}+2x+4\right)\bigg|_{0}^{2}-6\int_{0}^{2}\dfrac{1}{(x+1)^{2}+3}\mathrm{d}x$",
    r"$=\ln12-\ln4-\dfrac{6}{\sqrt{3}}\arctan\dfrac{x+1}{\sqrt{3}}\bigg|_{0}^{2}=\ln3-\dfrac{\pi}{\sqrt{3}}.$",
])

A[13] = ("0", [
    r"【答案】0",
    r"【解析】$f(x)$ 为周期为 $2\pi$ 的偶函数，$f^{\prime\prime\prime}(x)$ 为周期为 $2\pi$ 的奇函数，$f^{\prime\prime\prime}(2\pi)=f^{\prime\prime\prime}(0)=0$.",
])

A[14] = (r"\mathrm{e}^{2}-2\mathrm{e}+1", [
    r"【答案】$\mathrm{e}^{2}-2\mathrm{e}+1$",
    r"【解析】$\int_{-\infty}^{+\infty}\mathrm{d}x\int_{-\infty}^{+\infty}f(x)f(y-x)\mathrm{d}y=\int_{0}^{1}\mathrm{d}x\int_{x}^{x+1}\mathrm{e}^{x}\cdot\mathrm{e}^{y-x}\mathrm{d}y$",
    r"$=\int_{0}^{1}\mathrm{d}x\int_{x}^{x+1}\mathrm{e}^{x+1}-\mathrm{e}^{x}\mathrm{d}x=\mathrm{e}^{2}-2\mathrm{e}+1$",
])

A[15] = ("-1", [
    r"【答案】$-1$",
    r"【解析】由题可设 $B=\begin{pmatrix}-2&1&-1\\ 1&-1&0\\ -1&0&0\end{pmatrix}$",
    r"则 $E_{23}AE_{21}(-1)=B$，$A=E_{23}^{-1}BE_{21}^{-1}(-1)=E_{23}BE_{21}(1)$",
    r"$B=\begin{pmatrix}-2&1&-1\\ 1&-1&0\\ -1&0&0\end{pmatrix}\xrightarrow{E_{23}}\begin{pmatrix}-2&1&-1\\ 1&0&0\\ -1&-1&0\end{pmatrix}\xrightarrow{E_{21}(-1)}\begin{pmatrix}-1&1&-1\\ -1&0&0\\ 0&-1&0\end{pmatrix}$",
    r"即 $A=\begin{pmatrix}-1&1&-1\\ -1&0&0\\ 0&-1&0\end{pmatrix}$",
    r"$(A\vdots E)=\begin{pmatrix}-1&1&-1&1&0&0\\ -1&0&0&0&1&0\\ 0&-1&0&0&0&1\end{pmatrix}\longrightarrow\begin{pmatrix}1&0&0&0&-1&0\\ 0&1&0&0&0&-1\\ -1&1&-1&1&0&0\end{pmatrix}$",
    r"$\longrightarrow\begin{pmatrix}1&0&0&0&-1&0\\ 0&1&0&0&0&-1\\ 0&1&-1&1&-1&0\end{pmatrix}\longrightarrow\begin{pmatrix}1&0&0&0&-1&0\\ 0&1&0&0&0&-1\\ 0&0&-1&1&-1&1\end{pmatrix}$",
    r"$\longrightarrow\begin{pmatrix}1&0&0&0&-1&0\\ 0&1&0&0&0&-1\\ 0&0&1&-1&1&-1\end{pmatrix}$，故 $A^{-1}=\begin{pmatrix}0&-1&0\\ 0&0&-1\\ -1&1&-1\end{pmatrix}$，",
    r"故 $\mathrm{tr}\left(A^{-1}\right)=-1$",
])

A[16] = (r"\dfrac{5}{8}", [
    r"【答案】$\dfrac{5}{8}$",
    r"【解析】$P(B\cup C\mid A\cup B\cup C)=\dfrac{P(B\cup C)}{P(A\cup B\cup C)}$",
    r"由 $B$ 与 $C$ 相互独立知，",
    r"$P(B\cup C)=P(B)+P(C)-P(B)P(C)=\dfrac{5}{9}$，",
    r"又 $A$ 与 $B$ 互不相容，$A$ 与 $C$ 互不相容，",
    r"$P(A\cup B\cup C)=P(A)+P(B)+P(C)-P(AB)-P(AC)-P(BC)+P(ABC)$",
    r"$=P(A)+P(B)+P(C)-P(BC)=\dfrac{8}{9}$，",
    r"得 $P(B\cup C\mid A\cup B\cup C)=\dfrac{5}{8}$",
])
