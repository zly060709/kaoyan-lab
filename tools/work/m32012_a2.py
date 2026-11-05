# -*- coding: utf-8 -*-
"""2012 数学三 解析 填空题 9-14（原卷 p7-p8，逐字照录）"""

A = {}

A[9] = (r"e^{-\sqrt{2}}", [
    r"（9）【答案】$e^{-\sqrt{2}}$",
    r"【详解】“$1^{\infty}$”型极限，原式$=\lim\limits_{x\to\frac{\pi}{4}}(1+\tan x-1)^{\frac{1}{\cos x-\sin x}}"
    r"=e^{\lim\limits_{x\to\frac{\pi}{4}}\frac{\tan x-1}{\cos x-\sin x}}$；",
    r"$\lim\limits_{x\to\frac{\pi}{4}}\dfrac{\tan x-1}{\cos x-\sin x}"
    r"=\lim\limits_{x\to\frac{\pi}{4}}\dfrac{\sin x-\cos x}{\cos x(\cos x-\sin x)}"
    r"=\lim\limits_{x\to\frac{\pi}{4}}\dfrac{-1}{\cos x}=-\sqrt{2}$，于是，原式$=e^{-\sqrt{2}}$.",
])

A[10] = (r"\dfrac{1}{e}", [
    r"（10）【答案】$\dfrac{1}{e}$",
    r"【详解】$\dfrac{dy}{dx}\Big|_{x=e}=f'(f(x))f'(x)\Big|_{x=e}"
    r"=f'\left(\dfrac{1}{2}\right)f'(e)=2\cdot\dfrac{1}{2e}=\dfrac{1}{e}$.",
])

A[11] = ("2dx-dy", [
    r"（11）【答案】$2dx-dy$",
    r"【详解】$f(0,1)=1$",
    r"$\Rightarrow\lim\limits_{x\to0\atop y=1}\dfrac{f(x,1)-2x-1}{|x|}=0$，"
    r"$\lim\limits_{x\to0\atop y=1}\dfrac{f(x,1)-2x-1}{x}\cdot\dfrac{x}{|x|}=0$,",
    r"$\lim\limits_{x\to0\atop y=1}\dfrac{f(x,1)-2x-1}{x}=0\Rightarrow\lim\limits_{x\to0\atop y=1}\dfrac{f(x,1)-1}{x}=2$，"
    r"于是 $f_{x}(0,1)=2$,",
    r"同理，$\lim\limits_{x=0\atop y\to1}\dfrac{f(0,y)-1+y-1}{y-1}=0\Rightarrow"
    r"\lim\limits_{x=0\atop y\to1}\dfrac{f(0,y)-1}{y-1}+1=0,"
    r"\lim\limits_{x=0\atop y\to1}\dfrac{f(0,y)-1}{y-1}=-1$,",
    r"于是，$f_{y}(0,1)=-1$. 则有 $dz\big|_{(0,1)}=2dx-dy$.",
])

A[12] = (r"4\ln 2", [
    r"（12）【答案】$4\ln 2$.",
    r"【详解】$\int_{0}^{1}(4x-x)dx+\int_{1}^{2}\left(\dfrac{4}{x}-x\right)dx=4\ln 2$.",
])

A[13] = ("-27", [
    r"（13）【答案】$-27$.",
    r"【详解】设 $E_{12}=\begin{pmatrix}0&1&0\\ 1&0&0\\ 0&0&1\end{pmatrix}$",
    r"则 $B=E_{12}A$，从而 $\left|BA^{*}\right|=\left|E_{12}AA^{*}\right|"
    r"=-|A|\left|A^{*}\right|=-|A|^{3}=-27$.",
])

A[14] = (r"\dfrac{3}{4}", [
    r"（14）【答案】$\dfrac{3}{4}$",
    r"【详解】因为 $A$ 与 $C$ 互不相容，即 $AC=\phi$，又因为 $A=AC+A\overline{C}$，所以 $A\overline{C}=A$.",
    r"从而 $AB\overline{C}=AB$，则 $P(AB/\overline{C})=\dfrac{P(AB\overline{C})}{P(\overline{C})}"
    r"=\dfrac{P(AB)}{1-P(C)}=\dfrac{3}{4}$.",
])
