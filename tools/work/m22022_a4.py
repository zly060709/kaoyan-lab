# -*- coding: utf-8 -*-
"""2022 数学二 答案解析 解答题（p9 起）。"""

A = {}

A[17] = ("$f'(1)=-1$", [
    r"【解析】$f(x)$ 在 $x=1$ 处可导，则 $f(x)$ 在 $x=1$ 处连续，",
    r"$\lim\limits_{x\to 0}\left[f\left(\mathrm{e}^{x^{2}}\right)-3f\left(1+\sin^{2}x\right)\right]=-2f(1)$",
    r"又因为 $\lim\limits_{x\to 0}\dfrac{f\left(\mathrm{e}^{x^{2}}\right)-3f\left(1+\sin^{2}x\right)}{x^{2}}\cdot x^{2}=\lim\limits_{x\to 0}\dfrac{f\left(\mathrm{e}^{x^{2}}\right)-3f\left(1+\sin^{2}x\right)}{x^{2}}\cdot\lim\limits_{x\to 0}x^{2}=0$，所以 $f(1)=0$。",
    r"原式 $=\lim\limits_{x\to 0}\dfrac{f\left(\mathrm{e}^{x^{2}}\right)-f(1)}{x^{2}}-3\lim\limits_{x\to 0}\dfrac{f\left(1+\sin^{2}x\right)-f(1)}{x^{2}}=-2f'(1)=2$",
    r"所以 $f'(1)=-1$。",
])

A[18] = ("$L=\\dfrac{1}{4}\\mathrm{e}^{2}+\\dfrac{1}{4}$", [
    r"【解析】由 $y'-\dfrac{2}{x}y=\dfrac{\ln x}{x}-\dfrac{1}{2x}$，",
    r"$y(x)=\mathrm{e}^{\int\frac{2}{x}\mathrm{d}x}\left[\int\left(\dfrac{\ln x}{x}-\dfrac{1}{2x}\right)\mathrm{e}^{-\int\frac{2}{x}\mathrm{d}x}\mathrm{d}x+C\right]=-\dfrac{1}{2}\ln x+Cx^{2}$",
    r"又因为 $y(1)=\dfrac{1}{4}$，$\therefore C=\dfrac{1}{4}$；即 $y(x)=-\dfrac{1}{2}\ln x+\dfrac{1}{4}x^{2}$，",
    r"所以 $y'(x)=-\dfrac{1}{2x}+\dfrac{1}{2}x$ 从而弧长 $L=\displaystyle\int_{1}^{\mathrm{e}}\left(\dfrac{1}{2}x+\dfrac{1}{2x}\right)\mathrm{d}x=\left.\left(\dfrac{1}{4}x^{2}+\dfrac{1}{2}\ln|x|\right)\right|_{1}^{\mathrm{e}}=\dfrac{1}{4}\mathrm{e}^{2}+\dfrac{1}{4}$。",
])

A[19] = ("$2\\pi-2$", [
    r"【解析】令 $D_{1}=\left\{(r,\theta)\middle|0\leq r\leq 2,0\leq\theta\leq\dfrac{\pi}{2}\right\}$，",
    r"$D_{2}=\left\{(r,\theta)\middle|0\leq r\leq\dfrac{2}{\sin\theta-\cos\theta},\dfrac{\pi}{2}\leq\theta\leq\pi\right\}$，",
    r"$I=\displaystyle\iint_{D_{1}}\dfrac{(x-y)^{2}}{x^{2}+y^{2}}dxdy+\iint_{D_{2}}\dfrac{(x-y)^{2}}{x^{2}+y^{2}}dxdy$",
    r"$=\displaystyle\int_{0}^{\frac{\pi}{2}}d\theta\int_{0}^{2}\left(\cos\theta-\sin\theta\right)^{2}rdr+\int_{\frac{\pi}{2}}^{\pi}d\theta\int_{0}^{\frac{2}{\sin\theta-\cos\theta}}\left(\cos\theta-\sin\theta\right)^{2}rdr$",
    r"$=2\displaystyle\int_{0}^{\frac{\pi}{2}}\left(1-2\sin\theta\cos\theta\right)d\theta+\int_{\frac{\pi}{2}}^{\pi}2d\theta=2\pi-2$",
])

A[20] = ("(Ⅰ) $\\dfrac{\\partial g}{\\partial x}=2(2x-y)\\mathrm{e}^{-y}$；(Ⅱ) $f(u,v)=(u^{2}+v^{2})\\mathrm{e}^{-(u+v)}$，极小值 $f(0,0)=0$，$(1,1)$ 处不是极值", [
    r"【解析】(I) $\dfrac{\partial g(x,y)}{\partial x}=\dfrac{\partial f(x,y-x)}{\partial x}$，令 $u=x,v=y-x$，",
    r"$\dfrac{\partial f(x,y-x)}{\partial x}=\dfrac{\partial f(u,v)}{\partial u}\cdot\dfrac{\partial u}{\partial x}+\dfrac{\partial f(u,v)}{\partial v}\cdot\dfrac{\partial v}{\partial x}=\dfrac{\partial f(u,v)}{\partial u}-\dfrac{\partial f(u,v)}{\partial v}=2(u-v)\cdot\mathrm{e}^{-(u+v)}=2(2x-y)\cdot\mathrm{e}^{-y}$",
    r"(II) $g(x,y)=2(x^{2}-xy)\mathrm{e}^{-y}+C(y)$，又 $f(x,0)=g(x,x)=C(x)=x^{2}\mathrm{e}^{-x}$，",
])
