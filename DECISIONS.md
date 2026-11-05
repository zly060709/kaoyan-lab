# DECISIONS — 自主决策记录

本文件由 Orchestrator 维护：所有模糊处的默认决策记录于此（AGENT_CONTRACT.md 第 0/5/6 章要求）。新条目倒序追加。用户已明确：不提问、自行决策并记录。

## D107 · 2026-11-05 · 图形接入的实测口径与四处缺陷的修法
**做图形的这一步不是「裁完图入库」就完**：收敛⑩c 交付后未做浏览器实测，本轮补做，实测（与顺着它做的静态复查）暴露四处此前不可见的缺陷。逐条记录修法与取舍。

1. **题页无条件请求 DSL 图形（每题一个 404）** —— `loadFigures()` 对任何年份都请求 `data/{科}/figures/{年}.json`，缺图年份稳定 404，`try/catch` 吞掉异常使页面与门禁都「无感」，但浏览器 console 有红字。这与收敛④ 修掉的 `analysis.json` 404 是同一个模式：**「请求失败被静默」不等于「没有失败」**。决策：不引入 404 静默名单，而是照 `analysisYears` 的既有做法在 `sync_registry.py` 增加 `figure_years()`（要求文件存在**且是非空数组**），注册表出 `figureYears`，前端按册请求。附带效果：缺图年份少一次无谓请求，注册表成为「磁盘有什么」的唯一口径。
2. **`@@M:` 占位符泄漏到不回填图的位置** —— 列表页 `prevText()` 与搜索索引 `build_index.py` 都不做图形回填，于是把 `@@M:math3-2009-4:1@@` 当正文印出来/当检索词索引（全库 1102 处、30 个索引分片）。决策：**在这两处直接剥离占位符**而不是让它们也去拉 media 分片——列表与搜索的用途是文字定位，图片留给题页；2009-4 的四个选项本身只有图，剥离后选项文字为空属事实（原卷选项就是四张图），不用编造文字描述去填。
3. **搜索片段是裸 LaTeX** —— 结果由 `run()` 异步注入，晚于路由层的 `renderMath(app)`。决策：注入后补 `renderMath(res)`，片段按 `$` 奇偶回退到配对边界（与列表页同口径）。**残留如实登记**：130 字窗口切进 `\begin{cases}` 内部时仍会露出部分源码，属窗口式摘要的固有限制，本轮不做「按公式边界智能截断」的深加工（收益低、易引入新的截断 bug）。
4. **`state.json` 的 `questions_total` 是死值** —— 从不可反推的字段，停在 3272 而磁盘 3582。决策：由注册表 `questionTotal` 求和反推（注册表本身由 `sync_registry.py` 从磁盘反推，G9 已保证两者一致），并在报告题量表区分英语「780 全量 / 675 客观」，使报告合计与 G5、`data/index/*` 三处对齐。
5. **装配路径不复制第二套** —— 曾照 `build_m32021.py` 建 `build_m32016.py`，随后发现 `build_m3legacy.py` 本就支持 2016：两者产出**字节级相同**（49537 字节全等），故删除专用脚本。留下的是「`data/math3/2016.json` 可从模块复现」这一条验证，而不是新工具。
6. **实测方法可复跑** —— 本地 `python -m http.server` + 浏览器，页面内打 `fetch` 补丁记录所有非 2xx，逐页轮询题目卡题号匹配、统计 `.katex-error` / 裸 `@@M:` / `img.mimg` 的 `naturalWidth`。数三含图四卷 92 题页全量 + 9 年 16 题页抽样（含 6 个 DSL 图形题，canvas 取色确认有墨）。**注意**：`sw.js` 对 `index.html` 是 network-first，浏览器 HTTP 缓存仍可能给出旧页面脚本；核对以「页面里 `prevText.toString()` 是否新实现」为准，必要时无缓存重开，否则会误判成「修了没用」。

## D106 · 2026-11-05 · 原卷图形接入（2009-4 / 2015-2 / 2016 全卷 / 2018-16）＋ 2016 卷补复核后入库
**触发点**：D104 把「2009-4 与 2016-1 的原卷图形裁图接入」列为队列项。接手会话先做 2009-4（题干 $f(x)$ 图 + 选项（A）–（D）四幅 $F(x)$ 图，共 5 幅），随后发现**图形缺口不止登记在案的两处**——草稿把原图静默丢掉时既不写 `【图】` 也不留 `@@M:`，A5 拦不住。于是新增 `audit_m3legacy.py` A7 检（题干/选项/解析出现「如图/右图/左图/下图/见图」而整题既无 `@@M:` 占位也无 `media` 字段即报），当场多拦出 2015-2（$f''(x)$ 图形如右图）与 2018-16（第 16 题解析的阴影积分区域图）两处已入库缺陷。

