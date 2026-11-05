# -*- coding: utf-8 -*-
"""2023 数学三 解析 第 9~10 页：题 17-18"""

A = {}

A[17] = (r"a=1,b=-1；x=0 是极值点", [
    r"【答案】(1) $a=1,b=-1$。(2) 是",
    r"【解析】(1) 对 $a\mathrm{e}^{x}+y^{2}+y-\ln(1+x)\cos y+b=0$ 带入 $y(0)=0,x=0$ 可得：$a+b=0$",
    r"两端求导可得：$a\mathrm{e}^{x}+2yy'+y'-\dfrac{1}{1+x}\cos y+\ln(x+1)\cdot\sin y\cdot y'=0$；",
    r"带入 $x=0,y=0,y'(0)=0$ 可得：$a-1=0$，解得：$a=1,b=-1$。",
    r"(2) 对 $\mathrm{e}^{x}+2yy'+y'-\dfrac{1}{1+x}\cos y+\ln(x+1)\cdot\sin y\cdot y'=0$，再次求导可得：",
    r"$\mathrm{e}^{x}+2\left(y'\right)^{2}+2yy''+y''+\dfrac{1}{\left(1+x\right)^{2}}\cos y+\dfrac{1}{(1+x)}\sin y\cdot y'+\dfrac{1}{(1+x)}\sin y\cdot y'+\left(y'\cdot y'\cos y+\sin y\cdot y''\right)\cdot\ln(x+1)=0$",
    r"带入 $x=0,y=0,y'(0)=0$ 可得 $y''(0)=-2<0$，所以 $y(0)=0$ 为极大值点，是极值。",
])

A[18] = (r"(1)\ \ln(1+\sqrt{2}),\ (2)\ \pi\left(1-\dfrac{\pi}{4}\right)", [
    r"【答案】(1) $\ln(1+\sqrt{2})$，(2) $\pi\left(1-\dfrac{\pi}{4}\right)$。",
    r"【解析】(1) 由题意得：$S=\displaystyle\int_{1}^{+\infty}\dfrac{1}{x\sqrt{1+x^{2}}}\mathrm{d}x=\int_{\frac{\pi}{4}}^{\frac{\pi}{2}}\dfrac{1}{\sin t}\mathrm{d}t=\ln\dfrac{1-\cos t}{\sin t}\bigg|_{\frac{\pi}{4}}^{\frac{\pi}{2}}=\ln(1+\sqrt{2})$",
    r"(2) 由题意得：$V=\displaystyle\int_{1}^{+\infty}\pi\dfrac{1}{x^{2}\left(1+x^{2}\right)}\mathrm{d}x=\int_{1}^{+\infty}\pi\dfrac{1+x^{2}-x^{2}}{x^{2}\left(1+x^{2}\right)}\mathrm{d}x=\int_{1}^{+\infty}\pi\dfrac{1}{x^{2}}\mathrm{d}x-\int_{1}^{+\infty}\pi\dfrac{1}{\left(1+x^{2}\right)}\mathrm{d}x$",
    r"$=\pi-\dfrac{\pi^{2}}{4}=\pi\left(1-\dfrac{\pi}{4}\right)$。",
])
