# -*- coding: utf-8 -*-
"""数据分片体积门禁：把超过 500KB 的 data/**/*.json 切成 parts 子文件。

原文件改写为指针 {parts: [...]}，内容零丢失；前端 fetchShard() 按 parts 合并。
用法: python -I -X utf8 tools/split_shards.py [--check]
"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIMIT = 500 * 1024
TARGET = 430 * 1024  # 留出余量，避免序列化差异顶破上限
PART_RE = re.compile(r"\.p\d+\.json$")


def dump(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))


def atomic_write(path, text):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, path)


def chunks_of(items, size_of, base_meta):
    """按累计体积切分条目，返回若干完整载荷对象。"""
    out, cur, cur_size = [], {}, len(dump(base_meta))
    for key, val in items:
        v = size_of(key, val)
        if cur and cur_size + v > TARGET:
            out.append((cur, cur_size))
            cur, cur_size = {}, len(dump(base_meta))
        cur[key] = val
        cur_size += v
    if cur:
        out.append((cur, cur_size))
    return out


def split_media(path, rel):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    items = data.get("items") or {}
    base = {"subject": data.get("subject"), "year": data.get("year")}
    groups = chunks_of(
        list(items.items()),
        lambda k, v: len(dump({k: v})) - 2,
        base,
    )
    names = []
    for i, (part_items, _) in enumerate(groups, 1):
        name = "%s.p%d.json" % (os.path.basename(path)[:-5], i)
        payload = dict(base)
        payload["items"] = part_items
        atomic_write(os.path.join(os.path.dirname(path), name), dump(payload))
        names.append(name)
    pointer = dict(base)
    pointer["parts"] = names
    pointer["items"] = {}
    atomic_write(path, dump(pointer))
    return len(names)


def split_analysis(path, rel):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    entries = data.get("analysis") or []
    base = {"subject": data.get("subject"), "year": data.get("year")}
    groups = chunks_of(
        list(enumerate(entries)),
        lambda k, v: len(dump(v)),
        base,
    )
    names = []
    for i, (part_entries, _) in enumerate(groups, 1):
        name = "%s.p%d.json" % (os.path.basename(path)[:-5], i)
        payload = dict(base)
        payload["analysis"] = list(part_entries.values())
        atomic_write(os.path.join(os.path.dirname(path), name), dump(payload))
        names.append(name)
    pointer = dict(base)
    pointer["count"] = data.get("count", len(entries))
    pointer["parts"] = names
    pointer["analysis"] = []
    atomic_write(path, dump(pointer))
    return len(names)


def main():
    check_only = "--check" in sys.argv
    oversized = []
    for dirpath, dirnames, filenames in os.walk(os.path.join(ROOT, "data")):
        dirnames.sort()
        for fn in sorted(filenames):
            if not fn.endswith(".json") or PART_RE.search(fn):
                continue
            p = os.path.join(dirpath, fn)
            if os.path.getsize(p) > LIMIT:
                oversized.append((p, os.path.getsize(p)))
    if not oversized:
        print("全部分片 <= 500KB，无需处理")
        return 0
    for p, size in oversized:
        rel = os.path.relpath(p, ROOT).replace("\\", "/")
        if check_only:
            print("OVER %7d B  %s" % (size, rel))
            continue
        with open(p, encoding="utf-8") as f:
            head = json.load(f)
        if isinstance(head, dict) and "items" in head:
            n = split_media(p, rel)
        elif isinstance(head, dict) and "analysis" in head:
            n = split_analysis(p, rel)
        else:
            print("SKIP 无法识别结构 %s（需人工分片）" % rel)
            continue
        print("SPLIT %-40s -> %d parts" % (rel, n))
    return 1 if check_only else 0


if __name__ == "__main__":
    raise SystemExit(main())
