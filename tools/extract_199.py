# -*- coding: utf-8 -*-
"""199 管综迁移：用户提供的 Markdown 题库（真题 + 解析）-> data/mgt199/{年}.json
+ {年}.analysis.json + {年}.media.json + data/mgt199/pages/{年}/*.jpg（原卷切片压缩）。

保真原则（AGENT_CONTRACT 第 2 章）：
- 题干、选项、答案、解析逐字照录，不改写、不补全、不简化；
- 源 md 没有的内容一律不编造（例：条件充分性判断的 A-E 判断结果选项在源包里缺失 -> options 留空）；
- 每题 source_hash = sha256(该题真题 md 原文块 + 该题解析 md 原文块)，可逐题回溯；
- 原卷切片图全部保留（合同「不删原图」），只做无损语义的压缩（灰度 JPEG）。
用法: python -I -X utf8 tools/extract_199.py [--no-images]
"""
import glob
import hashlib
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = r"C:/Users/jld03/Documents/deepseek-harness/default-workspace/kaoyan-extra-13subjects/kaoyan-extra"
QDIR = os.path.join(SRC, "199管综真题_Markdown题库")
ADIR = os.path.join(SRC, "199管综答案_Markdown题库")
OUTD = os.path.join(ROOT, "data", "mgt199")
METAD = os.path.join(ROOT, "data", "meta")
os.makedirs(OUTD, exist_ok=True)
WITH_IMAGES = "--no-images" not in sys.argv

SECTION_RE = re.compile(r"^##\s*([一二三四五])、(.+?)[：:（(](.*)$")
QHEAD_RE = re.compile(r"^###\s*第\s*(\d+)\s*题\s*(.*)$")
OPT_RE = re.compile(r"^-\s*\*\*([A-E])\*\*[.．、]?\s*(.*)$")
IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
ANS_RE = re.compile(r"\*\*答案\*\*\s*[：:]\s*(.*)")
LETTER_ANS = re.compile(r"^([A-E])\b\s*(.*)$", re.S)


def sha256_text(s):
    return "sha256:" + hashlib.sha256(s.encode("utf-8")).hexdigest()


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def section_kind(title):
    if "问题求解" in title:
        return "single", "问题求解"
    if "条件充分性判断" in title:
        return "sufficiency", "条件充分性判断"
    if "逻辑推理" in title:
        return "logic", "逻辑推理"
    if "写作" in title:
        return "essay", "写作"
    return "other", title


def per_score(header):
    m = re.search(r"每小题\s*(\d+)\s*分", header)
    return int(m.group(1)) if m else None


def parse_paper(path):
    """-> (sections, questions) ；sections 保留章节指令原文，questions 保留原文块。"""
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")
    sections, cur, blocks = [], None, []
    for i, ln in enumerate(lines):
        m = SECTION_RE.match(ln.strip())
        if m:
            cur = {"ord": m.group(1), "title": m.group(2).strip(),
                   "header": m.group(3).strip(), "raw": ln.strip()}
            sections.append(cur)
            continue
        qm = QHEAD_RE.match(ln.strip())
        if qm:
            j = i + 1
            while j < len(lines) and not lines[j].startswith(("### ", "## ", "# ")):
                j += 1
            blocks.append({"num": int(qm.group(1)), "sub": qm.group(2).strip(),
                           "raw": "\n".join(lines[i:j]), "section": cur})
    return sections, blocks


def parse_answers(path):
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")
    out = {}
    i = 0
    while i < len(lines):
        qm = QHEAD_RE.match(lines[i].strip())
        if not qm:
            i += 1
            continue
        j = i + 1
        while j < len(lines) and not lines[j].startswith(("### ", "## ", "# ")):
            j += 1
        raw = "\n".join(lines[i:j])
        am = ANS_RE.search(raw)
        out[int(qm.group(1))] = {"raw": raw,
                                 "answer": (am.group(1).strip() if am else ""),
                                 "body": re.sub(r"^\s*第\s*\d+\s*题\s*\n", "", raw)}
        i = j
    return out


