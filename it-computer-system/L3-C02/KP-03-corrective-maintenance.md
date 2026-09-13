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
| NO. KOD | IT-020-3:2013-C02/KP(3/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-03-corrective-maintenance

**TUJUAN:** Kertas rujukan untuk KP-03-corrective-maintenance.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Define corrective maintenance and distinguish it from preventive and predictive maintenance
2. Apply a systematic fault-finding methodology to isolate hardware and software faults
3. Identify and describe common hardware faults and their corrective actions
4. Identify and describe common software and operating system faults and their corrective actions
5. Document corrective maintenance actions accurately in a fault and repair log

---

## 1.0 Introduction to Corrective Maintenance

Corrective maintenance (penyelenggaraan pembetulan) is the set of actions taken after a computer system fault (kerosakan) has been reported or detected. Unlike preventive maintenance, which is scheduled and proactive, corrective maintenance is reactive — it begins when a system has already failed or degraded to the point of affecting the user.

The objectives of corrective maintenance are:

- To identify the root cause (punca asas) of the fault
- To restore the system to full operational status within the minimum possible time
- To prevent recurrence of the same fault through appropriate corrective action
- To document the fault, diagnosis, and repair for the maintenance record

Corrective maintenance may involve component replacement (gantian komponen), software repair, configuration correction, or a combination of all three.

---

## 2.0 Systematic Fault-Finding Methodology

A structured approach to fault finding prevents wasted time, avoids introducing new faults, and produces a documented evidence trail. The following six-step methodology should be applied to all corrective maintenance tasks.

| Step | Action | Description |
|------|--------|-------------|
| 1 | **Identify the problem** | Gather information from the user. Ask: What symptoms are observed? When did it start? What changed recently (new software, hardware, Windows update)? Is it intermittent or constant? |
| 2 | **Establish a theory of probable cause** | Based on the symptoms, list the most likely causes in order of probability. Start with the simplest and most common cause. |
| 3 | **Test the theory** | Run targeted tests to confirm or eliminate the probable cause. Use diagnostic tools appropriate to the suspected fault area. |
| 4 | **Establish a plan of action** | Once the root cause is confirmed, plan the corrective action. Consider impact on other systems, data safety, and whether a backup must be taken first. |
| 5 | **Implement the solution** | Carry out the corrective action. Replace the faulty component, repair the software, or correct the configuration. |
| 6 | **Verify full functionality and document** | Test the system to confirm the fault is resolved and no new issues have been introduced. Complete the fault and repair log. |

---

## 3.0 Common Hardware Faults and Corrective Actions

### 3.1 No Power / System Does Not Start

**Symptoms:** Computer does not power on; no indicator lights, no fan spin.

| Probable Cause | Diagnostic Test | Corrective Action |
|----------------|----------------|------------------|
| Loose or disconnected power cable | Check mains cable at wall socket and PSU connection | Re-seat or replace the power cable |
| Faulty wall socket or power strip | Plug into a different socket; test socket with a known-good device | Replace power strip; report faulty wall socket to facilities |
| Faulty PSU (Power Supply Unit) | Use a PSU tester or substitute with a known-good PSU | Replace the PSU with a compatible unit (match wattage and connector type) |
| Loose internal power connectors | Open chassis; check 24-pin ATX and CPU 8-pin power connectors | Re-seat all internal power connectors |
| Faulty power button | Short the power button header pins on the motherboard with a screwdriver | Replace the front panel power button or cable |

### 3.2 System Starts But No Display

**Symptoms:** Fans spin, power LED is on, but the monitor shows no image.

| Probable Cause | Diagnostic Test | Corrective Action |
|----------------|----------------|------------------|
| Monitor not powered or input set incorrectly | Check monitor power and cycle through input sources (HDMI, DisplayPort, VGA) | Power on the monitor; select correct input |
| Loose video cable | Check the video cable at both ends | Re-seat or replace the video cable |
| Faulty or unseated GPU | Reseat the GPU in its PCIe slot; try onboard graphics if available | Clean PCIe slot contacts with IPA; re-seat GPU; replace if faulty |
| Faulty or incompatible RAM | Listen for POST beep codes; remove and re-seat RAM; test sticks individually | Clean RAM gold contacts with an eraser; re-seat; replace faulty stick |
| BIOS/UEFI POST failure | Observe POST beep codes (refer to motherboard manual) | Diagnose beep code; replace indicated faulty component |

**POST Beep Code Reference (Award BIOS):**

| Beep Pattern | Indicated Fault |
|-------------|----------------|
| 1 short beep | POST successful — normal boot |
| 1 long + 2 short | Video card or memory fault |
| 1 long + 3 short | Video card fault (no video card or bad video RAM) |
| Continuous long beeps | RAM not detected or not seated |
| No beep + no display | PSU fault, CPU fault, or no speaker connected |

### 3.3 System Overheating / Unexpected Shutdown

**Symptoms:** System shuts down without warning, especially under load; CPU/GPU temperature alerts in BIOS or monitoring software.

| Probable Cause | Diagnostic Test | Corrective Action |
|----------------|----------------|------------------|
| Dust-clogged heatsink or fan | Open chassis; visually inspect; measure CPU temperature with HWMonitor | Clean heatsink fins and fan blades with compressed air |
| Degraded or absent thermal paste | Check CPU temperature at idle; compare to safe operating range | Remove heatsink; clean old paste; re-apply new thermal paste |
| Faulty or failed CPU fan | Observe fan during POST; check fan speed in BIOS | Replace the CPU cooler fan or the entire cooler assembly |
| Inadequate case airflow | Check case fan operation and direction (intake at front/bottom, exhaust at rear/top) | Add or replace case fans; ensure cable management does not obstruct airflow |
| Ambient temperature too high | Measure room temperature | Relocate the system to a cooler area; improve room ventilation or air-conditioning |

### 3.4 Hard Disk Drive (HDD) / Solid-State Drive (SSD) Faults

**Symptoms:** System fails to boot with "Operating System Not Found" or "Boot Device Not Found"; slow read/write performance; file corruption; clicking sounds (HDD only).

| Probable Cause | Diagnostic Test | Corrective Action |
|----------------|----------------|------------------|
| Loose SATA data or power cable | Open chassis; check SATA connections at drive and motherboard | Re-seat SATA data and power cables |
| Drive not detected in BIOS | Enter BIOS setup; check boot device list and SATA port status | Replace SATA cable; swap to a different SATA port; replace drive if still not detected |
| Failing HDD (bad sectors) | Run `chkdsk /f /r` or CrystalDiskInfo S.M.A.R.T. check | Back up data immediately; replace the HDD; restore data from backup |
| Corrupted Master Boot Record (MBR) or boot files | Boot from Windows installation media; run `bootrec /fixmbr` and `bootrec /fixboot` | Repair the boot record; if unsuccessful, reinstall the OS |

### 3.5 RAM (Memory) Faults

**Symptoms:** Blue Screen of Death (BSOD) with MEMORY_MANAGEMENT or IRQL_NOT_LESS_OR_EQUAL errors; random crashes; system fails to POST.

**Diagnostic tool:** Memtest86 (bootable USB) — run for at least two full passes.

**Corrective actions:**
- Clean the RAM module gold contacts with a clean pencil eraser, then wipe with IPA.
- Re-seat the RAM module in the slot, ensuring the retention clips click into place.
- Test each RAM module individually to identify a faulty stick.
- Replace the faulty RAM module with a compatible replacement (match DDR generation, speed, and capacity).

### 3.6 USB Port / Peripheral Not Detected

**Symptoms:** Keyboard or mouse not recognised; USB device not detected; Device Manager shows unknown device or error code.

| Probable Cause | Corrective Action |
|----------------|------------------|
| Faulty USB port on chassis | Test the device on a different USB port |
| Corrupted USB driver | Uninstall the device in Device Manager and reconnect; Windows will reinstall the driver |
| Faulty device | Test the device on a known-good computer |
| USB controller disabled in BIOS | Enter BIOS and enable the USB controller |
| Clean the RAM gold contacts | Use isopropyl alcohol on a cotton swab to clean RAM contacts if device is internally connected |

---

## 4.0 Common Software and Operating System Faults

### 4.1 Blue Screen of Death (BSOD)

The Blue Screen of Death (Skrin Biru Kematian) indicates a critical system error from which Windows cannot recover. Every BSOD contains a stop code (kod henti) that identifies the fault category.

| Common Stop Code | Probable Cause | Corrective Action |
|-----------------|----------------|------------------|
| MEMORY_MANAGEMENT | Faulty or incompatible RAM | Run Memtest86; replace faulty RAM |
| DRIVER_IRQL_NOT_LESS_OR_EQUAL | Faulty or outdated driver | Boot into Safe Mode; uninstall the recently updated driver; roll back or reinstall |
| CRITICAL_PROCESS_DIED | Corrupted system files | Run `sfc /scannow` in Command Prompt (Admin); use `DISM /Online /Cleanup-Image /RestoreHealth` if SFC fails |
| INACCESSIBLE_BOOT_DEVICE | Boot drive fault or corrupted boot configuration | Check SATA connections; boot from Windows media and run Startup Repair |
| PAGE_FAULT_IN_NONPAGED_AREA | RAM fault or driver issue | Run Memtest86; update or roll back drivers |

**First response to BSOD:**
1. Record or photograph the stop code and any module name displayed.
2. Check whether the BSOD is intermittent or constant.
3. Review Event Viewer (System and Application logs) for errors immediately preceding the crash.
4. Identify any recent changes (updates, new hardware, new software).

### 4.2 Operating System Fails to Boot

**Symptoms:** System shows "Automatic Repair" loop; Windows fails to reach the login screen.

**Corrective procedure:**

1. Boot from Windows installation media (USB or DVD).
2. Select **Repair your computer → Troubleshoot → Advanced Options**.
3. Try **Startup Repair** first — Windows will attempt to diagnose and fix boot issues automatically.
4. If Startup Repair fails, open **Command Prompt** and run:
   - `bootrec /fixmbr` — repairs the Master Boot Record
   - `bootrec /fixboot` — repairs the boot sector
   - `bootrec /rebuildbcd` — rebuilds the Boot Configuration Data
5. If the above fails, use **System Restore** to revert to the last known-good system state.
6. As a last resort, perform an in-place upgrade repair installation using Windows installation media — this reinstalls Windows while preserving user data and applications.

### 4.3 Slow System Performance

**Symptoms:** Applications take a long time to open; system is unresponsive; high CPU or RAM usage reported in Task Manager.

| Probable Cause | Diagnostic Test | Corrective Action |
|----------------|----------------|------------------|
| Too many startup programmes | Task Manager → Startup tab | Disable non-essential startup items |
| Malware or virus | Run a full antivirus scan | Remove detected threats; run Malwarebytes for additional scan |
| Insufficient RAM | Task Manager → Performance → Memory (check % used at idle) | Close unnecessary applications; upgrade RAM if consistently above 80% |
| Fragmented HDD (not SSD) | Defragment and Optimise Drives | Run defragmentation on the HDD |
| Disk almost full (less than 10% free) | Check drive free space in File Explorer | Run Disk Cleanup; move large files to external storage |
| Outdated drivers or OS | Check Windows Update and Device Manager | Apply all pending updates |

### 4.4 Application Errors and Crashes

**Symptoms:** A specific application crashes on launch or during use; error dialogue boxes appear.

**Corrective procedure:**
1. Check the application's event log entry in **Event Viewer → Windows Logs → Application**.
2. Verify the application is compatible with the current version of Windows.
3. Run the application as Administrator (right-click → Run as Administrator) to rule out permission issues.
4. Uninstall and reinstall the application using the original installer or a fresh download.
5. Check for application updates or patches from the software vendor.
6. If a recent Windows update caused the issue, use **Windows Update → View Update History → Uninstall Updates** to remove the problematic update.

### 4.5 Network Connectivity Faults

**Symptoms:** Cannot access the internet or network shares; "No internet, secured" or "Unidentified network" shown in the system tray.

| Probable Cause | Diagnostic Test | Corrective Action |
|----------------|----------------|------------------|
| Faulty network cable (wired) | Test cable with a cable tester; try a known-good cable | Replace the network cable |
| NIC driver fault | Device Manager → Network Adapters (check for error icon) | Uninstall and reinstall the NIC driver |
| IP address conflict | `ipconfig /all` — check for APIPA address (169.254.x.x) | Release and renew IP: `ipconfig /release` then `ipconfig /renew`; check DHCP server |
| DNS fault | `ping 8.8.8.8` (if successful, DNS is the issue) | Flush DNS cache: `ipconfig /flushdns`; set DNS to 8.8.8.8 or organisational DNS server |
| Firewall blocking connection | Temporarily disable Windows Firewall to test | Adjust firewall rules; re-enable firewall after testing |

---

## 5.0 Escalation Criteria

Not all faults can be resolved at the technician level. The following situations require escalation to a senior technician or IT manager:

- Motherboard-level faults (no POST, multiple component failures simultaneously)
- Data recovery from a physically failed drive — requires specialist tools or a data recovery service
- Suspected security breach (ransomware, rootkit, or unauthorised access)
- Faults requiring specialised warranty repair by the manufacturer or authorised service centre
- System-wide network outages affecting multiple computers simultaneously

When escalating, the technician must provide: the asset tag, fault description, steps already taken, and any error codes observed.

---

## 6.0 Documenting Corrective Maintenance

All corrective maintenance activities must be documented in a **Fault and Repair Log** (Log Kerosakan dan Pembaikan). This document is essential for:

- Identifying recurring faults (chronic problems that require root-cause elimination)
- Supporting warranty or service contract claims
- Providing an audit trail for IT governance and compliance

| Field | Content |
|-------|---------|
| Request number | From the original maintenance request form |
| Asset tag / Serial number | Physical label on the computer |
| Fault reported | User's description of the problem |
| Date and time fault reported | From the request form |
| Date and time work commenced | When the technician began diagnosis |
| Diagnosis findings | Root cause identified, with evidence (error codes, test results) |
| Corrective action taken | Specific steps performed; parts replaced (include part numbers) |
| Date and time completed | When the system was returned to service |
| System tested and verified | Yes / No; description of verification test |
| Technician name and signature | |
| Supervisor sign-off | |

---

## 7.0 Common Errors in Corrective Maintenance

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Skipping fault-finding steps; replacing components without diagnosis | Unnecessary expenditure; fault not resolved because wrong component replaced | Follow the six-step methodology; test the theory before replacing parts |
| Not backing up data before making changes | Data lost if repair procedure corrupts or wipes the drive | Always offer to back up user data before any repair that touches the storage system |
| Mixing up components from multiple systems | Wrong parts returned to wrong units; traceability lost | Label all removed components with the asset tag before placing them aside |
| Marking a fault as resolved without a functionality test | Fault recurs immediately; user dissatisfied | Always run a full functionality test before returning the system |
| Not updating the fault log | Recurring faults not identified; no audit trail | Complete the log entry as the final step of every corrective maintenance task |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCU 2: Computer System Maintenance
- Jennifer's verified WIM reference: IT-020-3:2013-C02/P(1/16)
- CompTIA A+ Core 1 (220-1101) and Core 2 (220-1102) — Troubleshooting Methodology
- Microsoft Support: Windows BSOD stop codes and diagnostic tools
- Award BIOS POST beep code reference