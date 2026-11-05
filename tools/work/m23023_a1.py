# -*- coding: utf-8 -*-
"""2023 数学二 答案解析（视觉转录自 data/math2/pages/2023/p5-p13.png，原卷照录）。
键为题号；value = (answer, [解析行])。本文件：第 (1)(2) 题。"""

A = {}

A[1] = ("B", [
    r"斜渐近线方程为 $y=ax+b$。",
    r"$a=\lim\limits_{x\to\infty}\dfrac{y}{x}=\lim\limits_{x\to\infty}\ln(\mathrm{e}+\dfrac{1}{x-1})=1$",
    r"$b=\lim\limits_{x\to\infty}(y-x)=\lim\limits_{x\to\infty}\left[x\ln(\mathrm{e}+\dfrac{1}{x-1})-x\right]=\lim\limits_{x\to\infty}x\ln(1+\dfrac{1}{\mathrm{e}x-\mathrm{e}})=\lim\limits_{x\to\infty}\dfrac{x}{\mathrm{e}x-\mathrm{e}}=\dfrac{1}{\mathrm{e}}$",
    r"斜渐近线方程为 $y=x+\dfrac{1}{\mathrm{e}}$，故选（B）。",
])

A[2] = ("D", [
    r"当 $x\leqslant 0$ 时，$F(x)=\displaystyle\int f(x)\mathrm{d}x=\int\dfrac{1}{\sqrt{1+x^{2}}}\mathrm{d}x=\ln(\sqrt{1+x^{2}}+x)+C_{1}$，",
    r"当 $x>0$ 时，$F(x)=\displaystyle\int f(x)\mathrm{d}x=\int(x+1)\cos x\mathrm{d}x=(x+1)\sin x+\cos x+C_{2}$，",
    r"因为 $F(x)$ 在 $x=0$ 处连续，故 $F(0)=\lim\limits_{x\to 0^{-}}F(x)=\lim\limits_{x\to 0^{+}}F(x)$，即 $F(0)=C_{1}=C_{2}+1$。",
    r"任取 $C_{2}=0$，则 $F(0)=1,C_{1}=1$，得 $f(x)$ 的一个原函数 $F(x)=\begin{cases}\ln(\sqrt{1+x^{2}}+x)+1, & x\leqslant 0,\\ (x+1)\sin x+\cos x, & x>0,\end{cases}$，故应选（D）。",
])
