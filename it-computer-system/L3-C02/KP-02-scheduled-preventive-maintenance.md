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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C02 COMPUTER SYSTEM MAINTENANCE |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. IDENTIFY COMPUTER MAINTENANCE REQUIREMENTS<br>2. CARRY OUT COMPUTER SCHEDULED PREVENTIVE MAINTENANCE<br>3. PERFORM COMPUTER CORRECTIVE MAINTENANCE<br>4. PREPARE COMPUTER MAINTENANCE REPORT |
| NO. KOD | IT-020-3:2013-C02/KP(2/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-02-scheduled-preventive-maintenance

**TUJUAN:** Kertas rujukan untuk KP-02-scheduled-preventive-maintenance.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the purpose and benefits of scheduled preventive maintenance (PM) for computer systems
2. Describe the standard hardware PM procedures including cleaning, inspection, and component re-seating
3. Describe the standard software PM procedures including OS updates, driver updates, disk optimisation, and backup verification
4. Apply the correct PM schedule intervals (monthly, quarterly, annual) to appropriate tasks
5. Complete a preventive maintenance checklist accurately and legibly

---

## 1.0 Introduction to Scheduled Preventive Maintenance

Scheduled preventive maintenance (penyelenggaraan pencegahan berjadual) is a proactive, time-based activity carried out on a computer system before any fault occurs. The goal is to maintain optimal performance, extend the service life of hardware, reduce the likelihood of unexpected failure, and ensure software security and integrity.

PM is distinguished from corrective maintenance in that it is planned in advance and does not depend on a fault being present. A maintenance schedule (jadual penyelenggaraan) issued by the IT department or supervisor specifies which systems require PM, at what interval, and which tasks are to be performed.

Key benefits of scheduled PM include:

- Reduction in unplanned downtime (masa henti tidak terancang)
- Lower long-term repair costs by addressing wear before it causes failure
- Maintenance of warranty compliance for systems under manufacturer warranty
- Compliance with organisational IT governance and audit requirements

---

## 2.0 PM Schedule Intervals

Different tasks require different maintenance intervals based on the rate at which the condition deteriorates or the frequency with which software changes.

| Interval | Typical Tasks |
|----------|--------------|
| **Monthly** | Full virus and malware scan; check and apply OS security patches; review event logs for warnings; verify backup completion |
| **Quarterly** | Clean internal hardware (dust removal from fans, vents, heatsinks); check all cable connections; update drivers; apply firmware/BIOS updates where applicable; test UPS battery |
| **Annually** | Full hardware inspection; re-apply thermal paste on CPU; replace CMOS battery if voltage is low; review and update the maintenance schedule; review software licence compliance |

---

## 3.0 Hardware Preventive Maintenance Procedures

### 3.1 Preparation

Before opening the chassis:

1. Obtain the signed maintenance request form and confirm the asset tag matches the scheduled system.
2. Inform the system user that the computer will be taken offline. Agree on a time window.
3. Shut down the operating system properly. Do not power off abruptly.
4. Disconnect the power cable from the wall outlet. For tower PCs, also press the power button once after unplugging to discharge any residual capacitor charge.
5. Put on the anti-static wrist strap (tali pergelangan anti-statik) and connect the ground clip to the metal chassis.

### 3.2 External Cleaning

| Task | Method |
|------|--------|
| Wipe the monitor screen | Use a lint-free microfibre cloth slightly dampened with water or a monitor-safe cleaning solution. Never spray liquid directly onto the screen. |
| Clean the keyboard | Turn upside down and gently tap to dislodge debris. Use compressed air between keys. Wipe keycap surfaces with a cloth lightly dampened with IPA. |
| Clean the mouse | Wipe the exterior with IPA-dampened cloth. For optical mice, clean the sensor lens opening with a cotton swab. |
| Clean external chassis surfaces | Wipe with a dry or lightly dampened cloth. Do not use abrasive cleaners. |
| Check cables and connectors | Inspect all external cables (power, USB, video, network) for damage, kinking, or loose connections. Secure any loose connections. |

### 3.3 Internal Cleaning

Open the chassis side panel. Work in a well-ventilated area or use a designated dust-blowing area.

| Task | Method | Caution |
|------|--------|---------|
| Remove dust from case fans | Use short bursts of compressed air; hold the fan blade still with a finger or cable tie to prevent over-spin, which can damage the fan bearing. | Do not allow the fan to spin freely under compressed air — this generates voltage that may damage the motherboard. |
| Remove dust from CPU heatsink fins | Direct compressed air through the fins; use a soft brush for stubborn deposits. | Avoid physical pressure on the heatsink mounting clips. |
| Remove dust from PSU (Power Supply Unit) vent | Blow compressed air through the PSU exhaust vent from the outside. Do not open the PSU. | PSU capacitors retain charge even when unplugged. Never open the PSU casing. |
| Remove dust from RAM slots and expansion card areas | Use short bursts of compressed air; follow with a lint-free brush sweep. | |
| Inspect all internal cables | Check for fraying, pinching against sharp edges, or loose connectors. Re-seat any loose power or data connectors. | |
| Check expansion cards (GPU, NIC, sound card) | Verify cards are fully seated in their slots. Press firmly until the retention clip clicks. | |

### 3.4 Thermal Paste Replacement (Annual)

CPU thermal paste (pes haba) degrades over time, reducing heat transfer efficiency and causing CPU temperatures to rise. Replace annually or when CPU temperatures are consistently elevated.

**Procedure:**

1. Disconnect the CPU cooler power connector from the motherboard.
2. Unlock and remove the heatsink/cooler assembly. Some coolers use push-pins; others use screws.
3. Use a lint-free cloth or cotton swab dampened with IPA (isopropyl alcohol, 70–99%) to remove all old thermal paste from both the CPU lid (IHS) and the heatsink base. Allow to dry completely.
4. Apply a small amount of new thermal paste to the centre of the CPU lid — approximately the size of a grain of rice or a small pea. Do not spread manually; the pressure of mounting the heatsink will distribute it evenly.
5. Re-mount the heatsink, tightening screws in a cross pattern to ensure even pressure.
6. Reconnect the cooler power connector.

### 3.5 CMOS Battery Check (Annual)

The CMOS battery (bateri CMOS) is a CR2032 coin cell on the motherboard that maintains the BIOS settings and real-time clock when the system is powered off. A failing CMOS battery causes the system clock to reset and BIOS settings to revert to defaults.

- Check: If the system clock consistently resets to a default date (e.g. 1 January 2000) after power loss, the CMOS battery needs replacement.
- Replacement: Note all BIOS settings first. Remove the old battery and insert a new CR2032. Re-enter BIOS settings and set the correct date and time.

---

## 4.0 Software Preventive Maintenance Procedures

### 4.1 Operating System Updates

Keeping the operating system (sistem pengendalian) current is the single most important software PM task for security.

**Procedure (Windows):**

1. Open **Settings → Windows Update**.
2. Click **Check for Updates**.
3. Download and install all available updates, including optional driver updates if applicable.
4. Restart the system if prompted.
5. Re-check for updates after restarting — some updates only appear after a prior update is installed.

| Update Type | Priority |
|-------------|----------|
| Security updates (Kemas kini keselamatan) | Critical — install immediately |
| Cumulative updates | High — install at next scheduled PM |
| Feature updates (major OS version) | Medium — coordinate with IT manager; test on a pilot system first |
| Optional / driver updates | Low — evaluate before installing |

### 4.2 Driver and Firmware Updates

Device drivers (pemacu peranti) provide the interface between the operating system and hardware. Outdated drivers can cause instability, poor performance, or security vulnerabilities.

- **GPU drivers:** Update via the graphics card manufacturer's utility (NVIDIA GeForce Experience, AMD Radeon Software) or Device Manager.
- **Chipset and storage controller drivers:** Download from the motherboard manufacturer's support page.
- **BIOS/UEFI firmware:** Update only when the manufacturer releases a version addressing a known issue or security vulnerability. Always read the release notes before updating BIOS. A failed BIOS update can brick the motherboard.
- **Network adapter drivers:** Important for stability and security, especially on domain-joined machines.

### 4.3 Antivirus and Anti-Malware Scan

1. Verify the antivirus definition database (pangkalan data definisi) is current. Update if not.
2. Run a **Full Scan** — not a Quick Scan — as part of the scheduled PM. A full scan examines every file on all drives.
3. Review the scan results log. Quarantine or remove any detected threats.
4. Check that real-time protection (perlindungan masa nyata) is enabled and the antivirus service is running.

### 4.4 Disk Maintenance

| Task | Tool (Windows) | Notes |
|------|---------------|-------|
| Check disk for errors | `chkdsk C: /f /r` (run at next boot) or **Disk Management → Error Checking** | Checks for file system errors and bad sectors. Schedule during non-working hours as it can take hours on large drives. |
| Disk cleanup (Pembersihan cakera) | **Disk Cleanup** utility or `cleanmgr` | Removes temporary files, Windows Update cache, Recycle Bin contents. Can recover several GB on older systems. |
| Defragmentation (HDD only) | **Defragment and Optimise Drives** | Reorganises fragmented files on spinning-disk HDDs to improve read performance. **Do NOT defragment SSDs** — use the Optimise (TRIM) function instead, which is the default for SSDs in Windows. |
| S.M.A.R.T. status check | CrystalDiskInfo (free utility) or `wmic diskdrive get status` | Review reallocated sectors, pending sectors, and uncorrectable sectors counts. Any non-zero value for these attributes warrants investigation. |

### 4.5 Startup Programme Review

Over time, applications add themselves to the startup sequence, slowing boot time and consuming RAM.

1. Open **Task Manager → Startup** tab (Windows 10/11).
2. Review each enabled startup item. Disable any that are not required for business operations.
3. Do not disable antivirus, security agents, or VPN clients.

### 4.6 Backup Verification

Backups are only valuable if they can be restored. During PM, verify that the most recent backup completed successfully:

1. Check the backup software log for the last scheduled backup. Confirm it shows "Completed Successfully" or equivalent status.
2. Verify the backup file or set is present on the target destination (network share, external drive, or cloud).
3. Where possible, perform a test restore of one or more files to confirm backup integrity.
4. If the last backup failed, investigate the cause and initiate a manual backup before completing the PM.

---

## 5.0 Completing the PM Checklist

Upon completing all PM tasks, the technician records all actions taken in the PM checklist (senarai semak PM). This document must be:

- Completed in full — no blank fields
- Signed and dated by the technician
- Counter-signed by the supervisor or IT manager
- Filed in the system's maintenance record (rekod penyelenggaraan) for audit purposes

A sample PM checklist structure:

| # | Task | Done | Remarks |
|---|------|------|---------|
| 1 | External cleaning (monitor, keyboard, mouse) | ☐ | |
| 2 | Internal dust removal (fans, heatsink, PSU vent) | ☐ | |
| 3 | Cable and connector inspection | ☐ | |
| 4 | Thermal paste replacement (if annual) | ☐ | |
| 5 | CMOS battery check (if annual) | ☐ | |
| 6 | OS updates applied | ☐ | Build number after update: |
| 7 | Driver updates applied | ☐ | Components updated: |
| 8 | BIOS/firmware update (if applicable) | ☐ | New version: |
| 9 | Antivirus definitions updated and full scan completed | ☐ | Threats found: |
| 10 | Disk error check | ☐ | Result: |
| 11 | Disk cleanup | ☐ | Space recovered: |
| 12 | Disk defragmentation / optimisation | ☐ | |
| 13 | S.M.A.R.T. status checked | ☐ | Status: |
| 14 | Startup programmes reviewed | ☐ | Items disabled: |
| 15 | Backup verified | ☐ | Last backup date: |

---

## 6.0 Common Errors in Preventive Maintenance

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Spinning fans with compressed air | Fan bearing damage; voltage spike to motherboard | Hold fan blade still before blowing compressed air |
| Applying too much thermal paste | Paste overflows onto motherboard socket; short circuit | Apply a rice-grain-sized amount to the CPU centre only |
| Defragmenting an SSD | Reduces SSD lifespan by causing unnecessary write cycles | Always check drive type before running defrag; use Optimise for SSDs |
| Updating BIOS without reading release notes | Incompatible update bricks the motherboard | Read release notes; update only for known issues |
| Marking PM complete without verifying backup | Backup failure goes undetected until a restore is needed | Treat backup verification as a mandatory task, not optional |
| Not recording PM actions in the checklist | No evidence of work performed; audit failures | Complete the checklist before returning the system to the user |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCU 2: Computer System Maintenance
- Jennifer's verified WIM reference: IT-020-3:2013-C02/P(1/16)
- CompTIA A+ Core 1 (220-1101) — Hardware Maintenance and Troubleshooting
- Microsoft Support: Windows Update and Maintenance documentation
- CrystalDiskInfo documentation — S.M.A.R.T. attribute reference