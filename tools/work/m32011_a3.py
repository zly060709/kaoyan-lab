# -*- coding: utf-8 -*-
"""2011 数学三 解析 解答题 15-23（原卷 p8-p13，逐字照录）"""

A = {}

A[15] = (r"-\dfrac{1}{2}", [
    r"【解析】法一：$\lim\limits_{x\to0}\dfrac{\sqrt{1+2\sin x}-x-1}{x\ln(1+x)}"
    r"=\lim\limits_{x\to0}\dfrac{\sqrt{1+2\sin x}-x-1}{x^{2}}$",
    r"$=\lim\limits_{x\to0}\dfrac{\cos x-\sqrt{1+2\sin x}}{2x\sqrt{1+2\sin x}}"
    r"=\lim\limits_{x\to0}\dfrac{\cos x-\sqrt{1+2\sin x}}{2x}$",
    r"$=\dfrac{1}{2}\lim\limits_{x\to0}\left(-\sin x-\dfrac{\cos x}{\sqrt{1+2\sin x}}\right)=-\dfrac{1}{2}$",
    r"法二：$\lim\limits_{x\to0}\dfrac{\sqrt{1+2\sin x}-x-1}{x\ln(1+x)}"
    r"=\lim\limits_{x\to0}\dfrac{1+2\sin x-(x+1)^{2}}{x^{2}\left(\sqrt{1+2\sin x}+x+1\right)}$",
    r"$=\dfrac{1}{2}\lim\limits_{x\to0}\dfrac{2\sin x-x^{2}-2x}{x^{2}}"
    r"=-\dfrac{1}{2}+\lim\limits_{x\to0}\dfrac{\sin x-x}{x^{2}}"
    r"=-\dfrac{1}{2}+\lim\limits_{x\to0}\dfrac{\cos x-1}{2x}=-\dfrac{1}{2}$.",
])

A[16] = (r"f_{uu}''(2,2)+f_{v}'(2,2)f_{uv}''(1,1)", [
    r"【解析】令 $u=x+y,v=f(x,y)$，则",
    r"$\dfrac{\partial z}{\partial x}=z_{u}'+z_{v}'v_{x}'$，"
    r"$\dfrac{\partial^{2}z}{\partial x\partial y}=z_{uu}''+z_{uv}''v_{y}'"
    r"+\left(z_{vu}''+z_{vv}''v_{y}'\right)v_{x}'+z_{v}'v_{xy}''$.",
    r"由于 $f(1,1)=2$ 是 $f(u,v)$ 的极值，$f_{u}'(1,1)=f_{v}'(1,1)=0$，",
    r"所以 $\dfrac{\partial^{2}z}{\partial x\partial y}\Big|_{x=1,y=1}"
    r"=f_{uu}''(2,2)+f_{v}'(2,2)f_{uv}''(1,1)$.",
])

A[17] = (r"2\sqrt{x}(\arcsin\sqrt{x}+\ln x)-4\sqrt{x}+2\sqrt{1-x}+C", [
    r"【解析】令 $t=\sqrt{x}$，则有",
    r"$\int\dfrac{\arcsin\sqrt{x}+\ln x}{\sqrt{x}}\mathrm{d}x=\int\dfrac{\arcsin t+2\ln t}{t}2tdt"
    r"=2\int\left(\arcsin t+2\ln t\right)dt$",
    r"$=2t\left(\arcsin t+2\ln t\right)-2\int t\left(\dfrac{1}{\sqrt{1-t^{2}}}+\dfrac{2}{t}\right)dt$",
    r"$=2t\left(\arcsin t+2\ln t\right)-4t-2\int\dfrac{t}{\sqrt{1-t^{2}}}dt$",
    r"$=2t\left(\arcsin t+2\ln t\right)-4t+\int\dfrac{\mathrm{d}(1-t^{2})}{\sqrt{1-t^{2}}}$",
    r"$=2t\left(\arcsin t+2\ln t\right)-4t+2\sqrt{1-t^{2}}+C$",
    r"$=2\sqrt{x}\left(\arcsin\sqrt{x}+\ln x\right)-4\sqrt{x}+2\sqrt{1-x}+C$",
])

