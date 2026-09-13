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
| KOD DAN NAMA PROGRAM | IT-020-4:2013 PENTADBIRAN SISTEM KOMPUTER |
| TAHAP | 4 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C01 SERVER CONFIGURATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE SERVER CONFIGURATION REQUIREMENTS<br>2. PLAN SERVER ROLES AND SERVICES<br>3. CONFIGURE SERVER HARDWARE AND STORAGE<br>4. CONFIGURE SERVER OS AND ROLES<br>5. IMPLEMENT SERVER SECURITY SETTINGS<br>6. DOCUMENT SERVER CONFIGURATION |
| NO. KOD | IT-020-4:2013-C01/KT(6/6) |
| Muka Surat | 1/1 |
| WARNA KERTAS | MERAH JAMBU (Pink) |

**TAJUK:** KT-06-server-documentation-assignment

**TUJUAN:** Kertas rujukan untuk KT-06-server-documentation-assignment.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Arahan / Instructions

Answer ALL questions. Refer to KP(6/6) for guidance. Write clearly on a separate answer sheet.

**Masa / Duration:** 45 minutes

---

## Tugasan / Questions

### Bahagian A: Soalan Pelbagai Pilihan / Multiple Choice (20 marks — 4 marks each)

**A1.** The primary difference between a Server Configuration Record and an As-Built Document is:

- (a) The Configuration Record is written in Malay; the As-Built is in English
- (b) The As-Built Document reflects the ACTUAL final deployed state including deviations from the plan, while the Configuration Record may be based on the design plan
- (c) The Configuration Record is for management; the As-Built is for technicians only
- (d) There is no difference — they are the same document with different names

**A2.** A change log entry is described as "append-only" because:

- (a) New entries are added to the end; existing entries must never be modified or deleted
- (b) Only the most recent change is kept; older entries are deleted
- (c) The file can only be opened for reading, never for writing
- (d) Changes are logged automatically by the operating system without human input

**A3.** Which document describes step-by-step procedures for routine operations such as backup restore or server failover?

- (a) Requirements Traceability Matrix
- (b) As-Built Document
- (c) Runbook / Standard Operating Procedure (SOP)
- (d) Server Role Plan

**A4.** After a hardware replacement (e.g. motherboard swap) on a server running BitLocker, the most critical documentation action is:

- (a) Update the change log with the new serial number
- (b) Record the new BitLocker recovery key location — the old TPM binding is broken and a new key will be required
- (c) Update the IP address in the Server Configuration Record
- (d) Delete the old As-Built Document and create a new one from scratch

**A5.** Documentation should be stored in a team-accessible, backed-up location rather than a personal folder because:

- (a) Personal folders are not permitted by Microsoft licence agreements
- (b) If the documenting administrator leaves or is unavailable, the operations team must be able to access the documentation to manage the server
- (c) Server documentation files are too large for personal folders
- (d) Personal folders are not indexed by Windows Search

---

### Bahagian B: Soalan Jawapan Pendek / Short Answer (30 marks)

**B1.** List SIX (6) types of server documentation (from KP-06 Section 2.0) and state the primary purpose and primary audience for each. (18 marks)

**B2.** Explain why "documenting from memory weeks after deployment" is considered a professional error. State TWO (2) specific consequences of this practice. (6 marks)

**B3.** A server's IP address is changed from 10.0.1.10 to 10.0.1.15 during a network re-addressing exercise. State: (a) which documents must be updated, (b) the correct version numbering for each update, and (c) what must be added to the change log. (6 marks)

---

### Bahagian C: Soalan Situasi / Situational Question (50 marks)

**C1.** SRV-DC01 has been fully configured (hardware, OS, roles, and security as completed in KK-03 through KK-05). The time has come to produce the handover documentation and conduct a formal handover to the operations team.

**(a)** List ALL PowerShell commands you would run to collect the server's live configuration data as an evidence base for the As-Built Document. For each command, state what information it captures. (Minimum 6 commands.) (18 marks)

**(b)** Complete the Server Identity and Network Configuration sections of the Server Configuration Record for SRV-DC01 based on the following known values: Hostname = SRV-DC01; Domain = pioneer.edu.my; Roles = Domain Controller, DNS, DHCP; Rack = Server Room A, Rack 2, U3-U4; Asset Tag = PA-IT-2026-001; Production IP = 10.0.1.10/24, Gateway = 10.0.1.1, VLAN 10; iDRAC IP = 10.0.10.5/24, VLAN 20; Responsible admin = your name. Present these sections in the table format shown in KP-06. (12 marks)

**(c)** During the As-Built review, you discover that the planned RAID level for the DATA volume was RAID 10, but you actually configured RAID 5 (due to a hardware limitation discovered during installation). Describe how you would document this deviation: (i) what to write in the Deviations section, (ii) whether this requires a change request or stakeholder approval, and (iii) what risk note to include. (12 marks)

**(d)** You are conducting the handover walkthrough with the Operations Team Lead. Write a structured 5-item handover agenda (the five topics you will cover, in logical order) and for each item state what you will demonstrate or provide. (8 marks)

---

## Kriteria Penilaian / Assessment Criteria

| Section | Marks | Criteria |
|---------|-------|---------|
| A (MCQ) | 20 | Correct answer = 4 marks |
| B1 | 18 | 3 marks per doc type: name (1) + purpose (1) + audience (1) |
| B2 | 6 | Professional error explanation (2) + two consequences (2 each) |
| B3 | 6 | Documents to update (2) + version numbering (2) + change log entry (2) |
| C1(a) | 18 | 3 marks per command: command (1) + information captured (2); minimum 6 |
| C1(b) | 12 | Server Identity complete (6) + Network Configuration table complete (6) |
| C1(c) | 12 | Deviation written correctly (4) + change request decision + justification (4) + risk note (4) |
| C1(d) | 8 | 5 agenda items in logical order (5) + what demonstrated/provided per item (3) |
| **TOTAL** | **100** | |

---

## Skema Jawapan / Answer Scheme

*To be provided by the instructor after submission.*