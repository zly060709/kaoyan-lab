# -*- coding: utf-8 -*-
"""2023 数学三 解析 第 10~11 页：题 19"""

A = {}

A[19] = (r"3\sqrt{3}-\dfrac{32+\pi}{9}", [
    r"【答案】$3\sqrt{3}-\dfrac{32+\pi}{9}$",
    r"【解析】$\iint_{D}\left|\sqrt{x^{2}+y^{2}}-1\right|\mathrm{d}x\mathrm{d}y=\iint_{D_1}(1-\sqrt{x^{2}+y^{2}})\mathrm{d}x\mathrm{d}y+\iint_{D_2}(\sqrt{x^{2}+y^{2}}-1)\mathrm{d}x\mathrm{d}y$",
    r"$=\iint_{D}(1-\sqrt{x^{2}+y^{2}})\mathrm{d}x\mathrm{d}y-\iint_{D_2}(1-\sqrt{x^{2}+y^{2}})\mathrm{d}x\mathrm{d}y+\iint_{D_2}(\sqrt{x^{2}+y^{2}}-1)\mathrm{d}x\mathrm{d}y$",
    r"$=\iint_{D}(1-\sqrt{x^{2}+y^{2}})\mathrm{d}x\mathrm{d}y-2\iint_{D_2}(1-\sqrt{x^{2}+y^{2}})\mathrm{d}x\mathrm{d}y=I_1-2I_2$",
    r"$I_1=\displaystyle\iint_{D}(1-\sqrt{x^{2}+y^{2}})\mathrm{d}x\mathrm{d}y=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\mathrm{d}\theta\int_{0}^{2\cos\theta}(1-r)r\mathrm{d}r=2\int_{0}^{\frac{\pi}{2}}(2\cos^{2}\theta-\dfrac{8}{3}\cos^{3}\theta)\mathrm{d}\theta$",
    r"$=4\displaystyle\int_{0}^{\frac{\pi}{2}}\cos^{2}\theta\mathrm{d}\theta-\dfrac{16}{3}\int_{0}^{\frac{\pi}{2}}\cos^{3}\theta\mathrm{d}\theta=4\times\dfrac{1}{2}\times\dfrac{\pi}{2}-\dfrac{16}{3}\times\dfrac{2}{3}\times1=\pi-\dfrac{32}{9}$",
    r"$I_2=\displaystyle\iint_{D_2}(1-\sqrt{x^{2}+y^{2}})\mathrm{d}x\mathrm{d}y=\int_{-\frac{\pi}{3}}^{\frac{\pi}{3}}\mathrm{d}\theta\int_{1}^{2\cos\theta}(1-r)r\mathrm{d}r=2\int_{0}^{\frac{\pi}{3}}(2\cos^{2}\theta-\dfrac{8}{3}\cos^{3}\theta-\dfrac{1}{6})\mathrm{d}\theta$",
    r"$=2\displaystyle\int_{0}^{\frac{\pi}{3}}(\cos 2\theta-\dfrac{8}{3}\cos^{3}\theta+\dfrac{5}{6})\mathrm{d}\theta=\int_{0}^{\frac{\pi}{3}}\cos 2\theta\mathrm{d}(2\theta)-\dfrac{16}{3}\int_{0}^{\frac{\pi}{3}}\cos^{3}\theta\mathrm{d}\theta+2\int_{0}^{\frac{\pi}{3}}\dfrac{5}{6}\mathrm{d}\theta$",
    r"$=\dfrac{\sqrt{3}}{2}-\dfrac{16}{3}\times\dfrac{3\sqrt{3}}{8}+\dfrac{5\pi}{9}=\dfrac{5}{9}\pi-\dfrac{3\sqrt{3}}{2}$",
    r"$\therefore I_1-2I_2=\pi-\dfrac{32}{9}-2(\dfrac{5}{9}\pi-\dfrac{3\sqrt{3}}{2})=3\sqrt{3}-\dfrac{32+\pi}{9}$",
    r"即 $\iint_{D}\left|\sqrt{x^{2}+y^{2}}-1\right|\mathrm{d}x\mathrm{d}y=3\sqrt{3}-\dfrac{32+\pi}{9}$。",
])
