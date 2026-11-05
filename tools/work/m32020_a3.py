# -*- coding: utf-8 -*-
"""2020 数学三 解析 解答题 15-23（原卷 p8-p13，逐字照录）"""

A = {}

A[15] = (r"a=1,\ b=-\dfrac{1}{2}e", [
    r"（15）【答案】$a=1,b=-\dfrac{1}{2}e$",
    r"【解析】$\lim\limits_{n\to\infty}\dfrac{\left(1+\dfrac{1}{n}\right)^{n}-e}{\dfrac{b}{n^{a}}}"
    r"=\dfrac{1}{b}\lim\limits_{n\to\infty}\dfrac{e^{n\ln\left(1+\frac{1}{n}\right)}-e}{\dfrac{1}{n^{a}}}"
    r"=\dfrac{e}{b}\lim\limits_{n\to\infty}\dfrac{e^{n\ln\left(1+\frac{1}{n}\right)-1}-1}{\dfrac{1}{n^{a}}}$",
    r"$=\dfrac{e}{b}\lim\limits_{n\to\infty}\dfrac{n\ln(1+\dfrac{1}{n})-1}{\dfrac{1}{n^{a}}}"
    r"=\dfrac{e}{b}\lim\limits_{n\to\infty}\dfrac{n\left(\ln(1+\dfrac{1}{n})-\dfrac{1}{n}\right)}{\dfrac{1}{n^{a}}}$",
    r"由于 $\ln(1+\dfrac{1}{n})-\dfrac{1}{n}\sim\dfrac{1}{2}\dfrac{1}{n^{2}}\left(n\to\infty\right)$，则 $a=1$，"
    r"且①式 $\dfrac{-\dfrac{1}{2}e}{b}=1$，得 $b=-\dfrac{1}{2}e.$",
])

A[16] = (r"极小值 $-\dfrac{1}{216}$", [
    r"（16）【答案】极小值为 $f=\left(\dfrac{1}{6},\dfrac{1}{12}\right)=-\dfrac{1}{216}$",
    r"【解析】$\begin{cases}f_{x}'\left(x,y\right)=3x^{2}-y=0\\ f_{y}'\left(x,y\right)=24y^{2}-x=0\end{cases}$",
    r"所以 $\begin{cases}x=0\\ y=0\end{cases}$ 或 $\begin{cases}x=\dfrac{1}{6}\\ y=\dfrac{1}{12}\end{cases}$"
    r"，所以驻点为 $\left(0,0\right)$ 或 $\left(\dfrac{1}{6},\dfrac{1}{12}\right).$",
    r"$A=f_{xx}''\left(x,y\right)=6x$，$B=f_{xy}''\left(x,y\right)=-1$，$C=f_{yy}''\left(x,y\right)=48y$"
    r" 代入 $\left(0,0\right)$，此时 $AC-B^{2}<0$ 所以不是极值点，代入 $\left(\dfrac{1}{6},\dfrac{1}{12}\right)$，"
    r"$AC-B^{2}>0$ 且 $A>0$，所以 $\left(\dfrac{1}{6},\dfrac{1}{12}\right)$ 是极小值点，"
    r"$f=\left(\dfrac{1}{6},\dfrac{1}{12}\right)=-\dfrac{1}{216}$ 为极小值.",
])

A[17] = (r"(1)\ f(x)=e^{-x}\cos 2x;\ (2)\ \sum\limits_{n=1}^{\infty}a_{n}=\dfrac{1}{5}\dfrac{1}{e^{\pi}-1}", [
    r"（17）【答案】（I）$f(x)=e^{-x}\cos 2x$ （II）$\sum\limits_{n=1}^{\infty}a_{n}=\dfrac{1}{5}\sum\limits_{n=1}^{\infty}e^{-n\pi}=\dfrac{1}{5}\dfrac{1}{e^{\pi}-1}$",
    r"【解析】（I）由 $y''+2y'+5y=0$ 得 $\lambda^{2}+2\lambda+5=0$，解得 $\lambda_{1,2}=-1\pm 2i$，",
    r"则 $f(x)=e^{-x}\left(C_{1}\cos 2x+C_{2}\sin 2x\right)$，又由 $f(0)=1,f'(0)=-1$ 得 $C_{1}=1,C_{2}=0$，",
    r"则 $f(x)=e^{-x}\cos 2x.$",
    r"（II）$a_{n}=\int_{n\pi}^{+\infty}e^{-x}\cos 2xdx=\dfrac{1}{5}\left(-e^{-x}\cos 2x+2e^{-x}\sin 2x\right)\Big|_{n\pi}^{+\infty}$",
    r"$=\dfrac{1}{5}e^{-x}\left(-\cos 2x+2\sin 2x\right)\Big|_{n\pi}^{+\infty}=\dfrac{1}{5}e^{-n\pi}$，"
    r"则 $\sum\limits_{n=1}^{\infty}a_{n}=\dfrac{1}{5}\sum\limits_{n=1}^{\infty}e^{-n\pi}=\dfrac{1}{5}\dfrac{1}{e^{\pi}-1}.$",
])

