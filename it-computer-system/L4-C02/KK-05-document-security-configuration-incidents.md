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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C02 COMPUTER SYSTEM SECURITY CONTROL |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. IDENTIFY SECURITY REQUIREMENTS<br>2. IMPLEMENT ACCESS CONTROL AND AUTHENTICATION<br>3. CONFIGURE FIREWALL AND NETWORK SECURITY<br>4. MANAGE PATCHES AND SECURITY UPDATES<br>5. DOCUMENT SECURITY CONFIGURATION AND INCIDENTS |
| NO. KOD | IT-020-4:2013-C02/KK(5/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-05-document-security-configuration-incidents

**TUJUAN:** Kertas rujukan untuk KK-05-document-security-configuration-incidents.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

Complete a security configuration baseline record for a hardened Windows Server, enable and verify audit logging, and produce a full incident report for a simulated security incident scenario.

---

## Tempoh / Duration

2 hours

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Windows Server 2022 (hardened from KK-02 and KK-03 exercises, or as configured by instructor) | 1 |
| 2 | Security configuration baseline template (blank) | 1 |
| 3 | System hardening checklist (blank) | 1 |
| 4 | Incident report template (blank) | 1 |
| 5 | Incident scenario brief (provided by instructor) | 1 |
| 6 | Administrator credentials | Provided by instructor |

---

## Langkah Keselamatan / Safety Precautions

- Treat all incident scenario details as confidential training material
- Do not alter existing audit policy on production systems — work only in the lab environment
- Log off all sessions upon completion
- Submit all completed templates to instructor; do not retain copies outside the training environment

---

## Prosedur / Procedures

**Part A — Security Configuration Baseline Record**

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 1 | Using the security configuration baseline template provided, complete the **System Identification** section: hostname, IP address, OS version (run `winver`), hardware model, and asset tag. |
| 2 | Complete the **OS Configuration** section: list installed KB updates (`Get-HotFix | Select-Object HotFixID, InstalledOn`), list enabled Windows features (`Get-WindowsFeature | Where-Object {$_.InstallState -eq "Installed"}`), and note the local security policy settings applied. |
| 3 | Complete the **User and Group Configuration** section: list all local user accounts (`Get-LocalUser`), their enabled/disabled status, and group memberships (`Get-LocalGroupMember -Group "Administrators"`). |
| 4 | Complete the **Network Configuration** section: IP settings (`ipconfig /all`), active firewall profile, and a list of listening ports (`Get-NetTCPConnection -State Listen | Select-Object LocalAddress, LocalPort, OwningProcess`). |
| 5 | Complete the **Services Configuration** section: list all running services (`Get-Service | Where-Object {$_.Status -eq "Running"} | Select-Object Name, DisplayName, StartType`) and all disabled services. |
| 6 | Complete the **Installed Software** section: list all installed applications (`Get-WmiObject -Class Win32_Product | Select-Object Name, Version`). |
| 7 | Complete the **Audit and Logging** section: run `AuditPol /get /category:*` and record which audit categories are enabled for Success and/or Failure. Note the log storage path and current log size. |
| 8 | Sign and date the baseline record. The instructor will countersign as verifier. |

**Part B — Enable and Verify Audit Logging**

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 9 | Enable the following audit policies using `AuditPol`: Logon (Success + Failure), Account Logon (Success + Failure), Object Access (Failure), Account Management (Success + Failure), Policy Change (Success). Run `AuditPol /get /category:*` to confirm each is set correctly. |
| 10 | Generate test events: (a) Attempt to log in with a wrong password 3 times (Event ID 4625). (b) Create a new local user account (Event ID 4720). (c) Delete the test user (Event ID 4726). Open Event Viewer → Windows Logs → Security and locate each of the three event IDs. Record the event details (time, event ID, subject account). |

**Part C — Incident Report (Simulated Scenario)**

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 11 | Read the incident scenario brief provided by the instructor. The scenario describes a security incident that has occurred on the training network (e.g. a user account showing repeated failed logon attempts from an unusual IP address, followed by a successful logon outside business hours and access to a sensitive folder). |
| 12 | Using the incident report template, complete ALL sections: Incident ID, date/time reported, reported by, incident type, severity (P1–P4), systems affected, description of incident, timeline, root cause analysis, containment actions, eradication actions, recovery actions, data affected, lessons learned, and recommended actions. |
| 13 | Cross-reference the simulated audit log excerpts provided in the scenario brief. Cite specific Event IDs and timestamps in the incident timeline to demonstrate evidence-based reporting. |
| 14 | Present the completed incident report to the instructor (5-minute verbal summary). Justify the severity classification and the recommended actions. |

---

## Hasil Jangkaan / Expected Outcome

- Security configuration baseline record completed for all eight sections
- Audit policy correctly enabled for five categories; verified via AuditPol output
- Three test events generated and located in Event Viewer with event IDs recorded
- Incident report completed for all sections with evidence-based timeline
- Verbal summary presented with justified severity and recommendations

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Security configuration baseline record — all 8 sections completed | [ ] Yes  [ ] No |
| 2 | Baseline signed and countersigned | [ ] Yes  [ ] No |
| 3 | Audit policies enabled for 5 required categories | [ ] Yes  [ ] No |
| 4 | Three test events generated and located in Event Viewer | [ ] Yes  [ ] No |
| 5 | Incident report — all sections completed | [ ] Yes  [ ] No |
| 6 | Incident timeline cites specific Event IDs and timestamps | [ ] Yes  [ ] No |
| 7 | Severity classification justified | [ ] Yes  [ ] No |
| 8 | Verbal summary delivered clearly | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |