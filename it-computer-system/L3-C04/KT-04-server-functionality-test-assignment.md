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
| KOD DAN NAMA PROGRAM | IT-020-3:2013 OPERASI SISTEM KOMPUTER |
| TAHAP | 3 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C04 SERVER INSTALLATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE JOB ORDER/CHANGE REQUEST<br>2. EXECUTE HARDWARE INSTALLATION<br>3. CARRY OUT SOFTWARE INSTALLATION<br>4. PERFORM SERVER FUNCTIONALITY TEST<br>5. PREPARE SERVER INSTALLATION SET-UP REPORT |
| NO. KOD | IT-020-3:2013-C04/KT(4/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | MERAH JAMBU (Pink) |

**TAJUK:** KT-04-server-functionality-test-assignment

**TUJUAN:** Kertas rujukan untuk KT-04-server-functionality-test-assignment.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Arahan / Instructions

Answer ALL questions. Refer to KP-04 (Perform Server Functionality Test) for guidance. Write your answers in the space provided or on a separate answer sheet. This assignment is formative and does not count toward final assessment.

**Masa / Duration:** 45 minit / minutes

---

## Tugasan / Tasks

### Bahagian A: Soalan Pelbagai Pilihan / Multiple Choice (10 markah / marks)

**A1.** Which tool is used in Windows Server to verify that all installed hardware components are recognised by the operating system without errors?

- (a) Task Manager
- (b) Device Manager
- (c) Disk Management
- (d) Event Viewer — System Log

**A2.** A POST (Power-On Self-Test) failure indicated by repeated beep codes most likely signals:

- (a) A software licence expiry
- (b) A hardware fault such as missing or faulty RAM, CPU, or GPU
- (c) A corrupted Windows system file
- (d) An incorrect IP address configuration

**A3.** When testing network connectivity from the newly installed server, which command verifies that the server can reach the default gateway?

- (a) `ipconfig /all`
- (b) `netstat -an`
- (c) `ping 192.168.10.1`
- (d) `nslookup corp.prisma.local`

**A4.** A server functionality test for an Active Directory Domain Controller should include verifying that:

- (a) The server desktop wallpaper is displayed correctly
- (b) Domain authentication, DNS resolution, and replication with existing DCs are functioning
- (c) The server can browse the internet using a web browser
- (d) The server's BIOS date and time matches the wall clock

**A5.** When a RAID 5 volume shows a "Degraded" status after first power-on, the most likely cause is:

- (a) The RAID controller firmware needs updating
- (b) One or more drives failed to initialise or were not detected by the RAID controller
- (c) The server's power supply is insufficient for the drive count
- (d) The server operating system does not support RAID 5

---

### Bahagian B: Soalan Jawapan Pendek / Short Answer (15 markah / marks)

**B1.** List FIVE (5) areas that must be tested during a server functionality test after installation. *(5 markah)*

**B2.** Explain THREE (3) types of tests performed to verify server network functionality, stating the purpose of each test. *(6 markah)*

**B3.** Describe the procedure for using Windows Event Viewer to check for critical errors after a server installation, and state TWO (2) event categories a technician should examine. *(4 markah)*

---

### Bahagian C: Soalan Situasi / Situational Question (15 markah / marks)

**C1.** You have completed the hardware and software installation of a new rack server. The server has been configured as follows:

> **Server Role:** File and Print Server + Additional Domain Controller
> **OS:** Windows Server 2022 Standard (Desktop Experience)
> **IP Address:** 192.168.10.20/24
> **Domain:** corp.prisma.local
> **Storage:** RAID 5 volume (4 × 2 TB SAS, ~5.5 TB usable) — DFS share mapped as `\\corp.prisma.local\shared`
> **Print Service:** 3 shared printers configured
> **Redundant PSU:** Both PSUs connected to separate PDUs

During the functionality test, you observe the following:

- Event Viewer shows one Warning in the System log related to the NIC teaming driver (LACP negotiation delay)
- One shared printer shows status "Offline" in Print Management
- `ping corp.prisma.local` resolves correctly; `repadmin /showrepl` shows successful replication
- RAID volume status: Healthy (Initialising 4%)

Describe a systematic approach to performing the complete server functionality test, how you would respond to each of the four observations above, and what criteria must be met before you sign off the server as ready for handover. *(15 markah)*

---

## Kriteria Penilaian / Marking Criteria

| Bahagian | Soalan | Markah |
|---|---|---|
| A — Pelbagai Pilihan / Multiple Choice | A1–A5 | 10 |
| B — Jawapan Pendek / Short Answer | B1 | 5 |
| | B2 | 6 |
| | B3 | 4 |
| C — Situasi / Situational | C1 | 15 |
| **Jumlah / Total** | | **40** |

*Skema jawapan / Answer scheme: To be provided by the instructor after submission.*