# -*- coding: utf-8 -*-
"""2011 数学三 解析 选择题 1-8（原卷 p5-p7，逐字照录）"""

A = {}

A[1] = ("C", [
    r"【答案】（C）",
    r"【解析】法一：利用泰勒公式",
    r"$x\to0$ 时，$\sin x=x-\dfrac{x^{3}}{3!}+o(x^{3})$，$\sin 3x=3x-\dfrac{27x^{3}}{3!}+o(x^{3})$",
    r"$\lim\limits_{x\to0}\dfrac{3\sin x-\sin 3x}{cx^{k}}=\lim\limits_{x\to0}\dfrac{-\dfrac{x^{3}}{2}+\dfrac{9x^{3}}{2}+o(x^{3})}{cx^{k}}=\lim\limits_{x\to0}\dfrac{4x^{3}}{cx^{k}}=1$",
    r"所以 $k=3,c=4$.",
    r"法二：利用洛必达法则和和差化积公式",
    r"$\lim\limits_{x\to0}\dfrac{3\sin x-\sin 3x}{cx^{k}}=\lim\limits_{x\to0}\dfrac{3\cos x-3\cos 3x}{ckx^{k-1}}"
    r"=\lim\limits_{x\to0}\dfrac{3}{ck}\dfrac{-2\sin 2x\sin(-x)}{x^{k-1}}=\dfrac{12}{ck}\lim\limits_{x\to0}\dfrac{x^{2}}{x^{k-1}}=1$",
    r"所以 $k-1=2,ck=12$，即 $k=3,c=4$.",
])

A[2] = ("B", [
    r"【答案】（B）",
    r"【解析】方法一：因为 $f(x)$ 在 $x=0$ 处可导，故",
    r"$I=\lim\limits_{x\to0}\dfrac{x^{2}f(x)-2f(x^{3})}{x^{3}}"
    r"=\lim\limits_{x\to0}\dfrac{x^{2}f(x)-x^{2}f(0)}{x^{3}}-\lim\limits_{x\to0}\dfrac{2f(x^{3})-2f(0)}{x^{3}}"
    r"=f'(0)-2f'(0)=-f'(0)$",
    r"方法二：用泰勒展开式",
    r"$f(x)=f(0)+f'(0)x+o(x)=f'(0)x+o(x)$，",
    r"$f(x^{3})=f(0)+f'(0)x^{3}+o(x^{3})=f'(0)x^{3}+o(x^{3})$",
    r"$I=\lim\limits_{x\to0}\dfrac{x^{2}f(x)-2f(x^{3})}{x^{3}}"
    r"=\dfrac{x^{2}\left(f'(0)x+o(x)\right)-2\left(f'(0)x^{3}+o(x^{3})\right)}{x^{3}}"
    r"=\lim\limits_{x\to0}\dfrac{-f'(0)x^{3}+o(x^{3})}{x^{3}}=-f'(0)$",
])

A[3] = ("A", [
    r"【答案】（A）",
    r"【解析】$\sum\limits_{n=1}^{\infty}u_{n}$ 收敛，则对它的任意项加括号后所成的级数仍收敛，"
    r"故选项（A）正确，所以选（A）.",
])

A[4] = ("B", [
    r"【答案】（B）",
    r"【解析】在区间 $\left(0,\dfrac{\pi}{4}\right)$ 上，$\sin x<\cos x<\cot x$，且 $\ln x$ 是增函数，所以",
    r"$\ln(\sin x)<\ln(\cos x)<\ln(\cot x)$",
    r"由定积分比较大小的性质可知，应选（B）.",
])

A[5] = ("D", [
    r"【答案】（D）.",
    r"【解析】由初等变换及初等矩阵的性质易知 $\boldsymbol{P}_{2}\boldsymbol{A}\boldsymbol{P}_{1}=\boldsymbol{E}$，"
    r"从而 $\boldsymbol{A}=\boldsymbol{P}_{2}^{-1}\boldsymbol{P}_{1}^{-1}=\boldsymbol{P}_{2}\boldsymbol{P}_{1}^{-1}$，选（D）.",
])