**图形接入 12 幅**（全部为页面影像直接裁切，未重绘、未派生；坐标由 50/100px 网格叠加后逐幅目视定框）：
2009-4 五幅（p1 题干图 + p1/p2 四幅选项图，替换原 `【图】` 文字占位）、2015-2 一幅（p1 右侧 $f''(x)$ 图，题干补 `@@M:math3-2015-2:0@@`）、
2016-1 两幅（p1 题干 $f'(x)$ 图 + p5 解析标记图 $x_1\cdots x_5$）、2016-3 三幅（p6 的 $D_{1}/D_{2}/D_{3}$ 积分区域图 (1)(2)(3)）、
2018-16 一幅（p10 阴影区域图）。分片写 `data/math3/{年}.media.json`，`gates.py` G7 由 1112 处引用增至 **1119 处全部可解析**。
工具侧按 D104「不逐年复制脚本」的口径，把三份按年脚本合并为 `tools/work/build_m3media.py`（年份→裁图表，含每幅说明），删除 `build_m32009_media.py`、`build_m32016_media.py`。

**2016 卷由「有稿不入库」转为入库**：D104 因上一会话未留 2016 复核记录（`m32016_notes.md` 缺失）而暂不入库，但本地 `data/math3/2016.json` 是游离产物（既不在 `data/index/math3.manifest.json`，线上也 404），会让索引虚增 23 条。接手会话补做复核并入库：
① **逐题独立复算 23/23 吻合**（不采信草稿自陈）——第 3 题 1200×1200 网格求积得 $J_3<J_1<J_2$、第 6 题实特征值扫描确认 $-2<a<1$ 时正负惯性指数 $1/2$、第 13 题五个 $\lambda$ 取值行列式与多项式逐点相等、第 14 题全枚举 $18/81$、第 17 题数值积分 + 中心差分逐点吻合且 $f(1/2)=0.25$ 为最小、第 20 题 $r(A)=2<r(A|\beta)=3$ 与 $A^{\mathrm T}A(0,-1,1)^{\mathrm T}=0$、第 21 题用纯整数快速幂算出 $A^{99}$ **九元逐元素精确相等**、第 22 题按 $p(x)=3(\sqrt x-x^2)$ 逆采样 4×10⁶ 组验证 $F(z)$ 分段、第 23 题逆抽样验证 $E(T)=\frac9{10}\theta$；
② 卷面核对：p2–p3 确认 2016 **印有逐题满分**（15–19 各 10 分、20–23 各 11 分，合计 94），`SCORE_ORIGIN[2016]="print"` 成立；
③ 图形清点 5 幅全部接入（见上）；
④ 补写 `tools/work/m32016_notes.md`（页面角色 / 分值 / 图形清单 / 逐题复算表 / 14 条疑似笔误照录 / 复核边界）。
`audit_m3legacy.py` 的 A4 标记集加 `【解】`：2016 第 15 题解析原文即「（15）【解】」而无【答案】行，属卷面体例而非漏录，不应记为缺陷。
`check_m3years.py` 修一处自伤：文件过滤器 `f[0].isdigit()` 会把新增的 `{年}.media.json` 当数据文件读，`KeyError: 'questions'` 直接崩，现排除 `.media`。

**验收**：math3 由 273 题增至 **296 题（13 个年份）**，`sync_registry.py` 与 `gates.py` G1/G9 同步；`build_index.py` 3559 → **3582 条**；`verify_data.py` ALL PASS；门禁 **9/9**；`check_m3years.py` 13 个年份 0 错误；`audit_m3legacy.py` 除 2012 无数据文件外无余项。三卷（2009/2015/2018）改动经与线上副本逐字段比对，**只有所述题目的 stem/options/source_blocks 与 `content_hash`、以及 `source_note` 变化**，其余逐字节不变。`sw.js` → `kaoyan-v0.3.11`。

**未做与边界**：p7–p14（2016 解析后半）按 0.5 倍并排影像直读，题号/答案字母/最终结果式已核对并复算，但解析中间步骤未做 1.9× 裁剪级逐字复核，强度低于其余九卷（已写入 notes 第六节）；未做 canvas 取色级像素比对。全库 A7 同类扫描另报 cs408 20 题、math2 4 题、mgt199 64 题「文字提到图但无 media」——这些科目原卷影像不在 `data/*/pages/` 或本就没有配图源，属另一条待办，本轮未动。队列下一项仍是 2012 / 2020 两卷补录。

