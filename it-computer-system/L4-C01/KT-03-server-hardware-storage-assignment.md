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
| NO. KOD | IT-020-4:2013-C01/KT(3/6) |
| Muka Surat | 1/1 |
| WARNA KERTAS | MERAH JAMBU (Pink) |

**TAJUK:** KT-03-server-hardware-storage-assignment

**TUJUAN:** Kertas rujukan untuk KT-03-server-hardware-storage-assignment.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Arahan / Instructions

Answer ALL questions. Refer to KP(3/6) for guidance. Write clearly on a separate answer sheet.

**Masa / Duration:** 60 minutes

---

## Tugasan / Questions

### Bahagian A: Soalan Pelbagai Pilihan / Multiple Choice (20 marks — 4 marks each)

**A1.** A hardware RAID controller with a battery-backed write cache (BBWC) improves write performance because:

- (a) It compresses data before writing to disk
- (b) It safely acknowledges writes to the OS immediately while physically writing to disk later, buffering writes in battery-protected RAM
- (c) It uses a faster SATA interface than the OS can access directly
- (d) It bypasses RAID parity calculation entirely

**A2.** Which BIOS/UEFI setting must be ENABLED before a Type 1 hypervisor (e.g. VMware ESXi) can be installed on a server?

- (a) Secure Boot
- (b) C-States power management
- (c) Virtualisation Technology (VT-x / AMD-V)
- (d) Legacy/CSM boot mode

**A3.** Out-of-band server management (e.g. iDRAC, iLO) allows an administrator to:

- (a) Manage network switches remotely
- (b) Access the server console and power controls independently of the OS, even when the OS is unresponsive
- (c) Back up virtual machines automatically
- (d) Update application software on client workstations

**A4.** LRDIMM (Load-Reduced DIMM) memory is used in servers instead of RDIMM when:

- (a) The server requires ECC memory for the first time
- (b) Maximum memory capacity per server must be extended beyond what RDIMM supports
- (c) The server is a workstation and does not require ECC
- (d) The server is running Linux instead of Windows

**A5.** A SAN (Storage Area Network) differs from NAS (Network-Attached Storage) in that SAN provides:

- (a) File-level access over SMB or NFS
- (b) Block-level access — the server sees the SAN LUN as a locally attached disk
- (c) Wireless storage access for laptops
- (d) Backup-only storage with no direct access

---

### Bahagian B: Soalan Jawapan Pendek / Short Answer (30 marks)

**B1.** Explain THREE (3) differences between consumer desktop RAM and enterprise server ECC RDIMM. (9 marks)

**B2.** A server has 6 × 1.2 TB SAS SSDs. An administrator proposes RAID 5 across all 6 disks. (a) Calculate the usable capacity. (b) State ONE advantage and ONE disadvantage of this configuration for a database workload. (c) Recommend an alternative RAID configuration and justify your recommendation. (12 marks)

**B3.** Describe the procedure for verifying hardware health on a Dell PowerEdge server before OS installation, including which tool to use and FOUR (4) specific checks to perform. (9 marks)

---

### Bahagian C: Soalan Situasi / Situational Question (50 marks)

**C1.** You have received a Dell PowerEdge R750 server for deployment as Pioneer Academy's new primary domain controller. The server has: 2 × Intel Xeon Gold CPUs, 256 GB ECC DDR4 RAM, 6 × 900 GB SAS SSD drives, Dell PERC H755 RAID controller with 8 GB FBWC, dual 25GbE NICs, dual redundant PSU, and iDRAC9 Enterprise.

**(a)** List the BIOS/UEFI settings you would configure for this production server, grouped by category (Boot, Virtualisation, Power, Memory, Security). For each setting, state the value you would configure and the reason. (Minimum 8 settings.) (20 marks)

**(b)** You have decided to create two RAID logical drives: OS-RAID1 using 2 of the 6 drives, and DATA-RAID10 using the remaining 4 drives. For each logical drive: state the RAID level, the drives used, the usable capacity (show calculation), the stripe size chosen and reason, and the read/write cache policy. (16 marks)

**(c)** After configuring the RAID, you discover that the FBWC (Flash-Backed Write Cache) shows a warning status in the RAID controller utility. Describe: (i) what risk this warning represents, (ii) the impact on RAID write performance if the cache is in write-through mode, and (iii) the action you would take before proceeding with OS installation. (9 marks)

**(d)** The iDRAC9 is configured with the default username and password. Explain why this is a critical security risk and describe the two immediate actions you must take. (5 marks)

---

## Kriteria Penilaian / Assessment Criteria

| Section | Marks | Criteria |
|---------|-------|---------|
| A (MCQ) | 20 | Correct answer = 4 marks |
| B1 | 9 | 3 marks per difference: feature (1) + desktop value (1) + server value (1) |
| B2(a) | 3 | Correct formula and answer: (6−1)/6 × 6 × 1.2 TB = 6 TB usable |
| B2(b) | 4 | Advantage (2) + Disadvantage (2) — must relate to database workload |
| B2(c) | 5 | Correct recommendation (2) + specific justification for database (3) |
| B3 | 9 | Tool named (1) + 4 checks, 2 marks each (8) |
| C1(a) | 20 | Setting name (1) + value (1) + reason (0.5) per setting; minimum 8 settings |
| C1(b) | 16 | Per logical drive: RAID level (1) + drives (1) + capacity calculation (2) + stripe size + reason (2) + cache policy (2) |
| C1(c) | 9 | Risk (3) + performance impact (3) + action (3) |
| C1(d) | 5 | Risk explanation (2) + two actions (1.5 each) |
| **TOTAL** | **100** | |

---

## Skema Jawapan / Answer Scheme

*To be provided by the instructor after submission.*