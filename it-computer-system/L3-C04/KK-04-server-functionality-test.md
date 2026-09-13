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
| NO. KOD | IT-020-3:2013-C04/KK(4/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-04-server-functionality-test

**TUJUAN:** Kertas rujukan untuk KK-04-server-functionality-test.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objectives

Upon completing this activity, the trainee will be able to:
- Verify that server hardware components are functioning correctly after installation
- Confirm that all installed server roles and services are operational
- Test network connectivity between the server and designated client systems
- Document test results and identify any faults requiring corrective action

---

## Peralatan / Equipment Required

| No. | Item | Kuantiti / Quantity |
|-----|------|---------------------|
| 1 | Installed server (from KK-02 and KK-03) | 1 |
| 2 | Client workstation connected to the same network segment | 1 |
| 3 | KVM console or remote desktop access | 1 |
| 4 | Server functionality test checklist (provided by instructor) | 1 |
| 5 | Network patch cables | As needed |
| 6 | Pen and notepad for recording test results | 1 set |

---

## Langkah Keselamatan / Safety Precautions

- Do not connect the server to the live production network without instructor approval
- Conduct all tests in the designated training VLAN or isolated test network
- Do not modify any server configuration during testing — record failures and seek instructor guidance before making changes
- If the server exhibits abnormal behaviour (excessive heat, unusual noise, repeated crashes), power it off immediately and notify the instructor
- Ensure the UPS or PDU supplying the server is stable before running extended tests

---

## Prosedur / Procedure

| Langkah | Arahan / Instruction |
|---------|----------------------|
| 1 | **Hardware health check.** Log in to the server. Open the server management interface (e.g., Windows Server Manager, iDRAC System Summary, or `dmidecode` on Linux). Verify that all CPUs, RAM modules, and storage drives are detected and show a healthy status. Note any hardware warnings or alerts. |
| 2 | **Check system event log.** Open the Windows Event Viewer (System and Application logs) or the Linux `journalctl` / `dmesg` output. Review entries since the initial boot. Record any critical or error-level events. Investigate and resolve critical errors before proceeding. |
| 3 | **Verify storage health.** Open Disk Management (Windows) or `lsblk` / `fdisk -l` (Linux). Confirm all drives are online and partitions are formatted correctly. Check RAID status if a RAID controller is configured — all arrays must show as Optimal or Healthy. |
| 4 | **Test server-to-gateway connectivity.** Open a command prompt or terminal on the server. Run `ping <default gateway IP> -n 10` (Windows) or `ping -c 10 <default gateway IP>` (Linux). All 10 packets must succeed with no loss. Record the average latency. |
| 5 | **Test DNS resolution.** From the server command prompt, run `nslookup <internal domain name>` (Windows) or `dig <internal domain name>` (Linux). Verify the DNS server responds with the correct IP address. |
| 6 | **Test server-to-client connectivity.** From the client workstation, ping the server's IP address. Confirm bidirectional connectivity. Record the result. |
| 7 | **Verify installed server roles.** For each role installed in KK-03, perform the appropriate functional test: |
| | (a) **Active Directory / LDAP:** Run `dcdiag` (Windows) or query the LDAP port using `ldapsearch`. Confirm no failures. |
| | (b) **DNS Server:** From the client, run `nslookup <server hostname>`. Confirm the correct IP is returned. |
| | (c) **DHCP Server:** Connect a client workstation configured for DHCP. Confirm the client receives an IP address from the correct scope. Record the assigned IP, lease duration, and gateway. |
| | (d) **File and Storage Services:** Map a network drive from the client to a shared folder on the server. Confirm read and write access. Create a test file and verify it appears on the server. |
| | (e) **Web Server (IIS / Apache):** Open a browser on the client. Enter the server's IP address or hostname. Confirm the default web page loads successfully. |
| 8 | **Test remote management access.** From the client workstation, connect to the server via Remote Desktop Protocol (RDP) on port 3389 (Windows) or SSH on port 22 (Linux). Log in successfully. Confirm remote management is functional. |
| 9 | **Stress test — short duration.** Run a brief CPU and memory stress test (maximum 5 minutes) using a utility provided by the instructor (e.g., `stress` on Linux or Windows Performance Monitor baseline capture). Monitor CPU temperature and memory error count during the test. Record peak CPU temperature and confirm no memory errors occur. |
| 10 | **Record all test results.** Complete the server functionality test checklist. Mark each test as PASS or FAIL. For each FAIL, describe the observed symptom, the probable cause, and the corrective action taken or recommended. Sign the checklist and submit to the instructor. |

---

## Hasil Dijangka / Expected Outcome

A completed functionality test record showing:
- All hardware components healthy with no critical event log errors
- Storage drives online with RAID array (if applicable) in Optimal status
- Network connectivity confirmed — server to gateway, server to client, bidirectional
- DNS resolution functioning correctly
- All installed server roles verified as operational
- Remote management access confirmed
- No memory errors or overtemperature conditions during short stress test
- Test checklist signed and submitted to instructor

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Hardware health check completed — all components show healthy | [ ] Yes  [ ] No |
| 2 | System event log reviewed — no unresolved critical errors | [ ] Yes  [ ] No |
| 3 | All storage drives online and RAID status Optimal (if applicable) | [ ] Yes  [ ] No |
| 4 | Server-to-gateway ping: 0% packet loss | [ ] Yes  [ ] No |
| 5 | DNS resolution test passed | [ ] Yes  [ ] No |
| 6 | Server-to-client bidirectional connectivity confirmed | [ ] Yes  [ ] No |
| 7 | All installed server roles verified as operational | [ ] Yes  [ ] No |
| 8 | Remote management (RDP/SSH) access confirmed | [ ] Yes  [ ] No |
| 9 | Short stress test completed — no memory errors, temperature within limit | [ ] Yes  [ ] No |
| 10 | Test checklist fully completed with PASS/FAIL results and submitted | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Nama / Name | Tandatangan / Signature | Tarikh / Date |
|---|-------------|-------------------------|---------------|
| Pelatih / Trainee | | | |
| Pengajar / Instructor | | | |