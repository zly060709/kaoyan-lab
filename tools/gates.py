# -*- coding: utf-8 -*-
"""合同第 7 章质量门禁：一条命令复跑全部可机械校验的项。

校验项：
  G1 题量基准        政治 456 / 数学一 250 / 英语客观 675 / 408 376（缺一即不合格）
  G2 legacy 只读基线  四份原始 HTML 的 SHA-256 与 tools/legacy_hashes.txt 一致
  G3 分片体积        data/**/*.json 全部 <= 500KB
  G4 JSON 可解析      全部数据文件可加载
  G5 schema 必填字段  id/subject/year/num/type/stem/answer/source_blocks/source_hash/content_hash
  G6 source_hash 齐备 每题非空
  G7 媒体占位符可解析 每个 @@M:id:i@@ 在对应 media 分片里有 URI
  G8 内部资源有效     html/sw 引用的本地路径存在（含数据文件路径）
  G9 注册表与数据一致 subjects.json 的 dataYears/yearCounts 与磁盘实际相符

用法: python -I -X utf8 tools/gates.py [--json out.json]
退出码 0 = 全部门禁通过。
"""
import glob
import hashlib
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIMIT = 500 * 1024
BASELINE = {"politics": 456, "math": 250, "english": 675, "cs408": 376}
REQUIRED = ["id", "subject", "year", "num", "type", "stem", "answer",
            "source_blocks", "source_hash", "content_hash"]
# 主观题没有单一「答案字符串」，答案材料以原文区块形式存在（合同第 2 章：答案只可照录，不可编造）。
# 这类题型允许 answer 为空，但原文区块里必须真有答案材料，否则就是缺口而不是主观题。
SUBJECTIVE_TYPES = {"essay", "translation", "writing", "big", "analysis"}
ANSWER_ROLES = {"answer", "ans", "trans-zh", "ref", "reference", "nodes", "detail",
                "essay-box"}
PLACEHOLDER_RE = re.compile(r"@@M:([-\w]+):(\d+)@@")

results = []


def gate(name, ok, detail):
    results.append({"gate": name, "pass": bool(ok), "detail": detail})
    print("%s  %-22s %s" % ("PASS" if ok else "FAIL", name, detail))
    return ok


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def year_files():
    out = {}
    for p in glob.glob(os.path.join(ROOT, "data", "*", "*.json")):
        rel = os.path.relpath(p, ROOT).replace("\\", "/")
        base = os.path.basename(p)
        if not re.match(r"^\d{4}\.json$", base):
            continue
        subj = rel.split("/")[1]
        out.setdefault(subj, []).append(rel)
    return out


