# -*- coding: utf-8 -*-
"""从原卷页面影像裁出数学三各卷的原图，写成 data/math3/{年}.media.json
（base64 data URI，与 cs408 的 media 分片同格式；题干/解析以 @@M:<媒体 id>:<idx>@@ 引用）。

坐标来自 1075×1521 页面影像上的 50/100px 网格叠加复核（2026-11-05 主会话逐幅裁图核对）。
只裁不画：不重绘、不派生、不改变像素内容。
用法：python tools/work/build_m3media.py [年份 ...]（缺省处理下表全部年份）
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
        ("math3-2009-4", "p1", 330, 765, 705, 1050, "题干 y=f(x) 图形"),
        ("math3-2009-4", "p1", 195, 1065, 520, 1325, "选项（A）F(x) 图形"),
        ("math3-2009-4", "p1", 550, 1065, 890, 1325, "选项（B）F(x) 图形"),
        ("math3-2009-4", "p2", 195, 90, 520, 345, "选项（C）F(x) 图形"),
        ("math3-2009-4", "p2", 550, 90, 895, 385, "选项（D）F(x) 图形"),
    ],
    2015: [
        ("math3-2015-2", "p1", 678, 243, 948, 412, "题干 y=f''(x) 图形（x=1、x=2 处有虚线）"),
    ],
    2016: [
        ("math3-2016-1", "p1", 700, 350, 935, 582, "题干 y=f'(x) 图形"),
        ("math3-2016-1", "p5", 222, 515, 660, 880, "解析标记图（x1…x5）"),
        ("math3-2016-3", "p6", 160, 340, 355, 515, "区域图（1）D11/D12"),
        ("math3-2016-3", "p6", 370, 340, 585, 515, "区域图（2）D21/D22/D23"),
        ("math3-2016-3", "p6", 600, 340, 815, 515, "区域图（3）D33/D31/D32"),
    ],
    2018: [
        ("math3-2018-16", "p10", 146, 370, 338, 516, "第 16 题解析的阴影积分区域图"),
    ],
}


def build(year):
    pages = os.path.join(ROOT, "data", "math3", "pages", str(year))
    out = os.path.join(ROOT, "data", "math3", "%d.media.json" % year)
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
    doc = {"subject": "math3", "year": year,
           "source_note": "原卷 data/math3/pages/%d/%s 影像的对应图形区域直接裁切，未重绘、未派生。"
                          % (year, "、".join(sorted(used))),
           "items": items}
    json.dump(doc, io.open(out, "w", encoding="utf-8"), ensure_ascii=False)
    n = sum(len(v) for v in items.values())
    print("写出 %s %d 幅 %dKB" % (out, n, os.path.getsize(out) // 1024))


if __name__ == "__main__":
    for y in [int(a) for a in sys.argv[1:]] or sorted(MEDIA):
        build(y)
