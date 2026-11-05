# -*- coding: utf-8 -*-
"""2010 数学一 解析 填空题 9-14（原卷 p7-p8，逐字照录【答案】【详解】）"""

A = {}

A[9] = ("0", [
    r"【答案】0.",
    r"【详解】",
    r"$\dfrac{dy}{dx}=\dfrac{y'(t)}{x'(t)}=\dfrac{\ln(1+t^{2})}{-e^{-t}}$",
    r"$\dfrac{d^{2}y}{dx^{2}}=\dfrac{d}{dx}\left(\dfrac{dy}{dx}\right)=\dfrac{d}{dt}\left(\dfrac{dy}{dx}\right)\dfrac{dt}{dx}"
    r"=\left(\dfrac{\ln(1+t^{2})}{-e^{-t}}\right)'\dfrac{1}{x'(t)}$",
    r"$=-\dfrac{\dfrac{2t}{1+t^{2}}e^{-t}+\ln(1+t^{2})e^{-t}}{\left(e^{-t}\right)^{2}}\times\dfrac{1}{-e^{-t}}"
    r"=e^{2t}\left(\dfrac{2t}{1+t^{2}}+\ln(1+t^{2})\right)$",
    r"$\Rightarrow\dfrac{d^{2}y}{dx^{2}}\Big|_{t=0}=0$",
])

A[10] = (r"-4\pi", [
    r"【答案】$-4\pi$",
    r"【详解】令 $\sqrt{x}=t$, 原式为",
    r"$2\int_{0}^{\pi}t^{2}\cos t\,dt=2\left(t^{2}\sin t\big|_{0}^{\pi}-\int_{0}^{\pi}2t\sin t\,dt\right)"
    r"=-4\int_{0}^{\pi}t\sin t\,dt=4\left(t\cos t\big|_{0}^{\pi}-\int_{0}^{\pi}\cos t\,dt\right)=-4\pi$",
])

A[11] = ("0", [
    r"【答案】0.",
    r"【详解】令 $L_{1}:\begin{cases}x=t\\ y=1+t\end{cases}, -1\leqslant t\leqslant0$, $L_{2}:\begin{cases}x=t\\ y=1-t\end{cases}, 0\leqslant t\leqslant1$,",
    r"$\int_{L}xy\,dx+x^{2}dy=\int_{L_{1}}xy\,dx+x^{2}dy+\int_{L_{2}}xy\,dx+x^{2}dy"
    r"=\int_{-1}^{0}t(1+t)+t^{2}\,dt+\int_{0}^{1}t(1-t)-t^{2}\,dt$",
    r"$=\left(\dfrac{2}{3}t^{3}+\dfrac{t^{2}}{2}\right)\Big|_{-1}^{0}+\left(\dfrac{t^{2}}{2}-\dfrac{2}{3}t^{3}\right)\Big|_{0}^{1}=0$",
])

A[12] = (r"\dfrac{2}{3}", [
    r"【答案】$\dfrac{2}{3}.$",
    r"【详解】$\bar{z}=\dfrac{\iiint\limits_{\Omega}z\,dxdydz}{\iiint\limits_{\Omega}dxdydz}"
    r"=\dfrac{\int_{0}^{2\pi}d\theta\int_{0}^{1}rdr\int_{r^{2}}^{1}z\,dz}{\int_{0}^{2\pi}d\theta\int_{0}^{1}rdr\int_{r^{2}}^{1}dz}"
    r"=\dfrac{\dfrac{\pi}{3}}{\dfrac{\pi}{2}}=\dfrac{2}{3}.$",
])

A[13] = (r"\alpha=6", [
    r"【答案】$\alpha=6.$",
    r"【详解】由题意知向量组 $\alpha_{1},\alpha_{2},\alpha_{3}$ 线性相关，而其中两个向量线性无关，所以",
    r"$R(\alpha_{1},\alpha_{2},\alpha_{3})=2$",
    r"$\begin{pmatrix}1&1&2\\ 2&1&1\\ -1&0&1\\ 0&2&\alpha\end{pmatrix}"
    r"\xrightarrow[\;r_{3}+r_{1}\;]{\;r_{2}-2r_{1}\;}"
    r"\begin{pmatrix}1&1&2\\ 0&-1&-3\\ 0&1&3\\ 0&2&\alpha\end{pmatrix}"
    r"\xrightarrow[\;r_{4}+2r_{2}\;]{\;r_{3}+r_{2}\;}"
    r"\begin{pmatrix}1&1&2\\ 0&-1&-3\\ 0&0&0\\ 0&0&\alpha-6\end{pmatrix}$",
    r"故 $\alpha-6=0\Rightarrow\alpha=6$",
])

A[14] = ("2", [
    r"【答案】2.",
    r"【详解】由概率密度的性质 $\sum\limits_{k=0}^{\infty}P\{X=k\}=1$，有 $\sum\limits_{k=0}^{\infty}\dfrac{C}{k!}=1\Rightarrow C=e^{-1}$，即",
    r"$P\{X=k\}=\dfrac{e^{-1}}{k!}, k=0,1,2,\cdots$ 为参数为 1 的泊松分布，则有",
    r"$EX=1, DX=1\Rightarrow EX^{2}=DX+(EX)^{2}=2.$",
])
