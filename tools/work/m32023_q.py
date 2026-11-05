# -*- coding: utf-8 -*-
"""2023 数学三 题干视觉转录（照录 data/math3/pages/2023/*.png）"""

ITEMS = []

def add(**kw):
    ITEMS.append(kw)

# ---------- 选择题 1-10（每题 5 分） ----------
add(num=1, type="single", score=5, pages=[1], anchor="第(1)题",
    stem=r"已知函数 $f(x,y)=\ln\left(y+\left|x\sin y\right|\right)$，则（ ）",
    options=[
        r"$\left.\dfrac{\partial f}{\partial x}\right|_{(0,1)}$不存在，$\left.\dfrac{\partial f}{\partial y}\right|_{(0,1)}$存在",
        r"$\left.\dfrac{\partial f}{\partial x}\right|_{(0,1)}$存在，$\left.\dfrac{\partial f}{\partial y}\right|_{(0,1)}$不存在",
        r"$\left.\dfrac{\partial f}{\partial x}\right|_{(0,1)}$存在，$\left.\dfrac{\partial f}{\partial y}\right|_{(0,1)}$存在",
        r"$\left.\dfrac{\partial f}{\partial x}\right|_{(0,1)}$不存在，$\left.\dfrac{\partial f}{\partial y}\right|_{(0,1)}$不存在",
    ])

add(num=2, type="single", score=5, pages=[1], anchor="第(2)题",
    stem=r"已知函数 $f(x)=\begin{cases}\dfrac{1}{\sqrt{1+x^{2}}},&x\leqslant 0,\\ (x+1)\cos x,&x>0,\end{cases}$ 的一个原函数为（ ）",
    options=[
        r"$F(x)=\begin{cases}\ln\left(\sqrt{1+x^{2}}-x\right),&x\leqslant 0,\\ (x+1)\sin x+\cos x,&x>0,\end{cases}$",
        r"$F(x)=\begin{cases}\ln\left(\sqrt{1+x^{2}}+x\right)+1,&x\leqslant 0,\\ (x+1)\sin x+\cos x,&x>0,\end{cases}$",
        r"$F(x)=\begin{cases}\ln\left(\sqrt{1+x^{2}}-x\right),&x\leqslant 0,\\ (x+1)\cos x-\sin x,&x>0,\end{cases}$",
        r"$F(x)=\begin{cases}\ln\left(\sqrt{1+x^{2}}+x\right)+1,&x\leqslant 0,\\ (x+1)\cos x-\sin x,&x>0,\end{cases}$",
    ])

add(num=3, type="single", score=5, pages=[1], anchor="第(3)题",
    stem=r"若微分方程 $y^{\prime\prime}+ay^{\prime}+by=0$ 的解在 $(-\infty,+\infty)$ 上有界，则（ ）",
    options=[
        r"$a<0,b>0$",
        r"$a>0,b>0$",
        r"$a=0,b>0$",
        r"$a=0,b<0$",
    ])

add(num=4, type="single", score=5, pages=[1], anchor="第(4)题",
    stem=r"已知数列 $\left\{a_n\right\},\left\{b_n\right\}$ 满足 $a_n<b_n\ (n=1,2,3\cdots)$，且级数 $\sum\limits_{n=1}^{+\infty}a_n$、$\sum\limits_{n=1}^{+\infty}b_n$ 都收敛，则「$\sum\limits_{n=1}^{+\infty}a_n$ 绝对收敛」是「$\sum\limits_{n=1}^{+\infty}b_n$ 绝对收敛」的（ ）",
    options=[
        r"充分必要条件",
        r"充分不必要条件",
        r"必要不充分条件",
        r"既不充分也不必要条件",
    ])

add(num=5, type="single", score=5, pages=[1], anchor="第(5)题",
    stem=r"设 $A,B$ 为 $n$ 阶矩阵，$E$ 为 $n$ 阶单位矩阵，$M^{*}$ 为 $M$ 的伴随矩阵，则 $\begin{pmatrix}A&E\\ O&B\end{pmatrix}^{*}$ 为（ ）",
    options=[
        r"$\begin{pmatrix}|A|B^{*}&-B^{*}A^{*}\\ O&|B|A^{*}\end{pmatrix}$",
        r"$\begin{pmatrix}|B|A^{*}&-A^{*}B^{*}\\ O&|A|B^{*}\end{pmatrix}$",
        r"$\begin{pmatrix}|B|A^{*}&-B^{*}A^{*}\\ O&|A|B^{*}\end{pmatrix}$",
        r"$\begin{pmatrix}|A|B^{*}&-A^{*}B^{*}\\ O&|B|A^{*}\end{pmatrix}$",
    ])