A[18] = (r"\dfrac{3\pi^{2}}{128}", [
    r"（18）【答案】$\dfrac{3\pi^{2}}{128}$",
    r"【解析】设 $\iint_{D}f(x,y)dxdy=A$，则 $f(x,y)=y\sqrt{1-x^{2}}+Ax$，",
    r"两边同取积分得 $A=\iint_{D}f(x,y)dxdy=\iint_{D}y\sqrt{1-x^{2}}dxdy+\iint_{D}Axdxdy$",
    r"$=\iint_{D}y\sqrt{1-x^{2}}dxdy=2\iint_{D_{1}}y\sqrt{1-x^{2}}dxdy"
    r"=2\int_{0}^{1}\sqrt{1-x^{2}}dx\int_{0}^{\sqrt{1-x^{2}}}ydy$",
    r"$=\int_{0}^{1}\left(1-x^{2}\right)^{\frac{3}{2}}dx\xlongequal{x=\sin t}\int_{0}^{\frac{\pi}{2}}\cos^{4}tdt"
    r"=\dfrac{3}{4}\dfrac{1}{2}\dfrac{\pi}{2}=\dfrac{3\pi}{16}.$",
    r"则 $f(x,y)=f(x,y)+\dfrac{3\pi}{16}x$，$\iint_{D}xf(x,y)dxdy=\iint_{D}x\left(y\sqrt{1-x^{2}}+\dfrac{3\pi}{16}x\right)dxdy$",
    r"$=\dfrac{3\pi}{16}\cdot\iint_{D}x^{2}dxdy=\dfrac{3\pi}{16}\cdot 2\iint_{D_{1}}x^{2}dxdy"
    r"=\dfrac{3\pi}{16}\cdot 2\cdot\dfrac{1}{2}\iint_{D_{1}}\left(x^{2}+y^{2}\right)dxdy$",
    r"$=\dfrac{3\pi}{16}\int_{0}^{\frac{\pi}{2}}d\theta\int_{0}^{1}r^{2}rdr=\dfrac{3\pi}{16}\cdot\dfrac{\pi}{2}\cdot\dfrac{1}{4}=\dfrac{3\pi^{2}}{128}.$",
])

A[19] = ("证明见解析", [
    r"（19）【解析】（I）证明：（I）$M=0$ 时，则 $f(x)=0$，显然成立.",
    r"$M>0$ 时，不妨设在点 $c(\in(0,2))$ 处取得最大值 $\left|f(c)\right|=M.$",
    r"由拉格朗日中值定理得，存在 $\xi_{1}\in(0,c)$，使得 $\left|f'(\xi_{1})\right|=\left|\dfrac{f(c)-f(0)}{c-0}\right|=\dfrac{M}{c}$；",
    r"存在 $\xi_{2}\in(c,2)$，使得 $\left|f'(\xi_{2})\right|=\left|\dfrac{f(2)-f(c)}{2-c}\right|=\dfrac{M}{2-c}$；",
    r"所以 $\left(\dfrac{M}{c}-M\right)\left(\dfrac{M}{2-c}-M\right)=-M^{2}\dfrac{\left(c-1\right)^{2}}{c\left(2-c\right)}\leqslant 0$，"
    r"即 $M$ 介于 $\dfrac{M}{c}$ 与 $\dfrac{M}{2-c}$ 之间，",
    r"从而有 $\left|f'(\xi_{1})\right|\geqslant M$ 或 $\left|f'(\xi_{2})\right|\geqslant M$，结论得证.",
    r"（II）当 $c\neq 1$ 时，采用反证法，假设 $M>0$.",
    r"则 $\left|f'(\xi_{1})\right|>M$ 或 $\left|f'(\xi_{2})\right|>M$，与已知矛盾，假设不成立.",
    r"当 $c=1$ 时，此时 $\left|f(1)\right|=M$，易知 $f'(1)=0$.",
    r"不妨设 $f(1)=M$，则 $G(x)=f(x)-Mx,0\leqslant x\leqslant 1$；则有 $G'(x)=f'(x)-M\leqslant 0$，从而 $G(x)$ 单调递减.",
    r"又 $G(0)=G(1)=0$，从而 $G(x)=0$，即 $f(x)=Mx,0\leqslant x\leqslant 1.$",
    r"因此 $f^{\prime}_{-}(1)=M$，从而 $M=0$。综上所述，$M=0$.",
])