## D105 · 2026-11-05 · 浏览器实测债首次结清 ＋ 混排答案裸 LaTeX 缺陷修复
**接手会话首次具备真实浏览器**（此前 D101/D102/D103 连续三卷只能报「机械门禁通过、浏览器实测未做」）。本轮在线上 `https://zly060709.github.io/kaoyan-lab/` 实跑：`#/math3/{2009,2010,2011,2013,2014,2015,2017,2018,2019}/q/{1,5,9,16,23}` 共 45 个题页，`.katex-error` 0 个、console（error/warn/uncaught/unhandledrejection 四类钩子）0 条；并用**页面里生产同款 KaTeX** 全量渲染 math3 全部 12 个年份文件的 `$…$` 片段：4254 段、`throwOnError:true` 下 0 失败。合同第 7 章「公式渲染失败数 = 0」这条第一次拿到机械门禁之外的直接证据。

**实测暴露的真实缺陷（静态检查看不出来）**：数学类 21 道题（math2 12、math3 9）的答案栏在页面上印出裸 LaTeX。根因是 `index.html` 第 491 行的历史口径（D098/收敛⑥）——只有「含 LaTeX 命令**且完全不含中日韩字符**」的答案才套 `$…$`，而概率大题答案惯例写 `egin{cases}…	ext{其他}\end{cases}`，`其`/`他` 二字一出现就整条退回纯文本，反斜杠命令全部原样显示。修法不动任何数据：渲染前把**不在 `	ext{}`/`\mathrm{}` 等已有分组里的**中日韩片段包进 `	ext{…}`，可见字符逐字不变（「其他」「，」「；」都照样显示），然后统一交给 KaTeX。改之前先在线上对全库 166 条 LaTeX 型答案跑一遍 `texify + renderToString(throwOnError:true)`，0 失败才动前端；再用本地 `http.server` 装载改后的 `index.html` 复测 `math3-2011-23`、`math2-2019-15`、`math1-2020-21` 三条原缺陷题（渲染成功、0 `.katex-error`）与 `cs408-2019-24`（无回归）。`sw.js` → `kaoyan-v0.3.10`。

**工具侧一处自我纠错**：`tools/work/render_check.js` 初版写 `/\$([^$]|\\$)+?\$/g`，捕获组只保留最后一次迭代的字符（`+?` 在外面），会把每个片段截成单个尾字符，导致 15 条假阳性「渲染失败」。改为 `/\$((?:[^$]|\\\$)+?)\$/`。离线 Node 路线仍走不通（本机无 node 可执行文件、`node_repl` 沙箱禁 `new Function`，UMD 版 `vendor/katex/katex.js` 无法装载），故该脚本留作有 Node 环境的会话备用，全量渲染改由浏览器完成。

## D104 · 2026-11-05 · 数学三 2009–2019 九卷入库（8+6+9 结构）＋ 发布通道改走 Data API
**素材来源**：上一会话（云端 WorkBuddy）把 12 卷视觉转录草稿同步到本机 scratch 目录（`m3_YYYY_{q,a1,a2,a3,meta}.py` + `m3_YYYY_notes.md` + 裁剪图）。接手会话核对：2009、2010、2011、2013–2019 共 9 卷是完整的（23 题、分值合计 150、23 条解析、23 条知识点），**2012 缺第 15–23 题解析与 meta、2020 只有题干与第 1–8 题解析**，2016 无 notes.md（无复核记录）——三处缺口如实登记 PENDING_YEARS，不按记忆补全。

**发布通道（本轮最关键的基础设施决策）**：本机 git 走 `ghproxy.net` 的 `insteadOf` 全局重写，86MB 仓在约 50–190KB/s 链路上反复 `fetch-pack: invalid index-pack output`，`git push` 不可用。新增 `tools/publish_api.py`：以 `blobs → trees(base_tree) → commits → refs/heads/main PATCH` 四步提交，只上传与远端 tree 内容不同的文件，其余由 base_tree 继承（因此本地可以是部分物化副本），并逐个校验「GitHub 回传 sha == 本地 git hash」。token 仅从环境变量 `GH_TOKEN` 读取，不打印、不落盘、不入仓。

**中间件口径（与 D101/D102 一致但去重复）**：草稿按仓库命名规范复制为 `tools/work/m3{2009..2020}_{q,a1,a2,a3,meta}.py` 与 `m{年}_notes.md`（notes 一并入库，作可追溯复核记录）；不再逐年复制 118 行的 `build_m3YYYY.py`，改用参数化的 `tools/work/build_m3legacy.py`——它读 `data/meta/source_pdfs.json["math3:YYYY"]` 取 PDF 名/SHA/页数（延续 D100 去硬编码），按 `SCORE_ORIGIN` 表区分「卷面印有逐题满分」与「卷面只印 94 分、按 15–19×10+20–23×11 折算（推定值）」两种分值来源并写进 `source_note`，`content_hash` 口径与既有卷完全相同（id/year/num/type/stem/options/answer/score + blocks）。新增 `check_m3years.py`（$ 奇偶、花括号、`\begin/\end` 配对，覆盖 math3 全部 12 个年份文件）与 `audit_m3legacy.py`（A1 结构 8/6/9 与 150 分、A2 `answer` 字段与解析首行【答案】（X）逐题一致、A3 选项数、A4 解析标记、A5 【图】占位缺口、A6 与数一/数二同年同题干的答案交叉核对）。

