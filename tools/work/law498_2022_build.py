# -*- coding: utf-8 -*-
"""装配 2022 法硕（非法学）综合课：题干(law498_2022_q) + 解析(law498_2022_a) -> data/law498/2022.json"""
import hashlib
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from law498_2022_q import ITEMS
from law498_2022_a import A

REG = json.load(io.open(os.path.join(ROOT, "data", "meta", "source_pdfs.json"), encoding="utf-8"))
ENTRY = REG["law498:2022"]
PDF, SHA = ENTRY["pdf"], ENTRY["sha256"]

META = {
    1: (["习近平法治思想", "全面依法治国"], 2, "法理学"),
    2: (["法律关系", "隶属型与平权型法律关系"], 3, "法理学"),
    3: (["法律继承", "法律移植与法律全球化"], 2, "法理学"),
    4: (["法律规则的逻辑结构"], 3, "法理学"),
    5: (["大陆法系与英美法系"], 2, "法理学"),
    6: (["法律实施", "执法、司法与守法"], 2, "法理学"),
    7: (["司法原则", "司法公开"], 2, "法理学"),
    8: (["法律与社会", "市场经济法律调控"], 2, "法理学"),
    9: (["法的价值", "自由与秩序"], 3, "法理学"),
    10: (["行政执法", "依法行政与合理性原则"], 3, "法理学"),
    11: (["法律解释", "有权解释与学理解释"], 3, "法理学"),
    12: (["社会主义法与社会主义道德"], 2, "法理学"),
    13: (["近代宪法发展"], 2, "宪法学"),
    14: (["宪法的分类", "马克思主义宪法分类"], 2, "宪法学"),
    15: (["公民的基本义务", "服兵役"], 3, "宪法学"),
    16: (["选举制度", "直接选举与间接选举"], 2, "宪法学"),
    17: (["公民人身自由"], 3, "宪法学"),
    18: (["监察委员会"], 3, "宪法学"),
    19: (["全国人大会议主席团"], 3, "宪法学"),
    20: (["民族区域自治", "自治条例"], 3, "宪法学"),
    21: (["土地制度", "国家所有与集体所有"], 3, "宪法学"),
    22: (["选举制度", "代表候选人"], 3, "宪法学"),
    23: (["男女平等", "妇女权利保障"], 2, "宪法学"),
    24: (["基层群众自治制度", "村民委员会"], 3, "宪法学"),
    25: (["国徽的使用的限制"], 3, "宪法学"),
    26: (["人民法院", "最高人民法院"], 3, "宪法学"),
    27: (["全国人大常委会工作机构", "备案审查"], 4, "宪法学"),
    28: (["西周司法官责任", "五过之疵"], 3, "中国法制史"),
    29: (["秦律", "盗徙封罪"], 2, "中国法制史"),
    30: (["唐律自首", "自首不尽"], 3, "中国法制史"),
    31: (["埋藏物的归属", "得遗失物"], 3, "中国法制史"),
    32: (["革命根据地宪法性文件", "陕甘宁边区施政纲领"], 2, "中国法制史"),
    33: (["《法经》", "盗法与贼法"], 2, "中国法制史"),
    34: (["秦朝刑罚", "赀刑"], 2, "中国法制史"),
    35: (["汉代立法", "傍章律"], 2, "中国法制史"),
    36: (["唐代借贷契约"], 3, "中国法制史"),
    37: (["明代奸党罪"], 2, "中国法制史"),
    38: (["清代雇工人", "良贱相犯"], 3, "中国法制史"),
    39: (["清代少数民族司法管辖", "理藩院"], 2, "中国法制史"),
    40: (["清末司法制度", "会审公廨", "苏报案"], 2, "中国法制史"),
    41: (["新发展理念与立法"], 2, "法理学"),
    42: (["立法与立法体制"], 2, "法理学"),
    43: (["法律职业", "法官职业特征"], 2, "法理学"),
    44: (["法律方法", "判决理由的正当性"], 3, "法理学"),
    45: (["立法法", "规章的效力与裁决"], 3, "法理学"),
    46: (["特别行政区制度"], 3, "宪法学"),
    47: (["国家尊重和保障人权"], 2, "宪法学"),
    48: (["中国古代法律形式", "成例"], 3, "中国法制史"),
    49: (["唐律刑法原则", "轻重相举", "服制定罪"], 4, "中国法制史"),
    50: (["保安处分", "社会防卫主义"], 2, "中国法制史"),
    51: (["形式法律推理", "演绎推理与类比推理"], 3, "法理学"),
    52: (["宪法解释的方法"], 3, "宪法学"),
    53: (["宋朝监察制度"], 3, "中国法制史"),
    54: (["党和法的关系", "党的政策与国家法律"], 3, "法理学"),
    55: (["行政规范性文件", "备案审查"], 4, "宪法学"),
    56: (["清代秋审", "会审制度的发展"], 4, "中国法制史"),
    57: (["法治社会建设", "法治德治自治相结合"], 3, "法理学"),
    58: (["平等权", "特定群体权利保障"], 4, "宪法学"),
}


