# DEGRADED — 降级与跳过记录

按 AGENT_CONTRACT.md 第 6 章：同一任务连续 3 次失败 → 永久跳过并记录于此，全局继续。

| 时间 (UTC) | 任务 | 状态 | 处置 |
| --- | --- | --- | --- |
| 2026-11-05 | git push / git fetch（pack 通道） | 全局 `ghproxy.net` 的 `insteadOf` 重写 + 86MB 包 + 50–190KB/s 链路，多次 `fetch-pack: invalid index-pack output`；直连间歇性 443 连接失败 | 永久跳过 git 传输层，改走 GitHub Data API 四步提交（`tools/publish_api.py`，D104）；本地物化副本用 blobs API 逐文件取回并校验 git hash |
| 2026-11-05 | math3 KaTeX 全量离线渲染 | 本机 node 不在 PATH；`node_repl` 沙箱禁 `new Function`，无法装载 UMD 版 `vendor/katex/katex.js` | `tools/work/render_check.js` 写好待有 Node 的会话执行；本轮以 `check_m3years.py` 的 `$`/花括号/环境配对静态检查 + 前几卷浏览器实测口径替代，不谎报渲染通过 |
| 2026-11-05 | 数学三 2012 / 2020 两卷 | 上一会话草稿未定稿：2012 缺第 15–23 题解析与 meta，2020 缺第 9–23 题解析、meta 与 notes；2016 有稿但无 notes | 不入库、不按记忆补写；影像仍在 `data/math3/pages/`，登记 PENDING_YEARS 后续转录 |
| 2026-11-05 | 数三 2009-4 / 2016-1 图形 | 草稿以【图】占位（2009 第 4 题含题干图与 4 个选项图、2016 第 1 题含 $f'(x)$ 图），原图未裁出 | `audit_m3legacy.py` A5 持续拦截；待裁 `data/math3/pages/` 影像写 `{年}.media.json` 并替换为 `@@M:` 占位 |
| 2026-11-05 | 收敛⑩ 浏览器题页实测 | 接手会话仍无内嵌浏览器 / 无 CDP | 机械门禁 9/9 + `verify_data.py` ALL PASS + `check_m3years.py` 12 年 0 错误 + `audit_m3legacy.py` 余项均为已登记缺口 + 2019 抽样独立复算；不谎报浏览器实测 |
| 2026-11-04 15:23 | m0:github-auth | 第 1 个设备码 `1689-3469` 到期未授权 | 已重签 `96E4-E4F2`；按合同第 0 章第 4 条继续离线构建，授权通过立即建仓推送 |
| 2026-11-04 15:1x | m1:migrate_math（子 Agent 首次启动） | 并发上限启动失败 | 已按重试策略唤醒重跑（retry 1/3） |
| 2026-11-05 | 全部子 Agent 队列 | 用户指令「不要开子程序，你一个人按顺序做完」（D090） | 停止在跑子 Agent（实测停止时零产出），队列改由 Orchestrator 顺序执行；合同第 5 章编制暂停，其余条款继续生效 |
| 2026-11-05 | m8:legacy 哈希基线 | D007 记录的 `tools/legacy_hashes.txt` 实际不存在 | 降级为「用分享页 artifact 对象键里的 SHA-256 反查」，核对一致后补建基线文件；G2 恢复为真校验 |
| 2026-11-05 | 数学三 / 英语二 逐题转录 | 视觉转录需逐页读图，单会话上下文不足以一次吃完 15+16 卷 | 不编造、不批量伪转录；按年份切片续跑。数学三 2022、2023 两卷已转录入库（44 题，`imaging → active`），其余 13 卷仍只提供原卷影像；英语二保持 `pending` |
| 2026-11-05 | 收敛⑨ 浏览器题页实测 | 接手会话无内嵌浏览器，与收敛⑦⑧同口径 | 机械门禁 9/9 + `verify_data.py` ALL PASS（含 law498 58 题基线）+ 跨页/遮挡接缝逐一裁图裁决；不谎报浏览器实测 |
| 2026-11-05 | 收敛⑧ 浏览器题页实测 | 接手会话无内嵌浏览器，与收敛⑦同口径 | 机械门禁 9/9 + `verify_data.py` ALL PASS + `verify_figures.py` math3 12 幅 OK + `$`/花括号/环境配对静态检查 0 错误；不谎报浏览器实测，待有浏览器工具的会话补做 |
| 2026-11-05 | 收敛⑦ 浏览器题页实测 | 接手会话无内嵌浏览器 / 无 CDP，无法做 canvas 取色与 console 抽查 | 降级为机械门禁 9/9 + `verify_figures.py` 9 幅 OK + `$`/花括号/环境配对静态检查 0 错误；**不沿用也不谎报前几卷的浏览器实测数字**，待有浏览器工具的会话补做 |
| 2026-11-05 | ZCode 主会话 | 收敛⑥ 收尾（DEGRADED 口径更新后）请求失败 `The request could not be completed`，该轮成果未提交 | 由新会话接手：先核对门禁 9/9 与磁盘产出，补齐台账后 commit + push，再按 `state/queue_sequential` 继续；不回滚任何已落盘文件 |
| 2026-11-05 | 前端 JS 语法校验 | 本机 node 不在 PATH，无法 `node --check` | 降级为浏览器 `new Function(内联脚本)` 探针 + 本地 `http.server` 实路由抽查（曾据此定位并修复一个漏括号导致的整脚本不执行） |
| 2026-11-05 | 浏览器截图验收 | 内嵌浏览器无可见视口（`NATIVE_BROWSER_VIEWPORT_UNAVAILABLE`），Lighthouse 未跑分 | 改用 DOM 结构断言（选项高亮/图片破图/裸 JSON/undefined 文本）逐项验收；Lighthouse 分数不谎报，记于 QUALITY_REPORT「尚未执行的验收项」 |
| 2026-11-05 | 199 管综 / 396 经综 / eol 7 科 资料接入 | 用户新提供的资料尚未迁移入库 | 注册表保持 `pending`，不显示虚假年份；迁移在台账 #2/#4/#5 顺序推进 |

（空 = 暂无降级项。）
