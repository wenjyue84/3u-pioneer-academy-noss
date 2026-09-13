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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C04 SERVER INSTALLATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE JOB ORDER/CHANGE REQUEST<br>2. EXECUTE HARDWARE INSTALLATION<br>3. CARRY OUT SOFTWARE INSTALLATION<br>4. PERFORM SERVER FUNCTIONALITY TEST<br>5. PREPARE SERVER INSTALLATION SET-UP REPORT |
| NO. KOD | IT-020-3:2013-C04/KK(3/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-03-server-software-installation

**TUJUAN:** Kertas rujukan untuk KK-03-server-software-installation.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objectives

Upon completing this activity, the trainee will be able to:
- Boot a rack-mount server from installation media and complete a server OS installation
- Partition and format server storage drives according to best practice
- Configure server roles and features as specified in the job order
- Apply post-installation settings including hostname, IP address, DNS, and time zone

---

## Peralatan / Equipment Required

| No. | Item | Kuantiti / Quantity |
|-----|------|---------------------|
| 1 | Rack-mount server with hardware installed (from KK-02) | 1 |
| 2 | Server OS installation media (USB bootable or ISO via iDRAC/iLO) | 1 |
| 3 | Valid OS licence key (or evaluation key) | 1 |
| 4 | Approved job order / software requirement sheet | 1 |
| 5 | KVM console (keyboard, video, mouse) or remote console access | 1 set |
| 6 | Network patch cable | 1 |
| 7 | Network switch port assigned per job order | 1 |

---

## Langkah Keselamatan / Safety Precautions

- Verify the OS licence key and installation media are from authorised sources before beginning installation
- Do not connect the server to the production network until the OS is fully configured and the instructor has approved the configuration
- Do not use unlicensed or trial software unless the instructor has specifically approved it for training purposes
- Record all credentials (local administrator password, IPMI/iDRAC access) in the job order documentation — do not store passwords on loose paper
- Ensure the server room or training lab temperature is within operating range before powering on

---

## Prosedur / Procedure

| Langkah | Arahan / Instruction |
|---------|----------------------|
| 1 | **Power on and enter BIOS/UEFI.** Connect the KVM console to the server. Power on the server. Press the designated key (Del, F2, or F11 as shown on the POST screen) to enter the BIOS/UEFI setup. |
| 2 | **Verify hardware detection.** In the BIOS/UEFI, confirm that all installed CPUs, RAM modules, and storage drives are detected and match the job order specifications. If any component is missing, power off and reseat the component before continuing. |
| 3 | **Configure boot order.** Set the boot device priority: USB drive or virtual media (ISO) first. Save changes and exit BIOS/UEFI. |
| 4 | **Boot from installation media.** Insert the bootable USB drive or mount the ISO via the server's remote management interface (iDRAC, iLO, or IPMI). Restart the server. Confirm the OS installation wizard loads. |
| 5 | **Begin OS installation.** Select the language, time and currency format, and keyboard layout as specified in the job order. Click Install. |
| 6 | **Enter the licence key.** Input the OS licence key when prompted. Select the correct OS edition (e.g., Standard or Datacenter). Proceed. |
| 7 | **Select installation type.** Choose Custom installation (not upgrade). |
| 8 | **Configure disk partitions.** Delete existing partitions on the target OS drive. Create partitions as specified in the job order: (a) System Reserved partition (minimum 500 MB), (b) OS partition (minimum 60 GB for the system volume), (c) additional data partitions as required. Format each partition as NTFS (for Windows Server) or ext4/XFS (for Linux). |
| 9 | **Complete OS installation.** Select the OS partition and proceed with installation. The server will restart one or more times automatically. Do not interrupt the process. |
| 10 | **Initial configuration after first boot.** Set the local administrator password according to the organisation's password policy (minimum 12 characters, complexity enabled). Log in for the first time. |
| 11 | **Configure server identity.** Set the server hostname as specified in the job order. Set the correct time zone and synchronise the clock with the designated NTP server. |
| 12 | **Configure network settings.** Open the network adapter settings. Assign the static IP address, subnet mask, default gateway, and DNS server addresses as specified in the job order. Test connectivity by pinging the default gateway. |
| 13 | **Install server roles and features.** Using Server Manager (Windows) or the appropriate package manager (Linux), install all server roles listed in the job order (e.g., Active Directory Domain Services, DNS Server, DHCP Server, File and Storage Services, IIS). Restart the server if prompted. |
| 14 | **Apply OS updates and drivers.** Run Windows Update or the Linux package update command. Install any server-specific drivers (chipset, NIC, HBA, RAID controller) from the manufacturer's support site or the server OEM's driver pack. Restart as required. |
| 15 | **Verify installation.** Open the Server Manager dashboard or equivalent. Confirm all installed roles show a healthy status. Record the OS version, installed roles, IP address, and hostname on the job order documentation. Submit to the instructor for review before proceeding to KK-04. |

---

## Hasil Dijangka / Expected Outcome

A fully configured server with:
- Server OS installed on the correct partition with appropriate disk layout
- Server hostname, IP address, DNS, and time zone correctly configured
- All required server roles and features installed and operational
- OS and drivers updated to current versions
- Administrator credentials documented and secured
- Network connectivity confirmed (gateway ping successful)

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Hardware correctly detected in BIOS/UEFI before installation | [ ] Yes  [ ] No |
| 2 | OS installed from authorised media with valid licence key | [ ] Yes  [ ] No |
| 3 | Disk partitioned and formatted as specified in job order | [ ] Yes  [ ] No |
| 4 | Hostname set correctly per job order | [ ] Yes  [ ] No |
| 5 | Static IP address, subnet mask, gateway, and DNS configured | [ ] Yes  [ ] No |
| 6 | Time zone set and NTP synchronisation configured | [ ] Yes  [ ] No |
| 7 | All required server roles and features installed | [ ] Yes  [ ] No |
| 8 | OS updates and device drivers applied | [ ] Yes  [ ] No |
| 9 | Network connectivity verified (gateway ping successful) | [ ] Yes  [ ] No |
| 10 | Installation details recorded and submitted for instructor review | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Nama / Name | Tandatangan / Signature | Tarikh / Date |
|---|-------------|-------------------------|---------------|
| Pelatih / Trainee | | | |
| Pengajar / Instructor | | | |