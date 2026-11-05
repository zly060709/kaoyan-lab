# -*- coding: utf-8 -*-
"""data/schema.json 的消费者：内置 draft-07 子集校验器（type/required/enum/properties/items），
对全部年文件的每道题执行结构校验。gates.py 的 G10 与 tests/ 复用同一实现。
用法: python -I -X utf8 tools/validate_schema.py   （全部通过退出码 0）"""
import glob, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def validate(obj, schema, path="$"):
    """返回错误列表。支持的关键字：type / enum / required / properties / items。"""
    errs = []
    t = schema.get("type")
    if t:
        types = t if isinstance(t, list) else [t]
        ok = False
        for tt in types:
            ok = ok or {
                "object": isinstance(obj, dict),
                "array": isinstance(obj, list),
                "string": isinstance(obj, str),
                "integer": isinstance(obj, int) and not isinstance(obj, bool),
                "number": isinstance(obj, (int, float)) and not isinstance(obj, bool),
                "boolean": isinstance(obj, bool),
                "null": obj is None,
            }[tt]
        if not ok:
            return [f"{path}: 期望类型 {t}，实际 {type(obj).__name__}"]
    if "enum" in schema and obj not in schema["enum"]:
        errs.append(f"{path}: {obj!r} 不在枚举 {schema['enum']}")
    if isinstance(obj, dict):
        for k in schema.get("required", []):
            if k not in obj:
                errs.append(f"{path}: 缺必填字段 {k}")
        for k, sub in (schema.get("properties") or {}).items():
            if k in obj:
                errs += validate(obj[k], sub, f"{path}.{k}")
    if isinstance(obj, list) and "items" in schema:
        for i, it in enumerate(obj):
            errs += validate(it, schema["items"], f"{path}[{i}]")
    return errs

def load_schema():
    return json.load(open(os.path.join(ROOT, "data", "schema.json"), encoding="utf-8"))

def iter_questions():
    for fp in sorted(glob.glob(os.path.join(ROOT, "data", "*", "[12]*.json"))):
        if not re.match(r"^\d{4}\.json$", os.path.basename(fp)):
            continue
        d = json.load(open(fp, encoding="utf-8"))
        for q in d.get("questions", []):
            yield os.path.relpath(fp, ROOT).replace("\\", "/"), q

def main():
    schema = load_schema()
    qschema = dict(schema)
    bad, total = [], 0
    for rel, q in iter_questions():
        total += 1
        for e in validate(q, qschema, q.get("id", "?")):
            bad.append(f"{rel} {e}")
    print(f"schema 校验：{total} 题，错误 {len(bad)}")
    for b in bad[:10]:
        print("  -", b)
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
