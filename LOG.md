# LOG — noss-to-wim Project Activity Log

> **Concept:** Append-only narrative of what was done, when, and why — inspired by Andrej Karpathy's "LLM wiki" / dated-micro-essay approach. Each entry is a small self-contained chunk so any LLM reading the log can reconstruct context quickly. Newest entries at the top.
>
> **Rules:**
> - One entry per working session (or per meaningful milestone)
> - ISO dates (`YYYY-MM-DD`)
> - Lead with **what changed** then **why** then **what's next**
> - Keep entries scannable — bullets over prose
> - Do not edit old entries (append corrections as new entries)

## [2026-08-26] revision | N821 Office Admin SOALAN — full TUGASAN rewrite per Jennifer 00:52 feedback

**What:** Jennifer (00:52 MYT) provided a complete TUGASAN example for N821 Office Admin using CHARACTER International Academy's own company scenario (ADI seminar). Rewrote SET A and SET B SOALAN to match.

**Changes:**
- SET A: Replaced fictitious "Nexalink Corporate Services" scenario with Character Academy ADI seminar (20/11/2026, Classic Hotel, 40 pax, TAN SIOW INN, RM100/pax). 6 tasks: venue letter (C05), invitation letter (C06), sign-in list (C01), questionnaire (C01+C06), budget plan (C02), payment voucher (C02).
- SET B: Replaced "Ceria Furniture Industries" with Character Academy annual graduation ceremony (15/12/2026, Grand Palace Hotel, 60 pax). Parallel 6-task structure.
- Updated BAHAGIAN 5 oral section: changed inventory item code from `NLK-ST-003` to `CHAR-ST-003/007`.
- Built new DOCX for both sets; uploaded to Drive as `[N821 SET A/B SOALAN 26.08 v2]`.
- Sent 3 before/after comparison images to Jennifer via WhatsApp.

**Why:** Jennifer's 00:52 message explicitly provided an example TUGASAN. The old scenario (fictitious company) was inappropriate for students of Character Academy.

**Next:** Update SKEMA for both sets to match new TUGASAN. Monitor Jennifer for further feedback.

---

## [2026-08-25] engineering | NOSS→PPT-PPA 校验引擎 + JPK 排版管线；FB-018-3 SET B 重做至 0 错误

**触发：** Jennifer 2026-08-24 22:37–2026-08-25 00:08 WhatsApp 审阅（84 条消息，其中 33 条语音/图片，
23 条语音经本地 Whisper 转录）。她退回 8 月 23 日的交付，提出 10 项要求，其中「汽车买卖不能用，
汽车有自己的 NOSS」**只存在于语音里**——而我方 `fb-018-3-set-b-soalan.md` 整份是汽车场景。

**根因（排版）：** `build/ppa_integrate.py` → `wim_md_to_docx.py --style KP` 使用
`build/_templates/reference-textbook.docx`，其 `Normal` 样式为 `Source Serif 4` + `JUSTIFY`。
Jennifer 的 Mac 无此字体 → Word 回退成等宽字体（她截图里的「打字机效果」并不在源文件中）；
JUSTIFY 在短行上撑出字间空隙（她说的「跳来跳去」）；pandoc 表格样式 borders=none（「没有画线」）。

**新建 `_engine/`：**
- `ppa/schema.py` — NOSS 能力图谱 + 选择档（profile）的 dataclass。CU 的评估模式
  （practical/oral/excluded）是**输入**，永不由模型推断。
- `ppa/validate.py` — V01–V10。V10（评分表对账）是在发现改写 agent 谎报
  「totals reconcile」后当场补的：它删了 C02 实操分却未重分配 6%，全卷合计 94%。
- `ppa/worksheet.py` + `cli.py worksheet` — 生成马来文 CU 选择表，附时间容量模型
  （实操工位 ~48 min + 口试 30 min + 交卷 10 min → 3 小时约容纳 2 个实操 CU）。
- `cli.py lint` — 免 profile 的三项检查（语言/分数/页数），供尚未定 CU 的考卷体检。
- `render/ppa_docx.py` — JPK 专用 docx 渲染：Arial（强制 ascii/hAnsi/cs/eastAsia 四个字形槽）、
  全局左对齐、直接写 `w:tblBorders`（改 table.style 无效，pandoc 直接格式会覆盖样式）、
  Jata Negara 徽章、`w:tblHeader` 表头跨页重复、`w:cantSplit`、页脚参考编号+页码。
- `render/integrate.py` — 渲染→数页→回填 `⟪PAGES⟫`→重排→稳定→导 PDF→按 mtime/size 验证。

**图谱（6 份，41 CU / 217 WA / 750 PC）：** fb-018-3, fb-018-4, fb-018-5, g471-001-3,
m731-001-3, n821-001-3。逐条转录自 `raw/noss-character/txt/*.txt`，**照录不改**，
NOSS 原文自身的 20 处错漏全部记入 `source_notes`（含 N821 正文第 6 节 C07 作
"Staff Administration Supervision" 而其 CPC 图表作 "Office"——标准自相矛盾）。

**FB-018-3 SET B 交付（366 errors → 0）：**
- 首扫分布：V05 语言 335 · V04 已排除单元 20 · V06 封面 4 · V08 页数 4 · V02 实操 3 · V03 口试 2 · V07 时长 2
- 改动：全文单 BM · C01/C04/C05 实操 · C02/C03/C06 → 10 题口试（各题标注 PC 编号）·
  E01 全删（4 份文件 grep `E01|inventor|stok` = 0）· A. TEMPOH 3 JAM + 时间预算表 180 min ·
  中心名由 `VIZTECH TRADING SDN. BHD.`（**别家中心**，从参考样本误抄）改为
  `CHARACTER INTERNATIONAL ACADEMY SDN. BHD.`；场景公司另名 `Sinar Elektronik Sdn. Bhd.`
- 页数声明经渲染回填：SOALAN 19pp、SKEMA 23pp，与 PDF 实际页数一致（Jennifer 自己的样本此处
  两份都写错：soalan 写 13 实际 14，skema 写 14 实际 11）
- 归档：汽车版 SET B 与电器版 SET A 原件移入 `output/jennifer-ppa-soalan/_archive-2026-08-25-superseded/`

**校验器抓不到、人眼复核（PDF→PNG）才发现的两处：** ① CU 清单因缺空行被 pandoc 当作续行，
塌成一段跑马字 → 改为表格；② 无表头 markdown 表格经 pandoc 后首个**数据行**变 row 0，
被渲染器当表头涂灰 → `NAMA CALON` 填写栏长得像列标题。已在 `_is_header_row()` 中修正
（含填空下划线或空单元格的行不是表头）。

**其余 5 个 NOSS 体检（`cli lint`，44 份文件）：** 799 个待修问题，其中 775 为语言混排。
分布：FB-018-45 L4 = 258 · L5 = 201 · G471 = 129 · N821 = 120 · M731 = 67 · FB-018-3 = 0。
**未动其 CU 结构——CU 选择是 Jennifer 的决定**，6 张选择表已生成于 `_engine/worksheets/`。

**打包：** `.claude/skills/noss-ppa-generator/SKILL.md`——回应 Jennifer 00:08 的元需求
（「上传 NOSS + 告诉它要选的 CU → 自动出 soalan 和 skema」）。七步流程，第 3 步「填 CU 选择表」
由人执行，是整套设计的心脏。

**发布：** https://academy.wenjyue.com/engine.html （新页，explain-layman-html 风格）。
`/` 与 `/brief/` 顶部加更新横幅指向新页；线上旧版已备份为 `*.bak-20260825`。
三个 URL 均 HTTPS 200，本地/线上 md5 逐一比对一致。

**尚未处理 / 须 Jay 或 Jennifer 决定：**
- 中心名称改动为推断（依据 beauty L3 已批准卷），**未经 Jennifer 确认**
- Jennifer 的 SET A（房产版）在 Drive 与本地均未找到，须向她索取
- 8 月 23 日上传至她 Drive 的 FB-018-3 SET B（汽车版）**尚未撤下**
- 其余 5 个 NOSS 的 CU 选择表尚未发给她
- 她样本中的 ASSESSMENT ANSWER SHEET / EQUIPMENT VERIFICATION 原件**仍未审**
- 「三个 CU 仅以口试验证是否满足 JPK 对 PPA 的要求」——**须 PPL 确认**，无证据可依

**PETANG (14:00–16:20) — 格式基准换源，晨间一项结论被推翻**

**触发：** Jay 指示「Drive 里 owner 是 Jennifer Tan 的文件才算对，照那个格式做；政府 logo 和
表格框线是必须的」。用 `mcp__claude_ai_Google_Drive__get_file_metadata` 逐份查 owner —— `gog drive ls`
不返回 owner 字段，必须走 MCP。

`1grg0ck28lAZHeMhmVB7g1vh4V80NlY_o` 内 17 项，只有 4 份 owner 是 `jennifer@character.com.mx`
（全部 2026-08-20），其余均为 `wenjyue@gmail.com`（我方上传）。四份已下载至
`raw/jennifer-authoritative-fb018-3/`，逐页阅读。

**晨间结论被推翻 —— 语言规则做反了：**
她的权威版是 **马来文框架 + 英文正文**（`A. TEMPOH MASA` / `: 3 HOURS`；`C. TUGASAN` /
`The candidate is required to…`），两者从不在同一句里混。她 22:47 抱怨的「only one language」
指的是句内 `马来文 / English` 对照，**不是要求全马来文**。晨间把全文改成马来文属过度修正 ——
若用晨间规则去校验她自己的合格卷，会误报数百条。`profile.language` 增加第三值
`bm_frame_en_body`，V05 按值区别对待。

**选择信号一直在文件里 —— 是粗体：** 按 span 字体逐条抽取 `jen-skema-setA.pdf` 第 1 页：
C01/C04/C05 = `Arial-BoldMT`，C02/C03/C06 = `ArialMT`。正是她 00:02 才用文字说明的三个实操单元。
文本抽取丢弃格式，所以生成器看到的是六个等价单元。对应 WhatsApp 23:17「你这边加粗的意思是
选那些加粗的 cu 对吗」→「对」。**决策若只由视觉格式承载，就过不了管线；必须以数据形式携带。**

