# -*- coding: utf-8 -*-
"""2023 数学二 答案解析（视觉转录自 p9-p10）。本文件：第 (17)(18) 题。"""

A = {}

A[17] = (r"(1) $y(x)=-x\ln x+2x$；(2) 在 $\left(\mathrm{e}^{\frac{3}{2}},\dfrac{1}{2}\mathrm{e}^{\frac{3}{2}}\right)$ 处面积最小，$S_{\min}=\mathrm{e}^{3}$", [
    r"(1) 设在点 $P$ 处的切线为 $Y-y=y'(X-x)$，在 $y$ 轴上的截距为 $y-xy'$，",
    r"点 $P$ 到 $y$ 轴距离为 $x$，所以可列微分方程 $x=y-xy'$，整理得 $y'=\dfrac{y}{x}-1$，",
    r"解得 $y=-x\ln x+Cx$，又因为曲线过点 $\left(\mathrm{e}^{2},0\right)$，得 $C=2$，",
    r"所以 $y=-x\ln x+2x$。",
    r"(2) 切线为 $Y-y=y'(X-x)$ 在 $y$ 轴上的截距为 $y-xy'$，在 $x$ 轴上的截距为 $x-\dfrac{y}{y'}$，",
    r"所以三角形面积为 $S=\dfrac{1}{2}|y-xy'|\left|x-\dfrac{y}{y'}\right|$，代入 $y=-x\ln x+2x$，$y'=1-\ln x$，",
    r"化简为 $S=\dfrac{1}{2}\dfrac{x^{2}}{\ln x-1}$，$\dfrac{\mathrm{d}S}{\mathrm{d}x}=\dfrac{1}{2}\dfrac{2x(\ln x-1)-x}{(\ln x-1)^{2}}=\dfrac{1}{2}\dfrac{x(2\ln x-3)}{(\ln x-1)^{2}}$，",
    r"当 $x<\mathrm{e}^{\frac{3}{2}}$ 时 $\dfrac{\mathrm{d}S}{\mathrm{d}x}<0$，当 $x>\mathrm{e}^{\frac{3}{2}}$ 时 $\dfrac{\mathrm{d}S}{\mathrm{d}x}>0$，",
    r"所以 $\left(\mathrm{e}^{\frac{3}{2}},\dfrac{1}{2}\mathrm{e}^{\frac{3}{2}}\right)$ 取到面积最小值，最小值为 $S=\mathrm{e}^{3}$。",
])

A[18] = (r"极小值 $-\dfrac{\mathrm{e}^{2}}{2}$", [
    r"$f_{x}'(x,y)=\mathrm{e}^{\cos y}+x,\ f_{y}'(x,y)=x\mathrm{e}^{\cos y}(-\sin y)$",
    r"令 $f_{x}'(x,y)=f_{y}'(x,y)=0$",
    r"解得 $\begin{cases}x=-\mathrm{e}\\ y=2k\pi\end{cases}$，$\begin{cases}x=-\mathrm{e}^{-1}\\ y=(2k+1)\pi\end{cases}$，其中 $k=0,\pm1,\pm2,\cdots$",
    r"又 $f_{xx}''(x,y)=1,\ f_{xy}''(x,y)=\mathrm{e}^{\cos y}(-\sin y),\ f_{yy}''(x,y)=x\mathrm{e}^{\cos y}(\sin^{2}y-\cos y)$",
    r"当 $x=-\mathrm{e}$，$y=2k\pi$ 时，$A=1,B=0,C=\mathrm{e}^{2},AC-B^{2}>0$，且 $A>0$，则存在极小值，",
    r"极小值为 $f(-\mathrm{e},2k\pi)=-\dfrac{\mathrm{e}^{2}}{2}$。",
    r"当 $x=-\mathrm{e}^{-1}$，$y=(2k-1)\pi$ 时，$A=1,B=0,C=-\mathrm{e}^{-2},AC-B^{2}<0$，则不存在极值。",
    r"故函数 $f(x,y)$ 存在极小值，极小值为 $f(-\mathrm{e},2k\pi)=-\dfrac{\mathrm{e}^{2}}{2}$。",
])