A[18] = ("证明见解析", [
    r"【证明】设 $f(x)=4\arctan x-x+\dfrac{4\pi}{3}-\sqrt{3}$，$x\in(-\infty,+\infty)$",
    r"令 $f'(x)=\dfrac{3-x^{2}}{1+x^{2}}=0$，得 $x=\pm\sqrt{3}$.",
    r"当 $x\in(-\infty,-\sqrt{3})$ 和 $(\sqrt{3},+\infty)$ 时，$f'(x)<0$，此时 $f(x)$ 在 "
    r"$(-\infty,-\sqrt{3})$ 或 $(\sqrt{3},+\infty)$ 上单调递减；",
    r"当 $x\in(-\sqrt{3},\sqrt{3})$ 时，$f'(x)>0$，此时 $f(x)$ 在 $(-\sqrt{3},\sqrt{3})$ 上单调递增.",
    r"由于 $\lim\limits_{x\to-\infty}f(x)=+\infty$，$f(-\sqrt{3})=0$，"
    r"所以在区间 $(-\infty,-\sqrt{3}]$ 内 $f(x)$ 有唯一的零点 $x=-\sqrt{3}$；",
    r"由于 $f(\sqrt{3})=2\left(\dfrac{4\pi}{3}-\sqrt{3}\right)>0$，"
    r"$\lim\limits_{x\to+\infty}f(x)=-\infty$，所以在区间 $(\sqrt{3},+\infty)$ 内 $f(x)$ 有唯一零点，",
    r"在 $(-\sqrt{3},\sqrt{3})$ 内都没有实根.",
    r"综上所述，方程恰有两个实根.",
])

A[19] = (r"f(x)=\dfrac{4}{(2-x)^{2}},\ x\in[0,1]", [
    r"【解析】方程两端分别为",
    r"$\iint\limits_{D_{t}}f(t)\mathrm{d}x\mathrm{d}y=\dfrac{1}{2}t^{2}f(t)$",
    r"$\iint\limits_{D_{t}}f'(x+y)\mathrm{d}x\mathrm{d}y=\int_{0}^{t}\mathrm{d}x\int_{0}^{t-x}f'(x+y)\mathrm{d}y"
    r"=\int_{0}^{t}[f(t)-f(x)]\mathrm{d}x=tf(t)-\int_{0}^{t}f(x)\mathrm{d}x$",
    r"由题意知 $tf(t)-\int_{0}^{t}f(x)dx=\dfrac{1}{2}t^{2}f(t)$，",
    r"两边求导整理得 $(2-t)f'(t)=2f(t)$",
    r"解得 $f(t)=\dfrac{C}{(2-t)^{2}}$（$C$ 为任意常数）",
    r"将 $f(0)=1$ 代入，得 $C=4$，所以 $f(t)=\dfrac{4}{(2-t)^{2}}$，"
    r"即 $f(x)=\dfrac{4}{(2-x)^{2}}$，$x\in[0,1]$.",
])

A[20] = (r"(1)\ a=5;\ (2)\ \beta_{1}=2\alpha_{1}+4\alpha_{2}-\alpha_{3},\ "
         r"\beta_{2}=\alpha_{1}+2\alpha_{2},\ \beta_{3}=5\alpha_{1}+10\alpha_{2}-2\alpha_{3}", [
    r"【解析】(1) 易知 $\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}$ 线性无关，"
    r"由其不能被 $\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3}$ 线性表出，"
    r"得到 $\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3}$ 线性相关，"
    r"从而 $r(\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3})<3$.",
    r"由",
    r"$\begin{pmatrix}1&1&3\\1&2&4\\1&3&a\end{pmatrix}\to"
    r"\begin{pmatrix}1&1&3\\0&1&1\\0&2&a-3\end{pmatrix}\to"
    r"\begin{pmatrix}1&1&1\\0&1&1\\0&0&a-5\end{pmatrix}$",
    r"得 $a=5$.",
    r"(2) $(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}:"
    r"\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3})"
    r"=\begin{pmatrix}1&0&1&1&1&3\\0&1&3&1&2&4\\1&1&5&1&3&5\end{pmatrix}\to"
    r"\begin{pmatrix}1&0&1&1&1&3\\0&1&3&1&2&4\\0&1&4&0&2&2\end{pmatrix}$",
    r"$\to\begin{pmatrix}1&0&1&1&1&3\\0&1&3&1&2&4\\0&0&1&-1&0&-2\end{pmatrix}"
    r"\begin{pmatrix}1&0&0&2&1&5\\0&1&0&4&2&10\\0&0&1&-1&0&-2\end{pmatrix}$",
    r"故 $\boldsymbol{\beta}_{1}=2\boldsymbol{\alpha}_{1}+4\boldsymbol{\alpha}_{2}"
    r"-\boldsymbol{\alpha}_{3}$，$\boldsymbol{\beta}_{2}=\boldsymbol{\alpha}_{1}"
    r"+2\boldsymbol{\alpha}_{2}$，$\boldsymbol{\beta}_{3}=5\boldsymbol{\alpha}_{1}"
    r"+10\boldsymbol{\alpha}_{2}-2\boldsymbol{\alpha}_{3}$",
])

