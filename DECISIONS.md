# DECISIONS — 自主决策记录

本文件由 Orchestrator 维护：所有模糊处的默认决策记录于此（AGENT_CONTRACT.md 第 0/5/6 章要求）。新条目倒序追加。用户已明确：不提问、自行决策并记录。

## D096 · 2026-11-05 · 收敛②：门禁 9/9 的口径与修复清单
收尾复核发现三处真实缺口，全部按「原文照录、不编造」原则处理：
① **G2 legacy 基线**：D007 记录的 `tools/legacy_hashes.txt` 其实从未落盘。改用会话分享页 artifact 对象键里携带的完整 SHA-256 反查本地四份 legacy，逐字节一致后把基线补写进仓库，G2 由「文件缺失」变成真校验。
② **G5 政治答案缺口**：2016/2017/2018 各 33 题（共 99 道客观题）`answer` 字段为空，但原文 `source_blocks[role=answer]` 里有字母。新增 `tools/promote_politics_answers.py` 逐字提升（只认 A–E 字母形态，其他形态一律跳过并报告），零改写、跳过 0 题。
③ **G5 主观题口径**：essay / translation / writing / big 类没有单一答案字符串，允许 `answer` 为空，但原文区块里必须真有答案材料（answer / trans-zh / essay-box / nodes / detail），否则算缺口而不是主观题。实测 221 题按此口径放行，其中 30 道英语写作逐题确认含参考范文。
④ **G8 误报**：`src|href="${...}"` 是 JS 模板字面量不是静态路径，正则跳过 `${` / `{{`，21 处真实引用全部有效。

## D095 · 2026-11-05 · 408 题型与题干修正（重抽取 + 前后比对自证）
legacy `RAW_DATA` 的 `qtype` 是英文 `choice`/`big`，而旧 `qtype_map` 只认中文「单/多」→ 376 题全被误标成 `big`，选择题的自动高亮与题型统计因此失效。修正：`choice` 按答案字母个数映射 single/multi（不改答案本身），恢复 `cs408-2019-13` 的空题干（原文 `stem_nodes` 逐行照录进 `stem`，`.stem` 用 pre-wrap 保留换行，不加代码围栏），并把 `stem_nodes` 全量存为 `role=stem_nodes` 区块保证零丢失。重抽取后与备份逐题比对：**376 题、只有 type(320)/stem(1)/source_blocks(84)/content_hash(365) 变化，options / answer / source_hash 零变化**，`data/meta/migration_cs408.json` 仍 376/376。分片重切（11 个文件）后复检 ≤500KB。

## D094 · 2026-11-05 · 前端选项字母与结构化区块渲染
三处显示级缺陷修复：① 408 选项是无标签纯值（`["−1","−32767",…]`），整列都取不到字母时按位置补 A./B./C./D. 并高亮正确项，与 D037「按位置推断字母」口径一致；② `optLetter` 增加全角 `（A）` 形态识别，数学选项不再被重复加字母前缀；③ `source_blocks` 里的 `nodes`/`stem_nodes` 原本是裸 JSON 文本直接铺在页面上，改为结构化渲染（标签 + 逐行，代码行走 `pre`），原文区块里自带的选项列表保留不删、降级为虚线附录。`sw.js` → `kaoyan-v0.3.1` 强制丢弃旧数据缓存。

## D090 · 2026-11-05 · 【最高优先级·用户指令】单 Agent 顺序模式
用户明确指令：「不要开子程序，所有东西你一个人按顺序做完」。处置：①立即停止全部在跑子 Agent（实测停止时零产出，无损失）；②此后一切迁移/转录/图形化/精讲/部署由 Orchestrator 本体按优先级顺序亲自执行；③合同第 5 章多 Agent 编制暂停适用，其余章节（保真/门禁/防锁死）全部继续生效；④执行顺序按用户诉求排序：数学图形化 → 数二/数三/数一补卷（视觉转录）→ 英语二/英一补年（文本提取）→ 每步 commit+push。

