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
| NO. KOD | IT-020-3:2013-C07/KP(3/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-03-mobile-device-troubleshoot

**TUJUAN:** Kertas rujukan untuk KP-03-mobile-device-troubleshoot.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Describe a systematic approach to diagnosing mobile device problems
2. Identify common mobile device faults and their likely causes
3. Explain the procedures to resolve connectivity, application, account, and performance problems
4. Describe how to document troubleshooting actions and outcomes

---

## 1.0 Introduction to Mobile Device Troubleshooting

Mobile device troubleshooting (Penyelesaian Masalah Peranti Mudah Alih) is the process of identifying, diagnosing, and resolving faults on a smartphone or tablet. Problems may arise from hardware faults, OS errors, incorrect configuration, application conflicts, network issues, or user error.

A technician must approach troubleshooting systematically — gathering information, isolating the cause, applying a fix, and verifying the result — before returning the device to the user or proceeding to commissioning.

The troubleshooting process follows a standard cycle:

1. **Identify the problem (Kenal pasti masalah)** — gather information from the user and observe the fault
2. **Establish a probable cause (Tentukan punca yang mungkin)** — narrow down the source using diagnostic checks
3. **Test the probable cause (Uji punca yang mungkin)** — apply a targeted fix or diagnostic test
4. **Verify full functionality (Sahkan fungsi penuh)** — confirm the fix resolved the problem without introducing new issues
5. **Document findings and actions (Dokumentasi penemuan dan tindakan)** — record the fault, cause, resolution, and test results

---

## 2.0 Information Gathering / Pengumpulan Maklumat

Before performing any diagnostic action, the technician should gather the following information:

| Information | Questions to Ask / What to Check |
|-------------|----------------------------------|
| Fault description (Penerangan kerosakan) | What exactly is the problem? When did it start? Is it constant or intermittent? |
| Device details (Maklumat peranti) | Brand, model, OS version, current firmware version |
| Recent changes (Perubahan terkini) | Was a new app installed? Was the OS updated? Was the device dropped or exposed to water? |
| Error messages (Mesej ralat) | Note the exact error message text or error code |
| Fault reproducibility (Kebolehulangan kerosakan) | Can the fault be reproduced consistently? Under what conditions? |
| Network environment (Persekitaran rangkaian) | Is Wi-Fi available? Is mobile data active? Are other devices on the same network working? |

---

## 3.0 Common Mobile Device Problems and Diagnostic Procedures

### 3.1 Connectivity Problems / Masalah Sambungan

#### 3.1.1 Wi-Fi Cannot Connect / Wi-Fi Tidak Dapat Disambung

| Probable Cause | Diagnostic Check | Resolution |
|----------------|-----------------|------------|
| Wrong Wi-Fi password | Re-enter password manually | Forget the network and reconnect with correct credentials |
| Device Wi-Fi disabled | Check Wi-Fi toggle in Settings | Enable Wi-Fi; check Airplane Mode is OFF |
| IP address conflict | Check device IP via Settings → Wi-Fi → network details | Set static IP or release/renew DHCP lease (toggle Wi-Fi OFF then ON) |
| Router / AP fault | Test with another device on the same SSID | If other devices also fail, escalate to network administrator |
| MAC address filtering | Check router settings (requires admin access) | Register device MAC address in router's allowed list |
| 5 GHz band incompatible | Check device Wi-Fi specification | Connect to 2.4 GHz band instead |

#### 3.1.2 Mobile Data Not Working / Data Mudah Alih Tidak Berfungsi

| Probable Cause | Diagnostic Check | Resolution |
|----------------|-----------------|------------|
| Mobile data disabled | Settings → Mobile Network → Mobile Data | Enable mobile data; check data limit has not been reached |
| Incorrect APN settings | Settings → Mobile Network → APN | Delete and re-enter APN settings from carrier documentation |
| SIM card not seated properly | Power off; remove and reseat SIM | Reinsert SIM; verify SIM recognised in Settings |
| No network coverage | Check signal bars; test in another location | Move to area with coverage; contact carrier if persistent |
| Data roaming not enabled (overseas) | Settings → Mobile Network → Roaming | Enable roaming if authorised; check roaming charges |

#### 3.1.3 Bluetooth Cannot Pair / Bluetooth Tidak Dapat Dipasangkan

| Probable Cause | Diagnostic Check | Resolution |
|----------------|-----------------|------------|
| Bluetooth not discoverable | Check target device is in pairing mode | Set target device to discoverable; initiate pairing within time window |
| Devices out of range | Check distance between devices | Move devices within 10 metres of each other |
| Previous pairing cached | Old pairing entry listed | Forget the old pairing on both devices and pair again |
| Interference | Check for other 2.4 GHz devices nearby | Move away from microwave ovens, other wireless devices |

---

### 3.2 Application Problems / Masalah Aplikasi

| Problem | Probable Cause | Resolution |
|---------|----------------|------------|
| App crashes on launch | Corrupt app data or cache | Clear app cache: Settings → Apps → [App name] → Storage → Clear Cache; if unresolved, uninstall and reinstall |
| App will not install | Insufficient storage | Check storage: Settings → Storage; delete unused apps or media to free space |
| App will not install | OS version too old | Check minimum OS requirement; update OS if supported or request a compatible app version |
| App not updating | Play Store / App Store account issue | Sign out and sign back in to the store account; retry update |
| App permissions denied | Required permission not granted | Settings → Apps → [App name] → Permissions; enable required permissions (camera, microphone, location) |
| App shows "Not compatible with device" | Device does not meet hardware or OS requirement | Confirm device specifications; seek alternative compatible application |

---

### 3.3 Account and Email Problems / Masalah Akaun dan E-mel

| Problem | Probable Cause | Resolution |
|---------|----------------|------------|
| Cannot log in to Google / Apple ID | Wrong password or account locked | Reset password via account recovery; verify correct email address |
| Email not syncing | Incorrect server settings | Verify IMAP/Exchange server address, port, and SSL setting against IT documentation |
| Email account shows "Authentication failed" | Password changed on server | Remove and re-add account with updated credentials |
| Contacts / calendar not syncing | Sync disabled for account | Settings → Accounts → [Account] → enable Sync Contacts / Sync Calendar |
| MDM enrolment fails | Wrong corporate credentials | Confirm username and password with IT department; check network connectivity during enrolment |

---

### 3.4 Performance Problems / Masalah Prestasi

| Problem | Probable Cause | Resolution |
|---------|----------------|------------|
| Device slow / lagging | Insufficient free RAM | Close background apps; restart device |
| Device slow / lagging | Storage nearly full | Delete unused apps, photos, or cache data; move files to cloud storage |
| Battery drains quickly | App running in background | Check battery usage: Settings → Battery; identify and restrict high-drain apps |
| Device overheating | Processor overloaded or faulty battery | Close all apps; allow device to cool; check for runaway processes in battery settings |
| Screen unresponsive | Software freeze | Press and hold Power button for 10–15 seconds to force restart |
| Device freezes repeatedly | OS corruption or incompatible app | Boot into safe mode (Android) to check if a third-party app is causing the issue; uninstall recent apps |

---

### 3.5 Security and Authentication Problems / Masalah Keselamatan dan Pengesahan

| Problem | Probable Cause | Resolution |
|---------|----------------|------------|
| Forgotten screen lock PIN / password | User forgot credentials | Perform factory reset (data loss — confirm with user and obtain authorisation); restore from backup if available |
| VPN will not connect | Incorrect credentials or certificate expired | Verify VPN credentials; check certificate validity date; reinstall VPN certificate if expired |
| MDM policy blocks a function | Organisational policy enforcement | Explain to user that the restriction is policy-enforced; escalate if policy change is needed |
| Device flagged as non-compliant in MDM | Security policy not met (e.g., OS out of date, screen lock not set) | Update OS; set screen lock; re-enrol if required; verify compliance status in MDM console |

---

## 4.0 Soft Reset and Hard Reset Procedures / Prosedur Mulakan Semula Lembut dan Keras

### 4.1 Soft Reset (Restart) / Mulakan Semula Lembut

A soft reset restarts the device OS without erasing any data. It resolves many minor software faults:

- **Android:** Press and hold the Power button → tap **Restart (Mulakan Semula)**
- **iOS:** Press and hold Side button + Volume Down button → slide to power off → press Side button to restart

Use a soft reset when the device is frozen, an app has crashed, or Wi-Fi/Bluetooth is behaving erratically.

### 4.2 Hard Reset / Force Restart / Mulakan Semula Paksa

A force restart is used when the device is completely unresponsive:

- **Android (most models):** Press and hold Power + Volume Down for 10–15 seconds
- **iPhone 8 and later:** Press Volume Up → press Volume Down → press and hold Side button until Apple logo appears
- **iPhone 7:** Press and hold Volume Down + Sleep/Wake button for 10 seconds

### 4.3 Factory Reset / Tetapan Semula Kilang

A factory reset (hard reset) erases all data and returns the device to its original out-of-box state. It is a last-resort troubleshooting step and must only be performed with user authorisation and after a data backup:

| Platform | Path |
|----------|------|
| Android | Settings → General Management → Reset → Factory Data Reset |
| iOS | Settings → General → Transfer or Reset iPhone → Erase All Content and Settings |

> **Warning:** A factory reset permanently deletes all user data, accounts, and installed applications. Always confirm that a recent backup exists and obtain written authorisation before proceeding.

---

## 5.0 Network Troubleshooting Tools / Alat Penyelesaian Masalah Rangkaian

| Tool / Alat | Platform | Purpose |
|-------------|----------|---------|
| Ping (via network utility app) | Android / iOS | Test connectivity to gateway or DNS server |
| Wi-Fi Analyser | Android | Identify available SSIDs, signal strength, channel congestion |
| Network Info app | Android | Display current IP address, gateway, DNS, signal strength |
| Settings → Wi-Fi → network details | Android / iOS | View assigned IP address, subnet mask, and router address |
| nslookup / DNS test | Via browser or app | Verify DNS resolution is working correctly |
| MDM console (web) | PC / admin device | View device enrolment status, policy compliance, and remote diagnostics |

---

## 6.0 Troubleshooting Documentation / Dokumentasi Penyelesaian Masalah

After resolving a fault, the technician must document the following in the job order or service record:

| Field | Content |
|-------|---------|
| Fault description (Penerangan kerosakan) | Exact fault reported by user or observed by technician |
| Probable cause (Punca yang mungkin) | Root cause identified during diagnosis |
| Actions taken (Tindakan diambil) | Step-by-step actions performed to resolve the fault |
| Test results (Keputusan ujian) | Results of post-resolution testing — pass or fail for each test |
| Outstanding issues (Isu yang belum selesai) | Any problems not resolved; escalation required |
| Technician name and date (Nama juruteknik dan tarikh) | For accountability and audit trail |

---

## 7.0 Common Troubleshooting Errors

| Error / Kesilapan | Consequence / Akibat | Prevention / Pencegahan |
|-------------------|----------------------|-------------------------|
| Performing factory reset without backup | All user data permanently lost | Always confirm backup exists and obtain authorisation first |
| Clearing app data instead of cache | App settings and login credentials deleted | Clear cache first; only clear data if cache clear does not resolve the problem |
| Not testing after resolution | Problem recurs; user reports same fault again | Always run the full test checklist after every fix |
| Not documenting actions taken | No audit trail; same fault difficult to diagnose next time | Record every action in the service record immediately |
| Changing multiple settings simultaneously | Cannot identify which change fixed the problem | Change one setting at a time and test after each change |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCU 7: Mobile Device Configuration
- Jennifer's Teaching Plan Reference: IT-020-3:2013-C07/P(3/6)PM — Pengujian Konfigurasi Peranti Mudah Alih
- Google Android Help — support.google.com/android
- Apple Support — support.apple.com
- CompTIA A+ Certification Study Guide — Mobile Device Troubleshooting Chapter
- Microsoft Intune Troubleshooting Documentation — learn.microsoft.com/intune/troubleshoot