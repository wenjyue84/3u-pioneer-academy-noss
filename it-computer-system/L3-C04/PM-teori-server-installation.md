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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C04 SERVER INSTALLATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE JOB ORDER/CHANGE REQUEST<br>2. EXECUTE HARDWARE INSTALLATION<br>3. CARRY OUT SOFTWARE INSTALLATION<br>4. PERFORM SERVER FUNCTIONALITY TEST<br>5. PREPARE SERVER INSTALLATION SET-UP REPORT |
| NO. KOD | IT-020-3:2013-C04/PM(TEORI) |
| Muka Surat | 1/1 |
| WARNA KERTAS | KUNING (Yellow) |

**TAJUK:** PM-teori-server-installation

**TUJUAN:** Kertas rujukan untuk PM-teori-server-installation.

**TEMPAT:** BILIK KULIAH

**TEMPOH:** Rujuk JPW/RK.

**TUJUAN PENGAJARAN:** Pada akhir sesi pengajaran, pelatih akan dapat menguasai pengetahuan/kemahiran berkaitan aktiviti kerja CU ini.

**ALAT BANTUAN MENGAJAR:** Papan putih, projektor, slaid pengajaran, bahan tunjuk-cara.

<!-- /JPK_ENVELOPE_v1 -->
**TUJUAN:** Upon completion of all 5 KP/KT sessions, trainees will sit for the Knowledge Assessment (KA): IT-020-3:2013-C04/KA.

**TEMPAT:** BILIK KULIAH

**TEMPOH:** Rujuk JPW/RK. Jumlah jam teori: 72 jam (30% daripada 240 jam CoCU 4).

**TUJUAN PENGAJARAN:** Pada akhir sesi pengajaran, pelatih akan dapat menguasai pengetahuan berkaitan pemasangan pelayan merangkumi analisis job order, pemasangan perkakasan pelayan, pemasangan perisian dan sistem operasi pelayan, ujian fungsi pelayan, dan penyediaan laporan pemasangan.

**ALAT BANTUAN MENGAJAR:** Papan putih, projektor, slaid pengajaran, bahan tunjuk-cara, model perkakasan pelayan, diagram rack dan RAID.

---

## Agihan Masa Teori / Theory Time Allocation

| KP | Tajuk / Title | Jam / Hours |
|----|--------------|-------------|
| KP(1/5) | Server Job Order Analysis and Pre-Installation Planning | 10.8 |
| KP(2/5) | Server Hardware Architecture and Installation Principles | 28.8 |
| KP(3/5) | Server Operating System and Software Installation | 21.6 |
| KP(4/5) | Server Functionality Testing and Verification Methods | 7.2 |
| KP(5/5) | Server Installation Documentation and Reporting | 3.6 |
| **Jumlah / Total** | | **72.0** |

---

## Kandungan Topik / Topic Content Summary

### KP(1/5) — Server Job Order Analysis and Pre-Installation Planning (10.8 hours)

| Subtopik / Sub-topic | Isi Kandungan / Content |
|----------------------|-------------------------|
| 1.1 Job order structure | Mandatory fields: job order number, requestor, priority level, server specifications, deadline, site details |
| 1.2 Requirements interpretation | Reading technical specifications: CPU socket type, RAM type (ECC/non-ECC), storage interface (SAS/SATA/NVMe), network requirements |
| 1.3 Compatibility checking | CPU–motherboard socket compatibility; RAM type and speed compatibility; PCIe lane allocation for add-in cards |
| 1.4 Rack space planning | U-height calculation; weight load rating; front-to-back airflow direction; cable management tray placement |
| 1.5 Site readiness | Power circuit capacity; PDU rating; cooling adequacy; network switch port availability |
| 1.6 Change request management | Documenting deviations from original specification; approval workflow; impact assessment |

### KP(2/5) — Server Hardware Architecture and Installation Principles (28.8 hours)

| Subtopik / Sub-topic | Isi Kandungan / Content |
|----------------------|-------------------------|
| 2.1 Server form factors | Tower, rack-mount (1U/2U/4U), blade; trade-offs between density, cost, and serviceability |
| 2.2 Server CPUs | Intel Xeon vs AMD EPYC; NUMA architecture; multi-socket configurations; TDP and cooling requirements; ECC memory dependency |
| 2.3 ECC RAM | Error-correcting code memory; DIMM slot population rules; registered vs unbuffered; maximum capacity per platform |
| 2.4 Server storage subsystems | SAS vs SATA vs NVMe drives; HBA vs RAID controller cards; hot-swap bays; drive tray installation |
| 2.5 RAID levels | RAID 0, 1, 5, 6, 10 — minimum drives, parity, fault tolerance, read/write performance, typical use case |
| 2.6 Server power subsystems | Redundant PSU (1+1); hot-swap PSU; power factor correction; PDU connections; power budgeting |
| 2.7 Out-of-band management | iLO (HPE), iDRAC (Dell), IPMI standard; BMC functions; remote KVM; out-of-band network port |
| 2.8 Rack installation procedure | Rail kit types (tool-less, tooled, rapid deploy); rack unit alignment; server sliding and securing; cable arm routing |
| 2.9 ESD and rack safety | Anti-static wrist strap usage; grounding the rack; weight distribution; two-person lift for heavy servers |

### KP(3/5) — Server Operating System and Software Installation (21.6 hours)