## D045 · 2026-11-05 · 20 科统考扩展：以用户真实资料为唯一真题来源
用户 2026-11-05 提供《学科历年真题》资料库（D:\桌面\学科历年真题，96 个 PDF）并要求扩展为 20 科统考资料库。实测资料覆盖 6 科：政治 2013–2024、数学一/二/三 2009–2023、英语一 2005–2025、英语二 2010–2025。处置：①已有四科保留；②新开工 数一 2009–2012 补缺、数二、数三（全新）、英一 2005–2009+2025 补缺、英二（全新）；③其余统考科目（英二以外未提供的法硕/306 西医/307 中医/311 教育/312 心理/313 历史/199 管理/396 经济/314/315/414/415 等）**无资料不编造**，写入 PENDING_YEARS.md 待用户提供资料后按同一管线开工。首页以 data/meta/subjects.json 注册表驱动，20 科框架全部展示，未开工科目显示「待资料」。

## D044 · 2026-11-05 · 数学 PDF 保真管线：逐页影像 + 视觉转录
数学 PDF 公式在文本层严重乱序（不可靠），直接文本提取会违反保真。管线：PyMuPDF 将每份试卷逐页渲染为灰度 PNG（DPI≈130）入仓 data/{math2|math3|math1.pages}/pages/{year}/，Agent 逐页视觉转录题干/选项/答案/解析为 LaTeX，每题 source_ref 记 PDF 页码；source_hash=sha256(页面 PNG)。PDF 原件不入库（本地留存），SHA-256 与页数记入 data/meta/source_pdfs.json。英语/政治 PDF 文本层干净：直接文本提取，PDF 亦作为政治既有 456 题的交叉核对源。

## D043 · 2026-11-05 · 数学抽象概念图形化（图形规格 DSL + 前端引擎）
用户要求「数学题目抽象化的东西都具体做出变成图」。实现：Agent 为可图形化的题目产出 figure spec（JSON DSL：graph/shade/point/vline/hline/circle/segment/polygon/parametric/polar/text），存 data/{subject}/figures/{year}.json，origin=derived（不改原题内容，标注对应题号）；前端 Canvas 引擎按 spec 渲染（白名单表达式求值，禁 eval 拼接用户输入）。3D 曲面场景（Three.js）列入 M5，2D 覆盖函数/区域/几何/极坐标/参数曲线。

## D042 · 2026-11-05 · 部署通道：legacy 构建失败 → 切换 Actions 部署
GitHub Pages legacy 构建 1 次失败 + 1 次卡死 20 分钟；切换 build_type=workflow（PUT 204）+ .github/workflows/deploy-pages.yml（upload/deploy-pages）。当前 GitHub Actions 处于 partial_outage（官方状态页），运行排队中，恢复后自动部署；看护自动化每小时跟踪。

## D041 · 2026-11-05 · 英语/政治 PDF 交叉核对
政治 PDF（新东方在线版，含答案）与既有 456 题逐题交叉核对列为 M8 抽检任务；英一 2010–2024 PDF 与既有 675 题同样可交叉核对。核对只增「存疑标注」，不改答案（合同第 2 章第 3 条）。

## D040 · 2026-11-04 · 远端推送绕过 ghproxy 镜像（不改全局配置）

## D040 · 2026-11-04 · 远端推送绕过 ghproxy 镜像（不改全局配置）
宿主全局 git 配置存在 `url.https://ghproxy.net/https://github.com/.insteadOf`（只读加速镜像，不支持 push），导致推送无限挂起。处置：不修改用户全局配置，仅将本仓库 origin 设为 `https://github.com:443/zly060709/kaoyan-lab.git`（不匹配 insteadOf 前缀，直连 github.com），实测推送 183 对象/14.89MiB 成功。后续推送均用此 remote。

## D039 · 2026-11-04 · 英语翻译题 stem 与纯导航边界
翻译题（46–50）stem 取题卡内 trans-src 原文英文句；译文 trans-zh 与采分点 detail 全量入 source_blocks（role=trans-src/trans-zh/detail）。纯导航与脚本样式（#topnav、year-tabs、#toc、back-top、word-popup、selftest CSS、进度/切换脚本）不进数据层（沿用 D009）。

## D038 · 2026-11-04 · 英语内嵌大词典分片保全
英语 legacy 内嵌 LOCAL_DICT 大词典（5562 条）按首字母分 4 片存 `data/meta/english_dictionary_{a-g,h-n,o-t,u-z}.json`（单片 ≤500KB，内容一条不丢），保障合同「内嵌大词典与点词查词」资产可复原；封面/答案速查表/页脚文本快照存年文件顶层 cover/answer_sheet/footer 便于溯源。