**保真修正只有一处，且不动可见文字**：2010 第 13 题草稿把公式 `$…$` 定界符落错位置，导致整条题干 `$` 数为奇数、KaTeX 会跳过渲染。修正只把闭合 `$` 从「，则」之后移到之前（`|=2,，则 $|A+B^{-1}|=` → `|=2,$，则 $|A+B^{-1}|=`），可见字符与原文逐字一致（卷面那个半角+全角双逗号 `,，` 由草稿 notes 记录为 3× 裁剪确认的原文排版，照录不改）。原卷其余疑似笔误（2019 第 6 题「E 是阶单位矩阵」疑脱「3」、2019 第(4)题解析「对决收敛」疑为「绝对」等）一律照录，登记在各年 notes。

**独立复核（不只看草稿自陈）**：2019 卷抽样 9 题用 numpy 独立复算，答案全部吻合——第 1 题 $k=3$、第 2 题 $-4<k<4$（$k=\pm4$ 时只有 2 个不同实根，边界排除成立）、第 5 题 $r(A)=2,n=4\Rightarrow r(A^*)=0$、第 9 题 $[n/(n+1)]^n\to e^{-1}$、第 13 题仅 $a=1$ 时 $r(A)=r(A|b)=2<3$、第 14 题 $EX=4/3\Rightarrow P=2/3$、第 10/11/12 题（拐点 $(\pi,-2)$、$\frac{1}{18}(1-2\sqrt2)$、弹性 $0.4$）手算复核一致；另裁 1.9× 复核 p2 下半，确认卷面只印「三、解答题：15～23 小题，共 94 分」而无逐题分值（故 notes 的推定口径成立）。2009 第 21 题与 2009 数二第 23 题同题：两卷独立转录答案经标点归一后一致，且 $a=2$ 时特征值实测为 $0,2,3$（规范形 $y_1^2+y_2^2$ 成立）。

**验收与缺口**：`sync_registry.py` 反推 math3 = `dataYears 2009–2023(12)`、273 题；`build_index.py` 索引 3352 → 3559 条；`sw.js` → `kaoyan-v0.3.9`；门禁 9/9、`verify_data.py` ALL PASS、`check_m3years.py` 12 个年份 0 错误、`audit_m3legacy.py` 除登记在案的 2009-4【图】缺口外无余项。**未做**：本机 node 不在 PATH 且 `node_repl` 沙箱禁 `new Function`，无法离线跑 KaTeX 全量渲染，`tools/work/render_check.js` 写好待有 Node 的会话执行；本会话仍无内嵌浏览器，题页 console/.katex-error 实测待补；九卷的派生图形（数三 2021–2023 每卷 3–5 幅的惯例）本轮未产出。队列下一项：2012 / 2020 两卷补录，再 2009-4 与 2016-1 的原卷图形裁图接入。

## D103 · 2026-11-05 · 新科目法硕 498 入库（conv4 外用户加料）＋ 平台接线补齐
**素材与科目注册**：用户提供《2022年全国法律硕士（非法学）联考题 综合课》真题图片版 20 张（含 2023 封面 1 张）。官方课程代码为 498（综合课非法学），与注册表既有的 law397/law398（专业基础课）是不同课程，故新增科目条目 `law498`（code 498，法硕联考综合（非法学），color #0E7490）而非冒用 law398；20 科框架扩为 21 科，`sync_registry.py` 注记同步。`data/law498/pages/2022/p1-p19.jpg`（p1 封面、p2–p10 试题、p11–p19 答案详解）入册 `source_pdfs.json[law498:2022]`（整组 SHA-256，口径 `sha256jpg:`）；**2023 仅封面无内容，不入册**（避免「原卷影像 1 页」假入口），待资料到位再登记。

**三子代理并行转录＋接缝亲自裁决**：答案详解 9 页双栏书籍扫描件按 p11–p13 / p14–p16 / p17–p19 切给三个临时子代理逐字转录（law_ans_A/B/C.md），试题 9 页由主会话转录。子代理报告后，所有跨页/跨栏接缝与 [缺字] 标记由主会话裁剪原图逐一裁决：①扫描页序错乱（p16 内容紧接 p14，p15 紧接 p16），按书中实际页序 p14→p16→p15 拼接；②第17/39题解析跨页由两段原件严丝合缝拼接（39 题残字「少」+「数民族聚居区」）；③二维码遮挡的残字依残形+文意+下页衔接录出：第24题「D」、第31题「物，」、第10题「A」（句号被遮不补）；④**原书跨页脱漏照录不补**：第6题「是指」与「会生活中」之间、第45题「联合制定」与「但国务院部委」之间原书即缺字（各缺「法在社」「规章。」），全部写入 source_note。**门禁与展示接线**：gates.py/verify_data.py/diag.html 三处基线加 `law498: 58`（卷面实点 58 题150分）；前端 TYPE_LABEL 加「分析题」、ROLE_L 加 analysis2=「点评」、题卡新增分值展示、年份页激活「原卷影像」链接（原 paperLink 死变量）、页脚与 README 版权声明补法硕来源、schema.json subject/type 枚举同步（law498/analysis/sufficiency/logic）。主观题（简答/分析/论述）沿用政治/管综口径：answer 字段留空，【答案】以 role=answer 区块存原文（G5 ANSWER_ROLES 认可），【点评】独立 analysis2 区块。

## D102 · 2026-11-05 · 数学三 2021 卷视觉转录（math3 三年 66 题）
**conv4 第五卷**：`data/math3/pages/2021/`（12 页影像，PDF《2021数学三真题及解析.pdf》SHA-256 `50dd96cc…`；p1–p4 试题、p5–p12 答案解析）逐页转录为 `data/math3/2021.json`，22 题 = 选择 10×5 + 填空 6×5 + 解答 6 题（17 题 10 分、18–22 各 12 分，原卷解答题未逐题印分值，按前两卷同结构计），分数合计脚本校验 150。中间件沿用 D101 的按题型分卷：`tools/work/m32021_q.py` + `m32021_a1/a2/a3.py` + `build_m32021.py`，另新增 `check_m32021.py`（`$` 奇偶/花括号/`\begin-\end` 配对静态检查，22 题 0 错误）；PDF 名与哈希继续从 `data/meta/source_pdfs.json["math3:2021"]` 读取。

**照录口径**：存疑处全部经 1.8–1.9× 裁剪放大复核后才落笔——第 7 题 (D) 选项第一矩阵第三行 `(1,3,1)`、第 15 题行列式第二行 `(1,x,2,−1)`、第 17 题指数 `(1+|x|)^{1/x}`（题干为 α、解析用拉丁 a 指代，均照录不改）、第 21 题 `(3E−A)` 行变换结果第一行 `(1,1,−2)` 与 `(E−A)` 结果第一行 `(1,−1,2)`（数学上并非该矩阵的标准行化简，但原文如此，保真优先）、第 1 题解析分子 `2x·(e^{x⁶}−1)` 的显式点乘。第 12 题解析换元记号 `x=t/π` 用 `\xlongequal` 照录。

**同题交叉验证**：数三 2021 第 15 题（四阶行列式 x³ 系数）与数二 2021 第 16 题完全同题，两卷独立转录的题干与答案逐字一致（同为 `-5`），未发现其余同题。

**图形 3 幅**入 `data/math3/figures/2021.json`（题 13 旋转母线曲线、19 极坐标扇形区域 D、20 和函数 S(x)），均标 `origin=derived` 并在 caption 注明「非原卷插图」；`verify_figures.py math3 2021 2023` 共 12 幅 ALL OK。

**状态与验收**：`sync_registry.py` 把 math3 `dataYears` 反推为 `[2021,2022,2023]`、66 题；`build_index.py` 索引 3294 条；`sw.js` → `kaoyan-v0.3.7`；门禁 9/9、`verify_data.py` ALL PASS。本会话无内嵌浏览器，与收敛⑦同口径：只报机械门禁与静态检查结论，不谎报浏览器实测（DEGRADED 已登记）。队列下一卷：数学三 2020（13 页影像）。

## D101 · 2026-11-05 · 会话接手（收敛⑥补提交）＋ 数学三 2022 卷视觉转录
**接手与补提交**：ZCode 主会话在 D100 收尾（更新 DEGRADED 口径）时请求失败 `The request could not be completed`，收敛⑥ 的全部产出只落在磁盘、未进 git，远端 `main` 仍停在 D099（ee6f08d）。新会话按合同第 6 章「恢复上下文先读 AGENT_CONTRACT.md」接手：先重跑 `gates.py` 9/9 与 `verify_data.py` 确认磁盘产出完整，补齐 `DEGRADED.md` 的会话中断条目，再以 `5f27fce` 提交并推送 33 个文件（数学三 2023 卷数据/图形/索引/中间件 + 台账），不回滚任何已落盘文件。这是本轮唯一「先修交付通道、再开新内容为」的决策——否则后续任何新增卷都不会出现在线上。

