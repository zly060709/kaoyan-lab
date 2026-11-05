# -*- coding: utf-8 -*-
"""2023 数学二 答案解析（视觉转录自 data/math2/pages/2023/p5-p6.png）。本文件：第 (3)(4)(5) 题。"""

A = {}

A[3] = ("B", [
    r"在 $x\in\left(0,\dfrac{\pi}{2}\right)$ 时，$\dfrac{2}{\pi}x<\sin x$，即 $x_{n+1}=\sin x_{n}>\dfrac{2}{\pi}x_{n}$，$y_{n+1}=\dfrac{1}{2}y_{n}$",
    r"因此 $\dfrac{y_{n+1}}{x_{n+1}}<\dfrac{\frac{1}{2}y_{n}}{\frac{2}{\pi}x_{n}}=\dfrac{\pi}{4}\dfrac{y_{n}}{x_{n}}<\left(\dfrac{\pi}{4}\right)^{2}\dfrac{y_{n-1}}{x_{n-1}}<\cdots<\left(\dfrac{\pi}{4}\right)^{n}\dfrac{y_{1}}{x_{1}}$，故 $\lim\limits_{n\to\infty}\dfrac{y_{n}}{x_{n}}=0$。",
    r"即 $n\to\infty$ 时，$y_{n}$ 是 $x_{n}$ 的高阶无穷小，选（B）。",
])

A[4] = ("C", [
    r"若要在实数域内有界，必须要求解中不含指数形式，当 $a=0,b>0$ 的时候，特征根为 $\lambda=\pm\sqrt{b}i$，此时通解为 $y=C_{1}\cos\sqrt{b}x+C_{2}\sin\sqrt{b}x$，故有界，选 C。",
])

A[5] = ("C", [
    r"由于 $f'(0)=\lim\limits_{x\to 0}\dfrac{f(x)-f(0)}{x-0}=\lim\limits_{t\to 0}\dfrac{|t|\sin t-0}{2t+|t|-0}=\lim\limits_{t\to 0}\dfrac{|t|\sin t}{2t+|t|}=0$。故排除 A 选项。",
    r"当 $t>0$ 时，$\dfrac{\mathrm{d}y}{\mathrm{d}x}=\dfrac{\mathrm{d}y/\mathrm{d}t}{\mathrm{d}x/\mathrm{d}t}=\dfrac{\sin t+t\cos t}{3}$。",
    r"当 $t<0$ 时，$\dfrac{\mathrm{d}y}{\mathrm{d}x}=\dfrac{\mathrm{d}y/\mathrm{d}t}{\mathrm{d}x/\mathrm{d}t}=-\dfrac{(\sin t+t\cos t)}{1}=-(\sin t+t\cos t)$。",
    r"可见，$\lim\limits_{x\to 0^{+}}f'(x)=\lim\limits_{t\to 0^{+}}\dfrac{\sin t+t\cos t}{3}=0=f'(0)$，$\lim\limits_{x\to 0^{-}}f'(x)=\lim\limits_{t\to 0^{-}}-(\sin t+t\cos t)=0=f'(0)$。即 $f'(x)$ 在 $x=0$ 处连续，排除选项 B。",
    r"$f_{+}''(0)=\lim\limits_{x\to 0^{+}}\dfrac{f'(x)-f'(0)}{x-0}=\lim\limits_{t\to 0^{+}}\dfrac{\frac{\sin t+t\cos t}{3}}{3t}=\lim\limits_{t\to 0^{+}}\dfrac{\sin t+t\cos t}{9t}=\dfrac{2}{9}$",
    r"$f_{-}''(0)=\lim\limits_{x\to 0^{-}}\dfrac{f'(x)-f'(0)}{x-0}=\lim\limits_{t\to 0^{-}}\dfrac{-(\sin t+t\cos t)-0}{t}=-2$。",
    r"由于 $f_{+}''(0)\neq f_{-}''(0)$，所以 $f''(0)$ 不存在，即选项 C 正确。",
])
