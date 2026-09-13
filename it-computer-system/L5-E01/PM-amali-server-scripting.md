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

## PELAN MENGAJAR – AMALI

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-5:2013 PENGURUSAN SISTEM KOMPUTER |
| TAHAP | 5 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-E01 SERVER SCRIPTING |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ASSESS SERVER SCRIPTING REQUIREMENT<br>2. DEVELOP SERVER SCRIPT<br>3. EXECUTE AND DEPLOY SERVER SCRIPT<br>4. PREPARE SERVER SCRIPT DOCUMENTATION |
| NO. KOD | IT-020-5:2013-E01/PM(AMALI) |
| Muka Surat | 1/1 |
| WARNA KERTAS | KUNING (Yellow) |

**TAJUK:** PM-amali-server-scripting

**TUJUAN:** Kertas rujukan untuk PM-amali-server-scripting.

**TEMPAT:** BILIK AMALI / MAKMAL

**TEMPOH:** Rujuk JPW/RK.

**TUJUAN PENGAJARAN:** Pada akhir sesi pengajaran, pelatih akan dapat menguasai pengetahuan/kemahiran berkaitan aktiviti kerja CU ini.

**ALAT BANTUAN MENGAJAR:** Papan putih, projektor, slaid pengajaran, bahan tunjuk-cara.

<!-- /JPK_ENVELOPE_v1 -->
## Agihan Masa Amali / Practical Time Allocation

| KK | Tajuk / Title | Aktiviti Kerja | Jam / Hours |
|----|--------------|----------------|-------------|
| KK(1/4) | Assessing Server Scripting Requirements | WA1: Assess server scripting requirement | 15.4 |
| KK(2/4) | Developing Server Scripts | WA2: Develop server script | 21.0 |
| KK(3/4) | Executing and Deploying Server Scripts | WA3: Execute and deploy server script | 35.0 |
| KK(4/4) | Preparing Server Script Documentation | WA4: Prepare server script documentation | 12.6 |
| **Jumlah / Total** | | | **84.0** |

*Note: 30% theory / 70% practical split applied to 120-hour CU: 36 hours theory, 84 hours practical.*

---

## Kaedah Pengajaran / Teaching Method (4-Step)

### 1. PERSEDIAAN (Preparation)

| Langkah / Step | Aktiviti / Activity | Masa / Duration |
|----------------|---------------------|-----------------|
| 1.1 | Welcome trainees; take attendance; verify workstation access | 5 min |
| 1.2 | State the practical learning objectives for the session | 5 min |
| 1.3 | Review safety rules: no production system access; no credential storage in scripts; test before deploy | 5 min |
| 1.4 | Distribute the KK (Work Sheet) and explain the exercise structure and expected output | 5 min |
| 1.5 | Verify the training server environment is accessible: ping training servers; confirm Git repository access | 5 min |

### 2. PENYAMPAIAN (Demonstration)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 2.1 | Demonstrate the practical task step-by-step as per the KK procedures before trainees begin |
| 2.2 | KK(1/4): Show how to complete an SRD — walk through the template fields with the running scenario |
| 2.3 | KK(2/4): Live code demonstration: write the complete structure of a PowerShell script (param block → logging → error handling → main logic → exit codes). Then do the same in Bash. Leave Python for trainees to attempt independently |
| 2.4 | KK(3/4): Demonstrate: (a) registering a Task Scheduler task with `Register-ScheduledTask`; (b) adding a cron job; (c) verifying via log inspection. Show the failure simulation exercise |
| 2.5 | KK(4/4): Demonstrate: `Get-Help` on a complete script; complete STR template; Runbook Level 1 response section |
| 2.6 | Highlight critical points: `-WhatIf` before destructive operations; always test non-interactively before scheduling; no credentials in Git |
| 2.7 | Answer questions before trainees begin their own work |

### 3. PENGGUNAAN (Practice)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 3.1 | Trainees perform the practical task at their individual workstations following the KK procedures |
| 3.2 | Instructor circulates to observe, guide, and correct technique |
| 3.3 | Brief oral questioning during practice to verify understanding (e.g. "Why did you use `set -euo pipefail` here?") |
| 3.4 | Trainees complete the KK assessment checklist as they work |