A[20] = (r"(1)\ a=4,b=1;\ (2)\ Q=\begin{pmatrix}\dfrac{4}{5}&-\dfrac{3}{5}\\ -\dfrac{3}{5}&-\dfrac{4}{5}\end{pmatrix}", [
    r"（20）【解析】（I）设 $f=x^{T}Ax$，其中 $A=\begin{pmatrix}1&-2\\ -2&4\end{pmatrix}$，经正交变换 $x=Qy$，",
    r"$f=y^{T}Q^{T}AQy=y^{T}By$，其中 $B=\begin{pmatrix}a&2\\ 2&b\end{pmatrix}$；",
    r"可知 $Q^{T}AQ=Q^{-1}AQ=B$，即 $A$ 相似于 $B$，则 $\begin{cases}tr(A)=tr(B)\\ \left|A\right|=\left|B\right|\end{cases}$"
    r" 解得 $a=4,b=1$ ；",
    r"（II）设 $P_{1}^{-1}AP_{1}=\Lambda,P_{2}^{-1}BP_{2}=\Lambda$，则 $\left(P_{1}P_{2}^{-1}\right)^{-1}A\left(P_{1}P_{2}^{-1}\right)=B$，"
    r"因此 $Q=P_{1}P_{2}^{-1}$；",
    r"由 $\left|\lambdaE-A\right|=\begin{vmatrix}\lambda-1&2\\ 2&\lambda-4\end{vmatrix}=0$，解出 $\lambda_{1}=0,\lambda_{2}=5$；",
    r"$\left(0E-A\right)=\begin{pmatrix}-1&2\\ 2&-4\end{pmatrix}\rightarrow\begin{pmatrix}1&-2\\ 0&0\end{pmatrix}$，故 $\xi_{1}=\left(2,1\right)^{T}$；",
    r"$\left(5E-A\right)=\begin{pmatrix}4&2\\ 2&1\end{pmatrix}\rightarrow\begin{pmatrix}2&1\\ 0&0\end{pmatrix}$，"
    r"故 $\xi_{2}=\left(1,-2\right)^{T}$；故 $P_{1}=\dfrac{1}{\sqrt{5}}\begin{pmatrix}2&1\\ 1&-2\end{pmatrix}$；",
    r"$\left(0E-B\right)=\begin{pmatrix}-4&-2\\ -2&-1\end{pmatrix}\rightarrow\begin{pmatrix}2&1\\ 0&0\end{pmatrix}$，故 $\eta_{1}=\left(1,-2\right)^{T}$；",
    r"$\left(5E-B\right)=\begin{pmatrix}1&-2\\ -2&4\end{pmatrix}\rightarrow\begin{pmatrix}1&-2\\ 0&0\end{pmatrix}$，"
    r"故 $\eta_{2}=\left(2,1\right)^{T}$；$P_{2}=\dfrac{1}{\sqrt{5}}\begin{pmatrix}1&2\\ -2&1\end{pmatrix}$；",
    r"综上所述，$Q=P_{1}P_{2}^{-1}=\begin{pmatrix}\dfrac{4}{5}&-\dfrac{3}{5}\\ -\dfrac{3}{5}&-\dfrac{4}{5}\end{pmatrix}.$",
])

A[21] = (r"(1)\ 证明见解析;\ (2)\ P^{-1}AP=\begin{pmatrix}0&6\\ 1&-1\end{pmatrix}$，$A$ 可以相似对角化", [
    r"（21）【解析】（I）$\alpha$ 不是特征向量且 $\alpha\neq 0$，则 $A\alpha\neq k\alpha$，即 $A\alpha,\alpha$ 线性无关，"
    r"故 $P=\left(\alpha,A\alpha\right)$ 可逆.",
    r"（II）设 $P^{-1}AP=B$，则 $AP=PB$，即",
    r"$A(\alpha,A\alpha)=\left(A\alpha,A^{2}\alpha\right)=\left(A\alpha,6\alpha-A\alpha\right)="
    r"\left(\alpha,A\alpha\right)\begin{pmatrix}0&6\\ 1&-1\end{pmatrix}$",
    r"所以 $P^{-1}AP=B=\begin{pmatrix}0&6\\ 1&-1\end{pmatrix}$，则 $A\sim B$，",
    r"$\left|\lambdaE-B\right|=\begin{vmatrix}\lambda&-6\\ -1&\lambda+1\end{vmatrix}=\left(\lambda+3\right)\left(\lambda-2\right)=0$",
    r"$\lambda_{1}=-3,\lambda_{2}=2$，因为 $\lambda_{1}\neq\lambda_{2}$，所以 $B$ 可以相似对角化，则 $A$ 可以相似对角化.",
])

