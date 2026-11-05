# -*- coding: utf-8 -*-
"""2020 数学三 独立复算：不读草稿模块的解析，只用影像里读到的题面重新算一遍。

用法：python -X utf8 tools/work/check_m32020.py
任何一项不吻合即退出码 1（照录文本可能有错，以复算为准逐条回查）。
"""
import os
import sys
import math
import numpy as np
from fractions import Fraction as F

OK = FAIL = 0
LOG = []


def chk(label, got, want, tol=1e-9):
    global OK, FAIL
    if isinstance(want, (int, float)) and isinstance(got, (int, float)) and not isinstance(want, bool):
        good = abs(float(got) - float(want)) <= tol
    else:
        good = got == want
    if good:
        OK += 1
        LOG.append(f"  OK   {label}")
    else:
        FAIL += 1
        LOG.append(f"  FAIL {label}: got={got!r} want={want!r}")


def close(a, b, tol=1e-6):
    return abs(a - b) <= tol * max(1.0, abs(b))


# ---------------------------------------------------------------- 1 导数定义
# lim_{x->a} (f(x)-a)/(x-a) = b  =>  f(a)=a, f'(a)=b
# lim (sin f(x) - sin a)/(x-a) = cos(f(a)) * f'(a) = b cos a
a0, b0 = 1.3, -0.7
f = lambda x: a0 + b0 * (x - a0) + (x - a0) ** 2 * math.sin(1.0 / (x - a0))
g = lambda x: (math.sin(f(x)) - math.sin(a0)) / (x - a0)
want1 = b0 * math.cos(a0)
chk("1 极限值 = b*cos a（右趋）", g(a0 + 1e-7), want1, tol=1e-6)
chk("1 极限值 = b*cos a（左趋）", g(a0 - 1e-7), want1, tol=1e-6)
chk("1 前提 (f(x)-a)/(x-a) -> b", (f(a0 + 1e-7) - a0) / 1e-7, b0, tol=1e-6)

# ---------------------------------------------------------------- 2 第二类间断点
def fnc(x):
    try:
        return math.exp(1.0 / (x - 1)) * math.log(abs(1 + x)) / ((math.exp(x) - 1) * (x - 2))
    except OverflowError:
        return math.inf
    except ZeroDivisionError:
        return math.nan


# x=-1：ln|1+x| -> -inf，其余因子有界非零 => 极限为无穷 => 第二类
v_neg1 = [abs(fnc(-1 + d)) for d in (1e-3, 1e-9, 1e-15)]
chk("2 x=-1 无界增长（第二类）", v_neg1[2] > 3 * v_neg1[0], True)
# x=0：可去（第一类），左右极限相等且有限
chk("2 x=0 右极限 = -1/(2e)", fnc(0 + 1e-9), -1.0 / (2 * math.e), tol=1e-4)
chk("2 x=0 左极限 = -1/(2e)", fnc(0 - 1e-9), -1.0 / (2 * math.e), tol=1e-4)
# x=1：右极限 e^{1/(x-1)} -> +inf（第二类），左极限存在
chk("2 x=1 右极限发散", fnc(1 + 1e-3) > 1e3, True)
chk("2 x=1 左极限有限", abs(fnc(1 - 1e-3)) < 1e3, True)
# x=2：分子非零、分母 -> 0 => 无穷（第二类）
v_2 = [abs(fnc(2 + d)) for d in (1e-3, 1e-9)]
chk("2 x=2 无界增长（第二类）", v_2[1] > 100 * v_2[0], True)
chk("2 第二类间断点个数", sum([v_neg1[2] > 3 * v_neg1[0], fnc(1 + 1e-3) > 1e3, v_2[1] > 100 * v_2[0]]), 3)

# ---------------------------------------------------------------- 3 奇函数
# 取具体奇函数 f(x)=sin x + x（有连续导数），逐选项判定
xs = np.linspace(-3, 3, 1201)
mid = len(xs) // 2
sv = np.sin(xs) + xs
dv = np.cos(xs) + 1.0
hA = np.cos(sv) + dv            # cos f + f'  -> 偶
hC = np.cos(dv) + sv            # cos f' + f  -> 非奇非偶


