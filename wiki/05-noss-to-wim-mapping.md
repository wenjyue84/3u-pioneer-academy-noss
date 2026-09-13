# NOSS to WIM Mapping Guide

## The Conversion Chain

```
NOSS Document
    |
    +-- Component I (Standard Practice) --> WIM Front Matter (context only)
    |
    +-- Component II (Standard Content)
    |       |
    |       +-- CPC --> WIM CPC page (copied/reformatted)
    |       +-- CP  --> WIM learning objectives (derived from)
    |
    +-- Component III (CoCU)
            |
            +-- Work Activities ---------> KK (Work Sheets)
            +-- Related Knowledge -------> KP (Information Sheets)
            +-- Related Skills ----------> KK (Work Sheets)
            +-- Attitude/Safety/Env -----> KK checklists + KP safety sections
            +-- Training Hours ----------> PM (Lesson Plans) time allocation
            +-- Assessment Criteria -----> KA + PA (Assessment papers)
            +-- TEM ---------------------> KK equipment lists
```

## Detailed Mapping Rules

### CoCU "Related Knowledge" → KP (Information Sheet)

| CoCU Field | Maps To | Rule |
|------------|---------|------|
| Each Related Knowledge item | One or more KP pages | Group related items into one KP if they form a logical topic |
| Knowledge sub-items | KP sections/subsections | Each sub-item becomes a section within the KP |

**Content approach for KP:**
- Explain the "WHY" — theory, principles, concepts
- Include definitions, classifications, diagrams
- Reference standards, regulations, best practices
- Do NOT include step-by-step procedures (those go in KK)

### CoCU "Related Skills" + "Work Activities" → KK (Work Sheet)

| CoCU Field | Maps To | Rule |
|------------|---------|------|
| Each Work Activity | One or more KK | Complex WAs may need multiple KKs |
| Related Skills | KK step-by-step procedures | Each skill becomes actionable instructions |
| TEM | KK equipment/material list | Listed at top of each KK |
| Attitude/Safety/Env | KK safety checklist | Appended as assessment checklist |

**Content approach for KK:**
- Step-by-step "HOW" instructions
- Include labeled diagrams and illustrations
- List all tools, equipment, and materials needed
- Include safety precautions and PPE requirements
- End with assessment checklist (process, output, attitude, safety)

### CoCU "Related Knowledge" → KT (Assignment Sheet)

| CoCU Field | Maps To | Rule |
|------------|---------|------|
| Each KP topic | Corresponding KT | One KT per KP |
| Knowledge items | Question topics | Questions test comprehension of KP content |

**Question types for KT:**
- Multiple choice (minimum 4 options)
- True/False with justification
- Short answer
- Fill in the blanks
- Matching
- Essay/discussion questions
- Diagram labeling

### CoCU "Training Hours" → PM (Lesson Plan)

| CoCU Field | Maps To | Rule |
|------------|---------|------|
| Theory hours (30%) | PM Teori | Allocate across KP+KT delivery |
| Practical hours (70%) | PM Amali | Allocate across KK delivery |

### CoCU "Assessment Criteria" → KA + PA

| CoCU Field | Maps To | Rule |
|------------|---------|------|
| Knowledge assessment criteria | KA questions | Minimum 1 hour exam |
| Performance assessment criteria | PA tasks | Minimum 2 hours practical exam |

## Quantity Planning Formula

For each Competency Unit (CU):

```
Number of KP = Number of distinct knowledge topics in CoCU
Number of KT = Number of KP (1:1 mapping)
Number of KK = Number of Work Activities (or more if WA is complex)
Number of PM = 2 (one theory, one practical)
Number of KA = 1 per CU
Number of PA = 1 per CU
```

## Example Mapping

**NOSS:** G452-010-3:2023 — CU C01: Perform BEV Pre-Inspection

| CoCU Item | WIM Document | Content |
|-----------|-------------|---------|
| RK 1: BEV components and systems | KP(1/4): BEV Components Overview | Theory on BEV architecture |
| RK 2: Safety procedures for HV systems | KP(2/4): HV Safety Procedures | Theory on HV safety |
| RK 3: Diagnostic tools and equipment | KP(3/4): Diagnostic Tools | Theory on tool types/usage |
| RK 4: Pre-inspection checklist standards | KP(4/4): Inspection Standards | Theory on standards |
| WA 1: Inspect vehicle exterior | KK(1/3): Vehicle Exterior Inspection | Step-by-step procedure |
| WA 2: Inspect HV system safety | KK(2/3): HV System Safety Check | Step-by-step procedure |
| WA 3: Complete inspection report | KK(3/3): Inspection Reporting | Step-by-step procedure |
