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

## PELAN MENGAJAR – AMALI

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-3:2013 OPERASI SISTEM KOMPUTER |
| TAHAP | 3 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C05 SERVER MAINTENANCE |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE SERVER MAINTENANCE JOB ORDER<br>2. CARRY OUT HARDWARE MAINTENANCE<br>3. PERFORM SERVER OPERATING SYSTEM MAINTENANCE<br>4. PREPARE SERVER MAINTENANCE RECORD |
| NO. KOD | IT-020-3:2013-C05/PM(AMALI) |
| Muka Surat | 1/1 |
| WARNA KERTAS | KUNING (Yellow) |

**TAJUK:** PM-amali-server-maintenance

**TUJUAN:** Kertas rujukan untuk PM-amali-server-maintenance.

**TEMPAT:** BILIK AMALI / MAKMAL

**TEMPOH:** Rujuk JPW/RK.

**TUJUAN PENGAJARAN:** Pada akhir sesi pengajaran, pelatih akan dapat menguasai pengetahuan/kemahiran berkaitan aktiviti kerja CU ini.

**ALAT BANTUAN MENGAJAR:** Papan putih, projektor, slaid pengajaran, bahan tunjuk-cara.

<!-- /JPK_ENVELOPE_v1 -->
**TUJUAN:** Upon completion of all 4 KK sessions, trainees will sit for the Performance Assessment (PA).

**TEMPAT:** BILIK AMALI / MAKMAL PELAYAN (Server Lab)

**TEMPOH:** 126 jam amali / 126 practical hours (rujuk JPW/RK)

**TUJUAN PENGAJARAN:** Pada akhir sesi pengajaran, pelatih akan dapat melaksanakan analisis arahan kerja penyelenggaraan pelayan, penyelenggaraan perkakasan pelayan, penyelenggaraan sistem operasi pelayan, dan penyediaan rekod penyelenggaraan dengan betul dan selamat.

**ALAT BANTUAN MENGAJAR:** Pelayan latihan (tower/rack), set alatan penyelenggaraan, bahan pembersih, media pemasangan OS, borang rekod penyelenggaraan.

---

## Agihan Masa Amali / Practical Time Allocation

| KK | Tajuk / Title | Jam / Hours |
|----|--------------|-------------|
| KK(1/4) | Analysing Server Maintenance Job Orders and Preparing Maintenance Checklists | 19.0 |
| KK(2/4) | Carrying Out Server Hardware Maintenance — Cleaning, Inspection, and Component Verification | 57.0 |
| KK(3/4) | Performing Server OS Maintenance — Patching, Log Review, Filesystem Check, and Service Verification | 38.0 |
| KK(4/4) | Preparing and Submitting Server Maintenance Records | 12.0 |
| **Jumlah / Total** | | **126.0** |

> *Nisbah Teori:Amali = 30:70. Jumlah jam keseluruhan CU 5 = 180 jam. / Theory:Practical ratio = 30:70. Total CU 5 hours = 180.*

---

## Huraian Kandungan Amali / Practical Content Outline per KK

### KK(1/4) — Analysing Server Maintenance Job Orders and Preparing Maintenance Checklists *(19 hours)*

| Aktiviti | Huraian |
|----------|---------|
| 1.1 | Read and interpret provided maintenance job orders; identify server details, scope, maintenance window, and constraints |
| 1.2 | Cross-check job order fields against a standard checklist template; flag missing or ambiguous information |
| 1.3 | Identify all required tools, spare parts, and materials from the job order; prepare a bill of materials |
| 1.4 | Draft a step-by-step maintenance plan aligned to the job order scope and time window |
| 1.5 | Simulate pre-maintenance communication — notify instructor (acting as IT Manager) of readiness |

### KK(2/4) — Carrying Out Server Hardware Maintenance *(57 hours)*

