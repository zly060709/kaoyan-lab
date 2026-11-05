# -*- coding: utf-8 -*-
"""tests/test_schema_validator.py — validate_schema 校验器单元测试 + 全库结构回归。
运行: python -I -X utf8 -m unittest discover -s tests -v"""
import json
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
import validate_schema as vs  # noqa: E402


class TestMiniValidator(unittest.TestCase):
    S = {"type": "object", "required": ["id"], "properties": {
        "id": {"type": "string"},
        "year": {"type": "integer"},
        "subject": {"enum": ["math", "math2"]},
        "options": {"type": "array", "items": {"type": "string"}},
        "score": {"type": ["number", "null"]},
    }}

    def test_ok(self):
        self.assertEqual(vs.validate({"id": "m-1", "year": 2020, "subject": "math",
                                      "options": ["A", "B"], "score": 4}, self.S), [])

    def test_missing_required(self):
        errs = vs.validate({"year": 2020}, self.S)
        self.assertTrue(any("id" in e for e in errs))

    def test_wrong_type(self):
        errs = vs.validate({"id": 3}, self.S)
        self.assertTrue(any("id" in e for e in errs))

    def test_enum(self):
        errs = vs.validate({"id": "x", "subject": "chinese"}, self.S)
        self.assertTrue(any("枚举" in e for e in errs))

    def test_array_items(self):
        errs = vs.validate({"id": "x", "options": ["A", 2]}, self.S)
        self.assertTrue(any("options[1]" in e for e in errs))

    def test_bool_is_not_integer(self):
        errs = vs.validate({"id": "x", "score": True}, self.S)
        self.assertTrue(any("score" in e for e in errs))

    def test_nullable(self):
        self.assertEqual(vs.validate({"id": "x", "score": None}, self.S), [])


class TestWholeCorpus(unittest.TestCase):
    """全库回归：每道题都符合 data/schema.json。"""

    def test_all_questions_match_schema(self):
        schema = vs.load_schema()
        bad = []
        for rel, q in vs.iter_questions():
            for e in vs.validate(q, schema, q.get("id", "?")):
                bad.append(f"{rel} {e}")
        self.assertEqual(bad, [], "schema 违例 %d 处，例: %s" % (len(bad), bad[:3]))

    def test_index_parts_parse_and_size(self):
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        idx = os.path.join(root, "data", "index")
        total = 0
        for name in sorted(os.listdir(idx)):
            fp = os.path.join(idx, name)
            self.assertLessEqual(os.path.getsize(fp), 500 * 1024, f"{name} 超过 500KB")
            d = json.load(open(fp, encoding="utf-8"))
            if "parts" in d:
                self.assertTrue(all(os.path.exists(os.path.join(idx, p)) for p in d["parts"]),
                                f"{name} 指针指向的子片缺失")
            else:
                for e in d.get("entries", []):
                    self.assertIn("sid", e)
                    self.assertIn("num", e)
                total += d.get("count", len(d.get("entries", [])))
        self.assertGreater(total, 3000, "索引条目异常")


if __name__ == "__main__":
    unittest.main()
