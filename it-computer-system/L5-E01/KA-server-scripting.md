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

## KERTAS PENILAIAN PENGETAHUAN

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-5:2013 PENGURUSAN SISTEM KOMPUTER |
| TAHAP | 5 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-E01 SERVER SCRIPTING |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ASSESS SERVER SCRIPTING REQUIREMENT<br>2. DEVELOP SERVER SCRIPT<br>3. EXECUTE AND DEPLOY SERVER SCRIPT<br>4. PREPARE SERVER SCRIPT DOCUMENTATION |
| NO. KOD | IT-020-5:2013-E01/KA |
| Muka Surat | 1/1 |
| WARNA KERTAS | MERAH JAMBU (Pink) |

**TAJUK:** KA-server-scripting

**TUJUAN:** Kertas rujukan untuk KA-server-scripting.

**ARAHAN:** Jawab semua soalan / laksanakan semua tugas penilaian. Penilaian ini adalah sebahagian daripada Penilaian Akhir CU.

<!-- /JPK_ENVELOPE_v1 -->
## Arahan kepada Pelatih / Instructions to Trainee

1. This paper consists of THREE (3) sections: A, B, and C.
2. Answer ALL questions in ALL sections.
3. Write your answers clearly in the answer booklet provided.
4. This is a CLOSED BOOK examination. No reference materials are permitted.
5. Duration: **2 hours**.
6. Passing mark: **60%** (60 marks out of 100).

---

## Arahan kepada Pengajar / Instructions to Instructor

- Distribute the question paper and answer booklet to each trainee.
- Allow exactly **2 hours** for the examination.
- Collect all papers at the end of the allocated time.
- Mark using the answer scheme provided (separate instructor document).

---

## BAHAGIAN A: SOALAN PELBAGAI PILIHAN / SECTION A: MULTIPLE CHOICE (30 marks)

Answer all 15 questions. Each question carries 2 marks. Circle the correct answer.

**1.** Which of the following BEST defines the purpose of server scripting at Level 5 Systems Management?

- (a) Creating websites that run on a web server
- (b) Automating administrative, configuration, monitoring, and deployment tasks on server infrastructure
- (c) Writing firmware for server hardware components
- (d) Configuring server BIOS settings via scripts

**2.** The scripting requirements assessment phase called "Stakeholder Identification" is performed:

- (a) After the script has been fully developed and tested
- (b) As the FIRST phase, before any technical requirements are gathered
- (c) Only when the script will run in a production environment
- (d) Only for scripts that send email notifications

**3.** A server script that "produces the same result whether run once or ten times" is described as:

- (a) Recursive
- (b) Modular
- (c) Idempotent
- (d) Parameterised

**4.** In PowerShell, `[CmdletBinding(SupportsShouldProcess)]` combined with `$PSCmdlet.ShouldProcess(...)` enables:

- (a) Parallel execution across multiple servers
- (b) The `-WhatIf` dry-run flag, allowing the script to describe its actions without executing them
- (c) Automatic logging to the Windows Event Log
- (d) Remote execution via WinRM

**5.** The Bash directive `IFS=$'\n\t'` is set at the start of a script to:

- (a) Define the script's encoding as UTF-8
- (b) Set the Internal Field Separator to newline and tab, preventing word-splitting errors on filenames with spaces
- (c) Enable tab completion in the script
- (d) Import external shell functions

**6.** A Python script's `logging` module is configured with a file handler at `DEBUG` level and a console handler at `INFO` level. Which messages appear ONLY in the log file and NOT on the console?

- (a) INFO and above
- (b) WARNING and above
- (c) DEBUG messages only
- (d) ERROR and CRITICAL only

**7.** The cron expression `*/15 * * * *` executes the command:

- (a) At 15 minutes past every hour
- (b) Every 15 minutes
- (c) At 00:15, 01:15, 02:15... (once per hour, 15 minutes past)
- (d) On the 15th of every month

**8.** In Windows Task Scheduler, setting `RestartCount=3` and `RestartInterval=PT5M` means:

- (a) The task runs 3 times per day with 5-minute intervals
- (b) If the task fails, it will retry up to 3 times with a 5-minute wait between each attempt
- (c) The task will stop after 3 successful runs
- (d) The task is paused for 5 minutes before each of its 3 daily runs

**9.** Which environment in a deployment pipeline is used for testing scripts on infrastructure representative of production BEFORE they are deployed to live servers?

- (a) Development (DEV)
- (b) Disaster Recovery (DR)
- (c) User Acceptance Testing (UAT)
- (d) Sandbox

**10.** A script exits with code **1**. According to the exit code convention from this CU, this indicates:

- (a) Success
- (b) Partial success — some operations failed
- (c) Invalid arguments
- (d) General error — a fatal condition occurred

**11.** The PowerShell comment-based help section that describes what objects a script writes to the pipeline or to output files is:

- (a) `.DESCRIPTION`
- (b) `.OUTPUTS`
- (c) `.NOTES`
- (d) `.RETURNVALUE`

**12.** An Operational Runbook for a server script is PRIMARILY used by:

- (a) The original script developer during initial coding
- (b) The finance team for budget approval
- (c) On-call operations staff to respond to failures without contacting the script author
- (d) External auditors reviewing security compliance

**13.** The `git tag -a v1.2.0 -m "Release message"` command creates:

- (a) A new branch named v1.2.0
- (b) An annotated Git tag marking the current commit as version 1.2.0 with a message
- (c) A new commit with the message "Release message"
- (d) A lightweight tag without a message

**14.** In the Keep a Changelog format, changes that have been committed to the repository but not yet assigned to a release version are listed under:

- (a) `## [Latest]`
- (b) `## [Pending]`
- (c) `## [Unreleased]`
- (d) `## [Draft]`

**15.** Which of the following represents a CRITICAL security failure in a production server script?

- (a) The script uses verbose logging
- (b) The script's Git repository contains a `.env` file with database credentials committed to the main branch
- (c) The script exits with code 3 when some servers are unreachable
- (d) The script uses a generic List instead of array concatenation

---

## BAHAGIAN B: SOALAN JAWAPAN PENDEK / SECTION B: SHORT ANSWER (30 marks)

Answer all 6 questions.

**16.** List FOUR (4) categories of server scripting use cases and provide one concrete example for each. (8 marks)

**17.** Explain the SIX (6) phases of a scripting requirements assessment. For each phase, state what is produced as an output. (12 marks)

**18.** State the purpose of each of the following Bash directives: (a) `set -e`, (b) `set -u`, (c) `set -o pipefail`. Then explain why all three are typically combined as `set -euo pipefail` in production scripts. (5 marks)

**19.** Name FIVE (5) items that must appear in a complete handover package for a production server script, and state the primary audience for each. (5 marks)

---

## BAHAGIAN C: SOALAN ESEI / SECTION C: ESSAY (40 marks)

Answer all 2 questions.

**20.** You are a Level 5 Systems Management Specialist at a company managing a hybrid infrastructure of 10 Windows Server 2022 nodes and 8 Ubuntu 22.04 LTS servers.

The Security Manager has requested the following automation:

> *"Every Sunday at 2 AM, generate a security audit report for all servers. For Windows servers: collect all local Administrator group members and all accounts with 'Password Never Expires' set. For Linux servers: collect all users in the `sudo` group and all accounts with UID 0. Compile the results into a single JSON report and email it to the Security Manager."*

(a) Conduct a scripting requirements assessment for this scenario. Produce:
- Stakeholder table (minimum 3 parties)
- Functional requirements table (minimum 8 rows)
- Non-functional requirements table (minimum 4 rows)
- Risk register (minimum 4 risks with likelihood, impact, and mitigation)
(15 marks)

(b) Select the scripting approach (single language or combination) and justify your choice in at least 200 words. Explain how you would handle the Windows and Linux components, how results would be consolidated, and how the JSON report would be structured. (10 marks)

(c) Describe the complete deployment procedure for this script set, from development through to production scheduling. Include: deployment environments, pre-deployment checklist items specific to this scenario, scheduling approach for both Windows and Linux components, and verification steps. (8 marks)

(d) Write the complete Script Technical Reference (STR) Identification table and the Security Considerations section for ONE of the scripts in this solution. (7 marks)

**21.** A junior administrator has submitted the following Bash script for deployment to production. Review the script and perform a FULL code review.

```bash
#!/bin/bash
PASSWORD="admin123"
BACKUP_DIR=/home/admin/backups

backup_database() {
    mysqldump -u root -p$PASSWORD myapp_db > $BACKUP_DIR/backup_$(date).sql
    echo "Backup done"
}

cleanup() {
    rm -rf $BACKUP_DIR/*
    echo "Cleaned up"
}

backup_database
cleanup
```

(a) Identify ALL problems in this script. For each problem: state the problem, explain the consequence in a production environment, and provide the corrected code. You should find at least SIX (6) distinct problems. (20 marks)

(b) After correcting all problems, what additional documentation must accompany this script before it can be deployed to production? List the documents required and state what specific content each must contain for this particular script. (10 marks) *(Note: 10 marks allocated; total for Q21 = 30 marks — combined with 10 marks from Section B Q19-20 overflow. Adjust per institutional marking scheme.)*

---

## TAMAT / END OF PAPER

---

*Answer scheme is provided as a separate instructor document.*