# -*- coding: utf-8 -*-
"""2023 数学三 解析 第 6~7 页：题 7-10"""

A = {}

A[7] = ("D", [
    r"【答案】（D）",
    r"【解析】设 $\boldsymbol{\gamma}=k_1\boldsymbol{\alpha}_1+k_2\boldsymbol{\alpha}_2=k_3\boldsymbol{\beta}_1+k_4\boldsymbol{\beta}_2$，则 $k_1\boldsymbol{\alpha}_1+k_2\boldsymbol{\alpha}_2-k_3\boldsymbol{\beta}_1-k_4\boldsymbol{\beta}_2=\mathbf{0}$，",
    r"$(\boldsymbol{\alpha}_1,\boldsymbol{\alpha}_2,-\boldsymbol{\beta}_1,-\boldsymbol{\beta}_2)=\begin{pmatrix}1&2&-2&-1\\ 2&1&-5&0\\ 3&1&-9&-1\end{pmatrix}\xrightarrow{r}\begin{pmatrix}1&2&-2&-1\\ 0&-3&-1&2\\ 0&0&1&1\end{pmatrix}$",
    r"则 $k_3+k_4=0$，取 $k_3=k$，$k_4=-k$，则 $\boldsymbol{\gamma}=k\boldsymbol{\beta}_1-k\boldsymbol{\beta}_2=k\begin{pmatrix}1\\ 5\\ 8\end{pmatrix},\ k\in\mathbf{R}$，故选（D）。",
])

A[8] = ("C", [
    r"【答案】（C）",
    r"【解析】由 $X\sim P(1)$，故 $EX=1$。",
    r"$E\bigl(|X-EX|\bigr)=E\bigl(|X-1|\bigr)=\sum\limits_{k=0}^{\infty}|k-1|P\{X=k\}=\mathrm{e}^{-1}+\mathrm{e}^{-1}\sum\limits_{k=1}^{\infty}\dfrac{k}{(k+1)!}$",
    r"$=\mathrm{e}^{-1}+\mathrm{e}^{-1}\sum\limits_{k=1}^{\infty}\left(\dfrac{1}{k!}-\dfrac{1}{(k+1)!}\right)=\dfrac{2}{\mathrm{e}}$。",
])

A[9] = ("D", [
    r"【答案】（D）",
    r"【解析】由 $\dfrac{(n-1)S_1^{2}}{\sigma^{2}}\sim\chi^{2}(n-1),\dfrac{(m-1)S_2^{2}}{2\sigma^{2}}\sim\chi^{2}(m-1)$，且样本相互独立，故",
    r"$\dfrac{\dfrac{(n-1)S_1^{2}}{\sigma^{2}}\bigg/(n-1)}{\dfrac{(m-1)S_2^{2}}{2\sigma^{2}}\bigg/(m-1)}\sim F(n-1,m-1)$。",
    r"整理得 $\dfrac{2S_1^{2}}{S_2^{2}}\sim F\left(n-1,m-1\right)$，故选（D）。",
])

A[10] = ("A", [
    r"【答案】（A）",
    r"【解析】令 $Y=X_1-X_2$，则 $Y\sim N(0,2\sigma^{2})$。",
    r"$\sigma=E(\hat{\sigma})=aE\left|X_1-X_2\right|=aE|Y|=a\displaystyle\int_{-\infty}^{+\infty}|y|\dfrac{1}{2\sqrt{\pi}\sigma}\mathrm{e}^{-\frac{y^{2}}{4\sigma^{2}}}\mathrm{d}y=\dfrac{a}{\sqrt{\pi}\sigma}\displaystyle\int_{0}^{+\infty}y\mathrm{e}^{-\frac{y^{2}}{4\sigma^{2}}}\mathrm{d}y=\dfrac{2a}{\sqrt{\pi}}\sigma$，",
    r"得 $a=\dfrac{\sqrt{\pi}}{2}$，选（A）。",
])
