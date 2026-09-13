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
| NO. KOD | IT-020-4:2013-C01/KT(2/6) |
| Muka Surat | 1/1 |
| WARNA KERTAS | MERAH JAMBU (Pink) |

**TAJUK:** KT-02-server-roles-planning-assignment

**TUJUAN:** Kertas rujukan untuk KT-02-server-roles-planning-assignment.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Arahan / Instructions

Answer ALL questions. Refer to KP(2/6) for guidance. Write your answers clearly on a separate answer sheet.

**Masa / Duration:** 60 minutes

---

## Tugasan / Questions

### Bahagian A: Soalan Pelbagai Pilihan / Multiple Choice (20 marks — 4 marks each)

**A1.** A domain controller running Active Directory Domain Services (AD DS) must have a minimum of TWO instances because:

- (a) One is for students and one is for staff
- (b) A single DC is a single point of failure — loss of the only DC prevents all domain authentication
- (c) Two DCs provide double the storage capacity
- (d) Microsoft requires two DCs for licensing compliance

**A2.** Which RAID level is most appropriate for a database server requiring high IOPS and low write latency?

- (a) RAID 0 — no redundancy but maximum performance
- (b) RAID 5 — good capacity efficiency
- (c) RAID 10 — mirrors + stripes; high read and write performance with fault tolerance
- (d) RAID 6 — two disk fault tolerance; best for large archival arrays

**A3.** In a virtualised server environment, a "Type 1 hypervisor" is defined as:

- (a) A hypervisor installed inside an existing OS (e.g. VMware Workstation)
- (b) A bare-metal hypervisor that runs directly on the hardware without a host OS (e.g. VMware ESXi, Hyper-V)
- (c) A hypervisor used only for testing environments
- (d) A hypervisor that requires a RAID 0 array

**A4.** For an organisation with 200 users, the recommended approach to server infrastructure is:

- (a) One physical server hosting all roles with no virtualisation
- (b) A virtualised server farm with 2–3 physical hosts
- (c) A dedicated physical server for every single role
- (d) A cloud-only solution — no on-premise servers required

**A5.** The formula `Usable capacity = Raw − RAID overhead − filesystem overhead` means that a 4-disk RAID 5 array using 1 TB disks (4 TB raw) provides approximately:

- (a) 4 TB usable
- (b) 2 TB usable (RAID 10 formula applied incorrectly)
- (c) 3 TB usable (one disk worth of parity overhead)
- (d) 1 TB usable

---

### Bahagian B: Soalan Jawapan Pendek / Short Answer (30 marks)

**B1.** List FIVE (5) common server roles and for each state: (a) the primary service it provides, and (b) the Windows Server role name or Linux equivalent. (15 marks)

**B2.** Compare the Dedicated Server Model with the Role Consolidation Model. State TWO (2) advantages and ONE (1) disadvantage of each model. (12 marks)

**B3.** Explain the difference between "horizontal scaling" and "vertical scaling" in the context of server capacity planning. Give ONE example of each. (3 marks)

---

### Bahagian C: Soalan Situasi / Situational Question (50 marks)

**C1.** Pioneer Academy's requirements analysis (from KT-01) identified the following confirmed requirements for the new server deployment:

- 800 students + 120 staff = 920 users total; peak concurrent logons estimated at 300
- Services required: Domain Controller (minimum 2), File Server, DHCP, DNS
- Availability: 99.9% uptime for DC and file services
- Budget: Two physical servers maximum
- Data: 2 TB current shared files; 25% annual growth rate
- OS: Windows Server 2022 Standard

**(a)** Design the server role architecture for this deployment. State which roles will be hosted on which server (Server 1 and Server 2), your chosen architecture model, and justification. (10 marks)

**(b)** For Server 1 (primary DC + DNS + DHCP), calculate the recommended: (i) CPU (minimum core count, with utilisation target); (ii) RAM (apply the appropriate rule from KP-02); (iii) Storage — OS volume size and DATA volume size. Show all workings for the storage calculation including RAID level, raw capacity, RAID overhead, 3-year growth, and free space buffer. (20 marks)

**(c)** Design the network topology for the two servers. Specify: IP addresses, subnet, default gateway, VLAN assignment for Production and Management, and DNS server configuration (primary and secondary). Draw a simple topology diagram (hand-drawn or text-based). (12 marks)

**(d)** Windows Server 2022 Standard licences allow 2 VMs per physical server licence. Explain whether the proposed architecture complies with this licensing model and what additional licences, if any, are required. (8 marks)

---

## Kriteria Penilaian / Assessment Criteria

| Section | Marks | Criteria |
|---------|-------|---------|
| A (MCQ) | 20 | Correct answer = 4 marks |
| B1 | 15 | 3 marks per role: role name (1) + service (1) + Windows/Linux name (1) |
| B2 | 12 | 2 marks per advantage/disadvantage: correct statement (1) + brief explanation (1) |
| B3 | 3 | Horizontal definition + example (1.5) + Vertical definition + example (1.5) |
| C1(a) | 10 | Role allocation (4) + architecture model named (2) + justification (4) |
| C1(b) | 20 | CPU (4) + RAM (4) + Storage: OS (4), DATA calculation with all steps shown (8) |
| C1(c) | 12 | IP addresses and subnets (4) + VLANs (3) + DNS config (2) + diagram (3) |
| C1(d) | 8 | Licensing rule stated correctly (3) + compliance analysis (3) + additional licence recommendation (2) |
| **TOTAL** | **100** | |

---

## Skema Jawapan / Answer Scheme

*To be provided by the instructor after submission.*