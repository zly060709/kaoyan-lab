# -*- coding: utf-8 -*-
"""2022 数学二 答案解析（视觉转录自 data/math2/pages/2022/p5-p11.png，原卷照录）。
键为题号；value = (answer, [解析行])。"""

A = {}

A[1] = ("C", [
    r"①若 $\alpha(x)\sim\beta(x)$，则 $\lim\limits_{x\to 0}\dfrac{\alpha(x)}{\beta(x)}=1$。因此 $\lim\limits_{x\to 0}\dfrac{\alpha^{2}(x)}{\beta^{2}(x)}=\lim\limits_{x\to 0}\dfrac{\alpha(x)}{\beta(x)}\cdot\dfrac{\alpha(x)}{\beta(x)}=1\cdot 1=1$，①正确。",
    r"②错，反例 $\alpha(x)=x,\beta(x)=-x$；",
    r"③若 $\alpha(x)\sim\beta(x)$，则 $\lim\limits_{x\to 0}\dfrac{\alpha(x)}{\beta(x)}=1$，则 $\lim\limits_{x\to 0}\dfrac{\alpha(x)-\beta(x)}{\alpha(x)}=\lim\limits_{x\to 0}\dfrac{\alpha(x)}{\alpha(x)}-\dfrac{\beta(x)}{\alpha(x)}=1-1=0$，因此 $\alpha(x)-\beta(x)=o(\alpha(x))$，③正确。",
    r"④若 $\alpha(x)-\beta(x)=o(\alpha(x))$，则 $\lim\limits_{x\to 0}\dfrac{\alpha(x)-\beta(x)}{\alpha(x)}=0$，则 $\lim\limits_{x\to 0}\dfrac{\alpha(x)}{\alpha(x)}-\dfrac{\beta(x)}{\alpha(x)}=1-\lim\limits_{x\to 0}\dfrac{\beta(x)}{\alpha(x)}=0$，则 $\lim\limits_{x\to 0}\dfrac{\beta(x)}{\alpha(x)}=1$，即 $\alpha(x)\sim\beta(x)$，④正确。",
    r"因此真命题有①③④，选（C）",
])

A[2] = ("D", [
    r"$\displaystyle\int_{0}^{2}\mathrm{d}y\int_{y}^{2}\dfrac{y}{\sqrt{1+x^{3}}}\mathrm{d}x=\int_{0}^{2}\mathrm{d}x\int_{0}^{x}\dfrac{y}{\sqrt{1+x^{3}}}\mathrm{d}y=\int_{0}^{2}\dfrac{x^{2}}{2\sqrt{1+x^{3}}}\mathrm{d}x$",
    r"$=\displaystyle\int_{0}^{2}\dfrac{1}{6\sqrt{1+x^{3}}}\mathrm{d}(1+x^{3})\ =\dfrac{1}{3}\sqrt{1+x^{3}}\Big|_{0}^{2}=\dfrac{2}{3}$。",
])

A[3] = ("B", [
    r"$f(x)$ 在 $x=x_{0}$ 处二阶可导，则 $f(x)$ 在 $x=x_{0}$ 处一阶连续可导，若 $f'(x_{0})>0$，则在 $x=x_{0}$ 的邻域内 $f'(x)$ 均大于 0（局部保号性），因此 $f(x)$ 在此邻域内单调增。",
])

A[4] = ("C", [
    r"$F(x,y)=\displaystyle\int_{0}^{x-y}(x-y-t)f(t)\mathrm{d}t=x\int_{0}^{x-y}f(t)\mathrm{d}t-y\int_{0}^{x-y}f(t)\mathrm{d}t-\int_{0}^{x-y}tf(t)\mathrm{d}t$",
    r"所以 $\dfrac{\partial F}{\partial x}=\displaystyle\int_{0}^{x-y}f(t)\mathrm{d}t+xf(x-y)-yf(x-y)-(x-y)f(x-y)=\int_{0}^{x-y}f(t)\mathrm{d}t$",
    r"$\dfrac{\partial F}{\partial y}=-xf(x-y)-\displaystyle\int_{0}^{x-y}f(t)\mathrm{d}t+yf(x-y)+(x-y)f(x-y)=-\int_{0}^{x-y}f(t)\mathrm{d}t$",
    r"即 $\dfrac{\partial F}{\partial x}=-\dfrac{\partial F}{\partial y}$",
    r"$\dfrac{\partial^{2}F}{\partial x^{2}}=f(x-y),\ \dfrac{\partial^{2}F}{\partial y^{2}}=f(x-y),\ \therefore\dfrac{\partial^{2}F}{\partial x^{2}}=\dfrac{\partial^{2}F}{\partial y^{2}}$",
    r"综上，正确选项为（C）",
])

A[5] = ("A", [
    r"【解析】先考虑 $\displaystyle\int_{0}^{\frac{1}{2}}\dfrac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x$，",
    r"若 $p<1$，因为 $\lim\limits_{x\to 0^{+}}\dfrac{\dfrac{\ln x}{x^{p}(1-x)^{1-p}}}{\dfrac{1}{x^{\frac{1+p}{2}}}}=\lim\limits_{x\to 0^{+}}\left(x^{\frac{1-p}{2}}\cdot\ln x\right)=0$，而 $\displaystyle\int_{0}^{\frac{1}{2}}\dfrac{1}{x^{\frac{1+p}{2}}}\mathrm{d}x$ 收敛，故 $\displaystyle\int_{0}^{\frac{1}{2}}\dfrac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x$ 也收敛；",
    r"若 $p\geq 1$，$\lim\limits_{x\to 0^{+}}\dfrac{\dfrac{\ln x}{x^{p}(1-x)^{1-p}}}{\dfrac{1}{x}}=\lim\limits_{x\to 0^{+}}\dfrac{\ln x}{x^{p-1}}=\infty$，且 $\displaystyle\int_{0}^{\frac{1}{2}}\dfrac{1}{x}\mathrm{d}x$ 发散，故 $\displaystyle\int_{0}^{\frac{1}{2}}\dfrac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x$ 也发散。",
    r"再考虑 $\displaystyle\int_{\frac{1}{2}}^{1}\dfrac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x$，$\lim\limits_{x\to 1^{-}}\dfrac{\dfrac{\ln x}{x^{p}(1-x)^{1-p}}}{\dfrac{1}{(1-x)^{-p}}}=\lim\limits_{x\to 1^{-}}\dfrac{x-1}{(1-x)^{1-p}}=-1\neq 0$，",
    r"故 $\displaystyle\int_{\frac{1}{2}}^{1}\dfrac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x$ 与 $\displaystyle\int_{\frac{1}{2}}^{1}\dfrac{1}{(1-x)^{-p}}\mathrm{d}x$ 同敛散，故 $-p<1$，即 $p>-1$，选（A）",
])

A[6] = ("D", [
    r"【解析】取 $x_{n}=(-1)^{n}\dfrac{\pi}{2}$，则（A）、（B）、（C）均错，且（D）的“$\lim\limits_{n\to\infty}x_{n}$ 不一定存在”是正确的；（D）的“$\lim\limits_{n\to\infty}\cos x_{n}$ 存在”的原因：当 $-\dfrac{\pi}{2}\leq x_{n}\leq\dfrac{\pi}{2}$ 时，$0\leq\cos x_{n}\leq 1$，而 $\sin x$ 在 $[0,1]$ 上单调，故 $\lim\limits_{n\to\infty}\cos x_{n}$ 存在。",
])
