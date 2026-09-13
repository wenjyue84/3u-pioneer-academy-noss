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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C02 COMPUTER SYSTEM MAINTENANCE |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. IDENTIFY COMPUTER MAINTENANCE REQUIREMENTS<br>2. CARRY OUT COMPUTER SCHEDULED PREVENTIVE MAINTENANCE<br>3. PERFORM COMPUTER CORRECTIVE MAINTENANCE<br>4. PREPARE COMPUTER MAINTENANCE REPORT |
| NO. KOD | IT-020-3:2013-C02/PM(AMALI) |
| Muka Surat | 1/1 |
| WARNA KERTAS | KUNING (Yellow) |

**TAJUK:** PM-amali-computer-system-maintenance

**TUJUAN:** Kertas rujukan untuk PM-amali-computer-system-maintenance.

**TEMPAT:** BILIK AMALI / MAKMAL

**TEMPOH:** Rujuk JPW/RK.

**TUJUAN PENGAJARAN:** Pada akhir sesi pengajaran, pelatih akan dapat menguasai pengetahuan/kemahiran berkaitan aktiviti kerja CU ini.

**ALAT BANTUAN MENGAJAR:** Papan putih, projektor, slaid pengajaran, bahan tunjuk-cara.

<!-- /JPK_ENVELOPE_v1 -->
---

## Agihan Masa Amali / Practical Time Allocation

> Total CU hours: 120 hrs. Theory (30%): 36 hours. Practical (70%): **84 hours**.

| KK | Tajuk / Title | Jam / Hours |
|----|--------------|-------------|
| KK(1/4) | Identifying and Planning Computer Maintenance Requirements | 12.0 |
| KK(2/4) | Carrying Out Scheduled Preventive Maintenance | 33.0 |
| KK(3/4) | Performing Computer Corrective Maintenance | 33.0 |
| KK(4/4) | Preparing the Computer Maintenance Report | 6.0 |
| **Jumlah / Total** | | **84.0** |

---

## Kandungan Amali / Practical Content Outline

### KK(1/4) — Identifying and Planning Computer Maintenance Requirements (12.0 hours)

Trainees practise reading and interpreting maintenance work orders, classifying tasks as preventive or corrective, preparing maintenance checklists, and selecting the correct tools and PPE before commencing any maintenance activity.

**Key practical outcomes:**
- Read a simulated work order and correctly extract asset details, reported symptoms, and priority
- Produce a written maintenance checklist categorising all required actions
- Lay out the correct tools and materials at the workstation before starting

### KK(2/4) — Carrying Out Scheduled Preventive Maintenance (33.0 hours)

Trainees perform a full preventive maintenance cycle on training workstations:

**Hardware PM tasks:**
- Power off and safely disconnect the system; apply ESD protection
- Open chassis, remove and clean all dust accumulation (CPU heatsink/fan, case vents, expansion slots) using compressed air and vacuum cleaner
- Inspect and reseat RAM modules, PCIe cards, and all internal cable connectors
- Inspect CPU thermal paste condition; clean off old compound with isopropyl alcohol; apply fresh thermal paste using correct technique (pea-size centre application)
- Clean external surfaces, keyboard, and mouse

**Software PM tasks:**
- Run Windows Update; apply all critical and recommended patches
- Update device drivers (chipset, GPU, network, audio) and BIOS/UEFI firmware where applicable
- Update antivirus definitions; run a full system scan; review and resolve any threats
- Run chkdsk /f on HDD volumes; run TRIM optimisation on SSD volumes
- Run Disk Cleanup; remove temporary files and unnecessary startup programs (msconfig / Task Manager Startup tab)
- Verify backup status; perform a test data backup to external media or network share

### KK(3/4) — Performing Computer Corrective Maintenance (33.0 hours)

Trainees diagnose and resolve pre-configured hardware and software faults on training workstations. Faults are set by the instructor prior to each session.

**Diagnostic methodology (to be applied in order):**
1. Record reported symptoms from work order
2. Check Windows Event Viewer (System and Application logs) for error events
3. Check Device Manager for warning/error flags on hardware
4. Run SMART analysis (e.g., CrystalDiskInfo) on storage drives
5. Run MemTest86 if RAM instability is suspected
6. Use substitution testing (swap suspect component) to confirm fault
7. Apply corrective action; verify resolution; update work order with root cause and action

**Common fault scenarios covered (instructor-configured):**
- System randomly restarts — root cause: overheating CPU (blocked heatsink), faulty RAM, or driver conflict
- System very slow — root cause: fragmented HDD, malware, too many startup programs, or degraded thermal paste
- Blue Screen of Death (BSOD) — read stop code (e.g., MEMORY_MANAGEMENT, IRQL_NOT_LESS_OR_EQUAL); resolve driver or hardware fault
- USB device not detected — check Device Manager; test alternate port; update USB controller driver
- No network connectivity — run ipconfig, ping loopback, ping gateway; check NIC driver and physical cable connection
- Display abnormality — check display cable seating; update GPU driver; test with alternate monitor

### KK(4/4) — Preparing the Computer Maintenance Report (6.0 hours)

Trainees complete a full maintenance report using the standard form following each KK(2/4) and KK(3/4) session. Emphasis is on professional, factual language, accurate root cause description, and correct recording of all actions and test results.