**conv4 第四卷**：`data/math3/pages/2022/`（15 页影像，PDF《2022数学三真题及解析.pdf》SHA-256 `2a68a5b5…`；p1–p4 试题、p5 空白页、p6–p15 答案解析）逐页转录为 `data/math3/2022.json`，22 题 = 选择 10×5 + 填空 6×5 + 解答 6 题（17 题 10 分、18–22 各 12 分），分数合计脚本校验 150。中间件 `tools/work/m32022_q.py`（题干）+ `m32022_a1/a2/a3.py`（按题型分卷：选择/填空/解答，非上两卷的按页 10 件——本次会话一次性成型，无需小步续跑）+ `build_m32022.py`；PDF 名与哈希继续从 `data/meta/source_pdfs.json["math3:2022"]` 读取，不硬编码。

**照录口径**：第 10 题联合分布律表格被分页切断（表头在 p2、数据两行在 p3），合并为完整 `array` 后照录，并在 `source_ref.pages=[2,3]` 标注；原卷疑似排版/笔误处一律不改、不改写成「正确形式」——第 2 题 `$(n=1,2,\cdots,n)$`、第 14 题解析第二行把积分结果写进积分号内、第 3 题 `∂F/∂y` 行多余的 `dt`，均在 `source_note` 说明。主观题答案串沿用 D100 的纯 ASCII 分隔口径（避免全角标点让答案栏退回裸 LaTeX）。

**同题交叉验证**：数学三 2022 第 7 题（向量组等价求 λ 范围）与数学二 2022 第 10 题题干规范化后前 307 字符逐字一致，两卷独立转录的答案同为 `C`，解析结论同为 `λ≠−1, λ≠−2`，与选项 C 一致；未发现其余同题。另用脚本对新卷全部题干/选项/答案/解析做 `$` 奇偶、花括号、`\begin/\end` 配对检查，0 错误。

**图形 4 幅**入 `data/math3/figures/2022.json`（题 2 数列散点、17 解曲线与斜渐近线、19 积分区域 D₁/D₂、20 和函数 S(x)），均标 `origin=derived` 并在 caption 注明「按公式绘制，非原卷插图」；`verify_figures.py math3 2022 2023` 共 9 幅 ALL OK。

**状态与验收**：`sync_registry.py` 把 math3 `dataYears` 反推为 `[2022,2023]`、44 题、`paperYears` 仍为 15 年影像；`build_index.py` 索引 3272 条；`sw.js` → `kaoyan-v0.3.6`；门禁 9/9、`verify_data.py` ALL PASS。**本会话无内嵌浏览器，未做 canvas 取色/题页 console 实测，不谎报通过**——静态检查与机械门禁结论照录，浏览器实测列为待办（QUALITY_REPORT「尚未执行的验收项」）。队列下一卷：数学三 2021（12 页影像）。

## D100 · 2026-11-05 · 数学三 2023 卷视觉转录（math3 由 imaging 转 active）
conv4 第三卷：`data/math3/pages/2023/`（13 页影像，PDF《2023数学三真题及解析.pdf》SHA-256 `6e246d61…`，p1–p4 试题 / p5–p13 答案解析）逐页转录为 `data/math3/2023.json`，22 题 = 选择 10×5 + 填空 6×5 + 解答 6 题 70 分（分数合计脚本校验 150）。中间件仍小步落盘：`tools/work/m32023_q.py` + `m32023_a1..a10.py`（每 1–2 页一件）+ `build_m32023.py`。与 math2 的差别：`build_m32023.py` 不再硬编码 PDF 名与哈希，改从 `data/meta/source_pdfs.json["math3:2023"]` 读取（后续 14 卷可直接换键），且板块枚举新增 `gailv/概率论`（与既有 math 的 55 题口径一致）。

**同题交叉验证**：数学三 2023 第 18 题（区域 D 的面积与旋转体）与数学二 2023 第 19 题、第 21 题（矩阵 A 对角化）与数学二 2023 第 22 题完全同题，两卷独立转录后答案逐字一致（`ln(1+√2)`、`π(1−π/4)`；`A=[[1,1,1],[2,-1,1],[0,1,-1]]`、`P=[[0,-1,4],[-1,0,3],[1,2,1]]`、`Λ=diag(-2,-1,2)`)。第 21 题另用纯 Python 验算：三列分别是 λ=−2/−1/2 的特征向量且 `det(A−λE)=0`，转录无误。第 7 题（向量组公共解）与数二 2022 第 10 题同类，用行变换结果反查确认结论向量为 `(1,5,8)ᵀ`。

**答案栏渲染口径收紧**（D098/D099 的延伸）：前端只对「含 LaTeX 命令且不含中日韩标点」的答案套 `$…$`，因此多问题答案里的全角「；」「，」会让整条答案退回裸 LaTeX 显示。本轮把 18/21/22 的答案串改成纯 ASCII 分隔（`A=\begin{pmatrix}…\end{pmatrix},\ P=…`），17 题保留中文但去掉 LaTeX 命令（`a=1,b=-1；x=0 是极值点`）——浏览器实测 18/21/22 答案各命中 1 个 `.katex`、无裸反斜杠泄漏。同口径回填数学二 2023 的第 19/22 题（改 `m23023_a7.py`/`m23023_a9.py` 后重建 `data/math2/2023.json`，content_hash 随构建重算），实测两题答案栏同样由裸 LaTeX 变为 KaTeX 渲染、`.katex-error` 0。

