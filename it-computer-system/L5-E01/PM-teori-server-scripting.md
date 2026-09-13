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

## PELAN MENGAJAR – TEORI

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-5:2013 PENGURUSAN SISTEM KOMPUTER |
| TAHAP | 5 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-E01 SERVER SCRIPTING |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ASSESS SERVER SCRIPTING REQUIREMENT<br>2. DEVELOP SERVER SCRIPT<br>3. EXECUTE AND DEPLOY SERVER SCRIPT<br>4. PREPARE SERVER SCRIPT DOCUMENTATION |
| NO. KOD | IT-020-5:2013-E01/PM(TEORI) |
| Muka Surat | 1/1 |
| WARNA KERTAS | KUNING (Yellow) |

**TAJUK:** PM-teori-server-scripting

**TUJUAN:** Kertas rujukan untuk PM-teori-server-scripting.

**TEMPAT:** BILIK KULIAH

**TEMPOH:** Rujuk JPW/RK.

**TUJUAN PENGAJARAN:** Pada akhir sesi pengajaran, pelatih akan dapat menguasai pengetahuan/kemahiran berkaitan aktiviti kerja CU ini.

**ALAT BANTUAN MENGAJAR:** Papan putih, projektor, slaid pengajaran, bahan tunjuk-cara.

<!-- /JPK_ENVELOPE_v1 -->
## Agihan Masa Teori / Theory Time Allocation

| KP | Tajuk / Title | Aktiviti Kerja | Jam / Hours |
|----|--------------|----------------|-------------|
| KP(1/4) | Server Scripting Requirements Assessment | WA1: Assess server scripting requirement | 6.6 |
| KP(2/4) | Server Script Development | WA2: Develop server script | 9.0 |
| KP(3/4) | Server Script Execution and Deployment | WA3: Execute and deploy server script | 15.0 |
| KP(4/4) | Server Script Documentation | WA4: Prepare server script documentation | 5.4 |
| **Jumlah / Total** | | | **36.0** |

*Note: 30% theory / 70% practical split applied to 120-hour CU: 36 hours theory, 84 hours practical.*

---

## Kaedah Pengajaran / Teaching Method (4-Step)

### 1. PERSEDIAAN (Preparation)

| Langkah / Step | Aktiviti / Activity | Masa / Duration |
|----------------|---------------------|-----------------|
| 1.1 | Welcome trainees and take attendance | 5 min |
| 1.2 | State the learning objectives for the session; link to the relevant KP | 5 min |
| 1.3 | Relate the topic to workplace context — ask trainees about manual server tasks they have done | 10 min |
| 1.4 | Brief overview of today's KP content structure | 5 min |

### 2. PENYAMPAIAN (Presentation)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 2.1 | Deliver theory content from the relevant KP using slides and live terminal demonstrations |
| 2.2 | For KP(1/4): Walk through the 6-phase requirements assessment using a relatable workplace scenario. Show how a poorly defined requirement leads to a wrong script |
| 2.3 | For KP(2/4): Live code demonstration — write a short PowerShell, Bash, and Python script live in the terminal. Show the difference between a poorly structured script and a production-quality one |
| 2.4 | For KP(3/4): Demonstrate Task Scheduler and cron configuration live. Show what happens when a scheduled script fails silently versus one with logging |
| 2.5 | For KP(4/4): Show `Get-Help` in action on a well-documented vs poorly documented script. Demonstrate the difference to trainees |
| 2.6 | Highlight security considerations throughout: credential storage, execution policy, least privilege |
| 2.7 | Encourage questions and clarify misunderstandings immediately |

### 3. PENGGUNAAN (Application)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 3.1 | Distribute the corresponding KT (Assignment Sheet) for the session |
| 3.2 | Trainees complete the assignment individually |
| 3.3 | Instructor circulates to observe progress and provide targeted guidance |
| 3.4 | Discuss answers and common errors with the whole class after submission |

### 4. PENGESAHAN (Confirmation)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 4.1 | Review key learning points from the session |
| 4.2 | Conduct brief oral questioning: call on 3–4 trainees to answer concept questions |
| 4.3 | Collect completed KT for marking and feedback |
| 4.4 | Preview the next session topic |
| 4.5 | Record attendance and session completion |

---

## Sumber Pengajaran / Teaching Resources

| Sumber / Resource | Keterangan / Description |
|-------------------|--------------------------|
| KP(1/4) to KP(4/4) | Information Sheets for all 4 Work Activities |
| KT(1/4) to KT(4/4) | Assignment Sheets for all 4 Work Activities |
| Slide presentation | PowerPoint covering each KP topic; include live script examples |
| Whiteboard/projector | For architecture diagrams, cron syntax tables, deployment pipelines |
| Demo workstation | Windows Server 2022 VM + Ubuntu 22.04 VM for live terminal demonstrations |
| VS Code | Installed on demo workstation with PowerShell and Python extensions |
| Git repository | Training repository pre-configured with starter script stubs |
| NOSS document | IT-020-5:2013 CoCU E01 reference |

---

## Panduan Pensyarah / Instructor Notes

### KP(1/4) — Requirements Assessment (6.6 hours)
- Begin with a 5-minute demo: show a production server script that is completely undocumented with no requirements background. Ask trainees: "Would you deploy this? Why not?" This motivates the requirements phase.
- Use the "disk space monitoring" scenario throughout as the running example — it is concrete, universally understood, and used in subsequent KPs.
- Emphasise: the requirements phase catches wrong language selection BEFORE hours are spent coding. A common Level 5 error is jumping to scripting without assessing the environment.

### KP(2/4) — Script Development (9.0 hours)
- Live coding is essential for this KP. Do not just show finished scripts — write from scratch so trainees see the thought process.
- Common trainee errors to address proactively:
  - `$array += $item` in loops (O(n²) problem)
  - Hardcoded credentials
  - Missing `set -euo pipefail` in Bash
  - No exit codes — scripts that silently succeed or fail
- The three script examples in KP(2/4) are complete, working, production-quality examples. Use them as the benchmark.

### KP(3/4) — Execution and Deployment (15.0 hours)
- The most common exam failure: trainees know how to write scripts but do not understand why interactive scripts fail when scheduled. Spend time on the environment differences table.
- Cron vs systemd: both are examinable. Do not skip systemd — it is the modern standard on RHEL 8+/Ubuntu 20.04+.
- The deployment pipeline (DEV → UAT → PROD) must be emphasised. Trainees must internalise that you never skip UAT.

### KP(4/4) — Documentation (5.4 hours)
- Show `Get-Help` on a well-documented script. Then show `Get-Help` on a script with no comment-based help. The contrast is immediately compelling.
- The Operational Runbook exercise should use a realistic 3 AM failure scenario to make the stakes concrete.
- Documentation is frequently undervalued by trainees. Use the KP(4/4) risk table to demonstrate real consequences.

---

## Penilaian Teori / Theory Assessment

Upon completion of all 4 KP/KT sessions, trainees will sit for the Knowledge Assessment (KA):

- **Code:** IT-020-5:2013-E01/KA
- **Duration:** 2 hours
- **Format:** Written (MCQ + short answer + essay)
- **Pass mark:** 60% (60 marks out of 100)
- **Coverage:** All 4 Work Activities equally weighted