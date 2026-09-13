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

## PELAN MENGAJAR – TEORI

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-3:2013 OPERASI SISTEM KOMPUTER |
| TAHAP | 3 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C05 SERVER MAINTENANCE |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE SERVER MAINTENANCE JOB ORDER<br>2. CARRY OUT HARDWARE MAINTENANCE<br>3. PERFORM SERVER OPERATING SYSTEM MAINTENANCE<br>4. PREPARE SERVER MAINTENANCE RECORD |
| NO. KOD | IT-020-3:2013-C05/PM(TEORI) |
| Muka Surat | 1/1 |
| WARNA KERTAS | KUNING (Yellow) |

**TAJUK:** PM-teori-server-maintenance

**TUJUAN:** Kertas rujukan untuk PM-teori-server-maintenance.

**TEMPAT:** BILIK KULIAH

**TEMPOH:** Rujuk JPW/RK.

**TUJUAN PENGAJARAN:** Pada akhir sesi pengajaran, pelatih akan dapat menguasai pengetahuan/kemahiran berkaitan aktiviti kerja CU ini.

**ALAT BANTUAN MENGAJAR:** Papan putih, projektor, slaid pengajaran, bahan tunjuk-cara.

<!-- /JPK_ENVELOPE_v1 -->
**TUJUAN:** Upon completion of all 4 KP/KT sessions, trainees will sit for the Knowledge Assessment (KA).

**TEMPAT:** BILIK KULIAH

**TEMPOH:** 54 jam teori / 54 theory hours (rujuk JPW/RK)

**TUJUAN PENGAJARAN:** Pada akhir sesi pengajaran, pelatih akan dapat menguasai pengetahuan berkaitan analisis arahan kerja penyelenggaraan pelayan, penyelenggaraan perkakasan, penyelenggaraan sistem operasi pelayan, dan penyediaan rekod penyelenggaraan.

**ALAT BANTUAN MENGAJAR:** Papan putih, projektor, slaid pengajaran, bahan tunjuk-cara, contoh arahan kerja, log pelayan sebenar.

---

## Agihan Masa Teori / Theory Time Allocation

| KP | Tajuk / Title | Jam / Hours |
|----|--------------|-------------|
| KP(1/4) | Server Maintenance Job Order Analysis and Maintenance Planning | 8.0 |
| KP(2/4) | Server Hardware Components, Inspection Procedures, and Fault Diagnosis | 16.0 |
| KP(3/4) | Server Operating System Maintenance — Patching, Log Analysis, and Service Management | 22.0 |
| KP(4/4) | Server Maintenance Documentation and Record Preparation | 8.0 |
| **Jumlah / Total** | | **54.0** |

> *Nisbah Teori:Amali = 30:70. Jumlah jam keseluruhan CU 5 = 180 jam. / Theory:Practical ratio = 30:70. Total CU 5 hours = 180.*

---

## Huraian Kandungan / Content Outline per KP

### KP(1/4) — Server Maintenance Job Order Analysis and Maintenance Planning *(8 hours)*

| Topik | Kandungan |
|-------|-----------|
| 1.1 Types of server maintenance | Preventive maintenance (PM), corrective maintenance, predictive maintenance; scheduled vs. unscheduled |
| 1.2 Maintenance job order structure | Fields: server asset tag, model, OS, RAID config, scope of work, maintenance window, authorisation; interpreting priority levels |
| 1.3 Pre-maintenance planning | Reading and verifying job order; preparing maintenance checklist; identifying required tools, spare parts, and materials |
| 1.4 Change and risk management | Impact of maintenance on live services; communication protocol; rollback planning; maintenance window constraints |
| 1.5 Health and safety overview | Electrical safety; ESD precautions; PPE requirements; lock-out/tag-out (LOTO) principles |

### KP(2/4) — Server Hardware Components, Inspection Procedures, and Fault Diagnosis *(16 hours)*

| Topik | Kandungan |
|-------|-----------|
| 2.1 Server hardware architecture | Rack vs. tower form factors; chassis components; hot-swap vs. non-hot-swap bays; front/rear panel layout |
| 2.2 CPU and cooling systems | Server-grade CPUs (Intel Xeon, AMD EPYC); heatsink types; thermal paste application; fan zones; temperature thresholds |
| 2.3 Memory (RAM) | ECC vs. non-ECC; RDIMM vs. LRDIMM; memory population rules; ECC error detection and correction; replacing failed DIMMs |
| 2.4 Storage subsystem | HDD, SSD, NVMe in servers; RAID levels (0, 1, 5, 6, 10) — purpose, disk count, fault tolerance; RAID controller; hot-swap disk replacement; SMART data interpretation |
| 2.5 Power supplies | Redundant PSU (1+1, 2+2); hot-swap PSU; power draw calculation; UPS integration |
| 2.6 Cleaning and inspection procedures | Compressed air technique; lint-free cloths; anti-static mat; dust filter cleaning; cable inspection and management |
| 2.7 Hardware fault diagnosis | Using BIOS/iDRAC/iLO/BMC management consoles; POST error codes; LED indicators; RAID status indicators; identifying failed components |

### KP(3/4) — Server Operating System Maintenance — Patching, Log Analysis, and Service Management *(22 hours)*