## D037 · 2026-11-04 · 英语 options 字符串口径与个别缺标签选项
options 数组为字符串「[X] 英文 中文释义」；opt-zh 中文释义与英文之间补一个空格（原文紧排者照录于 source_blocks 的 options 原样 html，零丢失）。2023 年 Part B 为 A–H 八项、其余年份 A–G 七项；个别缺 [X] 标签 span 的选项（2013-38 [B]，原文即 `<span class="opt">`）按位置推断字母。Part B 无 options 数组，选项原文存 nt-opts。

## D036 · 2026-11-04 · 英语答案双源交叉核对
answer 以题卡 .q-answer 为准，并与答案速查表 45 格、opt.correct 标记两路交叉核对；本次 675 题三源零不一致。如不一致仅记录于 migration_english.json 的 answer_mismatches，绝不改写（合同第 2 章第 3 条）。

## D035 · 2026-11-04 · 英语序列化与原子写
年文件以紧凑序列化（separators=(',',':')，ensure_ascii=False，UTF-8）控制体积，tmp+os.replace 原子落盘；实测最大分片 334KB<500KB，无需按 passage 再分片。

## D034 · 2026-11-04 · 英语 question_count 采用客观题口径
年文件 question_count=客观题数（45/文件）以对齐 tools/verify_data.py 的「英语=675」验收语义；同时设 total_question_count=52 与 objective_count/translation_count/writing_count 分项，questions 数组仍含全部 52 条，无内容省略（与 D011 口径一致）。

## D033 · 2026-11-04 · 英语双哈希算法定义
source_hash=sha256(题卡纯文本，空白归一)；content_hash=sha256(以「|」连接的 id|year|num|type|stem|options…|answer|score|source_blocks.text… 各段 norm 文本)。算法定义写入 migration_english.json.hash_algorithm 供 CI 复算。

## D032 · 2026-11-04 · 英语 Part B stem 取原文【题目】段
新题型（41–45）题卡无 stem：取 partb .bilingual 的【题目】段为 stem（原文）；2020 年原文仅有【选项】段，回退取该双语块首段（均为原文内容，不编造）。nt-opts（新题型选项原文英汉对照）以 role="nt-opts" 全量附入 41–45 每题 source_blocks，另存结构化 partb_options 于年文件顶层。

## D031 · 2026-11-04 · 英语完形题 stem 派生规则
完形仅 7 个年份第 1 题带 .stem；其余题目 stem 从完形 .bilingual 原文抽取「含第 N 空标记的原句」（句子切分含数字开头句边界，如 "proof. 12 the precautionary…"；293 句派生+12 段单句段落），整段原文另存 role="stem-ctx"；stem 恒为 passage 原文子串，零编造、零丢失。

## D030 · 2026-11-04 · 英语写作题编号与组装
写作原卷无题卡：按 sub-banner 顺序组装为 num=51（Part A 小作文）/52（Part B 大作文），与封面「共 52 题」口径一致；stem=dir-en 英文原题指令，dir-box 与全部 essay-box（含 essay-zh 中文对照）全量入 source_blocks；score 仅当原文标注（10分/20分）才提取，其余题型 score=null（原文无分值不许编造）。

## D029 · 2026-11-04 · 数学分片文件形状
`data/math/{year}.json` = `{subject, year, paper, question_count, questions:[…]}`，paper 取自原文年份头「数学（一）真题精讲 · N 题」中「·」前文字。理由：与 `tools/verify_data.py` 读取约定（question_count/questions）对齐，年份级元数据不逐题重复。

## D028 · 2026-11-04 · 数学哈希配方
`source_hash = sha256(原始题卡 <article>…</article> HTML 子串, UTF-8)`（legacy 只读，故永稳）；`content_hash = sha256(canonical JSON{stem,options,blocks[role,label,text]}, ensure_ascii=False, sort_keys, 紧凑分隔符)`。理由：CI 可按配方复算，原文任何字节变动可检出。

## D027 · 2026-11-04 · 数学 text 字段规范化规则
实体解码（convert_charrefs）、`\xa0`→空格、段内软换行折叠为单空格（HTML 渲染语义，非内容改写）、块级标签处断行、去行首尾空白；`$...$`/`$$...$$` 位于文本节点逐字保留；`html` 字段保存源 HTML（除图片 src 路径化外零改动）。理由：text 供检索/阅读，html 供保真与逐字节复核，双轨互补。

