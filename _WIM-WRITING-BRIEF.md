# WIM Writing Brief — one Competency Unit, 12 files

You write the complete JPK WIM teaching material for ONE Competency Unit. The output goes to a
Malaysian government accreditation reviewer (JPK / PTPK). Format compliance and factual honesty
matter more than volume.

Your caller tells you two things: the **programme directory** (e.g. `ai-iso`) and the **CU code**
(e.g. `C03`). Everything else is here.

Repo root: `C:\Users\Jyue\Documents\1-projects\3u-pioneer-academy-noss\`

---

## 1. Read before writing

1. `<repo>\<programme-dir>\00-cu-spec.md` — the curriculum source of truth. Find your CU's section:
   CU code, CU title (EN + ZH), 4 Work Activities, 3 knowledge topics (→ KP-01/02/03), 2 practical
   tasks (→ KK-01/02), and the programme's "Malaysian grounding" list.
2. `<repo>\ai-digital-marketing\C01\KP-01.md` and `KK-01.md` — read **only** for house format and
   depth standard. Their subject matter is digital marketing; do not carry it into another
   programme.

Anything in 00-cu-spec.md marked `[derived — not in proposal]` is in scope, but treat it as the
thinnest part of the spec and say so in your report.

## 2. Write 12 files into `<repo>\<programme-dir>\<CU>\`

| File | Type | What it is |
|------|------|-----------|
| `KP-01.md` `KP-02.md` `KP-03.md` | Kertas Penerangan | Information Sheet, one per knowledge topic. **200–330 lines each.** The core teaching content: explain concepts properly, worked Malaysian examples, tables, step-by-step tool procedures. |
| `KK-01.md` `KK-02.md` | Kertas Kerja | Work Sheet, one per practical task. Work Activity Title · Learning Outcomes · Tools & Materials table · Safety Precautions · numbered Steps · Trainee Answer/Record section. |
| `KT-01.md` `KT-02.md` `KT-03.md` | Kertas Tugasan | Assignment Sheet mirroring each KP. Tujuan Tugasan · Arahan · tasks answerable **purely from that KP** · Kriteria Penilaian totalling 100 marks · Masa Diperuntukkan · Rujukan. |
| `KA.md` | Kertas Penilaian Pengetahuan | Section A multiple choice · Section B structured · Section C applied/essay · marking scheme. May only test content present in KP-01..03. |
| `PA.md` | Kertas Penilaian Prestasi | Observation checklist mapped to **all 4** Work Activities, plus a rubric describing performance levels. |
| `PM-teori.md` | Pelan Mengajar (Teori) | Session-by-session theory plan totalling **exactly 12 hours**. |
| `PM-amali.md` | Pelan Mengajar (Amali) | Session-by-session practical plan totalling **exactly 28 hours**, structured around the 4 Work Activities. |

Lesson-plan table columns: Sesi · Masa · Tajuk · Objektif Pembelajaran · Aktiviti P&P · Bahan/ABBM ·
Penilaian. Instructor name and signature fields stay **blank** for handwriting — never invent a name.

12 + 28 = 40 hours per CU. The 30 % theory / 70 % practical split is a hard JPK requirement: the
session hours must add up exactly, not approximately.

## 3. The JPK envelope — every file opens with it

Reproduce the `<!-- JPK_ENVELOPE_v1 -->` block structure verbatim from the reference file (logo
table, JPK Putrajaya address, doc-type heading, Medan/Nilai table, closing `<!-- /JPK_ENVELOPE_v1 -->`).

Populate from 00-cu-spec.md:
- `KOD DAN NAMA PROGRAM`, `TAHAP`, `KOD DAN TAJUK UNIT KOMPETENSI`
- `NO. DAN PERNYATAAN AKTIVITI KERJA` — the 4 Work Activities, uppercase, numbered. Identical in
  all 12 files.

| Doc | `NO. KOD` suffix | `WARNA KERTAS` | Heading |
|-----|------------------|----------------|---------|
| KP | `/KP(n/3)` | `PUTIH (White)` | `## KERTAS PENERANGAN` |
| KK | `/KK(n/2)` | `BIRU (Blue)` | `## KERTAS KERJA` |
| KT | `/KT(n/3)` | `MERAH JAMBU (Pink)` | `## KERTAS TUGASAN` |
| KA | `/KA(1/1)` | `MERAH JAMBU (Pink)` | `## KERTAS PENILAIAN PENGETAHUAN` |
| PA | `/PA(1/1)` | `BIRU MUDA (Light Blue)` | `## KERTAS PENILAIAN PRESTASI` |
| PM-teori | `/PM-T(1/1)` | `KUNING (Yellow)` | `## PELAN MENGAJAR (TEORI)` |
| PM-amali | `/PM-A(1/1)` | `KUNING (Yellow)` | `## PELAN MENGAJAR (AMALI)` |

`NO. KOD` is prefixed with the CU code from the spec, e.g. `ISO-AI-3:2026-C03/KP(1/3)`.

**TAJUK and TUJUAN must be real.** The older ai-digital-marketing files carry a known defect —
placeholder metadata like `**TAJUK:** KP-01` and `**TUJUAN:** Kertas rujukan untuk KP-01.` Do not
reproduce it. Every file gets a genuine descriptive title and a real one-sentence purpose.

## 4. Quality rules

**Bilingual house style.** Malay document furniture, headings and instructions; English technical
terms kept in English. Match the reference file.

**Internal consistency is what a reviewer checks first.** KA and KT may only test what KP-01..03
actually teach. PA may only assess the 4 Work Activities. If you define an acronym or framework,
use one expansion everywhere — an earlier CU shipped with its KA answer key contradicting its KP
body text, and that is exactly the kind of defect that gets flagged.

**Arithmetic must survive checking.** Session hours sum to the stated total. Marks sum to 100.
Any worked example's numbers actually work out.

**Never fabricate.** No invented instructor names, IC numbers, certificate numbers, company names,
SSM numbers, or statistics. For any regulated figure — statutory contribution rates, tax
thresholds, penalty amounts, commencement dates, section numbers — either you are confident it is
current, or you teach the mechanism and point the trainee at the issuing authority's current
guideline. A wrong legal or statutory figure in a government-submitted teaching document is worse
than no figure.

Where a worked example needs data, **define a synthetic dataset inside the document** and print it
in full, so every number traces to the page it appears on.

If a fact is genuinely needed but unknown, use the greppable placeholder:
`⟪TBD: what is needed | who must supply it | needed-by⟫`

## 5. Report back (max 250 words, no file dumps)

- The 12 filenames written
- The TAJUK chosen for each KP and KK
- Confirmation of the 12 / 28 hour totals
- Every regulated figure you chose to state, so it can be verified — and every one you
  deliberately left as a lookup
- Any place 00-cu-spec.md was too thin to write good material
