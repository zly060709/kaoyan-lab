# -*- coding: utf-8 -*-
"""2022 数学三 解析 解答题 17-22（原卷 p11-p15，逐字照录）"""

A = {}

A[17] = ("y=2x", [
    r"【解析】$y=\mathrm{e}^{-\int\frac{1}{2\sqrt{x}}\mathrm{d}x}\left[\int\left(2+\sqrt{x}\right)\mathrm{e}^{\int\frac{1}{2\sqrt{x}}\mathrm{d}x}\mathrm{d}x+C\right]=2x+C\mathrm{e}^{-\sqrt{x}}$.",
    r"将 $y(1)=3$ 代入可得 $C=\mathrm{e}$，即 $y=2x+\mathrm{e}^{1-\sqrt{x}}\ (x>0)$.",
    r"由函数解析式可知，曲线没有垂直渐近线；",
    r"又由于 $\lim\limits_{x\to+\infty}y(x)=\lim\limits_{x\to+\infty}\left(2x+\mathrm{e}^{1-\sqrt{x}}\right)=+\infty$，",
    r"曲线没有水平渐近线；",
    r"又 $k=\lim\limits_{x\to+\infty}\dfrac{y(x)}{x}=\lim\limits_{x\to+\infty}\dfrac{2x+\mathrm{e}^{1-\sqrt{x}}}{x}=2$，",
    r"$b=\lim\limits_{x\to+\infty}\left[y(x)-kx\right]=\lim\limits_{x\to+\infty}\left(2x+\mathrm{e}^{1-\sqrt{x}}-2x\right)=0$，",
    r"故曲线有斜渐近线 $y=2x$.",
])

A[18] = ("Q=384", [
    r"【解析】由题意得利润函数 $L=pQ-6x-8y=(1160-1.5Q)Q-6x-8y$，化简得",
    r"$L=13920x^{\frac{1}{2}}y^{\frac{1}{6}}-216xy^{\frac{1}{3}}-6x-8y$.",
    r"由 $L$ 分别对 $x$ 和 $y$ 求偏导并令其为零：",
    r"$\begin{cases}\dfrac{\partial L}{\partial x}=6960x^{-\frac{1}{2}}y^{\frac{1}{6}}-216y^{\frac{1}{3}}-6=0\\[4pt] "
    r"\dfrac{\partial L}{\partial y}=2320x^{\frac{1}{2}}y^{-\frac{5}{6}}-72xy^{-\frac{2}{3}}-8=0\end{cases}$",
    r"解得 $\begin{cases}x=256\\ y=64\end{cases}$",
    r"此时利润最大，利润最大时的产量 $Q=384$.",
])

A[19] = (r"2\pi-2", [
    r"【解析】令 $D_1=\left\{(r,\theta)\mid 0\leq r\leq2,0\leq\theta\leq\dfrac{\pi}{2}\right\}$，",
    r"$D_2=\left\{(r,\theta)\mid 0\leq r\leq\dfrac{2}{\sin\theta-\cos\theta},\dfrac{\pi}{2}\leq\theta\leq\pi\right\}$，",
    r"$I=\displaystyle\iint_{D_1}\dfrac{(x-y)^{2}}{x^{2}+y^{2}}\mathrm{d}x\mathrm{d}y"
    r"+\displaystyle\iint_{D_2}\dfrac{(x-y)^{2}}{x^{2}+y^{2}}\mathrm{d}x\mathrm{d}y$",
    r"$=\displaystyle\int_{0}^{\frac{\pi}{2}}\mathrm{d}\theta\int_{0}^{2}(\cos\theta-\sin\theta)^{2}r\mathrm{d}r"
    r"+\displaystyle\int_{\frac{\pi}{2}}^{\pi}\mathrm{d}\theta\int_{0}^{\frac{2}{\sin\theta-\cos\theta}}(\cos\theta-\sin\theta)^{2}r\mathrm{d}r$",
    r"$=2\displaystyle\int_{0}^{\frac{\pi}{2}}(1-2\sin\theta\cos\theta)\mathrm{d}\theta"
    r"+\displaystyle\int_{\frac{\pi}{2}}^{\pi}2\mathrm{d}\theta=2\pi-2$",
])

