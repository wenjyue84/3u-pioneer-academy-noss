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

## PELAN MENGAJAR – AMALI

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-4:2013 PENTADBIRAN SISTEM KOMPUTER |
| TAHAP | 4 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C01 SERVER CONFIGURATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE SERVER CONFIGURATION REQUIREMENTS<br>2. PLAN SERVER ROLES AND SERVICES<br>3. CONFIGURE SERVER HARDWARE AND STORAGE<br>4. CONFIGURE SERVER OS AND ROLES<br>5. IMPLEMENT SERVER SECURITY SETTINGS<br>6. DOCUMENT SERVER CONFIGURATION |
| NO. KOD | IT-020-4:2013-C01/PM(AMALI) |
| Muka Surat | 1/1 |
| WARNA KERTAS | KUNING (Yellow) |

**TAJUK:** PM-amali-server-configuration

**TUJUAN:** Kertas rujukan untuk PM-amali-server-configuration.

**TEMPAT:** BILIK AMALI / MAKMAL

**TEMPOH:** Rujuk JPW/RK.

**TUJUAN PENGAJARAN:** Pada akhir sesi pengajaran, pelatih akan dapat menguasai pengetahuan/kemahiran berkaitan aktiviti kerja CU ini.

**ALAT BANTUAN MENGAJAR:** Papan putih, projektor, slaid pengajaran, bahan tunjuk-cara.

<!-- /JPK_ENVELOPE_v1 -->
**TEMPAT:** BILIK AMALI / MAKMAL PELAYAN (Server Lab)

**TEMPOH:** 140 jam amali (70% daripada 200 jam CU)

**TUJUAN PENGAJARAN:** Pada akhir semua sesi amali, pelatih akan dapat melaksanakan konfigurasi pelayan secara menyeluruh — daripada analisis keperluan hingga penyerahan dokumentasi — secara berdikari dan mengikut piawaian profesional.

**ALAT BANTUAN MENGAJAR:** Pelayan fizikal atau platform virtualisasi makmal, papan putih, projektor, lembar kerja (KK), senarai semak, dokumentasi vendor.

---

## Agihan Masa Amali / Practical Time Allocation

| KK | Tajuk / Title | Jam / Hours |
|----|--------------|-------------|
| KK(1/6) | Analysing Server Configuration Requirements | 30.0 |
| KK(2/6) | Planning Server Roles and Services | 30.0 |
| KK(3/6) | Configuring Server Hardware and Storage | 50.0 |
| KK(4/6) | Configuring Server OS and Roles | 50.0 |
| KK(5/6) | Implementing Server Security Settings | 30.0 |
| KK(6/6) | Documenting Server Configuration | 10.0 |
| **Jumlah / Total** | | **200.0** |

*Note: Hours stated per KK reflect the total practical time allocated to each work activity across all exercises within that KK. Each KK encompasses multiple iterations and exercises, not a single session.*

---

## Kaedah Pengajaran / Teaching Method (4-Step)

### 1. PERSEDIAAN (Preparation)

| Langkah / Step | Aktiviti / Activity | Masa / Duration |
|----------------|---------------------|-----------------|
| 1.1 | Welcome trainees; take attendance; verify anti-static equipment availability | 5 min |
| 1.2 | State the practical learning objectives for the session — link to the KK and Work Activity | 5 min |
| 1.3 | Review safety rules: hardware ESD, power management, data destruction risk (RAID configuration), credential management | 10 min |
| 1.4 | Distribute the KK (Work Sheet) and explain the exercise structure and deliverables | 5 min |
| 1.5 | Verify all equipment and lab access (server, iDRAC/lab credentials, network access) are available | 5 min |

### 2. PENYAMPAIAN (Demonstration)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 2.1 | Demonstrate the practical task step-by-step on the instructor's server, projected to all trainees |
| 2.2 | Narrate reasoning aloud during demonstration: "I am choosing RAID 10 because this is a database workload with high random I/O requirements, which means RAID 5's write penalty would cause significant performance degradation..." |
| 2.3 | Highlight critical decision points: moments where a wrong choice causes irreversible consequences (wrong RAID disk target, domain join before hardening, BitLocker without recovery key backup) |
| 2.4 | Demonstrate both the correct procedure AND a common error, then show how to detect and resolve it |
| 2.5 | Answer clarification questions before trainees begin independent work |