| Topik | Kandungan |
|-------|-----------|
| 3.1 OS patch management (Windows Server) | Windows Update / WSUS; cumulative updates, security patches, service packs; patch testing and staging; applying updates; verifying patch status |
| 3.2 OS patch management (Linux Server) | `apt`/`yum`/`dnf` package managers; security repositories; kernel updates; checking installed packages (`dpkg -l`, `rpm -qa`) |
| 3.3 Event log analysis (Windows Server) | Event Viewer structure: Application, Security, System; event levels (Critical, Error, Warning, Information); identifying disk I/O errors, service failures, security events; exporting and archiving logs |
| 3.4 System log analysis (Linux Server) | `/var/log/syslog`, `/var/log/messages`, `/var/log/auth.log`; using `journalctl`; filtering by date and severity |
| 3.5 Filesystem integrity | `chkdsk /f /r` (Windows); `fsck` (Linux); `sfc /scannow` for Windows system file verification; scheduling filesystem checks; interpreting results |
| 3.6 Service management | `services.msc` (Windows); `systemctl` (Linux); identifying critical server services (DNS, DHCP, Active Directory, File Sharing, Web Server); starting/stopping/restarting services; configuring automatic recovery |
| 3.7 Server performance monitoring | Task Manager, Resource Monitor, Performance Monitor (Windows); `top`, `htop`, `vmstat`, `iostat` (Linux); baseline vs. current performance; identifying bottlenecks |
| 3.8 Security hardening checks | Reviewing user accounts; disabled accounts; password policies; firewall rules; antivirus/anti-malware status |

### KP(4/4) — Server Maintenance Documentation and Record Preparation *(8 hours)*

| Topik | Kandungan |
|-------|-----------|
| 4.1 Purpose of maintenance records | Compliance requirements; historical reference; warranty and SLA tracking; audit trail |
| 4.2 Maintenance record structure | Required fields: server details, date/time, technician name, scope of work performed, findings, components replaced, test results, next maintenance date, authorisation |
| 4.3 Recording hardware findings | How to document: cleaning performed, components inspected, faults found, remedial actions taken, RAID status |
| 4.4 Recording OS maintenance findings | Patches applied (KB numbers / package versions), log anomalies found and resolved, filesystem check results, service status |
| 4.5 Closing and submitting the record | Technician signature; supervisor/manager counter-signature; filing and retention procedures; updating asset management system |

---

## Kaedah Pengajaran / Teaching Method (4-Step)

### 1. PERSEDIAAN (Preparation)

| Langkah / Step | Aktiviti / Activity | Masa / Duration |
|----------------|---------------------|-----------------|
| 1.1 | Welcome trainees and take attendance | 5 min |
| 1.2 | State the learning objectives for the session | 5 min |
| 1.3 | Relate topic to previous knowledge (computer set-up, networking) and real-world server maintenance scenarios | 5 min |
| 1.4 | Provide overview of the Information Sheet (KP) content for the session | 5 min |

### 2. PENYAMPAIAN (Presentation)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 2.1 | Deliver theory content from the relevant KP using slides, diagrams, and real server examples |
| 2.2 | Explain key terms and concepts with workplace scenarios (e.g., RAID failure during business hours) |
| 2.3 | Show server hardware images, RAID diagrams, event log screenshots, and patch management interfaces |
| 2.4 | Discuss common server faults and systematic troubleshooting approaches |
| 2.5 | Encourage questions and clarify misunderstandings using worked examples |
| 2.6 | Highlight safety requirements: ESD protection, electrical isolation, hot-swap procedures |

### 3. PENGGUNAAN (Application)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 3.1 | Distribute the corresponding KT (Assignment Sheet) for the session |
| 3.2 | Trainees complete the assignment individually or in pairs |
| 3.3 | Instructor provides guidance and support during the exercise |
| 3.4 | Discuss answers and common errors with the class; review correct approaches |

### 4. PENGESAHAN (Confirmation)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 4.1 | Review key learning points from the session |
| 4.2 | Conduct brief oral questioning to verify understanding |
| 4.3 | Collect completed KT for marking and feedback |
| 4.4 | Preview the next session topic |
| 4.5 | Record attendance and session completion |

---

## Sumber Pengajaran / Teaching Resources

| Sumber / Resource | Keterangan / Description |
|-------------------|--------------------------|
| KP(1/4) to KP(4/4) | Information Sheets for all 4 Work Activities |
| KT(1/4) to KT(4/4) | Assignment Sheets for all 4 Work Activities |
| Slide presentation | PowerPoint or equivalent slides covering each KP topic |
| Whiteboard / projector | For diagrams, RAID layouts, and event log examples |
| Sample server (or photos) | For identifying components and discussing hardware PM |
| Printed job order samples | Sample maintenance job orders for analysis exercises |
| Printed event log excerpts | Sample Windows/Linux log outputs for analysis exercises |
| NOSS document | IT-020-3:2013 CoCu 5 reference |

---

## Penilaian Teori / Theory Assessment

Upon completion of all 4 KP/KT sessions, trainees will sit for the Knowledge Assessment (KA):

- **Kod / Code:** IT-020-3:2013-C05/KA
- **Tempoh minimum / Minimum duration:** 1 hour 30 minutes
- **Format:** Written test (MCQ, short answer, structured essay)
- **Markah lulus / Pass mark:** 60% (60/100)
- **Syarat / Condition:** Closed book; all KT assignments must be completed prior to sitting KA