A[20] = (r"[-1,1],\ S(x)=\dfrac{\arctan x}{x}+\dfrac{1}{x}\ln\left(\dfrac{2+x}{2-x}\right)\ (x\neq0),\ S(0)=2", [
    r"【解析】(1) 设 $u_n(x)=\dfrac{(-4)^{n}+1}{4^{n}(2n+1)}x^{2n}$，$\lim\limits_{n\to\infty}\left|\dfrac{u_{n+1}(x)}{u_n(x)}\right|<1$，",
    r"则 $x\in(-1,1)$，收敛区间为 $(-1,1)$，",
    r"当 $x=\pm1$，$\sum\limits_{n=0}^{\infty}\dfrac{(-4)^{n}+1}{4^{n}(2n+1)}"
    r"=\sum\limits_{n=0}^{\infty}\dfrac{(-1)^{n}}{(2n+1)}+\sum\limits_{n=0}^{\infty}\dfrac{1}{4^{n}(2n+1)}$ 收敛，则收敛域为 $[-1,1]$ (II)",
    r"$\sum\limits_{n=0}^{\infty}\dfrac{(-4)^{n}+1}{4^{n}(2n+1)}x^{2n}"
    r"=\sum\limits_{n=0}^{\infty}\dfrac{(-1)^{n}}{(2n+1)}x^{2n}+\sum\limits_{n=0}^{\infty}\dfrac{1}{4^{n}(2n+1)}x^{2n}$ 记",
    r"$S_1(x)=\sum\limits_{n=0}^{\infty}\dfrac{(-1)^{n}}{(2n+1)}x^{2n},\ "
    r"S_2(x)=\sum\limits_{n=0}^{\infty}\dfrac{1}{4^{n}(2n+1)}x^{2n}$，",
    r"关于 $S_1(x)$，当 $x=0$ 时，$S_1(x)=1$.",
    r"当 $x\neq0$ 时，$S_1(x)=\dfrac{1}{x}\sum\limits_{n=0}^{\infty}\dfrac{(-1)^{n}}{(2n+1)}x^{2n+1}$，",
    r"记 $S_3(x)=\sum\limits_{n=0}^{\infty}\dfrac{(-1)^{n}}{(2n+1)}x^{2n+1}$，",
    r"则 $S_3^{\prime}(x)=\sum\limits_{n=0}^{\infty}(-1)^{n}x^{2n}=\dfrac{1}{1+x^{2}}$，"
    r"$S_3(x)=\displaystyle\int_{0}^{x}\dfrac{1}{1+t^{2}}\mathrm{d}t+S_3(0)=\arctan x$.",
    r"$S_1(x)=\begin{cases}\dfrac{\arctan x}{x},&x\in[-1,0)\cup(0,1].\\ 1,&x=0.\end{cases}$",
    r"关于 $S_2(x)$，当 $x=0$ 时，$S_2(x)=1$.",
    r"当 $x\neq0$ 时，$S_2(x)=\dfrac{2}{x}\sum\limits_{n=0}^{\infty}\dfrac{1}{2n+1}\left(\dfrac{x}{2}\right)^{2n+1}$，",
    r"记 $S_4(x)=\sum\limits_{n=0}^{\infty}\dfrac{1}{2n+1}\left(\dfrac{x}{2}\right)^{2n+1}$，",
    r"则 $S_4^{\prime}(x)=\dfrac{1}{2}\sum\limits_{n=0}^{\infty}\left(\dfrac{x}{2}\right)^{2n}=\dfrac{2}{4-x^{2}}$，"
    r"$S_4(x)=\displaystyle\int_{0}^{x}\dfrac{2}{4-t^{2}}\mathrm{d}t+S_4(0)=\dfrac{1}{2}\ln\left|\dfrac{2+x}{2-x}\right|$",
    r"$S_2(x)=\begin{cases}\dfrac{1}{x}\ln\left(\dfrac{2+x}{2-x}\right),&x\in[-1,0)\cup(0,1].\\ 1,&x=0.\end{cases}$",
    r"则 $S(x)=\begin{cases}\dfrac{\arctan x}{x}+\dfrac{1}{x}\ln\left(\dfrac{2+x}{2-x}\right),"
    r"&x\in[-1,0)\cup(0,1].\\ 2,&x=0.\end{cases}$",
])

