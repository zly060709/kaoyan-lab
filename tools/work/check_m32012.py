# -*- coding: utf-8 -*-
"""2012 数学三 解答题 15-23 独立复算（不读解析文本，只按题干重算，再与照录结果比对）"""
import sys, os
from fractions import Fraction as F
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ok, bad = [], []


def chk(num, name, got, want, tol=1e-9):
    same = (got == want) if isinstance(want, (int, F, str, tuple, list, dict, type(None))) else abs(got - want) < tol
    (ok if same else bad).append((num, name, got, want))
    print(("  PASS " if same else "  FAIL ") + f"{num} {name}: 复算={got} 卷面={want}")


# ---------- 15：泰勒级数精确算 ----------
def series_mul(a, b, n=6):
    r = {}
    for i, ca in a.items():
        for j, cb in b.items():
            if i + j <= n:
                r[i + j] = r.get(i + j, F(0)) + ca * cb
    return r


def exp_of(u, n=6):
    out = {0: F(1)}
    term = {0: F(1)}
    k = 1
    while k <= 8:
        term = series_mul(term, u, n)
        for p, c in term.items():
            out[p] = out.get(p, F(0)) + c / F(k)
        k += 1
    return {p: c for p, c in out.items() if c != 0}


u1 = {2: F(1)}                                   # x^2
ex2 = exp_of(u1)                                 # e^{x^2}
cos = {0: F(1), 2: F(-1, 2), 4: F(1, 24), 6: F(-1, 720)}
u2 = {p: (-2 * c if p else 2 - 2 * c) for p, c in cos.items() if p}   # 2-2cos x
e2 = exp_of(u2)
diff = {p: ex2.get(p, F(0)) - e2.get(p, F(0)) for p in set(ex2) | set(e2)}
chk(15, "极限=1/12", diff.get(4, F(0)), F(1, 12))

# ---------- 16：二重积分 ----------
xs, ws = np.polynomial.legendre.leggauss(200)
gx = 0.5 * (xs + 1)
gw = 0.5 * ws
val = 0.0
for x, wx in zip(gx, gw):
    ts, tw = np.polynomial.legendre.leggauss(200)
    lo, hi = np.sqrt(x), 1 / np.sqrt(x)
    t = 0.5 * (hi - lo) * ts + 0.5 * (lo + hi)
    w = 0.5 * (hi - lo) * tw
    val += wx * np.sum(w * np.exp(x) * x * t)
chk(16, "∬e^x x y dxdy=1/2", round(val, 9), 0.5, tol=1e-6)

# ---------- 17：拉格朗日 ----------
A17 = np.array([[F(1, 2), 0, 1], [0, 1, 1], [1, 1, 0]], dtype=float)
b17 = np.array([-20, -6, 50], dtype=float)
x, y, lam = np.linalg.solve(A17, b17)
chk(17, "驻点 x", x, 24.0, tol=1e-9)
chk(17, "驻点 y", y, 26.0, tol=1e-9)
chk(17, "lambda", lam, -32.0, tol=1e-9)
C = 10000 + 20 * x + x * x / 4 + 6 * y + y * y / 2
chk(17, "最小总成本", C, 11118.0, tol=1e-9)
chk(17, "甲的边际成本", 20 + x / 2, 32.0, tol=1e-9)

# ---------- 18：不等式 ----------
def f18(t):
    return t * np.log((1 + t) / (1 - t)) + np.cos(t) - 1 - t * t / 2


def d2f18(t):
    return 4 / (1 - t * t) + 4 * t * t / ((1 + t) ** 2 * (1 - t) ** 2) - np.cos(t) - 1


ts = np.linspace(1e-4, 0.9999, 4000)
chk(18, "f''>0 于 (0,1)", bool(np.all(d2f18(ts) > 0)), True)
chk(18, "f(0)=0", f18(0.0), 0.0, tol=1e-12)
chk(18, "f>0 于 (0,1)", bool(np.all(f18(ts) > 0)), True)
neg = np.linspace(-0.9999, -1e-4, 4000)
chk(18, "偶函数+f>0 于 (-1,0)", bool(np.allclose(f18(neg), f18(-neg)) and np.all(f18(neg) > 0)), True)