def strip_q(s):
    s = s.strip()
    if s.startswith("$") and s.endswith("$") and s.count("$") == 2:
        s = s[1:-1]
    return s.replace("$", "")


questions = []
for it in ITEMS:
    num = it["num"]
    ans, blocks_spec = A[num]
    subjective = it["type"] in ("essay", "analysis")
    # 主观题 answer 字段留空（政治/管综同口径），答案材料在 role=answer 原文区块
    ans_field = "" if subjective else ans
    blocks = [{"role": role, "origin": "source", "text": text} for role, text in blocks_spec]
    kps, diff, cat = META[num]
    q = {
        "id": f"law498-2022-{num}",
        "subject": "law498",
        "year": 2022,
        "num": num,
        "type": it["type"],
        "score": it["score"],
        "stem": it["stem"],
        "options": it.get("options", []),
        "answer": ans_field,
        "source_blocks": blocks,
        "knowledge_points": kps,
        "difficulty": diff,
        "category": {"key": cat, "label": cat},
        "tags": ["law498", cat],
        "media": [],
        "related_ids": [],
        "variants": [],
        "origin": "source",
        "source_hash": f"sha256jpg:{SHA}",
        "source_ref": {"pdf": PDF, "sha256": SHA, "pages": it["pages"], "anchor": it["anchor"]},
        "schema_version": "1.0.0",
        "content_hash": "",
    }
    core = {k: q[k] for k in ("id", "year", "num", "type", "stem", "options", "answer", "score")}
    core["blocks"] = [{"role": b["role"], "origin": b["origin"], "text": b["text"]} for b in blocks]
    q["content_hash"] = "sha256:" + hashlib.sha256(
        json.dumps(core, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    questions.append(q)

doc = {
    "subject": "law498",
    "year": 2022,
    "paper": "法硕联考综合（非法学）·专业综合课",
    "schema_version": "1.0.0",
    "question_count": len(questions),
    "source_note": f"视觉转录自《{PDF}》（data/law498/pages/2022/，{ENTRY['pages']} 页）："
                   "p1 封面、p2–p10 试题（原卷第 1–9 页）、p11–p19 答案详解（双栏书籍扫描）；"
                   "题干/选项/答案/解析/点评逐字照录。原卷疑似排版问题一并不改并在此说明："
                   "第 25 题题干写《国旗法》而四个选项均为国徽图案使用（应为《国徽法》，原卷如此）；"
                   "第 45 题第四个选项标号原卷误印为“C.”（依解析引用口径实为 D 项）；"
                   "第 39 题引文“刑狱不决，则报于院”、第 49 题引文嵌套引号与“缌麻”均照录；"
                   "答案详解原书跨页脱漏照录不补：第 6 题解析“是指”与“会生活中”之间、"
                   "第 45 题解析“联合制定”与“但国务院部委”之间原书即缺字（分属前后两页页尾/页首）；"
                   "第 10 题解析末行句号、第 24 题末“D”字、第 31 题“物，”处被二维码部分遮挡，依残形与下页衔接录出。"
                   "第 17、39 题解析跨页由两段原件严丝合缝拼接。"
                   "2022 年法硕综合课结构：单项选择 40×1 分、多项选择 10×2 分、简答 3×10 分、"
                   "分析 3×10 分、论述 2×15 分，共 58 题 150 分。答案详解为第三方教辅（带掌上考研 APP 水印），"
                   "仅限个人学习使用。",
    "questions": questions,
}
out = os.path.join(ROOT, "data", "law498", "2022.json")
json.dump(doc, io.open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("写出", out, len(questions), "题", os.path.getsize(out) // 1024, "KB")
miss = [q["id"] for q in questions if not q["stem"]]
print("空题干:", miss or "无")
print("分数合计:", sum(q["score"] for q in questions))
empty_ans = [q["num"] for q in questions if not q["answer"] and q["type"] not in ("essay", "analysis")]
print("客观题空答案:", empty_ans or "无")
