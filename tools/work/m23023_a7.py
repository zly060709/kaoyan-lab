# -*- coding: utf-8 -*-
"""2023 数学二 答案解析（视觉转录自 p11）。本文件：第 (19)(20) 题。"""

A = {}

A[19] = (r"(1) $\ln(\sqrt{2}+1)$ (2) $\pi\left(1-\dfrac{\pi}{4}\right)$", [
    r"(1) $S=\displaystyle\int_{1}^{+\infty}\dfrac{1}{x\sqrt{1+x^{2}}}\mathrm{d}x\xlongequal{x=\tan t}\int_{\frac{\pi}{4}}^{\frac{\pi}{2}}\dfrac{1}{\tan t\sec t}\sec^{2}t\,\mathrm{d}t=\int_{\frac{\pi}{4}}^{\frac{\pi}{2}}\csc t\,\mathrm{d}t$",
    r"$=\ln|\csc t-\cot t|\Big|_{\frac{\pi}{4}}^{\frac{\pi}{2}}=\ln(\sqrt{2}+1)$",
    r"(2) $V=\pi\displaystyle\int_{1}^{+\infty}\dfrac{1}{x^{2}(1+x^{2})}\mathrm{d}x=\pi\int_{1}^{+\infty}\left(\dfrac{1}{x^{2}}-\dfrac{1}{1+x^{2}}\right)\mathrm{d}x$",
    r"$=\pi\left(-\dfrac{1}{x}-\arctan x\right)\Big|_{1}^{+\infty}=\pi\left(1-\dfrac{\pi}{4}\right)$",
])

A[20] = (r"\dfrac{\sqrt{3}\ln 2}{24}\pi", [
    r"利用极坐标：设 $x=r\cos\theta,\ y=r\sin\theta,\ \mathrm{d}x\mathrm{d}y=r\mathrm{d}r\mathrm{d}\theta$，根据 $x^{2}+y^{2}-xy=1$，$x^{2}+y^{2}-xy=2$，$y=\sqrt{3}x$，",
    r"从而得到：$0\leqslant\theta\leqslant\dfrac{\pi}{3}$，$\dfrac{1}{\sqrt{1-\sin\theta\cos\theta}}\leqslant r\leqslant\sqrt{\dfrac{2}{1-\sin\theta\cos\theta}}$",
    r"所以 $\displaystyle\iint_{D}\dfrac{1}{3x^{2}+y^{2}}\mathrm{d}x\mathrm{d}y=\int_{0}^{\frac{\pi}{3}}\mathrm{d}\theta\int_{\frac{1}{\sqrt{1-\sin\theta\cos\theta}}}^{\sqrt{\frac{2}{1-\sin\theta\cos\theta}}}\dfrac{r}{r^{2}(3\cos^{2}\theta+\sin^{2}\theta)}\mathrm{d}r$",
    r"$=\displaystyle\int_{0}^{\frac{\pi}{3}}\dfrac{\ln\sqrt{2}}{3\cos^{2}\theta+\sin^{2}\theta}\mathrm{d}\theta=\int_{0}^{\frac{\pi}{3}}\dfrac{\ln\sqrt{2}(\cos^{2}\theta+\sin^{2}\theta)}{3\cos^{2}\theta+\sin^{2}\theta}\mathrm{d}\theta$",
    r"$=\displaystyle\int_{0}^{\frac{\pi}{3}}\dfrac{\ln\sqrt{2}(1+\tan^{2}\theta)}{3+\tan^{2}\theta}\mathrm{d}\theta=\int_{0}^{\frac{\pi}{3}}\dfrac{\ln\sqrt{2}}{3+\tan^{2}\theta}\mathrm{d}\tan\theta=\dfrac{\sqrt{3}\ln 2}{24}\pi$",
])
