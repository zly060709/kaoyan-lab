# -*- coding: utf-8 -*-
"""全库数学公式审计：找出会被 KaTeX 渲染跑偏的内容。

审计口径（与前端渲染路径一致）：
  A. 字段内 $ 数量为奇数（公式截断，KaTeX 不渲染或渲染错位）
  B. $...$ 片段内含中日韩文字（KaTeX math 模式报 Unicode 错误 → katex-error）
  C. $...$ 片段内 \\begin{env} 与 \\end{env} 不配对
  D. answer 字段既有 LaTeX 命令又含中日韩文字（前端按口径退回纯文本，
     裸 \\dfrac 等命令直接上屏 = 视觉跑偏，需人工裁决）
只审计会渲染的字段：stem / options / answer / source_blocks[].text|html / title。
用法: python -I -X utf8 tools/audit_math.py   （只读，不改数据）
"""
import glob, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CJK = re.compile(r"[\u3000-\u303f\u3400-\u9fff\uff00-\uffef]")
CMD = re.compile(r"\\[a-zA-Z]+")
DOLLAR_SPAN = re.compile(r"\$([^$]*)\$")

FIELDS = ("stem", "answer", "title")


def spans_ok_issues(text):
    """返回 (奇数$?, [片段问题])。\\text{...} 内的中日韩文字 KaTeX 可渲染，不算问题。"""
    issues = []
    n = (text or "").count("$")
    odd = n % 2 == 1
    for m in DOLLAR_SPAN.finditer(text or ""):
        seg = re.sub(r"\\text\{[^{}]*\}", "", m.group(1))
        if CJK.search(seg):
            issues.append(("CJK", m.group(1)[:60]))
        begins = re.findall(r"\\begin\{(\w+\*?)\}", seg)
        ends = re.findall(r"\\end\{(\w+\*?)\}", seg)
        if sorted(begins) != sorted(ends):
            issues.append(("ENV", m.group(1)[:60]))
    return odd, issues


def walk(q, where, hits):
    for f in FIELDS:
        v = q.get(f)
        if isinstance(v, str) and "$" in v:
            odd, iss = spans_ok_issues(v)
            if odd:
                hits.append((where, f"$奇偶:{f}", v[:100]))
            for kind, seg in iss:
                hits.append((where, f"{kind}:{f}", seg))
    for i, o in enumerate(q.get("options") or []):
        s = o if isinstance(o, str) else json.dumps(o, ensure_ascii=False)
        if "$" not in s:
            continue
        odd, iss = spans_ok_issues(s)
        if odd:
            hits.append((where, f"$奇偶:options[{i}]", s[:100]))
        for kind, seg in iss:
            hits.append((where, f"{kind}:options[{i}]", seg))
    for b in (q.get("source_blocks") or []):
        for key in ("text", "html"):
            v = b.get(key)
            if isinstance(v, str) and "$" in v:
                odd, iss = spans_ok_issues(v)
                if odd:
                    hits.append((where, f"$奇偶:block.{key}", v[:100]))
                for kind, seg in iss:
                    hits.append((where, f"{kind}:block.{key}", seg))
    # D：答案混排（有 LaTeX 命令 + 有 CJK → 前端退回纯文本，裸命令上屏）
    ans = q.get("answer")
    if isinstance(ans, str) and CMD.search(ans) and CJK.search(ans) and "$" not in ans:
        hits.append((where, "答案混排退纯文本", ans[:80]))
    # 答案 $ 奇偶
    if isinstance(ans, str) and ans.count("$") % 2 == 1:
        hits.append((where, "$奇偶:answer", ans[:80]))


def main():
    hits = []
    files = sorted(glob.glob(os.path.join(ROOT, "data", "*", "[12]*.json")))
    files = [f for f in files if re.match(r"^\d{4}\.json$", os.path.basename(f))]
    nq = 0
    for fp in files:
        rel = os.path.relpath(fp, ROOT)
        try:
            d = json.load(open(fp, encoding="utf-8"))
        except Exception as e:
            hits.append((rel, "JSON解析失败", str(e)))
            continue
        for q in d.get("questions", []):
            nq += 1
            walk(q, f"{q.get('id')}", hits)
        for p in (d.get("passages") or []):
            for b in (p.get("blocks") or []):
                v = b.get("html") or b.get("text") or ""
                if isinstance(v, str) and "$" in v:
                    odd, iss = spans_ok_issues(v)
                    if odd:
                        hits.append((f"{rel} passage", "$奇偶:passage", v[:80]))
    by_kind = {}
    for _, kind, _ in hits:
        k = kind.split(":")[0]
        by_kind[k] = by_kind.get(k, 0) + 1
    print(f"扫描 {len(files)} 个年文件 / {nq} 题；命中 {len(hits)} 处")
    print("分类统计:", json.dumps(by_kind, ensure_ascii=False))
    for where, kind, seg in hits:
        print(f"  [{kind}] {where} :: {seg}")
    # 退出码口径：CJK 入公式 / 环境不配对 / 数学卷 $ 奇偶 = 致命；
    # 英语美元符号奇偶 与 答案混排 = 已由前端双模式渲染 + 分段渲染兜底，仅报告不拦。
    fatal = [h for h in hits
             if h[1].startswith("CJK") or h[1].startswith("ENV")
             or (h[1].startswith("$奇偶") and not h[0].startswith("eng-"))]
    if fatal:
        print(f"致命 {len(fatal)} 处（其余为已兜底类，仅报告）")
    return 1 if fatal else 0


if __name__ == "__main__":
    sys.exit(main())
