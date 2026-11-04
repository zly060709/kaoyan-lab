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
    state["updated_at"] = now()
    json.dump(state, open(sp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    json.dump({"updated_at": now(), "task": task, "by": "orchestrator"},
              open(os.path.join(S, "heartbeat.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("state updated:", json.dumps(state.get("metrics", {}).get("questions", {}), ensure_ascii=False))

if __name__ == "__main__":
    main()