A[6] = ("C", [
    r"【答案】（C）.",
    r"【解析】由 $\boldsymbol{\eta}_{1},\boldsymbol{\eta}_{2},\boldsymbol{\eta}_{3}$ 是非齐次线性方程组 "
    r"$\boldsymbol{Ax}=\boldsymbol{\beta}$ 的三个线性无关的解，知 $\boldsymbol{\eta}_{3}-\boldsymbol{\eta}_{1},"
    r"\boldsymbol{\eta}_{2}-\boldsymbol{\eta}_{1}$ 为 $\boldsymbol{Ax}=\boldsymbol{0}$ 的两个线性无关的解. "
    r"又由题设知矩阵 $\boldsymbol{A}$ 的秩为 1，所以 $\boldsymbol{Ax}=\boldsymbol{0}$ 的基础解系包含"
    r"$n-r(\boldsymbol{A})=2$ 个向量，从而 $\boldsymbol{\eta}_{3}-\boldsymbol{\eta}_{1},"
    r"\boldsymbol{\eta}_{2}-\boldsymbol{\eta}_{1}$ 为 $\boldsymbol{Ax}=\boldsymbol{0}$ 的一个基础解系. "
    r"另一方面，$\dfrac{\boldsymbol{\eta}_{2}+\boldsymbol{\eta}_{3}}{2}$ 为 $\boldsymbol{Ax}=\boldsymbol{\beta}$ 的解. "
    r"故由非齐次线性方程组解的结构，知 $\dfrac{\boldsymbol{\eta}_{2}+\boldsymbol{\eta}_{3}}{2}"
    r"+k_{1}(\boldsymbol{\eta}_{3}-\boldsymbol{\eta}_{1})+k_{2}(\boldsymbol{\eta}_{2}-\boldsymbol{\eta}_{1})$ 为"
    r"$\boldsymbol{Ax}=\boldsymbol{\beta}$ 的通解，故应选（C）.",
])

A[7] = ("D", [
    r"【答案】（D）.",
    r"【解析】由概率密度的性质知，概率密度必须满足 $\int_{-\infty}^{+\infty}f(x)dx=1$，故由题知",
    r"$\int_{-\infty}^{+\infty}\left[f_{1}(x)F_{2}(x)+f_{2}(x)F_{1}(x)\right]dx"
    r"=\int_{-\infty}^{+\infty}dF_{1}(x)F_{2}(x)=F_{1}(x)F_{2}(x)\Big|_{-\infty}^{+\infty}=1$，",
    r"故选择（D）",
])

A[8] = ("D", [
    r"【答案】（D）.",
    r"【解析】由题知 $EX_{i}=\lambda,DX_{i}=\lambda(i=1,2,\cdots,n)$，故有",
    r"$ET_{1}=\dfrac{1}{n}\sum\limits_{i=1}^{n}EX_{i}=\lambda$，",
    r"$ET_{2}=\dfrac{1}{n-1}\sum\limits_{i=1}^{n-1}EX_{i}+\dfrac{1}{n}EX_{n}=\lambda+\dfrac{1}{n}\lambda$",
    r"$DT_{1}=\dfrac{1}{n^{2}}\sum\limits_{i=1}^{n}DX_{i}=\dfrac{1}{n}\lambda$",
    r"$DT_{2}=\dfrac{1}{(n-1)^{2}}\sum\limits_{i=1}^{n-1}DX_{i}+\dfrac{1}{n^{2}}DX_{n}"
    r"=\dfrac{1}{n-1}\lambda+\dfrac{1}{n^{2}}\lambda$",
    r"由于 $\dfrac{1}{n}<\dfrac{1}{n-1}$，故有 $ET_{1}<ET_{2},DT_{1}<DT_{2}$，所以选择（D）",
])
