# -*- coding: utf-8 -*-
"""2016 数学三 解析 解答题 15-23（原卷 p9-p14，逐字照录）"""

A = {}

A[15] = (r"e^{\frac{1}{3}}", [
    r"【解】$\lim\limits_{x\to0}\left(\cos2x+2x\sin x\right)^{\frac{1}{x^{4}}}"
    r"=\lim\limits_{x\to0}\Bigl[1+(\cos2x-1+2x\sin x)\Bigr]^{\frac{1}{x^{4}}}$",
    r"$\lim\limits_{x\to0}\dfrac{\cos2x-1+2x\sin x}{x^{4}}"
    r"=\lim\limits_{x\to0}\dfrac{\Bigl[-\dfrac{(2x)^{2}}{2!}+\dfrac{(2x)^{4}}{4!}+o(x^{4})\Bigr]+2x\Bigl[x-\dfrac{x^{3}}{3!}+o(x^{3})\Bigr]}{x^{4}}$",
    r"$=\lim\limits_{x\to0}\dfrac{\dfrac{1}{3}x^{4}+o(x^{4})}{x^{4}}=\dfrac{1}{3}$",
    r"原式 $=e^{\frac{1}{3}}$. ",
])

A[16] = (r"Q(p)=10(120-p);\ \dfrac{dR}{dQ}\Big|_{p=100}=80", [
    r"【解析】（I）由弹性公式 $\eta=\Bigl|\dfrac{p}{Q}\dfrac{dQ}{dp}\Bigr|$ 得",
    r"$\dfrac{p}{Q}\dfrac{dQ}{dp}=\dfrac{-p}{120-p}$",
    r"$-\dfrac{dQ}{Q}=\dfrac{dp}{120-p}$",
    r"$Q=C(p-120)$",
    r"$Q(0)=1200$ 得 $C=-10,$ 需求函数为 $Q(p)=-10(p-120)=10(120-p)$.",
    r"（II）收益函数为 $R=Qp=(1200-10p)p$,",
    r"边际收益函数为 $\dfrac{dR}{dQ}=\dfrac{dR}{dp}\dfrac{dp}{dQ}=(1200-20p)\Bigl(-\dfrac{1}{10}\Bigr)=2p-120$,",
    r"由此可知 $\dfrac{dR}{dQ}\Big|_{p=100}=80$，经济意义是销售第 201 件商品时，收益增加 80 万元.",
])

A[17] = (r"f'(x)=\begin{cases}-2x+4x^{2},&0<x<1\\ 2x,&x\geqslant1\end{cases};\ "
         r"f_{\min}=f\Bigl(\dfrac{1}{2}\Bigr)=\dfrac{1}{4}", [
    r"【解析】",
    r"$f(x)=\begin{cases}\displaystyle\int_{0}^{x}(x^{2}-t^{2})dt+\displaystyle\int_{x}^{1}(t^{2}-x^{2})dt,0<x<1\\ "
    r"\displaystyle\int_{0}^{1}(x^{2}-t^{2})dt,x\geqslant1\end{cases}"
    r"=\begin{cases}\dfrac{4}{3}x^{3}-x^{2}+\dfrac{1}{3},0<x<1\\ x^{2}-\dfrac{1}{3},x\geqslant1\end{cases}.$ ",
    r"$f'(x)=\begin{cases}-2x+4x^{2},0<x<1\\ 2x,x\geqslant1\end{cases}.$ ",
    r"$f(x)$ 在 $x=1$ 处连续，$\lim\limits_{x\to1^{-}}f'(x)=\lim\limits_{x\to1^{-}}(-2x+4x^{2})=2.$",
    r"则 $f'_{-}(1)=f'_{+}(1)=2$，故 $f'(1)=2.$",
    r"令 $f'(x)=0$，$4x^{2}-2x=0\ \ (0<x<1)$",
    r"$2x(2x-1)=0$，$x=\dfrac{1}{2}$",
    r"当 $0<x<\dfrac{1}{2}$，$f'(x)<0$，$f(x)\searrow$",
    r"$\dfrac{1}{2}<x<1$，$f'(x)>0$，$f(x)\nearrow$",
    r"$x>1$，$f'(x)>0$，$f(x)\nearrow$",
    r"则 $f(x)$ 在 $x=\dfrac{1}{2}$ 处取最小值，"
    r"$f\Bigl(\dfrac{1}{2}\Bigr)=\dfrac{1}{3}-\Bigl(\dfrac{1}{2}\Bigr)^{2}+\dfrac{4}{3}\Bigl(\dfrac{1}{2}\Bigr)^{3}=\dfrac{1}{4}.$",
])

