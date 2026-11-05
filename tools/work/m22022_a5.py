# -*- coding: utf-8 -*-
"""2022 数学二 答案解析（p10）。A[20] 为续写行。"""

A20_CONT = [
    r"所以 $C(x)=x^{2}\mathrm{e}^{-x},g(x,y)=2(x^{2}-xy)\mathrm{e}^{-y}+y^{2}\mathrm{e}^{-y}=[2x^{2}-2xy+y^{2}]\mathrm{e}^{-y}$，",
    r"令 $\begin{cases}x=u\\ y-x=v\end{cases}\Rightarrow\begin{cases}x=u\\ y=u+v\end{cases}$ 得",
    r"$f(u,v)=-2uv\mathrm{e}^{-(u+v)}+(u+v)^{2}\mathrm{e}^{-(u+v)}=(u^{2}+v^{2})\mathrm{e}^{-(u+v)}$",
    r"令 $\begin{cases}f'_{u}=[2u-(u^{2}+v^{2})]\mathrm{e}^{-(u+v)}=0\\ f'_{v}=[2v-(u^{2}+v^{2})]\mathrm{e}^{-(u+v)}=0\end{cases}$ 得 $\begin{cases}u=0\\ v=0\end{cases}$ 或 $\begin{cases}u=1\\ v=1\end{cases}$",
    r"$A=\dfrac{\partial^{2}f}{\partial u^{2}}\big|_{(0,0)}=2,B=\dfrac{\partial^{2}f}{\partial u\partial v}\big|_{(0,0)}=0,C=\dfrac{\partial^{2}f}{\partial v^{2}}\big|_{(0,0)}=2,\ AC-B^{2}>0,A>0$，得 $f(u,v)\big|_{(0,0)}=0$ 为极小值；",
    r"$A=\dfrac{\partial^{2}f}{\partial u^{2}}\big|_{(1,1)}=0,B=\dfrac{\partial^{2}f}{\partial u\partial v}\big|_{(1,1)}=-2\mathrm{e}^{-2},C=\dfrac{\partial^{2}f}{\partial v^{2}}\big|_{(1,1)}=0,\ AC-B^{2}<0$，得在 $(1,1)$ 处不是极值。",
]

A = {}

A[21] = (None, [
    r"【解析】$f(x)=f\big(\dfrac{a+b}{2}\big)+f'\big(\dfrac{a+b}{2}\big)\big(x-\dfrac{a+b}{2}\big)+\dfrac{1}{2}f''(\xi)\big(x-\dfrac{a+b}{2}\big)^{2}$，$\xi$ 介于 $x$ 与 $\dfrac{a+b}{2}$ 之间。",
    r"$\displaystyle\int_{a}^{b}f(x)\mathrm{d}x=\int_{a}^{b}\left[f\big(\dfrac{a+b}{2}\big)+f'\big(\dfrac{a+b}{2}\big)\big(x-\dfrac{a+b}{2}\big)+\dfrac{1}{2}f''(\xi)\big(x-\dfrac{a+b}{2}\big)^{2}\right]\mathrm{d}x$",
    r"$=f\big(\dfrac{a+b}{2}\big)(b-a)+\displaystyle\int_{a}^{b}\left[\dfrac{1}{2}f''(\xi)\big(x-\dfrac{a+b}{2}\big)^{2}\right]\mathrm{d}x$",
    r"必要性：若 $f''(x)\geq 0$，则 $f''(\xi)\geq 0$，有 $\dfrac{\displaystyle\int_{a}^{b}f(x)\mathrm{d}x}{(b-a)}\geq f\big(\dfrac{a+b}{2}\big)$。",
    r"充分性：若存在 $x_{0}$ 使得 $f''(x_{0})<0$，因为 $f(x)$ 有二阶连续导数，故存在 $\delta>0$ 使得 $f''(x)$ 在 $\big[x_{0}-\delta,x_{0}+\delta\big]$ 内恒小于零，记 $a=x_{0}-\delta,b=x_{0}+\delta$，",
    r"此时 $\displaystyle\int_{a}^{b}f(x)\mathrm{d}x=f\big(\dfrac{a+b}{2}\big)(b-a)+\int_{a}^{b}\left[\dfrac{1}{2}f''(\xi)\big(x-\dfrac{a+b}{2}\big)^{2}\right]\mathrm{d}x<f\big(\dfrac{a+b}{2}\big)(b-a)$，矛盾！",
    r"故 $f''(x)\geq 0$。综上，充分性必要性均得证。",
])

A[22] = (None, [
    r"【解析】(I) $f\left(x_{1},x_{2},x_{3}\right)=3x_{1}^{2}+4x_{2}^{2}+3x_{3}^{2}+2x_{1}x_{3}$，",
])
