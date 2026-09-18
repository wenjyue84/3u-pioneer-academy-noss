# now.md — 3U Pioneer Academy / Character Intl. Academy

Last updated: 2026-09-18 09:30 MYT

## 🆕 2026-09-18 — IT-072 Video/Film Editing · ADI Pekerjaan 套件（`video-film-editing/`）

Jay 参加 MPC「Bengkel Personel ADI Siri 3/2026」（17–19 Sep, Le Grandeur Palm Resort Senai）。按官员模板夹做了 IT-072-3:2012 的全套 00–10（Proses Kerja → Lampiran 5 → Jadual → Nota → JSU → Soalan → Bukti → Penilaian → 装订）。入口 `video-film-editing/README.md`。
**待 Jay：** 申请公司是谁（ADI 主体必须是雇主，3U 只能当 Pusat Latihan）；P01–P12 让公司 Pembimbing 过目；Core Abilities 材料从官员 Drive 的 1.7 GB zip 取。


## 当前主线 —— Jennifer PPA Soalan（Character Intl. Academy）

Jennifer（Tan Siow Inn，`60126111677`，`jennifer@character.com.mx`）2026-08-20 23:53 发来 Drive
链接，要 Jay 帮忙出 **PPT-PPA 实操考卷（SOALAN + SKEMA）**。

Drive：`PPA SOALAN TO JAY FOR REFERENCE` — `11ATUjjbzsg7lbnZIRblc9x1ejoTlMHRg`
读取方式：`gog drive ls --account wenjyue@gmail.com --parent <id>`
⚠️ Drive MCP 的 `parentId` 查询对此文件夹返回空，**不可用**，一律走 gog。

### ✅ 2026-08-24 全量交付完成

全部 36 份 PPT-PPA 考卷文档已生产并上传 Jennifer Drive。

| NOSS | 课程 | Drive 文件夹 | 状态 |
|------|------|------------|------|
| FB-018-3:2012 L3 | Sales & Marketing Operation | 原 Jennifer 文件夹 | ✅ SET A (Jennifer) + SET B (我方) 齐 |
| N821-001-3:2020 L3 | Office Administration | `169-72I6UsuhSU55ExxVUDfSNzgmonCf1` | ✅ SET A + B 四件套已齐 |
| M731-001-3:2021 L3 | Digital Marketing Operation | `1UVrPhmrG0dkE-2YbSeFcQCzT-JZH_h30` | ✅ SET A + B 四件套已齐 |
| G471-001-3:2018 L3 | Retail Outlet Operations | `1w_BdONXPVyTBVDUQOUv7dKCkq3K8RQOn` | ✅ SET A + B 四件套已齐 |
| FB-018-45:2012 L4 | Sales & Marketing Administration | `1yRsIymqd3AzLMIzoHJ7epf2zsDJqBigC` | ✅ SET A + B 四件套已齐 |
| FB-018-45:2012 L5 | Sales & Marketing Management | `1B-ExSfT9MdjzoD0r23H_ZUuDftlXpFfc` | ✅ SET A + B 四件套已齐 |

**页数（Word COM 实测回填）：**

| SET | SOALAN | SKEMA | ANSWER SHEET | EQUIPMENT |
|-----|--------|-------|--------------|-----------|
| N821-B | 18pp | 21pp | 4pp | 4pp |
| M731-A | 17pp | 10pp | 4pp | 4pp |
| M731-B | 18pp | 11pp | 4pp | 4pp |
| G471-A | 17pp | 18pp | 4pp | 4pp |
| G471-B | 16pp | 19pp | 4pp | 4pp |
| FB45L4-A | 14pp | 21pp | 4pp | 4pp |
| FB45L4-B | 14pp | 21pp | 4pp | 4pp |
| FB45L5-A | 17pp | 23pp | 4pp | 5pp |
| FB45L5-B | 17pp | 24pp | 4pp | 5pp |

⚠️ 页数只对 `build/wim_md_to_docx.py` 生成的 .docx 成立。Jennifer 若用自己模板重排，页数会变，声明须重算。

全部核实记录见 `LOG.md` [2026-08-24] delivery 条目。

### 📊 进度追踪应用 —— https://academy.wenjyue.com

**一个项目一个 tab**，状态存服务器（手机/电脑同一份），改动即时保存：

| Tab | 内容 | 完成度 |
|---|---|---|
| `#ppt-ppa` **PPT-PPA 考卷** | Character Intl. Academy，3 小时实操考试，6 个 NOSS/Level × SET A/B × 4 种文档 | 21% |
| `#wim` **WIM 教材** | 3U Pioneer Academy，7 个科目 | 72% |

