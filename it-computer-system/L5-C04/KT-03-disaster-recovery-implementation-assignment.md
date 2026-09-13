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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-C04 DISASTER RECOVERY MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE DISASTER RECOVERY REQUIREMENTS<br>2. DEVELOP DISASTER RECOVERY MANAGEMENT PLAN<br>3. IMPLEMENT COMPUTER NETWORK DISASTER RECOVERY MANAGEMENT PLAN<br>4. PRODUCE DISASTER RECOVERY MANAGEMENT REPORT |
| NO. KOD | IT-020-5:2013-C04/KT(3/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | MERAH JAMBU (Pink) |

**TAJUK:** KT-03-disaster-recovery-implementation-assignment

**TUJUAN:** Kertas rujukan untuk KT-03-disaster-recovery-implementation-assignment.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
**TUJUAN:** Answer ALL questions. Refer to KP(3/4) for guidance. Write your answers in the space provided or on a separate answer sheet. This assignment is formative and does not count toward final assessment.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

---

## Arahan / Instructions

Answer ALL questions. Refer to KP(3/4) for guidance. Write your answers in the space provided or on a separate answer sheet. This assignment is formative and does not count toward final assessment.

**Masa / Duration:** 1 hour 30 minutes

---

## Soalan / Questions

### Bahagian A: Soalan Pelbagai Pilihan / Multiple Choice (20 marks — 2 marks each)

**A1.** During DR plan activation, who has the authority to formally declare a disaster and authorise DRP execution?

- (a) Any IT helpdesk staff member
- (b) The DR Coordinator or designated authority as defined in the DRP
- (c) The company's external auditor
- (d) Any employee who notices the system is down

**A2.** In the network recovery sequence, which step must be completed FIRST before servers can be restored?

- (a) Restore all application servers
- (b) Restore the database backup
- (c) Restore physical connectivity, core network services (DHCP, DNS)
- (d) Update application connection strings

**A3.** The primary reason for running `DBCC CHECKDB` after database restoration is to:

- (a) Check the network speed at the DR site
- (b) Verify database integrity and detect corruption after restoration
- (c) Apply the latest service pack to SQL Server
- (d) Create a new backup of the restored database

**A4.** DNS TTL values should be set LOW (e.g. 300 seconds) before a DR event to:

- (a) Reduce DNS server memory usage
- (b) Allow faster propagation of updated DNS records pointing to the DR site
- (c) Prevent hackers from accessing DNS records
- (d) Improve website loading speed

**A5.** A TABLETOP EXERCISE differs from a FULL INTERRUPTION TEST in that:

- (a) A tabletop exercise involves no actual system changes; it is discussion-based only
- (b) A tabletop exercise shuts down all production systems
- (c) A tabletop exercise requires a live DR site to be active
- (d) A tabletop exercise is only for senior management, not IT staff

**A6.** During database recovery using log shipping, after applying the full backup and all transaction logs, what is the correct next step?

- (a) Delete the primary database
- (b) Bring the standby database online and open for user access; redirect application connections
- (c) Reboot the DR site servers
- (d) Contact the software vendor for a new licence key

**A7.** What is FAILBACK in the context of disaster recovery?

- (a) The failure of the DR site during an actual disaster
- (b) The process of returning operations from the DR site to the restored primary site
- (c) A backup that fails to complete within the scheduled window
- (d) A second disaster occurring while the first is still being recovered

**A8.** Which of the following is the CORRECT sequence for restoring application services after network and database recovery?

- (a) Web tier → middleware → database → authentication
- (b) Authentication → database → middleware → application tier → web tier
- (c) Database → authentication → web tier → middleware
- (d) Application tier → authentication → database → network

**A9.** A DR test report MUST include which of the following elements?

- (a) The personal performance reviews of all DR team members
- (b) Actual RTO/RPO achieved vs. targets, issues found, and corrective action recommendations
- (c) A full copy of the DRP attached as appendix
- (d) The vendor invoice for DR site rental

**A10.** Before declaring recovery complete, the DR Coordinator requires sign-off from:

- (a) All 200 users confirming they can access their email
- (b) Application owners confirming Tier 1 and Tier 2 systems have passed validation; Security Officer confirming security posture
- (c) The software vendor confirming all licences are active
- (d) The CEO only — no technical sign-off needed

---

### Bahagian B: Soalan Jawapan Pendek / Short Answer (30 marks)

**B1.** Describe the FOUR (4) types of DR tests in order from least to most disruptive. For each type, state: what is tested, what resources are required, and the main limitation of that test type. (12 marks)

**B2.** A company's database was last backed up at 22:00 on Sunday night (full backup). A ransomware attack is discovered at 14:30 on Monday afternoon. The company decides to restore from the Sunday backup.

(a) Calculate the RPO achieved (in hours). (2 marks)

(b) If the RTO target is 6 hours and the IT team begins recovery at 14:30, by what time must the system be operational? (2 marks)

(c) The recovery actually completes at 22:15 on Monday. Calculate whether the RTO target was met, and classify the variance. (4 marks)

**B3.** Explain why the network infrastructure (DNS, firewall, core switches) must be recovered BEFORE servers and applications during a DR activation. What would happen if an administrator attempted to start the ERP application server before DNS was functioning? (5 marks)

**B4.** List FIVE (5) items that must be verified in the Recovery Validation Checklist before the DR Coordinator can declare recovery complete. For each item, state the verification method. (5 marks)

---

### Bahagian C: Soalan Esei / Essay (40 marks)

**C1.** **Scenario:** At 03:15 on a Tuesday, the fire suppression system at **Bank Utama Berhad's** primary data centre activates due to a server room electrical fault. The suppression gas extinguishes the fire but damages several servers. By 03:45, IT Operations confirms that the core banking system, internet banking platform, and ATM network are all offline. The DR Coordinator is notified at 03:50.

The bank's DRP specifies:
- Core banking system: RTO = 2 hours, RPO = 15 minutes
- Internet banking: RTO = 4 hours, RPO = 30 minutes
- ATM network: RTO = 1 hour, RPO = zero (synchronous replication to DR site)

(a) Write the first 15 actions the DR team should take, in chronological order, from 03:50 (DR Coordinator notified) until systems are declared recovered. For each action, specify the responsible role and the approximate time allowed. (15 marks)

(b) The ATM network uses synchronous replication to the DR site. Explain step-by-step how the DR team would bring the ATM network online at the DR site, including any validation steps required before ATMs are reconnected to the network. (10 marks)

(c) At the end of the recovery, the DR Coordinator discovers that the core banking system RTO target of 2 hours was NOT met — actual RTO was 3 hours 45 minutes. Write the RTO variance analysis section of the DR Test Report for this system, including: actual vs. target comparison, classification (minor/major variance), root cause identification (you may invent a plausible reason), and TWO recommended corrective actions. (15 marks)

---

## Skema Jawapan / Answer Scheme

*To be provided by the instructor after submission.*