add(num=6, type="single", score=5, pages=[2], anchor="第(6)题",
    stem=r"二次型 $f(x_1,x_2,x_3)=\left(x_1+x_2\right)^{2}+\left(x_1+x_3\right)^{2}-4\left(x_2-x_3\right)^{2}$ 的规范型为（ ）",
    options=[
        r"$y_1^{2}+y_2^{2}$",
        r"$y_1^{2}-y_2^{2}$",
        r"$y_1^{2}+y_2^{2}-4y_3^{2}$",
        r"$y_1^{2}+y_2^{2}-y_3^{2}$",
    ])

add(num=7, type="single", score=5, pages=[2], anchor="第(7)题",
    stem=r"设向量组 $\boldsymbol{\alpha}_1=\begin{pmatrix}1\\ 2\\ 3\end{pmatrix},\boldsymbol{\alpha}_2=\begin{pmatrix}2\\ 1\\ 1\end{pmatrix},\boldsymbol{\beta}_1=\begin{pmatrix}2\\ 5\\ 9\end{pmatrix},\boldsymbol{\beta}_2=\begin{pmatrix}1\\ 0\\ 1\end{pmatrix}$，若 $\boldsymbol{\gamma}$ 可由 $\boldsymbol{\alpha}_1,\boldsymbol{\alpha}_2$ 表示，也可由 $\boldsymbol{\beta}_1,\boldsymbol{\beta}_2$ 表示，则 $\boldsymbol{\gamma}=$（ ）",
    options=[
        r"$k\begin{pmatrix}3\\ 3\\ 4\end{pmatrix},\ k\in\mathbf{R}$",
        r"$k\begin{pmatrix}3\\ 5\\ 10\end{pmatrix},\ k\in\mathbf{R}$",
        r"$k\begin{pmatrix}-1\\ 1\\ 2\end{pmatrix},\ k\in\mathbf{R}$",
        r"$k\begin{pmatrix}1\\ 5\\ 8\end{pmatrix},\ k\in\mathbf{R}$",
    ])

add(num=8, type="single", score=5, pages=[2], anchor="第(8)题",
    stem=r"设随机变量 $X$ 服从参数为 1 的泊松分布，则 $E\bigl(|X-EX|\bigr)=$（ ）",
    options=[
        r"$\dfrac{1}{\mathrm{e}}$",
        r"$\dfrac{1}{2}$",
        r"$\dfrac{2}{\mathrm{e}}$",
        r"$1$",
    ])

add(num=9, type="single", score=5, pages=[2], anchor="第(9)题",
    stem=r"设 $X_1,X_2,\cdots,X_n$ 为来自总体 $N(\mu_1,\sigma^{2})$ 的简单随机样本，$Y_1,Y_2,\cdots,Y_m$ 为来自总体 $N(\mu_2,2\sigma^{2})$ 的简单随机样本，且两样本相互独立，记 $\overline{X}=\dfrac{1}{n}\sum\limits_{i=1}^{n}X_i,\overline{Y}=\dfrac{1}{m}\sum\limits_{i=1}^{m}Y_i$，$S_1^{2}=\dfrac{1}{n-1}\sum\limits_{i=1}^{n}(X_i-\overline{X})^{2},S_2^{2}=\dfrac{1}{m-1}\sum\limits_{i=1}^{m}(Y_i-\overline{Y})^{2}$，则（ ）",
    options=[
        r"$\dfrac{S_1^{2}}{S_2^{2}}\sim F\left(n,m\right)$",
        r"$\dfrac{S_1^{2}}{S_2^{2}}\sim F\left(n-1,m-1\right)$",
        r"$\dfrac{2S_1^{2}}{S_2^{2}}\sim F\left(n,m\right)$",
        r"$\dfrac{2S_1^{2}}{S_2^{2}}\sim F\left(n-1,m-1\right)$",
    ])

add(num=10, type="single", score=5, pages=[2], anchor="第(10)题",
    stem=r"设 $X_1,X_2$ 是来自总体 $N(\mu,\sigma^{2})$ 的简单随机样本，其中 $\sigma(\sigma>0)$ 为未知参数，记 $\hat{\sigma}=a\left|X_1-X_2\right|$，若 $E(\hat{\sigma})=\sigma$，则 $a=$（ ）",
    options=[
        r"$\dfrac{\sqrt{\pi}}{2}$",
        r"$\dfrac{\sqrt{2\pi}}{2}$",
        r"$\sqrt{\pi}$",
        r"$\sqrt{2\pi}$",
    ])

# ---------- 填空题 11-16（每题 5 分） ----------
add(num=11, type="blank", score=5, pages=[3], anchor="第(11)题",
    stem=r"$\lim\limits_{x\to\infty}x^{2}\left(2-x\sin\dfrac{1}{x}-\cos\dfrac{1}{x}\right)=$________.")

