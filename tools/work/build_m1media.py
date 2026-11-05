# -*- coding: utf-8 -*-
"""从原卷页面影像裁出数学一各卷的原图，写成 data/math/{年}.media.json
（base64 data URI，与 math3 / cs408 的 media 分片同格式；题干/选项以 @@M:<媒体 id>:<idx>@@ 引用）。

坐标来自 1075×1521 页面影像（复核裁图 tools/work/m12009_crops/）。只裁不画：不重绘、不派生。
用法：python -I -X utf8 tools/work/build_m1media.py [年份 ...]（缺省处理下表全部年份）
"""
import base64
import io
import json
import os
import sys

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 年份 -> (媒体 id, 页码, 左, 上, 右, 下, 说明)；同一媒体 id 内的顺序即 @@M:<id>:<idx>@@
MEDIA = {
    2009: [
        ("math1-2009-2", "p1", 420, 630, 730, 880, "第(2)题 正方形对角线分区图（D1~D4）"),
        ("math1-2009-3", "p1", 340, 920, 720, 1200, "第(3)题 题干 y=f(x) 图形"),
        ("math1-2009-3", "p2", 155, 145, 540, 400, "第(3)题 选项（A）F(x) 图形"),
        ("math1-2009-3", "p2", 540, 145, 905, 400, "第(3)题 选项（B）F(x) 图形"),
        ("math1-2009-3", "p2", 155, 465, 540, 710, "第(3)题 选项（C）F(x) 图形"),
        ("math1-2009-3", "p2", 540, 465, 905, 710, "第(3)题 选项（D）F(x) 图形"),
    ],
}


def build(year):
    pages = os.path.join(ROOT, "data", "math1.pages", "pages", str(year))
    out = os.path.join(ROOT, "data", "math", "%d.media.json" % year)
    items, used = {}, {}
    for mid, pg, l, t, r, b, desc in MEDIA[year]:
        im = Image.open(os.path.join(pages, "%s.png" % pg)).convert("RGB").crop((l, t, r, b))
        buf = io.BytesIO()
        im.save(buf, format="PNG", optimize=True)
        idx = len(items.setdefault(mid, {}))
        items[mid][str(idx)] = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()
        used.setdefault(pg, []).append(mid)
        print("  %s:%d %s %d×%d %dKB  %s" % (mid, idx, pg, im.width, im.height,
                                             len(buf.getvalue()) // 1024, desc))
    doc = {"subject": "math", "year": year,
           "source_note": "原卷 data/math1.pages/pages/%d/%s 影像的对应图形区域直接裁切，未重绘、未派生。"
                          % (year, "、".join(sorted(used))),
           "items": items}
    json.dump(doc, io.open(out, "w", encoding="utf-8"), ensure_ascii=False)
    print("写出", os.path.relpath(out, ROOT), len(items), "个媒体 id")


for arg in sys.argv[1:]:
    build(int(arg))
if len(sys.argv) <= 1:
    for y in MEDIA:
        build(y)
