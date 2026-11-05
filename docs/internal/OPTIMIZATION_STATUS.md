# 优化清单 77 条落地状态表（收敛⑩ · 2026-11-06）

> 对照《kaoyan-lab 优化清单》（77 条）。✅=已落地并验收；🟡=部分落地（说明余量）；⏸=本轮不做（含理由）。
> 合并说明：收敛⑩与并行会话的收敛⑪–⑭（影像入口、数三补全、搜索摘要修复）已合流，本表以后者为补充口径。

## A · P0（12 条）

| # | 状态 | 说明 |
| --- | --- | --- |
| A01 | ✅ | katex.min.css 入 index/lab3d head + SW CORE 预缓存；KaTeX 改惰性加载（E02），进题页才拉 |
| A02 | ✅ | manifest/icon/theme-color 四件套入三页；manifest 加 id/shortcuts；PNG 192/512 未生成（⏸ 图标 PNG，系统 svg 可安装） |
| A03 | ✅ | 页脚与 onerror 全改相对路径；404 页不再吞错 |
| A04 | ✅ | robots.txt 全站 Disallow + 每页 noindex；404 静态错误页（带定位手动返回）；sitemap 按私有化路线不生成 |
| A05 | ✅（加密路线） | 用户拍板：构建期全内容 AES-256-GCM 加密（data/**/* 1736 文件 99.9MB）+ 口令解锁 + 全站 noindex；法律定性差异由用户知悉并承担（about.html 已写明个人使用边界）；建议后续把仓库设 Private |
| A06 | ✅ | 部署白名单 dist/：md 内部文档、legacy 15MB、tools、明文 data 一律不发布；注册表 note 迁 docs/internal/ |
| A07 | ✅（撤销） | 按清单私有化路线：加密站不收录 → 预渲染/sitemap 不做，动 title/meta 已做（B16） |
| A08 | ✅ | esc 补 `'`；safeURL 白名单；safeColor 校验；b.html 清洗（script/on*/javascript:）；CSP meta（E08 后无 unsafe-eval）；blob: 仅 img-src |
| A09 | ✅ | RENDER_SEQ 全视图竞态防护（await 后 alive() 校验）；搜索 runId；loadFigures 校验 |
| A10 | ✅ | --math/--ink/--gold-l 定义入 index/lab3d；未定义变量已清 |
| A11 | ✅ | 首次安装不刷新；更新仅 toast 提示不自动 reload |
| A12 | ✅ | 双缓存桶：kyl-content 跨版本保留 data/enc/vendor；kyl-core-VER 版本化；KaTeX 入预缓存 |

## B · P1（16 条）

| # | 状态 | 说明 |
| --- | --- | --- |
| B01 | ✅ | 「我的」页收藏列表（跳转/移除），数据 bm: 键读取 |
| B02 | ✅ | hint: 累计展示于「我的」（提示依赖参考） |
| B03 | ✅ | 科目卡自测正确率条 + 首页「继续上次学习」（kyl:last）+ 全库随机一题 |
| B04 | ✅ | 自测 v2：完整选项可点选作答、判分、统计、错题本、重做回滚、主观题自评；答案在提交前不可见（揭示/判分后才渲染） |
| B05 | 🟡 | 错题本 ✅ + 错题加权随机（40%）✅；SM-2 复习队列 ⏸（待下一轮） |
| B06 | ⏸ | 计时/模考/统计图表：本轮未做（工作量一个整轮）；统计底座（per-subject 正确率）已有 |
| B07 | ✅ | JSON 备份导出/导入（「我的」页）+ 清空记录 |
| B08 | ✅ | 首页分组：可刷题/仅影像主区 + 规划中折叠；CTA 行 |
| B09 | 🟡 | 顶栏科目下拉 + 题目页跳题输入框 ✅；面包屑同级下拉 ⏸ |
| B10 | ✅ | 索引按科合并（≤480KB 分片），搜索 ≤8 请求，增量渲染 + 防竞态；实测首搜 1.3s |
| B11 | 🟡 | 命中计数/相关度排序/空态引导 ✅；同义词/分词 ⏸ |
| B12 | ✅ | 题目页 ⚑ 反馈（GitHub issue 深链带题号+哈希）+「我的」纠错说明 |
| B13 | 🟡 | 灯箱 dialog（翻页/缩放/键盘）✅；OCR/WebP/尺寸标注 ⏸（影像 1491 张转码留待专门轮次） |
| B14 | ✅ | 使用说明数字全部由注册表反推 |
| B15 | ✅ | 注册表失败显示重试页（不再放假数据）；SW 预缓存注册表支持离线 |
| B16 | ✅ | setMeta 每视图动态 title/description |

## C · P2（14 条）

| # | 状态 | 说明 |
| --- | --- | --- |
| C01 | 🟡 | 字体诚实化：UI=系统黑、正文=宋体栈（未加载 Noto Serif SC 的事实明确）；Web 子集化 ⏸（体积/收益比） |
| C02 | ✅ | 题目页阅读宽度 760px 居中 |
| C03 | 🟡 | 字号收敛 ≥12px 下限、圆角/间距/时长令牌；全量 token 化 ⏸ |
| C04 | ✅ | 深/浅/自动三态主题（html.dark 全量变量 + 影像降亮度 + theme-color 同步） |
| C05 | ✅ | 区块语义色收敛 5 类（color-mix），暗色自动成立 |
| C06 | ✅ | 正确项 ✓ 记号 + 徽标 ≥12px + pending 卡语义文案 |
| C07 | ✅ | safe-area 全套（顶栏/底栏/返回键）+ 760/640 双断点 |
| C08 | ✅ | hero 收敛（padding 减、CTA 行、去负 margin 叠压） |
| C09 | ✅ | 骨架屏（年份页）+ 重试按钮（失败态）+ fetch 重试 |
| C10 | ✅ | 日期 dialog（input[type=date] + 真实日期校验） |
| C11 | ✅ | 考试日期自动推算未来届次（2026/2027/2028）+「预计」标注 |
| C12 | ⏸ | SVG 图标系统：emoji 保留（一致性收益 vs 全量重绘成本，下轮） |
| C13 | 🟡 | --dur 统一过渡时长；动效审计全量 ⏸ |
| C14 | 🟡 | 令牌语义统一于 index 内联 + lab3d 变量补齐；拆分 tokens.css ⏸（与 E01 一并做） |

## D · P2 可访问性（13 条）

| # | 状态 | 说明 |
| --- | --- | --- |
| D01 | ✅ | main/skip-link/每视图唯一 h1/面包屑 nav+aria-label |
| D02 | ✅ | 自测开关 role=switch + aria-checked + 原生键盘 |
| D03 | ✅ | 返回顶部改 button + aria-label + visibility 隐藏 |
| D04 | ✅ | 全局键盘白名单（button/a/summary/switch 内不接管） |
| D05 | ✅ | `/` 全局搜索聚焦 + `?` 快捷键帮助 dialog + 题目页 A–H/回车 |
| D06 | ✅ | :focus-visible 全局金环 + 搜索框焦点环 |
| D07 | 🟡 | 影像/配图 alt 语义化 + canvas aria-label=图形说明；数据级 alt 字段 ⏸ |
| D08 | ✅ | toast role=status / errbar role=alert / 搜索结果 aria-live+busy |
| D09 | ✅ | 灯箱原生 dialog + 方向键翻页 + 缩放 + 焦点归还 |
| D10 | ✅ | 收藏/chips/九段 aria-pressed/expanded/controls |
| D11 | 🟡 | --muted 加深至 #52627a、最小字号 12px；对比度脚本化校验 ⏸ |
| D12 | ✅ | 可点图 tabIndex+role=button+Enter/Space |
| D13 | ⏸ | axe/Lighthouse CI：本机无 node；CI 已有门禁+schema+审计+测试四步，浏览器实测替代（console 0 / katex-error 0） |

## E · P3（14 条）

| # | 状态 | 说明 |
| --- | --- | --- |
| E01 | ⏸ | 模块化拆分：单文件 61KB 可缓存，重构收益排在功能后（与 C14 下一轮） |
| E02 | ✅ | KaTeX 惰性加载 + lab3d 依赖白名单化（vendor 只发 min 版） |
| E03 | 🟡 | KaTeX 随惰性加载即用时取；preload/font 策略随 C01 ⏸ |
| E04 | ⏸ | WebP/AVIF 转码：1491 张留专门轮次（含 srcset/尺寸） |
| E05 | ✅ | LRU 缓存（80 条）+ getContent 统一内容层 |
| E06 | ✅ | fetch 指数退避重试（404 立即失败）+ 15s 超时 |
| E07 | ✅ | SW 双桶 + enc/manifest 网络优先 + 核心页 1.5s 竞速 |
| E08 | ✅ | 递归下降表达式解析器替代 new Function；CSP 去 unsafe-eval |
| E09 | ✅ | CSP + Referrer-Policy + 外链 noopener + noindex meta |
| E10 | 🟡 | kyl: 命名空间新键 + 导出/导入兜底；存量键迁移 IndexedDB ⏸ |
| E11 | ✅ | 错误环形日志（kyl:errlog 20 条）+ unhandledrejection + diag 页可读 |
| E12 | ✅ | CI 四步（gates/schema/公式审计/单测）→ 加密构建 → 部署；G8 静态引用校验 |
| E13 | ✅ | 页脚内容版本（updated_at + 科数 + 题数）；diag 展示缓存桶与加密状态 |
| E14 | ⏸ | Pages 响应头不可配；资产瘦身随 E04 |

## F · P3（8 条）

| # | 状态 | 说明 |
| --- | --- | --- |
| F01 | ✅ | 站名/描述统一「考研真题逐题精讲 · 个人学习库」，数字全部动态 |
| F02 | ✅ | 注册表 note 迁 docs/internal/registry-notes.md；冗余 years 字段删除 |
| F03 | ✅ | 「分步揭示（本题 N 段）」按实际段数，9 段时才叫九段式 |
| F04 | ✅ | 哈希点击复制完整值 + 来源可点（影像对照链接） |
| F05 | ✅ | 四态改用户语言：可刷题/仅原卷影像/整理中/尚未收录 + 图标 |
| F06 | ✅ | 页脚内容版本展示；CHANGELOG 自动生成 ⏸ |
| F07 | ✅ | 题页区块三组分组（原文/解析/扩展）+「扩展 · 非原卷」标签 |
| F08 | ✅ | 页脚两行 + about.html（来源/版权/隐私/条款四合一，加密与个人使用口径一致） |

## 遗留清单（建议下一轮）

1. B06 模考与计时、B05 SM-2 复习队列（学习闭环下半场）
2. E04/B13 影像 WebP + 尺寸 + OCR 文本层（63MB → 预计 −60%）
3. E01/C14 前端模块化 + tokens.css（耐维护）
4. C12 SVG 图标、B11 同义词、D13 axe CI（需 node 环境）
5. 建议：仓库转 Private（A05 加密只护站点不护仓库历史，一个开关的事，由仓库所有者操作）
