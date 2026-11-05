# -*- coding: utf-8 -*-
"""2012 数学三 解析 解答题 15-23（原卷 p8-p13，逐字照录）"""

A = {}

A[15] = (r"\dfrac{1}{12}", [
    r"15【详解】",
    r"$\lim\limits_{x\to0}\dfrac{e^{x^{2}}-e^{2-2\cos x}}{x^{4}}"
    r"=\lim\limits_{x\to0}\dfrac{e^{2-2\cos x}\left(e^{x^{2}-\left(2-2\cos x\right)}-1\right)}{x^{4}}"
    r"=\lim\limits_{x\to0}\dfrac{e^{x^{2}-\left(2-2\cos x\right)}-1}{x^{4}}"
    r"=\lim\limits_{x\to0}\dfrac{x^{2}-\left(2-2\cos x\right)}{x^{4}}$",
    r"$=\lim\limits_{x\to0}\dfrac{x^{2}-\left(2-2\cos x\right)}{x^{4}}"
    r"=\lim\limits_{x\to0}\dfrac{x^{2}-2+2\left(1-\dfrac{x^{2}}{2!}+\dfrac{x^{4}}{4!}+o\left(x^{4}\right)\right)}{x^{4}}"
    r"=\dfrac{1}{12}.$",
])

A[16] = (r"\dfrac{1}{2}", [
    r"16【详解】由已知，$\iint\limits_{D}e^{x}xydxdy=\int_{0}^{1}dx\int_{\sqrt{x}}^{\frac{1}{\sqrt{x}}}xe^{x}ydy=\dfrac{1}{2}.$",
])

A[17] = (r"C\left(x,y\right)=10000+20x+\dfrac{1}{4}x^{2}+6y+\dfrac{1}{2}y^{2};"
         r"\ x=24,y=26 时总成本最小，$C=11118$（万元）；甲的边际成本为 $32$", [
    r"17.【详解】（1）根据题意，有$\dfrac{\partial C\left(x,y\right)}{\partial x}=20+\dfrac{x}{2},"
    r"\dfrac{\partial C\left(x,y\right)}{\partial y}=6+y.$",
    r"$C\left(x,y\right)=10000+20x+\dfrac{1}{4}x^{2}+6y+\dfrac{1}{2}y^{2}.$",
    r"（2）设",
    r"$F(x,y)=C\left(x,y\right)+\lambda(x+y-50)=10000+20x+\dfrac{1}{4}x^{2}+6y+\dfrac{1}{2}y^{2}"
    r"+\lambda(x+y-50)$",
    r"两边分别对 $x,y,\lambda$ 求导得",
    r"$\begin{cases}\dfrac{\partial F}{\partial x}=20+\dfrac{1}{2}x+\lambda=0\\ "
    r"\dfrac{\partial F}{\partial y}=6+y+\lambda=0\\ "
    r"\dfrac{\partial F}{\partial\lambda}=x+y-50=0\end{cases}$",
    r"解上述方程组得 $F(x,y)$ 的唯一驻点",
    r"$\begin{cases}x=24\\ y=26\\ \lambda=-32\end{cases}$",
    r"所以当 $x=24,y=26$ 时可使总成本最小，此时",
    r"$C\left(x,y\right)=10000+20\times24+\dfrac{1}{4}\times24^{2}+6\times26+\dfrac{1}{2}\times26^{2}"
    r"=11118$（万元）",
    r"（3）当 $x=24$ 时，总产量为50件且总成本最小，此时甲的边际成本为",
    r"$20+\dfrac{1}{2}\times24=32.$",
    r"经济意义是：当生产乙产品26件时，生产第25件甲产品需32万元.",
])

A[18] = ("证明见解析", [
    r"18.【证明】令 $f\left(x\right)=x\ln\dfrac{1+x}{1-x}+\cos x-1-\dfrac{x^{2}}{2}$，则 $f\left(0\right)=0.$",
    r"$f\left(x\right)$为偶函数，我们只需证明$0<x<1$ , $f\left(x\right)=x\ln\dfrac{1+x}{1-x}+\cos x-1-\dfrac{x^{2}}{2}>0$",
    r"$f^{\prime}\left(x\right)=\ln\dfrac{1+x}{1-x}+x\left(\dfrac{1}{1+x}+\dfrac{1}{1-x}\right)-\sin x-x$",
    r"$f^{\prime\prime}\left(x\right)=2\left(\dfrac{1}{1+x}+\dfrac{1}{1-x}\right)"
    r"+x\left(-\dfrac{1}{\left(1+x\right)^{2}}+\dfrac{1}{\left(1-x\right)^{2}}\right)-\cos x-1$",
    r"$=\dfrac{4}{1-x^{2}}+\dfrac{4x^{2}}{\left(1+x\right)^{2}\left(1-x\right)^{2}}-\cos x-1$",
    r"由 $0<x<1$ 可得，$\dfrac{4}{1-x^{2}}>4$，$\dfrac{4x^{2}}{\left(1+x\right)^{2}\left(1-x\right)^{2}}>0$，"
    r"$-2<-\cos x-1<-1$；所以当$0<x<1$，",
    r"$f^{\prime\prime}\left(x\right)>0$.因此，当$0<x<1$时 $f^{\prime}\left(x\right)$ 单调递增.而 $f^{\prime}\left(0\right)=0$，"
    r"所以 $f^{\prime}\left(x\right)>f^{\prime}\left(0\right)=0.$",
    r"得出 $f\left(x\right)$为增函数，又由 $f\left(0\right)=0$，得出 当$0<x<1$，",
    r"$f\left(x\right)=x\ln\dfrac{1+x}{1-x}+\cos x-1-\dfrac{x^{2}}{2}>0$，"
    r"即 $x\ln\dfrac{1+x}{1-x}+\cos x>1+\dfrac{x^{2}}{2}.$",
])

A[19] = (r"(1)\ f(x)=e^{x};\ (2)\ \left(0,0\right)", [
    r"19.【详解】（1）解二阶齐次微分方程及一阶线性微分方程组",
    r"$\begin{cases}f''\left(x\right)+f'\left(x\right)-2f(x)=0\\ f''\left(x\right)+f\left(x\right)=2e^{x}\end{cases}$",
    r"首先解得 $f''\left(x\right)+f'\left(x\right)-2f(x)=0$ 的通解为： $f\left(x\right)=c_{1}e^{x}+c_{2}e^{-2x}$，代入到",
    r"$f''\left(x\right)+f\left(x\right)=2e^{x}$ 中，即可解得： $c_{1}=1,c_{2}=0$，故 $f\left(x\right)=e^{x}.$",
    r"（2）由 $f\left(x\right)=e^{x}$ 可得",
    r"$y=f\left(x^{2}\right)\displaystyle\int_{0}^{x}f\left(-t^{2}\right)dt=e^{x^{2}}\displaystyle\int_{0}^{x}e^{-t^{2}}dt$",
    r"$y^{\prime}=2xe^{x^{2}}\displaystyle\int_{0}^{x}e^{-t^{2}}dt+e^{x^{2}}e^{-x^{2}}"
    r"=2xe^{x^{2}}\displaystyle\int_{0}^{x}e^{-t^{2}}dt+1$",
    r"$y^{\prime\prime}=2e^{x^{2}}\left(1+2x^{2}\right)\displaystyle\int_{0}^{x}e^{-t^{2}}dt+2x$",
    r"当 $x=0$ 时，二阶导数等于零，且 $x<0$ 时，二阶导数小于0， $x>0$ 时，二阶导数大于0，",
    r"所以 $\left(0,0\right)$ 点为其拐点.",
])

A[20] = (r"(1)\ |A|=1-a^{4};\ (2)\ a=1$ 时无解，$a=-1$ 时通解 "
         r"$\left(0,-1,0,0\right)^{T}+k\left(1,1,1,1\right)^{T}$", [
    r"20. 【详解】（1）按照第一列展开，得$\left|A\right|=1+\left(-1\right)^{5}a^{4}=1-a^{4}.$",
    r"（2）若 $Ax=\beta$ 有无穷多解，则$\left|A\right|=0$，即$1-a^{4}=0$，解得$a=1$或$a=-1$.",
    r"当 $a=1$ 时，",
    r"$\overline{A}=\begin{pmatrix}1&1&0&0&1\\ 0&1&1&0&-1\\ 0&0&1&1&0\\ 1&0&0&1&0\end{pmatrix}"
    r"\rightarrow\begin{pmatrix}1&1&0&0&1\\ 0&1&1&0&-1\\ 0&0&1&1&0\\ 0&0&0&0&-2\end{pmatrix}$",
    r"$r\left(A\right)<r\left(\overline{A}\right)$，方程组 $Ax=\beta$ 无解.",
    r"当 $a=-1$ 时，",
    r"$\overline{A}=\begin{pmatrix}1&-1&0&0&1\\ 0&1&-1&0&-1\\ 0&0&1&-1&0\\ -1&0&0&1&0\end{pmatrix}"
    r"\rightarrow\begin{pmatrix}1&-1&0&0&1\\ 0&1&-1&0&-1\\ 0&0&1&-1&0\\ 0&0&0&0&0\end{pmatrix}$",
    r"方程组 $Ax=\beta$ 有无穷多解，其通解为",
    r"$\begin{pmatrix}0\\ -1\\ 0\\ 0\end{pmatrix}+k\begin{pmatrix}1\\ 1\\ 1\\ 1\end{pmatrix}$，其中 $k$ 为任意常数.",
])

