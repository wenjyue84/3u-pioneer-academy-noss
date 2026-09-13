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

## KERTAS PENILAIAN PENGETAHUAN

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-4:2013 PENTADBIRAN SISTEM KOMPUTER |
| TAHAP | 4 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C01 SERVER CONFIGURATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE SERVER CONFIGURATION REQUIREMENTS<br>2. PLAN SERVER ROLES AND SERVICES<br>3. CONFIGURE SERVER HARDWARE AND STORAGE<br>4. CONFIGURE SERVER OS AND ROLES<br>5. IMPLEMENT SERVER SECURITY SETTINGS<br>6. DOCUMENT SERVER CONFIGURATION |
| NO. KOD | IT-020-4:2013-C01/KA |
| Muka Surat | 1/1 |
| WARNA KERTAS | MERAH JAMBU (Pink) |

**TAJUK:** KA-server-configuration

**TUJUAN:** Kertas rujukan untuk KA-server-configuration.

**ARAHAN:** Jawab semua soalan / laksanakan semua tugas penilaian. Penilaian ini adalah sebahagian daripada Penilaian Akhir CU.

<!-- /JPK_ENVELOPE_v1 -->
## Arahan kepada Pelatih / Instructions to Trainee

1. This paper consists of THREE (3) sections: A, B, and C.
2. Answer ALL questions in ALL sections.
3. Write your answers clearly in the answer booklet provided.
4. This is a CLOSED BOOK examination. No reference materials are permitted.
5. Duration: 1 hour 30 minutes.
6. Pass mark: 60 out of 100.

---

## Arahan kepada Pengajar / Instructions to Instructor

- Distribute the question paper and answer booklet simultaneously.
- Allow exactly 1 hour 30 minutes from the point all trainees confirm they have both items.
- Do NOT assist trainees with technical content during the examination.
- Collect all papers immediately at the end of the allocated time.
- Mark using the answer scheme provided (separate instructor document).

---

## BAHAGIAN A: SOALAN PELBAGAI PILIHAN / SECTION A: MULTIPLE CHOICE (30 marks)

Answer all 15 questions. Each question carries 2 marks. Circle the correct answer.

**1.** The MoSCoW prioritisation method classifies requirements into:

- (a) Mandatory, Standard, Complex, Optional, Withdrawn
- (b) Must Have, Should Have, Could Have, Won't Have
- (c) Management, Security, Configuration, Operations, Work
- (d) Mission-critical, Standard, Cost-optional, Waived

**2.** A domain controller must ALWAYS be deployed with at least TWO instances because:

- (a) Two DCs provide double the storage for the domain
- (b) One DC is for read operations; the other is for write operations only
- (c) The loss of a single DC causes complete failure of domain authentication for all users
- (d) Microsoft licensing requires a minimum of two per domain

**3.** Which storage type provides block-level access over a dedicated high-speed network, enabling server clustering and VM live migration?

- (a) NAS (Network-Attached Storage)
- (b) DAS (Direct-Attached Storage)
- (c) SAN (Storage Area Network)
- (d) Cloud Object Storage

**4.** ECC RAM (Error-Correcting Code) is mandatory for production servers because:

- (a) It is faster than non-ECC RAM at the same clock speed
- (b) It detects and corrects single-bit memory errors, preventing silent data corruption
- (c) It is required by Windows Server licensing
- (d) It reduces power consumption compared to standard RAM

**5.** The BIOS/UEFI setting "VT-d / AMD-Vi (IOMMU)" must be enabled for:

- (a) Dual-channel RAM operation
- (b) PCI device passthrough from hypervisor host to virtual machines
- (c) Secure Boot verification of signed bootloaders
- (d) NVMe drive support on SATA controllers

**6.** For a database server with high random I/O requirements, the recommended RAID level is:

- (a) RAID 0 — maximum throughput, no redundancy
- (b) RAID 5 — good capacity, acceptable write performance
- (c) RAID 6 — two-disk fault tolerance for large arrays
- (d) RAID 10 — mirrored pairs with striping; highest IOPS with fault tolerance

**7.** A battery-backed write cache (BBWC) on a RAID controller warns of a "degraded" status. The immediate impact is:

- (a) The RAID array is degraded and missing a disk
- (b) The RAID controller falls back to write-through mode — writes are acknowledged only after the data is physically written to disk, significantly reducing write performance
- (c) The RAID array switches from RAID 10 to RAID 5 automatically
- (d) No impact — the BBWC is only used during power failures

**8.** The PowerShell command to promote a Windows Server to a domain controller for a NEW forest is:

- (a) `Install-ADDSDomainController`
- (b) `New-ADForest`
- (c) `Install-ADDSForest`
- (d) `Promote-ADDomain`

**9.** The command `dcdiag /v` is used to:

- (a) Display DHCP lease statistics
- (b) Run a comprehensive diagnostic test on the domain controller and report detailed results
- (c) Verify DNS forwarder configuration
- (d) List all FSMO role holders in the domain

**10.** The principle of least privilege (Prinsip Hak Minimum) requires that:

