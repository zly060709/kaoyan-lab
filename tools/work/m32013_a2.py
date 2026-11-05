# -*- coding: utf-8 -*-
"""2013 数学三 解析 填空题 9-14（原卷 p7-p8，逐字照录）"""

A = {}

A[9] = ("-2", [
    r"【答案】$-2$",
    r"【解析】",
    r"由于 $y=f(x)$ 与 $y=x^{2}-x$ 在 $(1,0)$ 有公共切线，"
    r"所以 $f(1)=0$，$f'(1)=(x^{2}-x)'\big|_{x=1}=1$,",
    r"$\lim\limits_{n\to\infty}nf\left(\dfrac{n}{n+2}\right)"
    r"=\lim\limits_{n\to\infty}\dfrac{f\left(\dfrac{n}{n+2}\right)-f(1)}{\dfrac{n}{n+2}-1}\times\dfrac{-2n}{n+2}"
    r"=f'(1)\times(-2)\lim\limits_{n\to\infty}\dfrac{n}{n+2}=-2f'(1)=-2.$",
])

A[10] = (r"2(1-\ln 2)", [
    r"【答案】$2(1-\ln 2)$",
    r"【解析】",
    r"方程 $(z+y)^{x}=xy$ 两边同时对 $x$ 求偏导，"
    r"得 $(z+y)^{x}\Bigl[\ln(z+y)+\dfrac{x}{z+y}\cdot\dfrac{\partial z}{\partial x}\Bigr]=y$",
    r"又因 $x=1,y=2$ 时，$z=0$，所以 $\dfrac{\partial z}{\partial x}\Big|_{(1,2)}=2(1-\ln 2)$.",
])

A[11] = (r"\ln 2", [
    r"【答案】$\ln 2$",
    r"【解析】",
    r"$\displaystyle\int_{1}^{+\infty}\dfrac{\ln x}{(1+x)^{2}}dx=\lim\limits_{t\to+\infty}\int_{1}^{t}\dfrac{\ln x}{(1+x)^{2}}dx$，",
    r"又",
    r"$\displaystyle\int_{1}^{t}\dfrac{\ln x}{(1+x)^{2}}dx=-\int_{1}^{t}\ln xd\Bigl(\dfrac{1}{1+x}\Bigr)"
    r"=-\dfrac{\ln x}{1+x}\Big|_{1}^{t}+\int_{1}^{t}\dfrac{1}{1+x}\dfrac{1}{x}dx$",
    r"$=-\dfrac{\ln t}{1+t}+\int_{1}^{t}\Bigl(\dfrac{1}{x}-\dfrac{1}{1+x}\Bigr)dx"
    r"=-\dfrac{\ln t}{1+t}+\ln\Bigl|\dfrac{x}{1+x}\Bigr|\Big|_{1}^{t}"
    r"=-\dfrac{\ln t}{1+t}+\ln\Bigl|\dfrac{t}{1+t}\Bigr|+\ln 2$",
    r"所以 $\displaystyle\int_{1}^{+\infty}\dfrac{\ln x}{(1+x)^{2}}dx"
    r"=\lim\limits_{t\to+\infty}\Bigl(-\dfrac{\ln t}{1+t}+\ln\Bigl|\dfrac{t}{1+t}\Bigr|+\ln 2\Bigr)=\ln 2$",
])

A[12] = (r"(C_{1}+C_{2}x)e^{\frac{1}{2}x}", [
    r"【答案】$(C_{1}+C_{2}x)e^{\frac{1}{2}x}$",
    r"【解析】",
    r"微分方程 $y''-y'+\dfrac{y}{4}=0$ 的特征方程为 $\lambda^{2}-\lambda+\dfrac{1}{4}=0$，"
    r"所以 $\lambda=\dfrac{1}{2}$，所以微分方程的通解为 $y=(C_{1}+C_{2}x)e^{\frac{1}{2}x}$.",
])

A[13] = ("-1", [
    r"【答案】-1",
    r"【解析】由已知 $a_{ij}+A_{ij}=0$，得 $A_{ij}=-a_{ij}$，即 $A^{*}=-A^{T}$，",
    r"两边取行列式得 $\bigl|A^{*}\bigr|=\bigl|-A^{T}\bigr|\Rightarrow\bigl|A^{*}\bigr|=-|A|$，"
    r"又因为 $\bigl|A^{*}\bigr|=|A|^{n-1}=|A|^{2}$，",
    r"从而 $|A|^{2}=-|A|\Rightarrow|A|=0$ 或 $|A|=-1$，由 $A^{*}=-A^{T}\Rightarrow A^{T}A=-|A|E$，",
    r"若 $|A|=0$，则 $A^{T}A=0$，可得 $A=O$，与已知 $A$ 为三阶非零矩阵相矛盾,故 $|A|=-1$.",
])

A[14] = (r"2e^{2}", [
    r"【答案】$2e^{2}.$",
    r"【解析】",
    r"由题可得 $X\sim N(0,1)$，以及数学期望公式有 "
    r"$E\left(Xe^{2X}\right)=\displaystyle\int_{-\infty}^{+\infty}xe^{2x}\dfrac{1}{\sqrt{2\pi}}e^{-\frac{x^{2}}{2}}dx=$",
    r"$e^{2}\displaystyle\int_{-\infty}^{+\infty}x\dfrac{1}{\sqrt{2\pi}}e^{-\frac{(x-2)^{2}}{2}}dx$，"
    r"而 $\displaystyle\int_{-\infty}^{+\infty}x\dfrac{1}{\sqrt{2\pi}}e^{-\frac{(x-2)^{2}}{2}}dx$ "
    r"为服从 $N(2,1)$ 的期望，所以",
    r"$\displaystyle\int_{-\infty}^{+\infty}x\dfrac{1}{\sqrt{2\pi}}e^{-\frac{(x-2)^{2}}{2}}dx=2$，"
    r"于是 $E\left(Xe^{2X}\right)=2e^{2}$",
])