A[21] = (r"(1)\ \lambda_{1}=-1,\lambda_{2}=1,\lambda_{3}=0;\ (2)\ \boldsymbol{A}="
         r"\begin{pmatrix}0&0&1\\0&0&0\\1&0&0\end{pmatrix}", [
    r"【解析】(1) 根据题意，$\boldsymbol{A}\begin{pmatrix}1\\0\\-1\end{pmatrix}"
    r"=-1\times\begin{pmatrix}1\\0\\-1\end{pmatrix}$，"
    r"$\boldsymbol{A}\begin{pmatrix}1\\0\\1\end{pmatrix}=1\times\begin{pmatrix}1\\0\\1\end{pmatrix}$",
    r"所以特征值 $-1$ 对应的特征向量为 $k_{1}\begin{pmatrix}1\\0\\-1\end{pmatrix}$，"
    r"特征值 1 对应的特征向量为 $k_{2}\begin{pmatrix}1\\0\\1\end{pmatrix}$.",
    r"由 $r(\boldsymbol{A})=2$ 知 $\boldsymbol{A}$ 的另一个特征值为 0，"
    r"设特征值为 0 对应的特征向量为 $k_{3}\begin{pmatrix}x_{1}\\x_{2}\\x_{3}\end{pmatrix}$.",
    r"因为实对称矩阵不同特征值得特征向量正交，得到 "
    r"$\begin{cases}x_{1}-x_{3}=0\\x_{1}+x_{3}=0\end{cases}$",
    r"从而特征值 0 对应的特征向量为 $k_{3}\begin{pmatrix}0\\1\\0\end{pmatrix}$，"
    r"其中 $k_{1},k_{2},k_{3}$ 为不为零的任意常数.",
    r"(2) 令 $\boldsymbol{P}=\begin{pmatrix}1&1&0\\0&0&1\\-1&1&0\end{pmatrix}$，则 "
    r"$\boldsymbol{P}^{-1}=\begin{pmatrix}1&1&0\\0&0&1\\-1&1&0\end{pmatrix}^{-1}"
    r"=\begin{pmatrix}\dfrac{1}{2}&0&-\dfrac{1}{2}\\\dfrac{1}{2}&0&\dfrac{1}{2}\\0&1&0\end{pmatrix}$",
    r"由 $\boldsymbol{P}^{-1}\boldsymbol{AP}=\boldsymbol{\Lambda}$，知",
    r"$\boldsymbol{A}=\boldsymbol{P\Lambda P}^{-1}"
    r"=\begin{pmatrix}1&1&0\\0&0&1\\-1&1&0\end{pmatrix}"
    r"\begin{pmatrix}-1&0&0\\0&1&0\\0&0&0\end{pmatrix}"
    r"\begin{pmatrix}1&1&0\\0&0&1\\-1&1&0\end{pmatrix}^{-1}"
    r"=\begin{pmatrix}0&0&1\\0&0&0\\1&0&0\end{pmatrix}$",
])