- 交付简报移至 `/brief/`
- 下载：`/api/export`（JSON）或页内「下载快照 HTML」
- 源码 `app/`（`index.html` · `server.py` · `seed.json`）；服务 `academy-tracker.service`
- **状态改了要落在这里** —— 这个 app 现在是进度的真相来源，别再只更新 md

---

## ⚫ PTPK Skim TBT 2026 —— 已关闭，不再追踪

**Jay 2026-08-21 决定：不提交。** 2026-07-31 12:00 的截止日已过，未提交。
Yashini（`60184007417`，原联系人）已离职。

**从所有简报、扫描、追踪中移除。任何 agent 不得再把它当作待办。**

遗留物（保留不删，可能他用）：
- `proposals/ai-dm-proposal.md` · `ai-admin-proposal.md` · `ai-mfg-proposal.md` · `ai-iso-proposal.md`
  —— 四份草稿含约 39 个 `⟪TBD⟫`，**未清理，无需再清理**
- `_archive/proposals-baseline-290726/` — 基线快照
- ✅ **Hetzner 5 个 proposal 站已下架**（2026-08-21，Jay 授权；PM2 id=19~23 已删，port 3457~3461 无监听）
  详见 `LOG.md` [2026-08-21] infra 条目，含回滚指令。
  ⚠️ 遗留：nginx vhost 与 DNS 仍指向这 5 个域名，现在回 502 —— 是否清理待定。

---

## 仍然有效的发现（PTPK 死了但结论不死）

**NOSS code 更正** —— 旧 proposal 全部引用的 `DM-001-3:2026` 在 JPK 不存在，`DM-` 前缀也不合 JPK 格式。
正确为 **`M731-001-3:2021` Digital Marketing Operation**。
✅ 2026-08-20 Jennifer 已在 Drive 中提供该 NOSS 正本 PDF —— 等了 28 天的东西已到手。
此更正对任何未来的 DM 课程/考卷工作仍然适用。

**Character Intl. Academy 认证状态** —— 由「❓完全未确认」上调为「**部分证实**」：
Drive 中有 Character 名下**已批准**的 Beauty L1/L2/L3 PPT-PPA 考卷，抬头为 JPK/KSM「Pusat Bertauliah」。
→ 做 PPT-PPA 考卷即意味着持有 pentauliahan。
⚠️ 但 **pentauliahan 按 programme 发放**，Beauty（S960-002）不自动覆盖 Digital Marketing（M731）。
问题已从「Character 是否持牌」缩小为「**持牌范围是否含 M731 / N821 / G471**」—— 一句话可问清。

---

## Waiting On

| Who | What | Since |
|-----|------|-------|

---

## 项目惯例 —— 本批考题的三处偏离（待定，非缺陷）

1. 内容直接由 NOSS PDF 生成，**未先建 `00-noss-extract.md`**（CLAUDE.md 规定的 CU 真相来源）
   —— 代价已现：C07 单元名曾误写 `Staff` 而非 `Office` Administration Supervision，
   靠事后对 NOSS 目录逐条核验才抓出，已修正。
2. 产出置于 `output/` 而非科目文件夹惯例位置。
3. 未套 `<!-- JPK_ENVELOPE_v1 -->`。

**待 Jay 定性：** 这批是 **Character Intl. Academy 的 PPT-PPA 考卷**，不是 3U 的 WIM。
硬套 3U 的 WIM 惯例未必正确 —— 归属定了，惯例才好定。

---

## WIM / NOSS 建置现况（Workstream A，未受 PTPK 关闭影响）

- 4 个科目已全量套 JPK envelope：aesthetic-services · bev · IT · tuinalogy ✅
- ai-digital-marketing 55 个 WIM 文件已重新盖章 ✅
- E01 + E02 KP 文件各 3 份已建 ✅

---

## Reference

- Buku Panduan WIM Edisi 2020：https://anyflip.com/jpvdh/aagk/basic
- MySPIKE 持牌中心查询：https://www.myspike.my/index.php?r=umum-pb%2Findex-umum
- Jennifer 语音转录（机器转写，引用具体数字前须复核）：`wiki/08-jennifer-voicenotes-20260724.md`
- WhatsApp 脉络：`wiki/06-whatsapp-context.md`
- 正确 DM NOSS 出处：https://www.pptvm.org/blog/noss-199/m731-001-3-2021-digital-marketing-operation-noss-2080
