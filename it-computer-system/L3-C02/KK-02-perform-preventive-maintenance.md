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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C02 COMPUTER SYSTEM MAINTENANCE |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. IDENTIFY COMPUTER MAINTENANCE REQUIREMENTS<br>2. CARRY OUT COMPUTER SCHEDULED PREVENTIVE MAINTENANCE<br>3. PERFORM COMPUTER CORRECTIVE MAINTENANCE<br>4. PREPARE COMPUTER MAINTENANCE REPORT |
| NO. KOD | IT-020-3:2013-C02/KK(2/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-02-perform-preventive-maintenance

**TUJUAN:** Kertas rujukan untuk KK-02-perform-preventive-maintenance.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

By the end of this activity, trainees will be able to:
- Perform a complete physical cleaning of internal and external computer components
- Replace thermal paste on the CPU heatsink assembly
- Carry out software-based preventive maintenance tasks (disk cleanup, defragmentation, updates, antivirus scan)
- Verify system stability after preventive maintenance and record results

---

## Tempoh / Duration

6 hours

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Kuantiti / Quantity |
|-----|------|---------------------|
| 1 | Desktop computer (assigned unit) | 1 unit |
| 2 | Anti-static wrist strap | 1 |
| 3 | Screwdriver set (Phillips and flathead) | 1 set |
| 4 | Can of compressed air | 1 |
| 5 | Soft-bristle brush (ESD-safe) | 1 |
| 6 | Isopropyl alcohol (IPA) 70% or higher | 1 bottle |
| 7 | Lint-free cloths / cotton swabs | 1 pack |
| 8 | Thermal paste (CPU-grade compound) | 1 tube |
| 9 | Cable ties (nylon, assorted) | 1 pack |
| 10 | Preventive Maintenance Checklist (PM Checklist) | 1 |
| 11 | USB flash drive with antivirus update files (offline) | 1 |
| 12 | Maintenance log sheet | 1 |

---

## Langkah Keselamatan / Safety Precautions

- Power off the computer completely and disconnect the power cable before opening the casing
- Wear the anti-static wrist strap at all times when handling internal components
- Use compressed air in short bursts in a well-ventilated area or outdoors — dust particles can be an irritant
- Never use wet cloths inside the casing; use IPA on lint-free cloth only, and allow surfaces to dry completely before reconnecting power
- Do not touch capacitor leads or exposed PCB traces with bare hands
- When reapplying thermal paste, use only a pea-sized amount — excess paste can spread to the socket and cause short circuits
- Ensure all cables are securely reconnected and no tools are left inside the casing before powering on

---

## Prosedur / Procedures

### Bahagian A — Pembersihan Fizikal / Physical Cleaning

| Langkah | Arahan / Instruction |
|---------|----------------------|
| 1 | Power off the computer. Disconnect the power cable and all peripheral cables. Wear the anti-static wrist strap. Open the computer casing. |
| 2 | Using the soft-bristle brush and compressed air, clean dust from: (a) case fans and fan grilles, (b) CPU heatsink fins, (c) RAM slots, (d) expansion card slots and PCIe cards, (e) power supply intake vents, (f) the motherboard surface generally. Direct compressed air bursts away from components when blowing dust out. |
| 3 | Use a lint-free cloth lightly dampened with IPA to wipe the interior casing walls. Use cotton swabs with IPA for tight corners and connector ports on the rear panel. Allow to dry before proceeding. |
| 4 | Inspect all internal cables (power, SATA, front-panel connectors). Remove any cable ties that are worn or overtightened. Reroute cables neatly and secure with new cable ties to improve airflow. |
| 5 | Remove the CPU cooler (heatsink and fan assembly). Clean off old thermal paste from the CPU surface and heatsink base plate using IPA and a lint-free cloth. Inspect the CPU socket and pins for damage — do not touch pins. |
| 6 | Apply a fresh pea-sized amount of thermal paste to the centre of the CPU die. Reattach the heatsink following the manufacturer's diagonal-tightening sequence (do not tighten in a circle — alternate corners to ensure even pressure). Reconnect the CPU fan power connector. |
| 7 | Reconnect all internal cables. Perform a final visual inspection — confirm no tools, loose screws, or disconnected cables remain inside. Close the casing. |

### Bahagian B — Penyelenggaraan Perisian / Software Maintenance

| Langkah | Arahan / Instruction |
|---------|----------------------|
| 8 | Reconnect the power cable. Power on the computer. Verify that the POST completes without errors and the OS loads normally. |
| 9 | Open **Disk Cleanup** (Windows: `cleanmgr`). Select all categories including Temporary Files, Recycle Bin, and System Files. Run the cleanup and note the amount of space recovered. |
| 10 | Check the hard drive type. If HDD: open **Disk Defragmenter / Optimize Drives** (`dfrgui`), analyse the drive, and run defragmentation. If SSD: run **Optimize** (TRIM command) instead — do not defragment an SSD. Record the result. |
| 11 | Open **Windows Update** (Settings → Update & Security). Check for and install all available OS patches and security updates. If the machine is offline, apply updates from the USB flash drive provided. Restart as required. |
| 12 | Update all installed application software where applicable (browser, office suite, PDF reader). Use the in-application "Check for Updates" function or the offline update package on the USB flash drive. |
| 13 | Update the antivirus definition database using the provided USB flash drive update file. Run a **Full Disk Scan**. Record the scan result (threats found / quarantined / none). |
| 14 | Check BIOS/UEFI firmware version (press F2/Del at POST or use CPU-Z). If a firmware update is specified in the PM Checklist for this unit, follow the manufacturer's procedure exactly — do not interrupt the update process once started. |
| 15 | Verify firewall status is enabled. Check that Windows Defender or installed antivirus is active and real-time protection is on. |
| 16 | Restart the computer. Observe boot time and confirm all startup programs load correctly. Record the post-maintenance boot behaviour on the PM Checklist. |

### Bahagian C — Dokumentasi / Documentation

| Langkah | Arahan / Instruction |
|---------|----------------------|
| 17 | Complete all sections of the PM Checklist: physical cleaning tasks completed, software tasks completed, issues found, corrective actions taken, and next scheduled PM date. |
| 18 | Update the machine's Maintenance Log with today's date, tasks performed, technician name, and any components replaced or consumables used (thermal paste, cable ties). |
| 19 | Submit the completed PM Checklist and Maintenance Log to the instructor. |

---

## Hasil Dijangka / Expected Outcome

Upon completion, the trainee will have:
- A physically clean computer with renewed thermal paste, neat cable management, and dust-free components
- A fully updated OS, applications, drivers, and antivirus definitions
- A completed PM Checklist and Maintenance Log documenting all tasks performed
- A computer that boots and operates stably after maintenance

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Power disconnected and anti-static precautions in place before opening casing | [ ] Yes  [ ] No |
| 2 | Dust removed from all internal components using correct tools | [ ] Yes  [ ] No |
| 3 | Old thermal paste fully removed from CPU and heatsink | [ ] Yes  [ ] No |
| 4 | Correct amount of thermal paste applied and heatsink reattached properly | [ ] Yes  [ ] No |
| 5 | All cables reconnected and managed neatly with cable ties | [ ] Yes  [ ] No |
| 6 | Disk Cleanup performed and result recorded | [ ] Yes  [ ] No |
| 7 | Disk optimised (defrag for HDD / TRIM for SSD) | [ ] Yes  [ ] No |
| 8 | OS and application patches applied successfully | [ ] Yes  [ ] No |
| 9 | Antivirus definitions updated and full scan completed | [ ] Yes  [ ] No |
| 10 | Firewall and real-time protection confirmed active | [ ] Yes  [ ] No |
| 11 | PM Checklist fully completed with next PM date | [ ] Yes  [ ] No |
| 12 | Maintenance Log updated with technician details and date | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Nama / Name | Tandatangan / Signature | Tarikh / Date |
|---|-------------|-------------------------|----------------|
| Pelatih / Trainee | | | |
| Pengajar / Instructor | | | |