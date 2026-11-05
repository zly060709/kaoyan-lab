# -*- coding: utf-8 -*-
"""校验 data/meta/source_pdfs.json 声明的原卷页影像是否真的在仓库里。

只在 CI（全量检出）判定真伪：本机会作副本可能是稀疏物化，本地缺文件不等于仓库缺，
所以本地跑出「缺」只打印、不据此删清单。用法：
  python -X utf8 tools/verify_pages.py            # 缺文件即退出码 1（CI 用）
  python -X utf8 tools/verify_pages.py --report   # 只报告，不改退出码语义以外的东西
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "meta", "source_pdfs.json")


def main():
    report_only = "--report" in sys.argv[1:]
    manifest = json.load(open(SRC, encoding="utf-8"))
    missing, total = [], 0
    for key, info in sorted(manifest.items()):
        files = info.get("page_files") or []
        declared = len(files) or int(info.get("pages") or 0)
        total += declared
        miss = [f for f in files if not os.path.exists(os.path.join(ROOT, f.replace("\\", "/")))]
        if miss:
            missing.append((key, len(miss), len(files), int(info.get("pages") or 0)))
    print("影像声明 %d 页，清单条目 %d 个" % (total, len(manifest)))
    if missing:
        print("本机缺失 %d 个条目，共 %d 页：" % (len(missing), sum(m[1] for m in missing)))
        for key, nm, nf, npages in missing[:12]:
            note = "" if nf == npages else "（清单页数 %d ≠ 文件数 %d）" % (npages, nf)
            print("   %s: 缺 %d/%d 页%s" % (key, nm, nf, note))
        if len(missing) > 12:
            print("   ...另 %d 个条目" % (len(missing) - 12))
        print("提示：本地缺文件不代表仓库缺——工作副本可能是稀疏物化。判定以 CI 的全量检出为准，"
              "不要据此删减 source_pdfs.json。")
    else:
        print("全部声明的影像页都在磁盘上 [PASS]")
    if missing and not report_only:
        sys.exit(1)


if __name__ == "__main__":
    main()