| Aktiviti | Huraian |
|----------|---------|
| 2.1 | Power down server safely following correct shutdown procedure; disconnect power cables; attach anti-static wrist strap |
| 2.2 | Open server chassis; photograph internal layout before any work (simulated with mobile phone or worksheet diagram) |
| 2.3 | Use compressed air and lint-free cloths to clean heatsinks, CPU fans, case fans, air baffles, and motherboard surface |
| 2.4 | Inspect and reseat RAM DIMMs; check for physical damage or corrosion on contacts |
| 2.5 | Inspect and reseat expansion cards (RAID controller, NIC); check PCIe slots and connectors |
| 2.6 | Check all internal cables (power connectors, SATA/SAS data cables, front-panel cables) for secure seating and wear |
| 2.7 | Check drive bays: verify each drive is firmly seated; read RAID status LED indicators and record status |
| 2.8 | Check PSU fan operation; verify redundant PSU (if installed) and hot-swap functionality |
| 2.9 | Clean and replace dust filters (front intake, rear exhaust) |
| 2.10 | Reassemble server; restore power; verify successful POST and OS boot |
| 2.11 | Access management console (iDRAC / iLO / BIOS): check temperature, fan speed, and hardware health logs |
| 2.12 | Record all hardware findings, actions taken, and component status on the maintenance record form |

### KK(3/4) — Performing Server OS Maintenance *(38 hours)*

| Aktiviti | Huraian |
|----------|---------|
| 3.1 | Log in to server OS (Windows Server or Linux); verify current OS version and patch level |
| 3.2 | **Windows:** Open Windows Update / WSUS; check for available updates; apply security patches; reboot if required; verify patch installation success |
| 3.3 | **Linux:** Run `apt update && apt upgrade` (Debian/Ubuntu) or `yum update` / `dnf update` (RHEL/CentOS); verify package upgrade log |
| 3.4 | Open Event Viewer (Windows) or `journalctl` / `/var/log/` (Linux); review Application, Security, and System logs for errors and warnings over the past 30 days; document findings |
| 3.5 | Run `chkdsk C: /f` (Windows, schedule on next reboot) or `fsck /dev/sdX` (Linux, unmounted volume); document results and any bad sectors or errors found |
| 3.6 | Run `sfc /scannow` (Windows) to verify system file integrity; document outcome |
| 3.7 | Open Services (`services.msc`) or `systemctl list-units --type=service` (Linux); verify all critical services are running; restart any stopped services; document status |
| 3.8 | Check server performance baseline: CPU utilisation, RAM usage, disk I/O, network throughput using Task Manager / Performance Monitor (Windows) or `top` / `vmstat` (Linux); record readings |
| 3.9 | Verify antivirus/anti-malware definitions are current; run a quick scan; document result |
| 3.10 | Review firewall rules and active user accounts; flag any anomalies on the maintenance record |

### KK(4/4) — Preparing and Submitting Server Maintenance Records *(12 hours)*

| Aktiviti | Huraian |
|----------|---------|
| 4.1 | Complete the server maintenance record form: server details, maintenance date/time, technician name, scope of work |
| 4.2 | Record all hardware maintenance actions: components cleaned, inspected, reseated, or replaced; RAID status; temperature readings |
| 4.3 | Record all OS maintenance actions: patches applied (KB numbers / package names), log findings, filesystem check results, service status |
| 4.4 | Record test/verification outcomes: POST success, OS boot, service start-up, network connectivity, RAID integrity |
| 4.5 | Sign the maintenance record; present to instructor (acting as IT Manager) for counter-signature |
| 4.6 | Simulate filing: place completed record in the designated server maintenance folder / update asset register |

---

## Kaedah Pengajaran / Teaching Method (4-Step)

### 1. PERSEDIAAN (Preparation)

| Langkah / Step | Aktiviti / Activity | Masa / Duration |
|----------------|---------------------|-----------------|
| 1.1 | Welcome trainees; take attendance and verify PPE (anti-static wrist strap) | 5 min |
| 1.2 | State the practical learning objectives for the session | 5 min |
| 1.3 | Review safety rules: ESD protection, electrical isolation, compressed air handling, workspace hygiene | 5 min |
| 1.4 | Distribute the KK (Work Sheet) and explain the exercise structure and expected outcomes | 5 min |
| 1.5 | Verify all equipment and materials are available at each workstation before commencing | 5 min |