def cum_from_zero(h):
    c = np.zeros(len(h))
    c[1:] = np.cumsum((h[:-1] + h[1:]) * (xs[1] - xs[0]) / 2)
    return c - c[mid]


FA, FC = cum_from_zero(hA), cum_from_zero(hC)
chk("3 选项A 被积函数为偶", float(np.max(np.abs(hA[::-1] - hA))), 0.0, tol=1e-12)
chk("3 选项A 变限积分是奇函数", float(np.max(np.abs(FA[::-1] + FA))), 0.0, tol=2e-6)
chk("3 选项C 变限积分既非奇也非偶",
    float(np.max(np.abs(FC[::-1] + FC))) > 1e-3 and float(np.max(np.abs(FC[::-1] - FC))) > 1e-3, True)

# ---------------------------------------------------------------- 4 幂级数
# sum n a_n (x-2)^n 收敛区间 (-2,6) => 半径 4 => sum a_n t^n 半径也是 4
# sum a_n (x+1)^{2n}: |(x+1)^2| < 4 => -3 < x < 1
r = 4.0
chk("4 收敛区间 = (-3,1)", (-1 - math.sqrt(r), -1 + math.sqrt(r)), (-3.0, 1.0))

# ---------------------------------------------------------------- 5 伴随矩阵
rng = np.random.default_rng(20200501)
bad = 0
for _ in range(200):
    M = rng.integers(-3, 4, size=(4, 4)).astype(float)
    # 强制 rank=3 且 A_{12} != 0
    N = M[:3, :]
    if np.linalg.matrix_rank(N) < 3:
        continue
    row4 = rng.integers(-2, 3, size=(1, 4)).astype(float)
    A = np.vstack([N, row4])
    A[3, :] = A[0, :] * 0.5 + A[1, :] * 0.5 + A[2, :] * 0.0  # 第4行由前3行线性组合 => rank<=3
    if np.linalg.matrix_rank(A) != 3:
        continue
    A12 = ((-1) ** (1 + 2)) * np.linalg.det(np.delete(np.delete(A, 0, 0), 1, 1))
    if abs(A12) < 1e-6:
        continue
    Astar = np.zeros((4, 4))
    for i in range(4):
        for j in range(4):
            Astar[j, i] = ((-1) ** (i + j)) * np.linalg.det(np.delete(np.delete(A, i, 0), j, 1))
    ns = np.linalg.matrix_rank(Astar)
    # 通解基底应为 a1,a3,a4
    basis = A[:, [0, 2, 3]]
    resid = np.max(np.abs(Astar @ basis))
    if ns != 1 or resid > 1e-8 or np.linalg.matrix_rank(basis) != 3:
        bad += 1
chk("5 r(A*)=1 且 a1,a3,a4 构成 A*x=0 的基础解系", bad, 0)

# ---------------------------------------------------------------- 6 相似对角化
A6 = np.array([[1.0, 0, 2], [0, 1, 1], [0, 0, -1]])
a1v = np.array([1.0, 0, 0])      # 特征值 1
a2v = np.array([0.0, 1, 0])      # 特征值 1（与 a1v 无关）
a3v = np.array([-2.0, -1, 2])    # 特征值 -1
chk("6 a1,a2 是特征值 1 的无关特征向量",
    (np.max(np.abs(A6 @ a1v - a1v)), np.max(np.abs(A6 @ a2v - a2v))), (0.0, 0.0))
chk("6 a3 是特征值 -1 的特征向量", float(np.max(np.abs(A6 @ a3v + a3v))), 0.0, tol=1e-12)
chk("6 a1,a2 线性无关", float(np.linalg.matrix_rank(np.column_stack([a1v, a2v]))), 2.0)
P = np.column_stack([a1v + a2v, a3v, a2v])   # 解析里给的 P=(a1+a2, a3, a2)
chk("6 P^-1AP = diag(1,-1,1)",
    float(np.max(np.abs(np.linalg.inv(P) @ A6 @ P - np.diag([1.0, -1, 1])))), 0.0, tol=1e-12)