### 3. PENGGUNAAN (Practice)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 3.1 | Trainees perform the practical task at their individual workstations or assigned server/VM |
| 3.2 | Instructor circulates continuously — observe reasoning, technique, and safety compliance |
| 3.3 | Ask probing oral questions during practice: "Why did you configure that stripe size?", "What would happen if the BBWC fails now?" |
| 3.4 | Trainees record all commands executed and their outputs in the evidence file |
| 3.5 | Trainees complete the KK assessment checklist as they progress through each procedure |

### 4. PENGESAHAN (Confirmation)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 4.1 | Instructor checks each trainee's completed work against the KK assessment checklist |
| 4.2 | Verify the expected outcome is achieved (e.g. dcdiag /v PASSED, RAID Optimal, firewall rules verified) |
| 4.3 | Provide structured feedback: Process (did they follow the right sequence?), Output (is the result correct?), Attitude (were decisions well-reasoned and independent?), Safety (were all precautions observed?) |
| 4.4 | Trainees save all evidence files to the designated network share |
| 4.5 | Record session completion, outcomes, and any issues in the training register |

---

## Rancangan Sesi Amali Terperinci / Detailed Practical Session Plan

### KK(1/6) — Analysing Server Configuration Requirements (30.0 hours)

| Exercise | Activity | Duration |
|----------|---------|---------|
| Ex 1.1 | Scenario brief analysis: read, identify stakeholders, formulate elicitation questions | 6 hr |
| Ex 1.2 | Requirements extraction and categorisation: produce RTM with minimum 10 requirements | 6 hr |
| Ex 1.3 | MoSCoW prioritisation workshop: justify priority for each requirement | 6 hr |
| Ex 1.4 | Gap identification exercise: identify ambiguities; simulate stakeholder clarification | 6 hr |
| Ex 1.5 | Requirements Summary document production and peer review | 6 hr |

### KK(2/6) — Planning Server Roles and Services (30.0 hours)

| Exercise | Activity | Duration |
|----------|---------|---------|
| Ex 2.1 | Role inventory exercise: map requirements to server roles | 6 hr |
| Ex 2.2 | Capacity planning calculations: CPU, RAM, storage (worked independently, then verified) | 6 hr |
| Ex 2.3 | Network topology design using draw.io or Visio: IP addressing, VLANs, firewall zones | 6 hr |
| Ex 2.4 | OS and licensing plan exercise | 4 hr |
| Ex 2.5 | Server Role Plan document production | 4 hr |
| Ex 2.6 | Design presentation: 5-minute verbal presentation to instructor; Q&A; revision | 4 hr |

### KK(3/6) — Configuring Server Hardware and Storage (50.0 hours)

| Exercise | Activity | Duration |
|----------|---------|---------|
| Ex 3.1 | iDRAC/iLO initial configuration: IP, credentials, hardware health verification | 6 hr |
| Ex 3.2 | BIOS/UEFI configuration workshop: full checklist applied and documented | 8 hr |
| Ex 3.3 | RAID configuration — RAID 1 OS volume: creation, verification, and documentation | 8 hr |
| Ex 3.4 | RAID configuration — DATA volume (multiple RAID levels practised across exercises): creation, hot spare, BBWC verification | 12 hr |
| Ex 3.5 | Storage type exploration: NAS share access and iSCSI initiator connection (if lab equipment available) | 8 hr |
| Ex 3.6 | Fault simulation: disconnect one disk; observe RAID degraded state; reconnect; observe rebuild and hot spare activation | 8 hr |

### KK(4/6) — Configuring Server OS and Roles (50.0 hours)

| Exercise | Activity | Duration |
|----------|---------|---------|
| Ex 4.1 | Windows Server 2022 installation: full procedure from USB boot to Administrator password | 6 hr |
| Ex 4.2 | Post-installation configuration: IP, rename, timezone, NTP, RDP, WinRM, updates — all via PowerShell | 8 hr |
| Ex 4.3 | AD DS promotion: new forest (first DC); verification using dcdiag; OU structure creation | 10 hr |
| Ex 4.4 | DNS configuration: reverse zone, forwarders, scavenging; nslookup verification | 6 hr |
| Ex 4.5 | DHCP installation, authorisation, scope, and client lease verification | 6 hr |
| Ex 4.6 | File Services: share creation, NTFS permissions, DFS Namespace configuration | 8 hr |
| Ex 4.7 | Second DC addition exercise: add a replica DC to the domain; verify replication | 6 hr |

