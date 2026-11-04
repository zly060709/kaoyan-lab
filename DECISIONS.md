# DECISIONS — 自主决策记录

本文件由 Orchestrator 维护：所有模糊处的默认决策记录于此（AGENT_CONTRACT.md 第 0/5/6 章要求）。新条目倒序追加。用户已明确：不提问、自行决策并记录。

## D009 · 2026-11-04 · 纯导航元素不进入数据层
`nav.toc`、顶部年份 tab、进度条等纯导航/交互元素不迁移进题目 JSON，由前端按数据重建；题目内容区块（题干/选项/答案/解析/思路/背景/问答/框架/材料）全量迁移，一条不丢。

## D008 · 2026-11-04 · 数据迁移顺序
408（内嵌 RAW_DATA JSON，最易保真）→ 政治（结构规整）→ 英语 → 数学（超长行 + 内嵌 KaTeX 字体，最后处理）。英语/数学由两个隔离后台子 Agent 并行执行（合同第 5 章迁移工程师并发上限 2）。每科完成即 commit 并核对题量基准（408=376 / 政治=456 / 英语客观=675 / 数学=250）。

## D007 · 2026-11-04 · legacy 字节级只读基线
legacy/ 四文件字节原样复制；`.gitattributes` 对 `legacy/**` 关闭 EOL 转换；SHA-256 基线记录于 `tools/legacy_hashes.txt`（408: 6d1e706a…，数学: 4bb048e2…，政治: 3583872f…，英语: 933e4c54…）。任何阶段不得改动这些字节。

## D006 · 2026-11-04 · 看护自动化落地（用户指令）
用户要求「每 1 小时检测项目是否仍在运行，卡死则发『继续任务』直到完成」→ 已创建 hourly 自动化：heartbeat 距今 <15min（outer_timeout）视为正常运行（静默结束，避免与主会话冲突）；≥15min 或缺失判定卡死 → 输出「继续任务」并按 state/state.json checkpoint 幂等续跑；status=DONE（QUALITY_REPORT.md 标记已交付）→ CronPauseSelf 自停。

## D005 · 2026-11-04 · 脚本目录
合同目录清单未列脚本目录；解析/校验/状态工具统一放 `/tools/`（最小偏差，其余结构照合同）。

## D004 · 2026-11-04 · 解析器技术选型
Python 3 标准库（re/json/hashlib），零第三方依赖、零网络依赖——符合「无构建步骤」，规避沙箱不确定性。宿主实测 Python 3.10.6 可用、Node 不可用。统一以 `python -I -X utf8` 运行。

## D003 · 2026-11-04 · GitHub 授权路径
gh CLI 未安装 → 用 curl 实现 OAuth Device Flow（GitHub CLI 官方公开 client_id `178c6fc778ccc68e1d6a`，scope=repo workflow read:user）。device_code 存 `state/.auth/`（已 gitignore，不入库）；access_token 仅存用户级本地凭据（`~/.git-credentials`）或进程内存，绝不写入仓库/日志/回复。等待授权期间并行离线构建（合同第 0 章第 4 条），每完成原子任务重试授权。

## D002 · 2026-11-04 · 仓库命名与位置
仓库根目录 = 当前工作区（本文件所在目录）；仓库名 `kaoyan-lab`，重名自动 `-2`/`-3`（合同第 0 章第 5 条）。默认 public + README/LICENSE/页脚版权声明（合同第 0 章第 6 条）。

## D001 · 2026-11-04 · git 提交身份
宿主未配置 git 身份时，仅在仓库本地设置 user.name=kaoyan-orchestrator、user.email=orchestrator@kaoyan-lab.local，不动全局配置。
