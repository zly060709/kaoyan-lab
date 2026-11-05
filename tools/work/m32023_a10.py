# -*- coding: utf-8 -*-
"""2023 数学三 解析 第 12~13 页：题 22"""

A = {}

A[22] = (r"F(x)=\dfrac{\mathrm{e}^{x}}{1+\mathrm{e}^{x}},\ f_Y(y)=\dfrac{1}{(1+y)^{2}}\ (y\geqslant 0),\ E(Y)=+\infty", [
    r"【答案】(1) $F(x)=\dfrac{\mathrm{e}^{x}}{1+\mathrm{e}^{x}}$，$-\infty<x<+\infty$。",
    r"(2) $f_Y(y)=\begin{cases}\dfrac{1}{\left(1+y\right)^{2}},&y\geqslant0,\\ 0,&y<0.\end{cases}$",
    r"(3) 不存在。",
    r"【解析】(1) $F(x)=P\{X\leqslant x\}=\displaystyle\int_{-\infty}^{x}f(t)\mathrm{d}t=\int_{-\infty}^{x}\dfrac{\mathrm{e}^{t}}{\left(1+\mathrm{e}^{t}\right)^{2}}\mathrm{d}t=\dfrac{\mathrm{e}^{x}}{1+\mathrm{e}^{x}},-\infty<x<+\infty$。",
    r"(2) $Y=\mathrm{e}^{X}$，则有 $X=h(Y)=\ln Y$，则",
    r"$f_Y(y)=\begin{cases}f[h(y)]\cdot\left|h'(y)\right|,&y\geqslant0,\\ 0,&y<0,\end{cases}=\begin{cases}\dfrac{y}{\left(1+y\right)^{2}}\cdot\dfrac{1}{y},&y\geqslant0,\\ 0,&y<0,\end{cases}=\begin{cases}\dfrac{1}{\left(1+y\right)^{2}},&y\geqslant0,\\ 0,&y<0.\end{cases}$",
    r"(3) $E(Y)=\displaystyle\int_{-\infty}^{+\infty}y\cdot f_Y(y)\mathrm{d}y=\int_{0}^{+\infty}y\cdot\dfrac{1}{\left(1+y\right)^{2}}\mathrm{d}y=\left[\ln(1+y)+\dfrac{1}{1+y}\right]\bigg|_{0}^{+\infty}$",
    r"$=\lim\limits_{y\to+\infty}\left[\ln(1+y)+\dfrac{1}{1+y}\right]-1$，",
    r"因为此极限不存在，故反常积分发散，$Y$ 的期望不存在。",
])
