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
| NO. KOD | IT-020-5:2013-E01/KT(1/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | MERAH JAMBU (Pink) |

**TAJUK:** KT-01-server-scripting-requirements-assessment-assignment

**TUJUAN:** Kertas rujukan untuk KT-01-server-scripting-requirements-assessment-assignment.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Arahan / Instructions

Answer ALL questions. Refer to KP(1/4) for guidance. Write your answers clearly. This assignment is formative — it prepares you for the Knowledge Assessment (KA).

**Masa / Duration:** 1 hour

---

## Soalan / Questions

### Bahagian A: Soalan Pelbagai Pilihan / Multiple Choice (20 marks)

**A1.** A server script is best described as:

- (a) A web page that runs on a browser
- (b) An automated program that executes on server infrastructure to perform administrative tasks without manual intervention
- (c) A document that describes server hardware specifications
- (d) A network diagram for server topology

**A2.** Which scripting language is the BEST choice for automating tasks on a Windows Server environment that uses Active Directory and Microsoft 365?

- (a) Bash
- (b) Python
- (c) PowerShell
- (d) Ruby

**A3.** The principle of **idempotency** in server scripting means:

- (a) The script runs faster each time it is executed
- (b) Running the script multiple times produces the same result as running it once
- (c) The script can only be run by the Administrator account
- (d) The script generates a different output on each execution

**A4.** Which of the following is a NON-FUNCTIONAL requirement for a server script?

- (a) The script must check disk space on all servers
- (b) The script must send an email when disk usage exceeds 85%
- (c) The script must complete execution within 10 minutes to avoid impacting server load
- (d) The script must accept a list of server names as a parameter

**A5.** In a scripting requirements assessment, the **Constraint Analysis** phase identifies:

- (a) The functional tasks the script must perform
- (b) Limitations such as security policies, network restrictions, and licensing that bound the solution
- (c) The stakeholders who will approve the script
- (d) The error handling strategy

**A6.** The **principle of least privilege** applied to a server script's execution account means:

- (a) The service account should be a local Administrator on all servers
- (b) The service account should have only the minimum permissions required to perform the script's tasks
- (c) The script should run as the SYSTEM account
- (d) No service account is needed if the script is scheduled

**A7.** A scripting requirements assessment identifies a risk that "the script may delete files that are still in use by the application." The BEST mitigation is:

- (a) Run the script during business hours so the team is available to respond
- (b) Skip error handling to speed up execution
- (c) Implement a dry-run mode and verify file lock status before deletion
- (d) Schedule the script to run every minute

**A8.** Which field in a Scripting Requirements Document (SRD) would capture the information: "The script must not run during the monthly batch processing window (last Sunday of each month, 00:00–06:00)"?

- (a) Functional requirements
- (b) Stakeholder identification
- (c) Constraint analysis
- (d) Risk assessment

**A9.** On Linux, Bash is the PREFERRED scripting choice when:

- (a) The task requires complex REST API integration
- (b) The task involves Windows Active Directory administration
- (c) The target environment is Linux-only and the task is file/process management
- (d) The script must produce an Excel report

**A10.** A **Phase 6** output of the scripting requirements assessment is:

- (a) The completed and tested production script
- (b) The Scripting Requirements Document with stakeholder approval signatures
- (c) The scheduled task configuration
- (d) The Git repository containing the script

---

### Bahagian B: Soalan Jawapan Pendek / Short Answer (30 marks)

**B1.** List FOUR (4) common server scripting use cases and provide a one-sentence description of each. (8 marks)

**B2.** Explain the SIX (6) phases of the scripting requirements assessment process. For each phase, state its purpose in one sentence. (12 marks)

**B3.** Compare PowerShell, Bash, and Python scripting for server administration. For each language, state: (a) the primary target OS environment, (b) one key strength, and (c) one limitation. (10 marks)

---

### Bahagian C: Soalan Esei / Essay (30 marks)

**C1.** You are a Level 5 Systems Management Specialist. Your manager presents the following requirement:

> *"We have 30 Windows Server 2022 nodes in our data centre. Every Monday at 4 AM, we need a script to check whether Windows Defender definitions are up to date on each server. If any server has definitions older than 3 days, the script must trigger a forced update remotely and log the result. A summary report must be emailed to the Security Manager by 5 AM."*

(a) Conduct a full requirements assessment for this scenario. Produce:
- A stakeholder table (minimum 3 parties)
- A functional requirements table (minimum 6 rows)
- A non-functional requirements table (minimum 3 rows)
- A risk register (minimum 3 risks with likelihood, impact, and mitigation)
(20 marks)

(b) Select the most appropriate scripting language for this task and provide a written justification of at least 150 words, referencing specific criteria from the decision matrix in KP(1/4). (10 marks)

---

## Skema Jawapan / Answer Scheme

*To be provided by the instructor after submission.*