A[18] = (r"f(x)=-\dfrac{e^{x}+e^{-x}}{2}", [
    r"【解析】",
    r"$\displaystyle\int_{0}^{x}f(x-t)dt\ \overset{x-t=u}{=}\ \int_{0}^{x}f(u)du$",
    r"$\displaystyle\int_{0}^{x}f(u)du=x\int_{0}^{x}f(t)dt-\int_{0}^{x}tf(t)dt+e^{-x}-1$",
    r"等式两端对 $x$ 求导得 $f(x)=\displaystyle\int_{0}^{x}f(t)dt+xf(x)-xf(x)-e^{-x}"
    r"=\displaystyle\int_{0}^{x}f(t)dt-e^{-x}$",
    r"等式两端再对 $x$ 求导得 $f'(x)=f(x)+e^{-x}$ 即",
    r"$f'(x)-f(x)=e^{-x}$,",
    r"$f(x)=e^{-\int -dx}\Bigl[\int e^{-x}e^{\int -dx}+C\Bigr]=e^{x}\Bigl(-\dfrac{1}{2}e^{-2x}+C\Bigr)$,",
    r"又 $f(0)=-1,C=-\dfrac{1}{2}$,",
    r"$f(x)=-\dfrac{1}{2}e^{x}(e^{-2x}+1)=-\dfrac{e^{x}+e^{-x}}{2}$. ",
])

A[19] = (r"[-1,1],\ S(x)=\begin{cases}x\ln\dfrac{1+x}{1-x}+\ln(1-x^{2}),&-1<x<1\\ 2\ln2,&x=\pm1\end{cases}", [
    r"【解析】",
    r"因为 $\lim\limits_{n\to\infty}\Bigl|\dfrac{u_{n+1}}{u_{n}}\Bigr|=\lim\limits_{n\to\infty}"
    r"\left|\dfrac{\dfrac{x^{2(n+1)+2}}{(n+2)(2n+3)}}{\dfrac{x^{2n+2}}{(n+1)(2n+1)}}\right|=x^{2}$",
    r"所以当 $x^{2}<1$ 时，原级数收敛；当 $x^{2}>1$ 时，原级数发散. 因此原级数的收敛区间为 $(-1,1)$. ",
    r"而 $x=\pm1$ 时，原级数变为 $\displaystyle\sum_{n=0}^{\infty}\dfrac{1}{(n+1)(2n+1)}$ 是收敛的，"
    r"原级数的收敛域为 $[-1,1]$. ",
    r"设 $S(x)=\displaystyle\sum_{n=0}^{\infty}\dfrac{x^{2n+2}}{(n+1)(2n+1)},x\in(-1,1)$，"
    r"则 $\forall x\in(-1,1)$ 有",
    r"$S'(x)=2\displaystyle\sum_{n=0}^{\infty}\dfrac{x^{2n+1}}{2n+1},S''(x)=2\displaystyle\sum_{n=0}^{\infty}x^{2n}=\dfrac{2}{1-x^{2}}$,",
    r"所以 $S'(x)=S'(0)+\displaystyle\int_{0}^{x}S''(t)dt=\displaystyle\int_{0}^{x}\dfrac{2}{1-t^{2}}dt=\ln\dfrac{1+x}{1-x}$. ",
    r"$S(x)=S(0)+\displaystyle\int_{0}^{x}S'(t)dt=\displaystyle\int_{0}^{x}\ln\dfrac{1+t}{1-t}dt$",
    r"$=t\ln\dfrac{1+t}{1-t}\Big|_{0}^{x}-\displaystyle\int_{0}^{x}td\ln\dfrac{1+t}{1-t}"
    r"=x\ln\dfrac{1+x}{1-x}-\displaystyle\int_{0}^{x}\dfrac{2t}{1-t^{2}}dt=x\ln\dfrac{1+x}{1-x}+\ln(1-x^{2})$",
    r"$x=\pm1$ 时，$\displaystyle\sum_{n=0}^{\infty}\dfrac{1}{(n+1)(2n+1)}=2\displaystyle\sum_{n=0}^{\infty}\dfrac{1}{(2n+2)(2n+1)}"
    r"=2\displaystyle\sum_{n=0}^{\infty}\Bigl(\dfrac{1}{2n+1}-\dfrac{1}{2n+2}\Bigr)$",
    r"$=2\bigl(1-\dfrac{1}{2}+\dfrac{1}{3}-\dfrac{1}{4}+...\bigr)=2\ln2$. ",
    r"故 $S(x)=\begin{cases}x\ln\dfrac{1+x}{1-x}+\ln(1-x^{2}),-1<x<1\\ 2\ln2,x=\pm1\end{cases}.$ ",
])

