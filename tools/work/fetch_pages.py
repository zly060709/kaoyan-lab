# -*- coding: utf-8 -*-
"""从线上 Pages 把影像清单声明的页文件补到本机工作副本。

本仓工作副本是稀疏物化：影像只登记在 `data/meta/source_pdfs.json`，PNG/JPG 本体不在本机，
所以本地浏览器测影像页会稳定 404，转录管线也读不到图。转录某一卷前先跑本脚本把那一卷补齐。

只写 `data/**/*.png|jpg` 下清单已声明的路径（清单是唯一允许的下载来源，不接受任意 URL），
逐个用线上返回内容写入，写完按清单页数核对数量。用法：
  python -I -X utf8 tools/work/fetch_pages.py math1.pages 2009 2010 2011 2012
"""
import io
import json
import os
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE = "https://zly060709.github.io/kaoyan-lab/"
MANIFEST = os.path.join(ROOT, "data", "meta", "source_pdfs.json")


def main():
    prefix = sys.argv[1]
    years = sys.argv[2:]
    manifest = json.load(io.open(MANIFEST, encoding="utf-8"))
    todo = []
    for y in years:
        info = manifest.get("%s:%s" % (prefix, y))
        if not info:
            print("[跳过] 清单没有 %s:%s" % (prefix, y))
            continue
        todo += info.get("page_files") or []
    if not todo:
        print("没有要取的文件")
        return
    got, bad = 0, []
    for rel in todo:
        dest = os.path.join(ROOT, rel.replace("/", os.sep))
        if os.path.exists(dest) and os.path.getsize(dest) > 0:
            got += 1
            continue
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        try:
            blob = urllib.request.urlopen(BASE + rel, timeout=120).read()
        except Exception as e:
            bad.append("%s: %s" % (rel, e))
            continue
        if not blob:
            bad.append(rel + ": 返回空")
            continue
        with open(dest, "wb") as f:
            f.write(blob)
        got += 1
        print("  %s  %dKB" % (rel, len(blob) // 1024))
    print("清单声明 %d 页，本机现有 %d 页，失败 %d" % (len(todo), got, len(bad)))
    for b in bad:
        print("   [失败] " + b)
    if bad:
        sys.exit(1)


if __name__ == "__main__":
    main()
