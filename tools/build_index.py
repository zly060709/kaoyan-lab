# -*- coding: utf-8 -*-
"""构建跨科搜索索引 v2：data/index/{sid}.json（按科合并，>480KB 自动切 parts 子片）。

旧版按年 91 个分片，前端一次搜索要全量拉 100 个请求；v2 每科最多 1 个指针 +
2~3 个子片，前端逐科增量出结果。幂等：可重复运行；subjects.json 为科目清单来源。
用法: python -I -X utf8 tools/build_index.py
"""
import glob, json, os, re, sys, datetime

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, "data", "meta", "subjects.json")
reg = json.load(open(REG, encoding="utf-8"))
SNIP = 600
MAX_BYTES = 480 * 1024  # 留出余量，门禁红线是 500KB

def norm(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    s = re.sub(r"@@M:[-\w]+:\d+@@", " ", s)  # 图片占位符不进搜索文本，否则命中行印出裸 @@M:…@@
    return re.sub(r"\s+", " ", s).strip()

MATH_SIDS = {"math1", "math2", "math3", "mgt199"}

def conv_dollars(s):
    """数学类科目：把 $...$ / $$...$$ 转成 \\(...\\) / \\[...\\]，
    搜索结果页统一用 safe 模式渲染（单个 $ 保持字面），公式仍可渲染、货币符号不误判。"""
    out, i, n = [], 0, len(s)
    while i < n:
        if s.startswith("$$", i):
            j = s.find("$$", i + 2)
            if j > 0:
                out.append("\\[" + s[i + 2:j] + "\\]"); i = j + 2; continue
            out.append("$$"); i += 2; continue
        if s[i] == "$":
            j = s.find("$", i + 1)
            if j > 0:
                out.append("\\(" + s[i + 1:j] + "\\)"); i = j + 1; continue
            out.append("$"); i += 1; continue
        out.append(s[i]); i += 1
    return "".join(out)

def dump(path, obj):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, separators=(",", ":"))
    os.replace(tmp, path)

total = 0
for s in reg["subjects"]:
    sid, dd = s["id"], s.get("dataDir") or s["id"]
    files = sorted(glob.glob(os.path.join(ROOT, "data", dd, "[12]*.json")))
    files = [f for f in files if re.match(r"^\d{4}\.json$", os.path.basename(f))]
    if not files:
        continue
    entries = []
    for fp in files:
        try:
            d = json.load(open(fp, encoding="utf-8"))
        except Exception:
            continue
        year = d.get("year") or int(os.path.basename(fp)[:4])
        for q in d.get("questions", []):
            text_parts = [norm(q.get("stem"))]
            for o in (q.get("options") or [])[:6]:
                text_parts.append(norm(o if isinstance(o, str) else json.dumps(o, ensure_ascii=False)))
            for b in (q.get("source_blocks") or []):
                t = norm(b.get("text"))
                if t:
                    text_parts.append(t[:SNIP])
            text = " ".join(p for p in text_parts if p)[:1800]
            title = norm(q.get("title") or q.get("stem"))[:80]
            if sid in MATH_SIDS:
                text = conv_dollars(text)
                title = conv_dollars(title)
            entries.append({
                "id": q.get("id"), "sid": sid, "year": year, "num": q.get("num"),
                "type": q.get("type"), "title": title,
                "tags": (q.get("tags") or [])[:4], "text": text,
            })
    if not entries:
        continue
    # 单科合并 → 超 480KB 切 parts（保序均分，子片 {sid}.{n}.json）
    payload = json.dumps({"sid": sid, "count": len(entries), "entries": entries},
                         ensure_ascii=False, separators=(",", ":"))
    index_dir = os.path.join(ROOT, "data", "index")
    os.makedirs(index_dir, exist_ok=True)
    # 清掉该科旧文件（旧版按年分片 + manifest）
    for old in glob.glob(os.path.join(index_dir, sid + ".*.json")) + \
               glob.glob(os.path.join(index_dir, sid, "*.json")) + \
               [os.path.join(index_dir, f"{sid}.manifest.json")]:
        try:
            os.remove(old)
        except OSError:
            pass
    old_dir = os.path.join(index_dir, sid)
    if os.path.isdir(old_dir):
        try:
            os.rmdir(old_dir)
        except OSError:
            pass
    if len(payload.encode("utf-8")) <= MAX_BYTES:
        dump(os.path.join(index_dir, f"{sid}.json"), json.loads(payload))
        print(f"  {sid}.json: {len(entries)} 条 {len(payload.encode('utf-8'))//1024}KB 单文件")
    else:
        # 按条数均分成 N 片，每片重算体积直到全部 ≤ MAX_BYTES
        n = 2
        while True:
            per = (len(entries) + n - 1) // n
            chunks = [entries[i * per:(i + 1) * per] for i in range(n)]
            chunks = [c for c in chunks if c]
            sizes = [len(json.dumps({"sid": sid, "count": len(c), "entries": c},
                                    ensure_ascii=False, separators=(",", ":")).encode("utf-8")) for c in chunks]
            if max(sizes) <= MAX_BYTES:
                break
            n += 1
        parts = [f"{sid}.{i + 2}.json" for i in range(len(chunks))]
        dump(os.path.join(index_dir, f"{sid}.json"),
             {"sid": sid, "count": len(entries), "parts": parts})
        for name, chunk, size in zip(parts, chunks, sizes):
            dump(os.path.join(index_dir, name), {"sid": sid, "count": len(chunk), "entries": chunk})
            print(f"  {name}: {len(chunk)} 条 {size // 1024}KB")
        print(f"  {sid}.json: 指针 {len(entries)} 条 → {len(parts)} 片")
    total += len(entries)

print(f"index total: {total} 条")
