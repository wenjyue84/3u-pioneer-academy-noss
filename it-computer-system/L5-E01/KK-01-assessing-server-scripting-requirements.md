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
| NO. KOD | IT-020-5:2013-E01/KK(1/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-01-assessing-server-scripting-requirements

**TUJUAN:** Kertas rujukan untuk KK-01-assessing-server-scripting-requirements.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

Conduct a full scripting requirements assessment for the scenario below, select an appropriate scripting language with justification, and produce a completed Scripting Requirements Document (SRD).

---

## Tempoh / Duration

3 hours

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Workstation with internet access | 1 per trainee |
| 2 | Scenario brief (printed — provided by instructor) | 1 |
| 3 | SRD template (printed or digital) | 1 |
| 4 | Requirements assessment checklist | 1 |
| 5 | Scripting language comparison reference sheet | 1 |

---

## Langkah Keselamatan / Safety Precautions

- Do not access or modify any live production server during this assessment exercise
- Use only the designated training environment; do not install software on lab machines without instructor approval
- Handle all scenario documents as confidential; do not photograph or share outside the class

---

## Senario / Scenario

You are a Level 5 Systems Management Specialist at **Prisma Technology Sdn Bhd**. The Head of Infrastructure has raised the following request:

> *"We have 15 Linux servers (Ubuntu 22.04 LTS) running our web application stack. Every night at 11 PM, the application generates large temporary files in `/var/app/tmp/` that must be cleaned up before 1 AM to prevent disk exhaustion. Currently this is done manually by the on-call engineer. We need this automated. The script must log what it deleted and send a summary email to infra@prisma.com if more than 5 GB was cleared. The script must not delete any file created within the last 2 hours."*

---

## Prosedur / Procedures

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 1 | Read the scenario fully. Identify the **stakeholders**: requestor, server owner, end users, and approver. Record each with their role and contact details (invent plausible names for this exercise). |
| 2 | Extract and list all **functional requirements**. Use the table format from KP(1/4) Section 3.0 (Phase 2). Identify: task description, trigger, target systems, input sources, expected output, error handling, and logging requirements. |
| 3 | Identify all **non-functional requirements**: performance constraints (execution window), security requirements, maintainability, and auditability. |
| 4 | Perform **constraint analysis**: what constraints apply given the environment (Ubuntu 22.04, network access to SMTP, file system permissions needed)? |
| 5 | Conduct a **risk assessment**: identify at least THREE (3) risks, their likelihood and impact, and propose mitigations for each. |
| 6 | Select the **scripting language** (PowerShell, Bash, or Python) with a written justification referencing the decision matrix from KP(1/4). |
| 7 | Write a draft **pre-flight checklist** — five specific items the team must verify before deploying the script to production (e.g. permissions, SMTP access, cron user). |
| 8 | Compile all outputs into a completed **Scripting Requirements Document (SRD)** using the template from KP(4/4) Section 3.1. Include the approval section with appropriate roles. |
| 9 | Present your SRD verbally to the instructor (5 minutes). Justify your language selection and the risk mitigation for the most critical risk identified. |

---

## Hasil Jangkaan / Expected Outcome

A completed Scripting Requirements Document containing:
- Stakeholder table (minimum 3 parties)
- Functional requirements table (minimum 7 rows)
- Non-functional requirements table (minimum 4 rows)
- Risk register (minimum 3 risks with mitigations)
- Language selection with written justification (minimum 150 words)
- Pre-flight checklist (minimum 5 items)
- Approval section with named roles

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | All stakeholders identified with roles | [ ] Yes  [ ] No |
| 2 | Functional requirements complete (task, trigger, target, input, output, error, logging) | [ ] Yes  [ ] No |
| 3 | Non-functional requirements documented | [ ] Yes  [ ] No |
| 4 | Constraint analysis addresses the scenario environment | [ ] Yes  [ ] No |
| 5 | Risk register contains at least 3 risks with mitigations | [ ] Yes  [ ] No |
| 6 | Language selection justified with reference to decision matrix | [ ] Yes  [ ] No |
| 7 | Pre-flight checklist specific to this scenario (not generic) | [ ] Yes  [ ] No |
| 8 | SRD formatted correctly using template | [ ] Yes  [ ] No |
| 9 | Verbal presentation clear and technically accurate | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |