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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C01 COMPUTER SYSTEM SET-UP |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE JOB ORDER/CHANGE REQUEST<br>2. PREPARE COMPUTER SET-UP TOOLS, COMPUTER HARDWARE PARTS AND COMPUTER SOFTWARE<br>3. SET-UP COMPUTER HARDWARE<br>4. CARRY OUT COMPUTER SOFTWARE INSTALLATION<br>5. SET-UP COMPUTER PERIPHERALS<br>6. CARRY OUT UNIT FUNCTIONALITY TEST<br>7. PREPARE COMPUTER SET-UP REPORT |
| NO. KOD | IT-020-3:2013-C01/KK(6/7) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-06-system-functionality-stability-testing

**TUJUAN:** Kertas rujukan untuk KK-06-system-functionality-stability-testing.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

Perform comprehensive testing to verify the system is stable and ready for user handover.

---

## Tempoh / Duration

45 minutes

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Fully configured system from KK(5/7) | 1 |
| 2 | System utilities (built into OS) | -- |
| 3 | Multimeter (optional, for power verification) | 1 (shared) |
| 4 | Functionality test checklist form | 1 |
| 5 | Pen for recording results | 1 |

---

## Langkah Keselamatan / Safety Precautions

- Do not open the case or disconnect components while the system is powered on
- If the system becomes unstable during stress testing, power off immediately and investigate before restarting
- Record all test results honestly and accurately

---

## Prosedur / Procedures

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 1 | **Boot sequence check.** Power on the system and observe the boot sequence. Note any error messages, beep codes, or warnings. The system should boot to the OS login screen without issues. |
| 2 | **User account verification.** Log in to the user account. Verify the account is created correctly and the desktop loads. |
| 3 | **Device Manager check.** Open Device Manager. Verify all hardware devices are listed without unknown devices (no yellow triangles) or error codes. Record the result. |
| 4 | **Disk health check.** Open Command Prompt as Administrator. Run `chkdsk C:` (or equivalent) to check disk health. Record the result (no errors expected). |
| 5 | **CPU and RAM monitoring.** Open Task Manager (Ctrl+Shift+Esc). Monitor CPU usage, RAM usage, and disk activity during idle. CPU should be below 10% at idle; RAM usage should be reasonable for the OS. |
| 6 | **Network connectivity test.** Open Command Prompt. Run `ping 192.168.1.1` (or the gateway address) to verify local network. Run `ping 8.8.8.8` to verify internet. Open a browser and load a website to verify DNS resolution. Record results. |
| 7 | **File read/write test.** Copy a test file (e.g. 100 MB) to the storage drive and back. Verify the operation completes without errors and at reasonable speed. |
| 8 | **Application launch test.** Open each application specified in the job request (e.g. Office, browser, antivirus). Verify each launches and responds normally. Close after verification. |
| 9 | **Stress test.** Run a CPU-intensive operation (e.g. full antivirus scan or file compression) for 5 minutes. Monitor CPU temperature using Task Manager Performance tab or a monitoring utility. CPU temperature should remain below 80 degrees Celsius. |
| 10 | **Temperature check.** After the stress test, verify CPU and GPU temperatures are within safe operating range. Record the maximum temperature observed. |
| 11 | **Document results.** Record all test results on the functionality test checklist form. Note any issues found and whether they were resolved. |

---

## Hasil Jangkaan / Expected Outcome

- System boots without errors
- User account is functional
- All hardware recognised with no unknown devices
- Disk check completed with no errors
- CPU and RAM operating within expected parameters
- Network connectivity confirmed (local and internet)
- Applications launch and respond normally
- System remains stable under load
- CPU and GPU temperatures within safe range

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | System boots without errors | [ ] Yes  [ ] No |
| 2 | User account is functional | [ ] Yes  [ ] No |
| 3 | All hardware recognised with no unknown devices | [ ] Yes  [ ] No |
| 4 | Disk check completed with no errors | [ ] Yes  [ ] No |
| 5 | CPU and RAM operating within expected parameters | [ ] Yes  [ ] No |
| 6 | Network connectivity confirmed | [ ] Yes  [ ] No |
| 7 | Applications launch and respond normally | [ ] Yes  [ ] No |
| 8 | System remains stable under load | [ ] Yes  [ ] No |
| 9 | CPU and GPU temperatures within safe range | [ ] Yes  [ ] No |
| 10 | All test results documented on checklist | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |