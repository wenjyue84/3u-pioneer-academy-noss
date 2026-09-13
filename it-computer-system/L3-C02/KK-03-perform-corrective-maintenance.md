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
| NO. KOD | IT-020-3:2013-C02/KK(3/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-03-perform-corrective-maintenance

**TUJUAN:** Kertas rujukan untuk KK-03-perform-corrective-maintenance.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

By the end of this activity, trainees will be able to:
- Diagnose the cause of a reported computer fault using systematic troubleshooting methods
- Carry out the appropriate corrective action to restore the system to normal operation
- Verify that the fault has been resolved and the system functions within acceptable parameters
- Document the fault, diagnosis, corrective actions taken, and verification results

---

## Tempoh / Duration

6 hours

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Kuantiti / Quantity |
|-----|------|---------------------|
| 1 | Desktop computer with pre-introduced fault (assigned by instructor) | 1 unit |
| 2 | Anti-static wrist strap | 1 |
| 3 | Screwdriver set (Phillips and flathead) | 1 set |
| 4 | Multimeter (for power supply voltage check) | 1 |
| 5 | Compressed air can | 1 |
| 6 | Isopropyl alcohol (IPA) 70% or higher | 1 bottle |
| 7 | Lint-free cloths / cotton swabs | 1 pack |
| 8 | Spare RAM module (DDR4, compatible) | 1 |
| 9 | Spare SATA data cable | 1 |
| 10 | Bootable USB diagnostic tool (e.g., MemTest86, UBCD) | 1 |
| 11 | Fault Report Form (Borang Laporan Kerosakan) | 1 |
| 12 | Corrective Maintenance Log | 1 |
| 13 | Thermal paste | 1 tube |

---

## Langkah Keselamatan / Safety Precautions

- Power off and unplug the computer before performing any internal hardware work
- Wear the anti-static wrist strap at all times when handling components inside the casing
- When using a multimeter, ensure probes are in the correct ports (COM and V/Ω) and set the range correctly before measuring PSU voltages
- Do not short-circuit any connector or board trace when probing
- If a burning smell or visible burn marks are observed on any component, do not power on — report to the instructor immediately
- When replacing RAM, handle modules by the edges only — never touch the gold contacts
- Confirm all connections are secure and no tools remain inside the casing before powering on after repair

---

## Prosedur / Procedures

### Bahagian A — Penerimaan Aduan dan Pengumpulan Maklumat / Fault Reception and Information Gathering

| Langkah | Arahan / Instruction |
|---------|----------------------|
| 1 | Receive the Fault Report Form from the instructor. Read all reported symptoms carefully. Note: the symptom description, when the fault first occurred, whether it is intermittent or constant, and any recent changes to the system (new software installed, hardware moved, recent impact). |
| 2 | Interview the simulated user (instructor role-play): ask at least 3 clarifying questions to narrow the fault scope — e.g., "Does the computer power on at all?", "Are there any beep codes?", "Did any error message appear?" Record the responses. |
| 3 | Based on the symptom information, formulate a **hypothesis** — state the most likely fault cause and which component or subsystem is suspect. Record this on the Fault Report Form before proceeding. |

### Bahagian B — Diagnosis Kerosakan / Fault Diagnosis

| Langkah | Arahan / Instruction |
|---------|----------------------|
| 4 | Power on the computer without opening the casing. Observe the POST: does it complete? Are there beep codes? Does the OS load? Does it boot to BIOS only? Record all observations precisely. |
| 5 | If the system does not POST or shows beep codes, use the following sequence to isolate: (a) check all power connections (24-pin ATX, 4/8-pin CPU power); (b) reseat RAM modules — remove and reinstall one at a time; (c) reseat all expansion cards (GPU, if present); (d) check all SATA connections (data and power). |
| 6 | If the system POSTs but shows OS-level errors (e.g., Blue Screen of Death / BSOD, missing OS): boot from the USB diagnostic tool. Run **MemTest86** for at least one pass to check RAM integrity. Note: if errors are found, the RAM module is suspect. |
| 7 | If a storage-related fault is suspected: in the BIOS/UEFI setup, confirm the hard drive is detected under Storage/SATA configuration. If not detected, swap the SATA data cable with the spare. If detected in BIOS but not bootable, the issue is OS/file system level. |
| 8 | If a power-related fault is suspected (system does not power on, random shutdowns): use the multimeter to measure PSU output voltages on a free Molex or SATA power connector. Expected readings: +12V rail (11.4–12.6 V), +5V rail (4.75–5.25 V), +3.3V rail (3.135–3.465 V). Record readings. Out-of-range = PSU fault. |
| 9 | If an overheating fault is suspected: check BIOS hardware monitor for CPU and system temperatures. Clean all heatsink fins and case fans with compressed air. Verify CPU fan is spinning. Check thermal paste condition. Record temperature readings. |
| 10 | If a peripheral/interface fault is suspected (keyboard/mouse not detected, USB ports not working): test with a known-working device on a different port. Check Device Manager for driver errors or unknown devices. |
| 11 | Confirm the root cause. Update the Fault Report Form with your **confirmed diagnosis**: component identified, test method used, and evidence for your conclusion. |

### Bahagian C — Tindakan Pembetulan / Corrective Action

| Langkah | Arahan / Instruction |
|---------|----------------------|
| 12 | Power off the computer and disconnect the power cable. Wear the anti-static wrist strap. Open the casing. |
| 13 | Carry out the corrective action appropriate to the confirmed fault. Examples: (a) **Faulty RAM** — replace the defective module with the spare, ensuring correct DIMM slot placement per the motherboard manual; (b) **SATA cable fault** — replace the cable and confirm drive is detected in BIOS; (c) **Overheating** — remove and clean heatsink, reapply thermal paste, reinstall heatsink; (d) **Loose connection** — firmly reconnect the identified connector; (e) **Software/OS corruption** — use Windows Recovery Environment (WinRE) to run `sfc /scannow` or `chkdsk /f /r` from Command Prompt. |
| 14 | After the corrective action, perform a visual check: confirm all cables reconnected, no tools left inside, casing closed. |

### Bahagian D — Pengesahan dan Ujian / Verification and Testing

| Langkah | Arahan / Instruction |
|---------|----------------------|
| 15 | Power on the computer. Verify that the POST completes without error codes. Confirm the OS loads fully to the desktop. |
| 16 | Run the system for a minimum of 15 minutes with normal use (open applications, browse files, play a media file). Observe for any recurrence of the original symptom or new faults. |
| 17 | Re-run the diagnostic tool (if applicable) to confirm the fault is cleared — e.g., re-run MemTest86 for one pass after RAM replacement; verify drive is detected and accessible after cable replacement. |
| 18 | Check BIOS hardware monitor: confirm CPU temperature is within normal operating range (typically below 70°C under load for most desktop processors). |

### Bahagian E — Dokumentasi / Documentation

| Langkah | Arahan / Instruction |
|---------|----------------------|
| 19 | Complete the Fault Report Form: record the confirmed fault, corrective action taken, components replaced or adjusted, verification test results, and final system status. |
| 20 | Update the Corrective Maintenance Log with: asset number, fault description, diagnosis method, repair action, parts used, technician name, date and time of repair completion. |
| 21 | Submit all completed forms to the instructor for review. |

---

## Hasil Dijangka / Expected Outcome

Upon completion, the trainee will have:
- Correctly diagnosed the pre-introduced fault using a systematic troubleshooting approach
- Carried out the appropriate corrective action to restore normal system operation
- Verified the repair through post-repair testing and confirmed no recurrence
- Produced a fully completed Fault Report Form and Corrective Maintenance Log

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Fault Report Form read and symptom information gathered correctly | [ ] Yes  [ ] No |
| 2 | At least 3 clarifying questions asked to narrow fault scope | [ ] Yes  [ ] No |
| 3 | Initial hypothesis stated before diagnostic testing began | [ ] Yes  [ ] No |
| 4 | Systematic diagnostic steps followed in correct order | [ ] Yes  [ ] No |
| 5 | Root cause correctly identified with supporting evidence | [ ] Yes  [ ] No |
| 6 | Anti-static precautions observed throughout hardware work | [ ] Yes  [ ] No |
| 7 | Correct corrective action applied for the identified fault | [ ] Yes  [ ] No |
| 8 | System powers on and OS loads successfully after repair | [ ] Yes  [ ] No |
| 9 | Post-repair verification tests performed and results recorded | [ ] Yes  [ ] No |
| 10 | Fault Report Form fully completed including root cause and action taken | [ ] Yes  [ ] No |
| 11 | Corrective Maintenance Log updated with all required details | [ ] Yes  [ ] No |
| 12 | All tools accounted for; casing closed before powering on | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Nama / Name | Tandatangan / Signature | Tarikh / Date |
|---|-------------|-------------------------|----------------|
| Pelatih / Trainee | | | |
| Pengajar / Instructor | | | |