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
| KOD DAN NAMA PROGRAM | IT-020-4:2013 PENTADBIRAN SISTEM KOMPUTER |
| TAHAP | 4 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C01 SERVER CONFIGURATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE SERVER CONFIGURATION REQUIREMENTS<br>2. PLAN SERVER ROLES AND SERVICES<br>3. CONFIGURE SERVER HARDWARE AND STORAGE<br>4. CONFIGURE SERVER OS AND ROLES<br>5. IMPLEMENT SERVER SECURITY SETTINGS<br>6. DOCUMENT SERVER CONFIGURATION |
| NO. KOD | IT-020-4:2013-C01/KK(6/6) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-06-documenting-server-configuration

**TUJUAN:** Kertas rujukan untuk KK-06-documenting-server-configuration.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

Produce a complete, accurate, and professionally formatted Server Configuration Record and As-Built Document for the server configured in KK-03 through KK-05, and conduct a formal handover walkthrough with the instructor acting as the operations team lead.

---

## Tempoh / Duration

2 hours (practical session)

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Configured server (from KK-03 to KK-05) | 1 |
| 2 | Server Configuration Record template (from KP-06) | 1 |
| 3 | As-Built Document template | 1 |
| 4 | Handover checklist (from KP-06 Section 7.0) | 1 |
| 5 | Computer with word processor | 1 |
| 6 | All worksheets and command outputs from KK-03, KK-04, KK-05 | Previous sessions |

---

## Langkah Keselamatan / Safety Precautions

- Document actual configuration values — do not copy from the plan without verifying against the live server
- Do not include plaintext passwords in documentation — use masked values (e.g. `***`) or a reference to the secure credential store
- Classify the document as "CONFIDENTIAL — Internal IT Use Only" given that it contains IP addresses, account names, and security configuration details

---

## Prosedur / Procedures

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 1 | **Gather live configuration data:** On the server, run and save the output of the following commands to a text file named `server-audit-[hostname]-[date].txt`: `systeminfo`, `ipconfig /all`, `Get-WindowsFeature | Where Installed`, `Get-NetFirewallProfile`, `auditpol /get /category:*`, `Get-BitLockerVolume`, `Get-DhcpServerv4ScopeStatistics`, `dcdiag /v`, `Get-ADDomainController -Filter *`. This file is the raw evidence base for the documentation. |
| 2 | **Complete Section 1 — Server Identity:** Using the server audit file and the physical server label, fill in all fields of Section 1 of the Server Configuration Record: hostname, FQDN, roles, physical location, asset tag, serial number, purchase date, warranty expiry, and responsible administrator. |
| 3 | **Complete Section 2 — Hardware Configuration:** From the iDRAC hardware inventory and the RAID Configuration Worksheet (KK-03), complete all hardware fields: make/model, CPU, RAM, storage controller, physical disks, RAID configuration, NICs, PSU, and management interface. |
| 4 | **Complete Section 3 — Network Configuration:** From `ipconfig /all` and the IP assignment sheet, fill the network table: interface, IP address, subnet, gateway, VLAN, and purpose. Include the iDRAC management interface. |
| 5 | **Complete Sections 4–6 — OS, Roles, and Security:** From the audit file, complete OS version, build number, activation method, timezone, NTP, and update server. List all installed roles and features with configuration notes. Complete the security section: firewall status, BitLocker status, audit policy, password policy, account rename status. |
| 6 | **Complete Section 7 — Backup Configuration:** Record the backup software, schedule, retention policy, backup target, last successful backup time, and date of last recovery test. If backup has not been tested, note it as a known outstanding item. |
| 7 | **Produce the As-Built Document:** Copy the completed Server Configuration Record as the base. Add: (a) Deviations from the Server Role Plan — list any differences and justification; (b) Acceptance Test Results — list each test from the verification steps (KK-04 and KK-05) with Pass/Fail result; (c) Known Issues / Limitations — document any outstanding items not resolved at handover. |
| 8 | **Apply version control:** Set the document version to v1.0. Add the document header (Title, Owner, Version, Last Updated, Last Updated By, Review Date). Save as `SRV-DC01-Configuration-Record-v1.0-[date].docx`. |
| 9 | **Conduct handover walkthrough:** Present the As-Built Document to the instructor (acting as Operations Team Lead). Walk through: (a) what the server does and which roles it hosts; (b) how to access it (RDP, WinRM, iDRAC); (c) where the backup is stored and how to verify it; (d) what the known issues are and who is resolving them; (e) where the documentation is stored. Answer the instructor's questions. |
| 10 | **Complete the Handover Checklist** from KP-06 Section 7.0. Both trainee and instructor sign the handover sign-off table. Submit all documents. |

---

## Hasil Dijangka / Expected Outcome

- Server Configuration Record: all 7 sections complete with actual (not planned) values, no blank fields
- As-Built Document: includes deviations, acceptance test results, and known issues
- Document version v1.0 with correct header and versioned filename
- Handover walkthrough conducted; instructor satisfied that the operations team has sufficient information to manage the server
- Handover checklist signed by both trainee and instructor

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Server audit command outputs collected and saved to evidence file | [ ] Yes  [ ] No |
| 2 | All 7 sections of Server Configuration Record completed with actual values | [ ] Yes  [ ] No |
| 3 | No blank fields — all unknowns explicitly noted as "N/A" or "Pending — [reason]" | [ ] Yes  [ ] No |
| 4 | No plaintext passwords in documentation | [ ] Yes  [ ] No |
| 5 | As-Built Document includes deviations section | [ ] Yes  [ ] No |
| 6 | Acceptance test results table included with Pass/Fail for each test | [ ] Yes  [ ] No |
| 7 | Known issues / limitations explicitly stated | [ ] Yes  [ ] No |
| 8 | Document classified as CONFIDENTIAL; version header correct | [ ] Yes  [ ] No |
| 9 | Handover walkthrough conducted; all questions answered satisfactorily | [ ] Yes  [ ] No |
| 10 | Handover checklist signed by trainee and instructor | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |