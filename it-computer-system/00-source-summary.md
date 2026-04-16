# IT-020 Computer System Management -- Source Summary for WIM Conversion

**Source project:** `C:\Users\Jyue\Documents\1-projects\noss-it020-textbook\`
**Content root:** `content/IT-020-{3,4,5}/*.md` (single source of truth)
**Client:** 3U Pioneer Academy Sdn Bhd
**NOSS Programme:** IT-020 Computer System Management
**Date:** 2026-04-16

---

## 1. Three Levels Overview

| Code | Level | Title (EN) | Title (BM) | CoCU Count | Total Contact Hours |
|------|-------|-----------|-------------|------------|---------------------|
| IT-020-3:2013 | L3 | Computer System Operation | Operasi Sistem Komputer | 7 | 1,200 hrs |
| IT-020-4:2013 | L4 | Computer Systems Administration | Pentadbiran Sistem Komputer | 6 | 1,240 hrs |
| IT-020-5:2013 | L5 | Computer Systems Management | Pengurusan Sistem Komputer | 7 | 1,970 hrs |
| **Total** | | | | **20** | **4,410 hrs** |

Knowledge/Performance split: 30% Knowledge / 70% Performance across all levels.

---

## 2. All CU Titles by Level

### IT-020-3 (L3) -- Computer System Operation (1,200 hrs)

| CoCU | Title | Hours | % |
|------|-------|-------|---|
| 1 | Computer System Set-up | 300 | 25% |
| 2 | Computer System Maintenance | 120 | 10% |
| 3 | Computer System Repair | 180 | 15% |
| 4 | Server Installation | 240 | 20% |
| 5 | Server Maintenance | 180 | 15% |
| 6 | Computer Network Connectivity Set-up | 120 | 10% |
| 7 | Mobile Device Configuration | 60 | 5% |

**Work activities per CoCU (L3 example -- CoCU 1):**
1. Analyse job request/change order (10%, 30 hrs)
2. Prepare computer set-up tools, hardware parts and software (15%, 45 hrs)
3. Set-up computer hardware (30%, 90 hrs)
4. Carry out computer software installation (20%, 60 hrs)
5. Set-up computer peripherals (10%, 30 hrs)
6. Carry out unit functionality test (10%, 30 hrs)
7. Prepare computer system set-up report (5%, 15 hrs)

### IT-020-4 (L4) -- Computer Systems Administration (1,240 hrs)

| CoCU | Title | Hours | % |
|------|-------|-------|---|
| 1 | Server Configuration | 200 | 16% |
| 2 | Computer System Security Control | 200 | 16% |
| 3 | Computer System & Network Procurement | 200 | 16% |
| 4 | Network Cabling Management | 200 | 16% |
| 5 | Computer Network Installation Management | 240 | 19% |
| 6 | Computer System Maintenance Management | 200 | 16% |

### IT-020-5 (L5) -- Computer Systems Management (1,970 hrs)

| CoCU | Title | Hours | % |
|------|-------|-------|---|
| 1 | Computer Systems Planning and Operations Management | 200 | 10% |
| 2 | Computer System Asset Management | 350 | 18% |
| 3 | Computer System Security Management | 300 | 15% |
| 4 | Disaster Recovery Management | 350 | 18% |
| 5 | Computer System & Network Project Management | 350 | 18% |
| 6 | Computer System & Network SOP Development and Implementation Management | 300 | 15% |
| 7 | Server Scripting | 120 | 6% |

---

## 3. CoCU Content Structure Pattern (Gold Standard)

Each CoCU `.md` file in `content/` follows a consistent structure. The gold standard is `content/IT-020-3/01_CoCu-1-Computer-System-Set-up.md`.

### Section Order

1. **Title heading** -- `# CoCu N: Title (X hrs)`
2. **NOSS header table (page 1)** -- PROGRAM CODE AND NAME, LEVEL, UNIT TITLE, WORK ACTIVITY STATEMENT, NO. CODE + PAGE range
3. **Set-up Context table** -- 2 columns comparing two operational scenarios (e.g. Desktop/Standard vs Workstation/Custom, or Preventive vs Corrective). Rows: scope/trigger, tools, reporting.
4. **Key Terms / Tools table** -- `Type of Tools | Description` or `Type | Description`. Full prose descriptions per tool/concept.
5. **Contact Hour Distribution table** -- `% | Hrs | Work Activity | Knowledge 30% | Performance 70% | Total`. Totals to 100%.
6. **NOSS header table (page 2)** -- Same header, different PAGE range (second part of the CoCU document).
7. **Hardware Component table** -- `Hardware Component | Description`. Full prose per component.
8. **Inline images** -- e.g. `![RAID Level Comparison](images/raid-levels.png)`
9. **Software Component table** -- `Software Type | Description` or `Software / Configuration Tool | Description`.
10. **Common Faults table** -- `Common Fault | Cause | Action`.
11. **Learning Outcome Matrix** -- `Work Activity | Knowledge Outcome | Performance Outcome | Assessment Method | Evidence Required`.
12. **Practical Exercises** -- Lab exercises with: Objective, Duration, Equipment Required, Procedures (numbered steps), Expected Outcome, Assessment Checklist (checkbox items). One lab per work activity (7 labs for CoCU 1).

### Supporting Files per Level

- `00_Contact-hour_*.md` -- Contact hour summary, work activities by CoCU, Tools and Equipment List Appendix, CoCU document index with PAGE numbers.
- `00_standard-practice.md` -- Introduction, occupational structure, pre-requisites, career pathways.
- `CLAUDE.md` -- Level-specific agent instructions (if any).
- `images/` -- Referenced illustrations (PNG).

---

## 4. Content Inventory -- What Exists vs What Is Missing

### Content Files Present

| Level | File | Status |
|-------|------|--------|
| **L3** | 00_Contact-hour | Complete |
| | 00_standard-practice | Complete |
| | 01_CoCu-1-Computer-System-Set-up | Complete (gold standard, includes Learning Outcome Matrix + 7 Practical Labs) |
| | 02_CoCu-2-Computer-System-Maintenance | Complete |
| | 03_CoCu-3-Computer-System-Repair | Complete |
| | 04_CoCu-4-Server-Installation | Complete |
| | 05_CoCu-5-Server-Maintenance | Complete |
| | 06_CoCu-6-Computer-Network-Connectivity-Set-up | Complete |
| | 07_CoCu-7-Mobile-Device-Configuration | Complete |
| **L4** | 00_Contact-hour | Complete |
| | 00_standard-practice | Complete |
| | 01_CoCu-1-Server-Configuration | Complete |
| | 02_CoCu-2-Computer-System-Security-Control | Complete |
| | 03_CoCu-3-System-Network-Procurement | Complete |
| | 04_CoCu-4-Network-Cabling-Management | Complete |
| | 05_CoCu-5-Computer-Network-Installation-Management | Complete |
| | 06_CoCu-6-Computer-System-Maintenance-Management | Complete |
| **L5** | 00_Contact-hour | Complete |
| | 00_standard-practice | Complete |
| | 01_CoCu-1-Management-Overview | Complete |
| | 02_CoCu-2-Computer-System-Asset-Management | Complete |
| | 03_CoCu-3-Computer-System-Security-Management | Complete |
| | 04_CoCu-4-Disaster-Recovery-Management | Complete |
| | 05_CoCu-5-Computer-System-Network-Project-Management | Complete |
| | 06_CoCu-6-SOP-Development-And-Implementation | Complete |
| | 07_CoCu-7-Server-Scripting | Complete |

All 20 CoCU files and all supporting files are present. No content is missing from the source.

### Images Present (content/images/)

- asset-lifecycle.png
- cable-wiring-t568.png
- dr-recovery-sites.png
- maintenance-schedule.png
- network-topologies.png
- osi-tcpip-model.png
- project-lifecycle.png
- raid-levels.png
- security-zones.png
- server-rack-layout.png
- troubleshooting-flowchart.png

---

## 5. Mapping to WIM Components (KP, KT, KK, PM)

WIM (Work Instruction Manual / Workbook Instruction Manual) uses four core components:

| WIM Code | WIM Component | NOSS Source Content |
|----------|---------------|---------------------|
| **KP** (Kertas Penerangan / Information Sheet) | Theory and knowledge content -- concepts, definitions, principles, diagrams | Maps from: **Key Terms/Tools tables**, **Hardware Component tables**, **Software Component tables**, **Set-up Context descriptions** (prose sections). These provide the 30% Knowledge component. |
| **KT** (Kertas Tugasan / Assignment Sheet) | Written assignments and questions to assess understanding | Maps from: **Learning Outcome Matrix** (Knowledge Outcome column, Assessment Method column for written tests). Currently structured as table rows; needs conversion to question/assignment format. |
| **KK** (Kertas Kerja / Worksheet / Practical Sheet) | Hands-on practical exercises with step-by-step procedures | Maps from: **Practical Exercises** section (Lab exercises with Objectives, Procedures, Equipment, Assessment Checklists). These provide the 70% Performance component. |
| **PM** (Penilaian / Assessment) | Assessment criteria, rubrics, and evidence requirements | Maps from: **Learning Outcome Matrix** (Assessment Method + Evidence Required columns), **Assessment Checklists** in Practical Exercises, **Common Faults tables** (can inform troubleshooting assessment scenarios). |

### Mapping Detail by CoCU Section

| Existing Section | Primary WIM Target | Secondary WIM Target |
|------------------|-------------------|---------------------|
| NOSS Header table | WIM cover page metadata | -- |
| Set-up Context table | KP (scenario descriptions) | KT (compare/contrast assignment) |
| Key Terms / Tools table | KP (theory content) | KT (identification questions) |
| Contact Hour Distribution | WIM hour allocation | -- |
| Hardware Component table | KP (theory content) | KK (identification practical) |
| Software Component table | KP (theory content) | KK (installation practical) |
| Inline images | KP (diagrams/illustrations) | KK (reference during practical) |
| Common Faults table | KP (troubleshooting theory) | KK (troubleshooting practical), PM (scenario assessment) |
| Learning Outcome Matrix | PM (assessment criteria) | KT (knowledge assessment), KK (performance assessment) |
| Practical Exercises / Labs | KK (primary source) | PM (assessment checklists) |

### Conversion Notes

1. **KP extraction is straightforward** -- each CoCU already has rich prose descriptions in tables that map directly to information sheets. One KP per work activity or per CoCU.
2. **KT needs to be generated** -- the existing content has learning outcomes but not formatted as assignment questions. Written test items, short-answer questions, and case study prompts need to be derived from the Knowledge Outcome column.
3. **KK is mostly ready** -- the Practical Exercises sections already follow a lab-exercise format with numbered procedures, equipment lists, and checklists. These need reformatting into WIM KK template but content is complete.
4. **PM needs structuring** -- assessment criteria exist across Learning Outcome Matrix and Assessment Checklists but need consolidation into formal rubrics with pass/fail criteria and scoring.
5. **Standard Practice** (`00_standard-practice.md`) maps to the WIM front matter / programme overview section.
6. **Contact Hour** files map to the WIM allocation tables.

---

## 6. Reference Material Locations

| What | Path |
|------|------|
| Content source (single truth) | `noss-it020-textbook/content/IT-020-{3,4,5}/` |
| Original course .doc files | `noss-it020-textbook/_reference/course-originals/IT-020-{3,4,5}/` |
| WhatsApp reference (L3 CoCU originals) | `noss-it020-textbook/_reference/from-whatsapp/` |
| Kitchen template (WIM formatting reference) | `noss-it020-textbook/_reference/kitchen-template/Kitchen LV2 C01.docx` |
| NOSS framework docs | `noss-it020-textbook/_reference/noss-framework/` |
| Generated .docx output | `noss-it020-textbook/output/NOSS-IT-020-{3,4,5}-*.docx` |
| Build scripts | `noss-it020-textbook/scripts/` |
