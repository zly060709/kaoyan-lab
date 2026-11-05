# -*- coding: utf-8 -*-
"""2018 数学三 解析 选择题 1-8（原卷 p5-p7，逐字照录）"""

A = {}

A[1] = ("D", [
    r"【答案】（D）",
    r"【解析】选项（A）和（C），函数$|x|\sin|x|=x\sin x$，$\cos|x|=\cos x$，可导；",
    r"(B)选项，$f'(0)=\lim\limits_{x\to0}\dfrac{f(x)-f(0)}{x-0}=\lim\limits_{x\to0}\dfrac{|x|\sin\sqrt{|x|}}{x}"
    r"=\lim\limits_{x\to0}\dfrac{|x|\cdot\sqrt{|x|}}{x}=\lim\limits_{x\to0}\dfrac{|x|^{\frac{3}{2}}}{x}=0$，可导；",
    r"对于（D）选项，由定义得$f_{+}'(0)=\lim\limits_{x\to0^{+}}\dfrac{\cos\sqrt{|x|}-1}{x}"
    r"=\lim\limits_{x\to0^{+}}\dfrac{-\dfrac{1}{2}|x|}{x}=-\dfrac{1}{2}$；",
    r"$f_{-}'(0)=\lim\limits_{x\to0^{-}}\dfrac{\cos\sqrt{|x|}-1}{x}"
    r"=\lim\limits_{x\to0^{-}}\dfrac{-\dfrac{1}{2}|x|}{x}=\dfrac{1}{2}$.",
    r"因为$f_{+}'(0)\neq f_{-}'(0)$，所以不可导. 故选（D）",
])

A[2] = ("D", [
    r"【答案】（D）",
    r"【解析】由条件可知对函数$f(x)$在$x=\dfrac{1}{2}$点处二阶泰勒展开可得，",
    r"$f(x)=f\left(\dfrac{1}{2}\right)+f'\left(\dfrac{1}{2}\right)\left(x-\dfrac{1}{2}\right)+\dfrac{f''(\xi)}{2!}\left(x-\dfrac{1}{2}\right)^{2}$，"
    r"其中$\xi$在$x$与$\dfrac{1}{2}$之间，",
    r"则$\int_{0}^{1}f(x)\mathrm{d}x=\int_{0}^{1}\bigl[f\left(\dfrac{1}{2}\right)+f'\left(\dfrac{1}{2}\right)\left(x-\dfrac{1}{2}\right)+\dfrac{f''(\xi)}{2!}\left(x-\dfrac{1}{2}\right)^{2}\bigr]\mathrm{d}x$",
    r"$=f\left(\dfrac{1}{2}\right)+\dfrac{f''(\xi)}{2!}\int_{0}^{1}\left(x-\dfrac{1}{2}\right)^{2}\mathrm{d}x=0$，",
    r"其中积分$\int_{0}^{1}\left(x-\dfrac{1}{2}\right)\mathrm{d}x=\int_{0}^{1}x\mathrm{d}x-\dfrac{1}{2}=0$.",
    r"所以当$f''(x)>0$时，积分$\dfrac{f''(\xi)}{2!}\int_{0}^{1}\left(x-\dfrac{1}{2}\right)^{2}\mathrm{d}x>0$，"
    r"从而$f\left(\dfrac{1}{2}\right)<0$；",
    r"当$f''(x)<0$，有$f\left(\dfrac{1}{2}\right)>0$，选项B错误；取$f(x)=-x+\dfrac{1}{2}$，$f'(x)<0$, "
    r"$f\left(\dfrac{1}{2}\right)=0$，选项A错误；取$f(x)=x-\dfrac{1}{2}$，$f'(x)>0$, $f\left(\dfrac{1}{2}\right)=0$，"
    r"选项（C）错误. 故选（D）",
])

A[3] = ("C", [
    r"【答案】（C）",
    r"【解析】因为$M=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\dfrac{1+x^{2}+2x}{1+x^{2}}\mathrm{d}x"
    r"=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}(1+\dfrac{2x}{1+x^{2}})\mathrm{d}x=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}1\mathrm{d}x$，"
    r"$1\leqslant1+\sqrt{\cos x}$，",
    r"所以，$K>M$. 设$f(x)=e^{x}-x-1$，则$f'(x)=e^{x}-1$，所以当$x<0$时，$f'(x)<0$，$f(x)$"
    r"单调递减；当$x\geqslant0$时，$f'(x)\geqslant0$，$f(x)$单调递增，故$f(0)=0$是其最小值，"
    r"即$\dfrac{x+1}{e^{x}}\leqslant1$.",
    r"所以$M>N$，即$N<M<K$，故选（C）",
])

A[4] = ("D", [
    r"【答案】（D）",
    r"【解析】平均成本函数$\overline{C}(Q)=\dfrac{C(Q)}{Q}$，则$\overline{C}'(Q)=\dfrac{C'(Q)Q-C(Q)}{Q^{2}}$.",
    r"由题设产量为$Q_{0}$时平均成本最小，所以$\overline{C}'(Q_{0})=\dfrac{C'(Q_{0})Q_{0}-C(Q_{0})}{Q_{0}^{2}}=0$，",
    r"即$C'(Q_{0})Q_{0}=C(Q_{0})$. 故选（D）",
])

A[5] = ("A", [
    r"【答案】（A）",
    r"【解析】记矩阵$M=\begin{pmatrix}1&1&0\\ 0&1&1\\ 0&0&1\end{pmatrix}$，"
    r"则$|\lambda E-M|=\begin{vmatrix}\lambda-1&-1&0\\ 0&\lambda-1&-1\\ 0&0&\lambda-1\end{vmatrix}=(\lambda-1)^{3}=0$，",
    r"所以特征值为$\lambda_{1}=\lambda_{2}=\lambda_{3}=1$，且$r(\lambda E-M)=r(E-M)=2$；",
    r"对于（A）选项：记矩阵为$A$，解得特征值均为1，且$r(\lambda E-A)=r(E-A)=2$；",
    r"同理对于（B）（C）（D）选项：分别记矩阵为$B,C,D$，计算可得其特征值均为1，而",
    r"$r(E-B)=r(E-C)=r(E-D)=1$.",
    r"若矩阵$T,N$相似，则对应的矩阵$\lambda E-T$和$\lambda E-N$也相似，故秩相等. 由此可以排除选项"
    r"（B）（C）（D），故选（A）",
])

A[6] = ("A", [
    r"【答案】（A）",
    r"【解析】选项（A），易知$r(A\ AB)\geqslant r(A)$.由分块矩阵的乘法，可知$(A\ AB)=A(E\ B)$，",
    r"因此",
    r"$r(A\ AB)\leqslant\min\{r(A),\ r(E\ B)\}$，",
    r"从而",
    r"$r(A\ AB)\leqslant r(A)$，",
    r"所以",
    r"$r(A\ AB)=r(A)$，",
    r"则选项（A）正确.",
    r"（B）选项，令$A=\begin{pmatrix}1&0\\ 0&0\end{pmatrix}$，$B=\begin{pmatrix}0&1\\ 1&0\end{pmatrix}$，"
    r"则$r(A)=1$, $r(A\ BA)=2$；",
    r"（C）选项，令$A=\begin{pmatrix}1&0\\ 0&0\end{pmatrix}$，$B=\begin{pmatrix}0&0\\ 0&1\end{pmatrix}$，"
    r"则$r(A)=r(B)=1$, $r(A\ B)=2$；",
    r"（D）选项，令$A=\begin{pmatrix}1&0\\ 0&0\end{pmatrix}$，$B=\begin{pmatrix}0&1\\ 0&0\end{pmatrix}$，"
    r"则$r(A\ B)=1$, $r(A^{\mathrm{T}}\ B^{\mathrm{T}})=2$；",
    r"故选（A）",
])

A[7] = ("A", [
    r"【答案】（A）",
    r"【解析】因为$f(1+x)=f(1-x)$，所以$f(x)$的图像关于$x=1$对称，因此",
    r"$P\{X<0\}=P\{X>2\}$.",
    r"因为$\int_{0}^{2}f(x)\mathrm{d}x=0.6$，所以$P\{X<0\}+P\{X>2\}=2P\{X<0\}=1-0.6=0.4$，",
    r"从而$P\{X<0\}=0.2$，故选（A）",
])

A[8] = ("B", [
    r"【答案】（B）",
    r"【解析】根据单个正态总体的分布的性质可知",
    r"$\overline{X}\sim N(\mu,\dfrac{\sigma^{2}}{n})$，$\dfrac{\overline{X}-\mu}{\sigma/\sqrt{n}}\sim N(0,1)$，"
    r"$\dfrac{(n-1)S^{2}}{\sigma^{2}}\sim\chi^{2}(n-1)$，",
    r"且$\overline{X}$与$S^{2}$独立，所以"
    r"$\dfrac{\dfrac{\overline{X}-\mu}{\sigma/\sqrt{n}}}{\sqrt{\dfrac{(n-1)S^{2}}{\sigma^{2}}\cdot\dfrac{1}{n-1}}}\sim t(n-1)$，"
    r"即$\dfrac{\sqrt{n}(\overline{X}-\mu)}{S}\sim t(n-1)$. 故选（B）",
])
