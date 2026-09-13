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
| KOD DAN NAMA PROGRAM | IT-020-4:2013 PENTADBIRAN SISTEM KOMPUTER |
| TAHAP | 4 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C01 SERVER CONFIGURATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE SERVER CONFIGURATION REQUIREMENTS<br>2. PLAN SERVER ROLES AND SERVICES<br>3. CONFIGURE SERVER HARDWARE AND STORAGE<br>4. CONFIGURE SERVER OS AND ROLES<br>5. IMPLEMENT SERVER SECURITY SETTINGS<br>6. DOCUMENT SERVER CONFIGURATION |
| NO. KOD | IT-020-4:2013-C01/KK(3/6) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-03-configuring-server-hardware-and-storage

**TUJUAN:** Kertas rujukan untuk KK-03-configuring-server-hardware-and-storage.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

Configure a physical or simulated enterprise server: verify hardware health, configure BIOS/UEFI settings for production use, create a RAID array using the hardware RAID controller, and validate the storage configuration using out-of-band management tools.

---

## Tempoh / Duration

10 hours (practical session across multiple days as required)

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Enterprise server (Dell PowerEdge, HPE ProLiant, or equivalent) — physical or lab simulation | 1 per trainee or small group |
| 2 | Server RAID controller (hardware, e.g. Dell PERC, HPE Smart Array) | 1 (built into server) |
| 3 | Enterprise SAS or NVMe drives (minimum 4, matching capacity and type) | 4+ |
| 4 | Spare drive for hot spare configuration | 1 |
| 5 | Management workstation with network connection to server management VLAN | 1 |
| 6 | Anti-static wrist strap | 1 per person |
| 7 | Server hardware documentation / datasheet | 1 |
| 8 | BIOS/UEFI configuration checklist (from KP-03) | 1 |
| 9 | RAID configuration worksheet | 1 |

---

## Langkah Keselamatan / Safety Precautions

- Wear anti-static wrist strap at all times when handling server components; connect strap to a grounded point on the server chassis
- Ensure server power is OFF before removing or inserting drive caddies (unless drives are certified hot-swap and the RAID controller supports hot-plug for that operation)
- Do not force drive caddies — align correctly before sliding in; forcing damages the SAS/SATA connector
- Do not configure RAID on disks that contain existing data without explicit written authorisation — RAID configuration will destroy all data on the selected disks
- Verify the RAID controller's battery-backed write cache (BBWC) or flash-backed write cache (FBWC) is healthy before enabling write-back cache mode

---

## Prosedur / Procedures

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 1 | **Physical inspection:** Power on the server. Observe the POST (Power-On Self-Test) display. Record any POST error codes. Open the server chassis (power off first); inspect seating of all DIMMs, PCIe cards, and drive caddies. Reseat any components that appear loose. |
| 2 | **IPMI / iDRAC initial configuration:** Connect the management port to the management VLAN. Access the iDRAC/iLO web interface at the default IP (or via the physical front panel LCD). Change the default credentials immediately: set a strong password for the admin account. Assign a static IP address, subnet, and gateway for the management interface. |
| 3 | **Hardware health verification (iDRAC/iLO):** Log into the management interface. Navigate to the hardware health dashboard. Verify: all fans are spinning at normal speed (green), all PSUs are online (green), all temperature sensors are within normal range, no memory errors in the SEL (System Event Log). Record the iDRAC firmware version. |
| 4 | **BIOS/UEFI configuration:** Reboot the server and enter BIOS/UEFI setup (F2 or Del during POST, per vendor). Apply the following settings using the checklist from KP-03 Section 4: Boot mode = UEFI; Secure Boot = Enabled; Hyper-Threading = Enabled; VT-x/AMD-V = Enabled; VT-d/AMD-Vi = Enabled; C-States = OS Controlled (or Maximum Performance); Memory speed = rated profile; Boot order: Network PXE first, then USB, then local disk. Save and note all changes made. |
| 5 | **RAID controller access:** Reboot the server. During POST, press the key combination to enter the RAID controller configuration utility (e.g. Ctrl+R for Dell PERC, F5 for HPE Smart Array). The key combination is displayed on the POST screen. |
| 6 | **Physical disk verification:** In the RAID utility, view all detected physical disks. Verify: disk count matches installed drives, all disks show "Online" or "Ready" status (not "Failed" or "Foreign"), disk capacities are correct. |
| 7 | **RAID configuration — OS volume:** Create the first logical drive for the OS. Select RAID 1; select 2 disks of equal capacity; set stripe size to 64 KB; name the logical drive "OS-RAID1". Set the Read Policy to Read Ahead (Adaptive); Write Policy to Write Back (with BBWC/FBWC); I/O Policy to Direct. Begin Fast Initialisation. |
| 8 | **RAID configuration — Data volume:** Create the second logical drive for data. Select the RAID level specified in the Server Role Plan (e.g. RAID 10 for database, RAID 5 for file server); select the appropriate disks; configure stripe size; name the logical drive "DATA-RAID10" or "DATA-RAID5" as appropriate. Assign the remaining drive(s) as a Global Hot Spare. |
| 9 | **RAID verification:** After configuration, view the logical drive status in the RAID utility. Confirm: both logical drives show "Optimal" status, hot spare shows "Hot Spare" status, BBWC/FBWC shows "Charged" (green). Note the exact RAID configuration in the RAID Configuration Worksheet. |
| 10 | **Post-RAID verification via iDRAC:** After exiting the RAID utility and booting to a live environment (USB bootable diagnostic tool or OS), verify the logical drives are visible to the OS. On Windows PE: open Disk Management; on Linux live: run `lsblk`. Confirm logical drive sizes are as expected (after RAID overhead). |
| 11 | **Document the configuration:** Complete the RAID Configuration Worksheet: physical disk model, serial numbers, capacity; RAID level per logical drive; logical drive name, size, and purpose; hot spare assignment; BBWC/FBWC status; iDRAC IP and firmware version; all BIOS settings changed from default. |
| 12 | **Complete the assessment checklist** and submit the RAID Configuration Worksheet and completed checklist to the instructor. |

---

## Hasil Dijangka / Expected Outcome

- Server hardware health verified with no unresolved errors in the System Event Log
- BIOS/UEFI configured according to the production checklist; all changes documented
- Two RAID logical drives created: OS-RAID1 (RAID 1) and DATA volume (RAID level per plan), both in Optimal status
- At least one hot spare configured
- iDRAC management interface configured with static IP and changed credentials
- Completed RAID Configuration Worksheet submitted

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Anti-static strap worn throughout hardware handling | [ ] Yes  [ ] No |
| 2 | POST errors checked and recorded before proceeding | [ ] Yes  [ ] No |
| 3 | iDRAC/iLO default credentials changed; static IP assigned | [ ] Yes  [ ] No |
| 4 | Hardware health verified via iDRAC — no critical errors | [ ] Yes  [ ] No |
| 5 | BIOS/UEFI: UEFI mode, Secure Boot, VT-x, and C-States configured correctly | [ ] Yes  [ ] No |
| 6 | RAID utility accessed during POST | [ ] Yes  [ ] No |
| 7 | OS-RAID1 (RAID 1) created and shows Optimal status | [ ] Yes  [ ] No |
| 8 | Data RAID volume created with correct RAID level per plan | [ ] Yes  [ ] No |
| 9 | Hot spare assigned | [ ] Yes  [ ] No |
| 10 | BBWC/FBWC status verified as Charged | [ ] Yes  [ ] No |
| 11 | Logical drives visible in OS/live environment | [ ] Yes  [ ] No |
| 12 | RAID Configuration Worksheet completed and submitted | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |