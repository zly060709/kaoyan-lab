# -*- coding: utf-8 -*-
"""状态层维护：汇总 data/meta/migration_*.json -> state/state.json 指标 + 刷新心跳。
用法: python -I -X utf8 tools/update_state.py [task_label]
供 Orchestrator 与每小时看护自动化共用。"""
import datetime, json, os, sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = os.path.join(ROOT, "state")

def now():
    return datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

def main():
    sp = os.path.join(S, "state.json")
    try:
        state = json.load(open(sp, encoding="utf-8"))
    except Exception:
        state = {"schema_version": "1.0.0", "status": "RUNNING", "done_set": [], "metrics": {"questions": {}, "expected": {}}}

    for subj, f in [("politics", "migration_politics.json"), ("math", "migration_math.json"),
                    ("english", "migration_english.json"), ("cs408", "migration_cs408.json")]:
        p = os.path.join(ROOT, "data", "meta", f)
        if os.path.exists(p):
            try:
                m = json.load(open(p, encoding="utf-8"))
                state.setdefault("metrics", {}).setdefault("questions", {})[subj] = m.get("actual_total") or m.get("actual_objective") or 0
                if m.get("ok"):
                    ds = state.setdefault("done_set", [])
                    key = f"m1:migrate_{subj}"
                    if key not in ds:
                        ds.append(key)
            except Exception as e:
                print(f"[warn] {f}: {e}")

    task = sys.argv[1] if len(sys.argv) > 1 else "heartbeat"
    # 扩展科目（math2/math3/mgt199/law498…）不在 migration_*.json 里，一律按磁盘实数反推，
    # 否则 state 的题量指标会停在旧年份（曾长期显示 math3 44 题而磁盘已 273 题）。
    qs = state.setdefault("metrics", {}).setdefault("questions", {})
    for d in sorted(os.listdir(os.path.join(ROOT, "data"))):
        p = os.path.join(ROOT, "data", d)
        if not os.path.isdir(p):
            continue
        n = 0
        for f in os.listdir(p):
            if f.endswith(".json") and f[0].isdigit():
                try:
                    n += int(json.load(open(os.path.join(p, f), encoding="utf-8")).get("question_count") or 0)
                except Exception:
                    pass
        if n:
            qs[d] = n
    # 总题量按注册表求和（注册表由 sync_registry 从磁盘反推）。此前 questions_total
    # 是一个从不更新的死值，长期停在 3272 而磁盘实为 3582。
    try:
        reg = json.load(open(os.path.join(ROOT, "data", "meta", "subjects.json"), encoding="utf-8"))
        state["metrics"]["questions_total"] = sum(int(s.get("questionTotal") or 0) for s in reg["subjects"])
    except Exception as e:
        print(f"[warn] questions_total 反推失败: {e}")
    state["updated_at"] = now()
    if task != "heartbeat" and task not in state.setdefault("done_set", []):
        state["done_set"].append(task)
    json.dump(state, open(sp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    json.dump({"updated_at": now(), "task": task, "by": "orchestrator"},
              open(os.path.join(S, "heartbeat.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("state updated:", json.dumps(state.get("metrics", {}).get("questions", {}), ensure_ascii=False))

if __name__ == "__main__":
    main()
