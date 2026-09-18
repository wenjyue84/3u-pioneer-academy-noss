# video-film-editing/ — NOSS IT-072-3:2012 Video / Film (Editing) Level 3 · ADI Pekerjaan 教材套件

**读法：按编号 00 → 10 顺序读。** 每个文件开头都有一段"Apa dokumen ini"（这份文件是什么、从哪来、喂给谁）。
**做法来源：** MPC/JPK 政府官员的培训模板夹（Drive `1lzKA3Bg…`，本地 `raw/adi-mpc-template-2026-09/`）+ 17–19 Sep 2026 Le Grandeur Palm Resort Senai 的 Bengkel Personel ADI 议程。
**内容来源：** IT-072 NOSS 文件夹（Drive `173QrzPi…`，本地 `raw/it-072-video-editing/L3/`）。L4/L5 的 NOSS 主文件也已下载，但本套件只做 **L3**。
**语言：** 教材/表格用 Bahasa Malaysia（技术词保留英文，JPK 规定一份笔记只能一种语言）；README 用中文给 Jay 看。

---

## 一、先懂这个流程，文件就不乱了

ADI Pekerjaan（Akademi Dalam Industri — 在岗培训取证）和学校式 WIM 不一样：**学员（Bakat）80% 时间在公司干活，20% 时间上理论课**，最后由 JPK 派外部核查官（PPL-ADI）来看两样东西——理论考卷分数 + 工作证据夹。所以整套材料是从"公司每天做什么"倒推出来的，而不是从 NOSS 章节顺序正推：

```
NOSS (CU/WA)                         公司实际工序 (Proses Kerja P01…P12)
     │                                          │
     └──────── 02 Borang Matriks (Lampiran 5) ──┘   ← 两边对上，证明每个 WA 都有工序覆盖
                        │
          03 Jadual Latihan（18 个月怎么排：20% 理论 / 80% 工作）
                        │
        ┌───────────────┴───────────────┐
   理论线 (20%)                     工作线 (80%)
   04 Rangka Nota → 05 Nota          08 Senarai Bukti（每道工序要收什么证据）
   06 JSU → 07 Soalan (20 MCQ/CU)         │
        └───────────────┬───────────────┘
              09 Penilaian（Lampiran 6 + 4 + 成绩单）
                        │
              10 两个实体文件夹怎么装订
```

这正是议程上的顺序：Topik 4 Pemetaan NOSS Matrik vs Proses Kerja → Topik 5 Jadual Latihan → Topik 6 Bahan Pembelajaran → Topik 7/8 JSU & Soalan → Topik 7(Sabtu) Bukti Proses Kerja & Verifikasi PPL。

## 二、文件清单（读的顺序 = 做的顺序）

