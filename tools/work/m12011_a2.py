# -*- coding: utf-8 -*-
"""2011 数学一 解析 填空题 9-14（原卷 p6-p8，逐字照录【答案】【解析】）"""

A = {}

A[9] = (r"\ln(\sqrt{2}+1)", [
    r"【答案】$\ln(\sqrt{2}+1)$",
    r"【解析】由弧长公式知",
    r"$s=\int_{0}^{\frac{\pi}{4}}\sqrt{1+(y')^{2}}dx$",
    r"$=\int_{0}^{\frac{\pi}{4}}\sqrt{1+\tan^{2}x}dx=\int_{0}^{\frac{\pi}{4}}\sec xdx$",
    r"$=\ln|\sec x+\tan x|\Big|_{0}^{\frac{\pi}{4}}=\ln(\sqrt{2}+1)$",
])

A[10] = (r"e^{-x}\sin x", [
    r"【答案】$e^{-x}\sin x$",
    r"【解析】由一阶线性微分方程的求解公式",
    r"$y=e^{-\int1dx}(C+\int e^{-x}\cos x\cdot e^{\int1dx}dx)=e^{-x}(C+\sin x)$",
    r"由于 $y(0)=0$，所以 $y=e^{-x}\sin x$.",
])

A[11] = ("4", [
    r"【答案】4",
    r"【解析】由题意知",
    r"$\dfrac{\partial F}{\partial x}=\dfrac{\sin(xy)}{1+(xy)^{2}}y$，$\dfrac{\partial F}{\partial x}\Big|_{y=2}=\dfrac{2\sin2x}{1+4x^{2}}$",
    r"$\dfrac{\partial^{2}F}{\partial x^{2}}\Big|_{x=0,y=2}=\dfrac{\partial\left(\dfrac{\partial F}{\partial x}\Big|_{y=2}\right)}{\partial x}\Bigg|_{x=0}=\dfrac{d}{dx}\left(\dfrac{2\sin2x}{1+4x^{2}}\right)\Bigg|_{x=0}"
    r"=\dfrac{4\cos2x\cdot(1+4x^{2})-8x\cdot2\sin2x}{(1+4x^{2})^{2}}\Bigg|_{x=0}=4$",
    r"【注】这里对 $x$ 求偏导，$y$ 当成常量看待，所以可以把先 $y=2$ 代入再对 $x$ 偏导",
])

A[12] = (r"\pi", [
    r"【答案】$\pi$",
    r"【解析】方法一：利用斯托克斯公式",
    r"$I=\oint_{L}xz\,dx+x\,dy+\dfrac{y^{2}}{2}dz=\iint\limits_{\Sigma}\begin{vmatrix}-\dfrac{1}{\sqrt{3}}&-\dfrac{1}{\sqrt{3}}&\dfrac{1}{\sqrt{3}}\\ \dfrac{\partial}{\partial x}&\dfrac{\partial}{\partial y}&\dfrac{\partial}{\partial z}\\ xz&x&\dfrac{y^{2}}{2}\end{vmatrix}dS$",
    r"$=\iint\limits_{\Sigma}\dfrac{1}{\sqrt{3}}(1-x-y)dS=\iint\limits_{x^{2}+y^{2}\leqslant1}(1-x-y)dxdy=\iint\limits_{x^{2}+y^{2}\leqslant1}dxdy$",
    r"$=\pi$",
    r"方法二：将 $L$ 的方程化为参数方程形式：$\begin{cases}x=\cos t\\ y=\sin t\\ z=\cos t+\sin t\end{cases},(0\leqslant t\leqslant2\pi)$，则",
    r"$I=\oint_{L}xz\,dx+x\,dy+\dfrac{y^{2}}{2}dz$",
    r"$=\int_{0}^{2\pi}\left[\cos t\cdot(\cos t+\sin t)\cdot(-\sin t)+\cos t\cdot\cos t+\dfrac{1}{2}\sin^{2}t(-\sin t+\cos t)\right]dt$",
    r"$=\int_{0}^{2\pi}\cos^{2}tdt=\int_{0}^{2\pi}\dfrac{1+\cos2t}{2}dt$",
    r"$=\pi$",
])

A[13] = ("1", [
    r"【答案】1",
    r"【解析】由题意知二次型矩阵 $\boldsymbol{A}=\begin{pmatrix}1&a&1\\a&3&1\\1&1&1\end{pmatrix}$ 的特征值为 0,1,4，故",
    r"$|\boldsymbol{A}|=\begin{vmatrix}1&a&1\\a&3&1\\1&1&1\end{vmatrix}=0$",
    r"解得 $a=1$",
])

A[14] = (r"\mu(\mu^{2}+\sigma^{2})", [
    r"【答案】$\mu(\mu^{2}+\sigma^{2})$",
    r"【解析】由题知 $X$ 与 $Y$ 的相关系数 $\rho_{XY}=0$，即 $X$ 与 $Y$ 不相关.",
    r"当 $(X,Y)$ 服从二维正态分布，$X$ 与 $Y$ 不相关 $\Leftrightarrow$ $X$ 与 $Y$ 独立",
    r"所以 $X$ 与 $Y$ 独立，则有",
    r"$EX=EY=\mu, DX=DY=\sigma^{2}$",
    r"$EY^{2}=DY+(EY)^{2}=\mu^{2}+\sigma^{2}$",
    r"$E\left(XY^{2}\right)=EXEY^{2}=\mu\left(\mu^{2}+\sigma^{2}\right)$.",
])
