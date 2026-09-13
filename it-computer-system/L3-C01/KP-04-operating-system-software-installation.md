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
| NO. KOD | IT-020-3:2013-C01/KP(4/7) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-04-operating-system-software-installation

**TUJUAN:** Kertas rujukan untuk KP-04-operating-system-software-installation.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Describe the types of software installed during computer system set-up
2. Explain the operating system installation process including BIOS/UEFI configuration
3. State the correct order for driver installation
4. Identify common software installation faults and troubleshooting steps

---

## 1.0 Introduction

Software installation transforms assembled hardware into a functional computer system. This work activity covers installing the operating system, device drivers, and applications as specified in the job request. Proper software installation ensures the system is stable, secure, and ready for the end user.

---

## 2.0 Types of Software

### 2.1 Operating System (OS)

Windows, Linux, or other OS as per the job request. Installation media (USB or disc) and a valid licence or key are required. The installer partitions the drive, copies files, and configures the initial user and settings. Updates and drivers are applied after the base install.

### 2.2 Drivers

Device drivers for the motherboard (chipset, LAN, audio), GPU, and peripherals. Often supplied by the OS or from the manufacturer website. Missing or wrong drivers can cause devices not to work or to perform poorly. Install in the order recommended by the manufacturer (e.g. chipset first).

**Recommended driver installation order:**
1. Chipset driver
2. GPU / display driver
3. Network (LAN / Wi-Fi) driver
4. Audio driver
5. Other device-specific drivers (USB controllers, Bluetooth, etc.)

### 2.3 Applications

Office suite, browser, antivirus, and other applications as specified in the change order or standard build. May be installed from media, network share, or app store. Licence keys and configuration (e.g. default browser, updates) are applied according to organisational policy.

### 2.4 System Utilities and Firmware

Built-in tools (disk management, device manager, task manager) and BIOS/UEFI firmware used to configure, monitor, and troubleshoot the system after installation. Firmware updates may be needed for hardware compatibility. Utilities are used during set-up to verify partitions, check device status, and confirm system performance before user handover.

---

## 3.0 BIOS/UEFI Configuration Before OS Installation

Before booting from the installation media, the technician must configure BIOS/UEFI settings:

| Setting | Purpose |
|---------|---------|
| Boot order | Set USB or optical drive as the first boot device |
| Secure Boot | Enable or disable depending on the OS (some Linux installers require disabling) |
| UEFI vs Legacy/CSM | Select UEFI mode for modern OS installations; Legacy/CSM for older systems |
| XMP/EXPO profile | Enable to run RAM at its rated speed (if supported) |
| TPM | Enable TPM 2.0 for Windows 11 requirements |
| Storage mode | Set to AHCI for SSD/NVMe performance (not IDE mode) |

---

## 4.0 OS Installation Process

1. Connect monitor, keyboard, and mouse; power on the system
2. Enter BIOS/UEFI (typically DEL, F2, or F12 during POST)
3. Verify hardware detection: CPU, RAM, storage drives
4. Set boot order to USB first
5. Save BIOS settings and reboot
6. Boot from USB installer
7. Follow OS installation prompts: language, edition, licence key
8. Partition the storage drive according to job requirements
9. Complete base OS installation and initial configuration (username, password, region)
10. Remove USB installer and reboot into the installed OS
11. Install drivers in the correct order
12. Apply OS updates and security patches
13. Verify all devices in Device Manager -- no unknown devices or errors

---

## 5.0 Common Software Installation Faults

| Common Fault | Cause | Action |
|--------------|-------|--------|
| OS installer not booting | Boot order wrong; secure boot or legacy setting; corrupted USB | Set boot order in BIOS/UEFI; disable secure boot for some installers; recreate USB installer |
| Driver or device not working | Wrong or missing driver; driver not installed after OS | Install correct driver from manufacturer; run Windows Update or equivalent |
| OS activation failure | Invalid or already-used licence key; no internet connection | Verify licence key; ensure network connectivity for online activation |
| Application installation error | Insufficient disk space; missing prerequisites (.NET, VC++ runtime) | Check disk space; install required prerequisites first |

---

## 6.0 Post-Installation Verification

After completing software installation:
- Open Device Manager and confirm all devices are recognised (no yellow triangles)
- Verify network connectivity (ping a known address or open a website)
- Confirm the OS is activated and licensed
- Check that all specified applications are installed and launch correctly
- Run Windows Update (or equivalent) to ensure all patches are current

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation -- CoCu 1
- Microsoft Windows Server 2025 Installation and Configuration Guide
- CompTIA A+ Certification Study Guide -- OS Installation and Configuration
- American Megatrends (AMI) BIOS/UEFI Setup Documentation