### KK(5/6) — Implementing Server Security Settings (30.0 hours)

| Exercise | Activity | Duration |
|----------|---------|---------|
| Ex 5.1 | Windows Firewall: default-deny, role-based rules, source-IP restriction for RDP | 6 hr |
| Ex 5.2 | GPO creation and application: password policy, lockout policy, NTLMv2-only | 6 hr |
| Ex 5.3 | Advanced Audit Policy configuration and verification via Event Viewer | 6 hr |
| Ex 5.4 | Administrator account rename, Guest disable, Security Event Log sizing | 4 hr |
| Ex 5.5 | BitLocker: enable on data volume, recovery key backup, Network Unlock configuration (if WDS available) | 6 hr |
| Ex 5.6 | Security audit simulation: instructor introduces deliberate misconfigurations; trainee identifies and remedies | 2 hr |

### KK(6/6) — Documenting Server Configuration (10.0 hours)

| Exercise | Activity | Duration |
|----------|---------|---------|
| Ex 6.1 | Live configuration data collection: run all audit commands; save evidence file | 1 hr |
| Ex 6.2 | Server Configuration Record completion: all 7 sections from live data | 2 hr |
| Ex 6.3 | As-Built Document: deviations, acceptance tests, known issues | 2 hr |
| Ex 6.4 | Version control and document management | 1 hr |
| Ex 6.5 | Handover walkthrough simulation: role-play with instructor as Operations Lead | 2 hr |
| Ex 6.6 | Handover checklist sign-off and document submission | 2 hr |

---

## Peralatan dan Bahan / Equipment and Materials

| Item | Quantity per Trainee / Group | Notes |
|------|----------------------------|-------|
| Enterprise server (physical: Dell PowerEdge R450/R750, HPE ProLiant DL380 Gen10+, or equivalent) — OR — lab VM with nested virtualisation | 1 | Physical server preferred for WA3; VM acceptable for WA4–WA6 |
| Hardware RAID controller (PERC, Smart Array) | 1 | Built into physical server |
| Enterprise SAS SSD or NVMe drives (minimum 4, matching) | 4 | For RAID configuration exercises |
| Hot spare drive | 1 | For hot spare and rebuild exercises |
| Management workstation with RSAT, GPMC, draw.io or Visio, Word | 1 | Can be shared across 2 trainees |
| Network switch with VLAN support | 1 (shared, 1 per group) | For VLAN exercises |
| Anti-static wrist strap | 1 per trainee | Must be worn at all times during hardware work |
| Anti-static mat | 1 per workstation | Grounded work surface |
| Windows Server 2022 ISO (bootable USB or PXE) | 1 | Volume licence or evaluation copy |
| Microsoft Security Baseline GPO backup | 1 | Downloaded from Microsoft Security Compliance Toolkit |
| Documentation templates (all KK worksheets, Configuration Record, As-Built template) | 1 set | Printed or digital |

---

## Keselamatan / Safety Requirements

- Anti-static wrist strap MUST be worn when handling server components (CPU, RAM, PCIe cards, drive caddies)
- Power must be disconnected before opening the chassis or handling non-hot-swap internal components
- RAID configuration destroys existing data on selected disks — verify the correct disks are selected before confirming configuration
- iDRAC/iLO default credentials must be changed before connecting to the management network — default credentials are a critical vulnerability
- BitLocker recovery key must be backed up before the encryption process is started — losing the key = permanent data loss
- Evidence files containing IP addresses, hostnames, and account names must be treated as confidential — stored in the designated lab share only, not on personal USB drives

---

## Penilaian Amali / Practical Assessment

Upon completion of all 6 KK sessions, trainees will sit for the Performance Assessment (PA):

- **Kod / Code:** IT-020-4:2013-C01/PA
- **Tempoh / Duration:** 6 hours
- **Format:** Full server configuration scenario from requirements analysis to formal handover documentation
- **Pass mark:** 60 / 100; all WAs must achieve minimum 40% of WA maximum marks
- **Assessment criteria:** WA1 Requirements (15), WA2 Planning (15), WA3 Hardware (20), WA4 OS/Roles (20), WA5 Security (15), WA6 Documentation (15)