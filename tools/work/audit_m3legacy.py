# -*- coding: utf-8 -*-
"""数三 2009–2020 入库后的内容审计（不看原图也能拦住的错误）：
A1 结构：选择 8 / 填空 6 / 解答 9，分值 4/4/推定，合计 150
A2 answer 字段与解析块首行【答案】（X）逐题一致
A3 选择题恰 4 个选项、填空与解答不给选项
A4 解析块非空、含【答案】或【解析】/【详解】标记
A5 题干/选项里仍有【图】等未接图的占位 -> 登记为缺口
A6 与数学一/数学二同年份同题干的答案交叉核对
用法：python tools/work/audit_m3legacy.py [2019 ...]
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = lambda *p: os.path.join(ROOT, "data", *p)
TYPES = {"single": 8, "blank": 6, "essay": 9}


def load(subject, year):
    p = D(subject, f"{year}.json")
    return json.load(io.open(p, encoding="utf-8"))["questions"] if os.path.exists(p) else []


def norm_stem(s):
    s = re.sub(r"\s+", "", str(s or ""))
    s = re.sub(r"\\(?:mathrm|text|displaystyle|limits|,|;|！)", "", s)
    s = re.sub(r"\\[a-zA-Z]+", "", s)
    return re.sub(r"[，。．.；;：:（）()\[\]{}$]", "", s).lower()


def norm_ans(s):
    s = re.sub(r"\s+", "", str(s or ""))
    for x in ("$", "\\,", "\\!", "\\ "):
        s = s.replace(x, "")
    s = re.sub(r"[，。．.；;：:（）()\[\]{}｜|]", "", s)
    return s.replace("\\", "").lower()


def audit(year):
    qs = load("math3", year)
    out = []
    if not qs:
        return ["无数据文件"]
    from collections import Counter
    c = Counter(q["type"] for q in qs)
    if dict(c) != TYPES:
        out.append(f"A1 结构 {dict(c)}")
    if sum(q["score"] for q in qs) != 150:
        out.append(f"A1 分值合计 {sum(q['score'] for q in qs)}")
    for q in qs:
        blk = "\n".join(b["text"] for b in q["source_blocks"])
        if q["type"] == "single" and len(q["options"]) != 4:
            out.append(f"A3 {q['id']} 选项 {len(q['options'])} 个")
        if q["type"] != "single" and q["options"]:
            out.append(f"A3 {q['id']} 非选择题带选项")
        if len(blk.strip()) < 8:
            out.append(f"A4 {q['id']} 解析过短")
        if not re.search(r"【(答案|解析|详解|证明)】", blk):
            out.append(f"A4 {q['id']} 解析无【答案】/【解析】标记")
        m = re.search(r"【答案】\s*[（(]\s*([A-D])", blk)
        if m and q["type"] == "single" and m.group(1) != (q["answer"] or "").strip():
            out.append(f"A2 {q['id']} 字段 {q['answer']!r} vs 解析 {m.group(1)}")
        if "【图】" in q["stem"] or any("【图】" in o for o in q["options"]):
            out.append(f"A5 {q['id']} 题干/选项含【图】占位（原图未接入）")
    for other in ("math1", "math2"):
        for oq in load(other, year):
            key = norm_stem(oq["stem"])
            if len(key) < 40:
                continue
            for q in qs:
                if norm_stem(q["stem"]) == key:
                    tag = "一致" if norm_ans(oq["answer"]) == norm_ans(q["answer"]) else "!!! 不一致"
                    out.append(f"A6 同题 {other}-{year}-{oq['num']} ~ math3-{year}-{q['num']} {tag}")
    return out


if __name__ == "__main__":
    years = [int(a) for a in sys.argv[1:]] or list(range(2009, 2020))
    bad = 0
    for y in years:
        allr = audit(y)
        cross = [x for x in allr if x.startswith("A6 同题")]
        r = [x for x in allr if not x.startswith("A6 同题")] + [x for x in cross if "!!!" in x]
        bad += len(r)
        print(f"{y}: {'PASS' if not r else str(len(r)) + ' 项待处理'}{'  同题交叉 %d 组' % len(cross) if cross else ''}")
        for x in r[:8]:
            print("   ", x)
    print("非交叉问题合计", bad)