A[21] = (r"f=4y_1^{2}+4y_2^{2}+2y_3^{2},\ \min\limits_{x\neq0}\dfrac{f(x)}{x^{\mathrm{T}}x}=2", [
    r"【解析】(1) $f\left(x_1,x_2,x_3\right)=3x_1^{2}+4x_2^{2}+3x_3^{2}+2x_1x_3$，",
    r"二次型矩阵为 $A=\begin{pmatrix}3&0&1\\ 0&4&0\\ 1&0&3\end{pmatrix}$，则特征方程为",
    r"$|\lambda E-A|=\begin{vmatrix}\lambda-3&0&-1\\ 0&\lambda-4&0\\ -1&0&\lambda-3\end{vmatrix}=(\lambda-4)^{2}(\lambda-2)$",
    r"得特征值 $\lambda_1=\lambda_2=4,\lambda_3=2$.",
    r"当 $\lambda_1=\lambda_2=4$ 时，$(4E-A)x=0$ 得 $\xi_1=(0,1,0)^{\mathrm{T}},\xi_2=(1,0,1)^{\mathrm{T}}$",
    r"当 $\lambda_3=2$ 时，$(2E-A)x=0$ 得 $\xi_3=(1,0,-1)^{\mathrm{T}}$.",
    r"将 $\xi_1=(0,1,0)^{\mathrm{T}},\xi_2=(1,0,1)^{\mathrm{T}},\xi_3=(1,0,-1)^{\mathrm{T}}$ 正交单位化得",
    r"$\eta_1=(0,1,0)^{\mathrm{T}},\eta_2=\dfrac{1}{\sqrt{2}}(1,0,1)^{\mathrm{T}},"
    r"\eta_3=\dfrac{1}{\sqrt{2}}(1,0,-1)^{\mathrm{T}}$ 可得 "
    r"$Q=\begin{pmatrix}0&\dfrac{1}{\sqrt{2}}&\dfrac{1}{\sqrt{2}}\\ 1&0&0\\ "
    r"0&\dfrac{1}{\sqrt{2}}&-\dfrac{1}{\sqrt{2}}\end{pmatrix}$，即",
    r"$\begin{cases}x_1=\dfrac{1}{\sqrt{2}}y_2+\dfrac{1}{\sqrt{2}}y_3\\ x_2=y_1\\ "
    r"x_3=\dfrac{1}{\sqrt{2}}y_2-\dfrac{1}{\sqrt{2}}y_3\end{cases}$",
    r"$f(x)=4y_1^{2}+4y_2^{2}+2y_3^{2}$",
    r"(II) 由 (I) 知 $f(x)=4y_1^{2}+4y_2^{2}+2y_3^{2}$，$x=Qy$，故 "
    r"$x^{\mathrm{T}}x=y^{\mathrm{T}}Q^{\mathrm{T}}Qy=y^{\mathrm{T}}y$",
    r"故 $\dfrac{f(x)}{x^{\mathrm{T}}x}=\dfrac{g(y)}{y^{\mathrm{T}}y}"
    r"=\dfrac{4y_1^{2}+4y_2^{2}+2y_3^{2}}{y_1^{2}+y_2^{2}+y_3^{2}}"
    r"=2+\dfrac{2y_1^{2}+2y_2^{2}}{y_1^{2}+y_2^{2}+y_3^{2}}\geqslant2$",
    r"当 $y_1=y_2=0,y_3\neq0$ 时，可取到最小值 2.",
    r"所以存在非零向量 $\boldsymbol{y}$，即存在非零向量 $\boldsymbol{x}$，使得 $\dfrac{f(x)}{x^{\mathrm{T}}x}$ 取到最小值 2.得证.",
])

