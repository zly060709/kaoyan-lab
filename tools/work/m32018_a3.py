# -*- coding: utf-8 -*-
"""2018 数学三 解析 解答题 15-23（原卷 p9-p15，逐字照录）"""

A = {}

A[15] = (r"a=1,\ b=1", [
    r"【解析】$\lim\limits_{x\to+\infty}[(ax+b)e^{\frac{1}{x}}-x]=\lim\limits_{x\to+\infty}x(ae^{\frac{1}{x}}-1)+\lim\limits_{x\to+\infty}be^{\frac{1}{x}}$",
    r"$=\lim\limits_{x\to+\infty}x(ae^{\frac{1}{x}}-1)+b$，",
    r"因为极限存在，所以$\lim\limits_{x\to+\infty}(ae^{\frac{1}{x}}-1)=0$，即$a=1$.",
    r"而，$\lim\limits_{x\to+\infty}x(ae^{\frac{1}{x}}-1)+b=\lim\limits_{x\to+\infty}\dfrac{e^{\frac{1}{x}}-1}{\dfrac{1}{x}}+b=1+b=2$，所以$b=1$.",
    r"综上可得$a=1$，$b=1$.",
])

A[16] = (r"\dfrac{\sqrt{3}(\pi-2)}{32}", [
    r"【解析】积分区域如右图阴影部分所示，且曲线与直线的交点为"
    r"$\left(\dfrac{1}{\sqrt{2}},\dfrac{\sqrt{3}}{\sqrt{2}}\right)$.",
    r"则$\iint\limits_{D}x^{2}\mathrm{d}x\mathrm{d}y=\int_{0}^{\frac{\sqrt{2}}{2}}\mathrm{d}x\int_{\sqrt{3}x}^{\sqrt{3(1-x^{2})}}x^{2}\mathrm{d}y$",
    r"$=\sqrt{3}\int_{0}^{\frac{\sqrt{2}}{2}}x^{2}(\sqrt{1-x^{2}}-x)\mathrm{d}x$",
    r"$=\sqrt{3}(\int_{0}^{\frac{\sqrt{2}}{2}}x^{2}\sqrt{1-x^{2}}\mathrm{d}x-\int_{0}^{\frac{\sqrt{2}}{2}}x^{3}\mathrm{d}x)$，",
    r"其中，$\int_{0}^{\frac{\sqrt{2}}{2}}x^{2}\sqrt{1-x^{2}}\mathrm{d}x\xlongequal{x=\sin t}\int_{0}^{\frac{\pi}{4}}\sin^{2}t\cdot\cos^{2}t\mathrm{d}t$",
    r"$=\dfrac{1}{4}\int_{0}^{\frac{\pi}{4}}\sin^{2}2t\mathrm{d}t=\dfrac{1}{8}\int_{0}^{\frac{\pi}{4}}(1-\cos4t)\mathrm{d}t$",
    r"$=\dfrac{1}{8}(t-\dfrac{\sin4t}{4})\Big|_{0}^{\frac{\pi}{4}}=\dfrac{\pi}{32}$，",
    r"$\int_{0}^{\frac{\sqrt{2}}{2}}x^{3}\mathrm{d}x=\dfrac{x^{4}}{4}\Big|_{0}^{\frac{\sqrt{2}}{2}}=\dfrac{1}{16}$，",
    r"所以 $\iint\limits_{D}x^{2}\mathrm{d}x\mathrm{d}y=\sqrt{3}(\dfrac{\pi}{32}-\dfrac{1}{16})=\dfrac{\sqrt{3}(\pi-2)}{32}$.",
])