# ---------------------------------------------------------------- 7 恰有一个发生
P_all = 3 * F(1, 4) - 2 * (F(0) + F(1, 12) + F(1, 12))
chk("7 恰有一个事件发生 = 5/12", P_all, F(5, 12))

# ---------------------------------------------------------------- 8 二维正态
# X~N(0,1), Y~N(0,4), rho=-1/2；求 (X+Y)/sqrt(3) 与 X 独立且为标准正态
covxy = -0.5 * 1 * 2
var_sum = 1 + 4 + 2 * covxy
chk("8 D(X+Y)=3", var_sum, 3.0)
chk("8 Cov(X,(X+Y)/sqrt3)=0", (1 + covxy) / math.sqrt(var_sum), 0.0, tol=1e-12)
chk("8 D((X+Y)/sqrt3)=1", var_sum / var_sum, 1.0)
rng = np.random.default_rng(8)
L = np.linalg.cholesky(np.array([[1.0, covxy], [covxy, 4.0]]))
Z = rng.standard_normal((2, 400000))
XY = L @ Z
comb = (XY[0] + XY[1]) / math.sqrt(3.0)
chk("8 蒙特卡洛方差 ~1", float(np.var(comb)), 1.0, tol=0.02)
chk("8 蒙特卡洛与 X 相关 ~0", float(np.corrcoef(XY[0], comb)[0, 1]), 0.0, tol=0.02)

# ---------------------------------------------------------------- 9 全微分
# z = arctan[xy + sin(x+y)] 在 (0,pi)
# u = xy + sin(x+y); u_x = y + cos(x+y); u_y = x + cos(x+y); z_x = u_x/(1+u^2)
u = 0 * math.pi + math.sin(0 + math.pi)
zx = (math.pi + math.cos(math.pi)) / (1 + u ** 2)
zy = (0 + math.cos(math.pi)) / (1 + u ** 2)
chk("9 dz/dx = pi-1", zx, math.pi - 1, tol=1e-12)
chk("9 dz/dy = -1", zy, -1.0, tol=1e-12)

# ---------------------------------------------------------------- 10 切线
# x + y + e^{2xy} = 0 在 (0,-1)：1 + y' + e^{2xy}(2y + 2x y') = 0
yp = -(1 + math.exp(0) * 2 * (-1)) / (1 + math.exp(0) * 0)
chk("10 斜率 = 1", yp, 1.0)
chk("10 切线 y = x - 1 过 (0,-1)", 0 - 1, -1.0)

# ---------------------------------------------------------------- 11 利润最大
# p(Q) = 800/(Q+2) - 3; L = p*Q - (100+13Q)
Qs = np.linspace(0.5, 60, 12000)
p = 800 / (Qs + 2) - 3
L = p * Qs - (100 + 13 * Qs)
chk("11 最大利润产量 Q=8", float(Qs[np.argmax(L)]), 8.0, tol=0.01)
chk("12 dL/dQ 在 Q=8 处为 0", 1600 / (8 + 2) ** 2 - 16, 0.0, tol=1e-12)

# ---------------------------------------------------------------- 12 旋转体体积
# V = ∫0^1 2*pi*x*(1/(1+x^2) - x/2) dx
ts, ws = np.polynomial.legendre.leggauss(200)
xv = 0.5 * ts + 0.5
wv = 0.5 * ws
V = np.sum(wv * 2 * math.pi * xv * (1 / (1 + xv ** 2) - xv / 2))
chk("12 V = pi(ln2 - 1/3)", float(V), math.pi * (math.log(2) - 1 / 3), tol=1e-10)

