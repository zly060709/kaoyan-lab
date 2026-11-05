# -*- coding: utf-8 -*-
"""2022 数学二 答案解析（p11）：A[22] 续写行。"""

A22_CONT = [
    r"二次型矩阵为 $\boldsymbol{A}=\begin{pmatrix}3&0&1\\ 0&4&0\\ 1&0&3\end{pmatrix}$，则特征方程为",
    r"$|\lambda\boldsymbol{E}-\boldsymbol{A}|=\begin{vmatrix}\lambda-3&0&-1\\ 0&\lambda-4&0\\ -1&0&\lambda-3\end{vmatrix}=(\lambda-4)^{2}(\lambda-2)$",
    r"得特征值 $\lambda_{1}=\lambda_{2}=4,\lambda_{3}=2$。",
    r"当 $\lambda_{1}=\lambda_{2}=4$ 时，$(4\boldsymbol{E}-\boldsymbol{A})x=0$ 得 $\boldsymbol{\xi}_{1}=(0,1,0)^{\mathrm{T}},\boldsymbol{\xi}_{2}=(1,0,1)^{\mathrm{T}}$",
    r"当 $\lambda_{3}=2$ 时，$(2\boldsymbol{E}-\boldsymbol{A})x=0$ 得 $\boldsymbol{\xi}_{3}=(1,0,-1)^{\mathrm{T}}$。",
    r"将 $\boldsymbol{\xi}_{1}=(0,1,0)^{\mathrm{T}},\boldsymbol{\xi}_{2}=(1,0,1)^{\mathrm{T}},\boldsymbol{\xi}_{3}=(1,0,-1)^{\mathrm{T}}$ 正交单位化得",
    r"$\boldsymbol{\eta}_{1}=(0,1,0)^{\mathrm{T}},\boldsymbol{\eta}_{2}=\dfrac{1}{\sqrt{2}}(1,0,1)^{\mathrm{T}},\boldsymbol{\eta}_{3}=\dfrac{1}{\sqrt{2}}(1,0,-1)^{\mathrm{T}}$ 可得 $\boldsymbol{Q}=\begin{pmatrix}0&\dfrac{1}{\sqrt{2}}&\dfrac{1}{\sqrt{2}}\\ 1&0&0\\ 0&\dfrac{1}{\sqrt{2}}&-\dfrac{1}{\sqrt{2}}\end{pmatrix}$，即",
    r"$\begin{cases}x_{1}=\dfrac{1}{\sqrt{2}}y_{2}+\dfrac{1}{\sqrt{2}}y_{3}\\ x_{2}=y_{2}\\ x_{3}=\dfrac{1}{\sqrt{2}}y_{2}-\dfrac{1}{\sqrt{2}}y_{3}\end{cases}$",
    r"$f(\boldsymbol{x})=4y_{1}^{2}+4y_{2}^{2}+2y_{3}^{2}$",
    r"(II) 由（1）知 $f\left(\boldsymbol{x}\right)=4y_{1}^{2}+4y_{2}^{2}+2y_{3}^{2}$，$\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}$，故 $\boldsymbol{x}^{\mathrm{T}}\boldsymbol{x}=\boldsymbol{y}^{\mathrm{T}}\boldsymbol{Q}^{\mathrm{T}}\boldsymbol{Q}\boldsymbol{y}=\boldsymbol{y}^{\mathrm{T}}\boldsymbol{y}$",
    r"故 $\dfrac{f(\boldsymbol{x})}{\boldsymbol{x}^{\mathrm{T}}\boldsymbol{x}}=\dfrac{g(\boldsymbol{y})}{\boldsymbol{y}^{\mathrm{T}}\boldsymbol{y}}=\dfrac{4y_{1}^{2}+4y_{2}^{2}+2y_{3}^{2}}{y_{1}^{2}+y_{2}^{2}+y_{3}^{2}}=2+\dfrac{2y_{1}^{2}+2y_{2}^{2}}{y_{1}^{2}+y_{2}^{2}+y_{3}^{2}}\geq 2$",
    r"当 $y_{1}=y_{2}=0,y_{3}\neq 0$ 时，可取到最小值 2。",
    r"所以存在非零向量 $\boldsymbol{y}$，即存在非零向量 $\boldsymbol{x}$，使得 $\dfrac{f(\boldsymbol{x})}{\boldsymbol{x}^{\mathrm{T}}\boldsymbol{x}}$ 取到最小值 2。得证。",
]