A[17] = (r"\text{存在},\ S_{\min}=\dfrac{1}{\pi+3\sqrt{3}+4}", [
    r"【解析】设圆的周长为$x$，正三角周长为$y$，正方形的周长$z$，由题设$x+y+z=2$.",
    r"则目标函数$S=\pi\left(\dfrac{x}{2\pi}\right)^{2}+\dfrac{1}{2}\cdot\dfrac{\sqrt{3}}{2}\left(\dfrac{y}{3}\right)^{2}+\left(\dfrac{z}{4}\right)^{2}"
    r"=\dfrac{x^{2}}{4\pi}+\dfrac{\sqrt{3}}{36}y^{2}+\dfrac{z^{2}}{16}$，",
    r"构造拉格朗日函数$L(x,y,z;\lambda)=\dfrac{x^{2}}{4\pi}+\dfrac{\sqrt{3}}{36}y^{2}+\dfrac{z^{2}}{16}+\lambda(x+y+z-2)$，"
    r"对参数求导并令导"
    r"函数为零，则",
    r"$\begin{cases}L_{x}'=\dfrac{x}{2\pi}+\lambda=0,\\ L_{y}'=\dfrac{2\sqrt{3}y}{36}+\lambda=0,\\ "
    r"L_{z}'=\dfrac{2z}{16}+\lambda=0,\\ L_{\lambda}'=x+y+z-2=0.\end{cases}$",
    r"解得$x=\dfrac{2\pi}{\pi+3\sqrt{3}+4}$，$y=\dfrac{6\sqrt{3}}{\pi+3\sqrt{3}+4}$，$z=\dfrac{8}{\pi+3\sqrt{3}+4}$，",
    r"此时面积和有最小值为$S=\dfrac{1}{\pi+3\sqrt{3}+4}\ (\mathrm{m}^{2})$.",
])

A[18] = (r"a_{n}=n+1\ (n=1,3,5,\cdots);\ a_{n}=\dfrac{(-1)^{n/2}2^{n}}{n!}-n-1\ (n=0,2,4,\cdots)", [
    r"【解析】根据函数的幂级数展开有",
    r"$\cos2x=\sum\limits_{n=0}^{\infty}\dfrac{(-1)^{n}}{(2n)!}(2x)^{2n}=\sum\limits_{n=0}^{\infty}\dfrac{(-1)^{n}}{(2n)!}4^{n}x^{2n}$，",
    r"$-\dfrac{1}{(1+x)^{2}}=\left(\dfrac{1}{1+x}\right)'=\sum\limits_{n=0}^{\infty}[(-x)^{n}]'"
    r"=\sum\limits_{n=1}^{\infty}(-1)^{n}nx^{n-1}=\sum\limits_{n=0}^{\infty}(-1)^{n+1}(n+1)x^{n}$，",
    r"所以，$\sum\limits_{n=0}^{\infty}\dfrac{(-1)^{n}}{(2n)!}4^{n}x^{2n}=\sum\limits_{n=0}^{\infty}a_{n}x^{n}"
    r"-\sum\limits_{n=0}^{\infty}(-1)^{n+1}(n+1)x^{n}=\sum\limits_{n=0}^{\infty}[a_{n}-(-1)^{n+1}(n+1)]x^{n}$，$-1<x<1$",
    r"因为左边缺奇数项，因此$n$为奇数时，$a_{n}-(-1)^{n+1}(n+1)=0$，即$a_{n}=n+1$；",
    r"此时，$\sum\limits_{n=0}^{\infty}[a_{n}-(-1)^{n+1}(n+1)]x^{n}=\sum\limits_{n=0}^{\infty}[a_{2n}-(-1)^{2n+1}(2n+1)]x^{2n}"
    r"=\sum\limits_{n=0}^{\infty}[a_{2n}+(2n+1)]x^{2n}$，",
    r"即$a_{2n}+(2n+1)=\dfrac{(-1)^{n}}{(2n)!}4^{n}$，$a_{2n}=\dfrac{(-1)^{n}}{(2n)!}4^{n}-(2n+1)$，",
    r"综上可得",
    r"$a_{n}=\begin{cases}n+1, & n=1,3,5,\cdots;\\ \dfrac{(-1)^{\frac{n}{2}}2^{n}}{n!}-n-1, & n=0,2,4,\cdots.\end{cases}$",
])