- (a) All administrative accounts share the same password for simplicity
- (b) Every account, service, and process has only the minimum permissions required to perform its specific function
- (c) Only the IT Manager has administrative access to all servers
- (d) Standard user accounts have no access to shared network folders

**11.** Windows Security Event ID 4625 is generated when:

- (a) A user account is created or modified
- (b) A user logs on successfully
- (c) An account fails to log on
- (d) A service account password expires

**12.** BitLocker Drive Encryption primarily protects against:

- (a) Ransomware attacks that encrypt files over the network
- (b) Brute-force attacks on the domain administrator password
- (c) Unauthorised data access when a physical disk or server is removed from the secured premises
- (d) SQL injection attacks on database server volumes

**13.** A Group Managed Service Account (gMSA) is preferred for running Windows services because:

- (a) gMSA accounts have higher privileges than standard service accounts
- (b) gMSA passwords are automatically managed and rotated by Active Directory — no manual intervention required
- (c) gMSA accounts can log on interactively to the server console
- (d) gMSA accounts bypass Windows Firewall rules

**14.** The As-Built Document differs from the Server Configuration Plan in that the As-Built:

- (a) Is written before hardware is procured
- (b) Is only used by the finance department for asset tracking
- (c) Reflects the actual final deployed configuration including documented deviations from the plan
- (d) Contains only the network topology diagram

**15.** A "change log" for a server is described as "append-only" because:

- (a) Log entries are sorted alphabetically and new ones inserted at the correct position
- (b) New entries are added to the end and existing entries must never be modified or deleted — historical integrity is maintained
- (c) The file is read-only and can only be modified by the domain administrator
- (d) Changes are automatically logged by the OS without human action required

---

## BAHAGIAN B: SOALAN JAWAPAN PENDEK / SECTION B: SHORT ANSWER (30 marks)

Answer all 6 questions.

**16.** List and briefly describe THREE (3) categories of server requirements (Business, Technical, Compliance). Give ONE concrete example of each from a school server deployment context. (9 marks)

**17.** An organisation has 4 × 1.8 TB SAS SSD drives available for a file server. Calculate the usable capacity for: (a) RAID 5, (b) RAID 10. Show your workings. State which RAID level you would recommend for a file server and justify your choice in one sentence. (7 marks)

**18.** List FIVE (5) BIOS/UEFI settings that must be configured before installing a production server OS, and state the recommended value for each. (5 marks)

**19.** Describe the recommended Windows Server post-installation sequence. List FIVE (5) steps that must be completed BEFORE enabling server roles, in the correct order. (5 marks)

**20.** State the recommended account lockout policy (three parameters with values) and explain why a lockout threshold of 3 attempts may cause operational problems in a school environment with 800 students. (6 marks)

**21.** Explain the difference between the "Server Configuration Record" and the "Runbook / SOP" in terms of purpose, content, and primary audience. (3 marks — 1 mark per dimension)

---

## BAHAGIAN C: SOALAN ESEI / SECTION C: ESSAY (40 marks)

Answer both questions.

**22.** Pioneer Academy is deploying a new server infrastructure to support 920 users (800 students + 120 staff). The IT Manager wants: Active Directory (two DCs for redundancy), a centralised file server, DHCP, and DNS. The budget allows two physical servers. The organisation is subject to PDPA 2010.

**(a)** Design the server role architecture. State which roles will be on Server 1 and Server 2, the OS edition, and the RAID configuration for each server's OS and DATA volumes. Justify every decision. (12 marks)

**(b)** After the servers are deployed, a security auditor identifies the following issues: (i) RDP is open to the internet on both servers, (ii) no audit logging is configured, (iii) the data volume is unencrypted. For each issue, explain the risk and the specific remediation steps (include the PowerShell command or GPO path). (12 marks — 4 marks per issue)

**(c)** Three months after go-live, a disk in Server 2's DATA-RAID10 array fails and is replaced with a hot spare. Describe: (i) how you would detect the disk failure (tool and alert mechanism), (ii) the RAID rebuild process and estimated rebuild time considerations, (iii) what change log entry you would make, and (iv) whether a backup restore is required and why. (8 marks)

**23.** A junior IT technician who just completed Level 3 is joining the Level 4 team. They ask: "Why can't I just use the Domain Admin account for everything? It's easier — I only have to remember one password."

Write a structured explanation covering:

**(a)** The concept of the tiered administration model (Tier 0, 1, 2) and what types of tasks each tier account is used for. (8 marks)

**(b)** The specific attack scenarios (at least TWO) that become possible if Domain Admin credentials are used on a standard workstation and are compromised through phishing or malware. (6 marks)

**(c)** The practical alternative you would recommend: what account structure they should use for their daily tasks, server administration tasks, and DC administration tasks. (4 marks)

**(d)** How Group Managed Service Accounts (gMSA) address the password management burden for service accounts, so that the "I only want to remember one password" concern is met for services rather than interactive use. (2 marks)

---

## TAMAT / END OF PAPER

---

*Answer scheme is provided as a separate instructor document.*