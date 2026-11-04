# -*- coding: utf-8 -*-
"""数学真题 PDF → 逐页灰度 PNG 影像 + 源清单（保真基线）。
用法: python -I -X utf8 tools/render_math_pages.py [politics|english] (可选: 同时渲染其他科)
输出: data/math1.pages/pages/{year}/p{n}.png 等 + data/meta/source_pdfs.json"""
import hashlib, json, os, sys
import pymupdf

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_BASE = r"D:/桌面/学科历年真题/学科历年真题"

GROUPS = [
    ("math1.pages", os.path.join(SRC_BASE, "数学真题试卷电子版", "数一09-23真题pdf"), ["2009", "2010", "2011", "2012"]),
    ("math2", os.path.join(SRC_BASE, "数学真题试卷电子版", "数二09-23真题pdf"), None),
    ("math3", os.path.join(SRC_BASE, "数学真题试卷电子版", "数三09-23真题pdf"), None),
]

def year_of(name):
    for y in range(1998, 2027):
        if str(y) in name:
            return y
    return None

manifest = {}
mpath = os.path.join(ROOT, "data", "meta", "source_pdfs.json")
if os.path.exists(mpath):
    try:
        manifest = json.load(open(mpath, encoding="utf-8"))
    except Exception:
        manifest = {}

for out_id, folder, only_years in GROUPS:
    files = sorted(os.listdir(folder))
    for fn in files:
        if not fn.lower().endswith(".pdf"):
            continue
        y = year_of(fn)
        if y is None or (only_years and str(y) not in only_years):
            continue
        p = os.path.join(folder, fn)
        sha = hashlib.sha256(open(p, "rb").read()).hexdigest()
        doc = pymupdf.open(p)
        outd = os.path.join(ROOT, "data", out_id, "pages", str(y))
        os.makedirs(outd, exist_ok=True)
        pages = []
        for i in range(doc.page_count):
            out = os.path.join(outd, f"p{i+1}.png")
            if not os.path.exists(out):  # 幂等：已渲染跳过
                pix = doc[i].get_pixmap(dpi=130, colorspace=pymupdf.csGRAY)
                pix.save(out)
            pages.append(f"data/{out_id}/pages/{y}/p{i+1}.png")
        key = f"{out_id}:{y}"
        manifest[key] = {"pdf": fn, "sha256": sha, "pages": doc.page_count, "page_files": pages}
        print(f"{out_id} {y}: {doc.page_count} 页 -> {outd}")
        doc.close()

os.makedirs(os.path.join(ROOT, "data", "meta"), exist_ok=True)
json.dump(manifest, open(mpath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"manifest entries: {len(manifest)} -> data/meta/source_pdfs.json")
