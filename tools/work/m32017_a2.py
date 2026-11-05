# -*- coding: utf-8 -*-
"""2017 数学三 解析 填空题 9-14（原卷 p7-p8，逐字照录）"""

A = {}

A[9] = (r"\dfrac{\pi^{3}}{2}", [
    r"【答案】$\dfrac{\pi^{3}}{2}$.",
    r"【解析】$\displaystyle\int_{-\pi}^{\pi}\left(\sin^{3}x+\sqrt{\pi^{2}-x^{2}}\right)dx=\int_{-\pi}^{\pi}\sqrt{\pi^{2}-x^{2}}dx$",
    r"$=2\displaystyle\int_{0}^{\pi}\sqrt{\pi^{2}-x^{2}}dx\xlongequal{x=\pi\sin t}2\int_{0}^{\frac{\pi}{2}}\pi^{2}\cos^{2}tdt$",
    r"$=2\pi^{2}\displaystyle\int_{0}^{\frac{\pi}{2}}\cos^{2}tdt=\dfrac{\pi^{3}}{2}.$",
])

A[10] = (r"C2^{t}+\dfrac{1}{2}t2^{t}", [
    r"【答案】$C2^{t}+\dfrac{1}{2}t2^{t}$，$C$ 为任意常数.",
    r"【解析】$y_{t+1}-2y_{t}=0$ 的通解为 $y_{t}=C2^{t}$；设 $y_{t+1}-2y_{t}=2^{t}$ 的特解为 $y^{*}=at2^{t}$，"
    r"代入得 $a=\dfrac{1}{2}$，故 $y_{t+1}-2y_{t}=2^{t}$ 的通解为 $y_{t}=C2^{t}+\dfrac{1}{2}t2^{t}$，$C$ 为任意常数.",
])

A[11] = (r"1+e^{-Q}-Qe^{-Q}", [
    r"【答案】$1+e^{-Q}-Qe^{-Q}$.",
    r"【解析】平均成本为 $\overline{C}(Q)=\dfrac{C(Q)}{Q}=1+e^{-Q}$，总成本为 $C(Q)=Q+Qe^{-Q}$，"
    r"边际成本为 $C'(Q)=1+(1-Q)e^{-Q}$.",
])

A[12] = (r"xye^{y}", [
    r"【答案】$xye^{y}$.",
    r"【解析】由 $df(x,y)=ye^{y}dx+x(1+y)e^{y}dy=d(xye^{y})$ 得 $f(x,y)=xye^{y}+C$，",
    r"再由 $f(0,0)=0$ 得 $C=0$，故 $f(x,y)=xye^{y}$.",
])

A[13] = ("2", [
    r"【答案】2",
    r"【解析】$(\boldsymbol{A\alpha}_{1},\boldsymbol{A\alpha}_{2},\boldsymbol{A\alpha}_{3})=\boldsymbol{A}(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3})$.",
    r"因为 $\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}$ 线性无关，"
    r"所以 $(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3})$ 可逆.从而 "
    r"$r(\boldsymbol{A\alpha}_{1},\boldsymbol{A\alpha}_{2},\boldsymbol{A\alpha}_{3})=r(\boldsymbol{A})$.",
    r"由 $\boldsymbol{A}\to\begin{bmatrix}1&0&1\\ 0&1&1\\ 0&0&0\end{bmatrix}$ 得 $r(\boldsymbol{A})=2$，"
    r"故向量组 $\boldsymbol{A\alpha}_{1},\boldsymbol{A\alpha}_{2},\boldsymbol{A\alpha}_{3}$ 的秩为 2.",
])

A[14] = (r"\dfrac{9}{2}", [
    r"【答案】$\dfrac{9}{2}$.",
    r"【解析】$EX=-1+a+3b=0$，再由 $\dfrac{1}{2}+a+b=1$ 得 $a=b=\dfrac{1}{4}$，",
    r"$EX^{2}=(-2)^{2}\times\dfrac{1}{2}+1^{2}\times\dfrac{1}{4}+3^{2}\times\dfrac{1}{4}=\dfrac{9}{2}$ 所以，$DX=\dfrac{9}{2}$.",
])