A[19] = (r"\{x_{n}\}\ \text{收敛},\ \lim\limits_{n\to\infty}x_{n}=0", [
    r"【解析】设$f(x)=e^{x}-1-x$, $x>0$，则有",
    r"$f'(x)=e^{x}-1>0$, $f(x)$单调增加，$f(x)>f(0)=0$，$\dfrac{e^{x}-1}{x}>1$，",
    r"从而$e^{x_{2}}=\dfrac{e^{x_{1}}-1}{x_{1}}>1$, $x_{2}>0$.",
    r"猜想$x_{n}>0$，现用数学归纳法证明：",
    r"$n=1$时，$x_{1}>0$，成立；",
    r"假设$n=k(k=1,2,\cdots)$时，有$x_{k}>0$，则$n=k+1$时有",
    r"$e^{x_{k+1}}=\dfrac{e^{x_{k}}-1}{x_{k}}>1$, $x_{k+1}>0$；",
    r"因此$x_{n}>0$，有下界. 再证单调性.",
    r"$x_{n+1}-x_{n}=\ln\dfrac{e^{x_{n}}-1}{x_{n}}-\ln e^{x_{n}}=\ln\dfrac{e^{x_{n}}-1}{x_{n}e^{x_{n}}}$.",
    r"设$g(x)=e^{x}-1-xe^{x}$，$x>0$时，$g'(x)=e^{x}-e^{x}-xe^{x}=-xe^{x}<0$，所以$g(x)$单调递"
    r"减，$g(x)<g(0)=0$，即有$e^{x}-1<xe^{x}$，因此",
    r"$x_{n+1}-x_{n}=\ln\dfrac{e^{x_{n}}-1}{x_{n}e^{x_{n}}}<\ln1=0$，",
    r"即数列$\{x_{n}\}$单调递减. 故由单调有界准则可知极限$\lim\limits_{n\to\infty}x_{n}$存在.",
    r"不妨设$\lim\limits_{n\to\infty}x_{n}=A$，则$Ae^{A}=e^{A}-1$.",
    r"因为$g(x)=e^{x}-1-xe^{x}$只有唯一的零点$x=0$，所以$A=0$，即",
    r"$\lim\limits_{n\to\infty}x_{n}=0$.",
])

A[20] = (r"(I)\ a\neq2:x_{1}=x_{2}=x_{3}=0;\ a=2:x=k(-2,-1,1)^{\mathrm{T}};\ "
         r"(II)\ a\neq2:y_{1}^{2}+y_{2}^{2}+y_{3}^{2};\ a=2:y_{1}^{2}+y_{2}^{2}", [
    r"【解析】（I）由$f(x_{1},x_{2},x_{3})=0$得",
    r"$\begin{cases}x_{1}-x_{2}+x_{3}=0,\\ \quad x_{2}+x_{3}=0,\\ x_{1}\quad\ \,+ax_{3}=0,\end{cases}$",
    r"系数矩阵$A=\begin{pmatrix}1&-1&1\\ 0&1&1\\ 1&0&a\end{pmatrix}\xrightarrow{r}\begin{pmatrix}1&0&2\\ 0&1&1\\ 0&0&a-2\end{pmatrix}$，",
    r"所以，当$a\neq2$时，$r(A)=3$，方程组有唯一解，$x_{1}=x_{2}=x_{3}=0$.",
    r"当$a=2$时，$r(A)=2$，方程组有无穷解，$x=k\begin{pmatrix}-2\\ -1\\ 1\end{pmatrix}$，$k$为任意常数.",
    r"（II）当$a\neq2$时，令$\begin{cases}y_{1}=x_{1}-x_{2}+x_{3},\\ y_{2}=x_{2}+x_{3},\\ y_{3}=x_{1}+ax_{3},\end{cases}$"
    r"为可逆变换，此时规范形为$y_{1}^{2}+y_{2}^{2}+y_{3}^{2}$.",
    r"当$a=2$时，$f(x_{1},x_{2},x_{3})=(x_{1}-x_{2}+x_{3})^{2}+(x_{2}+x_{3})^{2}+(x_{1}+2x_{3})^{2}$",
    r"$=2x_{1}^{2}+2x_{2}^{2}+6x_{3}^{2}-2x_{1}x_{2}+6x_{1}x_{3}$",
    r"$=2(x_{1}-\dfrac{x_{2}-3x_{3}}{2})^{2}+\dfrac{3(x_{2}+x_{3})^{2}}{2}$，",
    r"此时规范形为$y_{1}^{2}+y_{2}^{2}$.",
])

