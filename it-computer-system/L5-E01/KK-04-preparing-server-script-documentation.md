<!-- JPK_ENVELOPE_v1 -->
<table border="0" cellspacing="0" cellpadding="8" width="100%">
<tr>
<td width="130" valign="top"><img src="../_assets/logos/jpk-logo.png" alt="JPK Logo" width="110"></td>
<td valign="middle">
<b>JABATAN PEMBANGUNAN KEMAHIRAN (JPK)</b><br>
TINGKAT 7-8, BLOK D4, KOMPLEKS D,<br>
PUSAT PENTADBIRAN KERAJAAN PERSEKUTUAN,<br>
62530 PUTRAJAYA
</td>
</tr>
</table>

## KERTAS KERJA

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-5:2013 PENGURUSAN SISTEM KOMPUTER |
| TAHAP | 5 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-E01 SERVER SCRIPTING |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ASSESS SERVER SCRIPTING REQUIREMENT<br>2. DEVELOP SERVER SCRIPT<br>3. EXECUTE AND DEPLOY SERVER SCRIPT<br>4. PREPARE SERVER SCRIPT DOCUMENTATION |
| NO. KOD | IT-020-5:2013-E01/KK(4/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-04-preparing-server-script-documentation

**TUJUAN:** Kertas rujukan untuk KK-04-preparing-server-script-documentation.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

Produce the full documentation package for the `Get-LocalUserAudit.ps1` script deployed in KK(3/4), including all documents required for operational handover to the IT Operations team.

---

## Tempoh / Duration

5 hours

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Workstation with VS Code or equivalent Markdown editor | 1 per trainee |
| 2 | Git client with training repository | 1 per trainee |
| 3 | KP(4/4) Information Sheet for reference | 1 |
| 4 | Script Technical Reference template (from KP(4/4)) | 1 |
| 5 | Operational Runbook template (from KP(4/4)) | 1 |
| 6 | Printer (for handover package physical copy) | 1 (shared) |

---

## Langkah Keselamatan / Safety Precautions

- Do not include any real passwords, API keys, or production system details in documentation
- Documents produced during this exercise are training materials — mark all pages as "TRAINING USE ONLY"
- Ensure Git repository does not contain sensitive configuration data before committing documentation

---

## Bahagian A — Inline Documentation Audit and Completion

### Procedure

| Langkah | Arahan / Instruction |
|---------|---------------------|
| A1 | Open `scripts/windows/Get-LocalUserAudit.ps1` from your training repository. Review the existing comment-based help block. Verify it contains all required sections: `.SYNOPSIS`, `.DESCRIPTION`, `.PARAMETER` (one per parameter), `.EXAMPLE` (minimum 2), `.INPUTS`, `.OUTPUTS`, `.NOTES` (with version, date, author, requires, change log). |
| A2 | If any sections are missing or incomplete, complete them now. The `.DESCRIPTION` must be at least 3 sentences explaining purpose, input, and output. Each `.PARAMETER` must explain the type, valid range (if applicable), and default value. |
| A3 | Verify `Get-Help .\Get-LocalUserAudit.ps1` returns correct and complete help output. Screenshot or copy the output to your work log. |
| A4 | Review all in-body comments. Every non-obvious code block must have a comment explaining WHY (not just what). Identify at least 3 places where a comment is missing or inadequate and add appropriate comments. |
| A5 | Commit the updated script: `git commit -m "docs: complete comment-based help and improve inline comments for Get-LocalUserAudit"` |

---

## Bahagian B — Script Technical Reference (STR)

### Procedure

| Langkah | Arahan / Instruction |
|---------|---------------------|
| B1 | Create a new file `docs/STR-Get-LocalUserAudit.md` in your training repository. |
| B2 | Using the STR template from KP(4/4) Section 3.1, complete all sections for `Get-LocalUserAudit.ps1`. Use realistic but fictional values for: Script Code (e.g. `IT-OPS-SCR-002`), Repository URL, Change Request number. |
| B3 | Complete the **Identification** table — all 9 fields must be filled. |
| B4 | Complete the **Target Environment** table. Include OS version, PowerShell version, execution host, target servers, and all required network access (specify ports). |
| B5 | Complete the **Dependencies** table. List every dependency: runtime, modules, service account, configuration files, and infrastructure services. |
| B6 | Complete the **Parameters** table — all 3 parameters with type, required/optional, default, and description. |
| B7 | Complete the **Input/Output** section. Be specific: what does the input file look like? What does the CSV output contain? What does each log entry look like? |
| B8 | Complete the **Error Handling** table — at least 4 failure conditions with their behaviour. |
| B9 | Complete the **Security Considerations** section — at least 4 points specific to this script. |
| B10 | Complete the **Change Log** table (minimum 2 versions — your initial and updated versions from this course). |
| B11 | Commit: `git add docs/STR-Get-LocalUserAudit.md && git commit -m "docs: add Script Technical Reference for Get-LocalUserAudit"` |

---

## Bahagian C — Operational Runbook

### Procedure

| Langkah | Arahan / Instruction |
|---------|---------------------|
| C1 | Create `docs/Runbook-Get-LocalUserAudit.md` in your training repository. |
| C2 | Define the **Alert Condition**: what symptoms indicate the script has failed? (Consider: no CSV report generated by 07:30, log file missing, Task Scheduler showing non-zero last result.) |
| C3 | Write the **Level 1 Initial Response** section with numbered steps an on-call operator can follow without contacting the script author. Include exact commands to check the scheduled task status, inspect the log file, and identify the most common failure modes. |
| C4 | Write the **Escalation** section with the escalation path (Level 1 → Level 2 → Script Owner) and the information the escalating operator must gather before calling the next level. |
| C5 | Write the **Manual Execution** section with the exact PowerShell commands to run the script manually in both normal mode and dry-run (`-WhatIf`) mode. |
| C6 | Write a **Known Issues** section listing at least 2 known limitations or conditions that cause false failures (e.g. server in maintenance window, WMI service restarting). |
| C7 | Commit: `git add docs/Runbook-Get-LocalUserAudit.md && git commit -m "docs: add operational runbook for Get-LocalUserAudit"` |

---

## Bahagian D — CHANGELOG and Version Tagging

### Procedure

| Langkah | Arahan / Instruction |
|---------|---------------------|
| D1 | Create or update `CHANGELOG.md` at the root of your training repository following the Keep a Changelog format from KP(4/4) Section 5.1. |
| D2 | Add entries for all changes made during this course: KK(2/4) initial development, KK(3/4) deployment configuration, KK(4/4) documentation. Use the correct categories: `Added`, `Changed`, `Fixed`. |
| D3 | Tag the current repository state as a release: `git tag -a v1.0.0 -m "Release v1.0.0 — Full documentation package for Get-LocalUserAudit"`. |
| D4 | Verify: `git log --oneline` shows all your commits with meaningful messages; `git tag -l` shows the v1.0.0 tag. |
| D5 | Verify no credentials or production configuration appear in any committed file: `git log --all --full-history -- "**/*.env" "**/*.key" "**/*.secret"` — must return nothing. |

---

## Bahagian E — Handover Package Assembly and Presentation

### Procedure

| Langkah | Arahan / Instruction |
|---------|---------------------|
| E1 | Compile the full handover package. It must contain all 7 items from KP(4/4) Section 6.0: STR, Runbook, CHANGELOG, deployment instructions, test plan, access request record, change request reference. |
| E2 | Write a brief `docs/DEPLOYMENT-INSTRUCTIONS.md` explaining how to deploy `Get-LocalUserAudit.ps1` to a new Windows server (installation steps, service account setup, Task Scheduler registration, verification). |
| E3 | Write a brief `docs/TEST-PLAN.md` with the steps to verify correct operation after deployment (manual run, log inspection, CSV output check, scheduled task verification). |
| E4 | Complete the **Handover Sign-Off table** from KP(4/4) Section 6.0 with the appropriate training roles (Script Author = trainee; Receiving IT Operations Lead = instructor; IT Manager = instructor or training coordinator). |
| E5 | Present the complete documentation package to the instructor in a 10-minute verbal presentation. Walk through each document, explain the purpose of each section, and demonstrate `Get-Help .\Get-LocalUserAudit.ps1` live. |

---

## Hasil Jangkaan / Expected Outcome

A complete, committed documentation package in the training repository containing:
- Fully documented `Get-LocalUserAudit.ps1` with complete inline help
- `docs/STR-Get-LocalUserAudit.md` — all sections complete
- `docs/Runbook-Get-LocalUserAudit.md` — L1/L2/escalation/manual steps
- `docs/DEPLOYMENT-INSTRUCTIONS.md`
- `docs/TEST-PLAN.md`
- `CHANGELOG.md` — all course versions documented
- Git tag `v1.0.0` applied
- Handover sign-off completed

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Inline help: all required sections present and complete | [ ] Yes  [ ] No |
| 2 | `Get-Help` returns correct output without errors | [ ] Yes  [ ] No |
| 3 | In-body comments explain non-obvious logic (WHY, not just WHAT) | [ ] Yes  [ ] No |
| 4 | STR: all 9 Identification fields filled | [ ] Yes  [ ] No |
| 5 | STR: Dependencies table includes all runtime, account, file, and network dependencies | [ ] Yes  [ ] No |
| 6 | STR: Error Handling table has at least 4 conditions | [ ] Yes  [ ] No |
| 7 | Runbook: L1 response uses exact, copy-pasteable commands | [ ] Yes  [ ] No |
| 8 | Runbook: Escalation path clearly defined with information to gather | [ ] Yes  [ ] No |
| 9 | CHANGELOG: all versions documented in Keep a Changelog format | [ ] Yes  [ ] No |
| 10 | Git tag v1.0.0 applied; no sensitive data in commit history | [ ] Yes  [ ] No |
| 11 | Handover package contains all 7 required documents | [ ] Yes  [ ] No |
| 12 | Presentation clear; `Get-Help` demonstrated live | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |