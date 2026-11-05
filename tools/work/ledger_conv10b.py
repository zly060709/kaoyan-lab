# -*- coding: utf-8 -*-
"""收敛⑩b 台账：浏览器实测结清 + 答案栏混排裸 LaTeX 缺陷修复（D105）。"""
import io
import sys

sys.stdout.reconfigure(encoding="utf-8")


def sub(path, pairs):
    t = io.open(path, encoding="utf-8").read()
    for old, new in pairs:
        n = t.count(old)
        assert n == 1, f"{path}: 锚点命中 {n} 次 -> {old[:36]!r}"
        t = t.replace(old, new)
    io.open(path, "w", encoding="utf-8", newline="\n").write(t)
    print("更新", path)


D105 = """## D105 · 2026-11-05 · 浏览器实测债首次结清 ＋ 混排答案裸 LaTeX 缺陷修复
**接手会话首次具备真实浏览器**（此前 D101/D102/D103 连续三卷只能报「机械门禁通过、浏览器实测未做」）。本轮在线上 `https://zly060709.github.io/kaoyan-lab/` 实跑：`#/math3/{2009,2010,2011,2013,2014,2015,2017,2018,2019}/q/{1,5,9,16,23}` 共 45 个题页，`.katex-error` 0 个、console（error/warn/uncaught/unhandledrejection 四类钩子）0 条；并用**页面里生产同款 KaTeX** 全量渲染 math3 全部 12 个年份文件的 `$…$` 片段：4254 段、`throwOnError:true` 下 0 失败。合同第 7 章「公式渲染失败数 = 0」这条第一次拿到机械门禁之外的直接证据。

**实测暴露的真实缺陷（静态检查看不出来）**：数学类 21 道题（math2 12、math3 9）的答案栏在页面上印出裸 LaTeX。根因是 `index.html` 第 491 行的历史口径（D098/收敛⑥）——只有「含 LaTeX 命令**且完全不含中日韩字符**」的答案才套 `$…$`，而概率大题答案惯例写 `\begin{cases}…\text{其他}\end{cases}`，`其`/`他` 二字一出现就整条退回纯文本，反斜杠命令全部原样显示。修法不动任何数据：渲染前把**不在 `\text{}`/`\mathrm{}` 等已有分组里的**中日韩片段包进 `\text{…}`，可见字符逐字不变（「其他」「，」「；」都照样显示），然后统一交给 KaTeX。改之前先在线上对全库 166 条 LaTeX 型答案跑一遍 `texify + renderToString(throwOnError:true)`，0 失败才动前端；再用本地 `http.server` 装载改后的 `index.html` 复测 `math3-2011-23`、`math2-2019-15`、`math1-2020-21` 三条原缺陷题（渲染成功、0 `.katex-error`）与 `cs408-2019-24`（无回归）。`sw.js` → `kaoyan-v0.3.10`。

**工具侧一处自我纠错**：`tools/work/render_check.js` 初版写 `/\$([^$]|\\\$)+?\$/g`，捕获组只保留最后一次迭代的字符（`+?` 在外面），会把每个片段截成单个尾字符，导致 15 条假阳性「渲染失败」。改为 `/\\$((?:[^$]|\\\\\\$)+?)\\$/`。离线 Node 路线仍走不通（本机无 node 可执行文件、`node_repl` 沙箱禁 `new Function`，UMD 版 `vendor/katex/katex.js` 无法装载），故该脚本留作有 Node 环境的会话备用，全量渲染改由浏览器完成。

"""

sub("DECISIONS.md", [("## D104 · 2026-11-05", D105 + "## D104 · 2026-11-05")]) if "## D105 " not in io.open("DECISIONS.md", encoding="utf-8").read() else print("D105 已存在，跳过")

sub("QUALITY_REPORT.md", [
    ("- 最后更新：2026-11-05（收敛⑩ · 数学三 2009–2019 九卷入库，全站累计 3559 题）",
     "- 最后更新：2026-11-05（收敛⑩b · 浏览器实测结清 + 混排答案裸 LaTeX 修复，全站累计 3559 题）"),
    ("6. **诚实边界** —— 本机无 Node（`new Function` 亦被沙箱禁止），KaTeX 全量渲染脚本 `tools/work/render_check.js` 已就位但未执行；本会话无内嵌浏览器，题页 console / `.katex-error` / canvas 取色实测仍未做，不谎报。九卷派生图形与 2009-4、2016-1 原卷裁图本轮未接入（见 PENDING_YEARS）。",
     """6. **浏览器实测首次做全**（D105）—— 线上 45 个数三题页 `.katex-error` 0 个、console 四类钩子 0 条；用页面生产同款 KaTeX 全量渲染 math3 12 个年份的 4254 个 `$…$` 片段，`throwOnError:true` 下 0 失败。
7. **实测顺带修掉一个真实渲染缺陷** —— 数学类 21 题（math2 12 / math3 9）答案栏此前印裸 LaTeX：老口径要求答案「完全不含中日韩字符」才套 `$…$`，而 `\text{其他}` 里的两个汉字就让整条退回纯文本。改为渲染前把未被 `\text{}` 包裹的中日韩片段包进 `\text{…}`（可见文字逐字不变），前端全量试算 166 条 LaTeX 型答案 0 失败后再落地；`sw.js` → v0.3.10。
8. **仍待补（诚实边界）** —— 本机无 Node 可执行文件（`node_repl` 沙箱又禁 `new Function`），`tools/work/render_check.js` 的离线路线未跑，全量渲染改由浏览器完成；canvas 取色级图形实测、九卷派生图形与 2009-4 / 2016-1 原卷裁图本轮仍未接入（见 PENDING_YEARS）。"""),
])

sub("DEGRADED.md", [
    ("| 2026-11-05 | math3 KaTeX 全量离线渲染 | 本机 node 不在 PATH；`node_repl` 沙箱禁 `new Function`，无法装载 UMD 版 `vendor/katex/katex.js` | `tools/work/render_check.js` 写好待有 Node 的会话执行；本轮以 `check_m3years.py` 的 `$`/花括号/环境配对静态检查 + 前几卷浏览器实测口径替代，不谎报渲染通过 |",
     "| 2026-11-05 | math3 KaTeX 全量离线渲染 | 本机 node 不在 PATH；`node_repl` 沙箱禁 `new Function`，无法装载 UMD 版 `vendor/katex/katex.js` | 离线路线放弃，改在线上页面内用生产同款 KaTeX 全量渲染：math3 12 个年份 4254 段 `$…$` 0 失败（D105）；`render_check.js` 留作有 Node 环境的会话备用，其捕获组缺陷已一并修正 |"),
    ("| 2026-11-05 | 收敛⑩ 浏览器题页实测 | 接手会话仍无内嵌浏览器 / 无 CDP | 机械门禁 9/9 + `verify_data.py` ALL PASS + `check_m3years.py` 12 年 0 错误 + `audit_m3legacy.py` 余项均为已登记缺口 + 2019 抽样独立复算；不谎报浏览器实测 |",
     "| 2026-11-05 | 收敛⑩ 浏览器题页实测 | ~~无内嵌浏览器~~ 本会话具备 browser-use，已补做 | **已结清**：线上 45 题页 `.katex-error` 0 / console 0，并据此发现且修掉 21 题答案栏裸 LaTeX（D105，`sw.js` v0.3.10）；canvas 取色级图形实测仍待做 |"),
])
