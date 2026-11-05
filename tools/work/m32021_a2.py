# -*- coding: utf-8 -*-
"""2021 数学三 解析 填空题 11-16（原卷 p8-p9，逐字照录）"""

A = {}

A[11] = (r"\dfrac{\sin e^{-1}}{2e}", [
    r"【答案】$\dfrac{\sin e^{-1}}{2e}$",
    r"【解析】$y'\Big|_{x=1}=\dfrac{e^{-\sqrt{x}}\sin e^{-\sqrt{x}}}{2\sqrt{x}}\Big|_{x=1}=\dfrac{\sin e^{-1}}{2e}$",
])

A[12] = ("6", [
    r"【答案】6",
    r"【解析】",
    r"$\displaystyle\int_{\sqrt{5}}^{5}\dfrac{x}{\sqrt{|x^{2}-9|}}dx=\int_{\sqrt{5}}^{3}\dfrac{x}{\sqrt{9-x^{2}}}dx"
    r"+\int_{3}^{5}\dfrac{x}{\sqrt{x^{2}-9}}dx=-\dfrac{1}{2}\int_{\sqrt{5}}^{3}\dfrac{d\left(9-x^{2}\right)}{\sqrt{9-x^{2}}}"
    r"+\dfrac{1}{2}\int_{3}^{5}\dfrac{d\left(x^{2}-9\right)}{\sqrt{x^{2}-9}}$",
    r"$=-\dfrac{1}{2}\cdot2\sqrt{9-x^{2}}\Big|_{\sqrt{5}}^{3}+\dfrac{1}{2}\cdot2\sqrt{x^{2}-9}\Big|_{3}^{5}=6.$",
])

A[13] = (r"\dfrac{\pi}{4}", [
    r"【答案】$\dfrac{\pi}{4}$",
    r"【解析】$V=\displaystyle\int_{0}^{1}\pi y^{2}(x)dx=\int_{0}^{1}\pi x\cdot\sin^{2}\pi xdx"
    r"\xlongequal{x=t/\pi}\dfrac{1}{\pi}\int_{0}^{\pi}t\sin^{2}tdt$",
    r"$=\dfrac{1}{\pi}\cdot\dfrac{\pi}{2}\int_{0}^{\pi}\sin^{2}tdt=\dfrac{\pi}{4}$",
])

A[14] = (r"y_{t}=C+\dfrac{t}{2}(t-1)", [
    r"【答案】$y_{t}=C+\dfrac{t}{2}(t-1)$（C 为任意常数）",
    r"【解析】齐次差分方程 $y_{t+1}-y_{t}=0$，即齐次方程的通解为 C（C 为任意常数），",
    r"设特解 $y_{t}^{*}=t\left(A_{0}+A_{1}t\right)$，代入原方程得 $(t+1)\left(A_{0}+A_{1}(t+1)\right)-t\left(A_{0}+A_{1}t\right)=t$，",
    r"$A_{0}+2A_{1}t+A_{1}=t$，解得 $A_{0}=-\dfrac{1}{2},A_{1}=\dfrac{1}{2}$，"
    r"故通解为 $y_{t}=C+\dfrac{t}{2}(t-1)$（C 为任意常数）.",
])

A[15] = ("-5", [
    r"【答案】-5",
    r"【解析】解法一：按照第一行进行行列式展开，",
    r"$f(x)=x\begin{vmatrix}x&2&-1\\ 1&x&1\\ -1&1&x\end{vmatrix}"
    r"-x\begin{vmatrix}1&2&-1\\ 2&x&1\\ 2&1&x\end{vmatrix}"
    r"+2\begin{vmatrix}1&x&-1\\ 2&1&1\\ 2&-1&x\end{vmatrix}"
    r"-2x\begin{vmatrix}1&x&2\\ 2&1&x\\ 2&-1&1\end{vmatrix}$",
    r"$x\begin{vmatrix}x&2&-1\\ 1&x&1\\ -1&1&x\end{vmatrix}$ 中没有 $x^{3}$ 项，"
    r"$-x\begin{vmatrix}1&2&-1\\ 2&x&1\\ 2&1&x\end{vmatrix}$ 中 $x^{3}$ 项的系数为 $-1$，"
    r"$\begin{vmatrix}1&x&-1\\ 2&1&1\\ 2&-1&x\end{vmatrix}$ 中没有 $x^{3}$ 项，",
    r"$-2x\begin{vmatrix}1&x&2\\ 2&1&x\\ 2&-1&1\end{vmatrix}$ 中 $x^{3}$ 项的系数为 $-4$，故 $f(x)$ 中 $x^{3}$ 项的系数为 $-5$.",
    r"解法二：根据行列式定义，行列式为不同行不同列对应元素乘积的代数和，",
    r"$f(x)=\begin{vmatrix}x&x&1&2x\\ 1&x&2&-1\\ 2&1&x&1\\ 2&-1&1&x\end{vmatrix}$ "
    r"的含 $x^{3}$ 项分别为 $-a_{12}a_{21}a_{33}a_{44}$ 和 $-a_{14}a_{22}a_{33}a_{41}$，即 $-x^{3}$ 和 $-4x^{3}$，",
    r"故 $f(x)$ 中 $x^{3}$ 项的系数为 -5.",
])

A[16] = (r"\dfrac{1}{5}", [
    r"【答案】$\dfrac{1}{5}$",
    r"$X$ 的取值为 0 和 1，分布律为",
    r"$\begin{array}{|c|cc|}\hline X&0&1\\\hline P&0.5&0.5\\\hline\end{array}$",
    r"$EX=0.5,DX=0.25$",
    r"$P\{Y=0\}=P\{X=0\}\cdot P\{Y=0|X=0\}+P\{X=1\}\cdot P\{Y=0|X=1\}=\dfrac{1}{2}$",
    r"同理 $P\{Y=1\}=\dfrac{1}{2}$.",
    r"故 $Y$ 的取值为 0 和 1，分布律为",
    r"$\begin{array}{|c|cc|}\hline Y&0&1\\\hline P&0.5&0.5\\\hline\end{array}$",
    r"$P\{XY=1\}=P\{X=1,Y=1\}=P\{X=1\}\cdot P\{Y=1|X=1\}=\dfrac{1}{2}\times\dfrac{3}{5}=\dfrac{3}{10}$",
    r"故",
    r"$\begin{array}{|c|cc|}\hline XY&0&1\\\hline P&0.7&0.3\\\hline\end{array}$",
    r"$\rho_{XY}=\dfrac{EXY-EXEY}{\sqrt{DX}\sqrt{DY}}=\dfrac{\dfrac{3}{10}-\dfrac{1}{2}\times\dfrac{1}{2}}{\dfrac{1}{2}\times\dfrac{1}{2}}=\dfrac{1}{5}$",
])