A[20] = (r"(I)\ a=0;\ (II)\ (1,-2,0)^{\mathrm{T}}+k(0,-1,1)^{\mathrm{T}}\ (k\ \text{为任意常数})", [
    r"【解析】对 $(A|\boldsymbol{\beta})$ 作初等行变换，有",
    r"$(A|\boldsymbol{\beta})=\begin{pmatrix}1&1&1-a&0\\ 1&0&a&1\\ a+1&1&a+1&2a-2\end{pmatrix}"
    r"\to\begin{pmatrix}1&1&1-a&0\\ 0&-1&2a-1&1\\ 0&-a&a(a+1)&2a-2\end{pmatrix}$",
    r"$\to\begin{pmatrix}1&1&1-a&0\\ 0&-1&2a-1&1\\ 0&0&a(2-a)&a-2\end{pmatrix}$",
    r"因方程组无解，故 $a=0.$",
    r"（II）对 $A^{\mathrm{T}}A\boldsymbol{x}=A^{\mathrm{T}}\boldsymbol{\beta}$，又 "
    r"$A^{\mathrm{T}}A=\begin{pmatrix}1&1&1\\ 1&0&1\\ 1&0&1\end{pmatrix}\begin{pmatrix}1&1&1\\ 1&0&0\\ 1&1&1\end{pmatrix}"
    r"=\begin{pmatrix}3&2&2\\ 2&2&2\\ 2&2&2\end{pmatrix}$,",
    r"$A^{\mathrm{T}}\boldsymbol{\beta}=\begin{pmatrix}1&1&1\\ 1&0&1\\ 1&0&1\end{pmatrix}\begin{pmatrix}0\\ 1\\ -2\end{pmatrix}"
    r"=\begin{pmatrix}-1\\ -2\\ -2\end{pmatrix}$，对 $\bigl(A^{\mathrm{T}}A\big|A^{\mathrm{T}}\boldsymbol{\beta}\bigr)$ 作初等行变换有",
    r"$\begin{pmatrix}3&2&2&-1\\ 2&2&2&-2\\ 2&2&2&-2\end{pmatrix}\to\begin{pmatrix}1&0&0&1\\ 0&1&1&-2\\ 0&0&0&0\end{pmatrix}$，"
    r"得方程组 $A^{\mathrm{T}}A\boldsymbol{x}=A^{\mathrm{T}}\boldsymbol{\beta}$ 的通解为",
    r"$(1,-2,0)^{\mathrm{T}}+k(0,-1,1)^{\mathrm{T}}$，$k$ 为任意常数.",
])

