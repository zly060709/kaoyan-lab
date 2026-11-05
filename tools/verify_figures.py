# -*- coding: utf-8 -*-
"""图形规格自检：镜像前端 compileExpr 白名单 + 取样求值 + qid 匹配。
用法: python -I -X utf8 tools/verify_figures.py math 2013 2023"""
import glob, json, math, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
subj = sys.argv[1] if len(sys.argv) > 1 else "math"
y1 = int(sys.argv[2]) if len(sys.argv) > 2 else 0
y2 = int(sys.argv[3]) if len(sys.argv) > 3 else 9999

FNS = {"sin", "cos", "tan", "asin", "acos", "atan", "sinh", "cosh", "tanh",
       "ln", "log", "log10", "exp", "sqrt", "abs", "floor", "ceil", "min", "max"}
PYFN = {"sin": math.sin, "cos": math.cos, "tan": math.tan, "asin": math.asin,
        "acos": math.acos, "atan": math.atan, "sinh": math.sinh, "cosh": math.cosh,
        "tanh": math.tanh, "ln": math.log, "log": math.log, "log10": math.log10,
        "exp": math.exp, "sqrt": math.sqrt, "abs": abs, "floor": math.floor,
        "ceil": math.ceil, "min": min, "max": max, "pi": math.pi, "e": math.e}
KINDS = {"graph", "shade_between", "shade_under", "point", "vline", "hline",
         "circle", "segment", "polygon", "parametric", "polar", "label"}

def compile_check(expr):
    cleaned = re.sub(r"\s+", "", expr or "")
    if not cleaned:
        raise ValueError("空表达式")
    if not re.match(r"^[0-9a-zA-Z_+\-*/^(),.]+$", cleaned):
        raise ValueError(f"非法字符: {expr}")
    toks = re.findall(r"[a-zA-Z_]+", cleaned)
    for t in toks:
        if t not in FNS and t not in ("x", "t", "pi", "e"):
            raise ValueError(f"未知符号 {t} in {expr}")
    js = cleaned.replace("^", "**")
    return js

def evaluate(js, x):
    env = dict(PYFN)
    env["x"] = x
    env["t"] = x
    try:
        return eval(js, {"__builtins__": {}}, env)  # 受控求值，仅白名单符号
    except Exception:
        return float("nan")

ok_all = True
total = 0
for fp in sorted(glob.glob(os.path.join(ROOT, "data", subj, "figures", "*.json"))):
    year = int(os.path.basename(fp)[:4])
    if not (y1 <= year <= y2):
        continue
    dat = json.load(open(os.path.join(ROOT, "data", subj, f"{year}.json"), encoding="utf-8"))
    ids = {q["id"] for q in dat.get("questions", [])}
    figs = json.load(open(fp, encoding="utf-8"))
    errs = []
    for f in figs:
        if f.get("qid") not in ids:
            errs.append(f"{f.get('qid')}: qid 不存在于 {year} 题库")
        if f.get("origin") != "derived":
            errs.append(f"{f.get('qid')}: origin 应为 derived")
        for it in f.get("items", []):
            if it.get("kind") not in KINDS:
                errs.append(f"{f.get('qid')}: 未知 kind {it.get('kind')}")
            for key in ("f", "f1", "f2", "fx", "fy", "r"):
                if key in it:
                    try:
                        js = compile_check(it[key])
                        vals = [evaluate(js, x) for x in (-2.1, -0.7, 0.31, 1.3, 2.9)]
                        if all(v != v for v in vals):  # 全 NaN
                            errs.append(f"{f.get('qid')}: {key}={it[key]} 全部取样为 NaN")
                    except ValueError as e:
                        errs.append(f"{f.get('qid')}: {e}")
            # circle 支持 cx/cy 任意圆心（与前端 DSL 同步，cx/cy 缺省 0）
            if it.get("kind") == "circle":
                for key in ("cx", "cy", "r"):
                    if key in it and not isinstance(it[key], (int, float)):
                        errs.append(f"{f.get('qid')}: circle.{key} 应为数值")
    total += len(figs)
    status = "OK" if not errs else "FAIL"
    if errs:
        ok_all = False
    print(f"{subj} figures {year}: {len(figs)} 幅 [{status}]")
    for e in errs[:6]:
        print("   -", e)

print(f"TOTAL figures checked: {total} -> {'ALL OK' if ok_all else 'HAS FAIL'}")
sys.exit(0 if ok_all else 1)