### 2. PENYAMPAIAN (Demonstration)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 2.1 | Demonstrate the practical task step-by-step as per the KK procedures |
| 2.2 | Highlight critical safety steps: attaching ESD wrist strap, disconnecting power before opening chassis, correct use of compressed air |
| 2.3 | Demonstrate correct and incorrect techniques; explain consequences of errors (e.g., ESD damage to DIMM, incorrect RAID disk replacement) |
| 2.4 | Demonstrate OS maintenance tools (Windows Update, Event Viewer, chkdsk, services.msc) with live or screenshot walk-through |
| 2.5 | Answer questions before trainees begin their own work |

### 3. PENGGUNAAN (Practice)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 3.1 | Trainees perform the practical task at their individual workstations following the KK work sheet |
| 3.2 | Instructor circulates to observe, guide, and correct technique without performing the task for the trainee |
| 3.3 | Brief oral questioning during practice to verify understanding of the steps being performed |
| 3.4 | Trainees complete the KK assessment checklist and maintenance record as they work |

### 4. PENGESAHAN (Confirmation)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 4.1 | Instructor checks each trainee's completed work against the KK assessment checklist |
| 4.2 | Verify the expected outcome is achieved: server boots cleanly, OS maintenance tasks completed, maintenance record complete and signed |
| 4.3 | Provide feedback on process, output, attitude, safety compliance, and workspace cleanliness |
| 4.4 | Trainees clean workspace, return tools to storage, and ensure server is left in operational condition |
| 4.5 | Record session completion and any issues for instructor log |

---

## Peralatan dan Bahan / Equipment and Materials

| Item | Kuantiti per Pelatih / Quantity per Trainee | Nota / Notes |
|------|---------------------------------------------|--------------|
| Tower or rack server (training unit) | 1 | Windows Server 2019/2022 or Linux installed |
| Phillips-head and flat-head screwdriver set | 1 | Including magnetic tip |
| Anti-static wrist strap | 1 | Must be worn during all hardware work |
| Anti-static mat | 1 | Grounded work surface |
| Compressed air canister | 1 (shared) | ESD-safe; do not tilt during use |
| Lint-free cleaning cloths | 2 | For chassis interior surfaces |
| Isopropyl alcohol (70–90%) | 1 bottle (shared) | For stubborn residue on contacts; allow to dry fully before reassembly |
| Thermal paste | 1 tube (shared) | If CPU heatsink is removed for deep cleaning |
| Replacement dust filters | 1 set (shared) | Front/rear intake filters |
| USB bootable media (OS installer / recovery) | 1 | In case OS repair is needed |
| Server maintenance record form | 1 per session | Printed template |
| Printed maintenance job order | 1 | Scenario sheet for the session |
| Network cable (Cat 5e or Cat 6) | 1 | For verifying network connectivity post-maintenance |

---

## Keselamatan / Safety Requirements

- Anti-static wrist strap **MUST** be worn and connected to the server chassis ground at all times when handling internal components.
- Server power **MUST** be fully disconnected before opening the chassis or handling the motherboard, RAM, CPU, or storage drives.
- Compressed air **must not** be directed at spinning fans — hold fans stationary with a finger or cable tie before blowing.
- Isopropyl alcohol must be fully dry before powering on the server.
- Cables must not obstruct fan airflow after reassembly.
- E-waste (damaged components, cleaning materials) must be disposed of through authorised channels; do not discard electronic components in general waste.

---

## Penilaian Amali / Practical Assessment

Upon completion of all 4 KK sessions, trainees will sit for the Performance Assessment (PA):

- **Kod / Code:** IT-020-3:2013-C05/PA
- **Tempoh / Duration:** 2 hours 15 minutes
- **Format:** Practical task — full server maintenance cycle from job order analysis to maintenance record submission
- **Kriteria penilaian / Assessment criteria:** Process, output, attitude, safety, and environmental compliance
- **Markah lulus / Pass mark:** Competent (C) — ≥ 60% overall with no critical safety failure