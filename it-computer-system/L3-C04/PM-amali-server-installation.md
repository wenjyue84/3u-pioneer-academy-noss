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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C04 SERVER INSTALLATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE JOB ORDER/CHANGE REQUEST<br>2. EXECUTE HARDWARE INSTALLATION<br>3. CARRY OUT SOFTWARE INSTALLATION<br>4. PERFORM SERVER FUNCTIONALITY TEST<br>5. PREPARE SERVER INSTALLATION SET-UP REPORT |
| NO. KOD | IT-020-3:2013-C04/PM(AMALI) |
| Muka Surat | 1/1 |
| WARNA KERTAS | KUNING (Yellow) |

**TAJUK:** PM-amali-server-installation

**TUJUAN:** Kertas rujukan untuk PM-amali-server-installation.

**TEMPAT:** BILIK AMALI / MAKMAL

**TEMPOH:** Rujuk JPW/RK.

**TUJUAN PENGAJARAN:** Pada akhir sesi pengajaran, pelatih akan dapat menguasai pengetahuan/kemahiran berkaitan aktiviti kerja CU ini.

**ALAT BANTUAN MENGAJAR:** Papan putih, projektor, slaid pengajaran, bahan tunjuk-cara.

<!-- /JPK_ENVELOPE_v1 -->
**TUJUAN:** Upon completion of all 5 KK sessions, trainees will sit for the Performance Assessment (PA): IT-020-3:2013-C04/PA.

**TEMPAT:** BILIK AMALI / MAKMAL RANGKAIAN

**TEMPOH:** Rujuk JPW/RK. Jumlah jam amali: 168 jam (70% daripada 240 jam CoCU 4).

**TUJUAN PENGAJARAN:** Pada akhir sesi amali, pelatih akan dapat melaksanakan pemasangan pelayan secara menyeluruh merangkumi pemasangan perkakasan dalam rak, konfigurasi RAID, pemasangan sistem operasi pelayan, pengujian fungsi, dan penyediaan laporan pemasangan.

**ALAT BANTUAN MENGAJAR:** Papan putih, projektor, slaid tunjuk-cara, peralatan sebenar pelayan, rak 19-inci, kit pemasangan rel, pemacu kilat USB berboot.

---

## Agihan Masa Amali / Practical Time Allocation

| KK | Tajuk / Title | Jam / Hours |
|----|--------------|-------------|
| KK(1/5) | Analysing Job Order and Planning Server Installation | 25.2 |
| KK(2/5) | Server Hardware Installation and Rack Mounting | 67.2 |
| KK(3/5) | Server Operating System and Software Installation | 50.4 |
| KK(4/5) | Server Functionality Testing and Verification | 16.8 |
| KK(5/5) | Server Installation Report Preparation and Handover | 8.4 |
| **Jumlah / Total** | | **168.0** |

---

## Huraian Aktiviti Amali / Practical Activity Description

### KK(1/5) — Analysing Job Order and Planning Server Installation (25.2 hours)

**Objektif:** Trainees can interpret a server installation job order, verify hardware specifications, plan rack space, and complete a pre-installation checklist.

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 1 | Read and interpret the simulated job order — identify server model, CPU, RAM, storage, RAID level, OS, and network requirements |
| 2 | Perform hardware compatibility check using vendor compatibility matrix |
| 3 | Measure rack unit availability; determine target U-position; check PDU capacity |
| 4 | Inspect all hardware boxes — verify against packing list; record serial numbers |
| 5 | Complete the pre-installation checklist form and submit to instructor for verification |

**Hasil yang Dijangkakan / Expected Outcome:** Completed pre-installation checklist with all fields filled accurately; instructor sign-off before proceeding to hardware installation.

---

### KK(2/5) — Server Hardware Installation and Rack Mounting (67.2 hours)

**Objektif:** Trainees can safely rack a server, install CPUs, ECC RAM, storage drives, and configure RAID using the controller utility.

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 1 | Don anti-static wrist strap; verify strap continuity with tester |
| 2 | Install rack rail kit — align rail brackets to correct U-position; secure with cage nuts and rail screws |
| 3 | Open server chassis; remove top cover using correct tool |
| 4 | Install CPU(s) — align triangle marker; lower CPU into socket; engage retention lever |
| 5 | Apply thermal interface material — correct quantity (pea-sized or thin even layer as per OEM guidance) |
| 6 | Mount CPU heatsink/cooler — tighten captive screws in cross pattern to correct torque |
| 7 | Install ECC RAM modules — match DIMM population rules per platform; press until clips engage |
| 8 | Install storage drives into hot-swap bays — align drive tray; slide until latched |
| 9 | Access RAID controller BIOS utility (Ctrl+C or F key as applicable); create RAID virtual disk; verify array initialises |
| 10 | Connect power cables (CPU power, DIMM power if applicable, drive backplane) |
| 11 | Route and manage cables — use tie wraps and cable arm to prevent fan obstruction |
| 12 | Replace top cover; slide server onto rack rails; secure with rack screws |
| 13 | Connect PDU power cable(s); connect network cable to management (ILO/iDRAC) port and data NIC port |
| 14 | Power on server; verify fans spin, power LED green, POST initiates |