**中心名确证：** 她的原件写 `CHARACTER INTERNATIONAL ACADEMY SDN. BHD.`。`VIZTECH TRADING
SDN. BHD.` 只出现在我方上传的文件里 —— 晨间的推断正确，现有证据。

**两份支撑文件结构完全做错（2026-08-21 审计中标注为「未审」的正是这两份）：**
- `ASSESSMENT ANSWER SHEET` 是 **8 页红字答案范本**（Appendix 3/4/5 填好答案），非空白答题纸
- `EQUIPMENT VERIFICATION` 是 **单页 JPK 表单**，页眉 `JPK/PPA-PPT/SP/1:2022`，14 行清单 +
  申请人/JPK 双栏核对 + 签名

**新增 `_engine/FORMAT-jpk-ppa.md`（9 节格式契约）+ V11–V15：**
- V11 六个马来文段落标题齐全且顺序正确 · V12 参考码存在且 SET 字母与文件名一致 ·
  V13 SKEMA 含 `UNTUK KEGUNAAN PEMERIKSA SAHAJA` / `AMARAN` / `SKALA PEMARKAHAN` ·
  V14 禁用词（`VIZTECH` / `Terlibut` / `DOCUMEN`）
- **V15 汇总表与原始数据对账** —— 见下

**V15 起因（本轮最严重的一条）：** 核对答案范本数字时发现 **考卷自身内部不自洽**。Appendix 2
的「已核实汇总表」与同一附录的 20 行原始数据打架：Married+Children 汇总 10 / 原始 11；
Air-Conditioner 汇总 7 / 原始 6；购买意向 Yes 汇总 15 / 原始 16。考生的任务恰是「分析原始数据」，
**照实数的考生会被评分表判错**。答案范本跟汇总表、skema 跟答案范本 —— 由内向外每层都自洽，
唯独与考生手上那张表不一致。三个 agent、十四个校验器全数漏过。已修（3 个单元格），并加 V15；
**并以反向注入验证 V15 确实会响**（把数字改回错的，立即报 2 条）。

**渲染器（`_engine/render/ppa_docx.py`）新增：**
- `⟪LOGO⟫` token → 徽章嵌入封面表格左上单元格（她的原件如此，非浮于页顶）
- `⏎` token → 真正的 `w:br`。`<br>` 被 pandoc docx writer 静默丢弃，导致
  `KEMAHIRANKEMENTERIAN SUMBER MANUSIAARAS`；用 `w:br` 还能保住每个 run 的粗体（封面必需）
- `⟪SPAN⟫` token → 整行跨列合并居中（封面标题行）。须在 `rule_all_tables` **之后**执行，
  否则居中被逐格左对齐覆盖
- `size_columns()` —— 按内容平方根分配列宽，并以「最长不可断词」为下限。仅设 `cell.width`
  无效：Word 依 pandoc 的 `w:tblGrid` 与 `w:tblLayout` 排版，必须重写网格并锁定 fixed，
  否则改动完全不生效（曾误判为已修）
- 参考码移至**页眉右上**，页码留页脚居中（原先两者都在页脚）；正文中重复的参考码自动删除
- logo 不再有「无 token 则浮于页顶」的回退 —— 该回退曾把徽章放到不该有徽章的 JPK 表单上
- `--table-font-pt` / `--margin-cm` 显式参数（设备核对表 9pt + 1.8cm 边距 = 单页）

**`_engine/render/integrate.py` 新增 `_assert_declaration_matches()`：** 导出 PDF 后**拿两个产物
互相核对**声明页数与实际页数。回填循环在页边距变更后失步，导致 soalan 声明 12 页而 PDF 为 13 页
—— 正是该循环存在的理由所指缺陷。循环自身的记账不是证据。

**FB-018-3 SET B 重建交付（V01–V15 全过，0 errors）：**
SOALAN 12pp（声明 12）· SKEMA 16pp（声明 16）· ANSWER SHEET 8pp · EQUIPMENT VERIFICATION **1pp**

**已送达 Jennifer（16:18–16:19，ack=4 已读）：** 主消息（7 项改动 + 2 项待她确认）+ 4 张
改动前后对照图（`_engine/reports/for-jennifer/`）+ 页数提醒（她自己的样本：soalan 声明 13
实际 14、skema 声明 14 实际 11）。4 份 PDF 以 `[fb3 B 25.08]` 前缀上传其 Drive 并经
`gog drive ls` 复查落地。

**监听：** `_engine/Watch-Jennifer.ps1`（读取新消息，语音自动 Whisper 转录 —— 她有要求只存在于
语音中）+ `_engine/Wait-Jennifer.ps1`（后台阻塞至有回复即退出）。水位线
`_engine/.jennifer-watermark`。

**PETANG LEWAT (16:40–17:30) — lima NOSS yang lain**

**触发：** Jay 指出其余科目也该改。**更正前提：** 昨天那 36 份是另一 session 在 Jennifer 审阅
*之前*生成的；今日稍早只做体检未动手。此轮才实际修改。

**`_engine/migrate_cover.py`（新）：** 把段落式封面机械转换为 JPK 单表格封面（`⟪LOGO⟫` /
`⏎` / `⟪SPAN⟫` token），并把硬编码页数换成 `⟪PAGES⟫`。幂等。批次中存在 **三种封面方言**
（标题有时是粗体行、有时只有 H1；中心名有时隔空行、有时紧接；SKEMA 封面有的完全没有 CU 清单
—— 从其 SOALAN 兄弟档取，不自创）。20/20 全部识别。原件备份至 `_archive-2026-08-25-precover/`。

**22 份 soalan + skema 全部重渲**，逐份核实：声明页数 = PDF 实际页数（0 不符）、页眉参考码全部到位。

**页眉正则缺陷（本轮最有代表性的一条）：** `_ref_code()` 与 V12 共用
`[A-Z]{1,3}-\d{3}-\d` —— 认不出 `N821-001-3` 这类「字母+数字」开头的代码，也认不出
`FB-018-45`（level 两位数）。后果：**N821 / M731 / G471 三科整份无页眉**，而 **V12 用同一个
错正则，因此一直静默通过**。改为 `[A-Z]{1,3}\d*-\d{3}-\d{1,2}`。
**教训：校验器与被校验对象共用同一错误假设时，它会 fail open。**

**跨文件查重（`cli lint`）：** L4 与 L5 两份不同考卷同印 `FB-018-45:2012/2026/A/01`。
第一版查重把同一份卷的四件套也误报 —— 四件共码是正确的（Jennifer 原件亦然），收窄为「跨 set
才算重复」后精确命中。

**FB-018-45 CU 代码无依据：** L4/L5 CoCU PDF 的 `CU Code` 栏**整栏空白**，NOSS 代码本身亦未印。
考卷用 `M01–M08`、图谱用 `C01–C08`，**皆为杜撰**。两份图谱已加 `⟪TBD⟫` source_note。

**自我更正：** 今晨称「N821 标准自相矛盾（C07 正文 Staff / 图表 Office）」**是错的**。
实读原文者报告 §6 p.6、CPC p.11、CoCU 15.7 p.71 三处**皆为 Staff**。系照抄 2026-08-21 审计
的错误结论而未复核。考卷现有的 `C07 STAFF ADMINISTRATION SUPERVISION` 正确。

**误报清算：** 今晨「其余科目 799 个问题」在改用正确语言规则（`bm_frame_en_body`）后为 **140**
—— **659 条系晨间过度修正的规则所生噪音**。`cli lint` 现涵盖 V05/V08/V10–V15 并支持 `--only`。

**已修：** `fb-018-45-l4-set-b-skema` 分节分母 `/3 → /57`、`/15`（Set A 于 08-24 已修，Set B 漏掉）。

**已送 Jennifer（16:59–17:00，12 条全部送达）：** 格式统一说明 + 3 张其余科目对照图 +
**6 份 CU 选择表 PDF**（马来文，含时间容量提示）+ FB-018-45 代码与撞号追问。

**`_engine/OPEN-QUESTIONS-jennifer.md`（新）：** 7 条待决事项，每条附证据。

**发布：** https://academy.wenjyue.com/engine.html 已更新并核实（md5 本地=线上，HTTPS 200）。


**MALAM (17:00–18:15) — dua jenis dokumen sokongan, dan pemeriksaan silang dokumen**

**V16（新）—— 整类文档漏网。** 今日的封面迁移只覆盖 `soalan` 与 `skema`，因此
**10 份 `equipment-verification` 全数仍為自创格式**、**10 份 `answer-sheet` 全数仍為空白表格式**。
此二者正是 2026-08-21 审计标注「未審」的文件 —— 搁置未读之物，往往错得最彻底。

**`_engine/gen_equipment.py`（新）：** 设备核对表改為**推导**而非撰写 —— 每一行直接取自该卷
§D + §E。以 FB-018-3 验证：产出 13 项，与先前手工版逐项一致。跨文档「考卷清单 vs 核对表清单」
不符由 **10 处降至 0**。超过 14 行（Jennifer 原件上限）時主动提示。

**V17（新）附录标签一致性：** Jennifer 原件 `Appendix` ×8、`Lampiran` ×0。我方 N821 soalan
`APPENDIX 1A` ×50 与 `LAMPIRAN 1` ×2 同处一档 —— 考生被要求填「Lampiran 2」需自行猜测那是
标题为「Appendix 2A」之物。已统一。

**跨文档：附录交叉引用（新）。** 答案范本引用之附录必须存在於其配对考卷。抓到 G471 ×2
（引用 `Appendix 3A/3B/5A/5B`，考卷實為 `APPENDIX 3` 内含 `### A.` `### B.`）与
FB-018-45 L4 ×2（引用 `Appendix 2B`，考卷實為 `APPENDIX 2` 内含 `**B. …**`）。
**内容理解正确、标签自造** —— 考官持卷搜寻该字串将一无所获。四处均已改為考卷自身写法。

