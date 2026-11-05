# -*- coding: utf-8 -*-
"""2023 数学三 解析 第 7~8 页：题 11-14"""

A = {}

A[11] = (r"\dfrac{2}{3}", [
    r"【答案】$\dfrac{2}{3}$",
    r"【解析】利用倒代换，令 $x=\dfrac{1}{t}$，可得，",
    r"$I=\lim\limits_{x\to\infty}x^{2}\left(2-x\sin\dfrac{1}{x}-\cos\dfrac{1}{x}\right)=\lim\limits_{t\to0}\dfrac{1}{t^{2}}\left(2-\dfrac{1}{t}\sin t-\cos t\right)=\lim\limits_{t\to0}\dfrac{2t-\sin t-t\cos t}{t^{3}}$，",
    r"由洛必达法则可知，$I=\lim\limits_{t\to0}\dfrac{2-2\cos t+t\sin t}{3t^{2}}=\lim\limits_{t\to0}\dfrac{2-2\cos t}{3t^{2}}+\dfrac{t\sin t}{3t^{2}}=\dfrac{2}{3}$。",
])

A[12] = (r"\dfrac{\pi}{3}", [
    r"【答案】$\dfrac{\pi}{3}$。",
    r"【解析】由题干可知 $\dfrac{\partial f(x,y)}{\partial x}=\dfrac{-y}{x^{2}+y^{2}}$，$\dfrac{\partial f(x,y)}{\partial y}=\dfrac{x}{x^{2}+y^{2}}$，",
    r"$\therefore f(x,y)=\displaystyle\int\dfrac{-y}{x^{2}+y^{2}}\mathrm{d}x+c_1(y)=-\arctan\dfrac{x}{y}+c_1(y)$，",
    r"将上式对 $y$ 求偏导，得 $\dfrac{\partial f(x,y)}{\partial y}=\dfrac{x}{x^{2}+y^{2}}+c_1'(y)$",
    r"由 $\dfrac{\partial f(x,y)}{\partial y}=\dfrac{x}{x^{2}+y^{2}}+c_1^{'}(y)=\dfrac{x}{x^{2}+y^{2}}$ 知 $c_1^{'}(y)=0$，$c_1(y)=C$",
    r"故 $f(x,y)=-\arctan\dfrac{x}{y}+C$，带入初始条件 $C=\dfrac{\pi}{2}$，故 $f(\sqrt{3},3)=\dfrac{\pi}{3}$",
])

A[13] = (r"\dfrac{1}{2}(\mathrm{e}^{x}+\mathrm{e}^{-x})", [
    r"【答案】$\dfrac{1}{2}(\mathrm{e}^{x}+\mathrm{e}^{-x})$",
    r"【解析】$s(x)=\sum\limits_{n=0}^{\infty}\dfrac{x^{2n}}{(2n)!}=1+\dfrac{1}{2!}x^{2}+\dfrac{1}{4!}x^{4}+\cdots+\dfrac{1}{(2n)!}x^{2n}+\cdots$",
    r"两边同时求导得，$s'(x)=\sum\limits_{n=1}^{\infty}\dfrac{x^{2n-1}}{(2n-1)!}=x+\dfrac{1}{3!}x^{3}+\dfrac{1}{5!}x^{5}+\cdots+\dfrac{1}{(2n-1)!}x^{2n-1}+\cdots$",
    r"因此可得微分方程，$s(x)+s'(x)=\mathrm{e}^{x}$，",
    r"解微分方程可得，$s(x)=\mathrm{e}^{-\int 1\mathrm{d}x}\left(\int\mathrm{e}^{x}\mathrm{e}^{\int 1\mathrm{d}x}\mathrm{d}x+C\right)=C\mathrm{e}^{-x}+\dfrac{1}{2}\mathrm{e}^{x}$，",
    r"又因为 $s(0)=1$，解得 $C=\dfrac{1}{2}$。因此，$s(x)=\dfrac{1}{2}(\mathrm{e}^{x}+\mathrm{e}^{-x})$",
])

A[14] = (r"2(\mathrm{e}^{t}-t-1)", [
    r"【答案】$2(\mathrm{e}^{t}-t-1)$。",
    r"【解析】依题意 $\displaystyle\int_{0}^{t}f(x)\mathrm{d}x=t\left[\dfrac{f(t)}{t}-t\right]=f(t)-t^{2}$",
    r"两边同对 $t$ 求导，得 $f'(t)-f(t)=2t$，",
    r"解此微分方程，得 $f(t)=\mathrm{e}^{t}\left(\displaystyle\int 2t\,\mathrm{e}^{-t}\mathrm{d}t+C\right)=C\mathrm{e}^{t}-2t-2$，",
    r"代入 $f(0)=0$，得 $f(t)=2(\mathrm{e}^{t}-t-1)$。",
])
