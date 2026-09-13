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

## KERTAS TUGASAN

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-4:2013 PENTADBIRAN SISTEM KOMPUTER |
| TAHAP | 4 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C01 SERVER CONFIGURATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE SERVER CONFIGURATION REQUIREMENTS<br>2. PLAN SERVER ROLES AND SERVICES<br>3. CONFIGURE SERVER HARDWARE AND STORAGE<br>4. CONFIGURE SERVER OS AND ROLES<br>5. IMPLEMENT SERVER SECURITY SETTINGS<br>6. DOCUMENT SERVER CONFIGURATION |
| NO. KOD | IT-020-4:2013-C01/KT(5/6) |
| Muka Surat | 1/1 |
| WARNA KERTAS | MERAH JAMBU (Pink) |

**TAJUK:** KT-05-server-security-assignment

**TUJUAN:** Kertas rujukan untuk KT-05-server-security-assignment.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Arahan / Instructions

Answer ALL questions. Refer to KP(5/6) for guidance. Write clearly on a separate answer sheet.

**Masa / Duration:** 60 minutes

---

## Tugasan / Questions

### Bahagian A: Soalan Pelbagai Pilihan / Multiple Choice (20 marks — 4 marks each)

**A1.** The principle of least privilege (Prinsip Hak Minimum) means:

- (a) Every user has the same level of access to simplify management
- (b) Every account, service, and process has ONLY the permissions required to perform its specific function
- (c) Administrative accounts have the fewest privileges in the organisation
- (d) Standard users have no access to any server resources

**A2.** Windows Firewall is configured with "Default Inbound = Block". Which of the following correctly describes the effect of this setting?

- (a) All inbound network traffic to the server is dropped unless an explicit Allow rule exists
- (b) All inbound traffic is allowed unless an explicit Block rule exists
- (c) Only traffic on port 80 and 443 is allowed inbound
- (d) Outbound traffic is also blocked

**A3.** A Group Managed Service Account (gMSA) is preferred over a standard service account because:

- (a) gMSA accounts have Domain Admin privileges by default
- (b) gMSA passwords are automatically managed and rotated by Active Directory — no manual password management required
- (c) gMSA accounts can log on interactively to the console
- (d) gMSA accounts do not require a Service Principal Name (SPN)

**A4.** BitLocker Drive Encryption on a server data volume protects against:

- (a) Ransomware encryption attacks over the network
- (b) Unauthorised access to data if a physical disk is removed from the server or the server is stolen
- (c) Brute-force attacks on the Administrator password
- (d) SQL injection attacks on the database

**A5.** Windows Security Event ID 4625 is logged when:

- (a) A user logs on successfully
- (b) A user account is created
- (c) An account fails to log on
- (d) A service starts successfully

---

### Bahagian B: Soalan Jawapan Pendek / Short Answer (30 marks)

**B1.** List the recommended account lockout policy settings (Threshold, Duration, Observation Window) and explain why the lockout duration should not be set to "0" (administrator must unlock manually) for a school environment. (8 marks)

**B2.** Explain what an Advanced Audit Policy is, how it differs from the basic Local Security Policy audit settings, and state FOUR (4) audit subcategories that must be enabled on a domain controller. (10 marks)

**B3.** Describe what "NTLMv2 only" authentication means and explain why LM and NTLM authentication should be refused on a production Windows Server domain. (7 marks)

**B4.** State the patch management phases (from KP-05 Section 7.1) and explain why patches should be tested before production deployment rather than applied directly. (5 marks)

---

### Bahagian C: Soalan Situasi / Situational Question (50 marks)

**C1.** Pioneer Academy's IT Manager has received a security audit report identifying the following issues on SRV-DC01 (their newly deployed domain controller):

- Issue 1: RDP (port 3389) is accessible from any IP address on the internet
- Issue 2: The built-in Administrator account has not been renamed and is in use for daily administrative tasks
- Issue 3: No audit policy is configured — the Security event log is empty
- Issue 4: The data volume (D:) is unencrypted
- Issue 5: The domain password policy allows 6-character passwords with no complexity requirement

**(a)** For each of the FIVE (5) issues, state: (i) the security risk the issue presents, and (ii) the specific remediation action (including PowerShell command or GPO setting path) to resolve it. (30 marks — 6 marks per issue)

**(b)** The IT Manager asks: "We have a firewall at the edge of the network — why do we also need Windows Firewall enabled on each server?" Write a clear technical explanation of the defence-in-depth principle (Pertahanan Berlapis) and how it justifies host-based firewall configuration even when an edge firewall exists. (10 marks)

**(c)** After enabling BitLocker on the D: volume, the server reboots for a scheduled patch cycle. The server does not restart automatically — it is waiting at a BitLocker recovery key prompt. Explain: (i) why this happened, (ii) what BitLocker Network Unlock is and how it prevents this, and (iii) what the on-call administrator should do immediately. (10 marks)

---

## Kriteria Penilaian / Assessment Criteria

| Section | Marks | Criteria |
|---------|-------|---------|
| A (MCQ) | 20 | Correct answer = 4 marks |
| B1 | 8 | Three settings correct (3) + explanation of why not "0" for school (5) |
| B2 | 10 | Advanced Audit definition (2) + difference from basic (3) + four subcategories (1.25 each) |
| B3 | 7 | NTLMv2 definition (3) + why LM/NTLM refused (4) |
| B4 | 5 | Phases listed (2) + justification for testing before production (3) |
| C1(a) | 30 | Per issue: risk (3) + remediation action (3); correct command/path required for full marks |
| C1(b) | 10 | Defence-in-depth concept (4) + host firewall justification (4) + specific server scenario (2) |
| C1(c) | 10 | Why it happened (3) + Network Unlock explanation (4) + immediate action (3) |
| **TOTAL** | **100** | |

---

## Skema Jawapan / Answer Scheme

*To be provided by the instructor after submission.*