## D026 · 2026-11-04 · 数学分块 role 命名与答案折叠态
role 以原文分块命名：q-stem→stem、ans-body→answer、b-kaodian→kaodian、b-silu→silu、b-jiefa→jiefa、b-biaozhun→biaozhun、b-qita→qita、b-yicuo→yicuo、b-guina→guina，未登记块→role="other" 全量保留；`label` 字段保存原文 b-tag 文字（考点定位/思路引导/解法构建/标准解答/其他解法 · 举一反三/易错点与陷阱/方法归纳，各 250）。源文件 250 题答案全部为展开态（aria-expanded="true" + class show）→ answer 块统一记 `"hidden": false`（代码支持 true，遇折叠原样记录）；ans-toggle 按钮为纯交互元素不入数据（沿 D009）。

## D025 · 2026-11-04 · 数学 knowledge_points 取值
原文无结构化考点列表，唯一考点标注是 b-kaodian「考点定位」段落 → `knowledge_points=[该段原文文字]`（单条 verbatim，不拆句、不改写、不编造）。理由：满足「仅取原文标注的考点文字」；知识点结构化拆分留给后续科目专家阶段。

## D024 · 2026-11-04 · 数学 tags 与原始模块分类
`tags=["math"]`（按任务基准字面执行）；原文卡片自带的模块分类（cat-gaoshu/xiandai/gailv + cat-pill 高等数学/线性代数/概率论，140/55/55 题）另存 `category={key,label}` 字段保真。理由：既不违背任务指定的 tags 值，又不丢失原分类，前端据此重建模块筛选。

## D023 · 2026-11-04 · 数学配图 base64 落盘为 PNG 文件
20 张题目配图为内嵌 base64（单图 49–304KB，2013 年两图合计 ~456KB，必破单文件 ≤500KB 分片上限）→ 解码字节落盘 `data/math/media/img-<sha12>.png`（PNG magic 校验通过，逐像素一致，同内容按哈希去重），html 中 src 改写为相对路径，`media[]` 记路径。理由：图像字节零损失，同时满足硬性分片上限；img 标签其余属性（alt/loading/data-action）原样保留。

## D022 · 2026-11-04 · 数学分值取值
`score` 仅取解答题题面「（本题满分 N 分）」原文标记（90 题：10/11/12 分），选择题与填空题原文无分值 → `score=null`。理由：以原文为准，不编造不推断（合同第 2 章第 7 条）。

## D021 · 2026-11-04 · 数学 options 提取边界
options 仅取结构化 `div.opt`（opt-key+opt-txt 原文拼接；空 opt-txt 保留为空串）。源文件 12 道选择题选项形态异常且原始如此：7 题无 opts div、选项含 display 公式而内联于题干段落（p2020-2/p2020-3/p2021-9/p2022-3/p2022-6/p2023-6/p2023-7）；5 题 opts div 不完整、部分选项溢出到相邻段落或 opt-txt 为空（p2017-7/p2017-8/p2019-7/p2020-4/p2022-7）。处理：stem 全量保留原始形态（含内联选项与空位），options 不做二次重组、不编造。理由：保真优先于结构整齐，重组即改写。

## D020 · 2026-11-04 · 数学解析锚点与切分策略
以 `<article class="card" id="pYYYY-N">`（自带 data-year/data-cat）为唯一切分单元，实测 250 张卡与题量基准（2013–2020 每年 23、2021–2023 每年 22）完全吻合；年份/题号/题型/模块全部取自卡片自身标记，不依赖外层 year-view；每卡结构校验（1×q-stem + 1×b-daan-wrap + 7×固定分块、`<article>`/`</article>` 平衡）不通过即告警并整体判 FAIL。另做逐题 LaTeX 守恒校验：原文题卡与产出 text 字段的 `$` 数量逐题相等（250/250 通过）。

## D011 · 2026-11-04 · 题量统计口径
tools/verify_data.py 仅统计 `{year}.json` 主题库文件；`{year}.analysis.json`、`{year}.media.json` 等辅助分片不计入题量；必填字段仅检查键缺失——answer/score 为 null 视为「原文如此」，不算失败（答案以原文为准，合同第 2 章第 3 条）。

## D010 · 2026-11-04 · 408 内嵌图片分片
RAW_DATA 内 `data:image;base64` 图片抽取至 `data/cs408/{year}.media.json`，题库中以 `@@M:qid:idx@@` 占位，前端渲染时回填 `<img>`——原图可达、可懒加载、主题库文件全部 ≤500KB（合同第 6 章浏览器级防锁死要求）。

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