**V05 语言：由 5 条误报归零，过程本身值得记录。** 三次「修一个误报、制造下一个」：
① 仅查斜杠右侧 → `Petty Cash Payment Form / Bills Collection Report`（两侧皆英文）误报；
② 為修①而将 `petty`/`cash` 加入英文词表 → `laporan bayaran bulanan / laporan petty cash`
（两侧皆马来文）误报；③ 為修②而要求左侧含马来文虚词 → `Tinjauan Pasaran & Produk`
（全实词）漏报。最终改為正面判据（左侧不似英文 + 右侧≥2 英文词 + 右侧无马来文词），
并**建立 7 个探针固定行為**：3 条真对照必须抓到、4 条假阳性必须放过。
**无探针的规则调整等同盲改。**

**渲染参数改為由文件类型决定。** 曾以 `--table-font-pt 9 --margin-cm 1.8`（专属设备表）
误套至 n821 soalan/skema，将使其与已渲之 18 份字号页边距不一致。已停批次并写入
`KIND_SETTINGS`；`integrate <任意文件>` 不带 flag 即為正确。**第四次将「须记住之事」
改為「不可能记错之事」**（前三：CU 选择入 profile、格式入契约、页数入终检）。

**签名孤儿页与连锁副作用。** 两份设备表第 2 页仅余一行签名。改為表格末行後，13 项那份
反由 1 页变 2 页 —— 真因在上游：`size_columns` 将**即将合并的跨列行**计入第一列宽度，
撑宽首列、挤扁其余。排除跨列行後恢复。**改动影响范围恒比预期大一格；唯有渲染出来数页数
方能察觉。**

**全量核验（44 份文件，0 问题）：** 每份 PDF 存在、声明页数 = 实际页数、页眉参考码到位。
逐文件检查 V05/V10/V11/V13/V15/V16/V17 全数归零；跨文档检查附录引用与设备清单均归零。
仅余 22 条 V08 页数提示（属预期）与 1 项 L4/L5 撞号（须 Jennifer 定夺）。

**未上传其余 5 科。** 其 CU 结构仍為「全数纳入」，待 Jennifer 填回选择表方能定案；
此刻上传将使其看似已完成，實则不然。FB-018-3 四件已於 16:18 上传并经复查。


---


## [2026-08-24] delivery | Round 3 PPT-PPA 36 份全量生产并上传 Jennifer Drive

**完成内容：**
- 全部 9 个新 SET × 4 件 = 36 份文档通过 graph-engineering pipeline（ARCHITECT→AUTHOR→MARKER→ATTACHMENTS→AUDITOR）
- 所有文档过 AUDITOR BASELINE §4（4.1–4.6）：零编造、配分自洽、可完成性估时 ≤ 153 min、A/B 卷对等
- INTEGRATOR 批量处理：md→docx→Word COM 实测页数→回填 `⟪PAGES⟫`→PDF，36 ok / 0 failed
- 36 份 PDF 上传 Jennifer 5 个 Drive 文件夹，全部经 `gog drive ls --parent` 核实

**修复（本次执行中）：**
- 7 个 SKEMA 声明行：统一为 `SKEMA PEMARKAHAN INI MENGANDUNGI ⟪PAGES⟫ MUKA SURAT BERCETAK TERMASUK MUKA HADAPAN`
- fb-018-45-l4-set-a-skema：Bahagian 总分分母 `/3 → /57`（B2）、`/15`（B3/B4）
- g471-B skema criterion 2.19：移除错误的 secondary AC 引用 C05 AC 2.5

**交付清单：**

| NOSS | Drive 文件夹 ID | SET A | SET B |
|------|--------------|-------|-------|
| N821 Office Admin | `169-72I6UsuhSU55ExxVUDfSNzgmonCf1` | 已有 | ✅ 新上传 |
| M731 Digital Marketing | `1UVrPhmrG0dkE-2YbSeFcQCzT-JZH_h30` | ✅ 新上传 | ✅ 新上传 |
| G471 Retail Outlet | `1w_BdONXPVyTBVDUQOUv7dKCkq3K8RQOn` | ✅ 新上传 | ✅ 新上传 |
| FB-018-45 L4 | `1yRsIymqd3AzLMIzoHJ7epf2zsDJqBigC` | ✅ 新上传 | ✅ 新上传 |
| FB-018-45 L5 | `1B-ExSfT9MdjzoD0r23H_ZUuDftlXpFfc` | ✅ 新上传 | ✅ 新上传 |

**Academy tracker 已更新：** http://127.0.0.1:8110（本地）/ https://academy.wenjyue.com（生产）

---

## [2026-07-29] note | Eligibility audit + proposal normalisation + now.md corrected

