# WIM Header Box Templates

Reference snippets for each WIM document type per Buku Panduan WIM Edisi 2020.
Copy the appropriate block and replace placeholder values before using.

## Required Header Fields

All WIM documents must include these four fields in the header section (first 20 lines):

| Field | Format | Example |
|-------|--------|---------|
| `Kod WIM / WIM Code` | `[NOSS]-[CU]/[DocCode]([Seq]/[Total])` | `S960-002-3:2020-C01/KP(1/5)` |
| `Effective / Berkuat Kuasa` | `YYYY-MM-DD` | `2024-01-01` |
| `Subject / Subjek` | Full subject name | `Aesthetic Services` |
| `Level / Tahap` | Numeric level | `3` |

---

## KP — Kertas Penerangan / Information Sheet (White / Putih)

```markdown
# KERTAS PENERANGAN / INFORMATION SHEET

**Kod WIM / WIM Code:** [NOSS_CODE]-[CU]/KP([Seq]/[Total])
**Effective / Berkuat Kuasa:** YYYY-MM-DD
**Subject / Subjek:** [Subject Name]
**Level / Tahap:** [N]
**Paper Colour / Warna Kertas:** WHITE / PUTIH
```

### Example — Aesthetic C01 KP(1/5)
```markdown
**Kod WIM / WIM Code:** S960-002-3:2020-C01/KP(1/5)
**Effective / Berkuat Kuasa:** 2024-01-01
**Subject / Subjek:** Aesthetic Services
**Level / Tahap:** 3
```

---

## KT — Kertas Tugasan / Assignment Sheet (Pink / Merah Jambu)

```markdown
# KERTAS TUGASAN / ASSIGNMENT SHEET

**Kod WIM / WIM Code:** [NOSS_CODE]-[CU]/KT([Seq]/[Total])
**Effective / Berkuat Kuasa:** YYYY-MM-DD
**Subject / Subjek:** [Subject Name]
**Level / Tahap:** [N]
**Paper Colour / Warna Kertas:** PINK / MERAH JAMBU
```

---

## KK — Kertas Kerja / Work Sheet (Blue / Biru)

```markdown
# KERTAS KERJA / WORK SHEET

**Kod WIM / WIM Code:** [NOSS_CODE]-[CU]/KK([Seq]/[Total])
**Effective / Berkuat Kuasa:** YYYY-MM-DD
**Subject / Subjek:** [Subject Name]
**Level / Tahap:** [N]
**Paper Colour / Warna Kertas:** BLUE / BIRU
```

---

## KA — Penilaian Pengetahuan / Knowledge Assessment (Pink / Merah Jambu)

```markdown
# PENILAIAN PENGETAHUAN / KNOWLEDGE ASSESSMENT

**Kod WIM / WIM Code:** [NOSS_CODE]-[CU]/KA
**Effective / Berkuat Kuasa:** YYYY-MM-DD
**Subject / Subjek:** [Subject Name]
**Level / Tahap:** [N]
**Paper Colour / Warna Kertas:** PINK / MERAH JAMBU
```

---

## PA — Penilaian Prestasi / Performance Assessment (Light Blue / Biru Muda)

```markdown
# PENILAIAN PRESTASI / PERFORMANCE ASSESSMENT

**Kod WIM / WIM Code:** [NOSS_CODE]-[CU]/PA
**Effective / Berkuat Kuasa:** YYYY-MM-DD
**Subject / Subjek:** [Subject Name]
**Level / Tahap:** [N]
**Paper Colour / Warna Kertas:** LIGHT BLUE / BIRU MUDA
```

---

## PM — Pelan Mengajar / Lesson Plan (Yellow / Kuning)

```markdown
# PELAN MENGAJAR TEORI / THEORY LESSON PLAN
# (or: PELAN MENGAJAR AMALI / PRACTICAL LESSON PLAN)

**Kod WIM / WIM Code:** [NOSS_CODE]-[CU]/PM
**Effective / Berkuat Kuasa:** YYYY-MM-DD
**Subject / Subjek:** [Subject Name]
**Level / Tahap:** [N]
**Paper Colour / Warna Kertas:** YELLOW / KUNING
```

---

## NOSS Codes by Subject

| Subject | NOSS Code | Default Level |
|---------|-----------|---------------|
| Aesthetic Services | `S960-002-3:2020` | 3 |
| BEV Diagnostic & Rectification | `G452-010-3:2023` | 3 |
| IT Computer System L3 | `IT-020-3:2013` | 3 |
| IT Computer System L4 | `IT-020-4:2013` | 4 |
| IT Computer System L5 | `IT-020-5:2013` | 5 |

---

## Running the Enforcer

```bash
# Scan all subjects and report non-compliant files
uv run python _tools/enforcer/header_box_enforcer.py --scan --all-subjects

# Scan a single subject
uv run python _tools/enforcer/header_box_enforcer.py --scan --subject Aesthetic

# Auto-insert missing header fields (manual verification required)
uv run python _tools/enforcer/header_box_enforcer.py --fix --all-subjects
```
