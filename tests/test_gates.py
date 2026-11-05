# -*- coding: utf-8 -*-
"""tests/test_gates.py — 门禁与工具链集成回归（子进程跑真脚本，断言退出码与关键输出）。
运行: python -I -X utf8 -m unittest discover -s tests -v"""
import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = [sys.executable, "-I", "-X", "utf8"]


def run(args, timeout=300):
    return subprocess.run(PY + args, cwd=ROOT, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", timeout=timeout)


class TestGates(unittest.TestCase):

    def test_gates_all_pass(self):
        r = run(["tools/gates.py"])
        self.assertEqual(r.returncode, 0, "gates 失败:\n" + r.stdout[-2000:] + r.stderr[-500:])
        self.assertIn("通过", r.stdout)

    def test_verify_data_pass(self):
        r = run(["tools/verify_data.py"])
        self.assertEqual(r.returncode, 0, r.stdout[-800:])
        self.assertIn("ALL PASS", r.stdout)


class TestMathAudit(unittest.TestCase):
    """公式渲染审计：CJK 入公式必须为 0；$ 奇偶只允许出现在英语美元符号场景。"""

    def test_no_cjk_inside_math(self):
        r = run(["tools/audit_math.py"])
        self.assertEqual(r.returncode, 0, "audit_math 命中:\n" + r.stdout[-1500:])

    def test_math_figures_verify(self):
        for subj in ("math", "math2", "math3"):
            r = run(["tools/verify_figures.py", subj])
            self.assertEqual(r.returncode, 0, f"{subj} 图形校验失败:\n" + r.stdout[-800:])


class TestSearchIndex(unittest.TestCase):
    """搜索索引 v2：指针分片结构合法、条目数与注册表题量一致。"""

    def test_index_counts_match_registry(self):
        import json
        reg = json.load(open(os.path.join(ROOT, "data", "meta", "subjects.json"), encoding="utf-8"))
        expect = {s["id"]: s.get("questionTotal") or 0 for s in reg["subjects"]}
        idx = os.path.join(ROOT, "data", "index")
        counts = {}
        for name in os.listdir(idx):
            if not name.endswith(".json"):
                continue
            d = json.load(open(os.path.join(idx, name), encoding="utf-8"))
            if "parts" in d:
                continue  # 指针文件本身不计条目，条目在子片里
            sid = name.split(".")[0]
            counts[sid] = counts.get(sid, 0) + len(d.get("entries", []))
        for sid, n in expect.items():
            if n == 0:
                continue
            self.assertEqual(counts.get(sid, 0), n,
                             f"{sid} 索引 {counts.get(sid, 0)} 条 != 注册表 {n} 条")


if __name__ == "__main__":
    unittest.main()
