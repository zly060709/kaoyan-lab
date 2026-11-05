# -*- coding: utf-8 -*-
"""数一单卷接入流水线：check → build → audit → 门禁 → 测试。
用法: python -I -X utf8 tools/work/integrate_math1_year.py 2009
前置: tools/work/m1{year}_q.py / _a1 / _a2 / _a3 / _meta 已由转录代理产出，
      math_batch_config.json 已含 math1:{year} 条目。
任一步骤失败即退出非零，不进入后续。"""
import subprocess, sys, os

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)

def run(cmd, must_pass=True):
    print(f"\n===== {' '.join(cmd)}")
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    tail = (r.stdout + r.stderr).strip().splitlines()
    for line in tail[-6:]:
        print("  ", line)
    if must_pass and r.returncode != 0:
        print(f"!! 失败（退出码 {r.returncode}），流水线中止")
        sys.exit(1)
    return r

year = sys.argv[1] if len(sys.argv) > 1 else ""
if not year:
    print("用法: integrate_math1_year.py <year>"); sys.exit(2)

# 1) 模块机械校验
run([sys.executable, "-I", "-X", "utf8", "tools/work/check_math_modules.py", f"m1{year}"])
# 2) 构建数据文件（math_batch_config 已含 math1:year 条目）
run([sys.executable, "-I", "-X", "utf8", "tools/work/build_math_batch.py", f"math1:{year}"])
# 3) 注册表反推 + 索引重建
run([sys.executable, "-I", "-X", "utf8", "tools/sync_registry.py"])
run([sys.executable, "-I", "-X", "utf8", "tools/build_index.py"])
# 4) 公式审计（致命类必须为 0）
r = run([sys.executable, "-I", "-X", "utf8", "tools/audit_math.py"], must_pass=True)
# 5) 门禁 + 单测
run([sys.executable, "-I", "-X", "utf8", "tools/gates.py"])
run([sys.executable, "-I", "-X", "utf8", "-m", "unittest", "discover", "-s", "tests"])
print(f"\n✅ {year} 卷接入完成：数据/注册表/索引/门禁/测试 全绿。")
print("后续（人工或继续任务执行）：git add -A && commit && push（gh-proxy 通道）→ 等 Actions 部署 → 线上核验。")
