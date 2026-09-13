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
| NO. KOD | IT-020-3:2013-C07/KP(4/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-04-mobile-device-commissioning

**TUJUAN:** Kertas rujukan untuk KP-04-mobile-device-commissioning.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the purpose and scope of mobile device commissioning
2. Describe the pre-handover verification checklist for a configured mobile device
3. Explain the procedure for handing over a mobile device to the user
4. Prepare and complete a mobile device commissioning report

---

## 1.0 Introduction to Mobile Device Commissioning

Mobile device commissioning (Pentauliahan Peranti Mudah Alih) is the final stage of the mobile device configuration workflow. It is the formal process of verifying that the device has been correctly configured according to the job order, obtaining user acceptance, and transferring custody of the device to the end user or organisation.

Commissioning ensures:

- All configuration tasks specified in the job order have been completed
- The device functions correctly in the target environment (not just on the technician's bench)
- The user understands how to use the device and is satisfied with the setup
- All documentation is completed and signed off for audit and asset management purposes

Commissioning is distinct from configuration testing (KP-02) and troubleshooting (KP-03). Those activities verify that individual settings work; commissioning verifies the complete, integrated device against the full job order scope and formalises the handover.

---

## 2.0 Pre-Handover Verification Checklist / Senarai Semak Pengesahan Pra-Serah

Before handing over the device, the technician must perform a systematic final check against the job order. Every item must be verified and the result recorded (Pass / Fail).

### 2.1 Device and Identity Verification / Pengesahan Peranti dan Identiti

| Check Item | Verification Method | Expected Result |
|------------|--------------------|-----------------| 
| Device brand, model, and serial number match job order | Compare physical device label / Settings → About → Serial Number against job order | Match confirmed |
| IMEI number recorded (SIM-capable devices) | Settings → About → IMEI or dial *#06# | IMEI recorded in commissioning report |
| OS version matches required version | Settings → About → Software Information | OS version meets or exceeds job order requirement |
| Device name / hostname set correctly | Settings → About → Device Name | Name matches organisational naming convention (if specified) |

### 2.2 Configuration Verification / Pengesahan Konfigurasi

| Check Item | Verification Method | Expected Result |
|------------|--------------------|-----------------| 
| Wi-Fi connected to correct SSID | Settings → Wi-Fi | Connected; internet accessible |
| Mobile data active (if applicable) | Settings → Mobile Network → Mobile Data | Active; correct APN configured |
| Email account configured and syncing | Open mail app; send and receive a test email | Email sent and received successfully |
| Calendar and contacts syncing | Open calendar app; verify entries from server appear | Sync active; entries visible |
| VPN profile installed and connects | Settings → VPN; connect and verify | VPN connects; internal resource accessible |
| MDM enrolment confirmed | MDM console → device list | Device listed as enrolled and compliant |
| All required applications installed | Compare installed apps against job order app list | All applications present and launch without error |
| Screen lock active and policy-compliant | Lock screen and attempt unlock | Locks at configured timeout; correct unlock method works |
| Encryption enabled (if required) | Settings → Security → Encryption | Encryption active (Android); enabled by default on iOS |
| Date and time correct and auto-synced | Settings → Date and Time | Correct time displayed; "automatic" enabled |

### 2.3 Environment Test / Ujian Persekitaran

The environment test is performed in or near the user's actual working environment, not only in the technician's workspace:

| Test | Purpose |
|------|---------|
| Wi-Fi signal at user's workstation | Confirm adequate signal strength at the user's actual location |
| Email receive in real time | Verify push notification delivers emails without delay |
| VPN connectivity from user location | Confirm VPN works from the user's network segment |
| Application login with user credentials | Confirm the user can log in to each application with their own credentials |
| Phone call / SIM function (if applicable) | Confirm voice call can be made and received |

---

## 3.0 User Briefing and Handover Procedure / Prosedur Taklimat Pengguna dan Serah Terima

### 3.1 Purpose of User Briefing / Tujuan Taklimat Pengguna

The user briefing (Taklimat Pengguna) ensures the end user understands:

- The device capabilities and configuration scope
- How to use key configured features (email, VPN, apps)
- Security responsibilities (screen lock, password management, reporting loss)
- Acceptable use policy (AUP) — what is and is not permitted on the device
- What to do if a problem arises — who to contact for IT support

### 3.2 Handover Procedure / Prosedur Serah Terima

| Step | Action |
|------|--------|
| 1 | Present the device to the user and confirm the device matches their job order |
| 2 | Demonstrate each configured feature — Wi-Fi, email, VPN, key applications |
| 3 | Explain the screen lock method and ask the user to set their own PIN/password if required by policy |
| 4 | Brief the user on the acceptable use policy and security responsibilities |
| 5 | Allow the user to test the device themselves — send a test email, open required apps, connect to VPN |
| 6 | Address any questions or concerns before sign-off |
| 7 | Obtain the user's signature on the commissioning report / acceptance form |
| 8 | Issue the device accessories checklist — charging cable, case, SIM card (if applicable) |

> **Note:** The technician must not hand over the device until the user has signed the acceptance form. If the user is unavailable, the device must be secured and the handover rescheduled.

---

## 4.0 Commissioning Report / Laporan Pentauliahan

The commissioning report is the formal record that the device has been configured, tested, and accepted. It forms part of the organisation's IT asset register and provides an audit trail for compliance purposes.

### 4.1 Commissioning Report Contents / Kandungan Laporan Pentauliahan

| Section | Content |
|---------|---------|
| Job order reference (Rujukan pesanan kerja) | Job order number and date |
| Device information (Maklumat peranti) | Brand, model, serial number, IMEI, asset tag |
| OS and firmware version (Versi OS dan firmware) | Recorded at time of commissioning |
| Configuration summary (Ringkasan konfigurasi) | List of all configuration tasks completed — Wi-Fi, email, VPN, MDM, applications |
| Verification checklist (Senarai semak pengesahan) | All checklist items with Pass / Fail results |
| Outstanding issues (Isu yang belum selesai) | Any items not completed and reason; escalation reference if applicable |
| Technician declaration (Perakuan juruteknik) | Technician name, signature, and date |
| User acceptance (Penerimaan pengguna) | User name, signature, and date |
| Supervisor / approver sign-off (Tandatangan penyelia) | Supervisor name and signature (if required by organisational procedure) |

### 4.2 Sample Commissioning Report Structure

```
MOBILE DEVICE COMMISSIONING REPORT
Laporan Pentauliahan Peranti Mudah Alih

Job Order No.      : ___________________________
Date               : ___________________________

DEVICE INFORMATION
Brand / Model      : ___________________________
Serial Number      : ___________________________
IMEI               : ___________________________
Asset Tag          : ___________________________
OS Version         : ___________________________

CONFIGURATION COMPLETED      [ ] Wi-Fi  [ ] Email  [ ] VPN  [ ] MDM  [ ] Applications

VERIFICATION CHECKLIST
[ ] Device identity verified          [ ] Wi-Fi connected
[ ] Email syncing                     [ ] VPN connects
[ ] MDM enrolled and compliant        [ ] All apps installed
[ ] Screen lock active                [ ] Date/time synced
[ ] Environment test passed           [ ] User briefed

OUTSTANDING ISSUES : ___________________________

Technician : _____________________ Date : __________  Signature : __________
User       : _____________________ Date : __________  Signature : __________
Supervisor : _____________________ Date : __________  Signature : __________
```

---

## 5.0 Post-Commissioning Actions / Tindakan Selepas Pentauliahan

After handover is complete, the technician must carry out the following actions:

| Action | Purpose |
|--------|---------|
| Update IT asset register (Kemaskini daftar aset IT) | Record device details, assigned user, date of issue, and configuration summary |
| File commissioning report (Failkan laporan pentauliahan) | Store signed copy in the job order file; send copy to IT department |
| Close job order in ticketing system | Mark job order as completed; attach commissioning report |
| Verify MDM console shows device as compliant | Confirm remote management is active after handover |
| Inform supervisor of completion | Provide verbal or written summary of job completion |

---

## 6.0 Common Commissioning Errors

| Error / Kesilapan | Consequence / Akibat | Prevention / Pencegahan |
|-------------------|----------------------|-------------------------|
| Handing over without user acceptance signature | No legal record of handover; disputes about device condition | Always obtain signature before releasing the device |
| Skipping environment test | Configuration that worked on the technician's bench fails at user's workstation | Always test in the actual user environment |
| Not recording IMEI and serial number | Device cannot be tracked if lost or stolen | Record IMEI and serial number in commissioning report before handover |
| Failing to brief user on security responsibilities | User sets weak PIN or installs unapproved applications | Include security briefing as a mandatory step in the handover procedure |
| Closing job order before verifying MDM compliance | Device remains unmanaged after handover | Confirm MDM compliance status in console before closing the job order |
| Not filing the commissioning report | No audit trail; compliance gap | File signed report immediately after handover |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCU 7: Mobile Device Configuration
- Jennifer's Teaching Plan Reference: IT-020-3:2013-C07/P(3/6)PM — Pengujian Konfigurasi Peranti Mudah Alih
- Google Android Enterprise Deployment Guide — support.google.com/work/android
- Apple Business Manager — business.apple.com
- Microsoft Intune Device Compliance Documentation — learn.microsoft.com/intune/compliance
- CompTIA A+ Certification Study Guide — Mobile Device Documentation and Handover