add(num=12, type="blank", score=5, pages=[3], anchor="第(12)题",
    stem=r"已知函数 $f(x,y)$ 满足 $\mathrm{d}f(x,y)=\dfrac{x\mathrm{d}y-y\mathrm{d}x}{x^{2}+y^{2}}$，$f(1,1)=\dfrac{\pi}{4}$，则 $f(\sqrt{3},3)=$________.")

add(num=13, type="blank", score=5, pages=[3], anchor="第(13)题",
    stem=r"$\sum\limits_{n=0}^{\infty}\dfrac{x^{2n}}{(2n)!}=$________.")

add(num=14, type="blank", score=5, pages=[3], anchor="第(14)题",
    stem=r"设某公司在 $t$ 时刻的资产为 $f(t)$，从 0 到 $t$ 时刻的平均资产为 $\dfrac{f(t)}{t}-t$，其中 $f(t)$ 连续且 $f(0)=0$，则 $f(t)=$________.")

add(num=15, type="blank", score=5, pages=[3], anchor="第(15)题",
    stem=r"已知线性方程组 $\begin{cases}ax_1+x_3=1\ x_1+ax_2+x_3=0\ x_1+2x_2+ax_3=0\ ax_1+bx_2=2\end{cases}$ 有解，其中 $a,b$ 为常数，且 $\begin{vmatrix}a&0&1\ 1&a&1\ 1&2&a\end{vmatrix}=4$，则 $\begin{vmatrix}1&a&1\ 1&2&a\ a&b&0\end{vmatrix}=$________.")

add(num=16, type="blank", score=5, pages=[3], anchor="第(16)题",
    stem=r"设随机变量 $X,Y$ 相互独立，$X\sim B(1,p),Y\sim B(2,p),p\in(0,1)$，则 $X+Y$ 与 $X-Y$ 的相关系数为________.")

# ---------- 解答题 17-22（共 70 分） ----------
add(num=17, type="essay", score=10, pages=[3], anchor="第(17)题",
    stem=r"已知 $a\mathrm{e}^{x}+y^{2}+y-\ln(1+x)\cos y+b=0$，$y(0)=0,y^{\prime}(0)=0$。(1) 求 $a,b$；(2) 判断 $x=0$ 是否为极值。")

add(num=18, type="essay", score=12, pages=[3], anchor="第(18)题",
    stem=r"已知平面区域 $D=\{(x,y)\mid 0\leqslant y\leqslant\dfrac{1}{x\sqrt{1+x^{2}}},x\geqslant 1\}$。(1) 求平面区域 $D$ 的面积；(2) 求 $D$ 绕 $x$ 轴旋转一周的旋转体体积。")

add(num=19, type="essay", score=12, pages=[3, 4], anchor="第(19)题",
    stem=r"已知平面区域 $D=\left\{(x,y)\middle|(x-1)^{2}+y^{2}\leqslant 1\right\}$，求 $\iint_{D}\left|\sqrt{x^{2}+y^{2}}-1\right|\mathrm{d}x\mathrm{d}y$。")

add(num=20, type="essay", score=12, pages=[4], anchor="第(20)题",
    stem=r"设函数 $f(x)$ 在 $[-a,a]$ 上具有二阶连续导数，证明："
         r"(Ⅰ) 若 $f(0)=0$，则存在 $\xi\in(-a,a)$ 使得 $f^{\prime\prime}(\xi)=\dfrac{1}{a^{2}}\bigl[f(a)+f(-a)\bigr]$；"
         r"(Ⅱ) 若 $f(x)$ 在 $(-a,a)$ 内取得极值，则存在 $\eta\in(-a,a)$ 使得 $\left|f^{\prime\prime}(\eta)\right|\geqslant\dfrac{1}{2a^{2}}\left|f(a)-f(-a)\right|$。")

add(num=21, type="essay", score=12, pages=[4], anchor="第(21)题",
    stem=r"若矩阵 $A$ 满足对任意的 $x_1,x_2,x_3$ 均有 $A\begin{pmatrix}x_1\ x_2\ x_3\end{pmatrix}=\begin{pmatrix}x_1+x_2+x_3\ 2x_1-x_2+x_3\ x_2-x_3\end{pmatrix}$。"
         r"(1) 求矩阵 $A$；(2) 求可逆矩阵 $P$ 与对角矩阵 $\Lambda$，使得 $P^{-1}AP=\Lambda$。")

add(num=22, type="essay", score=12, pages=[4], anchor="第(22)题",
    stem=r"设随机变量 $X$ 的概率密度为 $f(x)=\dfrac{\mathrm{e}^{x}}{\left(1+\mathrm{e}^{x}\right)^{2}}$，$-\infty<x<+\infty$。令 $Y=\mathrm{e}^{X}$。"
         r"(1) 求 $X$ 的分布函数；(2) 求 $Y$ 的概率密度；(3) $Y$ 的期望是否存在。")