A[21] = (r"(1)\ a=-1;\ (2)\ f\left(x_{1},x_{2},x_{3}\right)=2y_{1}^{2}+6y_{2}^{2}", [
    r"（21）【详解】（1） 对 $A$ 初等行变换，",
    r"$A=\begin{pmatrix}1&0&1\\ 0&1&1\\ -1&0&a\\ 0&a&-1\end{pmatrix}"
    r"\rightarrow\begin{pmatrix}1&0&1\\ 0&1&1\\ 0&0&a+1\\ 0&0&0\end{pmatrix}$",
    r"由 $r\left(A\right)=r\left(A^{T}A\right)=2$, 得 $a=-1$.",
    r"（2）",
    r"$A^{T}A=\begin{pmatrix}1&1&-1&-1\\ 0&1&0&-1\\ 1&0&-1&0\end{pmatrix}"
    r"\begin{pmatrix}1&0&1\\ 0&1&1\\ -1&0&-1\\ 0&-1&-1\end{pmatrix}="
    r"\begin{pmatrix}2&0&2\\ 0&2&2\\ 2&2&4\end{pmatrix}$",
    r"由 $A^{T}A$ 的特征多项式",
    r"$\left|\lambda E-A^{T}A\right|=\begin{vmatrix}\lambda-2&0&-2\\ 0&\lambda-2&-2\\ -2&-2&\lambda-4\end{vmatrix}"
    r"=\begin{vmatrix}\lambda-2&0&-2\\ -\left(\lambda-2\right)&\lambda-2&-2\\ 0&-2&\lambda-4\end{vmatrix}$",
    r"$=\left(\lambda-2\right)\begin{vmatrix}1&0&-2\\ -1&\lambda-2&-2\\ 0&-2&\lambda-4\end{vmatrix}"
    r"=\left(\lambda-2\right)\begin{vmatrix}1&0&-2\\ 0&\lambda-2&-4\\ 0&-2&\lambda-4\end{vmatrix}"
    r"=\lambda(\lambda-2)(\lambda-6)$",
    r"得矩阵 $A^{T}A$ 的特征值 $\lambda_{1}=2$， $\lambda_{2}=6$， $\lambda_{3}=0$.",
    r"当 $\lambda_{1}=2$ 时，解得$\left(2E-A^{T}A\right)x=0$ 的基础解系 $\alpha_{1}=\left(1,-1,0\right)^{T}$；",
    r"当 $\lambda_{2}=6$ 时，解得$\left(6E-A^{T}A\right)x=0$ 的基础解系 $\alpha_{2}=\left(1,1,2\right)^{T}$；",
    r"当 $\lambda_{3}=0$ 时，解得$\left(0E-A^{T}A\right)x=0$ 的基础解系 $\alpha_{3}=\left(1,1,-1\right)^{T}$；",
    r"由于 $\alpha_{1},\alpha_{2},\alpha_{3}$ 已是正交向量组，只需单位化，",
    r"$\gamma_{1}=\dfrac{1}{\sqrt{2}}\begin{pmatrix}1\\ -1\\ 0\end{pmatrix},"
    r"\gamma_{2}=\dfrac{1}{\sqrt{6}}\begin{pmatrix}1\\ 1\\ 2\end{pmatrix},"
    r"\gamma_{3}=\dfrac{1}{\sqrt{3}}\begin{pmatrix}1\\ 1\\ -1\end{pmatrix}$",
    r"令 $Q=\left(\gamma_{1},\gamma_{2},\gamma_{3}\right)$，经过正交变换 $x=Qy$，"
    r"二次型 $f\left(x_{1},x_{2},x_{3}\right)=x^{T}\left(A^{T}A\right)x$ 化成标",
    r"准形 $f\left(x_{1},x_{2},x_{3}\right)=2y_{1}^{2}+6y_{2}^{2}.$",
])