**What changed:**
- Audited official PTPK Garis Panduan (19 Mei 2025) — extracted key eligibility rules: active JPK/MQA pentauliahan mandatory (§4.8 + §8.1 + Lampiran 1 item 2.1); premises must be registered under that accreditation (§11.7); industry partner only needs LOC/LOA/MOA, ordinary Sdn Bhd qualifies (§6.2(iii) + §11.2(iv)) → Prisma and VecTech CAN be industry partners
- Established that no entity is confirmed accredited: 3U = no accreditation (Jay 2025-11-20, 2026-07-24); Character International Academy = UNCONFIRMED (Jennifer's 2026-07-24 message was a question, not a statement of fact); Prisma = no JPK licence or training centre
- Flagged NOSS code defect: all proposals cite `DM-001-3:2026` which does not exist — correct code is `M731-001-3:2021 Digital Marketing Operation`
- Reviewed 16 voice-note transcripts (wiki/08-jennifer-voicenotes-20260724.md — NOT ~12 as previously recorded): Jennifer's Plan A = Character applies DM, Jay's provider applies AI; Plan B = everything under Character if Prisma cannot apply; she named AI for Work + AI for Admin (not Manufacturing); confirmed grant is NOT HRDC and NOT COPTPA
- Normalised proposals: 30:70 method applied (C01–C07 = 84h:196h = 280h exactly); ai-dm ad budget now has cost line (RM3,800 / RM3,500); ai-admin Pakej A added; ~39 vague placeholders replaced with `⟪TBD: what | who | when⟫` form
- Verified contacts via Periskope: Jennifer = Tan Siow Inn (60126111677), Yashini Pure Ocean (60184007417), Jas Kae Shyong Prisma (60167166663), Chang SC VecTech (601117758060)
- Corrected deadline: 31 July 2026 at NOON (not end of day) per official guideline
- Rewrote wiki/now.md — removed three material errors (proposal count, voice-note count, deadline time); added Verified vs Unverified table; surfaced accreditation blocker as #1 priority

**Why:** now.md contained three factual errors that could mislead the next agent or Jay into a false sense of readiness. The eligibility audit revealed the accreditation gap is a hard blocker — no submission is valid without Sijil Akuan Pentauliahan.

**What's next:**
- Jay to call/WhatsApp Jennifer for Kod Pusat + Sijil Akuan Pentauliahan (Character Intl. Academy) — nothing can be submitted without this
- Fix NOSS code in all four proposal drafts: replace `DM-001-3:2026` → `M731-001-3:2021`
- Remove HRD Corp / COPTPA language from proposals
- Clear remaining ~39 `⟪TBD⟫` placeholders (especially Jurulatih 2, 3U address, registered venue)
- Submit via PTPK portal before 31 July 2026 12:00 PM

---

## [2026-07-25] build | PTPK Skim TBT 2026 — 5 Proposal Websites Live

Deployed 5 sites to Hetzner (deploy@5.223.54.57) for Jennifer (Character Academy) to review before 31 July PTPK deadline.

**Sites live:**
- Hub: https://3u-proposals.wenjyue.com/ (PM2 id=23, port 3461)
- DM: https://3u-proposal-ai-digital-marketing.wenjyue.com/ (PM2 id=19, port 3457)
- Admin: https://3u-proposal-ai-admin.wenjyue.com/ (PM2 id=20, port 3458)
- ISO: https://3u-proposal-ai-iso.wenjyue.com/ (PM2 id=21, port 3459)
- MFG: https://3u-proposal-ai-manufacturing.wenjyue.com/ (PM2 id=22, port 3460)

**Proposal docs (Chinese):** `proposals/ai-dm-proposal.md`, `ai-admin-proposal.md`, `ai-iso-proposal.md`, `ai-mfg-proposal.md`
**Training provider:** Character Academy Sdn Bhd (Jennifer / Tan Siow Inn)
**Content partner:** 3U Pioneer Academy + Prisma Technology (Badan Industri)
**PTPK deadline:** 2026-07-31 12:00PM
**Tech stack:** Go + Tailwind CDN, Nginx + Let's Encrypt SSL, PM2 on Hetzner
**Cloudflare DNS:** 5 A records (DNS-only) added to wenjyue.com zone

---

## [2026-07-24] build | AI Digital Marketing — E01/E02 electives + JPK envelope + PTPK TBT proposal

**What changed:**
- Added E01 (Automate Digital Marketing Workflows with AI) — 3 × KP files built, each with full JPK envelope
- Added E02 (Optimise Digital Presence for AI-Powered Search / GEO) — 3 × KP files built, each with full JPK envelope
- Added `ai_dm` subject to `.claude/skills/wim-jpk-format/data/subjects.json` (C01–C07, E01, E02)
- Updated `enhance_wim_jpk.py` — argparse choices now dynamically loaded from subjects.json (no more hardcoded list)
- Ran JPK envelope script on all 55 ai-digital-marketing files: C01–C07 × (KP×3, KK×2, KA, PA) + E01×KP×3 + E02×KP×3 — all updated
- Added E01/E02 CoCU definitions to `00-noss-extract.md` (Work Activities, Related Knowledge, Related Skills, Assessment Criteria)
- Created `ai-digital-marketing/proposal-ptpk-skim-tbt-2026.md` — full PTPK Skim TBT 2026 proposal in BM (Pakej A RM3,800/7-hari intensif, Pakej B RM3,500/14-minggu)

**Why:** 31 July 2026 deadline to apply for PTPK Skim TBT 2026. Jennifer confirmed ADI only needs KP. Jay requested all gaps closed for submission.

**What's next (Jay action):**
- Fill in Jurulatih 2 name + cert in proposal
- Add 3U Pioneer Academy address to proposal
- Submit via PTPK portal before 31/7
- Confirm Lesen Perniagaan status (Jennifer's Item 3)
- Transcribe Jennifer's 5–6 voice notes from 2026-07-19/20 (may contain additional scope)

---

## [2026-07-19] create | AI Digital Marketing course — new COPTPA programme added

- New sub-folder: `ai-digital-marketing/` — WIM content generation started
- NOSS code (placeholder): DM-001-3:2026, Level 3
- 7 Core CUs + 2 Elective CUs
- KP/KK being generated for C01–C07
- Proposal deck: `proposal-ai-digital-marketing.pptx` created
- INDEX.md updated to include new subject

---

## [2026-07-17] build | ADI Multimedia courses (J582) scaffolded — JPK COPTPA 2023 certification prep

**Context**
- Jennifer sent `1.xlsx` (JPK/SLDN/LP01 COPTPA 2023 verification table) on 2026-07-15 — this is the official JPK APV evaluation scoresheet used during accreditation site visits.
- 3U Pioneer Academy is applying for new course (Baharu) accreditation for two J582 multimedia programmes under the ADI (Apprenticeship/Industry) scheme.
- Total applicable COPTPA criteria: 51 items (from 90 total; B = Baharu filter). Spread across 7 Bidang.

**What changed**
- `raw/jennifer-multimedia/1.xlsx` — already present (Jennifer's COPTPA table)
- `raw/noss-pdf/` — folder created; J582 PDFs to be placed here once obtained from MySPIKE
- `multimedia-interactive-design/` — new subject folder (J582-001-3:2019, Level 3 SKM, 5 core CUs):
  - `00-README.md`, `00-noss-extract.md` (draft from NOSS knowledge — ⚠️ verify vs PDF), `01-jpw-distribution.md`
  - `C01/`–`C05/` created; WIM files (KP/KT/KK/PM/KA/PA) generated via parallel workflow
- `creative-multimedia-development/` — new subject folder (J582-001-4:2025, Level 4 DKM, 6 core CUs):
  - `00-README.md`, `00-noss-extract.md` (indicative stub — ⚠️ needs actual PDF), stubs only
  - `C01/`–`C06/` created with placeholder WIM files pending NOSS PDF
- `subjects.json` — extended with `multimedia_l3` and `multimedia_l4` keys (ready for `enhance_wim_jpk.py`)
- `INDEX.md` — added both multimedia subjects to Sub-effort A table

**Why**
- COPTPA BIDANG 1 (course development & delivery) requires complete WIM set for all CUs — this is the primary deliverable Jay/AI is responsible for. BIDANG 3/4/5/6/7 are Jennifer/3U Pioneer internal documents.
- ADI scheme requires KP (theory information sheets) as priority — these are the primary SLDN learning materials.

**Blockers / What's next**
1. ⚠️ **NOSS PDF required:** Download J582-001-3:2019 and J582-001-4:2025 from MySPIKE (www.myspike.my) → save to `raw/noss-pdf/` → verify/correct `00-noss-extract.md` for both subjects → regenerate any incorrect WIM content
2. Run `enhance_wim_jpk.py multimedia_l3` and `enhance_wim_jpk.py multimedia_l4` to apply JPK envelopes after files are complete
3. Jennifer / 3U Pioneer to prepare: lecturer qualification docs, student handbook, facility equipment list (BIDANG 3/4/5)
4. Confirm CU count and WA details for J582-001-4:2025 (2025 NOSS — very new)

---

## [2026-06-23] build | Full IT-020 WIM package authored to Jennifer's standard (362 files)

**What changed**
- Extended `subjects.json` with verified `it4` (IT-020-4:2013 Computer Systems Administration, 6 CUs) and `it5` (IT-020-5:2013 Computer Systems Management, 6 CUs + elective E01) blocks — CU titles + work activities extracted from Jay's actual NOSS Google Docs (not the corrupted metadata).
- Authored the COMPLETE WIM set for all 20 CUs (KP/KK/KT per work activity + KA + PA + PM-teori + PM-amali), via parallel per-CU subagents, in the native-header format the envelope generator consumes:
  - L3 (Computer System Operation): C01–C07, 127 files
  - L4 (Computer Systems Administration): C01–C06, 114 files
  - L5 (Computer Systems Management): C01–C06 + E01, 121 files
- Ran `enhance_wim_jpk.py it / it4 / it5` → all **362 files** carry the correct JPK envelope, programme name, CU title, codes (`IT-020-N:2013-C0x/…`), single header. Verified: 362/362 enveloped, 0 duplicate headers.
- Added `it4`/`it5` to the script's argparse choices.

**Why**
- Goal: enhance NOSS IT-020-3/4/5 and make Jay's materials fully adhere to Jennifer's verified WIM standard/format.

**What's next**
- Publish to Jay's Google Drive (`docs.google.com`) — outward-facing; confirm approach (markdown mirror vs built .docx) + authorization first.
- Optional: deeper best-of-breed merge of Jennifer's specific C01/C02/C07 sheet prose into the matching KP bodies.

---

## [2026-06-23] fix | IT-020-3 WIM aligned to Jennifer's verified standard

**What changed**
- Downloaded Jennifer's verified (NOSS-passing) IT-020-3:2013 WIM samples → `raw/folder-3-jennifer-it020-2026-06-21/` (6 files) + markdown refs in `raw/md/folder-3-jennifer-it020/`.
- Confirmed: Jennifer's files are **WIM** (teaching material), Jay's 3 Google Docs are **NOSS** (the standard) — different layers; IT-020-3 standard itself matches (same 7 CUs / work activities).
- Root-caused broken envelopes: `.claude/skills/wim-jpk-format/data/subjects.json` `it` block had wrong programme name ("Computer System Management") and only 4 *fabricated* CUs. **Rewrote it** to the correct programme (Computer System Operation / Operasi Sistem Komputer) + all 7 real CUs (titles + work activities from NOSS/Jennifer).
- Improved `enhance_wim_jpk.py`: drop redundant `L3-` code prefix (→ `IT-020-3:2013-C01/…`, matching Jennifer), strip the duplicate native header, recover real `TAJUK`, CU-title fallback for KA/PA/PM, ignore numbered lists in TUJUAN extraction.
- L3-C01: archived 25 bare-code duplicate files, regenerated 25 descriptive files with correct envelopes (verified KP-01 etc.). L3-C02: archived bare KA dup, regenerated.
- Wrote `it-computer-system/00-wim-standard-and-jennifer-alignment.md` (verified standard, best-of-breed decisions, corrected CU map, build plan).

**Why**
- Jay's goal: best-of-breed merge (learn from Jennifer where better, keep ours where better), complete all 7 CUs of IT-020-3 in JPK format, ensure full adherence to Jennifer's standard.

**What's next**
- Decide coding convention (keep `KP/KK/KT` vs switch to Jennifer's `P/K`).
- Build out C02 (KP/KK/KT/PA/PM); rebuild C03 (Repair) & C04 (Server Installation) — current KA bodies are wrong CU; create C05/C06/C07.
- Then L4 (6 CUs) + L5 (7 CUs); finally publish conformant WIM to Jay's Google Drive.

---

## [2026-06-22] structure | Four NOSS folders combined into 3u-pioneer-academy-noss

**What changed**
- Merged 4 sibling `1-projects/` folders into this umbrella project (Jay's instruction: flat merge, keep everything):
  - `noss-to-wim` (active WIM generator — Sub-effort A) → the structural base
  - `noss-it020-textbook` + near-duplicate `NOSS` (IT-020 textbook — Sub-effort B)
  - `Apply NOSS IT-020 Computer System Management` (accreditation application — Sub-effort C)
- Flat merge with **numbered backups** (`cp -a --backup=numbered`): every same-path collision preserved as `*.~1~`/`~2~`/`~3~` (≈3,028 backup files) — nothing overwritten silently
- `cp` stalled on a Windows **junction** inside `noss-to-wim` (`.git`/cache reparse points, CPU-spinning, zero progress) → killed and finished with `robocopy /E /XJ`, which skipped 304 junction reparse points (not real data)
- Final: 16,320 files / 861 MB; all key content dirs from all 4 sources verified present
- Archived the 4 originals (move, not delete) to `4-archive/old-projects/noss-merge-originals-2026-06-22/`
- Rewrote root `index.md` as an umbrella nav hub (4 sub-efforts) and added `wiki/00-umbrella-overview.md`

**Why**
- One client (3U Pioneer Academy), one goal (JPK accreditation), one contact (Jennifer) was spread across 4 folders — consolidating gives future sessions one entry point

**Caveats**
- `.git/` is now a **non-functional Frankenstein** (3 repos flat-merged) — `rm -rf .git && git init` if version control is needed
- ≈3,028 `*.~N~` collision backups can be pruned once canonical files are confirmed good
- `.venv/` + caches carried over verbatim (regenerable; not on the reading path)

**What's next**
- Optional cleanup pass: re-init git, prune `*.~N~` backups, drop `.venv`/caches
- Continue WIM QA + IT-020 accreditation application

---

## 2026-04-18 — BEV / Aesthetic / IT WIM filenames given descriptive suffixes (Option B, second pass)

**What changed**
- Renamed 302 WIM `.md` files via `git mv` across 3 subjects (BEV 83, Aesthetic 194, IT 25)
  - Same Option B pattern as the Tuinalogy pass: `KP-01.md` → `KP-01-<slug>.md`, `KA.md` → `KA-<cu-name>.md`, etc.
  - Slugs sourced from each file's body content:
    - BEV: H2 `## Work Activity N: <name>`
    - IT: H2 `## Tajuk / Title: <name>`
    - Aesthetic: bold line `**Work Activity N:** <name>` (with H2 `## N.0 <topic>` fallback)
    - KA / PA / PM-teori / PM-amali: CU name from JPK envelope row "KOD DAN TAJUK UNIT KOMPETENSI" (code prefix stripped)
  - Skipped the 3 IT KA-only stub folders (`L3-C02`, `L3-C03`, `L3-C04`) and `level-4/`
- Created `_tools/generate_rename_script.py` — reusable title-extractor + rename-plan generator
  - Outputs `_tools/rename_plan.csv` (302 rows) and `_tools/rename_other_subjects.sh`
- Updated 5 more cross-reference scripts (Tuinalogy pass already covered the other 6):
  - `tools/validate_it_ka.py` → fallback now globs `KA*.md`
  - `tools/validate_aesthetic_ka.py` → fallback now globs `KA*.md`
  - `scripts/audit_it_ka_completeness.py` → both KA discovery sites use `KA*.md` glob with literal fallback
  - `_tools/analyzers/question_type_analyzer.py` → rglob expanded for `KA*.md` + `PA*.md`
  - `tests/test_aesthetic_c04_modalities.py`, `tests/test_wim_export.py`, `tests/test_question_indexer.py` → glob first match instead of literal path
- Verified: `classify_doc` still 9/9 cases, `validate_training_distribution.py {bev,aesthetic,it}` all parse PM-teori/PM-amali for every CU, `validate_it_ka.py` and `validate_aesthetic_ka.py` find the renamed files via fallback

**Why**
- Same readability rationale as Tuinalogy pass — bare `KA.md` / `PA.md` / `PM-*.md` are opaque when grepping or browsing
- Body content is more descriptive than the JPK envelope's CU title in some cases (e.g. BEV C01 envelope says "BEV HIGH VOLTAGE SAFETY" but body says "Carry Out BEV Schedule Maintenance Workplace Preparation" — body wins for KP/KT/KK because the envelope name is repeated for every WA in a CU)

**Caveats**
- BEV C01 has data inconsistency between envelope CU title and body WA names — accepted as-is, not fixed in this rename pass
- `prd.json` still lists ~182 bare paths in story metadata — not run-time loaded, will refresh when Spiral regenerates story manifests
- `.spiral/` cache files reference old paths — runtime regenerated, ignore

**What's next**
- Optional: backfill `prd.json` paths during the next Spiral iteration cycle

---

## 2026-04-18 — Tuinalogy WIM filenames given descriptive suffixes (Option B)

**What changed**
- Renamed 91 Tuinalogy WIM `.md` files via `git mv` so history/blame survive
  - Pattern: `KP-01.md` → `KP-01-eight-core-techniques.md`, `KA.md` → `KA-pediatric-tuina.md`, etc.
  - English slugs derived from each file's first H1 heading
  - All 7 CUs covered: C01-C05 + E01, E02
- Updated 6 Python files to **prefix-match** WIM doc-codes instead of strict equality, so both the new tuinalogy names and the still-bare BEV/Aesthetic/IT names work:
  - `build/wim_consolidate_all.py` → `classify_doc()`
  - `.claude/skills/wim-jpk-format/scripts/enhance_wim_jpk.py` → `classify()`
  - `scripts/validate_training_distribution.py` → glob lookup for PM-teori/PM-amali
  - `_tools/classifiers/question_difficulty_classifier.py` → KA/PA rglob expanded
  - `_tools/assessment-time-validator.py` → KA/PA rglob + atype detection
  - `tools/question_bank_indexer.py` → KA stem check + rglob
- Updated 4 internal cross-references in `tuinalogy-services/E01/{KP-01,KP-02,KP-03,PA}.md`
- Updated `build/README.md` example command to point at the new C01 KP-01 filename
- Created `_tools/rename_tuinalogy_wim.sh` as the executed (and now-archived) rename script
- Verified: `classify_doc` 12/12 cases pass, `enhance_wim_jpk.classify` 7/7 cases pass, `wim_consolidate_all.py --subject tuina` builds the 8 MB consolidated docx successfully, `validate_training_distribution.py bev` still parses BEV unchanged (no regression)

**Why**
- The bare `KP-01.md` / `KA.md` / `PM-teori.md` codes are JPK-correct but opaque when browsing files — slugs make the directory readable without opening every file
- Suffix preserves the doc-code prefix so JPK coding (`MP-031-3:2016-C02/KP(1/3)`) and tooling stays intact
- Other 3 subjects (BEV/Aesthetic/IT) intentionally left bare for now — the prefix-matching code handles both naming styles

**What's next**
- Optional: rename BEV / Aesthetic / IT files for parity (low priority — the codes work fine for those)
- `pregnancy-check-report.csv` still references old paths — will regenerate on next `tools/check-pregnancy-safety.py` run

---

## 2026-04-17 — Jennifer's reference WIMs archived; docs + log + index introduced

**What changed**
- Downloaded two Google Drive folders of sample WIMs (provided by Jennifer as reference): `raw/folder-1-wim-panduan/` and `raw/folder-2-sample-wim/`
- Created `INDEX.md` — directory manifest for fast LLM navigation
- Created `LOG.md` (this file) — append-only activity log, Karpathy-style
- Updated `CLAUDE.md` to list Tuinalogy as the 4th subject and to instruct agents to read INDEX.md first
- Built consolidated DOCX outputs:
  - `build/WIM-Consolidated-All.docx` (8.4 MB, all 4 subjects, 433 md files)
  - `build/WIM-Tuinalogy.docx` (7.8 MB, Tuinalogy only with embedded images)
- Consolidation script `build/wim_consolidate_all.py` written (cover page, TOC, page numbers, colour-coded headings by doc type)

**Why**
- Jennifer's reference PDFs are the "what a JPK-compliant WIM should look like" benchmark — storing them locally so offline comparisons are possible
- Project now has 4 subjects (was 3) — CLAUDE.md needed updating so new agents don't miss Tuinalogy
- Karpathy's dated-log concept: LLMs that land in the project benefit from a narrative of what-and-why rather than only state; INDEX gives the map, LOG gives the journey

**What's next**
- Finalize pending Spiral stories (3 remaining as of last check)
- Review Jennifer's reference WIMs — compare format against current output, iterate if gaps
- **Neutralise Spiral's commit-clobbering bug** — its git-stash / reset cycle has wiped uncommitted work three times today

---

## 2026-04-17 — Tuinalogy image enrichment committed

**What changed**
- 27 CC-licensed images downloaded from Wikimedia Commons + Wellcome Collection
- Categorised into `_assets/{meridians,acupoints,anatomy,techniques,clinical}`
- `_assets/ATTRIBUTION.md` created — full legal manifest (CC BY 4.0, CC BY-SA 4.0, PD)
- 19 of 22 Tuinalogy KP files now reference images (11 commits on master)
- Skipped: all 6 C05 KPs (administrative topics — records, HR, hygiene supervision, accounting, marketing, complaints have no good Wikimedia match)

**Why**
- Tuinalogy teaches anatomy, meridians, acupoints, tongue diagnosis — text-only was insufficient
- CC-licensed sources avoid copyright issues for government training material

**Operational note**
- Spiral autonomous runner kept resetting `master` to `05cafb3` during the session, wiping enrichment commits twice
- Root cause: a respawner outside the normal `NOSS-Textbook-Refresh` Task Scheduler entry (which is disabled) keeps starting `python.exe` + `claude-code` + `ralph`. Respawner not yet identified — **investigate before next Spiral restart**

---

## 2026-04-17 — Tuinalogy subject launched (4th subject)

**What changed**
- Created `tuinalogy-services/` folder tree (C01–C05, E01, E02 — 7 CUs)
- Extracted NOSS MP-031-3:2016 CoCU into `tuinalogy-services/00-noss-extract.md`
- Generated Chinese (简体中文) WIM documents across all CUs (PM-teori, KP, KT, PM-amali, KK, KA, PA)
- Set Spiral focus to Tuinalogy only — pivoted away from BEV/Aesthetic/IT

**Why**
- Jennifer added Tuinalogy as a new scope (推拿疗法 MP-031-3:2016)
- Required Simplified Chinese with bilingual EN/BM for clinical vocabulary — different style from first three subjects

**What's next**
- Add images (done — see above entry)
- Run Spiral for ~50 user stories of content enhancement

---

## 2026-04-16 — BEV / Aesthetic / IT content enhancement via Spiral

**What changed**
- Ran Spiral autonomous loop to enhance existing BEV / Aesthetic / IT content
- First 30 user stories completed (captured in `10us.md` milestones 10, 20, 30)
- Major gains:
  - BEV C03 Thermal System scenario-based Knowledge Assessment
  - Aesthetic C03 manual body massage anatomy deepening
  - Aesthetic C04 six electrotherapy modality safety notes
  - Bilingual (EN+BM) Aesthetic terminology glossary with consistency validator

**Why**
- Baseline NOSS→WIM conversion produced competent-but-thin content
- Spiral iteratively adds depth, humanises language, adds scenario-based assessments, validates CoCU coverage

---

## 2026-04-16 — Project scaffolding

**What changed**
- Created project root at `C:\Users\Jyue\Documents\1-projects\noss-to-wim\`
- Top-level reading guides (`00-README.md` → `06-whatsapp-context.md`)
- Three subject folders created: BEV, Aesthetic, IT
- `CLAUDE.md` written with agent instructions (WIM structure, coding format, rules)
- Spiral skill configured (`spiral.config.sh`) for autonomous enhancement

**Why**
- Convert 3 NOSS occupational skill standards into Malaysian JPK-format Written Instructional Materials
- Target: government-standard training material ready for instructors

---

## Template for new entries

```markdown
## YYYY-MM-DD — one-line headline

**What changed**
- bullet
- bullet

**Why**
- bullet

**What's next** (optional)
- bullet
```

---

## [2026-04-22] structure | Add wiki/ folder and migrate numbered .md files

**What changed**
- Created `wiki/` folder at project root
- Moved numbered overview/reference files (01 through 07) into `wiki/`:
  - `01-noss-overview.md`, `02-wim-structure.md`, `03-wim-coding-system.md`
  - `04-wim-development-process.md`, `05-noss-to-wim-mapping.md`
  - `06-whatsapp-context.md`, `07-jpk-format-spec.md`
- `00-README.md` retained at root as entry point
- `raw/` already existed (Jennifer's sample WIM PDFs)

**Why**
- Applying Karpathy-style raw/wiki two-layer structure across 1-projects
- `wiki/` = synthesized/analysis docs; `raw/` = immutable source data

**What's next**
- Update INDEX.md to reflect wiki/ paths for numbered files

## [2026-07-19] enhance | AI Marketing KP/KK regenerated + website expanded + multi-role review

- Regenerated all 21 KP files (C01-C07) at BEV professional quality (200-330 lines each, bilingual, Malaysian regulatory grounding)
- Created 00-jpk-requirements-checklist.md from Jennifer's 1.xlsx (JPK COPTPA verification form)
- Website ai-marketing.wenjyue.com: added /materials (教材库) + /requirements (认证要求) pages, internal-only banner
- Ran 4-persona review (web designer, student, JPK officer, internal staff) via /loop engineering; applied 10 top improvements: mobile nav, ROI frame, intake dates, refund policy, schedule box, tool costs, readiness score, table overflow fixes, CTA hierarchy
- KEY JPK OFFICER FINDINGS (need Jay action): (1) KA+PA assessments still missing all 7 CUs; (2) NOSS code DM-001-3:2026 not in MySPIKE — needs JTK approval or NOSS development track; (3) only 2 electives (may need 4); (4) instructor TVET-i cert pending

## [2026-07-20] complete | KA/PA assessments + website features + loop-engineered quality

- Generated all 14 assessment files: 7 KA (Kertas Penilaian Pengetahuan, pink) + 7 PA (Kertas Penilaian Prestasi, light blue) for C01-C07, matching BEV format (Section A/B/C + Q-format bank + marking schemes + rubrics)
- Website: material content viewer (marked.js), JPK logo on viewer + envelopes, paper-colour-matched cards (KP white/KK blue/KA pink/PA light-blue), interactive requirements checklist with audit trail + name capture, Google Translate selector (BM/BI/中文), tool official links, 30/70 SLDN dual-training positioning
- Requirements readiness rose 55% → 71% (KA/PA now marked done)
- LOOP ENGINEERING quality cycle: independent evaluator baseline 74/100 → fixed 8 defects (CRAFT contradiction, duplicate objectives ×21 files, C07 title, segmentation count, WA4, PDPD name, penetration stat, C04 rubric) → re-eval 84/100 → cleared final blocker (C07/KA duplicate distractor) → submission-ready
- Live: https://ai-marketing.wenjyue.com (internal-only)

## [2026-08-21] develop | Jennifer PPA soalan — Office Admin SET A + CoCU 交叉核对

**触发**：Jennifer（Tan Siow Inn, Character Intl. Academy, 60126111677）2026-08-20 23:53 WA 发来
Drive 裸链接，无说明。文件夹 = `PPA SOALAN TO JAY FOR REFERENCE`
(`11ATUjjbzsg7lbnZIRblc9x1ejoTlMHRg`, owner `jennifer@character.com.mx`)。

**Drive 内容盘点**（`gog drive ls --account wenjyue@gmail.com --parent <id>`；Drive MCP 的
`parentId` 查询返回空，不可用 —— 走 gog）：
- `SOALAN & SKEMA - APPROVED` (`1pqZbaTSER1j-5J_VsnyJysKk8dHeO0RT`) — Beauty L1/L2/L3 全套
  SOALAN+SKEMA SET A/B 已批准，NOSS S960-002 系列
- `TO DEVELOP SOALAN` (`16XyTxJ5pCLre8fle2NnNJsWGbfQd1tkK`)：
  | NOSS | fileId | 状态 |
  |---|---|---|
  | N821-001-3:2020 Office Administration | `1Zsxvnm04tiuxKOLGFnAvc2XqD6T2BBia` | 100 页，已读 |
  | M731-001-3:2021 Digital Marketing Operation | `1i4Pt2LqmiCLurC6u9A-UPpqeM-gTUiJx` | 未读 |
  | G471-001-3:2018 Retail Outlet Operations | `1582qbs1vBuLdeiiSKumqbe1hsl3Dh3y3` | 未读 |
  | FB-018-45:2012 S&M Management | 子文件夹 L4+L5 | 无题 |
  | FB-018-3:2012 S&M Operation | 子文件夹 | Jennifer 已自备 SET A |

**产出** → `output/jennifer-ppa-soalan/`
- `n821-001-3-office-admin-set-a-soalan.md` + `-skema.md` — Office Admin PPA SET A
- `fb-018-3-set-b-soalan.md` + `-skema.md` — 依 Jennifer 已批准的 SET A 格式所建基线
- `README.md` — 范围、溯源、待确认项

**交叉核对（对照 NOSS PDF 目录 15.1–15.7，非依赖推测）**
C01–C06 六个单元名与 NOSS 完全一致；**C07 原草稿误写 `Staff Administration Supervision`，
NOSS 官方为 `Office Administration Supervision` —— 已在 soalan+skema 共 4 处更正。**

**溯源澄清**："just develop 1 set" 并非 Jennifer 的消息，而是**文件夹名**
`FB-018-3 2012 SALES & MARKETING OPERATION (JENNIFER JUST DEVELOP 1 SET)`。
读作「Jennifer 自己已完成 1 套」，非「只做一套」的指令。

**⚠️ 未依项目惯例之处（待补）**
- 本次内容直接由 NOSS PDF 生成，**未先建 `00-noss-extract.md`**，与 CLAUDE.md
  「每个 CU 的真相来源 = 该科目的 00-noss-extract.md」相悖。
- 产出置于 `output/`，未依科目文件夹惯例，亦未套 `<!-- JPK_ENVELOPE_v1 -->`。
- 两者是否补齐，待 Jay 决定该批考题的归属（Character Intl. Academy 的资产，非 3U 的 WIM）。

**未发任何消息给 Jennifer。**

## [2026-08-21] close | PTPK Skim TBT 2026 关闭 + now.md 重写

**Jay 决定（2026-08-21）：PTPK Skim TBT 2026 不提交，关闭。**
2026-07-31 12:00 截止日已过、未提交；原联系人 Yashini (60184007417) 已离职。
从所有简报/扫描/追踪移除；后续任何 agent 不得再将其列为待办。

**now.md 重写。** 原文停在 2026-07-29，头条仍是「Deadline: 31 July at NOON — 2 days away」，
即该项目区连续 23 天向所有读者（含 agent）输出一个已死的 P0。本项目 CLAUDE.md 明令
「不要问 Jay 状态，读 wiki/now.md」——  now.md 陈旧的代价因此高于一般文档。

**遗留物保留不删：** 四份 proposal 草稿（含约 39 个 ⟪TBD⟫，不再清理）、
`_archive/proposals-baseline-290726/`。

**⚠️ 待 Jay 决定：** Hetzner (deploy@5.223.54.57) 上 5 个 PTPK proposal 站仍在运行
（PM2 id=19~23，port 3457~3461）。PTPK 已死，是否下架释放端口与槽位。

**PTPK 死但结论不死，两项已并入新 now.md：**
1. NOSS code 更正 `DM-001-3:2026`（JPK 无此码）→ `M731-001-3:2021`。Jennifer 已于 2026-08-20
   在 Drive 提供该 NOSS 正本 PDF，等待 28 天的项目关闭。
2. Character Intl. Academy 认证状态由「完全未确认」上调为「部分证实」—— Drive 内有其名下
   已批准的 Beauty L1/L2/L3 PPT-PPA 考卷，抬头为 JPK/KSM Pusat Bertauliah。
   ⚠️ pentauliahan 按 programme 发放，Beauty (S960-002) 不自动覆盖 M731/N821/G471。

**新主线立项：** Jennifer PPA Soalan（Character Intl. Academy），详见 wiki/now.md。

## [2026-08-21] build | Hetzner 下架 5 个 PTPK proposal 站（Jay 授权）

`deploy@5.223.54.57` — stop → delete → `pm2 save`，已核验：

| PM2 id | name | 二进制路径（保留未删） |
|---|---|---|
| 19 | ai-dm-proposal | `/home/deploy/ai-dm-proposal/ai-dm-proposal` |
| 20 | ai-admin-proposal | `/home/deploy/ai-admin-proposal/ai-admin-proposal` |
| 21 | ai-iso-proposal | `/home/deploy/ai-iso-proposal/ai-iso-proposal` |
| 22 | ai-mfg-proposal | `/home/deploy/ai-mfg-proposal/ai-mfg-proposal` |
| 23 | ai-proposals-hub | `/home/deploy/ai-proposals-hub/ai-proposals-hub` |

核验：`pm2 list` 五者已消失；`ss -tlnp` 确认 port 3457–3461 无监听。
**未触碰 id=18 `ai-marketing`**（ai-marketing.wenjyue.com 教材库站，与 PTPK 无关）。
其余服务（rainbow-* / pelangi / pms / sihat-tcm）均未受影响。

回滚：`pm2 start /home/deploy/<name>/<name> --name <name> && pm2 save`

⚠️ 遗留：nginx vhost 与 DNS 仍指向这 5 个域名，现在会回 502。是否清理待定。

## [2026-08-23] content | N821 Office Admin SET A 补齐四件套 + 修正 C07 残留

**新增**（`output/jennifer-ppa-soalan/`）：
- `n821-001-3-office-admin-set-a-answer-sheet.md` — Lembaran Jawapan，C01–C07 共 14 份 lampiran 提交核对表
- `n821-001-3-office-admin-set-a-equipment-verification.md` — 设备/材料/环境三段核查表，含 front-office 模拟柜台项

两者格式对齐 Jennifer 的 FB-018-3 SET A 样本四件套（`ASSESSMENT ANSWER SHEET.pdf` / `EQUIPMENT
VERIFICATION.pdf`），编号沿用 `N821-001-3:2020/2026/A/01`。
→ 结清 `AUDIT-jennifer-sample-fb018-3.md` 建议动作 #6（我方缺这两件）。

**修正** `n821-001-3-office-admin-set-a-soalan.md`：
C07 单元名误写 `Staff Administration` 的两处残留（B 段 KETERAMPILAN、C 段 Tugasan V）改为
NOSS 正本名 `Office Administration Supervision`。2026-08-21 那次只改了封面 CU 清单，正文漏改。

**仍未结**：soalan 封面 `14 MUKA SURAT BERCETAK` 为照抄占位值（AUDIT 缺陷 D1），
须在 build 成 .docx 后回填真实页数。

## [2026-08-23] content | 结清 AUDIT 缺陷 D1 —— 四份考卷页数声明回填并复核

8 份 md 经 `build/wim_md_to_docx.py --style KA` 生成 .docx 至
`output/jennifer-ppa-soalan/docx/`，用 Word COM `ComputeStatistics(2)` 实测页数，
回填声明后**重新 build 复核**，声明与实测全部一致：

| 文件 | 回填前 | 回填后 = 实测 |
|---|---|---|
| n821 SET A soalan | 14（照抄占位值） | **20** |
| n821 SET A skema | 无声明行 | **19**（新增该行） |
| fb-018-3 SET B soalan | 13（继承 Jennifer SET A 之误） | **14** |
| fb-018-3 SET B skema | 无声明行 | **24**（新增该行） |

两份 skema 此前完全缺少 `SKEMA PEMARKAHAN INI MENGANDUNGI X MUKA SURAT BERCETAK
TERMASUK MUKA HADAPAN` 一行 —— Jennifer 已批准的样本有此行，属格式缺口，一并补上。

⚠️ **有效范围：** 页数仅对本 build 脚本的模板成立。换模板重排须重算。

Word COM 单实例连开多份会 RPC 崩溃（0x800706BE），须每份新建实例。
`build/` 被全局 deny 规则 `Read(**/build/**)` 挡住（该规则本为 JS 构建产物而设），
脚本源码不可读但可执行。

## [2026-08-23] delivery | 8 份考卷 PDF 上传 Jennifer Drive + academy.wenjyue.com 上线

**触发：** Jennifer 今日 17:30–18:01 WhatsApp —— 下周四要提交申请，提交前须 Panel Soalan
审核签名；已把 Drive 链接开为 Editor：「你可以把你做好的 soalan 放里面」「你放考题了让我知道」。
她澄清「完整」定义：**以 NOSS 计，每个 Level 需 Set A + Set B + relative attachment**。

**上传**（`gog drive upload --account wenjyue@gmail.com`，命名沿用她 SET A 惯例 + SET 后缀）：

| 目标文件夹 | 文件 | fileId |
|---|---|---|
| FB-018-3 2012 SALES & MARKETING (`1grg0ck2…`) | SOALAN … (SET B).pdf | `1cOCUetSutESp0CTtOOqgoSdnPhSrIu1L` |
| 同上 | SKEMA … (SET B).pdf | `1315CZJbdvKbna_cffAzy_lvETreBsQ2n` |
| 同上 | ASSESSMENT ANSWER SHEET (SET B).pdf | `1U_LvxlDVArEZuZjqNtR7erQK2_0_e0r1` |
| 同上 | EQUIPMENT VERIFICATION (SET B).pdf | `1rsEHEAh9tLgBSUOnjuebjssbHV7bAH6J` |
| N821-001-3-2020 OFFICE ADMIN (`169-72I6…`) | SOALAN … (SET A).pdf | `1e_xZzCQxyNWAp_8ZJZH9U2RLWWDEje2O` |
| 同上 | SKEMA … (SET A).pdf | `10u8OvIkKWgPYHHFVOvTSX3DrvgRBIk1o` |
| 同上 | ASSESSMENT ANSWER SHEET (SET A).pdf | `1WvB-22ZGA83GFwC0SmZe7QlP63amjOv4` |
| 同上 | EQUIPMENT VERIFICATION (SET A).pdf | `1bFwSZuGjR-TTJtfmYwMqiCCOmcoLMWNM` |

核实方式：上传后重新 `gog drive ls` 两个目录，8 份逐一确认存在（未仅依赖 API 返回码）。

**覆盖率落差（须向 Jennifer 澄清）：** 按她的定义，Sales & Marketing 完整需 3 Level × A/B ×
(soalan+skema) = 12 份，现仅 L3 齐（她 SET A + 我方 SET B）；FB-018-45 L4/L5 **一份没有**。
N821 仅 Set A，缺 Set B。

**academy.wenjyue.com 上线** —— 交付简报页：
- `*.wenjyue.com` 已有泛解析 → 5.223.54.57，**无需改 DNS**（CF token 无 DNS 权限，此路本也不通）
- webroot `/var/www/academy.wenjyue.com`（静态，无 PM2 进程）
- nginx vhost `academy.wenjyue.com` + certbot 证书（到期 2026-11-21，自动续期）
- 校验：HTTPS 200 · `ssl_verify=0` · HTTP 301→HTTPS · 线上 md5 `1be423fd…` 与本地一致
- 源文件 `html/index.html`（本仓库）

**环境笔记：** Hetzner 无 `rsync`，用 `scp`。CF 两个 token 均无 DNS 读写权限
（凭证文件已自注「created without permission scopes」）—— 需要改 DNS 时得先补 scope。

## [2026-08-23] build | Academy Tracker 上线 academy.wenjyue.com

**需求：** 一个追踪 academy 交付进度的应用，**一个项目一个 tab**。
（Jay：FB-018-3 与 N821 同属一个项目 —— 3 小时实操考试。）

**架构**（Hetzner 5.223.54.57，无 node/go，用 Python 3.10 stdlib 零依赖）：

| 层 | 位置 |
|---|---|
| 前端 | `/var/www/academy.wenjyue.com/index.html` — 原生 JS，无构建步骤 |
| 后端 | `/opt/academy-tracker/server.py` — `GET/PUT /api/state`、`/api/export`、`/api/health` |
| 数据 | `/opt/academy-tracker/data/state.json`（原子写 + 每次写入快照到 `backups/`，保留 60 份） |
| 托管 | systemd `academy-tracker.service`，端口 8110，`Restart=always` |
| 路由 | nginx `location /api/` 反代 8110；静态走 root |
| 简报 | 今晚的交付简报移至 `/brief/`（未删） |

**数据模型：** 通用交付矩阵 —— `project.matrix.{groups,cols}` × `course.cells["group|col"]`，
一个渲染器同时支撑两种形态：
- **PPT-PPA 考卷**：groups = SET A/B，cols = SOALAN/SKEMA/ANSWER SHEET/EQUIPMENT
- **WIM 教材**：groups = 单组，cols = NOSS 提取/JPW 分配/KP-KT/KK-PA/JPK 封套

状态六态循环：`none → draft → uploaded → panel → approved → issue`，加权算完成度。
种子数据 `app/seed.json` 全部来自本 session 已核实事实（fileId、实测页数、AUDIT 缺陷、Jennifer 原话）。

**验证（全部实测，非推断）：**
- API：GET/PUT/export/health 逐一通过；坏载荷被拒（`payload must have a projects array`）
- **持久化跨重启**：PUT 改一格 → `systemctl restart` → 值仍在；备份文件正常累积
- **前端实际渲染**：Chrome headless 截图两个 tab，DOM 关键串齐全，无 JS 错误
- 校验和：本地与服务器三份文件 md5 全部一致

**入口：** https://academy.wenjyue.com （`#ppt-ppa` / `#wim` 可直达指定 tab）
下载：右上「下载 JSON」→ `/api/export`；「下载快照 HTML」→ 离线单页。

**环境笔记：** deploy 用户无 node/pm2（PTPK 那批 Go 站由别的用户跑）；Hetzner 无 rsync，用 scp。

## [2026-08-23] note | academy.wenjyue.com 改写为 Minto Pyramid 三层结构

**要求（Jay）：** BLOT 结构 —— 第一层结论、第二层推理、第三层源数据；
且零背景的人能顺读理解全部内容。

**站点重组：**

| 路径 | 内容 |
|---|---|
| `/` | **新** — 三层金字塔文档（`app/doc.html`） |
| `/tracker/` | 进度看板（原根目录的 app） |
| `/brief/` | 旧版简报，保留未删（已被 `/` 取代） |
| `/api/*` | 状态 API（未动） |

**面向零背景读者的处理：** 顶部「30 秒背景」框（NOSS/JPK/pentauliahan 是什么、
Jennifer 与 Jay 是谁）；第三层含 12 条名词表；正文首次出现的术语用中文解释而非直接抛缩写。

**核实中发现并修正的一处自造事实：**
我此前在 tracker 里把截止日直接写成 `2026-08-27`，但 Jennifer 原话只说「下个星期四」，
**从未给出日期**。经核：2026-08-27 与 2026-09-03 都是星期四，距今分别为 4 天与 11 天。
→ 已从 seed.json 与线上 state 中移除该日期，改为标注「未确认，两种读法差 7 天」。
→ 教训：转述他人口语中的相对时间时，不得代为解析为绝对日期。

**同类标注：** 「12 个文件」口径是 Jay 提出、Jennifer **未反对**（非明确确认），
文档中已按「未被反对 ≠ 已确认」如实标注。

**验证：** 5 条路由全部 200；页内 4 个锚点与 4 条锚链接经 Python 比对无断链；
所有站内 href 逐条 curl 确认可达；Chrome headless 全页截图目视复核。
（注：`grep -c` 对该页返回 0 是 RTK 输出裁剪造成的假象，改用 Python 复核。）

## [2026-08-24] build | Round 1 — Baseline + NOSS 提取（graph engineering）

**角色图：** EXTRACTOR → ARCHITECT → AUTHOR/MARKER → ATTACHMENTS → AUDITOR（对抗性，不由生成者兼任）→ INTEGRATOR
**Baseline：** `output/jennifer-ppa-soalan/BASELINE.md` —— DoD、36 份缺口清单、AUDITOR 检查表、6 条红线

**执行：** Workflow `ppa-baseline-extract`，10 个 agent（5 EXTRACTOR ∥ 5 AUDITOR），
83 万 token，约 20 分钟。5 份提取 AUDITOR 全部 **PASS，零编造**。
产物：`output/jennifer-ppa-soalan/noss-extracts/*.md`；源文本 `raw/noss-character/txt/`

### 🔴 发现一：我此前把 C07 单元名改错，且已交付客户

2026-08-23 我依据 NOSS **目录页**把 N821 的 C07 从 `Staff Administration Supervision`
改成 `Office Administration Supervision`，并上传 Jennifer Drive。**改反了。**

实测 NOSS 全文：`Staff Administration Supervision` **8 次**（§6 职业能力清单、CPC 图表、
Competency Profile 的 CU TITLE 字段 ×2、§15.7 正文标题、COMPETENCY UNIT TITLE 字段、
TEM 表、配分表）；`Office Administration Supervision` **1 次**，且仅出现在目录索引行。
原文并列写明 `NOSS TITLE: Office Administration` / `COMPETENCY UNIT TITLE: Staff Administration Supervision`
—— 目录那一行把课程名与单元名混写了。

**已修正并重传**（旧 fileId 已删）：
`SOALAN` → `1NppuyrJXwGWgHZPiGR8S9psC5L2R_v-9` · `SKEMA` → `1xvdG4pwsXf7ENY1Bgj0IZ5aS3VNgpbo4`
从 Drive 下载回验：SOALAN 20 页 STAFF×4 OFFICE×0；SKEMA 19 页 STAFF×2 OFFICE×0。

**教训：** 单一来源（目录页）不足以推翻多处正文。多数决 + 字段语义（CU TITLE 字段 vs 目录索引）
才是判据。上一轮的「已修正」结论本身就是错的，我照单继承还扩大了范围。

### 🔴 发现二：FB-018-45 L4/L5 的 CoCU 正本缺失 —— 16 份文档全部阻塞

Drive 中名为 `CU, CP SALES & MARKETING - Level 4/5.pdf` 的文件**只是 Competency Profile**，
不是 Curriculum of Competency Unit。按 TOC，真正的 CoCU 在 L4 pp.15–74、L5 pp.17–95，
**未包含在任何已提供文件中**。

后果：这两个 Level **没有 Related Knowledge，也没有 Assessment Criteria**
（CP 只有 Performance Criteria，是不同字段）。按 BASELINE §4.1「每个评分点对应
Assessment Criteria」与红线「NOSS 没写的不准写」，**L4/L5 共 16 份无法开工**，须向 Jennifer 索取。

### 其他

- N821 提取发现 C03 工时算术不一致（76+260=336≠330，NOSS 自身缺陷）；
  A/S/E 栏位 C02–C07 未提取，若考题须映射 A/S/E 则覆盖不足
- G471 提取 Gaps 第 7 条「其他 CU 同样不符」经核为**错误**（C01/C03 实际吻合），待修
- M731 无任何工时数据，仅有百分比权重；6 个 CU 全核心、无选修
- FB-018-45 L5 的 C07 名称三源不一致（CP 作 Administration，TOC 与工时表作 Management），未擅自裁定

**工具坑：** Word COM 导出 PDF 报 HRESULT 错误时**仍会打印旧文件的体积**，
看似成功实则未写入；且 `cp` 因文件占用失败后旧文件仍在原名下 —— 两者叠加导致
一次「已上传修正版」实为上传旧版。**唯一可靠做法：从 Drive 下载回来验证内容。**


## [2026-08-26] fix | N821 Office Admin — CU 选择按 Jennifer 指示重排

**触发：** Jennifer 2026-08-26 00:04:11 WA 指示：「office admin共7个CU，3小时的实操必须cover4个cu内容，选择实操CU1 CU2 CU5 CU6」

**已改（Set A 和 Set B 均适用）：**
- 封面 NAMA UNIT KOMPETENSI：C01 C02 C05 C06 加粗（实操），C03 C04 C07 普通（口试）
- 实操 TUGASAN：由 7 个缩减为 4 个，删除 C03/C04/C07，保留 C01/C02/C05/C06
- Appendix：由 7 份减为 4 份（Appendix 1-4 对应 C01/C02/C05/C06）
- 新增 BAHAGIAN 5 口试题：10 题，C03×3 + C04×3 + C07×4，Set A/B 共用
- 页数：19pp → 13pp（自动计算后填入）

**产物：**
- output/jennifer-ppa-soalan/n821-001-3-office-admin-set-a-soalan.md (525 lines)
- output/jennifer-ppa-soalan/n821-001-3-office-admin-set-b-soalan.md (498 lines)
- Drive: [N821 SET A 26.08] id=1LsMnRjgU_ENSFc2vhlnY_la9cPtcpp94
- Drive: [N821 SET B 26.08] id=1AqJlXYohTEC-S-67_z-9vo02CJiEc9A9

**已送达 Jennifer（~00:25，3 张对照图）：** 主消息 + 封面对照图 + 结构对照图 + 口试页截图

**关闭 OPEN-QUESTIONS #1（部分）：** N821 CU 选择已确认；其余 5 个 NOSS 仍待 Jennifer 填选择表

## [2026-09-18] feat | video-film-editing — IT-072-3:2012 ADI Pekerjaan 教材套件（新科目）

**触发：** Jay 08:31 — 按政府官员的 Senai Palm Resort 培训模板夹（Drive `1lzKA3BgCuQLKsrWmevjdpr6yr_2zh3eJ`）为 IT-072 Video/Film Editing（Drive `173QrzPi93oDBW-jwuvKEmj_Gvzd8P0Z-`）做一整套：先 Proses Kerja，再 Lampiran 5 矩阵，再其他，编号顺序 + README。

**下载：** `raw/adi-mpc-template-2026-09/`（34 文件 + `_md/` 转换 + 两份幻灯片文字层）、`raw/it-072-video-editing/L3|L4|L5`（20 文件）。跳过 1.7 GB Core Abilities zip 和 MySPIKE 用户手册。

**产物 `video-film-editing/`：** README.md · 00-noss-extract.md (1112 行, 1960 h) · 01-proses-kerja.md (P01–P12) · 02-borang-matriks-lampiran-5.md/.xlsx (31/31 WA) · 03-jadual-latihan.md/.xlsx (2880 h / 576 h 理论) · 04-rangka-nota-pembelajaran/ (6) · 05-nota-pembelajaran/ (31 WA) · 06-jsu.md (6×20 题) · 07-soalan-penilaian-pengetahuan/ (6 卷) · 08-senarai-bukti-proses-kerja.md (39 证据) · 09-penilaian-kekompetenan.md · 10-susunan-fail-kompilasi.md

**分工：** Sonnet ×(3 scout + 1 extract + 6 nota + 6 soalan)，Haiku ×1 template inventory；01/02/03/06/08/09/10/README 本 session。脚本在 session scratchpad（build_matrix/build_jsu/build_jadual/office2md/pdftext）。

**发现：** pdftoppm 未装，图片型 PDF 只能走 pypdf 文字层或 agent 端 PyMuPDF+Tesseract；官方样本 Kompilasi（154 页）里没有讲义和考卷，只有成绩单；模板 3.3a 是 1 WA = 1 Nota，幻灯片 p.62 是 1 CU = 1 Nota。

**待定：** 申请公司名（⟪TBD⟫）；P01–P12 待公司 Pembimbing 确认；Core Abilities 讲义/考题未做；是否套 JPK_ENVELOPE。

## [2026-09-18] feat | video-film-editing/11-core-abilities — Core Abilities Z-009-1/2/3:2015 视频剪辑情境版

**触发：** Jay 09:19 — 官员 Drive 的 Core Abilities 笔记是通用/别的科目，要为 video-film-editing 填写。

**来源：** 官员 Drive zip `Core Abilities Level 1_2_3_4_5 Nota dan Soalan.zip`（1.87 GB；gog 在 360 MB 超时，改 rclone `--drive-root-folder-id` 成功）→ `raw/adi-mpc-template-2026-09/core-abilities/`，只解压 L1–L3 的 71 份 PDF/DOCX（跳过 mp4）→ PyMuPDF + Tesseract 转文本 `_txt/`，Sonnet 侦察写出 `_txt/00-INVENTORY.md`（14 模块、47 KP、16 套官方考卷的逐条大纲）。

**产物：** `11-core-abilities/00-ca-spec.md`（写作规格 + 模块→文件夹表）+ 14 个模块文件夹：**47 份 `KP-x.y.md`**（官方编号标题逐字保留、法律条文照抄，只把例子换成剪辑工作室情境，BM）+ **14 套 `Soalan-CAxx.md`**（各 20 MCQ，R/S/T = 10/6/4 脚本重数全部通过，CA03 60 分钟其余 30 分钟）。共约 10.7 万字。Sonnet ×14 写作 + ×1 侦察；4 套考卷比例初次不对，回炉改题后通过。

**其他：** 安装 Poppler 25.07（pdftoppm 现可用）；`video-film-editing/` 镜像到 Jay 自己的 Drive `gdrive:3u-pioneer-academy-noss/video-film-editing`（116 文件 = 本地）：https://drive.google.com/drive/folders/1CVkS-IfG_h528DtO-6nSwxZSF2tgEI0T ；README/09/10 已改指向 11。
**待定：** 考卷抬头 `⟪TBD: kod pusat bertauliah⟫`（14 处）；上课用官方通用版还是情境版由 Jay 定。