### 4. PENGESAHAN (Confirmation)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 4.1 | Instructor checks each trainee's completed work against the KK assessment checklist |
| 4.2 | Verify the expected outcome: script runs correctly; log files present; scheduled task or cron job active; Git commits made with correct messages |
| 4.3 | Provide feedback on process, output, security practice, and documentation quality |
| 4.4 | Trainees clean up the training environment (remove test scheduled tasks/cron entries; delete test files) |
| 4.5 | Record session completion and any issues for follow-up |

---

## Peralatan dan Bahan / Equipment and Materials

| Item | Quantity per Trainee | Notes |
|------|---------------------|-------|
| Workstation with VS Code, PowerShell 7, Git | 1 | Windows 10/11 or Windows Server |
| WSL2 (Ubuntu 22.04) or Linux VM access | 1 | For Bash scripting exercises |
| Training Windows Server 2022 node | 1 (shared pool) | Accessible via RDP or SSH remoting |
| Training Ubuntu 22.04 LTS node | 1 (shared pool) | Accessible via SSH |
| Training Git repository (per trainee) | 1 | Pre-configured with starter stubs |
| SMTP test relay (e.g. Mailtrap) | 1 (shared) | For email sending tests |
| SRD template (printed or digital) | 1 | From KP(4/4) |
| STR template (printed or digital) | 1 | From KP(4/4) |
| Runbook template (printed or digital) | 1 | From KP(4/4) |
| Training service account credentials | 1 set per trainee | Read-only / limited access; rotated per cohort |

---

## Keselamatan / Safety Requirements

- **No production system access:** Trainees must work only within the designated training server environment
- **No credential storage:** All service account passwords must be stored in the Windows Credential Manager or a `.env` file that is explicitly excluded from Git via `.gitignore`
- **Dry-run before live execution:** Every script with file deletion, service modification, or email sending must be tested with dry-run mode BEFORE live execution in the training environment
- **Principle of least privilege:** Training service accounts have the minimum required access. Trainees must not attempt to elevate privileges beyond what is provided
- **Environment cleanup:** All scheduled tasks, cron jobs, and test files created during practicals must be removed at the end of each session

---

## Penilaian Amali / Practical Assessment

Upon completion of all 4 KK sessions, trainees will sit for the Performance Assessment (PA):

- **Code:** IT-020-5:2013-E01/PA
- **Duration:** 8 hours (2 sessions of 4 hours each)
- **Format:** Practical task — full server scripting cycle from requirements assessment to documentation handover
- **Assessment criteria:** Process, Output, Attitude, Safety, Environmental compliance
- **Pass mark:** 60 marks out of 100

---

## Panduan Pensyarah / Instructor Notes

### KK(1/4) — Requirements Assessment (15.4 hours)
- The SRD must be assessed by the instructor before trainees proceed to KK(2/4). This gate prevents poorly defined requirements carrying through to broken scripts.
- Trainees who rush the SRD consistently produce scripts that do not meet the scenario requirements. Enforce the gate.
- Award marks generously for well-structured risk registers — this is a Level 5 competency that demonstrates systems thinking.

### KK(2/4) — Script Development (21.0 hours)
- The PowerShell script (Tugasan 1) should be completed in 3 hours. Trainees who take longer are usually struggling with the comment-based help block — direct them to the KP(2/4) example.
- The Bash script (Tugasan 2) frequently trips trainees on the `mapfile` / `find -mmin` combination. Demonstrate this once on the board before trainees attempt it.
- The Python script (Tugasan 3) is intentionally the most open-ended. Do not over-guide — Level 5 trainees should be comfortable with the Python `subprocess` + `logging` pattern from KP(2/4).
- Check Git commits mid-session: trainees who commit at the end lose context and write poor commit messages. Encourage atomic commits after each working increment.

### KK(3/4) — Execution and Deployment (35.0 hours)
- The largest practical block. Spread across at least 5 sessions.
- The Windows failure simulation (A8 in KK-03) is the most instructive exercise in this CU — watching a script log a meaningful error message versus crash with an unhandled exception makes the error handling lesson concrete.
- Insist on the pre-deployment checklist sign-off before any deployment. This habit must be formed here, not in production.
- The cron vs systemd comparison (B10 in KK-03) should produce a written record of at least 3 differences. Review these as a class discussion.

### KK(4/4) — Documentation (12.6 hours)
- The handover presentation (E5 in KK-04) should be treated seriously — use it as a mock PA rehearsal.
- Common gap: trainees write STR Identification tables but skip the Security Considerations section. This section is directly assessed in both KA and PA.
- The CHANGELOG.md exercise reinforces Git discipline. Verify that trainee CHANGELOG entries match their actual Git commits.