| # | 文件 | 这是什么 | 对应 Jay 说的 WIM 部件 | 状态 |
|---|---|---|---|---|
| 00 | `00-noss-extract.md` | NOSS 全文抽取（CPC、6 个 CU 的 Work Activities、Performance Criteria、CoCU 的 Related Knowledge/Skills、时数、Assessment Criteria、工具、参考书）。**唯一真相来源**，后面每个文件都只能引用它，不能加 NOSS 没有的内容。 | Learning outcome（每个 CU 的 CoCU Learning Outcome 在这里） | ✅ 1112 行 |
| 01 | `01-proses-kerja.md` | 公司（剪辑工作室）的 12 道真实工序 P01–P12，每道列出步骤、对应的 WA/PC、会产生什么证据。**Jay 要求的第一步。** | Kertas Kerja（工作步骤） | ✅ 草稿，待公司 Pembimbing 确认 |
| 02 | `02-borang-matriks-lampiran-5.md` + `.xlsx` | JPK 官方表格 Lampiran 5：行 = 31 个 WA，列 = P01–P12，✓ = 覆盖。**Jay 要求的第二步。** Excel 版与官方模板同布局，可直接打印进 Fail Pelaksanaan。 | — | ✅ 31/31 WA 全覆盖 |
| 03 | `03-jadual-latihan.md` + `.xlsx` | 18 个月排程：A) 理论时数分配（2880 h × 20% = 576 h；CA 80 h + 每 CU 82.67 h，按模板 4.2 公式）；B) 理论周表；C) 工序周表。给了 interleaved 和 block-release 两种模型。 | — | ✅ 日期待填 |
| 04 | `04-rangka-nota-pembelajaran/<CU>-rangka.md` | 每个 WA 的讲义大纲：Bab = CoCU 的 Related Knowledge 条目（逐字），先定大纲再写正文（模板 3.3a 的做法）。 | Kertas Penerangan 的目录 | 6 个文件（agent 产出） |
| 05 | `05-nota-pembelajaran/<CU>-W0n.md` | **31 份讲义**，一个 WA 一份（模板 3.3a 规则：1 WA = 1 Nota）。五段式：Tajuk / Tujuan / Penerangan（一章一个 Related Knowledge）/ 3 道课堂问答 / Rujukan。 | Kertas Penerangan | 31 个文件（agent 产出） |
| 06 | `06-jsu.md` | 出题规格表 Jadual Spesifikasi Ujian：每 CU 20 题 / 30 分钟，难度 Rendah 10 : Sederhana 6 : Tinggi 4，构念 Prosedur 10 : Fakta 6 : Sikap 4，再按 WA 数分配（逐字抄 JPK 的 4/5/6-WA 表）。**先有 JSU 才能出题。** | 理论题的"配方" | ✅ 脚本生成并断言校验 |
| 07 | `07-soalan-penilaian-pengetahuan/<CU>.md` | 6 套理论考卷，每套 20 道 MCQ + 答案 + 每题标注 WA/难度/构念/出处（讲义哪一章）。按 JPK MCQ 格式规则写。 | Soalan（teori） | 6 个文件（agent 产出） |
| 08 | `08-senarai-bukti-proses-kerja.md` | 实操"考题"：ADI 没有单独的实操考试，**工作证据就是实操评估**。每道工序要收哪 39 份证据、编号、对应 CU-WA；并反向列出每个 WA 有哪些证据（给 Lampiran 6 用）。 | Soalan（praktikal） | ✅ |
| 09 | `09-penilaian-kekompetenan.md` | 评估三张表预填：Lampiran 6（PPL 核查报告，31 个 WA × 证据编号）、Lampiran 4（导师声明 P01–P12）、成绩单（6 CU + Core Abilities，60% 及格）；以及公司需要自建的 10 张内部表格清单。 | Assessment | ✅ |
| 10 | `10-susunan-fail-kompilasi.md` | 两个实体夹的装订顺序（按 JPK 已批准样本的 9 个分节）+ 每节从本文件夹哪个文件打印；附"Jay 的 WIM 词汇 ↔ ADI 文件"对照表。 | 其他 | ✅ |
| 11 | `11-core-abilities/` | **Core Abilities（Z-009-1/2/3:2015）视频剪辑情境版**。T3 学员必须累计通过 L1+L2+L3 共 14 个模块（80 h）才能进 PPL 核查。JPK 官方材料是通用版（工厂、机器、矿场例子）——这里保留官方每份 Kertas Penerangan 的编号标题和法律条文，只把例子换成剪辑工作室情境。`00-ca-spec.md` = 写作规格与模块→文件夹对照；每模块文件夹 = 若干 `KP-x.y.md`（对应官方 KP）+ `Soalan-CAxx.md`（20 MCQ + 答案）。官方原件在 `raw/adi-mpc-template-2026-09/core-abilities/`（PDF）和 `…/_txt/`（文本 + `00-INVENTORY.md` 清单）。 | Core Abilities 的 KP + Soalan | 47 份 KP + 14 套考卷（agent 产出） |

## 三、还没有的 / 需要 Jay 决定的

用 `rg "⟪TBD" video-film-editing/` 可以列出全部待补项。最重要的三个：

1. **申请公司是谁**（`⟪TBD: nama syarikat⟫`）。ADI Pekerjaan 的申请主体是雇用 Bakat 的公司，3U Pioneer Academy 只能当 Pusat Latihan。Lampiran 5、成绩单、Surat Tawaran 都要公司名和 letterhead。
2. **P01–P12 要公司 Pembimbing 过目**——我按行业通行的后期流程写的，如果工作室实际不做外拍（P12），删掉即可，E01 是选修。
3. **Core Abilities** 已按 Jay 指示做成视频剪辑情境版（`11-core-abilities/`）；官方通用版 zip（1.87 GB）已下载到 `raw/adi-mpc-template-2026-09/core-abilities/`，L1–L3 的 PDF 已解压（视频未解压）。用哪一版给学员上课由 Jay 定——JPK 考的是官方能力陈述，两版标题一致。

次要：3 名人员（Penyelaras / Pembimbing / Pengajar）的 Kursus Induksi 证书和委任信；MySPIKE 注册截图；09-D 列出的 10 张公司内部表格的 Word 模板。

## 四、注意事项

- **每个 CU 的 Learning Outcome / Related Knowledge 只认 `00-noss-extract.md`**。改内容先改 00，再改下游。
- 讲义按"1 WA = 1 Nota"写（2026-07 模板 3.3a）；官员幻灯片第 62 页说"一份笔记覆盖整个 CU"——两者不冲突，打印时把同一 CU 的几份装订成一本即可，封面字段见幻灯片第 65 页（Logo/Alamat Syarikat、Nama Nota、Kod Program、Tahap、Kod CU、No. WA、No. Kod Nota、Muka Surat）。
- 本文件夹**没有**套 3U 其他科目用的 `<!-- JPK_ENVELOPE_v1 -->`——那是 WIM/SLDN 格式，ADI Pekerjaan 用的是 MPC 模板的封面字段。要不要统一，Jay 定。
- 原始参考：`raw/adi-mpc-template-2026-09/`（含 `_md/` 转换文本、两份幻灯片的文字层 `SLAID-*.txt`）、`raw/it-072-video-editing/`。