A[22] = (r"(1)\ 分布律见解析;\ (2)\ \rho=\dfrac{1}{3}", [
    r"（22）【解析】由题意 $f\left(x,y\right)=\begin{cases}\dfrac{2}{\pi},\left(x,y\right)\in D\\ 0,\left(x,y\right)\notin D\end{cases}$，所以可计算",
    r"$P\left(Z_{1}=0,Z_{2}=0\right)=P\left(X-Y\leq 0,X+Y\leq 0\right)=\dfrac{1}{4}$；",
    r"$P\left(Z_{1}=0,Z_{2}=1\right)=P\left(X-Y\leq 0,X+Y>0\right)=\dfrac{1}{2}$；",
    r"$P\left(Z_{1}=1,Z_{2}=0\right)=P\left(X-Y>0,X+Y\leq 0\right)=0$；",
    r"$P\left(Z_{1}=1,Z_{2}=1\right)=P\left(X-Y>0,X+Y>0\right)=\dfrac{1}{4}.$",
    r"可得 $\begin{array}{|c|c|c|}\hline Z_{1}\backslash Z_{2}&0&1\\ \hline 0&\dfrac{1}{4}&\dfrac{1}{2}\\ \hline 1&0&\dfrac{1}{4}\\ \hline\end{array}$",
    r"由（1）可计算 $E\left(Z_{1}\right)=\dfrac{1}{4},E\left(Z_{2}\right)=\dfrac{3}{4},D\left(Z_{1}\right)=\dfrac{3}{16},"
    r"D\left(Z_{2}\right)=\dfrac{3}{16},E\left(Z_{1}Z_{2}\right)=\dfrac{1}{4}.$",
    r"所以可得 $\rho=\dfrac{Cov\left(Z_{1},Z_{2}\right)}{\sqrt{DZ_{1}}\sqrt{DZ_{2}}}"
    r"=\dfrac{E\left(Z_{1}Z_{2}\right)-EZ_{1}\cdot EZ_{2}}{\sqrt{DZ_{1}}\sqrt{DZ_{2}}}=\dfrac{1}{3}.$",
])

A[23] = (r"(1)\ P\left\{T>t\right\}=e^{-\left(\frac{t}{\theta}\right)^{m}},\ P\left\{T>s+t\mid T>s\right\}=e^{\left(\frac{s}{\theta}\right)^{m}-\left(\frac{s+t}{\theta}\right)^{m}};\ (2)\ \hat{\theta}=\sqrt[m]{\dfrac{1}{n}\sum\limits_{i=1}^{n}t_{i}^{m}}", [
    r"（23）【解析】（I）$P\left\{T>t\right\}=1-P\left\{T\leq t\right\}=1-F\left(t\right)=e^{-\left(\frac{t}{\theta}\right)^{m}}$，",
    r"$P\left\{T>t+s\mid T>s\right\}=\dfrac{P\left\{T>t+s,T>s\right\}}{P\left\{T>s\right\}}"
    r"=\dfrac{e^{-\left(\frac{s+t}{\theta}\right)^{m}}}{e^{-\left(\frac{s}{\theta}\right)^{m}}}"
    r"=e^{\left(\frac{s}{\theta}\right)^{m}-\left(\frac{s+t}{\theta}\right)^{m}}$；",
    r"（II）求得密度函数 $f\left(t\right)=\begin{cases}\dfrac{mt^{m-1}}{\theta^{m}}e^{-\left(\frac{t}{\theta}\right)^{m}},&t\geq 0\\ 0,&t<0\end{cases}$，",
    r"故可构造似然函数为 $L\left(\theta\right)=\dfrac{m^{n}\prod\limits_{i=1}^{n}t_{i}^{m-1}}{\theta^{mn}}"
    r"e^{-\sum\limits_{i=1}^{n}\left(\frac{t_{i}}{\theta}\right)^{m}},\quad t_{i}>0,i=1,2,3,...,n,$",
    r"取对数 $\ln L\left(\theta\right)=n\ln m+\left(m-1\right)\ln\left(t_{1}t_{2}\cdots t_{n}\right)-mn\ln\theta-\dfrac{1}{\theta^{m}}\sum\limits_{i=1}^{n}t_{i}^{m}$",
    r"求导可得 $\dfrac{d\ln L\left(\theta\right)}{d\theta}=-\dfrac{mn}{\theta}+m\dfrac{1}{\theta^{m+1}}\sum\limits_{i=1}^{n}t_{i}^{m}=0,$",
    r"解出 $\theta$ 的极大似然估计为 $\hat{\theta}=\sqrt[m]{\dfrac{1}{n}\sum\limits_{i=1}^{n}t_{i}^{m}}$ .",
])