# ---------- 19 ----------
# f=c1 e^x + c2 e^{-2x} 代入 f''+f=2e^x：2c1 e^x + 5c2 e^{-2x} = 2e^x
M19 = np.array([[2.0, 0.0], [0.0, 5.0]])
c1, c2 = np.linalg.solve(M19, np.array([2.0, 0.0]))
chk(19, "c1", c1, 1.0, tol=1e-12)
chk(19, "c2", c2, 0.0, tol=1e-12)
for r in (1.0, -2.0):
    if abs(r * r + r - 2) > 1e-12:
        bad.append((19, "特征根", r, "r^2+r-2=0"))
    else:
        ok.append((19, "特征根", r))
print("  PASS 19 特征方程 r^2+r-2=0 的根 1,-2 均满足")


def y19(t):
    xs_, ws_ = np.polynomial.legendre.leggauss(400)
    u = 0.5 * t * xs_ + 0.5 * t
    w = 0.5 * t * ws_
    return np.exp(t * t) * np.sum(w * np.exp(-u * u))


def d2y_formula(t):
    xs_, ws_ = np.polynomial.legendre.leggauss(400)
    u = 0.5 * t * xs_ + 0.5 * t
    w = 0.5 * t * ws_
    return 2 * np.exp(t * t) * (1 + 2 * t * t) * np.sum(w * np.exp(-u * u)) + 2 * t


for t in (-0.8, -0.3, 0.3, 0.8):
    h = 1e-5
    num = (y19(t + h) - 2 * y19(t) + y19(t - h)) / (h * h)
    if abs(num - d2y_formula(t)) > 1e-3:
        bad.append((19, f"y''({t})", num, d2y_formula(t)))
        print(f"  FAIL 19 y''({t}): 数值={num} 卷面式={d2y_formula(t)}")
    else:
        ok.append((19, f"y''({t})"))
        print(f"  PASS 19 y''({t}) 与卷面表达式一致（符号：{'负' if num < 0 else '正'}）")
chk(19, "y''(0)", d2y_formula(0.0), 0.0, tol=1e-9)

# ---------- 20 ----------
def det4(M):
    r = F(0)
    for j in range(4):
        if M[0][j] == 0:
            continue
        minor = [[M[i][k] for k in range(4) if k != j] for i in range(1, 4)]
        r += F((-1) ** j) * M[0][j] * det3(minor)
    return r


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def A20(a):
    return [[F(1), F(a), 0, 0], [0, F(1), F(a), 0], [0, 0, F(1), F(a)], [F(a), 0, 0, F(1)]]


beta = [F(1), F(-1), F(0), F(0)]
for a in (2, 3, F(1, 2), -1, 1):
    got = det4(A20(a))
    want = F(1) - F(a) ** 4
    if got != want:
        bad.append((20, f"|A| a={a}", got, want))
        print(f"  FAIL 20 |A|(a={a}) = {got}，应为 {want}")
print("  PASS 20 |A|=1-a^4（a=2,3,1/2,-1,1 五值精确相等）")
chk(20, "|A|(a=1)=0", det4(A20(1)), F(0))
M = np.array([[1.0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 1]])
Ma = np.column_stack([M, [1.0, -1, 0, 0]])
chk(20, "a=1: r(A)<r(增广)", (np.linalg.matrix_rank(M), np.linalg.matrix_rank(Ma)), (3, 4))
M2 = np.array([[1.0, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, -1], [-1, 0, 0, 1]])
M2a = np.column_stack([M2, [1.0, -1, 0, 0]])
chk(20, "a=-1: r(A)=r(增广)=3", (np.linalg.matrix_rank(M2), np.linalg.matrix_rank(M2a)), (3, 3))
p0 = np.array([0.0, -1, 0, 0])
p1 = np.array([1.0, 1, 1, 1])
chk(20, "特解满足 A x=beta", list(M2 @ p0), [1.0, -1.0, 0.0, 0.0], tol=1e-12)
chk(20, "导出组基础解系", list(M2 @ p1), [0.0, 0.0, 0.0, 0.0], tol=1e-12)

# ---------- 21 ----------
Aq = np.array([[1.0, 0, 1], [0, 1, 1], [-1, 0, -1], [0, -1, -1]])
G = Aq.T @ Aq
chk(21, "A^T A", G.tolist(), [[2.0, 0, 2], [0, 2, 2], [2, 2, 4]], tol=1e-12)
ev = np.linalg.eigvalsh(G)
chk(21, "特征值集合", sorted(np.round(ev, 9).tolist()), [0.0, 2.0, 6.0], tol=1e-9)
for lamv, vec in ((2.0, [1, -1, 0]), (6.0, [1, 1, 2]), (0.0, [1, 1, -1])):
    v = np.array(vec, dtype=float)
    resid = np.linalg.norm(G @ v - lamv * v)
    chk(21, f"特征向量 {vec}", round(resid, 12), 0.0, tol=1e-9)
