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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C07 MOBILE DEVICE CONFIGURATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE JOB ORDER/CHANGE REQUEST<br>2. CARRY OUT MOBILE DEVICE CONFIGURATION<br>3. PERFORM MOBILE DEVICE TROUBLESHOOT<br>4. CARRY OUT MOBILE DEVICE COMMISSIONING |
| NO. KOD | IT-020-3:2013-C07/KP(1/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-01-analyse-mobile-job-order

**TUJUAN:** Kertas rujukan untuk KP-01-analyse-mobile-job-order.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the purpose and structure of a job order and change request for mobile device configuration
2. Identify mobile device types, specifications, and compatibility requirements from a job order
3. Describe how to verify software, application, and network requirements for mobile devices
4. List the key decision criteria when analysing a mobile device job order

---

## 1.0 Introduction to Mobile Device Job Order Analysis

A job order (also called a work order or service request) is the formal document that initiates a mobile device configuration task. It is issued by the supervisor, IT department, or end-user and contains the device details and configuration requirements the technician must follow. Accurate analysis of the job order is the foundation of a successful mobile device configuration — errors at this stage lead to wrong application installations, incompatible OS versions, or unmet user requirements.

A change request (Permintaan Perubahan) is a formal modification to an existing job order. It may add requirements (e.g., additional email account), change specifications (e.g., different OS version), or cancel parts of the original request. Change requests must be documented and approved before work proceeds.

Mobile devices covered under this CoCU include:

| Device Type / Jenis Peranti | Description |
|-----------------------------|-------------|
| Smartphone (Telefon Pintar) | Pocket-sized communication device with full OS (Android / iOS), cellular connectivity, and app ecosystem |
| Tablet | Larger touchscreen device running Android or iOS/iPadOS; used for productivity and media |
| PDA (Personal Digital Assistant) | Legacy handheld device; may still appear in specialised field or logistics environments |
| Navigation Device (Peranti Navigasi) | GPS-enabled device; may require map data and connectivity configuration |

---

## 2.0 Job Order Structure for Mobile Devices

A typical mobile device job order contains the following fields:

| Field / Medan | Description / Keterangan |
|---------------|--------------------------|
| Job order number (No. Pesanan Kerja) | Unique identifier for tracking and record-keeping |
| Date issued (Tarikh Dikeluarkan) | Date the request was created |
| Requested by (Dimohon Oleh) | Name and department of the person or entity requesting configuration |
| Priority (Keutamaan) | Urgency level — Normal, High, or Critical |
| Device details (Maklumat Peranti) | Brand / model, IMEI, serial number, OS version, current firmware |
| Configuration scope (Skop Konfigurasi) | What must be set up — email, VPN, MDM enrolment, applications, accounts |
| Network requirements (Keperluan Rangkaian) | Wi-Fi SSID/password, APN settings, VPN profile |
| Application list (Senarai Aplikasi) | Applications to be installed, including version and source (Play Store / App Store / MDM) |
| Security requirements (Keperluan Keselamatan) | Screen lock type, encryption, MDM policy, remote wipe capability |
| Delivery date (Tarikh Selesai) | When the configuration must be completed |
| Approver (Pelulus) | Person authorising the job order |

---

## 3.0 Mobile Device Types and Specifications

When analysing a job order, the technician must verify the device specifications to ensure all configuration requirements are achievable on the target device.

### 3.1 Key Device Specifications / Spesifikasi Peranti Utama

| Specification / Spesifikasi | Relevance to Configuration |
|-----------------------------|---------------------------|
| Brand / Model (Jenama / Model) | Determines available settings menus, manufacturer customisations, and compatible accessories |
| RAM capacity (Kapasiti RAM) | Affects whether the required applications can run simultaneously without performance issues |
| Storage size (Saiz Storan) | Determines whether sufficient space exists for OS updates and application installations |
| Display type (Jenis Paparan) | Relevant for screen resolution settings and accessibility configuration |
| Input method (Kaedah Input) | Touchscreen, stylus, or physical keyboard — affects on-screen keyboard and language settings |
| Connectivity (Sambungan) | Wi-Fi bands (2.4 GHz / 5 GHz), Bluetooth version, NFC, USB type (Type-C / Lightning / Micro-USB), USB OTG |
| OS and OS version (OS dan Versi OS) | Determines which applications are compatible and which configuration menus are available |

### 3.2 Operating System Platforms

| Platform | Common Versions | App Source |
|----------|----------------|------------|
| Android | 9.0 Pie, 10, 11, 12, 13, 14 | Google Play Store |
| iOS / iPadOS | iOS 14, 15, 16, 17 | Apple App Store |

---

## 4.0 Application and Software Requirements

Before proceeding with configuration, the technician must identify and verify all application and software requirements stated in the job order.

### 4.1 Types of Applications and Software / Jenis Aplikasi dan Perisian

| Category | Examples |
|----------|----------|
| Productivity (Produktiviti) | Microsoft 365 (Word, Excel, Outlook), Google Workspace |
| Communication (Komunikasi) | Microsoft Teams, Zoom, WhatsApp Business |
| Enterprise / MDM client | Microsoft Intune Company Portal, VMware Workspace ONE |
| Security | VPN client (Cisco AnyConnect, FortiClient), antivirus |
| Utilities | File manager, PDF reader, barcode scanner |

### 4.2 Software Licences / Lesen Perisian

| Licence Type | Description |
|--------------|-------------|
| Proprietary licence (Lesen Hak Milik) | Requires purchase or subscription; must verify licence availability before installation |
| Open-source licence (Lesen Sumber Terbuka) | Free to use; verify compliance with organisational policy |
| Enterprise licence | Organisation-wide licence managed via MDM or volume purchase programme |

### 4.3 Software Version Verification / Pengesahan Versi Perisian

The technician must confirm:

1. The required application version is compatible with the device OS version
2. The device OS version meets the minimum requirement for each application
3. OS updates required by the job order can be applied to the specific device model
4. Application updates are available from the correct app store for the platform (Play Store for Android; App Store for iOS)

---

## 5.0 Compatibility Verification / Pengesahan Kesesuaian

### 5.1 Hardware and Software Compatibility / Kesesuaian Perkakasan dan Perisian

| Compatibility Check | What to Verify |
|---------------------|----------------|
| OS version vs. application requirement | Minimum Android / iOS version stated in app requirements |
| Storage availability | At least 15–20% free internal storage after all installations |
| RAM availability | Device RAM meets recommended requirement for enterprise applications |
| Connectivity standard | USB cable type matches device port — USB Type-A, Type-B, Lightning (iPhone), USB-C, USB OTG |

### 5.2 Network Compatibility / Kesesuaian Rangkaian

- Verify device supports the required Wi-Fi frequency band (2.4 GHz or 5 GHz)
- Confirm cellular band compatibility if SIM-based connectivity is required
- Check that VPN protocol supported by device OS matches the organisational VPN server configuration

### 5.3 Security Settings Compatibility / Kesesuaian Tetapan Keselamatan

- Device OS must support the MDM enrolment method specified (Android Enterprise / Apple Device Enrolment Programme)
- Encryption requirements (e.g., AES-256) must be supported by device hardware
- Screen lock policy (PIN length, biometric type) must be enforceable on the device OS version

---

## 6.0 Requirements Extraction Process

When analysing a mobile device job order, the technician should follow this systematic approach:

1. **Read the entire job order** before taking any action. Note any fields that are incomplete or unclear.
2. **Verify device specifications** — confirm brand, model, current OS version, storage, and connectivity interfaces against the job order requirements.
3. **Verify application requirements** — confirm OS compatibility, licence availability, and correct app store source for each listed application.
4. **Check for incompatibilities** — identify any mismatch between device OS version and required applications or MDM policies.
5. **Identify missing information** — if the job order does not specify a detail (e.g., Wi-Fi password, email server address), clarify with the requestor before proceeding.
6. **Document the analysis** — record verified requirements, identified gaps, and the planned configuration sequence for approval before starting work.

---

## 7.0 Common Errors in Mobile Job Order Analysis

| Error / Kesilapan | Consequence / Akibat | Prevention / Pencegahan |
|-------------------|----------------------|-------------------------|
| Not verifying OS version | Application fails to install due to incompatible OS | Check minimum OS version in app requirements before proceeding |
| Assuming device has sufficient storage | Installation fails mid-process | Check available storage; confirm at least 20% free space |
| Not confirming connectivity type | Wrong USB cable used; data transfer or charging fails | Identify device port type from model specification — USB-C, Lightning, or Micro-USB |
| Proceeding without licence verification | Unlicensed software installed on organisational device | Confirm licence availability with IT department before installation |
| Not documenting change requests | Untracked deviations from original job order | Record all changes on an approved change request form |
| Ignoring network coverage availability | Configuration steps requiring internet access cannot be completed | Verify Wi-Fi or cellular coverage at the configuration location |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCU 7: Mobile Device Configuration
- Jennifer's Teaching Plan Reference: IT-020-3:2013-C07/P(2/6)PM — Jenis dan Spesifikasi Peranti
- Google Android Documentation — developer.android.com
- Apple iOS Deployment Reference — support.apple.com/enterprise
- CompTIA A+ Certification Study Guide — Mobile Devices Chapter