A[22] = (r"\hat{\theta}=\dfrac{1}{n+m}\left(\sum\limits_{i=1}^{n}X_i+\dfrac{1}{2}\sum\limits_{j=1}^{m}Y_j\right),"
         r"\ D\hat{\theta}=\dfrac{\theta^{2}}{n+m}", [
    r"【解析】(1) 由题意得，$\lambda_x=\dfrac{1}{\theta}$，$\lambda_y=\dfrac{1}{2\theta}$，",
    r"则 $f_X(x)=\begin{cases}\dfrac{1}{\theta}\mathrm{e}^{-\frac{1}{\theta}x}&x>0\\ 0&\text{其它}\end{cases},\ "
    r"f_Y(y)=\begin{cases}\dfrac{1}{2\theta}\mathrm{e}^{-\frac{1}{2\theta}y}&y>0\\ 0&\text{其它}\end{cases}$",
    r"设 $x_1,x_2,\cdots,x_n,y_1,y_2,\cdots,y_m$ 为 $X_1,X_2,\cdots,X_n,Y_1,Y_2,\cdots,Y_m$ 的样本观察值，则",
    r"$L(\theta)=\displaystyle\prod_{i=1}^{n}f_X(x_i)\prod_{j=1}^{m}f_Y(y_j)$",
    r"当 $x_i>0,y_j>0$ 时，",
    r"$L(\theta)=\left(\dfrac{1}{\theta}\right)^{n}\mathrm{e}^{-\frac{1}{\theta}\sum\limits_{i=1}^{n}x_i}"
    r"\left(\dfrac{1}{2\theta}\right)^{m}\mathrm{e}^{-\frac{1}{2\theta}\sum\limits_{j=1}^{m}y_j}"
    r"=2^{-m}\theta^{-(n+m)}\mathrm{e}^{-\frac{1}{\theta}\sum\limits_{i=1}^{n}x_i}"
    r"\mathrm{e}^{-\frac{1}{2\theta}\sum\limits_{j=1}^{m}y_j}$",
    r"$LnL(\theta)=-m\ln2-(n+m)\ln\theta-\dfrac{1}{\theta}\sum\limits_{i=1}^{n}x_i"
    r"-\dfrac{1}{2\theta}\sum\limits_{j=1}^{m}y_j$",
    r"令 $\dfrac{\mathrm{d}LnL(\theta)}{\mathrm{d}\theta}=-\dfrac{n+m}{\theta}"
    r"+\dfrac{1}{\theta^{2}}\sum\limits_{i=1}^{n}X_i+\dfrac{1}{2\theta^{2}}\sum\limits_{j=1}^{m}Y_j=0$，",
    r"得 $\theta$ 的最大似然估计量为 "
    r"$\hat{\theta}=\dfrac{1}{n+m}\left(\sum\limits_{i=1}^{n}X_i+\dfrac{1}{2}\sum\limits_{j=1}^{m}Y_j\right)$.",
    r"(II) $D(\hat{\theta})=D\left[\dfrac{1}{n+m}\left(\sum\limits_{i=1}^{n}X_i"
    r"+\dfrac{1}{2}\sum\limits_{j=1}^{m}Y_j\right)\right]$",
    r"$=\dfrac{1}{(n+m)^{2}}\left[nD(X_i)+\dfrac{1}{4}mD(Y_j)\right]$",
    r"$=\dfrac{1}{(n+m)^{2}}\left(n\theta^{2}+\dfrac{1}{4}m4\theta^{2}\right)=\dfrac{1}{n+m}\theta^{2}$",
])