**Report sections trainees must complete:**
- Asset information and work order reference
- Date of maintenance and technician name
- Pre-maintenance condition (findings before work started)
- Actions taken — preventive (list each task) and corrective (root cause + action)
- Parts replaced (part name, quantity, reason)
- Post-maintenance test results (system stability, performance, no error events)
- Recommendations (next scheduled maintenance date, parts to monitor, user advisories)

---

## Kaedah Pengajaran / Teaching Method (4-Step)

### 1. PERSEDIAAN (Preparation)

| Langkah / Step | Aktiviti / Activity | Masa / Duration |
|----------------|---------------------|-----------------|
| 1.1 | Welcome trainees; take attendance and verify PPE (anti-static wrist strap) is worn | 5 min |
| 1.2 | State the practical learning objectives for the session | 5 min |
| 1.3 | Review safety rules: ESD protection, power isolation before opening chassis, compressed air usage, isopropyl alcohol handling | 5 min |
| 1.4 | Distribute the KK (Work Sheet) and explain the exercise structure and expected outcomes | 5 min |
| 1.5 | Verify all equipment, tools, and materials are available and in working order at each workstation | 5 min |

### 2. PENYAMPAIAN (Demonstration)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 2.1 | Demonstrate the practical task step-by-step as per the KK procedures, narrating each action aloud |
| 2.2 | Highlight critical safety steps: grounding procedure, compressed air distance, correct thermal paste application technique |
| 2.3 | Show correct and incorrect techniques side-by-side (e.g., correct vs. excessive thermal paste; correct vs. bent RAM reseating angle) |
| 2.4 | Demonstrate diagnostic tool usage: Event Viewer navigation, CrystalDiskInfo SMART reading, Device Manager interpretation |
| 2.5 | Answer all questions before trainees begin independent practice |

### 3. PENGGUNAAN (Practice)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 3.1 | Trainees perform the practical task at their individual workstations following the KK procedure |
| 3.2 | Instructor circulates to observe, guide, and correct technique — ensure ESD straps are worn throughout |
| 3.3 | Conduct brief oral questioning during practice to verify understanding of each step |
| 3.4 | Trainees complete the KK assessment checklist as they work, recording findings and actions taken |

### 4. PENGESAHAN (Confirmation)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 4.1 | Instructor checks each trainee's completed work against the KK assessment checklist |
| 4.2 | Verify expected outcomes are achieved (e.g., system boots cleanly, no error events in Event Viewer, maintenance report fully completed) |
| 4.3 | Provide individual feedback on process, output, attitude, safety, and workspace cleanliness |
| 4.4 | Trainees power off systems, clean and return all tools and materials to designated storage |
| 4.5 | Record session completion and any safety or quality issues observed |

---

## Peralatan dan Bahan / Equipment and Materials

| Item | Quantity per Trainee | Notes |
|------|---------------------|-------|
| Desktop PC workstation (training unit) | 1 | Reusable; instructor pre-configures faults for KK3 sessions |
| Screwdriver set (Phillips, flat) | 1 | For opening chassis and reseating components |
| Anti-static wrist strap | 1 | MUST be worn during all hardware handling |
| Anti-static mat | 1 | Grounded work surface |
| Compressed air canister | 1 (shared per bench) | For dust removal; use in ventilated area |
| Vacuum cleaner (ESD-safe) | 1 (shared) | For dust removal from chassis interior |
| Isopropyl alcohol (IPA 99%) and lint-free wipes | 1 set (shared) | For cleaning old thermal paste from CPU and heatsink |
| Thermal paste (new) | 1 tube (shared) | For CPU thermal interface replacement |
| USB bootable diagnostic media | 1 | Loaded with MemTest86, HDD diagnostic tools |
| Maintenance form set | 1 per trainee | Computer Service Request Form + Maintenance Report template |
| Label maker or adhesive tags | 1 (shared) | For cable labelling during cable management tasks |
| Multimeter | 1 (shared) | For checking PSU rail voltages if power fault suspected |

---

## Keselamatan / Safety Requirements

- Anti-static wrist strap MUST be worn when handling any internal computer component (RAM, PCIe cards, CPU, motherboard)
- Power must be fully disconnected (power button held 5 seconds, power cable removed) before opening chassis or handling internal components
- Compressed air must be used in a well-ventilated area; hold cans upright to prevent liquid propellant discharge; wear eye protection
- Isopropyl alcohol must be used in ventilated conditions; keep away from open flames; allow surfaces to dry completely before reassembly
- Thermal paste must be applied in correct quantity (pea-size) — excess can cause short circuits on adjacent components
- Cables must be routed and secured to avoid fan obstruction and tripping hazards
- Electronic waste (damaged components, used wipes, packaging) must be disposed of through authorised e-waste or recycling channels

---

## Penilaian Amali / Practical Assessment

Upon completion of all 4 KK sessions, trainees will sit for the Performance Assessment (PA):

- **Code:** IT-020-3:2013-C02/PA
- **Minimum duration:** 3 hours 20 minutes
- **Format:** Practical task — full maintenance cycle (requirement identification → preventive maintenance → corrective maintenance → maintenance report) on a pre-configured workstation
- **Assessment criteria:** Work Activity performance (WA1–WA4), attitude, safety compliance, and environmental responsibility