# preschool-teaching/ — NOSS P851-002-4:2025 Preschool Teaching (Pengajaran Prasekolah) **Level 4 / DKM** · ADI Pekerjaan 教材套件

> **交给政府官员的是 `output/`**（同 `video-film-editing/` 的做法，Jay 2026-09-18）：官员模板夹（Drive `1lzKA3Bg…`，本地 `raw/adi-mpc-template-2026-09/`）的 .xlsx/.docx/.pptx 原样填写，子文件夹和文件名与官员一致，后缀 ` (P851)`。清单：`output/INDEX-fail-pegawai.md`。下面的 00–12 `.md` 是内部记录/来源，不是交付物。
>
> **和 IT-072（Level 3）最大的不同：这是 Level 4 = DKM。** 时长、理论考卷形式、Core Abilities 层数、以及多一份 LPKC 都不一样，见第三节。

**读法：按编号 00 → 12 顺序读。** 每个文件开头都有一段"Apa dokumen ini"。
**做法来源：** MPC/JPK 官员培训模板夹 + `Panduan ADI Pekerjaan 552025.pdf` + `SLAID DKM ADI.pdf`（DKM 专场，图片版，已人工读完）+ `Buku Panduan Pembangunan Soalan Edisi 2024`（Tahap 4 主观题规则）。
**内容来源：** `raw/NOSS P851-002-4-2025 PRESCHOOL TEACHING.pdf`（Jay 提供，2026-09-18）→ 文字层 `raw/noss-p851-002-4-2025.txt` → `00-noss-extract.md`。
**语言：** 教材/表格 Bahasa Malaysia（KSPK/课程术语保留英文）；README 中文给 Jay 看。

---

## 一、流程（和 IT-072 一样，先懂这个）

```
NOSS (5 CU / 21 WA)                    Tadika 实际工序 P01…P12
     │                                          │
     └──── 02 Borang Matriks (Lampiran 5) ──────┘   ← 每个 WA 都有工序覆盖 (21/21)
                        │
          03 Jadual Latihan（30 个月：20% 理论 960 h / 80% 工作 3840 h）
                        │
        ┌───────────────┴───────────────┐
   理论线 (20%)                     工作线 (80%)
   04 Rangka → 05 Nota (21 份)       08 Senarai Bukti（每道工序收什么证据）
   06 JSU → 07 Soalan（主观题）           │
   11 Core Abilities L1–L4               12 LPKC（DKM 专属项目报告）
        └───────────────┬───────────────┘
              09 Penilaian（Lampiran 6 + 4 + 成绩单 + LPKC 评分）
                        │
              10 两个实体文件夹怎么装订
```

## 二、文件清单（读的顺序 = 做的顺序）

| # | 文件 | 这是什么 | 状态 |
|---|---|---|---|
| 00 | `00-noss-extract.md` | NOSS 全文抽取：CPC、CP（每个 WA 的 Performance Criteria）、CoCU（Related Knowledge/Skills/Attitude、Assessment Criteria）、TEM、§18 权重、附录 A/B。**唯一真相来源。** ⚠️ 这份 2025 版 NOSS **全篇没有课时表**（只有权重），所有课时字段是 `⟪TBD⟫`——ADI 的课时不靠 NOSS 课时，靠模板公式，所以不阻塞。 | ✅ 1075 行 |
| 01 | `01-proses-kerja.md` | Tadika 的 12 道真实工序 P01–P12（到校/健康检查、休息进食、如厕、放学、RPT、RPH+BBM、上课、教学反思、教室环境+库存、行为管理、评估+档案、家长社区活动），每步对应 WA/PC。**申请公司 = 一家 tadika，名字 ⟪TBD⟫。** | ✅ 草稿，待 Pembimbing 确认 |
| 02 | `02-borang-matriks-lampiran-5.md` | Lampiran 5：21 WA × P01–P12，21/21 覆盖 | ✅ |
| 03 | `03-jadual-latihan.md` | §A 时数：30 月 × 160 = 4800 h；理论 20% = 960 h；CA L1–L4 = 120 h；余 840 h ÷ 5 CU = 168 h/CU = 21 天；共 120 天 = 120 周。§B 理论周表：CA 1–15 → C01 16–36 → C02 37–57 → C03 58–78 → C04 79–99 → C05 100–120。§C 工序周表。§D Jadual 3 的短时长变体（有资格/经验者 1–1.5 年）。 | ✅ 日期待填 |
| 04 | `04-rangka-nota-pembelajaran/Cxx-rangka.md` | 每个 WA 的讲义大纲（Bab = Related Knowledge 逐字） | ✅ 5 份 |
| 05 | `05-nota-pembelajaran/Cxx-W0n.md` | **21 份讲义**，1 WA = 1 Nota，五段式（Tajuk/Tujuan/Penerangan/3 问/Rujukan），每 Bab ≥250 词 | ✅ 21 份 |
| 06 | `06-jsu.md` | JSU **主观题版**（官员 3.2 模板的 `JSU STD THP 4-5 (SUBJEKTIF)` sheet）：每 CU 1 Struktur (a–d) + 1 Esei | ✅ |
| 07 | `07-soalan-penilaian-pengetahuan/Cxx.md` | 5 套**主观题**考卷：Struktur 20 分 + Esei 20 分 = 40 分，1 小时，及格 60%，附 Skema Jawapan 和"答案出处"表（每个得分点都能在讲义里 grep 到）。格式规则：`00-format-subjektif-tahap4.md` | ✅ 5 份 |
| 08 | `08-senarai-bukti-proses-kerja.md` | 每道工序要收的工作证据（RPT/RPH/BBM/出勤/库存/观察记录/进度报告/活动照片…）及反向 WA → 证据表；新增家长肖像/记录同意书 ⟪TBD⟫（未成年人，PDPA） | ✅ |
| 09 | `09-penilaian-kekompetenan.md` | Lampiran 6 / Lampiran 4 / 成绩单（5 CU 主观题 + 22 个 Core Abilities）/ LPKC 评分 70-15-15 / DKM 核查 = 面试 + 档案 + LPKC | ✅ |
| 10 | `10-susunan-fail-kompilasi.md` | 两个实体夹装订顺序（加 LPKC 软拷贝 PDF） | ✅ |
| 11 | `11-core-abilities/` | **尚未做（Phase 2）。** DKM 要 L1+L2+L3+L4 = 4+4+6+8 = 22 个模块、120 h。IT-072 那套是"视频剪辑情境版"，不能直接给幼教用；L4 官方原件已从 zip 解出并转文字：`raw/adi-mpc-template-2026-09/core-abilities/_txt/Z-009-4-2015__*` + `00-INVENTORY-L4.md`。 | ⏳ 见第四节 |
| 12 | `12-lpkc.md` + `12-lpkc-template-outline.md` | **LPKC（Laporan Projek Kompetensi Calon）指南** — DKM 专属：Jadual 10 格式、Bab 1–4 结构、10 个 tadika 可做的项目题目（覆盖 5 个 CU）、评分 70/15/15、15–20 页幻灯 30+10 分钟、30 个月内的建议时间线；以及可直接填的骨架 | ✅ |