A[21] = (r"(I)\ a=2;\ (II)\ P=\begin{pmatrix}-6k_{1}+3&-6k_{2}+4&-6k_{3}+4\\ 2k_{1}-1&2k_{2}-1&2k_{3}-1\\ k_{1}&k_{2}&k_{3}\end{pmatrix},"
         r"\ k_{2}\neq k_{3}", [
    r"【解析】（I）由题设条件可知矩阵$A$与$B$等价，则$r(A)=r(B)$.",
    r"因为",
    r"$|A|=\begin{vmatrix}1&2&a\\ 1&3&0\\ 2&7&-a\end{vmatrix}\xrightarrow{r_{1}+r_{3}}\begin{vmatrix}1&2&a\\ 1&3&0\\ 3&9&0\end{vmatrix}=0$，",
    r"所以",
    r"$|B|=\begin{vmatrix}1&a&2\\ 0&1&1\\ -1&1&1\end{vmatrix}\xrightarrow{r_{3}+r_{1}}\begin{vmatrix}1&a&2\\ 0&1&1\\ 0&a+1&3\end{vmatrix}=2-a=0$，",
    r"因此",
    r"$a=2$.",
    r"（II）设矩阵$P=\begin{pmatrix}x_{11}&x_{12}&x_{13}\\ x_{21}&x_{22}&x_{23}\\ x_{31}&x_{32}&x_{33}\end{pmatrix}$，"
    r"对增广矩阵作初等变换可得，",
    r"$(A,B)=\left(\begin{array}{ccc|ccc}1&2&2&1&2&2\\ 1&3&0&0&1&1\\ 2&7&-2&-1&1&1\end{array}\right)"
    r"\to\left(\begin{array}{ccc|ccc}1&0&6&3&4&4\\ 0&1&-2&-1&-1&-1\\ 0&0&0&0&0&0\end{array}\right)$，",
    r"解得，$\begin{pmatrix}x_{11}\\ x_{21}\\ x_{31}\end{pmatrix}=\begin{pmatrix}-6k_{1}+3\\ 2k_{1}-1\\ k_{1}\end{pmatrix}$，"
    r"$\begin{pmatrix}x_{12}\\ x_{22}\\ x_{32}\end{pmatrix}=\begin{pmatrix}-6k_{2}+4\\ 2k_{2}-1\\ k_{2}\end{pmatrix}$，"
    r"$\begin{pmatrix}x_{13}\\ x_{23}\\ x_{33}\end{pmatrix}=\begin{pmatrix}-6k_{3}+4\\ 2k_{3}-1\\ k_{3}\end{pmatrix}$，",
    r"所以",
    r"$P=\begin{pmatrix}-6k_{1}+3&-6k_{2}+4&-6k_{3}+4\\ 2k_{1}-1&2k_{2}-1&2k_{3}-1\\ k_{1}&k_{2}&k_{3}\end{pmatrix}$.",
    r"又$P$可逆，因此",
    r"$|P|=\begin{vmatrix}-6k_{1}+3&-6k_{2}+4&-6k_{3}+4\\ 2k_{1}-1&2k_{2}-1&2k_{3}-1\\ k_{1}&k_{2}&k_{3}\end{vmatrix}"
    r"\xrightarrow{r_{1}+3r_{2},r_{2}-2r_{3}}\begin{vmatrix}0&1&1\\ 1&-1&-1\\ k_{1}&k_{2}&k_{3}\end{vmatrix}=k_{2}-k_{3}\neq0$，",
    r"即$k_{2}\neq k_{3}$.",
    r"故$P=\begin{pmatrix}-6k_{1}+3&-6k_{2}+4&-6k_{3}+4\\ 2k_{1}-1&2k_{2}-1&2k_{3}-1\\ k_{1}&k_{2}&k_{3}\end{pmatrix}$，"
    r"其中$k_{1},k_{2},k_{3}$为任意常数，且$k_{2}\neq k_{3}$.",
])

A[22] = (r"(I)\ \mathrm{Cov}(X,Z)=\lambda;\ (II)\ P\{Z=0\}=e^{-\lambda},\ "
         r"P\{Z=k\}=\dfrac{\lambda^{|k|}e^{-\lambda}}{2\cdot|k|!}\ (k=\pm1,\pm2,\cdots)", [
    r"【解析】（I）因为随机变量$X$的概率分布为$P\{X=1\}=P\{X=-1\}=\dfrac{1}{2}$，",
    r"所以，$E(X)=0$, $E(X^{2})=1$, $D(X)=1$.",
    r"因为，$Y$的分布律为$P\{Y=k\}=\dfrac{\lambda^{k}e^{-\lambda}}{k!}$, $k=0,1,\cdots$，",
    r"所以，$E(Y)=\lambda$.",
    r"因为，$Cov(X,Z)=Cov(X,XY)=E(X^{2}Y)-E(X)E(XY)$，且$X$与$Y$相互独立，",
    r"所以，$Cov(X,Z)=E(X^{2})E(Y)-E^{2}(X)E(Y)=D(X)E(Y)=\lambda$.",
    r"（II）利用全概率公式有，",
    r"$P\{Z=k\}=P\{XY=k\}=P\{X=1\}P\{XY=k|X=1\}+P\{X=-1\}P\{XY=k|X=-1\}$，",
    r"再由$X$与$Y$相互独立可得",
    r"$P\{Z=k\}=P\{X=1\}P\{Y=k\}+P\{X=-1\}P\{Y=-k\}$",
    r"$=\dfrac{1}{2}[P\{Y=k\}+P\{Y=-k\}]$.",
    r"当$k=0$时，$P\{Z=0\}=P\{Y=0\}=e^{-\lambda}$；",
    r"当$k$为正整数时，$P\{Z=k\}=\dfrac{1}{2}P\{Y=k\}=\dfrac{e^{-\lambda}\lambda^{k}}{2\cdot k!}$；",
    r"当$k$为负整数时，$P\{Z=k\}=\dfrac{1}{2}P\{Y=-k\}=\dfrac{e^{-\lambda}\lambda^{-k}}{2\cdot(-k)!}$.",
    r"综上所述，有$P\{Z=k\}=\begin{cases}e^{-\lambda}, & k=0,\\ \dfrac{\lambda^{|k|}e^{-\lambda}}{2\cdot|k|!}, & k=\pm1,\pm2\cdots\end{cases}$",
])

