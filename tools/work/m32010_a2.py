# -*- coding: utf-8 -*-
"""2010 数学三 解析 填空题 9-14（原卷 p6-p7，逐字照录）"""

A = {}

A[9] = ("-1", [
    r"【答案】$-1$",
    r"【详解】两边同时对 $x$ 求导得，",
    r"$e^{-(x+y)^{2}}(1+y')=\int_{0}^{x}\sin t^{2}dt+x\sin x^{2}$",
    r"将 $x=0$ 代入上式，得 $e^{-y^{2}}(1+y')=0,\therefore y'=-1$",
])

A[10] = (r"\dfrac{\pi^{2}}{4}", [
    r"【答案】$\dfrac{\pi^{2}}{4}$",
    r"【详解】$V=\int_{e}^{+\infty}\pi\left(\dfrac{1}{\sqrt{x(1+\ln^{2}x)}}\right)^{2}dx$",
    r"令 $x=e^{t}$，则 $V=\int_{1}^{+\infty}\pi\dfrac{1}{e^{t}(1+t^{2})}\cdot e^{t}dt=\pi\arctan t\Big|_{1}^{+\infty}=\dfrac{\pi^{2}}{4}$",
])

A[11] = (r"pe^{\frac{p^{3}-1}{3}}", [
    r"【答案】$pe^{\frac{p^{3}-1}{3}}$",
    r"【详解】",
    r"由弹性函数得 $\dfrac{dR}{dp}\dfrac{p}{R}=1+p^{3}$，分离变量得 $\dfrac{dR}{R}=\left(\dfrac{1}{p}+p^{2}\right)dp$，"
    r"于是 $\ln R=\ln p+\dfrac{1}{3}p^{3}+C$，",
    r"带入初始条件 $R(1)=1$，得 $C=-\dfrac{1}{3}$，从而得 $R=pe^{\frac{p^{3}-1}{3}}$.",
])

A[12] = ("3", [
    r"【答案】$3$",
    r"【详解】由题设条件有 $0=(-1)^{3}+a(-1)^{2}+b(-1)+1$，且 $y''\big|_{x=-1}=(6x+2a)\big|_{x=-1}=0$",
    r"解得 $a=3$，$b=3$.",
])

A[13] = ("3", [
    r"【答案】$3$",
    r"【详解】$\left|A+B^{-1}\right|=\left|B^{-1}(BA+E)\right|=\left|B^{-1}(BA+A^{-1}A)\right|$",
    r"$=\left|B^{-1}(B+A^{-1})A\right|=\left|B^{-1}\right|\left|\left(B+A^{-1}\right)\right|\left|A\right|"
    r"=\dfrac{1}{|B|}\left|\left(B+A^{-1}\right)\right|\left|A\right|$",
    r"$=\dfrac{1}{2}\times2\times3=3$",
])

A[14] = (r"\mu^{2}+\sigma^{2}", [
    r"【答案】$\mu^{2}+\sigma^{2}$",
    r"【详解】由题知 $EX=\mu, DX=\sigma^{2}\Rightarrow EX^{2}=\mu^{2}+\sigma^{2}$, 则有",
    r"$ET=E(\dfrac{1}{n}\sum\limits_{i=1}^{n}X_{i}^{2})=\dfrac{1}{n}\sum\limits_{i=1}^{n}EX_{i}^{2}=EX^{2}=\mu^{2}+\sigma^{2}$.",
])