A[22] = (r"(1)\ P\{X=2Y\}=\dfrac{1}{4};\ (2)\ DX=\dfrac{5}{9},\ DY=\dfrac{2}{3},"
         r"\ \mathrm{cov}\left(X-Y,Y\right)=-\dfrac{2}{3}", [
    r"(22)【详解】由联合概率分布可知：",
    r"$P\{X=0,Y=0\}=\dfrac{1}{4},\ \ P\{X=2,Y=1\}=0$",
    r"$\Rightarrow P(X=2Y)=P(X=0,Y=0)+P(X=2,Y=1)=\dfrac{1}{4}+0=\dfrac{1}{4}$",
    r"(2)由$X$与$Y$的联合概率分布可知：",
    r"随机变量$X,Y$以及$XY$ 的分布律如下表所示：",
    r"$\begin{array}{|c|c|c|c|}\hline X & 0 & 1 & 2\\ \hline P & \dfrac{1}{2} & \dfrac{1}{3} & \dfrac{1}{6}\\ \hline \end{array}$",
    r"$\begin{array}{|c|c|c|c|}\hline Y & 0 & 1 & 2\\ \hline P & \dfrac{1}{3} & \dfrac{1}{3} & \dfrac{1}{3}\\ \hline \end{array}$",
    r"$\begin{array}{|c|c|c|c|c|}\hline XY & 0 & 1 & 2 & 4\\ \hline "
    r"P & \dfrac{7}{12} & \dfrac{1}{3} & 0 & \dfrac{1}{12}\\ \hline \end{array}$",
    r"所以",
    r"$EX=0\times\dfrac{1}{2}+1\times\dfrac{1}{3}+2\times\dfrac{1}{6}=\dfrac{2}{3};"
    r"\ EX^{2}=0^{2}\times\dfrac{1}{2}+1^{2}\times\dfrac{1}{3}+2^{2}\times\dfrac{1}{6}=1$",
    r"$EY=0\times\dfrac{1}{3}+1\times\dfrac{1}{3}+2\times\dfrac{1}{3}=1;"
    r"\ \ EY^{2}=0^{2}\times\dfrac{1}{3}+1^{2}\times\dfrac{1}{3}+2^{2}\times\dfrac{1}{3}=\dfrac{5}{3}$",
    r"$EXY=0\times\dfrac{7}{12}+1\times\dfrac{1}{3}+2\times0+4\times\dfrac{1}{12}=\dfrac{2}{3}$",
    r"则$DX=EX^{2}-\left(EX\right)^{2}=1-(\dfrac{2}{3})^{2}=\dfrac{5}{9},"
    r"DY=EY^{2}-\left(EY\right)^{2}=\dfrac{5}{3}-1^{2}=\dfrac{2}{3}$",
    r"$\mathrm{cov}(X-Y,Y)=\mathrm{cov}(X,Y)-\mathrm{cov}(Y,Y)$",
    r"$=\left(EXY-EX\cdot EY\right)-\left(EY^{2}-EY\cdot EY\right)$",
    r"$=(\dfrac{2}{3}-\dfrac{2}{3}\times1)-(\dfrac{5}{3}-1\times1)$",
    r"$=-\dfrac{2}{3}$",
])

A[23] = (r"(1)\ f_{Z}(z)=\begin{cases}2e^{-2v},&v>0\\ 0,&v\leq0\end{cases};\ (2)\ E(U+V)=2", [
    r"23.【详解】由已知条件知，随机变量$X$ 和$Y$ 的概率密度分别为：",
    r"$f_{X}\left(x\right)=\begin{cases}e^{-x},x\geq 0\\ 0,\ \text{其他}\end{cases}"
    r"\ \ \ \ f_{Y}\left(y\right)=\begin{cases}e^{-y},y\geq 0\\ 0,\ \text{其他}\end{cases}$",
    r"因为随机变量$X$ 和$Y$ 相互独立，所以$X$ 和$Y$ 的联合概率密度为",
    r"$f(x,y)=\begin{cases}e^{-(x+y)},x\geq0,y\geq0\\ 0,\ \text{其他}\end{cases}$",
    r"（利用分布函数法求随机变量$V$ 的概率密度）",
    r"随机变量$V$ 的分布函数为：",
    r"$F_{V}\left(v\right)=P\left\{V\leq v\right\}=P\left\{\min(X,Y)\leq v\right\}"
    r"=1-P\left\{\min(X,Y)>v\right\}=1-P\left\{X>v,Y>v\right\}$",
    r"① $v\leq0$时，$F_{V}\left(v\right)=1-P\left\{X>v,Y>v\right\}"
    r"=1-\displaystyle\int_{0}^{+\infty}\int_{0}^{+\infty}e^{-(x+y)}dxdy=1-1=0$",
    r"$v>0$时，$F_{V}\left(v\right)=1-P\left\{X>v,Y>v\right\}"
    r"=1-\displaystyle\int_{v}^{+\infty}\int_{v}^{+\infty}e^{-(x+y)}dxdy"
    r"=1-\displaystyle\int_{v}^{+\infty}e^{-x}dx\displaystyle\int_{v}^{+\infty}e^{-y}dy$",
    r"$=1-e^{-2v}$",
    r"所以随机变量$V$ 的概率函数为：",
    r"$f_{z}(z)=F_{Z}^{\prime}(z)=\begin{cases}2e^{-2v},v>0\\ 0,\ \ \ v\leq0\end{cases}$",
    r"（2）因为$U+V=\max(X,Y)+\min(X,Y)=X+Y$",
    r"又因为$X$ 和$Y$ 相互独立，所以$E(U+V)=E(X+Y)=E(X)+E(Y)=2.$",
])
