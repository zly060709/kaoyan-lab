# -*- coding: utf-8 -*-
"""2023 数学三 解析 第 5 页：题 1-3"""

A = {}

A[1] = ("A", [
    r"【答案】（A）",
    r"【解析】由偏导数定义可知，$\dfrac{\partial f}{\partial x}\bigg|_{(0,1)}=\lim\limits_{x\to0}\dfrac{f(x,1)-f(0,1)}{x}=\lim\limits_{x\to0}\dfrac{\ln(1+|x\sin1|)}{x}=\lim\limits_{x\to0}\dfrac{|x\sin1|}{x}=\sin1\cdot\lim\limits_{x\to0}\dfrac{|x|}{x}$，",
    r"因为 $\lim\limits_{x\to0^{+}}\dfrac{|x|}{x}=\lim\limits_{x\to0^{+}}\dfrac{x}{x}=1,\ \lim\limits_{x\to0^{-}}\dfrac{|x|}{x}=\lim\limits_{x\to0^{-}}\dfrac{-x}{x}=-1$，故 $\dfrac{\partial f}{\partial x}\bigg|_{(0,1)}$ 不存在。",
    r"同理，$\dfrac{\partial f}{\partial y}\bigg|_{(0,1)}=\lim\limits_{y\to1}\dfrac{f(0,y)-f(0,1)}{y-1}=\lim\limits_{y\to1}\dfrac{\ln y}{y-1}=\lim\limits_{y\to1}\dfrac{y-1}{y-1}=1$，因此 $\dfrac{\partial f}{\partial y}\bigg|_{(0,1)}$ 存在。故选（A）。",
])

A[2] = ("D", [
    r"【答案】（D）",
    r"【解析】当 $x\leqslant0$ 时，$F(x)=\displaystyle\int f(x)\mathrm{d}x=\int\dfrac{1}{\sqrt{1+x^{2}}}\mathrm{d}x=\ln(\sqrt{1+x^{2}}+x)+C_1$，",
    r"当 $x>0$ 时，$F(x)=\displaystyle\int f(x)\mathrm{d}x=\int(x+1)\cos x\mathrm{d}x=(x+1)\sin x+\cos x+C_2$，",
    r"因为 $F(x)$ 在 $x=0$ 处连续，故 $F(0)=\lim\limits_{x\to0^{-}}F(x)=\lim\limits_{x\to0^{+}}F(x)$，即 $F(0)=C_1=C_2+1$。",
    r"取 $C_2=0$，则 $F(0)=1,C_1=1$，得 $f(x)$ 的一个原函数 $F(x)=\begin{cases}\ln(\sqrt{1+x^{2}}+x)+1,&x\leqslant0,\\ (x+1)\sin x+\cos x,&x>0.\end{cases}$ 故应选（D）。",
])

A[3] = ("C", [
    r"【答案】（C）",
    r"【解析】特征方程为 $r^{2}+ar+b=0$，得 $r_{1,2}=\dfrac{-a\pm\sqrt{a^{2}-4b}}{2}$；",
    r"若 $a^{2}-4b=0$，则 $y(x)=(C_1+C_2x)\mathrm{e}^{-\frac{a}{2}x}$，此时解在 $(-\infty,+\infty)$ 无界；",
    r"若 $a^{2}-4b>0$，则 $y(x)=C_1\mathrm{e}^{r_1x}+C_2\mathrm{e}^{r_2x}$，此时解在 $(-\infty,+\infty)$ 无界；",
    r"若 $a^{2}-4b<0$，此时 $r_{1,2}=\alpha\pm\beta i$，则 $y(x)=\mathrm{e}^{\alpha x}(C_1\cos\beta x+C_2\sin\beta x)$，当 $a=0,b>0$ 时 $y(x)=(C_1\cos\beta x+C_2\sin\beta x)$，解在 $(-\infty,+\infty)$ 有界，故选（C）。",
])