| Subtopik / Sub-topic | Isi Kandungan / Content |
|----------------------|-------------------------|
| 3.1 BIOS/UEFI configuration | Boot order; Secure Boot; Intel VT-x / AMD-V; RAID mode vs AHCI mode; memory frequency; time and date synchronisation |
| 3.2 RAID configuration via controller | Accessing RAID BIOS utility; creating virtual disk; selecting RAID level; initialisation; verifying array status |
| 3.3 OS selection for servers | Windows Server 2022 (Standard/Datacenter); Ubuntu Server LTS; licensing considerations |
| 3.4 OS installation sequence | Bootable media preparation; partition planning (OS volume + data volume); driver injection during setup |
| 3.5 Driver installation order | RAID/storage controller → chipset → NIC → management agent (iLO/iDRAC) → optional components |
| 3.6 Server role configuration | Windows Server: Roles and Features Wizard (File and Storage Services, Active Directory, DNS); Linux: package manager-based service installation |
| 3.7 Network configuration | Static IP assignment; DNS server; default gateway; NIC teaming / bonding; VLAN tagging |
| 3.8 Remote management setup | Enabling ILO/iDRAC network access; setting administrator credentials; verifying remote console connectivity |

### KP(4/5) — Server Functionality Testing and Verification Methods (7.2 hours)

| Subtopik / Sub-topic | Isi Kandungan / Content |
|----------------------|-------------------------|
| 4.1 POST verification | Interpreting POST codes and LED indicators; resolving common POST errors |
| 4.2 Hardware detection check | Device Manager (Windows) / `lspci`, `lshw` (Linux); confirming all CPUs, RAM, NICs, and storage detected |
| 4.3 RAID status verification | RAID controller management utility; verifying array state (Optimal/Degraded/Failed) |
| 4.4 Network connectivity test | `ipconfig /all` or `ip addr`; `ping` gateway and external host; `tracert`/`traceroute` |
| 4.5 Server role test | Mapping a network drive to test file share; querying Active Directory; verifying service status |
| 4.6 Stress and stability test | Running CPU and memory stress tools (e.g. Prime95, MemTest86) to verify stability under load |
| 4.7 Remote management test | Logging in via iLO/iDRAC web interface; verifying sensor readings (temperature, fan speed, power) |

### KP(5/5) — Server Installation Documentation and Reporting (3.6 hours)

| Subtopik / Sub-topic | Isi Kandungan / Content |
|----------------------|-------------------------|
| 5.1 Set-up report structure | Mandatory sections: job order reference, hardware inventory (make/model/serial), RAID configuration, OS version and licence key, IP addressing, driver versions, test results, deviations |
| 5.2 Deviation documentation | Recording component substitutions; obtaining supervisor/customer approval signature; attaching supporting evidence |
| 5.3 Handover procedure | Presenting report to requestor; demonstrating server accessibility; obtaining sign-off |
| 5.4 Record-keeping | Filing set-up report in asset management system; updating network documentation |

---

## Kaedah Pengajaran / Teaching Method (4-Step)

### 1. PERSEDIAAN (Preparation)

| Langkah / Step | Aktiviti / Activity | Masa / Duration |
|----------------|---------------------|-----------------|
| 1.1 | Welcome trainees and take attendance | 5 min |
| 1.2 | State the learning objectives for the session | 5 min |
| 1.3 | Relate topic to real-world data centre and server room contexts | 5 min |
| 1.4 | Provide overview of the Information Sheet (KP) content for the session | 5 min |

### 2. PENYAMPAIAN (Presentation)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 2.1 | Deliver theory content from the relevant KP using slides, diagrams, and worked examples |
| 2.2 | Explain key technical terms (RAID levels, ECC, ILO/iDRAC, NVMe, SAS) with real-world scenarios |
| 2.3 | Show rack diagrams, RAID parity calculations, and network topology drawings |
| 2.4 | Discuss common server installation faults and troubleshooting approaches (POST errors, memory training failure, RAID degraded state) |
| 2.5 | Encourage questions; clarify misconceptions with specific server-context examples |
| 2.6 | Highlight safety requirements: ESD protection, two-person rack lift procedures, electrical isolation |

### 3. PENGGUNAAN (Application)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 3.1 | Distribute the corresponding KT (Assignment Sheet) for the session |
| 3.2 | Trainees complete the assignment individually or in pairs |
| 3.3 | Instructor provides guidance and support during the exercise |
| 3.4 | Discuss answers and common errors with the class |

### 4. PENGESAHAN (Confirmation)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 4.1 | Review key learning points from the session |
| 4.2 | Conduct brief oral questioning to verify understanding (e.g. "What is the minimum number of drives for RAID 5?") |
| 4.3 | Collect completed KT for marking and feedback |
| 4.4 | Preview the next session topic |
| 4.5 | Record attendance and session completion |

---

## Sumber Pengajaran / Teaching Resources

| Sumber / Resource | Keterangan / Description |
|-------------------|--------------------------|
| KP(1/5) to KP(5/5) | Information Sheets for all 5 Work Activities |
| KT(1/5) to KT(5/5) | Assignment Sheets for all 5 Work Activities |
| Slide presentation | PowerPoint or equivalent slides covering each KP topic |
| Whiteboard / projector | For rack diagrams, RAID parity tables, network topology |
| Sample server hardware | Server chassis, CPU, ECC RAM, SAS/NVMe drives, RAID controller for show-and-tell |
| NOSS document | IT-020-3:2013 CoCU 4 reference |
| Vendor documentation | HPE ProLiant / Dell PowerEdge quick-start guides as supplementary reference |

---

## Penilaian Teori / Theory Assessment

Upon completion of all 5 KP/KT sessions, trainees will sit for the Knowledge Assessment (KA):

- **Code:** IT-020-3:2013-C04/KA
- **Minimum duration:** 1 hour 30 minutes
- **Format:** Written test (MCQ, short answer, structured essay)
- **Total marks:** 100
- **Pass mark:** 60