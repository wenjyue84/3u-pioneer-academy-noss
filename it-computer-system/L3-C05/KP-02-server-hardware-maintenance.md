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

## KERTAS PENERANGAN

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-3:2013 OPERASI SISTEM KOMPUTER |
| TAHAP | 3 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C05 SERVER MAINTENANCE |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE SERVER MAINTENANCE JOB ORDER<br>2. CARRY OUT HARDWARE MAINTENANCE<br>3. PERFORM SERVER OPERATING SYSTEM MAINTENANCE<br>4. PREPARE SERVER MAINTENANCE RECORD |
| NO. KOD | IT-020-3:2013-C05/KP(2/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-02-server-hardware-maintenance

**TUJUAN:** Kertas rujukan untuk KP-02-server-hardware-maintenance.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Describe the components of a server that require regular hardware maintenance
2. Perform preventive hardware maintenance tasks including cleaning, thermal management, and component inspection
3. Carry out corrective hardware maintenance including component replacement and cable management
4. Manage firmware and BIOS/UEFI updates following safe update procedures
5. Assess and maintain RAID array health, including rebuilding a degraded array
6. Verify server hardware health using built-in management tools and POST diagnostics
7. Apply ESD safety procedures and data protection measures throughout all hardware maintenance activities

---

## 1.0 Introduction to Server Hardware Maintenance

Server hardware maintenance (penyelenggaraan perkakasan pelayan) encompasses all physical activities performed on a server to ensure its components remain in optimal working condition. Unlike a desktop PC, a server operates continuously — often 24 hours a day, 7 days a week — and supports multiple users and critical business services simultaneously. Hardware failure on a server can cause widespread service disruption, data loss, and financial impact.

Hardware maintenance is divided into two categories:

- **Preventive maintenance (PM) / Penyelenggaraan pencegahan:** Scheduled, routine tasks that reduce the probability of failure. Examples include cleaning dust filters, verifying RAID health, and inspecting cable integrity.
- **Corrective maintenance (CM) / Penyelenggaraan pembetulan:** Reactive tasks performed after a fault has been detected. Examples include replacing a failed hard disk drive, re-seating a memory module, or swapping a faulty power supply unit.

Both categories require the same level of care and documentation.

---

## 2.0 Server Hardware Components and Maintenance Scope

The following table lists key server hardware components and their maintenance requirements:

| Component | Komponen | PM Tasks | CM Tasks |
|-----------|----------|----------|----------|
| Processor (CPU) | Pemproses | Inspect heatsink seating; verify thermal compound; check fan speed via IPMI | Replace thermal paste if dried/cracked; reseat heatsink; replace faulty CPU fan |
| Random Access Memory (RAM) | Memori Akses Rawak | Inspect module seating; check error logs for ECC corrections | Reseat or replace faulty DIMM; verify replacement with POST |
| Hard Disk Drive / SSD | Pemacu Cakera Keras / Pemacu Keadaan Pepejal | Check S.M.A.R.T. status; monitor reallocated sectors; verify RAID status | Replace failed drive; initiate RAID rebuild; verify array integrity |
| RAID Controller | Pengawal RAID | Verify cache battery (BBU) health; update firmware | Replace failed RAID controller card; restore RAID configuration |
| Power Supply Unit (PSU) | Unit Bekalan Kuasa | Inspect for dust buildup; verify fan operation; check voltage output via IPMI | Replace faulty PSU (hot-swap if supported); verify power rail readings |
| Cooling System | Sistem Penyejukan | Clean dust filters; verify fan RPM via IPMI/BMC; check airflow direction | Replace failed fan module; clean heat exchanger fins; verify ambient temperature |
| Motherboard (System Board) | Papan Induk | Inspect capacitors for swelling; check CMOS battery voltage | Replace swollen/leaking capacitors (depot repair); replace CMOS battery |
| Network Interface Card (NIC) | Kad Antara Muka Rangkaian | Inspect cable connections; check link status LEDs; verify NIC firmware version | Replace faulty NIC; update NIC firmware/drivers |
| Fibre Channel / SAS HBA | — | Check cable integrity; verify HBA firmware version | Replace faulty HBA; reconfigure SAN zoning after replacement |
| Cables and Connectors | Kabel dan Penyambung | Inspect for wear, kinking, or loose seating; check cable labels | Replace damaged cables; re-label and redress cable management |
| Server Chassis / Rack | Sasis Pelayan / Rak | Inspect rack rails for proper seating; check chassis screws and panels | Tighten loose fasteners; replace damaged rack rails or blanking panels |
| UPS (Uninterruptible Power Supply) | Bekalan Kuasa Tidak Terganggu | Test battery runtime; verify bypass circuit; check event log | Replace aging batteries; test automatic transfer switch |

---

## 3.0 Preventive Hardware Maintenance Procedures

### 3.1 Safety Preparation

Before commencing any hardware maintenance:

1. Review and accept the approved job order.
2. Confirm a current, verified backup exists for the server.
3. Notify affected users and obtain downtime approval from the service owner.
4. Wear an anti-static wrist strap (gelang anti-statik) at all times when handling internal components.
5. Work on an anti-static mat where possible.
6. For PSU or UPS work: isolate power and apply Lockout/Tagout (LOTO) procedure.

### 3.2 Dust Cleaning and Filter Maintenance

Dust accumulation is the leading cause of overheating in servers. Overheating reduces component lifespan and can trigger emergency shutdowns.

**Procedure:**

1. Power down the server following the correct shutdown sequence (graceful OS shutdown, then physical power-off). For hot-swap PM on a running system, do not remove active drives or core components.
2. Remove the server from the rack if required by the maintenance scope.
3. Use an ESD-safe vacuum or compressed air (held 15 cm from components) to remove dust from:
   - Air intake and exhaust vents
   - Fan blades and fan housing
   - Heatsink fins (CPU and chipset)
   - Dust filters (remove, wash with water, allow to dry completely before reinstalling)
   - PSU vents
4. Do not use compressed air to spin fan bearings at excessive speed — this can damage bearings.
5. Reinstall all panels and filters before restoring power.
6. After power-on, verify fan RPM and CPU temperature via IPMI/BMC console.

### 3.3 Thermal Paste (Thermal Interface Material) Inspection and Replacement

Thermal paste (pes haba) transfers heat from the CPU die to the heatsink. It degrades over time and must be replaced every 2–3 years or when CPU temperatures are abnormally high.

**Procedure:**

1. Power down the server; apply ESD precautions.
2. Remove the heatsink retention screws in a cross-pattern to apply even pressure.
3. Lift the heatsink carefully. If it is stuck, apply gentle lateral force — do not pry.
4. Remove the old thermal paste from the CPU IHS (Integrated Heat Spreader) and heatsink base using isopropyl alcohol (≥90%) and a lint-free cloth. Do not allow alcohol to contact the CPU socket or motherboard.
5. Apply a pea-sized amount of fresh thermal paste to the centre of the CPU IHS.
6. Reinstall the heatsink and tighten retention screws in a cross-pattern to the manufacturer's specified torque.
7. Power on and verify CPU temperature has returned to the normal range.

### 3.4 Component Inspection

During each PM cycle, physically inspect the following:

| Item | What to Look For |
|------|-----------------|
| RAM modules | Proper seating in slot; no burn marks or corrosion on gold contacts |
| Capacitors on system board | Bulging tops or leaked electrolyte around the base — these indicate imminent failure |
| CMOS battery | Check voltage with a multimeter; replace if below 2.8 V (nominal 3.0 V CR2032) |
| Cable connections | All data and power cables fully seated; no fraying, kinking, or damaged connectors |
| Drive indicator LEDs | All drives show solid green (healthy); amber indicates a fault requiring immediate attention |
| PSU indicator LEDs | Green = normal; amber or red = fault — check PSU event log |
| Rack blanking panels | All empty rack units must have blanking panels installed to maintain proper airflow |

---

## 4.0 RAID Array Health and Maintenance

### 4.1 What is RAID?

RAID (Redundant Array of Independent Disks / Tatasusunan Cakera Bebas Berlebihan) combines multiple physical drives into a logical volume that provides improved performance, fault tolerance, or both, depending on the RAID level configured.

### 4.2 Common RAID Levels in Server Environments

| RAID Level | Minimum Drives | Fault Tolerance | Typical Use Case |
|------------|----------------|-----------------|-----------------|
| RAID 1 (Mirroring) | 2 | 1 drive failure | OS volume; critical small databases |
| RAID 5 (Striping with parity) | 3 | 1 drive failure | General-purpose file and application servers |
| RAID 6 (Dual parity) | 4 | 2 drive failures | High-availability environments requiring extended rebuild windows |
| RAID 10 (Mirrored stripes) | 4 | 1 drive per mirrored pair | High I/O databases; virtualisation hosts |

### 4.3 Checking RAID Array Health

The method for checking RAID health depends on the controller type:

| Controller Type | Tool / Interface | Healthy Status Indicator |
|-----------------|------------------|--------------------------|
| Hardware RAID controller (e.g. HPE Smart Array, Dell PERC) | Vendor management utility (e.g. HPE SSA, OMSA), BIOS RAID utility, IPMI/iDRAC | "Optimal" or "Online" |
| Software RAID (Linux mdadm) | `cat /proc/mdstat` or `mdadm --detail /dev/md0` | "active" with all drives "[UUU]" (U = Up) |
| Windows Storage Spaces | Server Manager → File and Storage Services → Storage Pools | "OK" with no warnings |

RAID health checks must be performed at every PM cycle and after any corrective maintenance involving drive replacement.

### 4.4 Responding to a Degraded RAID Array

A degraded array means one or more drives have failed or been removed. The array is still functional but has no fault tolerance — a second failure will cause data loss. A degraded array is a **High priority** corrective maintenance event.

**Procedure for replacing a failed drive and initiating RAID rebuild:**

1. Identify the failed drive using the RAID management utility or drive LED indicators (typically solid amber on the failed drive).
2. Confirm the replacement drive is the correct model, interface (SAS/SATA/NVMe), and capacity (must be equal to or larger than the failed drive).
3. If the server supports **hot-swap** (penukar panas): remove the failed drive carrier and insert the replacement without powering down the server. The RAID controller will automatically detect the new drive.
4. If the server does **not** support hot-swap: schedule a maintenance window, power down, replace the drive, power up.
5. Using the RAID management utility, initiate a rebuild (pembinaan semula) on the replacement drive.
6. Monitor rebuild progress. Do not power down the server during rebuild unless there is an emergency — an interrupted rebuild may require a full rebuild restart.
7. After rebuild completion, verify the array status returns to "Optimal" or "Online".
8. Document the replaced drive's serial number, date, and rebuild completion time in the maintenance record.

**Estimated rebuild times (approximate):**

| Drive Capacity | Estimated Rebuild Time (RAID 5, single drive) |
|---------------|-----------------------------------------------|
| 1 TB HDD | 3–5 hours |
| 4 TB HDD | 12–20 hours |
| 1 TB SSD | 30–60 minutes |

Do not perform other intensive I/O operations on the server during a RAID rebuild — this extends rebuild time and increases the risk of a second drive failure.

---

## 5.0 Firmware and BIOS/UEFI Management

### 5.1 What is Firmware?

Firmware (perisian tegar) is low-level software stored in non-volatile memory (ROM/Flash) on hardware components. It initialises hardware during boot and provides the interface between the operating system and physical components. Firmware is distinct from the operating system — it exists below the OS level.

Key firmware components in a server:

| Component | Firmware Type | Function |
|-----------|--------------|----------|
| System board | BIOS / UEFI | Hardware initialisation (POST); boot device selection; hardware configuration |
| RAID controller | Controller firmware | Manages disk I/O, RAID logic, cache policy |
| Network Interface Card | NIC firmware | Controls network offload functions; PXE boot |
| Hard Disk Drive / SSD | Drive firmware | Controls internal drive operations; S.M.A.R.T. reporting |
| Baseboard Management Controller (BMC) | BMC firmware (e.g. iDRAC, iLO, IPMI) | Out-of-band server management; remote console; hardware monitoring |
| UPS | UPS firmware | Controls battery management and automatic transfer switch |

### 5.2 Why Firmware Updates Are Necessary

Firmware updates (kemaskini perisian tegar) are performed to:

- Fix security vulnerabilities (e.g. Spectre/Meltdown CPU microcode updates)
- Improve hardware compatibility with new operating systems or components
- Resolve known bugs that cause instability or data corruption
- Add new features or management capabilities
- Maintain vendor support and compliance

Firmware updates should be applied when:
- A new security advisory or CVE is published that affects the firmware version in use
- Vendor releases a "critical" or "recommended" update
- A hardware issue is being investigated and the vendor recommends a firmware update as part of diagnosis

### 5.3 BIOS/UEFI Settings Relevant to Server Maintenance

The following BIOS/UEFI settings are commonly reviewed during server hardware maintenance:

| Setting | Purpose | Typical Server Value |
|---------|---------|----------------------|
| Boot order (Urutan but) | Defines the sequence of boot devices | Set to boot from OS drive first; disable unused boot devices |
| Secure Boot | Prevents loading of unsigned boot loaders | Enabled on production servers (if OS supports it) |
| Hyper-Threading | Enables logical CPU cores (Intel) or SMT (AMD) | Enabled (improves virtualisation and multithreaded workload performance) |
| Power management profile | Controls CPU power states (C-states, P-states) | "Maximum Performance" for latency-sensitive workloads; "Balanced" for general use |
| Turbo Boost / Precision Boost | Allows CPU to exceed base clock speed | Enabled unless thermal constraints exist |
| Memory speed and timing | RAM frequency and latency configuration | Set to maximum rated speed supported by the installed modules |
| IPMI/BMC access | Out-of-band management access | Enabled; assign a dedicated management IP address |
| Hardware prefetcher | CPU cache prefetch optimisation | Enabled (default); disable only for specific workloads as directed by vendor |

**Before modifying any BIOS/UEFI setting:** document the current value and obtain change approval through the change management process.

### 5.4 Firmware Update Procedure

Firmware updates carry a risk of rendering the server unbootable if the update process is interrupted. Follow this procedure strictly:

1. **Identify current firmware versions.** Record the current BIOS/UEFI version, RAID controller firmware version, BMC/IPMI firmware version, and NIC firmware version.
2. **Download updates from the official vendor website only.** Do not use third-party firmware packages. Verify the checksum (MD5/SHA256) of the downloaded file.
3. **Review the firmware release notes.** Check for known issues, prerequisites (e.g. must be at version X before upgrading to version Y), and any required intermediate steps.
4. **Confirm a full backup is available** and the backup has been verified (tested restore).
5. **Schedule a maintenance window.** Most firmware updates require a server restart. Notify affected users.
6. **Perform the update using the vendor's recommended tool:**
   - HPE servers: SPP (Service Pack for ProLiant), iLO interface, or SUM (Smart Update Manager)
   - Dell servers: iDRAC Lifecycle Controller, OMSA, or DSU (Dell System Update)
   - Supermicro/generic servers: Web-based BMC interface or vendor utility
7. **Do not interrupt power or reset the server** during the update process. If possible, connect the server to a UPS before beginning.
8. **Verify the update after restart.** Confirm the new firmware version is reported in BIOS/UEFI and the management utility.
9. **Test server functionality.** Verify all services start correctly, RAID array is optimal, and network connectivity is restored.
10. **Document the update** in the maintenance record: previous version, new version, update tool used, date, technician name.

### 5.5 Firmware Update Failure — Recovery Steps

| Scenario | Recovery Action |
|----------|-----------------|
| Server does not POST after BIOS update | Use vendor BIOS recovery mode (e.g. dual BIOS chip, USB recovery image) |
| RAID controller firmware update failed | Boot from vendor rescue media; reflash controller firmware via command line |
| BMC/IPMI unresponsive after update | Perform BMC cold reset via physical jumper or vendor recovery utility |
| NIC firmware update failed | Replace NIC with a spare; update firmware on the bench before reinstalling |

---

## 6.0 Power Supply and UPS Maintenance

### 6.1 Power Supply Unit (PSU) Maintenance

Enterprise servers typically use hot-swap, redundant PSUs (usually N+1 configuration). This allows one PSU to be replaced while the server continues running on the remaining unit.

**Preventive maintenance tasks:**
- Inspect PSU vents for dust buildup; clean with compressed air.
- Verify PSU fan is spinning and not making abnormal noise.
- Check PSU output voltages via IPMI/BMC (typically +12V, +5V, +3.3V rails).
- Confirm both PSUs in a redundant pair are load-sharing (indicated by management console).

**Corrective maintenance — hot-swap PSU replacement:**
1. Identify the faulty PSU by the amber fault LED on the PSU module.
2. Confirm the remaining PSU(s) can carry the full server load (check power draw via IPMI).
3. Unlatch and slide out the faulty PSU module.
4. Insert the replacement PSU module until it latches. The server management system should automatically detect the new PSU and begin load sharing.
5. Verify the new PSU shows green status in the management console.
6. Document the replacement.

### 6.2 UPS (Uninterruptible Power Supply) Maintenance

A UPS protects the server against power outages, voltage sags, and surges. The UPS battery must be regularly tested and replaced before it degrades below its rated capacity.

| Task | Frequency | Procedure |
|------|-----------|-----------|
| Battery runtime test | Every 6 months | Initiate a self-test from the UPS management interface; verify runtime meets the minimum SLA requirement |
| Visual inspection | Monthly | Check for battery case swelling, electrolyte leakage, or corrosion on terminals |
| Battery replacement | Every 3–5 years (or when runtime drops below 80% of rated) | Replace battery cartridges per manufacturer procedure; dispose of old batteries as hazardous waste |
| Bypass circuit test | Annually | Verify the UPS can transfer load to bypass without interruption |
| Firmware update | Per vendor advisory | Update UPS firmware via management interface |

---

## 7.0 Cable Management

Proper cable management in a server rack ensures good airflow, reduces the risk of accidental disconnection, and simplifies troubleshooting. Cable management tasks include:

- **Labelling:** All cables must be labelled at both ends with a consistent naming convention (e.g. `SRV01-HBA1-PORT1 → SAN-SW01-P12`).
- **Routing:** Power cables and data cables should be routed separately to reduce electromagnetic interference (EMI).
- **Securing:** Use hook-and-loop (Velcro) ties — not zip ties — for cables that may need to be rerouted. Zip ties can damage cables if overtightened.
- **Slack management:** Maintain adequate cable slack to allow components to be slid out of the rack for maintenance without disconnecting cables.
- **Inspection:** Check for kinked, damaged, or unlabelled cables during every PM cycle. Replace immediately.

---

## 8.0 Post-Maintenance Verification

After completing hardware maintenance tasks, the technician must verify the server has returned to full operational status before closing the job order:

| Verification Step | Method |
|-------------------|--------|
| POST completion | Server boots without errors; no beep codes or POST error messages |
| OS boot | Operating system loads fully; no crash or driver error at startup |
| RAID array status | All arrays show "Optimal" or equivalent healthy status |
| Fan and temperature | All fans report normal RPM; CPU and system temperatures within operating range |
| Power supply status | All PSUs show green status; output voltages within specification |
| Network connectivity | Server responds to ping on all configured network interfaces |
| Service availability | All intended services (e.g. web server, database, file shares) are running and accessible |
| Event log review | No new critical or error events in the system event log (SEL) after maintenance |

---

## 9.0 Common Errors in Server Hardware Maintenance

| Error | Ralat | Consequence | Prevention |
|-------|-------|-------------|------------|
| Not wearing ESD strap | Tidak memakai gelang anti-statik | Static discharge damages RAM, CPU, or system board | Always wear ESD strap when handling internal components |
| Performing maintenance without a backup | Menjalankan penyelenggaraan tanpa sandaran | Data loss if a fault occurs during maintenance | Verify backup before starting; do not proceed without confirmed backup |
| Interrupting a firmware update | Mengganggu kemaskini perisian tegar | Server may become unbootable | Never remove power or reset the server during a firmware flash |
| Not monitoring RAID rebuild | Tidak memantau pembinaan semula RAID | Second drive failure during rebuild causes data loss | Monitor rebuild progress; defer non-critical I/O operations |
| Overtightening screws | Mengetatkan skru terlalu ketat | Cracked PCB, stripped threads, or damaged heatsink | Use torque driver; follow manufacturer specifications |
| Using wrong replacement part | Menggunakan alat ganti yang salah | Component incompatibility; system instability | Verify part number, interface, and speed rating before installation |
| Not documenting changes | Tidak mendokumentasikan perubahan | Audit failures; difficulty in future troubleshooting | Complete maintenance record immediately after each task |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCU 5: Server Maintenance
- CompTIA Server+ Certification Study Guide — Chapters: Hardware Maintenance, Storage, Power
- HPE ProLiant Gen10 Server Maintenance and Service Guide
- Dell EMC PowerEdge Servers — Hardware Owner's Manual
- Intel Server Products — BIOS and Firmware Update Procedures
- ITIL Foundation — Problem Management and Change Management
- Organisational IT Maintenance Policy and Change Management Procedure