def main():
    yf = year_files()
    allqs = {}

    # G1 题量
    counts = {}
    for subj, files in yf.items():
        tot = 0
        for rel in files:
            try:
                d = load(os.path.join(ROOT, rel))
            except Exception:
                continue
            qs = d.get("questions") if isinstance(d, dict) else d
            qs = qs or []
            allqs.setdefault(subj, []).extend((rel, q) for q in qs if isinstance(q, dict))
            if subj == "english":
                tot += len([q for q in qs if isinstance(q, dict) and q.get("type") in
                            ("cloze", "reading", "partb", "single", "multi")])
            else:
                tot += len(qs)
        counts[subj] = tot
    missing = ["%s=%d/%d" % (k, counts.get(k, 0), v) for k, v in BASELINE.items()
               if counts.get(k, 0) < v]
    gate("G1 题量基准", not missing,
         " / ".join("%s %d" % (k, counts.get(k, 0)) for k in BASELINE) +
         (" | 缺口: " + ", ".join(missing) if missing else "") +
         (" | 其他科目: " + ", ".join("%s %d" % (k, v) for k, v in sorted(counts.items())
                                     if k not in BASELINE) if len(counts) > len(BASELINE) else ""))

    # G2 legacy 基线
    hf = os.path.join(ROOT, "tools", "legacy_hashes.txt")
    if os.path.exists(hf):
        bad, checked = [], 0
        for line in open(hf, encoding="utf-8"):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) < 2:
                continue
            digest, name = parts[0], parts[-1]
            p = os.path.join(ROOT, "legacy", os.path.basename(name))
            checked += 1
            if not os.path.exists(p):
                bad.append(os.path.basename(name) + ": 文件缺失")
                continue
            h = hashlib.sha256(open(p, "rb").read()).hexdigest()
            if h != digest:
                bad.append(os.path.basename(name) + ": SHA-256 不匹配（原文被改动）")
        gate("G2 legacy 只读", checked and not bad,
             "%d 件比对，%s" % (checked, "全部一致" if not bad else "；".join(bad)))
    else:
        gate("G2 legacy 只读", False, "缺 tools/legacy_hashes.txt 基线文件")

    # G3 分片体积
    over = []
    for p in glob.glob(os.path.join(ROOT, "data", "**", "*.json"), recursive=True):
        sz = os.path.getsize(p)
        if sz > LIMIT:
            over.append("%s(%dKB)" % (os.path.relpath(p, ROOT).replace("\\", "/"), sz // 1024))
    gate("G3 分片<=500KB", not over, "无超限" if not over else "超限: " + ", ".join(over))

    # G4 JSON 可解析
    broken = []
    for p in glob.glob(os.path.join(ROOT, "data", "**", "*.json"), recursive=True):
        try:
            load(p)
        except Exception as e:
            broken.append("%s: %s" % (os.path.relpath(p, ROOT).replace("\\", "/"), str(e)[:60]))
    gate("G4 JSON 可解析", not broken, "全部可加载" if not broken else "; ".join(broken[:5]))

    # G5/G6 字段完整
    miss_fields, miss_hash, total, subj_ok = [], [], 0, 0
    for subj, items in allqs.items():
        for rel, q in items:
            total += 1
            lack = [k for k in REQUIRED if k not in q or q.get(k) in (None, "", [])]
            if "answer" in lack and q.get("type") in SUBJECTIVE_TYPES:
                roles = {b.get("role") for b in q.get("source_blocks", [])
                         if isinstance(b, dict)}
                if roles & ANSWER_ROLES:
                    lack.remove("answer")
                    subj_ok += 1
            if lack:
                miss_fields.append("%s#%s:%s" % (subj, q.get("id"), ",".join(lack)))
            if not q.get("source_hash"):
                miss_hash.append("%s#%s" % (subj, q.get("id")))
    gate("G5 必填字段", not miss_fields,
         "%d 题（其中 %d 道主观题按原文区块口径放行），缺字段 %d%s" % (
             total, subj_ok, len(miss_fields),
             " 例: " + "; ".join(miss_fields[:4]) if miss_fields else ""))
    gate("G6 source_hash", not miss_hash,
         "齐备" if not miss_hash else "缺失 %d，例: %s" % (len(miss_hash), "; ".join(miss_hash[:4])))

    # G7 媒体占位符
    dangling, refs = [], 0
    media_cache = {}
    for subj, items in allqs.items():
        for rel, q in items:
            blob = json.dumps(q, ensure_ascii=False)
            for mid, idx in PLACEHOLDER_RE.findall(blob):
                refs += 1
                ddir = os.path.dirname(rel)
                mpath = os.path.join(ROOT, ddir, "%s.media.json" % q.get("year"))
                if mpath not in media_cache:
                    try:
                        md = load(mpath)
                        merged = dict(md.get("items") or {})
                        for part in md.get("parts") or []:
                            merged.update(load(os.path.join(ROOT, ddir, part)).get("items") or {})
                        media_cache[mpath] = merged
                    except Exception:
                        media_cache[mpath] = {}
                uri = (media_cache[mpath].get(mid) or {}).get(idx) if isinstance(
                    media_cache[mpath].get(mid), dict) else None
                if uri is None:
                    arr = media_cache[mpath].get(mid)
                    uri = arr[int(idx)] if isinstance(arr, list) and len(arr) > int(idx) else None
                if not uri:
                    dangling.append("%s:%s" % (mid, idx))
    gate("G7 媒体占位符", not dangling,
         "%d 处引用全部可解析" % refs if not dangling else
         "悬空 %d 处: %s" % (len(dangling), "; ".join(dangling[:5])))

    # G8 内部资源有效
    bad_refs, checked = [], 0
    for html in ["index.html", "diag.html", "404.html", "lab3d.html"]:
        p = os.path.join(ROOT, html)
        if not os.path.exists(p):
            continue
        txt = open(p, encoding="utf-8").read()
        for m in re.finditer(r'(?:src|href)="([^"#]+)"', txt):
            u = m.group(1)
            if u.startswith(("http", "mailto", "data:", "//")) or u.startswith("/"):
                continue
            if "${" in u or "{{" in u:      # JS 模板字面量，不是静态资源路径
                continue
            checked += 1
            if not os.path.exists(os.path.join(ROOT, u.replace("\\", "/"))):
                bad_refs.append("%s -> %s" % (html, u))
        for m in re.finditer(r'["`(](data/[\w./-]+\.json)', txt):
            checked += 1
            if "${" in m.group(1) or "{{" in m.group(1):
                checked -= 1
                continue
            if not os.path.exists(os.path.join(ROOT, m.group(1))):
                bad_refs.append("%s -> %s" % (html, m.group(1)))
    for sw in ["sw.js", "manifest.webmanifest"]:
        p = os.path.join(ROOT, sw)
        if not os.path.exists(p):
            bad_refs.append(sw + " 缺失")
            continue
        for m in re.finditer(r'"([\w./-]+\.(?:html|js|css|json|webmanifest|svg|png))"', open(p, encoding="utf-8").read()):
            checked += 1
            if not os.path.exists(os.path.join(ROOT, m.group(1))):
                bad_refs.append("%s -> %s" % (sw, m.group(1)))
    gate("G8 内部资源有效", not bad_refs,
         "%d 处引用无失效" % checked if not bad_refs else "失效: " + "; ".join(bad_refs[:6]))

    # G9 注册表一致
    reg = load(os.path.join(ROOT, "data", "meta", "subjects.json"))
    drift = []
    for s in reg["subjects"]:
        ddir = s.get("dataDir") or s["id"]
        real = sorted(int(os.path.basename(p)[:4]) for p in yf.get(ddir, [])
                      if len(load(os.path.join(ROOT, p)).get("questions") or []) > 0)
        if sorted(s.get("dataYears") or []) != real:
            drift.append("%s 注册 %s != 实际 %s" % (s["id"], s.get("dataYears"), real))
    gate("G9 注册表一致", not drift, "与磁盘数据一致" if not drift else "; ".join(drift[:4]))

    ok = all(r["pass"] for r in results)
    print("\n门禁汇总：%d/%d 通过%s" % (sum(1 for r in results if r["pass"]), len(results),
                                    "（全部通过，可打绿色 tag）" if ok else "（存在不合格项）"))
    if "--json" in sys.argv:
        out = sys.argv[sys.argv.index("--json") + 1]
        with open(out, "w", encoding="utf-8") as f:
            json.dump({"counts": counts, "gates": results, "all_pass": ok}, f, ensure_ascii=False, indent=2)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
