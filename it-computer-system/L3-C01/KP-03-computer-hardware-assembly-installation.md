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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C01 COMPUTER SYSTEM SET-UP |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE JOB ORDER/CHANGE REQUEST<br>2. PREPARE COMPUTER SET-UP TOOLS, COMPUTER HARDWARE PARTS AND COMPUTER SOFTWARE<br>3. SET-UP COMPUTER HARDWARE<br>4. CARRY OUT COMPUTER SOFTWARE INSTALLATION<br>5. SET-UP COMPUTER PERIPHERALS<br>6. CARRY OUT UNIT FUNCTIONALITY TEST<br>7. PREPARE COMPUTER SET-UP REPORT |
| NO. KOD | IT-020-3:2013-C01/KP(3/7) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-03-computer-hardware-assembly-installation

**TUJUAN:** Kertas rujukan untuk KP-03-computer-hardware-assembly-installation.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Describe the function and installation procedure of each major hardware component
2. Explain hardware compatibility requirements (socket type, form factor, interface)
3. Identify common hardware installation faults and their causes
4. State the importance of proper thermal paste application and cable management

---

## 1.0 Introduction

Hardware assembly is the core practical activity in computer system set-up. It involves physically installing all components into the computer case and connecting them correctly. This work activity accounts for 30% (90 hours) of the total CU hours, reflecting its importance and complexity.

---

## 2.0 Hardware Components

### 2.1 CPU (Central Processing Unit)

The processor that executes instructions. It must match the socket type of the motherboard (e.g. LGA1700, AM5). Thermal paste and a heatsink or fan are required; the paste fills microscopic gaps between the CPU and heatsink for efficient heat transfer. Incorrect installation can cause overheating and permanent damage.

**Installation notes:**
- Align the CPU with the socket indicator (triangle or notch)
- Lower the CPU gently into the socket; never force it
- Apply a pea-sized amount of thermal paste to the centre of the CPU
- Attach the heatsink/fan and connect the fan cable to the CPU_FAN header

### 2.2 RAM (Random Access Memory)

Temporary storage for running programs and data. Types include DDR5; capacity and speed must be compatible with the motherboard and CPU. Modules are installed in the correct slots (often pairs for dual-channel). Not fully seated or incompatible RAM can cause no POST or random crashes.

**Installation notes:**
- Identify the correct slots for dual-channel configuration (refer to motherboard manual)
- Open the retention clips on the RAM slot
- Align the notch on the module with the key in the slot
- Press firmly and evenly until the retention clips snap into place

### 2.3 Motherboard

The main board that connects the CPU, RAM, storage, and peripherals. Form factor (e.g. ATX, micro-ATX) determines case compatibility. The BIOS or UEFI firmware is used to set boot order, secure boot, and hardware options. All other components connect to the motherboard.

**Installation notes:**
- Install the I/O shield into the case before inserting the motherboard
- Align the motherboard with the standoffs in the case
- Secure with the correct screws; do not overtighten
- Ensure no standoff is under the board where there is no mounting hole (risk of short circuit)

### 2.4 Storage (HDD / SSD / NVMe)

HDD (hard disk drive) is used for bulk storage at lower cost; SSD and NVMe offer much faster boot and application load. Interface (SATA, M.2 PCIe Gen5) must match the motherboard.

**Installation notes:**
- SATA drives: mount in the drive bay, connect SATA data cable and SATA power cable
- NVMe Gen5 drives: insert into the M.2 PCIe Gen5 slot at an angle, press down, and secure with the standoff and screw
- Verify the drive is detected in BIOS/UEFI after installation

### 2.5 Power Supply Unit (PSU)

Converts AC from the wall to DC and supplies the correct voltages to the motherboard and components. Wattage must meet the total system requirement (CPU, GPU, drives). Cabling must match the motherboard (e.g. 24-pin, 8-pin CPU, PCIe for GPU). Modular PSUs allow unused cables to be left off for better airflow.

**Installation notes:**
- Mount the PSU in the case (usually at the bottom)
- Connect the 24-pin ATX power connector to the motherboard
- Connect the 8-pin (or 4+4 pin) CPU power connector
- Connect PCIe power connectors to the GPU if applicable
- Connect SATA power connectors to storage drives

### 2.6 Peripherals

Monitor, keyboard, mouse, printer, and other devices. Connected via USB, HDMI or DisplayPort, or legacy ports as specified in the job request. Drivers and settings (e.g. resolution, refresh rate) are configured during software installation and set-up.

---

## 3.0 Common Faults During Hardware Set-up

| Common Fault | Cause | Action |
|--------------|-------|--------|
| No power / no POST | PSU not switched on, power cable loose, front-panel wires wrong, or PSU fault | Check power cable and switch; verify front-panel header; test with known-good PSU if needed |
| No display | Monitor not connected or wrong input; GPU not seated; RAM not seated | Check cable and input; reseat GPU and RAM; try onboard video if available |
| System instability / crashes | RAM not fully seated, incompatible RAM, or insufficient PSU wattage | Reseat RAM; verify compatibility; check PSU wattage rating |
| Overheating at first boot | Thermal paste not applied or CPU cooler not properly attached | Reapply thermal paste; verify cooler mounting and fan connection |

---

## 4.0 Cable Management

Proper cable management is essential for:
- **Airflow:** Cables that obstruct fans or vents cause higher temperatures
- **Maintenance:** Organised cables make troubleshooting and upgrades easier
- **Safety:** Loose cables can contact moving parts (fans) or short circuit

Best practices:
- Route cables behind the motherboard tray where possible
- Use cable ties or velcro straps to bundle cables
- Keep power and data cables separated where practical
- Ensure no cable obstructs the CPU or case fans

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation -- CoCu 1
- CompTIA A+ Certification Study Guide -- Hardware Installation
- Intel ARK Processor Specifications -- Socket Compatibility and TDP
- JEDEC DDR5 Memory Standard