**Hasil yang Dijangkakan / Expected Outcome:** Server is racked, powered on, and passes POST with all hardware detected. RAID virtual disk created and initialising.

---

### KK(3/5) — Server Operating System and Software Installation (50.4 hours)

**Objektif:** Trainees can configure BIOS/UEFI, install a server OS, install drivers in the correct order, configure server roles, and set a static IP address.

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 1 | Access BIOS/UEFI setup; configure boot order (USB first, then RAID volume); enable Intel VT-x / AMD-V; set RAID mode; verify date and time |
| 2 | Insert bootable USB OS installer; boot from USB |
| 3 | Select language, keyboard layout, and installation type (Clean Install) |
| 4 | Select RAID virtual disk as installation target; create OS partition and data partition as per job order |
| 5 | Complete OS installation; system reboots to first-boot configuration screen |
| 6 | Complete initial server configuration: administrator password, computer name, workgroup/domain |
| 7 | Install drivers in correct sequence: RAID/storage controller → chipset → NIC → out-of-band management agent (iLO/iDRAC) |
| 8 | Verify all devices shown without errors in Device Manager (Windows) or via `lspci -v` (Linux) |
| 9 | Configure static IP address, subnet mask, default gateway, and DNS as per job order |
| 10 | Install and configure assigned server role (e.g. File and Storage Services via Server Manager; or `samba` package via apt/yum) |
| 11 | Configure out-of-band management interface — assign dedicated IP; set credentials; test web console login |
| 12 | Run Windows Update / `apt upgrade` to apply OS patches |

**Hasil yang Dijangkakan / Expected Outcome:** Server OS installed and updated; all drivers loaded; server role active; static IP assigned; remote management accessible.

---

### KK(4/5) — Server Functionality Testing and Verification (16.8 hours)

**Objektif:** Trainees can systematically test all hardware and software components of the installed server and record results on a test checklist.

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 1 | Open Device Manager (Windows) / run `lshw -short` (Linux) — verify all CPUs, RAM, NICs, and storage controller listed without errors |
| 2 | Open RAID management utility — confirm RAID virtual disk status is "Optimal"; record drive health indicators |
| 3 | Run `ipconfig /all` (Windows) or `ip addr` (Linux) — verify IP, subnet, gateway, and DNS match job order |
| 4 | Run `ping <gateway>` and `ping <external host>` — verify successful replies; record latency |
| 5 | Test server role from a client machine — map a network share drive; verify read/write access |
| 6 | Log in to ILO/iDRAC web console — verify temperature sensors, fan speeds, and power readings are within normal range |
| 7 | Record all test results on the server functionality test checklist form |
| 8 | Identify and resolve any failed test items; re-test after remediation |

**Hasil yang Dijangkakan / Expected Outcome:** All test items pass; test checklist completed with pass/fail results and remarks; no unresolved hardware or software faults.

---

### KK(5/5) — Server Installation Report Preparation and Handover (8.4 hours)

**Objektif:** Trainees can prepare a complete and accurate server installation set-up report and present it to the assessor/requestor for sign-off.

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 1 | Complete the set-up report form — record: job order reference, server make/model/serial number, CPU model and quantity, RAM size and configuration, RAID level and drive details, OS version and edition, IP address, driver versions, server role, and test results |
| 2 | Document any deviations from the original job order — state what was substituted, reason, and approval obtained |
| 3 | Attach the completed functionality test checklist to the report |
| 4 | Present report to assessor verbally — explain installation decisions, any issues encountered, and how they were resolved |
| 5 | Obtain assessor/requestor signature on the set-up report |
| 6 | Clean workstation, return tools to storage, dispose of packaging in designated waste bins |

**Hasil yang Dijangkakan / Expected Outcome:** Complete, accurate set-up report submitted; assessor sign-off obtained; workstation cleaned.

---

## Kaedah Pengajaran / Teaching Method (4-Step)

### 1. PERSEDIAAN (Preparation)