def split_stem_options(raw):
    stem_lines, opts, img = [], [], None
    for ln in raw.split("\n")[1:]:
        s = ln.strip()
        om = OPT_RE.match(s)
        if om:
            opts.append({"letter": om.group(1), "text": om.group(2).strip(), "raw": s})
            continue
        im = IMG_RE.search(s)
        if im:
            img = im.group(1)
            continue
        if s:
            stem_lines.append(s)
    return "\n\n".join(stem_lines), opts, img


def compress_image(src_abs, dst_abs):
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None
    if not os.path.exists(dst_abs):
        im = Image.open(src_abs)
        im = im.convert("L")
        if im.width > 1100:
            im = im.resize((1100, int(im.height * 1100 / im.width)), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=58, optimize=True)
        with open(dst_abs, "wb") as f:
            f.write(buf.getvalue())
    return os.path.getsize(dst_abs)


def main():
    baseline = {"package": SRC, "subject": "mgt199", "files": {}, "years": {}}
    report = []
    for ydir in sorted(glob.glob(os.path.join(QDIR, "*年"))):
        year = int(os.path.basename(ydir).replace("年", ""))
        qmds = glob.glob(os.path.join(ydir, "*真题试卷.md"))
        if not qmds:
            qmds = glob.glob(os.path.join(ydir, "*.md"))
        if not qmds:
            report.append("%d 无真题 md，跳过" % year)
            continue
        qmd = qmds[0]
        adir = os.path.join(ADIR, "%d年" % year)
        amds = glob.glob(os.path.join(adir, "*.md")) if os.path.isdir(adir) else []
        amds = [a for a in amds if "真题试卷" not in os.path.basename(a)]
        sections, blocks = parse_paper(qmd)
        answers = parse_answers(amds[0]) if amds else {}
        baseline["files"][os.path.relpath(qmd, SRC).replace("\\", "/")] = sha256_file(qmd)
        if amds:
            baseline["files"][os.path.relpath(amds[0], SRC).replace("\\", "/")] = sha256_file(amds[0])

        questions, analysis, media_items = [], [], {}
        pagod = os.path.join(OUTD, "pages", str(year))
        if WITH_IMAGES:
            os.makedirs(pagod, exist_ok=True)
        for b in blocks:
            num = b["num"]
            sec = b["section"] or {"title": "", "header": "", "raw": ""}
            typ, cat = section_kind(sec["title"])
            sub = b.get("sub") or ""
            sub_score = re.search(r"\((\d+)\s*分\)", sub)
            if sub and ("论证有效性分析" in sub or "论说文" in sub):
                cat = sub.split("·")[-1].split("(")[0].strip() or cat
            elif sub and sub.strip().startswith("·"):
                cat = sub.strip().lstrip("·").strip() or cat
            stem, opts, imgrel = split_stem_options(b["raw"])
            ans = answers.get(num, {})
            answer_raw = ans.get("answer", "")
            # 答案字母照录；源包里括号内的校注（如「原 PDF 所标 E 经复核有误」）
            # 按合同只作存疑标注，不丢弃、不改写 -> 进 source_blocks(role=note)
            lm = LETTER_ANS.match(answer_raw) if answer_raw else None
            answer = lm.group(1) if (lm and typ != "essay") else None
            annotation = (lm.group(2).strip() if lm else
                          (answer_raw if answer_raw and typ == "essay" else ""))
            qid = "mgt199-%d-%02d" % (year, num)
            blocks_out = [{"role": "stem", "html": "", "text": stem}]
            if opts:
                blocks_out.append({"role": "options", "html": "",
                                   "text": "\n".join(o["raw"] for o in opts)})
            if answer_raw and not answer:
                blocks_out.append({"role": "answer", "html": "", "text": answer_raw})
            if annotation:
                blocks_out.append({"role": "note", "html": "", "text": annotation})
            src_hash = sha256_text(b["raw"] + "\n<<<SPLIT>>>\n" + ans.get("raw", ""))
            media = []
            if imgrel:
                src_img = os.path.normpath(os.path.join(ydir, imgrel))
                dst_name = "%d_q%02d.jpg" % (year, num)
                dst = os.path.join(pagod, dst_name)
                rel = "data/mgt199/pages/%d/%s" % (year, dst_name)
                if WITH_IMAGES and os.path.exists(src_img):
                    compress_image(src_img, dst)
                    media_items[qid] = {0: rel}
                    blocks_out.append({"role": "paper_slice", "html": "",
                                       "text": "@@M:%s:0@@" % qid})
                elif os.path.exists(src_img):
                    blocks_out.append({"role": "paper_slice", "html": "",
                                       "text": "原卷切片：%s" % rel})
            q = {
                "id": qid, "subject": "mgt199", "year": year, "num": num,
                "paper": cat or "199管综", "type": typ, "category": cat,
                "title": "%d 年 199 管综 · %s 第 %d 题" % (year, cat, num),
                "stem": stem,
                "options": ["%s．%s" % (o["letter"], o["text"]) for o in opts],
                "answer": answer,
                "score": (int(sub_score.group(1)) if sub_score
                          else per_score(sec.get("header", "")) if typ != "essay"
                          else (30 if num == 56 else 35 if num == 57 else None)),
                "source_blocks": blocks_out,
                "knowledge_points": [], "difficulty": None,
                "tags": [t for t in [cat] if t],
                "media": media, "related_ids": [], "variants": [],
                "origin": "source", "source_hash": src_hash,
                "source_ref": {"file": os.path.relpath(qmd, SRC).replace("\\", "/"),
                               "anchor": "第 %d 题" % num,
                               "answer_file": (os.path.relpath(amds[0], SRC).replace("\\", "/")
                                               if amds else None),
                               "year": year, "num": num},
                "content_hash": "", "schema_version": "1.0.0",
            }
            if typ == "sufficiency" and not opts:
                q["options_note"] = "条件充分性判断的 A-E 判断结果选项在源 md 包中未给出，按合同不编造；原卷切片见 paper_slice 区块"
            q["content_hash"] = sha256_text(json.dumps(q, ensure_ascii=False, sort_keys=True))
            questions.append(q)
            if ans.get("raw"):
                analysis.append({"id": qid, "num": num,
                                 "desc": answer_raw,
                                 "nodes": [{"type": "text", "label": "完整推导",
                                            "lines": [l for l in ans["body"].split("\n") if l.strip()]}]})
        year_obj = {"subject": "mgt199", "year": year,
                    "title": "%d 年全国硕士研究生招生考试 管理类综合能力（199）" % year,
                    "sections": [{"ord": s["ord"], "title": s["title"], "header": s["header"]}
                                 for s in sections],
                    "question_count": len(questions), "questions": questions}
        tmp = os.path.join(OUTD, "%d.json" % year)
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(year_obj, f, ensure_ascii=False)
        with open(os.path.join(OUTD, "%d.analysis.json" % year), "w", encoding="utf-8") as f:
            json.dump({"subject": "mgt199", "year": year, "count": len(analysis),
                       "analysis": analysis}, f, ensure_ascii=False)
        with open(os.path.join(OUTD, "%d.media.json" % year), "w", encoding="utf-8") as f:
            json.dump({"subject": "mgt199", "year": year, "items": media_items}, f, ensure_ascii=False)
        noans = sum(1 for q in questions if not q["answer"] and q["type"] != "essay")
        baseline["years"][year] = {"questions": len(questions), "with_answer": len(questions) - noans,
                                   "analysis": len(analysis), "images": len(media_items)}
        report.append("%d 题=%d 有答案=%d 解析=%d 图=%d 缺答案题=%s" % (
            year, len(questions), len(questions) - noans, len(analysis), len(media_items),
            [q["num"] for q in questions if not q["answer"] and q["type"] != "essay"][:8]))
    with open(os.path.join(METAD, "mgt199_source.json"), "w", encoding="utf-8") as f:
        json.dump(baseline, f, ensure_ascii=False, indent=2)
    for r in report:
        print(" ", r)
    print("TOTAL 题=%d" % sum(v["questions"] for v in baseline["years"].values()))


if __name__ == "__main__":
    main()
