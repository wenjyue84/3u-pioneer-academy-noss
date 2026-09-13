# 审计报告 — Jennifer 的 FB-018-3:2012 SET A 样本

**审计日期：** 2026-08-21
**受审文件（Jennifer 的 Drive，`gog drive download` 取得原件）：**

| 文件 | fileId | 页数 |
|---|---|---|
| `SOALAN PENILAIAN AMALI PPT （SET A).pdf` | `1aXOCpgJaT5grOt7ER7MKH8QuGF6tGXFn` | 14 |
| `SKEMA PENILAIAN AMALI PPT-PPA (SET A).pdf` | `1TwY-fPMkviqWlhYIFOemOWvafby1PelR` | 11 |
| `ASSESSMENT ANSWER SHEET.pdf` | `17OhhRHGcWVdHu31z4WhRMGhew2DrRetN` | 未审 |
| `EQUIPMENT VERIFICATION.pdf` | `1hDi-MSwvSH4vy629B37uUyTKXdOaRhHP` | 未审 |

**比对基准：** `CU, CP S&M- FB-018-3 2012.pdf`（`1m9UiWNbjGb_bJBpZ7gTyFttZYgD5xREj`，NOSS 正本）

> Jennifer 原话（经 Jay 转述）：样本「不完全正确」，要 Jay 检查后再用 AI 出新卷。
> 以下每一条都可追溯到本次实际读取的 PDF 文本，未依赖推测。

---

## ✅ 先说对的部分

**CU 清单与 NOSS 完全一致。** 对照 NOSS 正本逐条核过：

C01 Market & Product Survey · C02 Direct/Retail Sales · C03 After Sales Service ·
C04 Self Sales Performance Assessment · C05 Online Sales · C06 Product Marketing · E01 Inventory Control（选修）

**KPI 演算全部正确。** SKEMA 中 6 项达成率逐条验算无误：
90/120=75.00% · 65/80=81.25% · 35/50=70.00% · 30/40=75.00% · 8/12=66.67% · 8/12=66.67%

**口试配分自洽。** 10 题（5.1–5.10）× 每题满分 3 = 30，换算式 `(Markah/30) × 20` 与 20% 权重一致。

**SKEMA 结构完整。** 结尾有 `JUMLAH MARKAH KESELURUHAN` 与 PPL-PPT 签名栏 —— **未截断**
（初查曾疑似缺页，复核后排除）。

---

## 🔴 确认缺陷

### D1 — 两份文件的「印刷页数」声明都写错

| 文件 | 封面声明 | 实际页数 | 差 |
|---|---|---|---|
| SOALAN | `KERTAS INI MENGANDUNGI **13** MUKA SURAT BERCETAK` | **14** | −1 |
| SKEMA | `SKEMA PEMARKAHAN INI MENGANDUNGI **14** MUKA SURAT BERCETAK TERMASUK MUKA HADAPAN` | **11** | +3 |

JPK 考卷封面须声明印刷页数，用于防抽页。两处都不符，属合规瑕疵，PPL 审卷会挑。

### D2 — E01 Inventory Control 声明了却完全没有评分【最严重】

- SOALAN 封面：`SENARAI KOMPETENSI ELEKTIF  E01 INVENTORY CONTROL`
- SKEMA 封面：`NAMA UNIT KOMPETENSI ELEKTIF  INVENTORY CONTROL`
- **但整份 SKEMA 中 `Inventory` 出现 0 次、`E01` 出现 0 次** —— 正文、评分表、口试题（5.1–5.10）无一处涉及。

→ 选修单元被列入考卷，却无任何题目或分数对应。要么补 E01 的题与分，要么从两份封面撤下。

### D3 — SKEMA 封面漏了 E01 代码

SOALAN 写 `E01 INVENTORY CONTROL`，SKEMA 只写 `INVENTORY CONTROL`，少了代码。两份须一致。

### D4 — 拼写错误 `Terlibut` → 应为 `Terlibat`