A[22] = (r"(I)\ P\{X=0,Y=0\}=P\{X=1,Y=-1\}=P\{X=1,Y=1\}=1/3;\ "
         r"(II)\ P\{Z=-1\}=P\{Z=0\}=P\{Z=1\}=1/3;\ (III)\ \rho_{XY}=0", [
    r"【解析】（Ⅰ）由于 $P\{X^{2}=Y^{2}\}=1$，即",
    r"$P\{X=0,Y=0\}+P\{X=1,Y=-1\}+P\{X=1,Y=1\}=1$",
    r"则有",
    # 原卷此行排版为 "P{X=0,Y=-}1"（负号在花括号内、1 在括号外），照录
    r"$P\{X=1,Y=0\}=P\{X=0,Y=-\}1=P\{X=0,Y=1\}=0$",
    r"$P\{X=0,Y=0\}=P\{Y=0\}-P\{X=1,Y=0\}=\dfrac{1}{3}$",
    r"$P\{X=1,Y=-1\}=P\{Y=-1\}-P\{X=0,Y=-1\}=\dfrac{1}{3}$",
    r"$P\{X=1,Y=1\}=P\{Y=1\}-P\{X=0,Y=1\}=\dfrac{1}{3}$",
    r"所以 $(X,Y)$ 的概率分布为",
    # 原卷为表格：行 X=0：0，1/3，0；行 X=1：1/3，0，1/3（列 Y=-1,0,1），转录为线性文本
    r"$X=0$：$0$，$\dfrac{1}{3}$，$0$；$X=1$：$\dfrac{1}{3}$，$0$，$\dfrac{1}{3}$"
    r"（列 $Y$：$-1$，$0$，$1$）",
    r"（Ⅱ）易知随机变量 $Z$ 的可能取值为 $-1,0,1$，则有",
    r"$P\{Z=1\}=P\{X=1,Y=1\}=\dfrac{1}{3}$",
    r"$P\{Z=-1\}=P\{X=1,Y=-1\}=\dfrac{1}{3}$",
    r"$P\{Z=0\}=1-P\{Z=1\}-P\{Z=-1\}=\dfrac{1}{3}$",
    r"故 $Z=XY$ 的概率分布为",
    r"$Z$：$-1$，$0$，$1$；$P$：$\dfrac{1}{3}$，$\dfrac{1}{3}$，$\dfrac{1}{3}$",
    r"（Ⅲ）由（Ⅰ）和（Ⅱ）知",
    r"$E(XY)=EZ=(-1)\times\dfrac{1}{3}+1\times\dfrac{1}{3}=0$",
    r"$EX=\dfrac{2}{3}$，$EY=(-1)\times\dfrac{1}{3}+1\times\dfrac{1}{3}=0$",
    r"故有 $Cov(X,Y)=E(XY)-EXEY=0$，所以 $\rho_{XY}=0$.",
])

A[23] = (r"(I)\ f_{X}(x)=\begin{cases}x,&0<x\leqslant1\\2-x,&1<x<2\\0,&\text{其他}\end{cases};\ "
         r"(II)\ f_{X|Y}(x|y)=\begin{cases}\dfrac{1}{2(1-y)},&(x,y)\in G\\0,&(x,y)\notin G\end{cases}"
         r"\ (0<y<1)", [
    r"【解析】由题知二维随机变量 $(X,Y)$ 的概率密度函数为",
    r"$f(x,y)=\begin{cases}1,(x,y)\in G\\0,(x,y)\notin G\end{cases}$",
    r"（Ⅰ）由边缘密度的定义知",
    r"当 $0<x\leqslant1$ 时，有 $f_{x}(x)=\int_{-\infty}^{+\infty}f(x,y)\mathrm{d}y"
    r"=\int_{0}^{x}\mathrm{d}y=x$，",
    r"当 $1<x<2$ 时，有 $f_{x}(x)=\int_{0}^{2-x}\mathrm{d}y=2-x$，",
    r"所以 $f_{x}(x)=\begin{cases}x,&0<x\leqslant1\\2-x,&1<x<2\\0,&\text{其他}\end{cases}$",
    r"（Ⅱ）同（Ⅰ）可得",
    r"当 $0<y<1$ 时，有 $f_{y}(y)=\int_{-\infty}^{+\infty}f(x,y)\mathrm{d}x"
    r"=\int_{y}^{2-y}\mathrm{d}x=2(1-y)$",
    r"所以 $f_{y}(y)=\begin{cases}2(1-y),&0<y<1\\0,&\text{其他}\end{cases}$",
    r"当 $0<y<1$ 时",
    r"$f_{X|Y}(x|y)=\dfrac{f(x,y)}{f_{y}(y)}"
    r"=\begin{cases}\dfrac{1}{2(1-y)},&(x,y)\in G\\0,&(x,y)\notin G\end{cases}$.",
])
