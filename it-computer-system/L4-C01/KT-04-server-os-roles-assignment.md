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
| NO. KOD | IT-020-4:2013-C01/KT(4/6) |
| Muka Surat | 1/1 |
| WARNA KERTAS | MERAH JAMBU (Pink) |

**TAJUK:** KT-04-server-os-roles-assignment

**TUJUAN:** Kertas rujukan untuk KT-04-server-os-roles-assignment.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Arahan / Instructions

Answer ALL questions. Refer to KP(4/6) for guidance. Write clearly on a separate answer sheet.

**Masa / Duration:** 60 minutes

---

## Tugasan / Questions

### Bahagian A: Soalan Pelbagai Pilihan / Multiple Choice (20 marks — 4 marks each)

**A1.** The recommended sequence for post-installation configuration of a Windows Server is:

- (a) Join domain → Install roles → Configure IP → Patch
- (b) Configure IP → Rename computer → Apply patches → Install roles → Join domain (if applicable)
- (c) Install roles → Configure IP → Patch → Rename
- (d) Join domain → Patch → Configure IP → Install roles

**A2.** The PowerShell command to install the Active Directory Domain Services role is:

- (a) `Add-WindowsRole -Name "ADDS"`
- (b) `Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools`
- (c) `Enable-WindowsFeature -Name ActiveDirectory`
- (d) `Set-ADForest -Name "pioneer.edu.my"`

**A3.** `dcdiag /v` is used to:

- (a) Configure DNS forwarders
- (b) Run a comprehensive diagnostic test on the domain controller and display detailed results
- (c) Display DHCP lease statistics
- (d) Promote a member server to domain controller

**A4.** A DHCP server must be "authorised" in Active Directory because:

- (a) It requires a licence from Microsoft before it can issue leases
- (b) AD prevents unauthorised (rogue) DHCP servers from issuing leases to domain-joined clients
- (c) Authorisation configures the DHCP scope automatically
- (d) Without authorisation, the DHCP server cannot communicate with DNS

**A5.** The best practice for NTFS and Share permissions on a Windows file server is:

- (a) Set NTFS to Full Control for Everyone; use Share permissions for all access control
- (b) Set Share permissions to Everyone = Full Control; use NTFS permissions for granular access control
- (c) Set both NTFS and Share to the same permissions for every user
- (d) Disable Share permissions entirely; use only NTFS

---

### Bahagian B: Soalan Jawapan Pendek / Short Answer (30 marks)

**B1.** Explain the purpose of the DSRM (Directory Services Restore Mode) password set during domain controller promotion and when it is used. (6 marks)

**B2.** A new administrator asks why a reverse DNS lookup zone must be created after AD DS promotion. Provide a clear explanation, including TWO (2) specific services or situations where reverse DNS lookup is required. (8 marks)

**B3.** Write the PowerShell commands to: (a) create a DHCP scope for the 192.168.10.0/24 network with range .100 to .200; (b) set scope options for default gateway 192.168.10.1, DNS server 192.168.10.10, and DNS domain name "academy.edu.my"; (c) activate the scope. (9 marks — 3 marks per command group)

**B4.** Describe the tiered administration model (Tier 0, Tier 1, Tier 2) and explain why a Domain Administrator account should never be used for daily administrative tasks. (7 marks)

---

### Bahagian C: Soalan Situasi / Situational Question (50 marks)

**C1.** You have completed the hardware configuration of SRV-DC01 (from KK-03). You are now ready to install Windows Server 2022 and configure it as the first domain controller for pioneer.edu.my. The approved IP assignment is: Production IP 10.0.1.10/24, Gateway 10.0.1.1, DNS (self) 10.0.1.10; Management (iDRAC) 10.0.10.5/24.

**(a)** Describe the complete Windows Server 2022 installation procedure from booting the installation media to the point immediately after the Administrator password is set. Include: edition selection, installation type, disk selection consideration, and why you should NOT join a domain at this stage. (12 marks)

**(b)** List, in the correct order, ALL post-installation steps you would perform before installing any roles. For each step, state the purpose and the PowerShell command or GUI action used. (Minimum 7 steps.) (21 marks)

**(c)** After promoting SRV-DC01 to domain controller, you run `dcdiag /v` and see the following failure: `TEST: Advertising (Advertising) — FAILED: SRV-DC01 is not advertising as a time server.` Explain: (i) what this error means, (ii) why time synchronisation is critical for Active Directory, and (iii) the PowerShell commands to resolve this. (12 marks)

**(d)** Explain the purpose of DFS Namespace (DFS-N) in a file server environment and describe ONE specific scenario at Pioneer Academy where DFS-N would improve the user experience. (5 marks)

---

## Kriteria Penilaian / Assessment Criteria

| Section | Marks | Criteria |
|---------|-------|---------|
| A (MCQ) | 20 | Correct answer = 4 marks |
| B1 | 6 | DSRM purpose (3) + when used (3) |
| B2 | 8 | Explanation (3) + two specific services (2.5 each) |
| B3 | 9 | Correct commands for (a) 3 + (b) 3 + (c) 3; syntax must be valid |
| B4 | 7 | Tier 0 (2) + Tier 1 (2) + Tier 2 (1) + why not Domain Admin for daily tasks (2) |
| C1(a) | 12 | Edition selection (2) + install type (2) + disk selection (3) + domain join reason (5) |
| C1(b) | 21 | 3 marks per step: purpose (1) + command/action (2); minimum 7 steps |
| C1(c) | 12 | Error meaning (3) + time sync criticality for AD (4) + resolution commands (5) |
| C1(d) | 5 | DFS-N purpose (2) + specific Academy scenario (3) |
| **TOTAL** | **100** | |

---

## Skema Jawapan / Answer Scheme

*To be provided by the instructor after submission.*