# ---------------------------------------------------------------- 13 行列式
for av in (0.0, 1.0, 2.5, -3.0):
    A13 = np.array([[av, 0, -1, 1], [0, av, 1, -1], [-1, 1, av, 0], [1, -1, 0, av]], float)
    chk(f"13 行列式 a={av}", float(np.linalg.det(A13)), av ** 2 * (av ** 2 - 4), tol=1e-9)

# ---------------------------------------------------------------- 14 EY
# X ~ P(X=k)=1/2^k；Y = X mod 3。等比级数取闭式，避免截断误差
q = F(1, 8)
py = {0: F(1, 8) / (1 - q), 1: F(1, 2) / (1 - q), 2: F(1, 4) / (1 - q)}
chk("14 P(Y=0)=1/7", py[0], F(1, 7))
chk("14 P(Y=1)=4/7", py[1], F(4, 7))
chk("14 P(Y=2)=2/7", py[2], F(2, 7))
chk("14 概率和 = 1", sum(py.values()), F(1))
chk("14 EY = 8/7", sum(i * py[i] for i in range(3)), F(8, 7))
# 蒙特卡洛对照
rng14 = np.random.default_rng(14)
u14 = rng14.random(400000)
X14 = np.ceil(-np.log(u14) / np.log(2)).astype(int)   # P(X=k)=2^-k
chk("14 蒙特卡洛 EY ~ 8/7", float(np.mean(X14 % 3)), 8.0 / 7.0, tol=0.01)

# ---------------------------------------------------------------- 15 等价无穷小定参
# (1+1/n)^n - e ~ b/n^a  =>  a=1, b=-e/2
def ratio(n, aa, bb):
    return (math.exp(n * math.log1p(1.0 / n)) - math.e) / (bb / n ** aa)
n15 = 10 ** 6
chk("15 a=1,b=-e/2 时比值 -> 1", ratio(n15, 1.0, -math.e / 2), 1.0, tol=1e-3)
chk("15 a=2 时比值发散（不是等价）", abs(ratio(n15, 2.0, -math.e / 2)) > 1e5, True)
chk("15 a=1,b=-e 时比值 -> 1/2（b 唯一）", ratio(n15, 1.0, -math.e), 0.5, tol=1e-3)
# 书面向导：n(ln(1+1/n)-1/n) ~ -1/(2n)
chk("15 n(ln(1+1/n)-1/n)*2n -> -1", n15 * (math.log1p(1.0 / n15) - 1.0 / n15) * 2 * n15, -1.0, tol=1e-3)

# ---------------------------------------------------------------- 16 二元极值
f16 = lambda x, y: x ** 3 + 8 * y ** 3 - x * y
gx = lambda x, y: 3 * x ** 2 - y
gy = lambda x, y: 24 * y ** 2 - x
chk("16 驻点(1/6,1/12) 梯度为 0", (gx(1 / 6, 1 / 12), gy(1 / 6, 1 / 12)), (0.0, 0.0))
chk("16 AC-B^2 在(1/6,1/12)", 6 * (1 / 6) * 48 * (1 / 12) - 1, 3.0)
chk("16 AC-B^2 在(0,0) < 0", 0 * 0 - 1, -1.0)
chk("16 极小值 = -1/216", f16(1 / 6, 1 / 12), -1 / 216, tol=1e-12)
nb = min(f16(1 / 6 + dx / 1000, 1 / 12 + dy / 1000) for dx in range(-9, 10) for dy in range(-9, 10))
chk("16 邻域内不更低", nb >= f16(1 / 6, 1 / 12) - 1e-15, True)

