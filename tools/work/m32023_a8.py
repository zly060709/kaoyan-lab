# -*- coding: utf-8 -*-
"""2023 数学三 解析 第 11~12 页：题 20（证明题）"""

A = {}

A[20] = ("证明见解析", [
    r"【证明】(Ⅰ) 由泰勒公式可知",
    r"$\begin{cases}f(a)=f(0)+f'(0)a+\dfrac{f''(\xi_1)}{2}a^{2},\ \xi_1\in(0,a),\\[4pt] f(-a)=f(0)-f'(0)a+\dfrac{f''(\xi_2)}{2}a^{2},\ \xi_2\in(-a,0),\end{cases}$",
    r"两式相加得 $f(a)+f(-a)=\dfrac{f''(\xi_1)+f''(\xi_2)}{2}a^{2}$，",
    r"再由平均值定理可知存在 $\xi\in(-a,a)$ 使得 $f''(\xi)=\dfrac{f''(\xi_1)+f''(\xi_2)}{2}$，",
    r"即存在 $\xi\in(-a,a)$ 使得 $f''(\xi)=\dfrac{1}{a^{2}}\bigl[f(a)+f(-a)\bigr]$。",
    r"(Ⅱ) 由 $f(x)$ 在 $(-a,a)$ 内取得极值，故存在 $c\in(-a,a)$ 使得 $f'(c)=0$。",
    r"由泰勒公式可知 $\begin{cases}f(a)=f(c)+f'(c)(a-c)+\dfrac{f''(\eta_1)}{2}(a-c)^{2},\ \eta_1\in(c,a),\\[4pt] f(-a)=f(c)+f'(c)(-a-c)+\dfrac{f''(\eta_2)}{2}(a+c)^{2},\ \eta_2\in(-a,c),\end{cases}$",
    r"两式相减得 $f(a)-f(-a)=\dfrac{f''(\eta_1)}{2}(a-c)^{2}-\dfrac{f''(\eta_2)}{2}(a+c)^{2}$，",
    r"令 $\left|f''(\eta)\right|=\max\left\{\left|f''(\eta_1)\right|,\left|f''(\eta_2)\right|\right\}$，则",
    r"$\left|f(a)-f(-a)\right|\leqslant\left|\dfrac{f''(\eta)}{2}\right|\left[(a-c)^{2}+(a+c)^{2}\right]=\left|\dfrac{f''(\eta)}{2}\right|\left(2a^{2}+2c^{2}\right)\leqslant 2a^{2}\left|f''(\eta)\right|$，",
    r"即存在 $\eta\in(-a,a)$ 使得 $\left|f''(\eta)\right|\geqslant\dfrac{1}{2a^{2}}\left|f(a)-f(-a)\right|$。",
])