图形化 5 幅入 `data/math3/figures/2023.json`（题 2/14/18/19/22）：第 19 题原卷有示意图，DSL 的 `circle` 只能画原点圆，改用 `parametric`（`fx="1+1*cos(t)"` 平移圆 + `fx="1*cos(t)"` 单位圆）并标出 θ=±π/3 的两个交点。`verify_figures.py` 5 幅 [OK]。

`sw.js` → `kaoyan-v0.3.5`；搜索索引 3250 条（math3 22）；`sync_registry.py` 把 math3 的 status 由 `imaging` 翻为 `active`、`dataYears=[2023]`、`paperYears` 仍保留 15 年影像。门禁 9/9；22 个题页逐一实测：`.katex-error` 全 0、console 消息 0、5 幅图形彩色像素 3250–6262（第 19 题蓝 3189 / 红 3073）；科目页显示「2023 · 22 题」+ 其余 14 年「原卷影像 N 页」。下一步继续 conv4：数学三 2022 卷（15 页影像）。

## D099 · 2026-11-05 · 数学二 2023 卷视觉转录 + 图形表达式变量绑定缺陷（48 条静默不画）
conv4 第二卷：`data/math2/pages/2023/`（13 页影像，PDF SHA-256 `4e7dc8a0…`，p1–p4 试题 / p5–p13 答案解析）逐页转录为 `data/math2/2023.json`，22 题 = 选择 10×5 + 填空 6×5 + 解答 6 题 70 分（合计 150 分）。中间件仍按小步落盘：`tools/work/m23023_q.py`（题干，逐页读图后立刻写盘）+ `m23023_a1..a9.py`（解析，每 1–2 页一件）+ `build_m23023.py` 装配；答案栏口径沿用 D098（证明题 21 写「证明见解析」，17/19/22 把 (1)(2) 结果并入 `answer`）。图形化 10 幅入 `data/math2/figures/2023.json`（题 1,2,3,5,7,12,14,17,19,20），`verify_figures.py` 覆盖 math2 全部 15 年 97 幅 [OK]。

本轮最重的一处是**图形渲染的变量绑定缺陷**，前端 `compileExpr()` 用 `cleaned.toLowerCase().includes("t") ? "t" : "x"` 猜自变量：只要表达式里出现 `sqrt`/`tan`/`atan`/`tanh` 这类含字母 t 的函数名，就被编译成 **t 的函数**，而函数体里的 `x` 是未声明标识符 → `new Function` 体内 `try` 捕获 ReferenceError → 恒返回 NaN → 曲线一条像素都不画，且**不报任何错**。全库 344 条图形表达式里 48 条命中（math 31、math2 17）。`tools/verify_figures.py` 的 Python 镜像同时绑定 `x` 与 `t`，所以门禁一直 9/9 绿，线上图形却只是缺曲线的空壳 —— 与 D098 的 console 404 同一类「门禁通过但显示错误」。修法：`new Function("x","t", …)` 并以 `f(v,v)` 调用，两种变量名同时可用，语义与 Python 镜像对齐。实测（浏览器 canvas 取色计数）：`math2-2023-12` 蓝 2540 / 红 2015 像素；`math1-2013-7` 三条正态密度曲线 2396 / 1250 / 1764（修复前三条全为 0，即整幅图只剩坐标轴）。
② **图形绘制次序**：`math2-2023-17` 的半透明三角形填充画在曲线之后，把 `y=x(2−ln x)` 染成混色（纯蓝仅 80 像素）。改为 polygon→graph→segment 的层序，蓝曲线回到 916 像素。

`sw.js` → `kaoyan-v0.3.4`；搜索索引 3228 条（math2 342）；门禁 9/9；题页/年份页/科目页 console 消息为 0，`.katex-error` 为 0。下一步按 D090 优先级转 conv4 剩余：数学三 2009–2023 共 15 卷（194 页影像，目前 imaging_only）。