A[21] = (r"(I)\ A^{99}=\begin{pmatrix}-2+2^{99}&1-2^{99}&2-2^{98}\\ -2+2^{100}&1-2^{100}&2-2^{99}\\ 0&0&0\end{pmatrix};\ "
         r"(II)\ \boldsymbol{\beta}_{1}=(-2+2^{99})\boldsymbol{\alpha}_{1}+(-2+2^{100})\boldsymbol{\alpha}_{2};\ "
         r"\boldsymbol{\beta}_{2}=(1-2^{99})\boldsymbol{\alpha}_{1}+(1-2^{100})\boldsymbol{\alpha}_{2};\ "
         r"\boldsymbol{\beta}_{3}=(2-2^{98})\boldsymbol{\alpha}_{1}+(2-2^{99})\boldsymbol{\alpha}_{2}", [
    r"【解析】（I）由 $A$ 的特征多项式",
    r"$|\lambda E-A|=\begin{vmatrix}\lambda&1&-1\\ -2&\lambda+3&0\\ 0&0&\lambda\end{vmatrix}"
    r"=\lambda(\lambda+1)(\lambda+2)$，即 $A$ 的特征值为 $0,-1,-2.$",
    r"对 $\lambda=0$ 由 $(0E-A)\boldsymbol{x}=\boldsymbol{0}$，",
    r"$\begin{pmatrix}0&1&-1\\ -2&3&0\\ 0&0&0\end{pmatrix}$",
    r"得基础解系 $\boldsymbol{\gamma}_{1}=(3,2,2)^{\mathrm{T}}$",
    r"对 $\lambda=-1$ 由 $(-E-A)\boldsymbol{x}=\boldsymbol{0}$，",
    r"$\begin{pmatrix}1&-1&0\\ 0&0&1\\ 0&0&0\end{pmatrix}$",
    r"得基础解系 $\boldsymbol{\gamma}_{2}=(1,1,0)^{\mathrm{T}}$",
    r"对 $\lambda=-2$ 由 $(-2E-A)\boldsymbol{x}=\boldsymbol{0}$，",
    r"$\begin{pmatrix}-2&1&0\\ 0&0&1\\ 0&0&0\end{pmatrix}$",
    r"得基础解系 $\boldsymbol{\gamma}_{3}=(1,2,0)^{\mathrm{T}}$",
    r"令 $P=(\boldsymbol{\gamma}_{1},\boldsymbol{\gamma}_{2},\boldsymbol{\gamma}_{3})$ 有 "
    r"$P^{-1}AP=\Lambda=\begin{pmatrix}0&&\\ &-1&\\ &&-2\end{pmatrix}$，对于 $P$，利用初等变换可求出",
    r"$P^{-1}=\dfrac{1}{2}\begin{pmatrix}0&0&1\\ 4&-2&-4\\ -2&2&1\end{pmatrix}$,",
    r"则 $P^{-1}A^{99}P=\Lambda^{99}\Rightarrow A^{99}=P\Lambda^{99}P^{-1}"
    r"=\begin{pmatrix}3&1&1\\ 2&1&2\\ 2&0&0\end{pmatrix}\begin{pmatrix}0&&\\ &-1&\\ &&-2^{99}\end{pmatrix}"
    r"\dfrac{1}{2}\begin{pmatrix}0&0&1\\ 4&-2&-4\\ -2&2&1\end{pmatrix}$",
    r"$=\begin{pmatrix}-2+2^{99}&1-2^{99}&2-2^{98}\\ -2+2^{100}&1-2^{100}&2-2^{99}\\ 0&0&0\end{pmatrix}.$ ",
    r"（II）因 $B^{2}=BA$ 知 $B^{3}=B(BA)=B^{2}A=BA^{2}$,",
    r"归纳得",
    r"$B^{100}=BA^{99}=(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3})"
    r"\begin{pmatrix}-2+2^{99}&1-2^{99}&2-2^{98}\\ -2+2^{100}&1-2^{100}&2-2^{99}\\ 0&0&0\end{pmatrix}$,",
    r"$=\bigl((-2+2^{99})\boldsymbol{\alpha}_{1}+(-2+2^{100})\boldsymbol{\alpha}_{2},"
    r"(1-2^{99})\boldsymbol{\alpha}_{1}+(1-2^{100})\boldsymbol{\alpha}_{2},"
    r"(2-2^{98})\boldsymbol{\alpha}_{1}+(2-2^{99})\boldsymbol{\alpha}_{2}\bigr)$",
    r"$\boldsymbol{\beta}_{1}=(-2+2^{99})\boldsymbol{\alpha}_{1}+(-2+2^{100})\boldsymbol{\alpha}_{2};\ "
    r"\boldsymbol{\beta}_{2}=(1-2^{99})\boldsymbol{\alpha}_{1}+(1-2^{100})\boldsymbol{\alpha}_{2};$",
    r"$\boldsymbol{\beta}_{3}=(2-2^{98})\boldsymbol{\alpha}_{1}+(2-2^{99})\boldsymbol{\alpha}_{2}.$ ",
])