A[23] = (r"(I)\ \hat{\sigma}=\dfrac{1}{n}\sum\limits_{i=1}^{n}|X_{i}|;\ (II)\ E(\hat{\sigma})=\sigma,\ "
         r"D(\hat{\sigma})=\dfrac{\sigma^{2}}{n}", [
    r"【解析】（I）似然函数 $L(\sigma)=\prod\limits_{i=1}^{n}\dfrac{1}{2\sigma}e^{-\frac{|x_{i}|}{\sigma}}"
    r"=\dfrac{1}{2^{n}\sigma^{n}}e^{-\frac{1}{\sigma}\sum\limits_{i=1}^{n}|x_{i}|}$，",
    r"取对数：$\ln L(\sigma)=-n\ln2-n\ln\sigma-\dfrac{1}{\sigma}\sum\limits_{i=1}^{n}|x_{i}|$，",
    r"求导：$\dfrac{\mathrm{d}\ln L(\sigma)}{\mathrm{d}\sigma}=-\dfrac{n}{\sigma}+\dfrac{1}{\sigma^{2}}\sum\limits_{i=1}^{n}|x_{i}|=0$，",
    r"解得$\sigma=\dfrac{\sum\limits_{i=1}^{n}|x_{i}|}{n}$，所以$\sigma$的最大似然估计量 $\hat{\sigma}=\dfrac{\sum\limits_{i=1}^{n}|X_{i}|}{n}$.",
    r"（II）$E(\hat{\sigma})=\dfrac{1}{n}\sum\limits_{i=1}^{n}E(|X_{i}|)=E(|X|)=\int_{-\infty}^{+\infty}|x|\dfrac{1}{2\sigma}e^{-\frac{|x|}{\sigma}}\mathrm{d}x$",
    r"$=\int_{0}^{+\infty}\dfrac{x}{\sigma}e^{-\frac{x}{\sigma}}\mathrm{d}x=-\int_{0}^{+\infty}x\mathrm{d}e^{-\frac{x}{\sigma}}$",
    r"$=-xe^{-\frac{x}{\sigma}}\Big|_{0}^{+\infty}+\int_{0}^{+\infty}e^{-\frac{x}{\sigma}}\mathrm{d}x=\sigma$；",
    r"$D(\hat{\sigma})=\dfrac{1}{n^{2}}\sum\limits_{i=1}^{n}D(|X_{i}|)=\dfrac{D(|X|)}{n}=\dfrac{E(|X|^{2})-E^{2}(|X|)}{n}$",
    r"$=\dfrac{1}{n}(\int_{-\infty}^{+\infty}|x|^{2}\dfrac{1}{2\sigma}e^{-\frac{|x|}{\sigma}}\mathrm{d}x-\sigma^{2})"
    r"=\dfrac{1}{n}(\int_{0}^{+\infty}\dfrac{x^{2}}{\sigma}e^{-\frac{x}{\sigma}}\mathrm{d}x-\sigma^{2})$",
    r"$=\dfrac{1}{n}(\int_{0}^{+\infty}-x^{2}\mathrm{d}e^{-\frac{x}{\sigma}}-\sigma^{2})\ =\dfrac{1}{n}(\int_{0}^{+\infty}2xe^{-\frac{x}{\sigma}}\mathrm{d}x-\sigma^{2})=\dfrac{1}{n}(2\sigma^{2}-\sigma^{2})$",
    r"$=\dfrac{\sigma^{2}}{n}$.",
])
