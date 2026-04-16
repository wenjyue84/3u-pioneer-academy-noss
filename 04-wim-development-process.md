# WIM Development Process

## 5-Step Development Process

### Step 1: Determine Training Program
- Identify the NOSS code and level
- Obtain the official NOSS document from DSD/MySPIKE
- Confirm the NOSS version is current

### Step 2: Identify CoCU
- Extract the Curriculum of Competency Unit (CoCU) from the NOSS document (Component III)
- List all Competency Units with their codes
- Note total training hours per CU and overall program hours

### Step 3: Refine CoCU
- Panel review of CoCU content
- Verify work activities, knowledge, and skills are current
- Confirm training hours allocation is appropriate
- Validate Tools, Equipment & Materials (TEM) list

### Step 4: Prepare JPW (Jadual Pembahagian WIM)
- Create the WIM Distribution Schedule
- Determine quantity and titles of:
  - KP (Information Sheets) per CU
  - KT (Assignment Sheets) per CU
  - KK (Work Sheets) per CU
  - PM (Lesson Plans) — theory and practical per CU
- Map each Work Activity to specific WIM documents
- Calculate page counts and time allocation

### Step 5: Develop Instructional Materials
Write each document following prescribed format:

#### For each CU, produce:

**Theory Set:**
1. PM Teori (Theory Lesson Plan) — YELLOW
2. KP (Information Sheets) — WHITE — one per knowledge topic
3. KT (Assignment Sheets) — PINK — one per KP

**Practical Set:**
4. PM Amali (Practical Lesson Plan) — YELLOW
5. KK (Work Sheets) — BLUE — one per practical task/work activity

**Assessment:**
6. KA (Knowledge Assessment) — PINK — minimum 1 hour
7. PA (Performance Assessment) — LIGHT BLUE — minimum 2 hours

## Who Can Develop WIM?

- Personnel who have completed a **5-day WIM Development Course** (via CIAST/MySPIKE)
- Personnel with **VTO (Vocational Training Operation)** certification
- Panel must include subject matter experts (industry practitioners)

## Quality Assurance

1. Internal review by qualified panel
2. Content accuracy verification by subject matter experts
3. Format compliance check against Buku Panduan WIM Edisi 2020
4. Language review (grammar, technical accuracy)
5. Coding system verification
6. Cross-reference against NOSS CoCU — every Related Knowledge and Related Skill must be covered

## Common Mistakes to Avoid

1. Writing textbook-style content instead of competency-based WIM
2. Not coding documents correctly
3. Missing the 30/70 theory/practical split
4. KP explaining "how" instead of "why" (procedures belong in KK)
5. KT questions not matching KP content
6. KK missing safety/environment checklist
7. Not covering all Work Activities from CoCU
8. Incorrect paper color assignment

## File Organization for This Project

For each subject, we organize WIM .md files as:

```
subject-folder/
├── 00-README.md              # Subject overview, CU list, navigation
├── 00-noss-extract.md        # Full NOSS data extraction (source of truth)
├── 01-jpw-distribution.md    # JPW — WIM distribution schedule
├── C01/                      # Competency Unit 1
│   ├── PM-teori.md           # Theory Lesson Plan
│   ├── KP-01.md              # Information Sheet 1
│   ├── KP-02.md              # Information Sheet 2
│   ├── KT-01.md              # Assignment Sheet 1
│   ├── KT-02.md              # Assignment Sheet 2
│   ├── PM-amali.md           # Practical Lesson Plan
│   ├── KK-01.md              # Work Sheet 1
│   ├── KK-02.md              # Work Sheet 2
│   ├── KA.md                 # Knowledge Assessment
│   └── PA.md                 # Performance Assessment
├── C02/                      # Competency Unit 2
│   └── ...
└── ...
```

Each .md file follows WIM format requirements and will later be converted to .docx/.pdf with proper formatting (fonts, paper colors, headers, coding).
