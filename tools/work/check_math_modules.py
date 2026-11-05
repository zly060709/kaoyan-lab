# -*- coding: utf-8 -*-
"""子代理交付模块的机械校验：题数/分值/LaTeX 配对/答案字母/选项数/META 完整性。
用法: python -I -X utf8 tools/work/check_math_modules.py m32020 m12009 ...
退出码 0 = 全部通过；[缺字] 不算失败但会列出，由父会话裁决。"""
import importlib
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ok_all = True
for pfx in sys.argv[1:]:
    errs, flags = [], []
    q = importlib.import_module(f"{pfx}_q")
    a1 = importlib.import_module(f"{pfx}_a1")
    a2 = importlib.import_module(f"{pfx}_a2")
    a3 = importlib.import_module(f"{pfx}_a3")
    meta = importlib.import_module(f"{pfx}_meta")
    ANA = {}
    for m in (a1, a2, a3):
        ANA.update(m.A)
    META = meta.META
    items = q.ITEMS
    nums = [it["num"] for it in items]
    if nums != list(range(1, len(nums) + 1)):
        errs.append(f"题号不连续: {nums}")
    total = sum(it["score"] for it in items)
    if total != 150:
        errs.append(f"分数合计 {total} != 150")
    if len(items) != 23:
        flags.append(f"题数 {len(items)} != 23（老结构应为 23）")
    for it in items:
        n, typ = it["num"], it["type"]
        if typ not in ("single", "blank", "essay", "analysis"):
            errs.append(f"Q{n} 非法题型 {typ}")
        if typ == "single" and len(it.get("options", [])) != 4:
            errs.append(f"Q{n} 选项数 {len(it.get('options', []))} != 4")
        if typ == "single" and n > 8:
            flags.append(f"Q{n} single 在老结构里应属填空/解答区间")
        texts = [("stem", it["stem"])] + [(f"opt{i+1}", o) for i, o in enumerate(it.get("options", []))]
        for name, t in texts:
            if t.count("$") % 2:
                errs.append(f"Q{n} {name}: $ 奇偶")
            if t.count("{") != t.count("}"):
                errs.append(f"Q{n} {name}: 花括号不配对")
            for env in re.findall(r"\\begin\{(\w+\*?)\}", t):
                if t.count(f"\\begin{{{env}}}") != t.count(f"\\end{{{env}}}"):
                    errs.append(f"Q{n} {name}: {env} 不配对")
        if n not in ANA:
            errs.append(f"Q{n} 缺解析")
            continue
        ans, lines = ANA[n]
        block_text = "\n".join(lines)
        if block_text.count("$") % 2:
            errs.append(f"Q{n} 解析: $ 奇偶")
        if block_text.count("{") != block_text.count("}"):
            errs.append(f"Q{n} 解析: 花括号不配对")
        for env in re.findall(r"\\begin\{(\w+\*?)\}", block_text):
            if block_text.count(f"\\begin{{{env}}}") != block_text.count(f"\\end{{{env}}}"):
                errs.append(f"Q{n} 解析: {env} 不配对")
        if "[缺字]" in block_text or "[缺字]" in it["stem"]:
            flags.append(f"Q{n} 含 [缺字]")
        if typ == "single" and (not isinstance(ans, str) or not re.fullmatch(r"[A-D]", ans.strip())):
            errs.append(f"Q{n} 客观题答案异常: {ans!r}")
        if n not in META:
            errs.append(f"Q{n} 缺 META")
        else:
            kps, diff, cat = META[n]
            if cat not in ("gaoshu", "xiandai", "gailv"):
                errs.append(f"Q{n} META 板块异常 {cat}")
            if not isinstance(diff, int) or not (1 <= diff <= 5):
                errs.append(f"Q{n} META 难度异常 {diff}")
            if not kps:
                errs.append(f"Q{n} META 知识点为空")
    status = "PASS" if not errs else "FAIL"
    if errs:
        ok_all = False
    print(f"{pfx}: {len(items)} 题 {total} 分 [{status}]  flags={len(flags)}")
    for e in errs[:12]:
        print("   -", e)
    for f in flags[:8]:
        print("   ·", f)
print("CHECK", "ALL OK" if ok_all else "HAS FAIL")
sys.exit(0 if ok_all else 1)
