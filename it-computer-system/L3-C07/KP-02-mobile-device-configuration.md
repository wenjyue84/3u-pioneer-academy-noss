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
| NO. KOD | IT-020-3:2013-C07/KP(2/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-02-mobile-device-configuration

**TUJUAN:** Kertas rujukan untuk KP-02-mobile-device-configuration.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the device settings that must be configured during mobile device setup
2. Describe network configuration procedures including IP address, authentication, and Wi-Fi settings
3. Explain the application installation procedure and post-installation configuration steps
4. Describe the procedure for testing a configured mobile device to verify correct operation

---

## 1.0 Introduction to Mobile Device Configuration

Mobile device configuration (Konfigurasi Peranti Mudah Alih) is the process of setting up a mobile device — smartphone or tablet — so that it meets organisational or user requirements. Configuration covers three main areas:

1. **Device settings (Tetapan Peranti)** — language, date/time, display, accounts, and security
2. **Network configuration (Konfigurasi Rangkaian)** — Wi-Fi, mobile data APN, VPN
3. **Application installation and configuration (Pemasangan dan Konfigurasi Aplikasi)** — installing required apps and configuring them for the user

Configuration must follow the approved job order. Any deviation must be documented as a change request before implementation.

---

## 2.0 Device Settings Configuration / Tetapan Konfigurasi Peranti

### 2.1 Initial Setup Menu / Menu Tetapan Awal

When configuring a new or factory-reset device, the technician steps through the initial setup wizard and then configures additional settings via the **Settings (Tetapan)** menu:

| Setting Category | Items to Configure |
|------------------|--------------------|
| Language and input (Bahasa dan Input) | Display language, keyboard language, autocorrect settings |
| Date and time (Tarikh dan Masa) | Time zone, automatic date/time sync (recommended), 24-hour or 12-hour format |
| Display (Paparan) | Screen brightness, screen timeout duration, font size |
| Sound and notification (Bunyi dan Pemberitahuan) | Ringtone, notification sounds, Do Not Disturb schedule |
| Accounts (Akaun) | Google Account (Android) or Apple ID (iOS) — required for app downloads and cloud sync |
| Security (Keselamatan) | Screen lock type (PIN, pattern, password, biometric), encryption status |
| Accessibility (Kebolehaksesan) | Screen reader, display size, magnification — configure if specified in job order |

### 2.2 Account Setup / Tetapan Akaun

Account configuration is required before applications that depend on cloud services (email, calendar, contacts) can be used:

| Account Type | Platform | Purpose |
|--------------|----------|---------|
| Google Account | Android | Play Store access, Gmail, Google Drive, calendar, contacts sync |
| Apple ID | iOS | App Store access, iCloud backup, iMessage, FaceTime |
| Microsoft 365 / Exchange | Android and iOS | Corporate email, calendar, and contacts via Exchange ActiveSync or Outlook app |
| Corporate MDM account | Android and iOS | Enrolment in Mobile Device Management for policy enforcement |

> **Note:** Corporate accounts must use the email address and credentials provided in the job order. Personal accounts must not be used on corporate-managed devices unless permitted by policy.

---

## 3.0 Network Configuration / Konfigurasi Rangkaian

### 3.1 Wi-Fi Configuration / Konfigurasi Wi-Fi

Steps to configure Wi-Fi on a mobile device:

1. Open **Settings → Wi-Fi (Tetapan → Wi-Fi)**
2. Toggle Wi-Fi to **ON**
3. Select the correct SSID (network name) from the list
4. Enter the Wi-Fi password (or EAP credentials for enterprise Wi-Fi)
5. Verify connection — the device should display the Wi-Fi icon in the status bar
6. Test connectivity by opening a browser or pinging a known address

| Wi-Fi Security Type | Description |
|---------------------|-------------|
| WPA2-Personal | Home or small-office Wi-Fi; requires a shared password |
| WPA3-Personal | Newer standard; stronger encryption; backward-compatible devices only |
| WPA2/WPA3-Enterprise (EAP) | Corporate Wi-Fi; requires username, password, and certificate — common in MDM-managed environments |

### 3.2 IP Address Configuration / Konfigurasi Alamat IP

Most mobile devices use DHCP by default. A static IP address may be required for devices in specialised roles (e.g., POS terminals, kiosk tablets):

| Parameter | DHCP (Auto) | Static (Manual) |
|-----------|-------------|-----------------|
| IP Address | Assigned automatically by router | Specified in job order (e.g., 192.168.1.50) |
| Subnet Mask | Assigned automatically | Specified in job order (e.g., 255.255.255.0) |
| Gateway | Assigned automatically | Specified in job order (e.g., 192.168.1.1) |
| DNS Server | Assigned automatically | Specified in job order (e.g., 8.8.8.8) |

**To set a static IP on Android:**
Settings → Wi-Fi → Long press network → Modify network → Advanced options → IP settings → Static

**To set a static IP on iOS:**
Settings → Wi-Fi → Tap (i) next to network → Configure IP → Manual

### 3.3 Mobile Data APN Configuration / Konfigurasi APN Data Mudah Alih

APN (Access Point Name) settings are required when the device uses a SIM card for mobile data. Most carriers push APN settings automatically; manual entry is required if automatic settings are unavailable:

| APN Parameter | Description |
|---------------|-------------|
| APN name | Provided by mobile carrier (e.g., "celcom3g", "maxis", "umobile") |
| Username / Password | Required by some carrier APNs |
| Authentication type | PAP, CHAP, or None — as specified by carrier |
| MCC / MNC | Mobile Country Code / Mobile Network Code — identify the carrier |

### 3.4 Authentication / Pengesahan

Network authentication ensures only authorised devices and users can access network resources:

| Authentication Method | Description |
|----------------------|-------------|
| Password / PIN | Basic credential for Wi-Fi or email login |
| Digital certificate (Sijil Digital) | Used in enterprise Wi-Fi (EAP-TLS); certificate must be installed before Wi-Fi profile is applied |
| MDM-enforced policy | Authentication rules pushed by MDM server — screen lock requirements, password complexity |
| Two-factor authentication (2FA) | Adds a second verification step (OTP via SMS or authenticator app) for enterprise accounts |

---

## 4.0 Application Installation and Configuration / Pemasangan dan Konfigurasi Aplikasi

### 4.1 Application Installation Procedure / Prosedur Pemasangan Aplikasi

**Method 1 — From App Store (Standard):**

1. Open **Google Play Store** (Android) or **App Store** (iOS)
2. Search for the required application by name or use the direct link from the job order
3. Verify the application publisher matches the expected organisation (e.g., "Microsoft Corporation" for Outlook)
4. Tap **Install** and wait for download and installation to complete
5. Verify the app icon appears on the home screen or app drawer
6. Open the app and proceed to configuration

**Method 2 — From MDM Server (Enterprise):**

1. Enrol the device in MDM (see Section 4.2)
2. Open the **Company Portal** or MDM client app
3. Navigate to the app catalogue
4. Select and install required applications as pushed by the MDM administrator
5. Verify installation status in the MDM console

**Method 3 — Sideloading / APK (Android only — restricted):**

Only permitted if explicitly stated in the job order and approved by the IT security policy. Requires enabling **Install unknown apps** under device security settings. This method is not recommended for production devices.

### 4.2 MDM Enrolment Procedure / Prosedur Pendaftaran MDM

Mobile Device Management (MDM) allows the organisation to centrally manage device policies, enforce security settings, and deploy applications:

| Step | Android (Android Enterprise) | iOS (Apple DEP / ABM) |
|------|------------------------------|----------------------|
| 1 | Download and install **Company Portal** from Play Store | Device is pre-enrolled via Apple Business Manager (ABM) or Configurator |
| 2 | Open Company Portal and sign in with corporate credentials | During initial setup, device auto-enrols when connected to Wi-Fi |
| 3 | Follow on-screen enrolment wizard; accept managed device profile | Accept MDM profile when prompted |
| 4 | Device profile is applied; MDM policies take effect | Device profile is applied; MDM policies take effect |
| 5 | Verify enrolment in MDM console | Verify enrolment in MDM console |

### 4.3 Email and Calendar Configuration / Konfigurasi E-mel dan Kalendar

| Step | Procedure |
|------|-----------|
| 1 | Open **Settings → Accounts → Add Account** (Android) or **Settings → Mail → Accounts → Add Account** (iOS) |
| 2 | Select account type: Exchange, Office 365, Gmail, IMAP, or POP3 |
| 3 | Enter email address and password as specified in the job order |
| 4 | Enter server settings if not auto-detected: incoming server (IMAP/Exchange), outgoing server (SMTP), port numbers, SSL/TLS requirement |
| 5 | Select sync options: mail, contacts, calendar — as per job order scope |
| 6 | Verify that new emails appear in the mail app and calendar events sync correctly |

**Common Exchange / Office 365 settings:**

| Parameter | Value |
|-----------|-------|
| Server (Exchange) | outlook.office365.com |
| Port (IMAP) | 993 (SSL) |
| Port (SMTP) | 587 (TLS) or 465 (SSL) |
| Domain | As specified in job order (e.g., company.com) |

### 4.4 VPN Configuration / Konfigurasi VPN

| Step | Procedure |
|------|-----------|
| 1 | Open **Settings → Network → VPN** (Android) or **Settings → General → VPN** (iOS) |
| 2 | Tap **Add VPN configuration** |
| 3 | Select VPN type: IKEv2, L2TP/IPSec, or SSL (as specified in job order) |
| 4 | Enter VPN server address, account name, and authentication credentials |
| 5 | Install VPN certificate if required (certificate file provided by IT department) |
| 6 | Save and connect; verify VPN icon appears in status bar |
| 7 | Test connectivity — access an internal resource to confirm the VPN tunnel is active |

---

## 5.0 Configuration Testing / Pengujian Konfigurasi

After completing all configuration steps, the technician must test every configured function before signing off the job order.

### 5.1 Authentication Test / Ujian Pengesahan

| Test | Expected Result |
|------|----------------|
| Screen lock activates after timeout | Device locks at the configured timeout duration |
| PIN / password / biometric unlock | Device unlocks correctly with correct credential; rejects incorrect credential |
| Corporate account login | User can log in to email and corporate apps with provided credentials |
| MDM policy enforcement | Device complies with MDM policies (e.g., camera disabled if policy requires) |

### 5.2 Network and Communication Test / Ujian Rangkaian dan Komunikasi

| Test | Expected Result |
|------|----------------|
| Wi-Fi connectivity | Device connects to configured SSID; browser loads a webpage successfully |
| Mobile data connectivity | Device accesses internet via SIM (if configured); correct APN active |
| Email send and receive | Test email sent from and received on the device mail app |
| VPN connection | VPN connects and internal resources are accessible |
| Ping test | Open a terminal / network tool app and ping the gateway or a known internal server |

### 5.3 Application Test / Ujian Aplikasi

| Test | Expected Result |
|------|----------------|
| All required apps installed | Every application listed in the job order is present and opens without error |
| App account login | Each app that requires authentication can log in with configured credentials |
| Data sync | Contacts, calendar, and email sync correctly with the server |
| Push notification | Test notification received in real time |

---

## 6.0 Common Configuration Errors

| Error / Kesilapan | Consequence / Akibat | Prevention / Pencegahan |
|-------------------|----------------------|-------------------------|
| Wrong Wi-Fi password entered | Device cannot connect to Wi-Fi; time lost retrying | Copy password directly from job order; verify by typing carefully |
| Incorrect Exchange server address | Email account fails to set up | Confirm server address with IT department; check autoconfiguration first |
| Application installed from unofficial source | Security risk; app may not receive updates | Always install from Play Store or App Store unless MDM-deployed |
| MDM enrolment skipped | Device not managed; policies not enforced | Follow job order; verify enrolment status in MDM console after setup |
| No configuration test performed | Defects discovered only after device handed to user | Always run the full test checklist before sign-off |
| Date/time not synced | Certificates and authentication may fail due to time mismatch | Enable automatic date/time synchronisation during setup |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCU 7: Mobile Device Configuration
- Jennifer's Teaching Plan Reference: IT-020-3:2013-C07/P(3/6)PM — Konfigurasi Mobile Device
- Google Android Enterprise Help — support.google.com/work/android
- Apple Business Essentials Deployment Reference — support.apple.com/enterprise
- Microsoft Intune Documentation — learn.microsoft.com/intune
- CompTIA A+ Certification Study Guide — Mobile Device Configuration Chapter