# ---------------------------------------------------------------- 17 微分方程 + 级数
# y''+2y'+5y=0, f(0)=1, f'(0)=-1 -> e^{-x}cos2x
f17 = lambda x: math.exp(-x) * math.cos(2 * x)
h17 = 1e-5
d1 = (f17(h17) - f17(-h17)) / (2 * h17)
d2 = (f17(h17) - 2 * f17(0.0) + f17(-h17)) / h17 ** 2
chk("17 f(0)=1", f17(0.0), 1.0)
chk("17 f'(0)=-1", d1, -1.0, tol=1e-6)
chk("17 f''+2f'+5f = 0", d2 + 2 * d1 + 5 * f17(0.0), 0.0, tol=1e-4)
ts17, ws17 = np.polynomial.legendre.leggauss(400)
lo, hi = math.pi, 60.0
t = 0.5 * (hi - lo) * ts17 + 0.5 * (lo + hi)
w = 0.5 * (hi - lo) * ws17
a1n = float(np.sum(w * np.exp(-t) * np.cos(2 * t)))
chk("17 a_1 = (1/5)e^{-pi}", a1n, math.exp(-math.pi) / 5, tol=1e-8)
chk("17 sum = (1/5)/(e^pi-1)", a1n / (1 - math.exp(-math.pi)), 0.2 / (math.exp(math.pi) - 1), tol=1e-8)

# ---------------------------------------------------------------- 18 二重积分
# A = int_0^1 (1-x^2)^{3/2} dx = 3pi/16 ;  I = A * int_0^1 x^2 sqrt(1-x^2) dx *? 见下
ts18, ws18 = np.polynomial.legendre.leggauss(2000)
xg = 0.5 * ts18 + 0.5
wg = 0.5 * ws18
A18 = float(np.sum(wg * (1 - xg ** 2) ** 1.5))
chk("18 A = 3pi/16", A18, 3 * math.pi / 16, tol=1e-10)
J = float(np.sum(wg * xg ** 2 * np.sqrt(1 - xg ** 2)))
chk("18 int_{-1}^{1}x^2 sqrt(1-x^2)dx = pi/8", 2 * J, math.pi / 8, tol=1e-7)
chk("18 结果 = 3pi^2/128", A18 * 2 * J, 3 * math.pi ** 2 / 128, tol=1e-7)

# ---------------------------------------------------------------- 19 中值定理（代数核）
for c in (0.4, 1.0, 1.7):
    M = 2.5
    lhs = (M / c - M) * (M / (2 - c) - M)
    rhs = -M ** 2 * (c - 1) ** 2 / (c * (2 - c))
    chk(f"19 恒等式 c={c}", lhs, rhs, tol=1e-12)

# ---------------------------------------------------------------- 20 二次型
A20 = np.array([[1.0, -2], [-2, 4]])
B20 = np.array([[4.0, 2], [2, 1]])
chk("20 tr 相等", np.trace(A20), np.trace(B20))
chk("20 行列式相等", np.linalg.det(A20), np.linalg.det(B20), tol=1e-12)
Q20 = (1 / 5) * np.array([[4.0, -3], [-3, -4]])
chk("20 Q 正交", np.max(np.abs(Q20.T @ Q20 - np.eye(2))), 0.0, tol=1e-12)
chk("20 Q^T A Q = B", np.max(np.abs(Q20.T @ A20 @ Q20 - B20)), 0.0, tol=1e-12)
P1 = (1 / math.sqrt(5)) * np.array([[2.0, 1], [1, -2]])
P2 = (1 / math.sqrt(5)) * np.array([[1.0, 2], [-2, 1]])
chk("20 Q = P1 P2^{-1}", np.max(np.abs(P1 @ np.linalg.inv(P2) - Q20)), 0.0, tol=1e-12)
chk("20 P1^-1 A P1 = diag(0,5)", np.max(np.abs(np.linalg.inv(P1) @ A20 @ P1 - np.diag([0.0, 5.0]))), 0.0, tol=1e-10)
chk("20 P2^-1 B P2 = diag(0,5)", np.max(np.abs(np.linalg.inv(P2) @ B20 @ P2 - np.diag([0.0, 5.0]))), 0.0, tol=1e-10)