## 三、Level 4 (DKM) 和 Level 3 (SKM) 的差异 — 每条都有出处

| 项 | IT-072 (Tahap 3) | **P851 (Tahap 4 / DKM)** | 出处 |
|---|---|---|---|
| 时长 | 18 月 / 2880 h | **30 月 / 4800 h**（NOSS 从 Tahap 4 起算，无资格 <2 年经验）；有 SKM3 → 1 年；有学术/TVET 证书 → 1–1.5 年 | Panduan ADI Jadual 1 & 3 (p.6–7); SLAID DKM p.6–7 |
| 理论 20% | 576 h | **960 h** | 模板 4.2 公式 |
| Core Abilities | L1–L3 = 80 h (14 模块) | **L1–L4 = 120 h (22 模块)**；L4 = Z-009-4:2015 八个模块 | SLAID Bengkel slide 73; SLAID DKM p.10 |
| 理论考卷 | 20 MCQ / 30 分钟 | **主观题 2 题（1 Struktur + 1 Esei）/ 1 小时**，60% 及格 | Panduan ADI Jadual 8 (p.22); 3.2 模板末 sheet; Buku Panduan Soalan 2024 §5.5.6 |
| 核查 (verifikasi) | 面试 + 档案 | 面试 + 档案 + **LPKC 答辩** | Panduan ADI §3.4.2; SLAID DKM p.15 |
| 额外交付 | — | **LPKC**（15–80 页，Bab 1–4，评分表 JPK/ADI/04-2024） | Panduan ADI §3.3.5, Jadual 10–11 |
| 注册费 | RM300 | **RM500/program** | SLAID DKM p.3 |

## 四、还没有的 / 需要 Jay 决定的

用 `rg "⟪TBD" preschool-teaching/` 列全部待补项。最重要的：

1. **申请公司是哪家 tadika**（`⟪TBD: nama tadika/syarikat ADI⟫`）。ADI Pekerjaan 的申请主体是雇用 Bakat 的公司；3U Pioneer Academy 只能当 Pusat Latihan。所有表格的抬头都等这个。
2. **时长选 30 月还是 Jadual 3 的短版**——取决于 Bakat 的入学资格（有 SKM3 / 幼教证书 / 工作经验就短很多）。周表按 30 月做的，换了要重排 `03` 和 `output/03`。
3. **Core Abilities 怎么给**：(a) 直接用 JPK 官方通用版（`raw/…/core-abilities/`，L1–L4 齐全，可免费向 JPK 申请 Nota）；(b) 像 IT-072 一样做幼教情境版（22 模块 ≈ 70+ 份 KP + 22 套题，另开一轮）。**我建议先 (a) 交件，(b) 排 Phase 2。** 另注意：L4 官方考卷本身是主观题，但 Panduan ADI 3.3.2 规定 CA 考卷"至少 20 题客观选择题"——两者冲突，交件前问官员。
4. **LPKC 题目**：`12-lpkc.md` 给了 10 个候选，由 Bakat + Pembimbing 定一个。
5. P01–P12 的时间要对齐 tadika 实际学年（RPT 在 1 月前、进度报告在学期末）——`03` §C 里标了，Pembimbing 定。

## 五、注意事项

- 每个 CU 的内容只认 `00-noss-extract.md`；改内容先改 00，再改下游。
- 讲义 header 里的 `PROSES KERJA BERKAITAN` 和 `JAM PENGETAHUAN` 在 md 里是 `⟪TBD⟫`，**生成 output 时由脚本从 02 矩阵和 §18 权重自动填**（168 h × WA 权重），对照表在 `output/_tools/derived-wa-hours.md`。
- 本文件夹**没有**套 `<!-- JPK_ENVELOPE_v1 -->`（那是 WIM/SLDN 格式），同 IT-072 的决定。
- 生成/重跑 output：`uv run --with openpyxl --with python-docx --with python-pptx --with docxcompose python preschool-teaching/output/_tools/build_output.py all`；PDF 用 `output/_tools/Export-Pdf.ps1`（需要本机 Word）。
