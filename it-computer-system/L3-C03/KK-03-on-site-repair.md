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

## KERTAS KERJA

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-3:2013 OPERASI SISTEM KOMPUTER |
| TAHAP | 3 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C03 COMPUTER SYSTEM REPAIR |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ASSESS COMPUTER REPAIR JOB ORDER/CHANGE REQUEST<br>2. CARRY OUT ONLINE TROUBLESHOOTING<br>3. PERFORM ON-SITE REPAIR<br>4. PREPARE COMPUTER STATUS REPORT |
| NO. KOD | IT-020-3:2013-C03/KK(3/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-03-on-site-repair

**TUJUAN:** Kertas rujukan untuk KK-03-on-site-repair.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objectives

Upon completion of this activity, the trainee will be able to:
1. Prepare the repair workstation with appropriate tools, ESD protection, and spare parts before commencing work.
2. Identify and replace or reseat defective hardware components following safe disassembly and reassembly procedures.
3. Perform software-level repairs including OS repair, driver reinstallation, and data backup where required.
4. Conduct post-repair functionality testing to confirm the fault is fully resolved.
5. Restore the computer to its pre-repair configuration and return it to the customer in accordance with organisational procedures.

---

## Peralatan / Equipment Required

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Faulty desktop or laptop unit (simulated fault scenario) | 1 |
| 2 | Anti-static wrist strap (ESD wrist strap) | 1 |
| 3 | Anti-static mat | 1 |
| 4 | Precision screwdriver set (Phillips and flathead) | 1 set |
| 5 | Torx screwdriver set (for laptop units) | 1 set |
| 6 | Spare RAM module (compatible) | 1 |
| 7 | Spare HDD or SSD (compatible) | 1 |
| 8 | Compressed air canister | 1 |
| 9 | Thermal paste (for CPU reseating scenarios) | 1 tube |
| 10 | USB bootable OS repair / diagnostics drive | 1 |
| 11 | Replacement PSU (for power fault scenarios) | 1 |
| 12 | Cable ties and label tags | 1 set |
| 13 | Repair log form | 1 |
| 14 | Digital multimeter | 1 |

---

## Langkah Keselamatan / Safety Precautions

- **Power off and unplug** the unit from the mains before opening the chassis. For laptops, remove the battery if detachable.
- **Wear the ESD wrist strap** and connect it to the anti-static mat or chassis ground before handling any internal components. Failure to do so can permanently damage the motherboard, CPU, or RAM through electrostatic discharge.
- Do not force connectors or screws. If resistance is felt, re-examine the orientation before applying further force.
- Keep all removed screws in a labelled tray — mixing screws can cause thread damage or short circuits if an oversized screw is used.
- When using compressed air, hold the can upright and keep the nozzle at least 5 cm from components to avoid moisture or propellant damage.
- When replacing a PSU, verify the output voltage ratings match the system board requirements before powering on.
- Do not perform repairs in a damp or dusty environment. Ensure adequate lighting at the workstation.
- Back up customer data before any repair that involves storage media replacement or OS reinstallation. Obtain written acknowledgement (simulated) from the customer before any data-destructive action.

---

## Prosedur / Procedure

| Langkah | Arahan / Instruction |
|---------|----------------------|
| 1 | Receive the faulty unit and the approved job order from the instructor. Review the job order: confirm the asset tag, customer name, fault description, scope of repair authorised, and any special handling instructions (e.g. "preserve all data"). |
| 2 | Prepare the workstation: lay out the anti-static mat, connect the ESD wrist strap, arrange tools, and place the spare parts within reach. Verify the spare parts are compatible with the unit's model number before opening the chassis. |
| 3 | Power off the unit completely. Disconnect the power cable (and remove the laptop battery if applicable). Hold the power button for 3 seconds to discharge residual capacitor voltage. |
| 4 | Open the chassis following the manufacturer's disassembly sequence. For desktop units: remove the side panel screws and slide the panel off. For laptop units: refer to the service manual order — typically remove the base screws, release the bottom cover clips, and lift the cover. Place all screws in a labelled tray. |
| 5 | **Visual inspection:** Before replacing any component, inspect the interior for: (a) bulging or leaking capacitors on the motherboard; (b) burn marks or discolouration; (c) dislodged or cracked connectors; (d) excessive dust accumulation on heatsink and fan. Clean dust using compressed air. Record all visual findings in the repair log. |
| 6 | Perform the repair action corresponding to the fault scenario assigned by the instructor. Follow the relevant sub-procedure: |
| | **6a — RAM fault (no POST / memory error):** Remove existing RAM modules. Clean the gold contacts gently with a dry lint-free cloth. Reseat the modules firmly into the slots (listen for the clip lock). If reseating fails, replace with the spare module. |
| | **6b — HDD/SSD fault (system not detected / read errors):** Disconnect the SATA/NVMe cable and power connector from the drive. Remove the drive mounting screws. Install the replacement drive. Reconnect cables securely. Proceed to Step 7 for OS repair. |
| | **6c — Thermal fault (overheating / random shutdown):** Remove the heatsink assembly by unscrewing in a cross pattern. Clean old thermal paste from the CPU lid and heatsink base using isopropyl alcohol and a lint-free cloth. Apply a pea-sized amount of fresh thermal paste to the centre of the CPU lid. Reinstall the heatsink in the same cross pattern, gradually tightening to ensure even contact. |
| | **6d — PSU fault (no power):** Identify the PSU connectors (24-pin ATX, 8-pin CPU). Disconnect all connectors. Remove PSU mounting screws from the rear of the chassis. Slide out the PSU. Install the replacement unit, route all cables, and reconnect all power connectors securely. |
| 7 | If the fault involves the OS (boot failure, corrupted Windows, driver fault): (a) Insert the USB bootable repair drive; (b) Boot the unit and enter the BIOS/UEFI setup (typically F2 or Del); (c) Set boot priority to USB; (d) Use Windows Recovery Environment (WinRE) > Startup Repair for boot failures, or Advanced Options > System Restore / Reset This PC where applicable; (e) For driver faults, boot into Safe Mode and uninstall the problematic driver via Device Manager. |
| 8 | Reassemble the chassis in reverse disassembly order. Ensure all cables are routed clear of fans and sharp edges. Secure the chassis panel. Reconnect the power cable. |
| 9 | Power on the unit. Observe the POST screen — confirm no error beep codes and that the BIOS detects all installed components (RAM capacity, storage drive). Boot into Windows and log in. |
| 10 | Conduct post-repair functionality testing: (a) Confirm the original fault symptom no longer occurs; (b) Run **Windows Memory Diagnostic** (mdsched.exe) if RAM was serviced; (c) Run **SMART status check** via CrystalDiskInfo or command `wmic diskdrive get status` if HDD/SSD was replaced; (d) Verify CPU temperature is within normal operating range (below 80°C at idle under HWMonitor or Core Temp) if thermal paste was replaced; (e) Confirm stable power delivery and all fans are running if PSU was replaced. |
| 11 | Record all repair actions, components replaced, test results, and the final resolution status in the repair log. Sign and date the log. Submit the repaired unit and completed repair log to the instructor for assessment. |

---

## Hasil Dijangka / Expected Outcome

- Unit disassembled and reassembled safely with no component damage.
- Defective component identified, removed, and replaced (or reseated) correctly.
- Post-repair functionality tests completed and passed.
- Original fault symptom confirmed resolved.
- Repair log fully completed with all actions, replaced parts, and test results recorded.

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | ESD wrist strap worn and anti-static mat in use throughout repair | [ ] Yes  [ ] No |
| 2 | Unit powered off and discharged before opening chassis | [ ] Yes  [ ] No |
| 3 | Disassembly carried out without forced or missing screws | [ ] Yes  [ ] No |
| 4 | Visual inspection completed and findings recorded | [ ] Yes  [ ] No |
| 5 | Correct spare part verified as compatible before installation | [ ] Yes  [ ] No |
| 6 | Repair action performed correctly per assigned fault scenario | [ ] Yes  [ ] No |
| 7 | OS/software repair steps applied where applicable | [ ] Yes  [ ] No |
| 8 | Chassis reassembled cleanly; cables routed and secured | [ ] Yes  [ ] No |
| 9 | POST screen and Windows boot confirmed after reassembly | [ ] Yes  [ ] No |
| 10 | Post-repair functionality test passed and result recorded | [ ] Yes  [ ] No |
| 11 | Repair log completed, signed, and dated | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Nama / Name | Tandatangan / Signature | Tarikh / Date |
|---|-------------|------------------------|---------------|
| Pelatih / Trainee | | | |
| Pengajar / Instructor | | | |