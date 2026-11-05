# -*- coding: utf-8 -*-
"""数学卷公式显示层修复（一次性）：
  1. 手工修复 math3-2010-13 题干「，则」被并入 $ 公式跨度的转录粘连；
  2. 对 data/{math,math2,math3} 的 stem / options / source_blocks[].text 内
     $...$（含 $$...$$）跨度里裸露的中日韩文字与全角标点包上 \\text{...}，
     使 KaTeX math 模式不再报 Unicode 错（渲染结果与原卷阅读顺序一致，不改数学内容）；
  3. 被编辑题目重算 content_hash：
     - data/math/2013-2023（extract_math 家族）：{stem,options,blocks[role,label,text]} 裸 hex；
     - 其余数学文件（build_math_batch 家族口径，同 finalize_questions.chash）：
       {id,year,num,type,stem,options,answer,score,blocks[role,origin,text]} 前缀 sha256:；
     - data/math2/2009-2021 旧哈希本就不可复现，全文件规范化到 chash 口径（备注见 notes）。
运行后需重跑 tools/audit_math.py、tools/build_index.py、tools/gates.py。
"""
import glob, hashlib, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOG = []

TEXT_RE = re.compile(r"\\text\{[^{}]*\}")
CJK_RE = re.compile(r"([\u3000-\u303f\u3400-\u9fff\uf900-\ufaff\uff01-\uff65\u2018-\u201d]+)")

def wrap_span(seg):
    prot = {}
    def _p(m):
        k = f"\x00{len(prot)}\x00"; prot[k] = m.group(0); return k
    s = TEXT_RE.sub(_p, seg)
    s = CJK_RE.sub(lambda m: "\\text{" + m.group(1) + "}", s)
    for k, v in prot.items():
        s = s.replace(k, v)
    return s

def wrap_dollars(text):
    """处理一个字段字符串：$...$ / $$...$$ 跨度内包 \\text，返回 (新串, 是否变化)"""
    out, i, n, changed = [], 0, len(text), False
    while i < n:
        if text.startswith("$$", i):
            j = text.find("$$", i + 2)
            if j > 0:
                seg = text[i + 2:j]
                ns = wrap_span(seg)
                if ns != seg: changed = True
                out.append("$$" + ns + "$$"); i = j + 2; continue
            out.append("$$"); i += 2; continue
        if text[i] == "$":
            j = text.find("$", i + 1)
            if j > 0:
                seg = text[i + 1:j]
                ns = wrap_span(seg)
                if ns != seg: changed = True
                out.append("$" + ns + "$"); i = j + 1; continue
            out.append("$"); i += 1; continue
        out.append(text[i]); i += 1
    return "".join(out), changed

def chash_a(q):  # extract_math 家族（裸 hex）
    payload = json.dumps({"stem": q.get("stem"), "options": q.get("options"),
        "blocks": [{"role": b["role"], "label": b.get("label"), "text": b["text"]}
                   for b in q.get("source_blocks", [])]},
        ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()

def chash_b(q):  # finalize_questions / build_math_batch 家族
    core = {k: q.get(k) for k in ("id", "year", "num", "type", "stem", "options", "answer", "score") if k in q}
    for b in q.get("source_blocks", []):
        core.setdefault("blocks", []).append({"role": b.get("role"), "origin": b.get("origin"), "text": b.get("text")})
    return "sha256:" + hashlib.sha256(json.dumps(core, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()

def scheme_for(subj, year):
    if subj == "math" and 2013 <= year <= 2023:
        return chash_a
    return chash_b

def q_edit(q, field, old, new, scheme):
    q[field] = new
    q["content_hash"] = scheme(q)
    LOG.append(f"{q['id']} {field}: {old[:60]!r} -> {new[:60]!r}")

def main():
    manual = [
        # 转录粘连：原卷「公式，则 公式」，把「，则」移出公式跨度
        ("data/math3/2010.json", 13, "stem",
         "$|A|=3,|B|=2,|A^{-1}+B|=2,，则 $", "$|A|=3,|B|=2,|A^{-1}+B|=2$，则 $"),
    ]
    files = []
    for dd in ("math", "math2", "math3"):
        files += [f for f in sorted(glob.glob(os.path.join(ROOT, "data", dd, "[12]*.json")))
                  if re.match(r"^\d{4}\.json$", os.path.basename(f))]
    nq = nfix = 0
    for fp in files:
        rel = os.path.relpath(fp, ROOT).replace("\\", "/")
        subj = os.path.basename(os.path.dirname(fp))
        year = int(os.path.basename(fp)[:4])
        d = json.load(open(fp, encoding="utf-8"))
        scheme = scheme_for(subj, year)
        normalize = (subj == "math2" and year <= 2021)  # 旧哈希不可复现 → 全文件规范化
        fchg = 0
        for q in d.get("questions", []):
            nq += 1
            pre = [m for m in manual if m[0] == rel and m[1] == q.get("num")]
            edited = False
            for _, _, field, old, new in pre:
                if field in q and old in q[field]:
                    q[field] = q[field].replace(old, new, 1)
                    LOG.append(f"{q['id']} {field}: 手工移出「，则」")
                    edited = True
            for field in ("stem",):
                v = q.get(field)
                if isinstance(v, str) and "$" in v:
                    nv, ch = wrap_dollars(v)
                    if ch:
                        q[field] = nv; edited = True
                        LOG.append(f"{q['id']} {field}: \\text 包裹")
            for o in (q.get("options") or []):
                if isinstance(o, str) and "$" in o:
                    nv, ch = wrap_dollars(o)
                    if ch:
                        opts = q["options"]; opts[opts.index(o)] = nv; edited = True
                        LOG.append(f"{q['id']} options: \\text 包裹")
            for b in (q.get("source_blocks") or []):
                v = b.get("text")
                if isinstance(v, str) and "$" in v:
                    nv, ch = wrap_dollars(v)
                    if ch:
                        b["text"] = nv; edited = True
                        LOG.append(f"{q['id']} block[{b.get('role')}]: \\text 包裹")
            if edited or normalize:
                q["content_hash"] = scheme(q)
                fchg += 1
                nfix += 1
        if fchg:
            tmp = fp + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(d, f, ensure_ascii=False, indent=1)
            os.replace(tmp, fp)
            print(f"{rel}: 编辑/规范化 {fchg} 题")
    print(f"共扫描 {nq} 题，编辑/规范化 {nfix} 题")
    with open(os.path.join(ROOT, "tools", "work", "fix_math_cjk_notes.md"), "w", encoding="utf-8") as f:
        f.write("# 数学卷公式显示层修复（\\text 包裹）变更清单\n\n"
                "口径：只把 $…$ 跨度内裸露的中日韩文字/全角标点包进 \\text{}，"
                "渲染结果与原卷阅读顺序一致，不改数学内容；被编辑题 content_hash 按各文件构建家族算法重算；"
                "data/math2/2009-2021 旧哈希本就不可复现，全文件规范化到 finalize_questions.chash 口径。\n\n")
        for line in LOG:
            f.write(f"- {line}\n")
    print("notes -> tools/work/fix_math_cjk_notes.md")

if __name__ == "__main__":
    main()
