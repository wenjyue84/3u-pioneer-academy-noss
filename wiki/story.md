# The Government's Teaching Manual — Building WIMs for 3U Pioneer Academy

> *This is not a technical document. This is a story.*

---

## Chapter 1: The Gap Between a Standard and a Classroom

Malaysia's skills training system runs on a document called NOSS — the National Occupational Skills Standard. Written by JPK (Jabatan Pembangunan Kemahiran) and mandated by the Ministry of Human Resources, NOSS tells the world exactly what a Level 3 Tuina therapist, a BEV diagnostic technician, or a computer systems operator must be able to do before they can receive a nationally-recognised skills certificate.

But NOSS is a *standard*, not a *lesson plan*. It tells you what competency looks like at the finish line. It does not hand you the classroom materials — the handouts, the exercises, the practical worksheets, the exam papers. That gap is filled by a second set of documents: **WIM** (Workplace Instructional Material), also called Bahan Instruksional Tempat Kerja (BIT).

3U Pioneer Academy runs programmes across four different NOSS codes — Tuinalogy, Aesthetic Services, BEV Diagnostic & Rectification, and IT Computer System (the same IT-020 series also being tackled in the textbook project). Each of those programmes, to achieve JPK accreditation, needs a full set of WIM documents: one per Competency Unit, seven document types per unit, produced to an exact JPK format with government logos and identification tables on every page.

That is an enormous amount of structured writing.

---

## Chapter 2: Seven Colours of Paper, Hundreds of Documents

The WIM system is precise by design. JPK mandates seven distinct document types for every Competency Unit, each printed on a different colour of paper so teachers and students can navigate the classroom physically:

| Document | Colour | Purpose |
|----------|--------|---------|
| PM-teori (Lesson Plan — Theory) | Yellow | The teacher's theory class plan |
| KP (Information Sheet) | White | Knowledge content — one sheet per Related Knowledge item |
| KT (Assignment Sheet) | Pink | Exercises mirroring each KP |
| PM-amali (Lesson Plan — Practical) | Yellow | The teacher's practical class plan |
| KK (Work Sheet) | Blue | Step-by-step practical activity guide |
| KA (Knowledge Assessment) | Pink | Written exam paper |
| PA (Performance Assessment) | Light blue | Practical skill evaluation checklist |

Multiply seven document types by every Competency Unit across four subjects at multiple levels, and the scope becomes clear: this is not a writing task, it is a *content manufacturing* task. The noss-to-wim project exists to automate as much of that manufacturing as possible.

The pipeline works from the NOSS CoCU (Curriculum of Competency Unit) — the third component of every NOSS document, written for training personnel — extracting each Knowledge and Performance item, then generating the WIM documents in structured Markdown before rendering them to the JPK-required format.

---

## Chapter 3: Four Subjects, One Pipeline

The project covers four subject areas, each at a different stage of completion:

| Subject | NOSS Code | Status |
|---------|-----------|--------|
| Tuinalogy 推拿疗法 | MP-031-3:2016 | Active — enriched with images + Chinese WIM |
| Aesthetic Services | S960-002-3:2020 | Content complete |
| BEV Diagnostic & Rectification | G452-010-3:2023 | Content complete |
| IT Computer System | IT-020-3/4/5:2013 | Content complete (L3 primary) |

Tuinalogy is the most complex — it has both Core (C) and Elective (E) competency units, and the WIM content includes Chinese-language materials to serve the bilingual context of the training cohort. A `10us.md` file tracks every ten-story SPIRAL milestone in Chinese, reflecting the pace and language of real operations.

Every subject folder mirrors the same internal architecture: a `00-README.md` entry point, a `00-noss-extract.md` as the raw source of truth, a `01-jpw-distribution.md` for the 30/70 knowledge/performance hour split, and then one folder per Competency Unit containing all seven WIM file types.

The JPK format specification — every WIM document must carry a government logo and a standard identification table — is documented in `wiki/07-jpk-format-spec.md` and enforced by validators in the build pipeline.

---

## Chapter 4: Where Things Stand

As of April 2026, three of four subjects are marked content-complete. Tuinalogy remains active, with image enrichment and Chinese-language WIM content still in progress. The SPIRAL-driven generation pipeline (tracked in `spiral_events.jsonl` and `progress.txt`) has run hundreds of stories to produce and validate the content.

The remaining work is on the compliance and quality-assurance side: ensuring every generated document passes the JPK format validators, that the 30/70 hour distribution is correctly reflected in lesson plans, and that Tuinalogy's bilingual content meets the same standard as the English-only subjects.

If the full WIM library is accepted by JPK, 3U Pioneer Academy gains the instructional backbone to run four nationally-accredited programmes. If it stalls — typically on format errors or missing document types — the accreditation submission cannot proceed and the academy's expansion plans wait.

The pipeline is largely built. The last mile is quality, not quantity.

---

*Written: 2026-05-22 | Status: Active (Tuinalogy in progress; 3 of 4 subjects content-complete)*

---

## Chapter 5: A New Chapter — AI-Powered Digital Marketing

As three of four original subjects reach completion, 3U Pioneer Academy looks to expand. The next programme — AI-Powered Digital Marketing Specialist — breaks from the established NOSS pattern: instead of adopting an existing government-written standard, the academy is developing its own through the COPTPA route, with Prisma Technology as the proposing Industry Body.

The content is grounded in real operations: the marketing workflows documented for a Johor Bahru café (AI-generated menus, multilingual reviews, social media prompts) and a city-centre homestay (SEO/GEO articles, OTA management, direct booking campaigns) serve directly as classroom case studies. Students learn from live business operations, not textbook scenarios.

With 7 Core Competency Units covering the full digital marketing lifecycle — strategy, content, visuals, video, web presence, campaign analytics, and customer engagement — and 2 electives in automation and AI search optimisation, the programme targets the fastest-growing skills gap in Malaysian SMEs.

*Updated: 2026-07-19*
