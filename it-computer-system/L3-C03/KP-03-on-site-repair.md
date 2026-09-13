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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C03 COMPUTER SYSTEM REPAIR |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ASSESS COMPUTER REPAIR JOB ORDER/CHANGE REQUEST<br>2. CARRY OUT ONLINE TROUBLESHOOTING<br>3. PERFORM ON-SITE REPAIR<br>4. PREPARE COMPUTER STATUS REPORT |
| NO. KOD | IT-020-3:2013-C03/KP(3/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-03-on-site-repair

**TUJUAN:** Kertas rujukan untuk KP-03-on-site-repair.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the Power-On Self-Test (POST) sequence and interpret beep codes and on-screen fault indicators
2. Apply a structured hardware fault diagnosis process using appropriate tools and instruments
3. Identify and replace faulty hardware components following ESD safety and organisational procedures
4. Use diagnostic utilities (Memtest86, SMART, multimeter) to confirm hardware faults before replacement
5. Carry out a post-repair functionality test to verify the computer operates correctly
6. Document all repair actions, parts used, and test results on the job order

---

## 1.0 Introduction to On-Site Repair

On-site repair (Pembaikan Di Tapak) requires the technician to be physically present at the computer's location or to have the unit brought to the workshop. It encompasses the full hardware diagnostic and repair cycle: from initial power-on observation, through systematic fault isolation, to component replacement and final functionality testing.

On-site repair is required when:
- The computer cannot power on or does not reach the operating system
- Online troubleshooting has confirmed a hardware fault
- Physical inspection, cable reseating, or component replacement is needed
- Specialist diagnostic instruments (multimeter, POST card) must be used

---

## 2.0 Safety Precautions Before Opening a Computer

All on-site repair work must comply with the following safety requirements:

| Precaution | Reason |
|------------|--------|
| Power off and unplug the computer from the mains | Prevents electric shock and protects components from live voltage |
| Wear an anti-static wrist strap (gelang anti-statik) connected to an earth point | Prevents electrostatic discharge (ESD / Nyahcas Elektrostatik) damaging sensitive components |
| Work on an anti-static mat | Provides a secondary ESD protection surface |
| Store removed components in anti-static bags | Protects components from ESD during transit and storage |
| Do not wear loose clothing or jewellery near the open chassis | Prevents accidental contact with components or short circuits |

---

## 3.0 Power-On Self-Test (POST)

POST (Ujian Kendiri Semasa Menghidupkan) is the built-in diagnostic sequence executed by the BIOS/UEFI firmware every time the computer powers on. It checks the CPU, RAM, GPU, and storage controller before handing control to the operating system bootloader.

### 3.1 Normal POST Sequence

1. Power button pressed → PSU provides stable voltage → motherboard initialises
2. BIOS/UEFI firmware loads from ROM chip
3. CPU, RAM, and system clock are tested
4. Video card is initialised; the manufacturer splash screen or POST screen appears on the monitor
5. Storage devices are detected and enumerated
6. BIOS/UEFI passes control to the boot device (e.g. NVMe SSD, SATA HDD)
7. Operating system bootloader starts

A successful POST produces one short beep (on BIOS systems that use a speaker) and proceeds to boot.

### 3.2 POST Beep Codes

BIOS manufacturers use different beep code patterns. The table below covers the two most common BIOS brands:

| BIOS Brand | Beep Pattern | Meaning |
|------------|-------------|---------|
| AMI BIOS | 1 short | POST passed — normal boot |
| AMI BIOS | 2 short | POST error — check screen for message |
| AMI BIOS | 1 long, 3 short | Video card fault |
| AMI BIOS | Continuous long beeps | RAM not detected or seated incorrectly |
| Award BIOS | 1 long, 2 short | Video card fault |
| Award BIOS | Repeating short beeps | PSU problem or CPU overheating |
| Award BIOS | 1 long, 3 short | Video card RAM fault |
| Phoenix BIOS | 1-1-3 | CMOS read/write error |
| Phoenix BIOS | 1-3-1 | RAM refresh failure |

> **Note:** Modern UEFI systems may display error messages on-screen rather than using beep codes. Always check both the speaker and the monitor during POST.

### 3.3 On-Screen POST Error Messages

| Message | Likely Cause |
|---------|-------------|
| "No bootable device found" | Boot drive not detected; wrong boot order; failed drive |
| "Reboot and select proper boot device" | Boot order does not include the OS drive |
| "CPU Fan Error" | CPU fan not connected or failed; thermal protection triggered |
| "CMOS checksum error" | CMOS battery (CR2032) is dead or BIOS settings were reset |
| "Memory not detected" | RAM module loose, incompatible, or failed |

---

## 4.0 Hardware Fault Diagnosis

### 4.1 Diagnostic Process Overview

Hardware fault diagnosis follows a systematic elimination approach:

1. **Observe POST behaviour** — does the system reach POST? Does it display an error or beep?
2. **Inspect visually** — open the chassis; check for burnt components, swollen capacitors, disconnected cables, loose expansion cards
3. **Reseat all connectors** — RAM, GPU, storage data and power cables, PCIe cards
4. **Isolate to minimum configuration** — remove non-essential components (secondary drives, PCIe cards, extra RAM sticks) and test with only CPU, one RAM stick, and PSU
5. **Test suspect components** using diagnostic tools
6. **Replace confirmed faulty components** and retest

### 4.2 PSU Diagnosis — Multimeter Check

A faulty power supply unit (PSU / Unit Bekalan Kuasa) is a common cause of no-power or random shutdown faults. The multimeter (multimeter) is used to measure DC output voltages from the PSU.

**Procedure (24-pin ATX connector, PSU removed from chassis):**

1. Short the PSU on (PS_ON — green wire, pin 16) to ground (black wire, any adjacent ground pin) using a jumper wire to simulate the motherboard power-on signal
2. Set the multimeter to DC voltage (V DC)
3. Probe between the colour-coded wire and any black (ground) wire:

| Rail | Expected Voltage | Wire Colour | Acceptable Range |
|------|-----------------|-------------|-----------------|
| +12 V | 12.0 V | Yellow | 11.4 V – 12.6 V |
| +5 V | 5.0 V | Red | 4.75 V – 5.25 V |
| +3.3 V | 3.3 V | Orange | 3.135 V – 3.465 V |
| −12 V | −12.0 V | Blue | −10.8 V – −13.2 V |
| +5 VSB | 5.0 V | Purple | 4.75 V – 5.25 V |

A reading outside the acceptable range indicates a faulty PSU that must be replaced. Do not continue using a PSU that fails this test.

### 4.3 RAM Diagnosis — Memtest86

Memtest86 is a standalone memory diagnostic utility (alat diagnostik memori) that runs independently of the operating system. It thoroughly tests RAM for bit errors, addressing faults, and timing issues.

**Procedure:**
1. Download Memtest86 from the official website (memtest86.com) and create a bootable USB drive
2. Boot the computer from the Memtest86 USB drive (adjust boot order in BIOS/UEFI)
3. Memtest86 begins automatically; allow at least **2 full passes** (one pass takes 10–30 minutes depending on RAM size)
4. A result of **0 errors** indicates RAM is functioning correctly
5. Any error count above zero indicates faulty RAM

**Isolation procedure for multiple RAM sticks:**
- If the system has more than one RAM module, test each module individually in the primary RAM slot (Slot A1 / DIMM 1)
- The module that produces errors is the faulty one and must be replaced
- Replace with a module of the same type (DDR4/DDR5), speed, and capacity; consult the motherboard QVL (Qualified Vendor List) if available

### 4.4 Storage Diagnosis — SMART Data

SMART (Self-Monitoring, Analysis and Reporting Technology) is a built-in monitoring system in HDDs and SSDs that tracks health indicators and predicts impending failure.

**Reading SMART data remotely (if OS is accessible):**
- PowerShell: `Get-PhysicalDisk | Select FriendlyName, HealthStatus, OperationalStatus`
- CrystalDiskInfo (third-party): displays all SMART attributes with colour-coded health status

**Key SMART attributes to check:**

| Attribute | Meaning | Warning Sign |
|-----------|---------|-------------|
| Reallocated Sector Count | Number of bad sectors remapped to spare areas | Any non-zero value on HDD; rising count |
| Pending Sector Count | Sectors waiting to be remapped (unstable) | Any non-zero value |
| Uncorrectable Sector Count | Sectors that could not be read or remapped | Any non-zero value — critical |
| Power-On Hours | Total hours the drive has been powered on | High hours on HDD (>30,000 hrs) — plan replacement |
| Temperature | Drive operating temperature | HDD: above 55°C; SSD: above 70°C — investigate cooling |
| SSD Wear Levelling Count | Remaining life of SSD NAND cells | Low values indicate approaching end of rated write life |

A SMART status of "Caution" or "Bad" is an immediate indicator that the drive must be backed up and replaced without delay.

### 4.5 GPU and Display Diagnosis

| Symptom | Diagnostic Step | Likely Cause |
|---------|----------------|-------------|
| No display, POST appears to succeed (beep heard) | Test with known-good monitor and cable | Faulty monitor or cable, not GPU |
| No display, no beep | Check GPU seated fully in PCIe slot; test with integrated graphics if available | GPU not seated; GPU failed |
| Artefacts, lines, or flickering on screen | Update or roll back GPU driver; test monitor on different PC | Driver fault or GPU overheating |
| PC crashes under graphics load | Check GPU temperature during load (GPU-Z); check PCIe power connectors | Overheating GPU; insufficient PCIe power |

---

## 5.0 Component Replacement Procedures

### 5.1 RAM Replacement

1. Power off and unplug; wear anti-static wrist strap
2. Press the retention clips at both ends of the DIMM slot outward until the module tilts up
3. Remove the faulty module; handle only by the edges
4. Align the new module's notch with the key in the DIMM slot; press down firmly and evenly until both retention clips click into place
5. Verify module is fully seated — no gap between the module and the slot
6. Power on and confirm the BIOS/UEFI detects the correct RAM capacity before booting the OS

### 5.2 HDD/SSD Replacement

1. Power off and unplug; wear anti-static wrist strap
2. Disconnect the SATA data cable and SATA power cable (or remove the M.2 screw and slide out the M.2 module)
3. Remove the drive from its bay or slot; retain mounting screws and brackets
4. Install the replacement drive; reconnect cables (or secure M.2 module with screw)
5. If replacing the OS drive: reinstall the operating system or restore from backup image
6. Run SMART check after installation to confirm baseline health

### 5.3 PSU Replacement

1. Power off and unplug; wait 30 seconds for capacitors to discharge
2. Photograph or label all power connector locations before disconnecting
3. Disconnect all power connectors: 24-pin ATX motherboard, CPU EPS (4-pin or 8-pin), PCIe GPU connectors, SATA power, and Molex connectors
4. Remove the PSU mounting screws (four screws on the rear panel) and slide the PSU out
5. Install the replacement PSU; connect all power connectors; route cables for airflow
6. Power on and verify all voltages using multimeter or confirm stable operation through POST and OS boot

### 5.4 Thermal Paste and CPU Cooler Replacement

1. Remove the CPU cooler by unlocking the retention mechanism (LGA push-pins or AMD AM4/AM5 bracket screws)
2. Clean old thermal paste from the CPU IHS (Integrated Heat Spreader) and cooler base plate using 99% isopropyl alcohol (IPA / Alkohol Isopropil) and lint-free wipes
3. Apply a small amount (pea-sized, approximately 0.2 mL) of new thermal paste to the centre of the CPU IHS — do not spread manually; pressure from the cooler will spread it evenly
4. Reinstall the cooler; tighten retention screws in a cross pattern to ensure even pressure
5. Reconnect the CPU fan header to the motherboard (CPU_FAN connector)
6. Boot the system and confirm CPU temperatures are within normal range (idle: below 50°C; load: below 90°C for most desktop CPUs)

---

## 6.0 Post-Repair Functionality Test

After completing the repair and reassembling the computer, a full functionality test must be performed before the unit is returned to the user.

| Test | Method | Pass Criteria |
|------|--------|---------------|
| POST and boot | Power on; observe POST; boot to OS login screen | No error messages or unusual beep codes; OS loads normally |
| RAM recognition | BIOS/UEFI System Information screen | Full installed RAM capacity detected |
| Storage recognition | BIOS/UEFI storage list; Windows Disk Management | All installed drives detected; OS drive shows correct capacity |
| Temperature check | HWMonitor or BIOS hardware monitor after 10 minutes at idle | CPU below 50°C; GPU below 50°C; HDD/SSD below 45°C at idle |
| Replaced component stress test | Run Memtest86 (RAM) or CrystalDiskMark (storage) for 15–30 minutes | No errors; performance within expected range |
| Network connectivity | `ping 8.8.8.8`; open a web browser | Network responds; internet accessible |
| OS and application launch | Open OS settings, file manager, and key business applications | No crashes or error messages |
| All peripherals functional | Test keyboard, mouse, external drives, display outputs | All peripherals respond correctly |

---

## 7.0 Common Errors in On-Site Repair

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Not wearing anti-static wrist strap | ESD damage to CPU, RAM, or motherboard | Always strap up before touching internal components |
| Forcing connectors | Bent pins, broken sockets | Check connector orientation before inserting; never force |
| Over-applying thermal paste | Paste spreads onto motherboard socket; poor thermal contact | Use a pea-sized amount at the centre only |
| Not testing after reassembly | Fault reoccurs; unit returned incomplete | Always complete the full functionality test checklist before returning the unit |
| Replacing components without confirming the fault | Unnecessary expense; original fault persists | Diagnose with tools first; replace only confirmed faulty components |
| Losing screws or small parts | Incomplete reassembly; loose components cause shorts | Use a magnetic parts tray; keep screws organised by location |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCU 3: Computer System Repair
- CompTIA A+ Core 1 (220-1101) — Hardware Troubleshooting, Storage, RAM, PSU
- Intel ATX12V Power Supply Design Guide — PSU voltage tolerances
- Memtest86 Official Documentation — memtest86.com
- CrystalDiskInfo SMART Attribute Reference
- Manufacturer BIOS reference guides (AMI, Award, Phoenix)