Q = np.column_stack([np.array([1, -1, 0]) / np.sqrt(2), np.array([1, 1, 2]) / np.sqrt(6),
                     np.array([1, 1, -1]) / np.sqrt(3)])
chk(21, "Q 正交", np.round(np.linalg.norm(Q.T @ Q - np.eye(3)), 12), 0.0, tol=1e-9)
chk(21, "Q^T G Q 对角元", np.round(np.diag(Q.T @ G @ Q), 9).tolist(), [2.0, 6.0, 0.0], tol=1e-9)
# a=-1 的必要性：r(A)=2
chk(21, "r(A) 当 a=-1", int(np.linalg.matrix_rank(np.array([[1.0, 0, 1], [0, 1, 1], [-1, 0, -1], [0, -1, -1]]))), 2)

# ---------- 22 ----------
P = {(0, 0): F(1, 4), (0, 2): F(1, 4), (1, 1): F(1, 3), (2, 0): F(1, 12), (2, 2): F(1, 12)}
chk(22, "联合分布和为1", sum(P.values()), F(1))
px = {i: sum(v for (a, b), v in P.items() if a == i) for i in (0, 1, 2)}
py = {j: sum(v for (a, b), v in P.items() if b == j) for j in (0, 1, 2)}
chk(22, "X 分布律", [px[0], px[1], px[2]], [F(1, 2), F(1, 3), F(1, 6)])
chk(22, "Y 分布律", [py[0], py[1], py[2]], [F(1, 3), F(1, 3), F(1, 3)])
chk(22, "P(X=2Y)", P[(0, 0)] + P.get((2, 1), F(0)), F(1, 4))
pXY = {}
for (a, b), v in P.items():
    pXY[a * b] = pXY.get(a * b, F(0)) + v
chk(22, "XY 分布律", [pXY.get(k, F(0)) for k in (0, 1, 2, 4)], [F(7, 12), F(1, 3), F(0), F(1, 12)])
EX = sum(a * v for (a, b), v in P.items())
EX2 = sum(a * a * v for (a, b), v in P.items())
EY = sum(b * v for (a, b), v in P.items())
EY2 = sum(b * b * v for (a, b), v in P.items())
EXY = sum(a * b * v for (a, b), v in P.items())
chk(22, "EX", EX, F(2, 3))
chk(22, "EX^2", EX2, F(1))
chk(22, "EY", EY, F(1))
chk(22, "EY^2", EY2, F(5, 3))
chk(22, "EXY", EXY, F(2, 3))
chk(22, "DX", EX2 - EX * EX, F(5, 9))
chk(22, "DY", EY2 - EY * EY, F(2, 3))
chk(22, "cov(X-Y,Y)", (EXY - EX * EY) - (EY2 - EY * EY), F(-2, 3))

# ---------- 23 ----------
rng = np.random.default_rng(20121105)
X = rng.exponential(1.0, 4_000_000)
Y = rng.exponential(1.0, 4_000_000)
V = np.minimum(X, Y)
U = np.maximum(X, Y)
chk(23, "V 的均值≈1/2", round(V.mean(), 3), 0.5, tol=0.01)
chk(23, "E(U+V)=E(X+Y)=2", round((U + V).mean(), 3), 2.0, tol=0.01)
chk(23, "P(V>v)≈e^{-2v} (v=1)", round(float((V > 1).mean()), 3), round(float(np.exp(-2)), 3), tol=0.01)
vs = np.linspace(0.05, 3, 60)
cdf = np.array([(V <= v).mean() for v in vs])
theo = 1 - np.exp(-2 * vs)
chk(23, "分布函数=1-e^{-2v}", round(float(np.max(np.abs(cdf - theo))), 4), 0.0, tol=0.005)
edges = np.linspace(0, 2.5, 26)
cnt, _ = np.histogram(V, bins=edges)
centers = 0.5 * (edges[:-1] + edges[1:])
dens = cnt / (len(V) * (edges[1] - edges[0]))
chk(23, "密度=2e^{-2v}（直方图）", round(float(np.max(np.abs(dens - 2 * np.exp(-2 * centers)))), 4), 0.0, tol=0.03)

print("\n================ 复算汇总 ================")
print(f"吻合 {len(ok)} 项，不吻合 {len(bad)} 项")
for b in bad:
    print("  不吻合：", b)
sys.exit(1 if bad else 0)