# ---------------------------------------------------------------- 21 P^{-1}AP
alpha = np.array([1.0, 2.0])
A21 = np.array([[1.0, 3.0], [2.0, 2.0]])   # A^2+A-6E=0 的矩阵？先验证
A21 = np.array([[0.0, 6], [1, -1]])        # 满足 A^2+A-6E=0
v = A21 @ alpha
P = np.column_stack([alpha, v])
chk("21 P 可逆", abs(float(np.linalg.det(P))) > 1e-9, True)
chk("21 A^2 alpha + A alpha - 6 alpha = 0", np.max(np.abs(A21 @ A21 @ alpha + A21 @ alpha - 6 * alpha)), 0.0, tol=1e-12)
B21 = np.linalg.inv(P) @ A21 @ P
chk("21 P^-1AP = [[0,6],[1,-1]]", np.max(np.abs(B21 - np.array([[0.0, 6], [1, -1]]))), 0.0, tol=1e-12)
ev = np.linalg.eigvals(np.array([[0.0, 6], [1, -1]]))
chk("21 B 特征值 = -3,2", sorted(np.round(ev.real, 9).tolist()), [-3.0, 2.0])
chk("21 A 可对角化（两个不同特征值）", len(set(np.round(np.linalg.eigvals(A21).real, 6))), 2)

# ---------------------------------------------------------------- 22 二维均匀分布
rng = np.random.default_rng(22)
N = 400000
th = rng.uniform(0, math.pi, N)
rr = np.sqrt(rng.uniform(0, 1, N))
X = rr * np.cos(th)
Y = rr * np.sin(th)
z1 = ((X - Y) > 0).astype(int)
z2 = ((X + Y) > 0).astype(int)
joint = {(i, j): float(np.mean((z1 == i) & (z2 == j))) for i in (0, 1) for j in (0, 1)}
chk("22 P(0,0) ~ 1/4", joint[(0, 0)], 0.25, tol=0.004)
chk("22 P(0,1) ~ 1/2", joint[(0, 1)], 0.50, tol=0.004)
chk("22 P(1,0) ~ 0", joint[(1, 0)], 0.0, tol=0.004)
chk("22 P(1,1) ~ 1/4", joint[(1, 1)], 0.25, tol=0.004)
ez1, ez2 = z1.mean(), z2.mean()
dz1, dz2 = z1.var(), z2.var()
rho = ((z1 * z2).mean() - ez1 * ez2) / math.sqrt(dz1 * dz2)
chk("22 EZ1 ~ 1/4", ez1, 0.25, tol=0.004)
chk("22 EZ2 ~ 3/4", ez2, 0.75, tol=0.004)
chk("22 rho ~ 1/3", rho, 1 / 3, tol=0.01)
chk("22 密度 2/pi", 1.0 / (math.pi / 2), 2 / math.pi, tol=1e-12)

# ---------------------------------------------------------------- 23 威布尔 MLE
m23, th23 = 2.3, 1.7
rng = np.random.default_rng(23)
samp = th23 * (-np.log(1 - rng.uniform(0, 1, 200000))) ** (1 / m23)
chk("23 P(T>t) 解析=经验", float(np.mean(samp > 1.1)), math.exp(-(1.1 / th23) ** m23), tol=0.006)
s, tt = 0.8, 1.4
chk("23 条件概率解析=经验",
    float(np.mean((samp > s + tt)[samp > s])),
    math.exp((s / th23) ** m23 - ((s + tt) / th23) ** m23), tol=0.008)
th_hat = (np.mean(samp ** m23)) ** (1 / m23)
chk("23 MLE 估计接近真值", float(th_hat), th23, tol=0.02)
# 对数似然求导公式在 theta_hat 处为 0
n23 = len(samp)
dl = -m23 * n23 / th_hat + m23 * np.sum(samp ** m23) / th_hat ** (m23 + 1)
chk("23 dlnL/dtheta 在 theta_hat 处 = 0", float(dl / n23), 0.0, tol=1e-6)

print("\n".join(LOG))
print(f"吻合 {OK} 项，不吻合 {FAIL} 项")
sys.exit(1 if FAIL else 0)