A[22] = (r"(I)\ f_{1}(x,y)=\begin{cases}3,&0<x<1,x^{2}<y<\sqrt{x}\\ 0,&\text{其他}\end{cases};\ "
         r"(II)\ U\ \text{与}\ X\ \text{不相互独立};\ (III)\ F(z)\ \text{分段见解析}", [
    r"【解析】（I）$(X,Y)$ 的概率密度可用在区域 $D$ 上均匀分布的密度公式直接写出：",
    r"$S_{D}=\displaystyle\int_{0}^{1}(\sqrt{x}-x^{2})dx=\dfrac{1}{3}$",
    r"$f_{1}(x,y)=\begin{cases}3,0<x<1,x^{2}<y<\sqrt{x}\\ 0,\text{其他}\end{cases}$",
    r"（II）由于 $U$ 是离散型随机变量，考查 $U$ 与 $X$ 是否独立，只要验证是否成立，",
    r"$P\{U=i,X\leqslant x_{1}\}=P\{U=i\}P\{X\leqslant x_{1}\},i=0,1.$ ",
    r"不妨取 $0\leqslant x_{1}\leqslant1$，则有",
    r"$P\{U=0,X\leqslant x_{1}\}=P\{X>Y,X\leqslant x_{1}\}=P\{Y<X\leqslant x_{1}\}"
    r"=\displaystyle\iint\limits_{y<x\leqslant x_{1}}f_{1}(x,y)dxdy$",
    r"$=\displaystyle\int_{0}^{x_{1}}dx\displaystyle\int_{x^{2}}^{x}3dy=\displaystyle\int_{0}^{x_{1}}3(x-x^{2})dx"
    r"=\dfrac{3}{2}x_{1}^{2}-x_{1}^{3}$,",
    r"$P\{U=0\}=P\{X>Y\}=\displaystyle\iint\limits_{x>y}f_{1}(x,y)dxdy"
    r"=\displaystyle\int_{0}^{1}dx\displaystyle\int_{x^{2}}^{x}3dy=\dfrac{1}{2}$,",
    r"$P\{X\leqslant x_{1}\}=\displaystyle\iint\limits_{x\leqslant x_{1}}f_{1}(x,y)dxdy"
    r"=\displaystyle\int_{0}^{x_{1}}dx\displaystyle\int_{x^{2}}^{\sqrt{x}}3dy=2x_{1}^{\frac{3}{2}}-x_{1}^{3}$,",
    r"所以 $P\{U=i,X\leqslant x_{1}\}\neq P\{U=i\}P\{X\leqslant x_{1}\},i=0,1.$ 即 $U$ 与 $X$ 不相互独立.",
    r"（III）$Z=U+X$ 其分布函数",
    r"$F(z)=P\{Z\leqslant z\}=P\{U+X\leqslant z\}$",
    r"$=P\{U=0,U+X\leqslant z\}+P\{U=1,U+X\leqslant z\}$",
    r"$=P\{X>Y,X\leqslant z\}+P\{X\leqslant Y,X\leqslant z-1\}$",
    r"$=\displaystyle\iint\limits_{x>y,x\leqslant z}f_{1}(x,y)dxdy+\displaystyle\iint\limits_{x\leqslant y,x\leqslant z-1}f_{1}(x,y)dxdy$",
    r"当 $z<0$ 时，$F(z)=0$;",
    r"当 $0\leqslant z<1$ 时，$F(z)=\displaystyle\iint\limits_{x>y\atop x\leqslant z}f_{1}(x,y)dxdy+0"
    r"=\displaystyle\int_{0}^{z}dx\displaystyle\int_{x^{2}}^{x}3dy=\dfrac{3}{2}z^{2}-z^{3}$;",
    r"当 $1\leqslant z<2$ 时，",
    r"$F(z)=\displaystyle\iint\limits_{x>y\atop x\leqslant z}f_{1}(x,y)dxdy+\displaystyle\iint\limits_{x\leqslant y\atop x\leqslant z-1}f_{1}(x,y)dxdy"
    r"=\displaystyle\int_{0}^{1}dx\displaystyle\int_{x^{2}}^{x}3dy+\displaystyle\int_{0}^{z-1}dx\displaystyle\int_{x}^{\sqrt{x}}3dy$",
    r"$=\dfrac{1}{2}+2(z-1)^{\frac{3}{2}}-\dfrac{3}{2}(z-1)^{2}$;",
    r"当 $z\geqslant2$ 时，$F(z)=1$. ",
])