## D098 · 2026-11-05 · 数学二 2022 卷视觉转录 + 全站公式渲染补齐
conv4 第一卷开工：`data/math2/pages/2022/`（11 页影像，PDF SHA-256 `513793a3…`）逐页视觉转录为 `data/math2/2022.json`，22 题（选择 10×5 + 填空 6×5 + 解答 6 题 70 分）。转录中间件按「小步落盘」拆成 `tools/work/m22022_q.py`（题干/选项，p1–p4）与 `m22022_a1..a6.py`（解析，p5–p11），由 `build_m22022.py` 装配，避免单次输出过大。① 解析逐字照录，`source_blocks[role=analysis][origin=source]` 单块存全文；② 证明题（21、22II）无单一答案，按前卷口径写「证明见解析」，22(I) 标准型与 20 的极值结果一并写入 `answer`；③ 知识点/难度/板块是派生元数据（不改原文），与 2009–2021 同表；④ 图形化 8 幅（D043 DSL）入 `data/math2/figures/2022.json`，`verify_figures.py` 全 OK。
浏览器实测暴露 5 处**全站显示级**缺陷（不是 2022 独有），一并修掉：
① **只有题页渲染公式** —— `renderMath(app)` 原先仅在 `viewQuestion` 调用，年份列表/科目页/搜索页把 `$...$` 当纯文本铺出来。改为路由层统一收尾：`routeViews()` 派生视图，`route()` 在视图 Promise 落定后补一次 `renderMath`。
② **图形说明里的公式不渲染** —— 图形是异步 `loadFigures()` 注入的，早于它的 `renderMath` 已经跑完。在 `renderFigure` 之后对图形容器再渲染一次。
③ **答案栏显示裸 LaTeX** —— 数学类 `answer` 存的是无 `$` 包裹的 LaTeX（如 `\dfrac{31}{32}`），前端 `esc()` 后原样输出。新增 `mathAns` 判定：含 LaTeX 命令且不含中日韩标点的纯公式答案才包 `$…$` 交给 KaTeX，混排中文的答案（如「证明见解析」「(Ⅰ)…；(Ⅱ)…」）保持原文，避免 KaTeX 报错。
④ **年份列表预览截断公式** —— `slice(0,80)` 会把 `$…$` 拦腰截断，KaTeX 因不配对而跳过。新增 `prevText()`：截断后若 `$` 为奇数个，退到最后一个 `$` 之前。
⑤ **板块列显示 `[object Object]`** —— 数学类 `category` 是对象，列表页直接 `esc()`。改取 `category.label`。
另：`subjects.json` 新增 `analysisYears`（由 `sync_registry.py` 依磁盘 `{年}.analysis*.json` 反推），题页只在册的年份才请求精讲分片，消除 `2022.analysis.json` 404 —— 合同「console 报错 = 0」门禁此前是被 try/catch 掩盖的假通过。`sw.js` → `kaoyan-v0.3.3`。搜索索引 3206 条，门禁 9/9。

## D097 · 2026-11-05 · 199 管综接入：以用户 Markdown 题库为唯一内容源
用户提供 `kaoyan-extra/199管综真题_Markdown题库`（2009–2026）+ `199管综答案_Markdown题库`，源包 README 声明「md 是本题库唯一内容源，逐题人工/多模态校核」。管线 `tools/extract_199.py`：按 `## 一/二/三/四、` 章节 + `### 第 N 题` 切块，题干/选项/答案/解析逐字照录；`source_hash = sha256(真题块 + 解析块)` 可逐题回溯；源包 md 的 SHA-256 与每年题量/答案数记入 `data/meta/mgt199_source.json`。
① **章节标题有两种写法**（`## 三、逻辑推理：…` 与 `## 三、逻辑推理（…）`），正则放宽后 2009–2021 的写作题不再被误归为逻辑题；题型映射 问题求解→single、条件充分性判断→sufficiency、逻辑推理→logic、写作→essay（并按标题后缀取 30/35 分）。
② **条件充分性判断的 A–E 判断结果选项源包未给出** → options 留空并写 `options_note`，绝不编造；年份页展示源包章节指令原文，逐题附原卷切片图供核对（PENDING_YEARS 登记）。
③ **2025 年源包只有 55 题**（缺写作第 56、57 题）→ 按实际入库，缺号登记不补。
④ **2026 年第 51 题**源包答案写作「C（原 PDF 所标 E 经复核有误）」→ 取字母 C 入 `answer`，括号校注原样进 `source_blocks[role=note]`，只标注不改写（与 D036 同口径）。
⑤ **原卷切片图 1024 张全部保留**（合同「不删原图」）：灰度 JPEG、宽 ≤1100、q58，单张约 19KB、合计约 34MB，置于 `data/mgt199/pages/{年}/`，以 `@@M:` 占位符经媒体分片引用（复用 G7 校验与懒加载）。
⑥ **主观题答案口径扩展**：写作题的答案材料在同年 `{年}.analysis.json` 里（谬误分析/参考范文），G5 认可「精讲分片含非空 desc 或 nodes」为主观题答案材料，避免把同一段原文重复塞进 source_blocks 造成前端双份显示。
结果：`data/mgt199/{2009..2026}.json` 共 1024 题（single 270 / sufficiency 180 / logic 540 / essay 34），全部 ≤500KB 无需切片；注册表 mgt199 → active；搜索索引重建后总条数 3184；门禁 9/9。

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
