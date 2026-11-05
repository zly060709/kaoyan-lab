# -*- coding: utf-8 -*-
"""2023 数学二 答案解析（视觉转录自 p11-p12）。本文件：第 (21) 题（证明题）。"""

A = {}

A[21] = ("证明见解析", [
    r"(1) 由泰勒公式可知 $\begin{cases}f(a)=f(0)+f'(0)a+\dfrac{f''(\xi_{1})}{2}a^{2},\ \xi_{1}\in(0,a),\\ f(-a)=f(0)-f'(0)a+\dfrac{f''(\xi_{2})}{2}a^{2},\ \xi_{2}\in(-a,0),\end{cases}$",
    r"两式相加得 $f(a)+f(-a)=\dfrac{f''(\xi_{1})+f''(\xi_{2})}{2}a^{2}$，",
    r"再由平均值定理可知存在 $\xi\in(-a,a)$ 使得 $f''(\xi)=\dfrac{f''(\xi_{1})+f''(\xi_{2})}{2}$，",
    r"即存在 $\xi\in(-a,a)$ 使得 $f''(\xi)=\dfrac{1}{a^{2}}[f(a)+f(-a)]$。",
    r"(2) 由 $f(x)$ 在 $(-a,a)$ 内取得极值，故存在 $c\in(-a,a)$ 使得 $f'(c)=0$。",
    r"由泰勒公式可知 $\begin{cases}f(a)=f(c)+f'(c)(a-c)+\dfrac{f''(\eta_{1})}{2}(a-c)^{2},\ \eta_{1}\in(c,a),\\ f(-a)=f(c)+f'(c)(-a-c)+\dfrac{f''(\eta_{2})}{2}(a+c)^{2},\ \eta_{2}\in(-a,c),\end{cases}$",
    r"两式相减得 $f(a)-f(-a)=\dfrac{f''(\eta_{1})}{2}(a-c)^{2}-\dfrac{f''(\eta_{2})}{2}(a+c)^{2}$，",
    r"令 $|f''(\eta)|=\max\left\{|f''(\eta_{1})|,|f''(\eta_{2})|\right\}$，则",
    r"$|f(a)-f(-a)|\leqslant\left|\dfrac{f''(\eta)}{2}\right|\left[(a-c)^{2}+(a+c)^{2}\right]=\left|\dfrac{f''(\eta)}{2}\right|\left(2a^{2}+2c^{2}\right)\leqslant 2a^{2}|f''(\eta)|$",
    r"即存在 $\eta\in(-a,a)$ 使得 $|f''(\eta)|\geqslant\dfrac{1}{2a^{2}}|f(a)-f(-a)|$。",
])