A[23] = (r"(I)\ f_{T}(t)=\begin{cases}\dfrac{9t^{8}}{\theta^{9}},&0<t<\theta\\ 0,&\text{其他}\end{cases};\ "
         r"(II)\ a=\dfrac{10}{9}", [
    r"【解析】（I）$F(x)=\displaystyle\int_{-\infty}^{x}f(x;\theta)dx"
    r"=\begin{cases}0,&x<0\\ \dfrac{x^{3}}{\theta^{3}},&0\leqslant x<\theta\\ 1,&\theta\leqslant x\end{cases}$",
    r"$F_{T}(t)=P\{T\leqslant t\}=P\{\max(X_{1},X_{2},X_{3})\leqslant t\}"
    r"=P\{X_{1}\leqslant t,X_{2}\leqslant t,X_{3}\leqslant t\}$",
    r"由于 $X_{1},X_{2},X_{3}$ 相互独立，所以 $P\{X_{1}\leqslant t\}P\{X_{2}\leqslant t\}P\{X_{3}\leqslant t\}=F^{3}(t)$",
    r"$f_{T}(t)=F_{T}'(t)=3F_{T}^{2}(t)f(t;\theta)"
    r"=\begin{cases}3\bigl(\dfrac{t^{3}}{\theta^{3}}\bigr)^{2}\dfrac{3t^{2}}{\theta^{3}},0<t<\theta\\ 0,\text{其他}\end{cases}"
    r"=\begin{cases}\dfrac{9t^{8}}{\theta^{9}},0<t<\theta\\ 0,\text{其他}\end{cases}$",
    r"（II）$ET=\displaystyle\int_{-\infty}^{+\infty}tf_{T}(t)dt=\displaystyle\int_{0}^{\theta}\dfrac{9t^{9}}{\theta^{9}}dt"
    r"=\dfrac{9}{10}\theta,E(aT)=aET=a\cdot\dfrac{9}{10}\theta=\theta$，则 $a=\dfrac{10}{9}.$",
])
