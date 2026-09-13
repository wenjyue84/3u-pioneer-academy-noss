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

## KERTAS TUGASAN

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-5:2013 PENGURUSAN SISTEM KOMPUTER |
| TAHAP | 5 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-E01 SERVER SCRIPTING |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ASSESS SERVER SCRIPTING REQUIREMENT<br>2. DEVELOP SERVER SCRIPT<br>3. EXECUTE AND DEPLOY SERVER SCRIPT<br>4. PREPARE SERVER SCRIPT DOCUMENTATION |
| NO. KOD | IT-020-5:2013-E01/KT(4/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | MERAH JAMBU (Pink) |

**TAJUK:** KT-04-server-script-documentation-assignment

**TUJUAN:** Kertas rujukan untuk KT-04-server-script-documentation-assignment.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Arahan / Instructions

Answer ALL questions. Refer to KP(4/4) for guidance. This assignment is formative.

**Masa / Duration:** 1 hour 30 minutes

---

## Soalan / Questions

### Bahagian A: Soalan Pelbagai Pilihan / Multiple Choice (20 marks)

**A1.** The PowerShell comment-based help section `.PARAMETER ServerName` should contain:

- (a) The data type of the parameter only
- (b) A description of the parameter including type, valid values or range, and default value
- (c) An example of a complete script execution
- (d) The internal variable name used in the script body

**A2.** In Python, a **docstring** (PEP 257) on a function should describe:

- (a) The implementation algorithm in detail
- (b) What the function does, its arguments (with types), return value, and any exceptions it may raise
- (c) The Git commit history for that function
- (d) The author's name only

**A3.** An in-body code comment should explain:

- (a) Every single line of code regardless of complexity
- (b) What the next line of code does in plain English
- (c) WHY a non-obvious approach was chosen, or what constraint the code addresses
- (d) The variable names used in the function

**A4.** The Script Technical Reference (STR) document is intended to be read by:

- (a) Only the original script author
- (b) Any IT professional who needs to understand, maintain, or troubleshoot the script without reading the source code first
- (c) The finance department for cost assessment
- (d) External auditors only

**A5.** An Operational Runbook for a scheduled script is MOST valuable when:

- (a) The script is running normally and no issues have occurred
- (b) An on-call operations engineer receives a failure alert at 3 AM and needs to diagnose and resolve the issue without the original author
- (c) The script author wants to add a new feature
- (d) The IT Manager needs to approve the script for production

**A6.** In the Keep a Changelog format, the `[Unreleased]` section contains:

- (a) Scripts that have been deprecated and removed
- (b) Changes that have been committed but not yet tagged as a release
- (c) Known bugs that have not been fixed
- (d) Scripts that are pending code review

**A7.** Which of the following is MOST important to include in the **Security Considerations** section of a Script Technical Reference?

- (a) The colour scheme of the documentation
- (b) The execution account's privilege level, credential storage method, and execution policy scope
- (c) The name of the project manager
- (d) The number of servers the script targets

**A8.** A **handover package** for a production server script must include a document that explains how a new team member would deploy the script to a new server. This document is the:

- (a) CHANGELOG.md
- (b) Script Technical Reference
- (c) Deployment Instructions
- (d) Operational Runbook

**A9.** The Conventional Commits prefix for a change that restructures script code without changing its functionality is:

- (a) `feat:`
- (b) `fix:`
- (c) `refactor:`
- (d) `docs:`

**A10.** Before completing a handover, which Git command should be run to confirm that no credentials or sensitive files appear in the commit history?

- (a) `git status`
- (b) `git log --all --full-history -- "**/*.env" "**/*.key" "**/*.secret"`
- (c) `git diff HEAD~1`
- (d) `git stash list`

---

### Bahagian B: Soalan Jawapan Pendek / Short Answer (30 marks)

**B1.** Explain FOUR (4) operational risks that arise when a server script is deployed without documentation. For each risk, describe one specific scenario where the lack of documentation caused or would cause a problem. (12 marks)

**B2.** List and briefly describe the SEVEN (7) documents that form a complete handover package for a production server script. For each document, state its primary audience (who reads it and when). (14 marks)

**B3.** What is the difference between an inline code comment and a function docstring? Give one example of each for a Bash function. (4 marks)

---

### Bahagian C: Soalan Esei / Essay (30 marks)

**C1.** Study the following PowerShell comment-based help block. It has FIVE (5) deficiencies. Identify each deficiency, explain why it is a problem, and rewrite the corrected version.

```powershell
<#
.SYNOPSIS
    Restarts services.
.NOTES
    Version: 1
#>
param(
    [string]$ServiceName,
    [string[]]$Computers,
    [int]$TimeoutSeconds = 60
)
```
(15 marks)

**C2.** You have been asked to hand over the `cleanup_tmp.sh` script you developed during this course to the IT Operations team at the end of your project contract. The Operations team has no prior knowledge of the script.

(a) Describe the complete handover process you would follow, including what documents you would prepare, how you would present them, and what sign-off you would obtain. (10 marks)

(b) The Operations Lead says: "We don't need all this documentation — just give us the script file and tell us the cron job syntax." Write a professional response of at least 150 words explaining why complete documentation is essential, using at least TWO (2) specific examples of problems that would arise without it. (5 marks)

---

## Skema Jawapan / Answer Scheme

*To be provided by the instructor after submission.*