| Langkah / Step | Aktiviti / Activity | Masa / Duration |
|----------------|---------------------|-----------------|
| 1.1 | Welcome trainees; take attendance and verify PPE (anti-static strap, safety shoes where applicable) | 5 min |
| 1.2 | State the practical learning objectives for the session | 5 min |
| 1.3 | Review safety rules: ESD protection, rack safety (two-person lift for heavy servers), electrical isolation before opening chassis | 5 min |
| 1.4 | Distribute the KK (Work Sheet) and explain the exercise structure and expected outcome | 5 min |
| 1.5 | Verify all equipment and materials are available at each workstation; confirm server is powered off before commencing | 5 min |

### 2. PENYAMPAIAN (Demonstration)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 2.1 | Demonstrate the practical task step-by-step as per the KK procedures at the instructor demonstration station |
| 2.2 | Highlight critical safety steps: ESD strap verification; two-person rack lift; correct torque for rack screws; CPU retention lever engagement |
| 2.3 | Demonstrate correct and incorrect techniques side-by-side (e.g. correct vs excess thermal paste; correct vs wrong DIMM slot population) |
| 2.4 | Show RAID controller BIOS navigation and virtual disk creation on projector screen |
| 2.5 | Answer questions from trainees before they commence their own work |

### 3. PENGGUNAAN (Practice)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 3.1 | Trainees perform the practical task at their individual workstations following the KK procedure |
| 3.2 | Instructor circulates to observe, guide, and correct technique — particular attention to ESD handling and cable management |
| 3.3 | Conduct brief oral questioning during practice to verify understanding (e.g. "Why do you install the RAID driver before the OS?") |
| 3.4 | Trainees complete the KK assessment checklist as they work through each step |

### 4. PENGESAHAN (Confirmation)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 4.1 | Instructor checks each trainee's completed work against the assessment checklist |
| 4.2 | Verify the expected outcome is achieved — server operational, RAID status optimal, OS installed, functionality test passed, report complete |
| 4.3 | Provide feedback on process, output, attitude, safety, and workspace cleanliness |
| 4.4 | Trainees power down server safely, disconnect cables, return tools and materials to storage |
| 4.5 | Record session completion and any issues requiring remediation |

---

## Peralatan dan Bahan / Equipment and Materials

| Item | Kuantiti per Pelatih / Qty per Trainee | Nota / Notes |
|------|----------------------------------------|--------------|
| Rack-mount server chassis (1U or 2U) | 1 | Reusable training unit |
| Server rail kit | 1 set | Must match chassis model |
| Server-grade motherboard | 1 | Compatible with provided CPU |
| Server CPU with heatsink | 1 (minimum) | Matching socket type |
| ECC RAM modules | 2–4 | As per platform population rules |
| Storage drives (SAS or SATA) | 2 minimum | For RAID 1 configuration |
| RAID controller card (if no onboard RAID) | 1 | Optional if platform supports it |
| Server power supply unit (PSU) | 1–2 | Redundant PSU preferred |
| Network switch port | 1 | Pre-configured VLAN |
| 19-inch training rack (shared) | 1 per bay | Minimum 12U; earthed |
| Cage nuts and rack screws | 1 set | M6 or M5 as applicable |
| Screwdriver set | 1 | Phillips, flat, Torx T10/T20 |
| Anti-static wrist strap | 1 | Must be worn; continuity tested before use |
| Anti-static mat | 1 | Grounded work surface |
| Multimeter | 1 (shared) | PSU voltage verification |
| USB bootable media (server OS installer) | 1 | Licensed OS image |
| Thermal interface material | 1 tube (shared) | Apply as per OEM specification |
| Cable ties and velcro straps | 1 bag (shared) | Cable management |
| Server installation set-up report template | 1 | Printed form |
| Functionality test checklist | 1 | Printed form |

---

## Keselamatan / Safety Requirements

- Anti-static wrist strap MUST be worn and continuity tested before handling any server components (motherboard, CPU, RAM, PCIe cards)
- Power MUST be disconnected and PDU circuit breaker OFF before opening the server chassis or handling internal components
- Servers exceeding 15 kg must be racked using a two-person lift or a server lift tool — do not rack heavy servers alone
- Thermal interface material must be applied in the correct quantity — excess paste can migrate onto the socket and cause shorts
- All cables must be routed through cable management arms and trays to avoid obstruction of hot-swap bays and airflow paths
- E-waste (damaged drives, packaging materials) must be segregated and disposed of through authorised recycling channels

---

## Penilaian Amali / Practical Assessment

Upon completion of all 5 KK sessions, trainees will sit for the Performance Assessment (PA):

- **Code:** IT-020-3:2013-C04/PA
- **Minimum duration:** 4 hours
- **Format:** Practical task — complete server installation from job order to set-up report sign-off
- **Assessment criteria:** Per-WA observable criteria (Process, Output, Safety & Attitude) as per PA rubric
- **Pass mark:** 60 out of 100 (Competent); below 60 = Not Yet Competent (NYC)