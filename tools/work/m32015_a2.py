# -*- coding: utf-8 -*-
"""2015 数学三 解析 填空题 9-14（原卷 p7-p8，逐字照录）"""

A = {}

A[9] = (r"-\dfrac{1}{2}", [
    r"【答案】$-\dfrac{1}{2}$",
    r"【解析】原极限$\lim\limits_{x\to0}\dfrac{\ln(1+\cos x-1)}{x^{2}}=\lim\limits_{x\to0}\dfrac{\cos x-1}{x^{2}}=-\dfrac{1}{2}$.",
])

A[10] = ("2", [
    r"【答案】$2$",
    r"【解析】因为 $f(x)$ 连续，所以 $\varphi(x)$ 可导，所以 $\varphi'(x)=\int_{0}^{x^{2}}f(t)\mathrm{d}t+2x^{2}f(x^{2})$；",
    r"因为 $\varphi(1)=1$，所以 $\varphi(1)=\int_{0}^{1}f(t)\mathrm{d}t=1$,",
    r"又因为 $\varphi'(1)=5$，所以 $\varphi'(1)=\int_{0}^{1}f(t)\mathrm{d}t+2f(1)=5$.故 $f(1)=2$.",
])

A[11] = (r"-\dfrac{1}{3}dx-\dfrac{2}{3}dy", [
    r"【答案】$-\dfrac{1}{3}dx-\dfrac{2}{3}dy$",
    r"【解析】当 $x=0,y=0$ 时带入 $\mathrm{e}^{x+2y+3z}+xyz=1$，得 $z=0$.",
    r"对 $\mathrm{e}^{x+2y+3z}+xyz=1$求微分，得 $\mathrm{d}\left(\mathrm{e}^{x+2y+3z}+xyz\right)=\mathrm{e}^{x+2y+3z}d(x+2y+3z)+d(xyz)$",
    r"$=\mathrm{e}^{x+2y+3z}\left(dx+2dy+3dz\right)+yzdx+xzdy+xydz=0$",
    r"把 $x=0,y=0,z=0$ 代入上式，得 $dx+2dy+3dz=0$",
    r"所以 $dz\big|_{(0,0)}=-\dfrac{1}{3}dx-\dfrac{2}{3}dy$.",
])

A[12] = (r"e^{-2x}+2e^{x}", [
    r"【答案】$y(x)=e^{-2x}+2e^{x}$",
    r"【解析】$y''+y'-2y=0$ 的特征方程为 $\lambda^{2}+\lambda-2=0$，特征根为 $\lambda=-2,\lambda=1$，所以该齐",
    r"次微分方程的通解为 $y(x)=C_{1}e^{-2x}+C_{2}e^{x}$，因为 $y(x)$ 可导，所以 $x=0$ 为驻点，即",
    r"$y(0)=3,y'(0)=0$，所以 $C_{1}=1,C_{2}=2$，故 $y(x)=e^{-2x}+2e^{x}$.",
])

A[13] = ("21", [
    r"【答案】$21$",
    r"【解析】$\boldsymbol{A}$ 的所有特征值为 $2,-2,1,\boldsymbol{B}$ 的所有特征值为 $3,7,1$. 所以$\left|\boldsymbol{B}\right|=3\times7\times1=21$.",
])

A[14] = (r"\dfrac{1}{2}", [
    r"【答案】$\dfrac{1}{2}$",
    r"【解析】由题设知，$X\sim N(1,1),Y\sim N(0,1)$，而且 $X$、$Y$ 相互独立，从而",
    r"$P\{XY-Y<0\}=P\{(X-1)Y<0\}=P\{X-1>0,Y<0\}+P\{X-1<0,Y>0\}$",
    r"$=P\{X>1\}P\{Y<0\}+P\{X<1\}P\{Y>0\}=\dfrac{1}{2}\times\dfrac{1}{2}+\dfrac{1}{2}\times\dfrac{1}{2}=\dfrac{1}{2}$.",
])
