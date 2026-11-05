# -*- coding: utf-8 -*-
"""2009 数学一 解析 填空题 9-14（原卷 p8-p9，逐字照录【答案】【解析】）"""

A = {}

A[9] = (r"xf_{12}''+f_{2}'+xyf_{22}''", [
    r"【答案】$xf_{12}''+f_{2}'+xyf_{22}''$.",
    r"【解析】$\dfrac{\partial z}{\partial x}=f_{1}'+f_{2}'.y$, $\dfrac{\partial^{2}z}{\partial x\partial y}=xf_{12}''+f_{2}'+xyf_{22}''$.",
])

A[10] = (r"-xe^{x}+x+2", [
    r"【答案】$y=-xe^{x}+x+2$.",
    r"【解析】由 $y=(C_{1}+C_{2}x)e^{x}$，得二阶常系数线性齐次微分方程 $y''+ay'+by=0$ 的特征",
    r"值 $\lambda_{1}=\lambda_{2}=1$，故 $a=-2,b=1$，要求解的微分方程为 $y''-2y'+y=x$.",
    r"设特解 $y_{0}=Ax+B$ 代入微分方程 $y''-2y'+y=x$，得出 $-2A+Ax+B=x$, $A=1$,",
    r"$B=2$,故微分方程为的 $y''-2y'+y=x$ 特解 $y''=x+2$，通解为",
    r"$y=(C_{1}+C_{2}x)e^{x}+x+2$ 代入初始条件 $y(0)=2, y'(0)=0$，得 $C_{1}=0,C_{2}=-1$，要求",
    r"的解为 $y=-xe^{x}+x+2$.",
])

A[11] = (r"\dfrac{13}{6}", [
    r"【答案】$\dfrac{13}{6}$",
    r"【解析】由题意，$x=x, y=x^{2},0\leqslant x\leqslant\sqrt{2}$，则 $ds=\sqrt{(x')^{2}+(y')^{2}}dx=\sqrt{1+4x^{2}}dx$，",
    r"所以 $\int_{L}xds=\int_{0}^{\sqrt{2}}x\sqrt{1+4x^{2}}dx=\dfrac{1}{8}\int_{0}^{\sqrt{2}}\sqrt{1+4x^{2}}d(1+4x^{2})=\dfrac{1}{8}\cdot\dfrac{2}{3}\sqrt{(1+4x^{2})^{3}}\Big|_{0}^{\sqrt{2}}=\dfrac{13}{6}$.",
])

A[12] = (r"\dfrac{4}{15}\pi", [
    r"【答案】$\dfrac{4}{15}\pi$.",
    r"【解析】（方法一）由轮换对称性，$\iiint\limits_{\Omega}x^{2}dxdydz=\iiint\limits_{\Omega}y^{2}dxdydz=\iiint\limits_{\Omega}z^{2}dxdydz$",
    r"$\iiint\limits_{\Omega}z^{2}dxdydz=\dfrac{1}{3}\iiint\limits_{\Omega}(x^{2}+y^{2}+z^{2})dxdydz=\dfrac{1}{3}\int_{0}^{2\pi}d\theta\int_{0}^{\pi}d\varphi\int_{0}^{1}\rho^{2}\cdot\rho^{2}\sin\varphi d\rho=\dfrac{4}{15}\pi$",
    r"（方法二）$\iiint\limits_{\Omega}z^{2}dxdydz=\int_{0}^{2\pi}d\theta\int_{0}^{\pi}d\varphi\int_{0}^{1}\rho^{2}\sin\varphi\cdot\rho^{2}\cos^{2}\varphi d\rho$",
    r"$=\int_{0}^{2\pi}d\theta\int_{0}^{\pi}\cos^{2}\varphi d(-\cos\varphi)\int_{0}^{1}\rho^{4}d\rho=2\pi\cdot\dfrac{2}{3}\cdot\dfrac{1}{5}=\dfrac{4}{15}\pi$.",
])

A[13] = ("2", [
    r"【答案】2",
    r"【解析】由 $\boldsymbol{\alpha}^{T}\boldsymbol{\beta}=2$, $\left(\boldsymbol{\beta}\boldsymbol{\alpha}^{T}\right)\boldsymbol{\beta}=\boldsymbol{\beta}\left(\boldsymbol{\alpha}^{T}\boldsymbol{\beta}\right)=2\boldsymbol{\beta}$, 得 $\boldsymbol{\beta}\boldsymbol{\alpha}^{T}$ 的非零特征值为 2.",
])

A[14] = ("-1", [
    r"【答案】$-1$",
    r"【解析】由 $\overline{X}+kS^{2}$ 为 $np^{2}$ 的无偏估计,即 $np+knp(1-p)=np^{2}$；即 $1+k(1-p)=p$，",
    r"从而 $k=-1$.",
])