出现在评分表栏目名 `KRITERIA PENILAIAN | CU Terlibut | Markah`，**至少 2 处**（SKEMA p10、p11）。
马来文「涉及」为 *terlibat*。

---

## 🟠 风险项（须 PPL 确认，我不下定论）

### R1 — 实作部分只练到 3 个 CU，另 3 个仅靠口试

封面声明 6 个必修 CU，但：

| 部分 | 权重 | 实际覆盖 |
|---|---|---|
| Proses Kerja + Hasil Kerja + Sikap | **80%** | C01 · C04 · C05 |
| Sesi Soal Jawab（口试） | **20%** | C02 · C03 · C06 |
| — | — | **E01 完全未覆盖（见 D2）** |

KETERAMPILAN 一栏本身也只写了三件事：
`CONDUCT MARKET & PRODUCT SURVEY, PREPARE ONLINE SALES COLLATERAL AND EVALUATE SALES PERFORMANCE`。

C02（Direct/Retail Sales）、C03（After Sales Service）、C06（Product Marketing）**确实有被评到**
（口试 5.1–5.4 属 CU2、5.5–5.7 属 CU3、5.8–5.10 属 CU6）—— 我最初误判为「完全未覆盖」，此处已更正。

**但这是 *Penilaian Amali*（实作评估）。** 三个 CU 的 work activity 只用口头问答验证、
不经实作，是否满足 JPK 对 PPA 的要求，需 PPL 或 JPK 方面确认。若不满足，需为
C02/C03/C06 各补实作任务。

---

## ⚠️ 这些缺陷已经传染到我方产出

我方 `n821-001-3-office-admin-set-a-soalan.md` 是照她的格式生成的，因此继承了：

1. **页数声明为照抄的占位值**（写死 `14 MUKA SURAT`）—— md 转 docx 前无法得知真实页数，
   **必须在 build 后回填真实页数**，否则重蹈 D1。
2. 已发生并已修复的同类问题：C07 单元名曾误写 `Staff` Administration Supervision，
   NOSS 正本为 `Office` Administration Supervision —— 靠对 NOSS 目录逐条核验才抓出。
   → **印证了本项目 CLAUDE.md「每个 CU 的真相来源 = `00-noss-extract.md`」这条规矩存在的理由。**
3. 我方目前只做了 soalan + skema **两件**；Jennifer 的完整样本是**四件套**，
   另有 `ASSESSMENT ANSWER SHEET` 与 `EQUIPMENT VERIFICATION` —— **我方缺这两件**。

---

## 建议动作

| # | 动作 | 归属 |
|---|---|---|
| 1 | 修正 SOALAN/SKEMA 封面页数声明（D1） | 可代 Jennifer 改 |
| 2 | 决定 E01：补题补分，或从封面撤下（D2） | **须 Jennifer 定** |
| 3 | SKEMA 封面补上 `E01` 代码（D3） | 可代改 |
| 4 | 全文 `Terlibut` → `Terlibat`（D4） | 可代改 |
| 5 | 向 PPL 确认 R1：口试是否足以覆盖 C02/C03/C06 | **须 Jennifer 问 PPL** |
| 6 | 补做 ANSWER SHEET + EQUIPMENT VERIFICATION 两件 | 我方 |
| 7 | 审 `ASSESSMENT ANSWER SHEET.pdf` 与 `EQUIPMENT VERIFICATION.pdf`（本次未审） | 我方 |

---

## 未审 / 未知

- `ASSESSMENT ANSWER SHEET.pdf`、`EQUIPMENT VERIFICATION.pdf` 本次**未下载未审**。
- Beauty L1/L2/L3「已批准」那批**未审** —— 若那批是 JPK 已通过的，则它才是更权威的格式基准，
  值得优先拿来对照（本次以 FB-018-3 SET A 为基准，因它是 Jennifer 明确点名的样本）。
- Character Intl. Academy 的 pentauliahan 是否涵盖 N821 / M731 / G471，**仍未确认**。
