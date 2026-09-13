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

## KERTAS PENILAIAN PRESTASI

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-5:2013 PENGURUSAN SISTEM KOMPUTER |
| TAHAP | 5 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-E01 SERVER SCRIPTING |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ASSESS SERVER SCRIPTING REQUIREMENT<br>2. DEVELOP SERVER SCRIPT<br>3. EXECUTE AND DEPLOY SERVER SCRIPT<br>4. PREPARE SERVER SCRIPT DOCUMENTATION |
| NO. KOD | IT-020-5:2013-E01/PA |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU MUDA (Light Blue) |

**TAJUK:** PA-server-scripting

**TUJUAN:** Kertas rujukan untuk PA-server-scripting.

**ARAHAN:** Jawab semua soalan / laksanakan semua tugas penilaian. Penilaian ini adalah sebahagian daripada Penilaian Akhir CU.

<!-- /JPK_ENVELOPE_v1 -->
## Arahan kepada Pelatih / Instructions to Trainee

1. This is a PRACTICAL examination. You will be assessed on your ability to complete a full server scripting cycle: requirements assessment, script development, deployment, and documentation.
2. You will receive a scenario brief. You must complete all four work activities within the allocated time.
3. You will be assessed on: **Process** (how you work), **Output** (what you produce), **Attitude** (professionalism), **Safety** (data and system security), and **Environmental** compliance (documentation quality and workspace standards).
4. All work must be performed in the designated training environment. Do NOT use production systems.
5. All scripts must be committed to the training Git repository before submission.

---

## Arahan kepada Penilai / Instructions to Assessor

- Provide each trainee with a workstation, access to the training server environment, and the printed scenario brief.
- Observe each trainee throughout the assessment. Do NOT provide technical assistance.
- Mark each criterion on the rubric as the trainee works and at submission.
- Verify all output artefacts (scripts, documentation, Git repository, scheduled task/cron) at the end.
- The assessment runs over two sessions as indicated in the scenario.

---

## Tugasan / Task Description

### Scenario: PA-2026-E01

You are a Level 5 Systems Management Specialist at **Teknikal Maju Sdn Bhd**. The Head of IT Infrastructure has issued the following requirement:

> *"We have 5 Windows Server 2022 nodes and 3 Ubuntu 22.04 LTS servers. We need an automated script to monitor available disk space daily. For Windows: if any drive on any server exceeds 80% utilisation, write a warning entry to a log file and send an HTML summary email. For Linux: if any filesystem exceeds 75% utilisation, append a warning to a syslog-format log file. Both scripts must run at 06:00 daily. All scripts must be deployed to the appropriate servers, scheduled, tested, documented, and handed over to the Operations team."*

**Assessment sessions:**

| Session | Duration | Activities |
|---------|----------|------------|
| Session 1 | 4 hours | WA1 (Requirements Assessment) + WA2 (Script Development) |
| Session 2 | 4 hours | WA3 (Deployment + Scheduling + Verification) + WA4 (Documentation + Handover) |

**Total assessment time: 8 hours**

---

### WA1 Task: Requirements Assessment (Session 1, first 1.5 hours)

1. Read the scenario brief in full.
2. Produce a completed Scripting Requirements Document (SRD) covering:
   - Stakeholder table (minimum 3 parties)
   - Functional requirements table (Windows and Linux components)
   - Non-functional requirements table
   - Risk register (minimum 3 risks with mitigations)
   - Language selection with written justification
   - Pre-deployment checklist (minimum 5 items)
3. Submit SRD to assessor for review before proceeding to WA2.

### WA2 Task: Script Development (Session 1, remaining 2.5 hours)

Develop the following scripts and commit them to the training Git repository:

**Script 1 — PowerShell (`Check-DiskSpace-PA.ps1`):**
- Parameters: `ComputerList` (string array), `Threshold` (int, default 80), `SmtpServer` (string), `ReportRecipient` (string)
- Query disk space on each Windows server using CIM
- Log warning entries to `C:\Logs\DiskCheck_YYYYMMDD.log`
- Send HTML email if any drive is flagged
- Handle unreachable servers gracefully; return exit code 0/3/1
- Complete comment-based help block required

**Script 2 — Bash (`check_disk.sh`):**
- Arguments: `THRESHOLD` (default 75), `LOG_FILE`
- Query local disk using `df`
- Append syslog-format entries for flagged filesystems
- Use `set -euo pipefail`; implement `log()` and `die()` functions
- Return exit code 0/1

Both scripts must demonstrate:
- Input validation
- Structured logging with timestamps
- Error handling that does not crash the script on individual failures
- Dry-run mode (PowerShell: `-WhatIf`; Bash: `--dry-run` flag or `DRY_RUN=1` environment variable)
- Committed to Git with meaningful commit message

### WA3 Task: Execution and Deployment (Session 2, first 3 hours)

1. Complete the pre-deployment checklist for both scripts.
2. Deploy `Check-DiskSpace-PA.ps1` to the Windows training server. Register a scheduled task to run daily at 06:00 as the training service account.
3. Deploy `check_disk.sh` to the Linux training server. Add a cron job for the service account to run at 06:00 daily.
4. Manually trigger both scheduled jobs. Verify:
   - PowerShell: `LastTaskResult = 0`; log file present and contains correct entries
   - Bash: Cron test execution completes; log file present
5. Simulate a failure on one server (disconnect one training node). Re-run the PowerShell script. Verify the unreachable server is logged as `UNREACHABLE` and the script still exits with code 3 (not crashes).
6. Demonstrate rollback for the PowerShell script: disable the task, restore a previous Git commit, redeploy, re-enable.

### WA4 Task: Documentation and Handover (Session 2, remaining 1 hour)

Produce and submit:
1. Script Technical Reference (STR) for `Check-DiskSpace-PA.ps1` — all sections complete
2. Operational Runbook for `Check-DiskSpace-PA.ps1` — L1 response with exact commands
3. `CHANGELOG.md` entry covering both scripts
4. Git tag `v1.0.0` applied
5. Verbal handover presentation (5 minutes): walk through the SRD, scripts, scheduled tasks, and STR. Demonstrate `Get-Help .\Check-DiskSpace-PA.ps1`.

---

## Rubrik Penilaian / Assessment Rubric

### A. PROSES (Process) — 30 marks

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| A1 | WA1: SRD produced with all required sections before beginning development | 5 | |
| A2 | WA2: Script structure follows canonical pattern (param block, logging function, error handling, exit codes) | 5 | |
| A3 | WA2: Dry-run mode implemented and tested before live execution | 5 | |
| A4 | WA3: Pre-deployment checklist completed and submitted before deploying to training server | 5 | |
| A5 | WA3: Scheduled tasks configured correctly with service account (not personal account) | 5 | |
| A6 | WA4: Documentation and handover completed within allotted time; verbal presentation delivered | 5 | |
| | **Subtotal Process** | **30** | |

### B. HASIL (Output) — 30 marks

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| B1 | PowerShell script: all parameters, logging, error handling, and exit codes function correctly | 6 | |
| B2 | Bash script: `set -euo pipefail`, `log()`, `die()`, correct df parsing, and exit codes function correctly | 6 | |
| B3 | Both scripts committed to Git with meaningful commit messages; no credentials in repository | 5 | |
| B4 | Scheduled task (Windows) and cron job (Linux) verified running; correct exit codes confirmed | 5 | |
| B5 | Failure simulation: unreachable server handled gracefully; exit code 3 confirmed | 4 | |
| B6 | STR and Runbook complete; Git tag v1.0.0 applied | 4 | |
| | **Subtotal Output** | **30** | |

### C. SIKAP (Attitude) — 15 marks

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| C1 | Works independently and methodically; does not seek unnecessary assistance | 5 | |
| C2 | Follows a logical sequence (requirements → development → test → deploy → document) without prompting | 5 | |
| C3 | Verbal presentation is clear, technically accurate, and covers all required artefacts | 5 | |
| | **Subtotal Attitude** | **15** | |

### D. KESELAMATAN (Safety) — 15 marks

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| D1 | No credentials (passwords, keys) stored in scripts or committed to Git at any point | 5 | |
| D2 | Scripts tested with dry-run before live execution; no accidental data deletion or modification | 5 | |
| D3 | Principle of least privilege applied: service account has only the minimum access needed | 5 | |
| | **Subtotal Safety** | **15** | |

### E. ALAM SEKITAR (Environmental) — 10 marks

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| E1 | Training environment left in clean state (scheduled tasks removed or disabled; test files cleaned up) at end of assessment | 5 | |
| E2 | All documentation is clearly written, professionally formatted, and usable by a third party without clarification | 5 | |
| | **Subtotal Environmental** | **10** | |

---

## Ringkasan Markah / Score Summary

| Section | Maximum | Score |
|---------|---------|-------|
| A. Process | 30 | |
| B. Output | 30 | |
| C. Attitude | 15 | |
| D. Safety | 15 | |
| E. Environmental | 10 | |
| **TOTAL** | **100** | |

---

## Keputusan / Result

| | |
|---|---|
| **Lulus / Pass** (≥ 60 marks) | [ ] |
| **Gagal / Fail** (< 60 marks) | [ ] |

---

## Pengesahan / Verification

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Assessor 1 | | | |
| Assessor 2 (if applicable) | | | |
| Internal Verifier | | | |

---

## Ulasan / Comments

*(Assessor to provide feedback on strengths, areas for improvement, and any critical non-compliance observed — especially regarding credential security and dry-run testing.)*

|  |
|---|
|  |
|  |
|  |
|  |