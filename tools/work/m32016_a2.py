# -*- coding: utf-8 -*-
"""2016 数学三 解析 填空题 9-14（原卷 p7-p8，逐字照录）"""

A = {}

A[9] = ("6", [
    r"【答案】$6$.",
    r"【解析】$\lim\limits_{x\to0}\dfrac{\sqrt{1+f(x)\sin2x}-1}{e^{3x}-1}"
    r"=\lim\limits_{x\to0}\dfrac{\dfrac{1}{2}f(x)\sin2x}{3x}=\dfrac{1}{3}\lim\limits_{x\to0}f(x)=2$",
    r"则 $\lim\limits_{x\to0}f(x)=6.$",
])

A[10] = (r"\sin1-\cos1", [
    r"【答案】$\sin1-\cos1$",
    r"【解析】$\lim\limits_{n\to\infty}\dfrac{1}{n^{2}}\Bigl(\sin\dfrac{1}{n}+2\sin\dfrac{2}{n}+\cdots+n\sin\dfrac{n}{n}\Bigr)$",
    r"$=\lim\limits_{n\to\infty}\dfrac{1}{n}\Bigl[\dfrac{1}{n}\sin\dfrac{1}{n}+\dfrac{2}{n}\sin\dfrac{2}{n}+\cdots+\dfrac{n}{n}\sin\dfrac{n}{n}\Bigr]$",
    r"$=\lim\limits_{n\to\infty}\dfrac{1}{n}\displaystyle\sum_{i=1}^{\infty}\dfrac{i}{n}\sin\dfrac{i}{n}=\displaystyle\int_{0}^{1}x\sin xdx$",
    r"$=-x\cos x\Big|_{0}^{1}+\displaystyle\int_{0}^{1}\cos xdx=\sin1-\cos1$",
])

A[11] = (r"-dx+2dy", [
    r"【答案】$-dx+2dy.$",
    r"【解析】易得 $x=0,y=1$ 时 $z=1$，方程两边求全微分",
    r"$zdx+(x+1)dz-2ydy=2xfdx+x^{2}\bigl[f_{1}'(dx-dz)+f_{2}'dy\bigr]$",
    r"把 $x=0,y=1,z=1$ 代入上式有 $dz\big|_{(0,1)}=-dx+2dy$",
])

A[12] = (r"\dfrac{1}{3}(1-2e^{-1})", [
    r"【答案】$\dfrac{1}{3}(1-2e^{-1})$.",
    r"【解析】利用二重积分的对称性",
    r"$\displaystyle\iint\limits_{D}x^{2}e^{-y^{2}}dxdy=2\displaystyle\iint\limits_{D_{右}}x^{2}e^{-y^{2}}dxdy"
    r"=2\displaystyle\int_{0}^{1}e^{-y^{2}}dy\displaystyle\int_{0}^{y}x^{2}dx=\dfrac{2}{3}\displaystyle\int_{0}^{1}y^{3}e^{-y^{2}}dy$",
    r"$=-\dfrac{1}{3}\displaystyle\int_{0}^{1}y^{2}de^{-y^{2}}=-\dfrac{1}{3}\Bigl(y^{2}e^{-y^{2}}\Big|_{0}^{1}-2\displaystyle\int_{0}^{1}ye^{-y^{2}}dy\Bigr)$",
    r"$=-\dfrac{1}{3}\Bigl(e^{-1}+e^{-y^{2}}\Big|_{0}^{1}\Bigr)=\dfrac{1}{3}(1-2e^{-1})$",
])

A[13] = (r"\lambda^{4}+\lambda^{3}+2\lambda^{2}+3\lambda+4", [
    r"【答案】$\lambda^{4}+\lambda^{3}+2\lambda^{2}+3\lambda+4.$",
    r"【解析】按第 $1$ 列展开",
    r"$D=\lambda\begin{vmatrix}\lambda&-1&0\\ 0&\lambda&-1\\ 3&2&\lambda+1\end{vmatrix}"
    r"+4(-1)^{4+1}\begin{vmatrix}-1&0&0\\ \lambda&-1&0\\ 0&\lambda&-1\end{vmatrix}$",
    r"$=\lambda\Bigl(\lambda\begin{vmatrix}\lambda&-1\\ 2&\lambda+1\end{vmatrix}+3\cdot(-1)^{3+1}\begin{vmatrix}-1&0\\ \lambda&-1\end{vmatrix}\Bigr)+4$",
    r"$=\lambda^{4}+\lambda^{3}+2\lambda^{2}+3\lambda+4$",
])

A[14] = (r"\dfrac{2}{9}", [
    r"【答案】$\dfrac{2}{9}.$",
    r"【解析】本题为古典概型，用概率公式 $P(A)=\dfrac{m}{n}$",
    r"$n$ 计算：恰好取 4 次停止，每次取球有 3 种不同颜色，又是有放回的，所以总的情况 $n=3^{4}.$",
    r"$m$ 计算：先考虑第 4 次的颜色，这颜色一定与前 3 次的不同. 前 3 次必定已有且仅有 2 种不",
    r"同颜色，这样第 4 次抽到第 3 色才凑够 3 种颜色，总之第 4 次有 3 种可能，前 3 次由其余 2 种",
    r"颜色构成，其总数为每次有 2 种可能，3 次有 $2^{3}=8$ 种可能，扣除 3 次同一色共 2 种，所以",
    r"前 3 次由两种不同颜色构成共有 $8-2=6$ 种可能，所有 $m=3\cdot6=18.$ 故 $P(A)=\dfrac{18}{3^{4}}=\dfrac{2}{9}.$",
])
