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
| KOD DAN NAMA PROGRAM | IT-020-4:2013 PENTADBIRAN SISTEM KOMPUTER |
| TAHAP | 4 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C01 SERVER CONFIGURATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE SERVER CONFIGURATION REQUIREMENTS<br>2. PLAN SERVER ROLES AND SERVICES<br>3. CONFIGURE SERVER HARDWARE AND STORAGE<br>4. CONFIGURE SERVER OS AND ROLES<br>5. IMPLEMENT SERVER SECURITY SETTINGS<br>6. DOCUMENT SERVER CONFIGURATION |
| NO. KOD | IT-020-4:2013-C01/KP(1/6) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-01-server-configuration-requirements-analysis

**TUJUAN:** Kertas rujukan untuk KP-01-server-configuration-requirements-analysis.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the purpose and components of a server configuration requirements document
2. Distinguish between business, technical, and compliance requirements for server deployment
3. Apply a structured methodology to analyse and validate server requirements
4. Identify common gaps and ambiguities in requirements documents and recommend remediation actions
5. Produce a verified requirements summary ready for planning and procurement

---

## 1.0 Introduction to Server Configuration Requirements Analysis

At Level 4, the IT administrator operates at an administrative and managerial altitude. Unlike a Level 3 technician who assembles a single workstation from a completed job request, a Level 4 administrator must interpret organisational needs, translate them into precise technical specifications, and validate those specifications against capacity, security, and compliance constraints before a single component is ordered or a service is enabled.

A server is a shared, critical resource. Errors in requirements analysis propagate downstream into procurement, installation, and long-term operations. An undersized server may fail under production load; an over-provisioned server wastes capital expenditure. Misunderstanding a compliance requirement (e.g. data residency) may expose the organisation to regulatory penalties.

Requirements analysis (Analisis Keperluan) is therefore the most consequential phase of server configuration. All subsequent planning, hardware selection, and configuration decisions depend on the accuracy and completeness of the requirements captured here.

---

## 2.0 Categories of Server Requirements

Server requirements fall into three primary categories:

| Category | Description | Examples |
|----------|-------------|---------|
| **Business Requirements** (Keperluan Perniagaan) | What the organisation needs to achieve; derived from stakeholders and organisational strategy | "Support 500 concurrent users", "99.9% uptime SLA", "data must remain in Malaysia" |
| **Technical Requirements** (Keperluan Teknikal) | Specific hardware, software, and architectural specifications | CPU cores, RAM capacity, storage type and IOPS, OS version, network interface speed |
| **Compliance Requirements** (Keperluan Pematuhan) | Regulatory, legal, and policy mandates that the server configuration must satisfy | PDPA 2010 (Personal Data Protection Act), ISO/IEC 27001, organisational IT security policy, software licensing terms |

All three categories must be captured, cross-referenced, and validated. A server may meet business and technical requirements but fail a compliance audit if encryption-at-rest is not configured.

---

## 3.0 Stakeholders and Requirements Sources

Requirements are gathered from multiple stakeholders (Pemegang Kepentingan):

| Stakeholder | Typical Input |
|-------------|--------------|
| Business Owner / Department Head | Service level expectations, user count, growth projections, budget ceiling |
| IT Manager | Existing infrastructure topology, standards, integration constraints |
| Application Owner | Application architecture, software prerequisites, performance benchmarks |
| Security Officer (CISO/ISO) | Security policy, hardening standards, audit requirements |
| Compliance / Legal | Regulatory requirements, data classification, retention policy |
| Operations / Helpdesk | Manageability, monitoring integration, support escalation paths |

The administrator must conduct structured interviews or review formal Request for Proposal (RFP) / Project Scope documents to extract requirements from each stakeholder group.

---

## 4.0 Structured Requirements Analysis Methodology

A systematic four-phase methodology ensures completeness:

### Phase 1: Elicitation (Penggalian Maklumat)

1. Review all available documentation: project brief, existing infrastructure diagrams, SLA agreements, previous incident reports
2. Conduct stakeholder interviews using a structured questionnaire covering: workload type, user concurrency, data volume, retention period, peak load characteristics, geographic distribution
3. Identify the server's primary role: file server, application server, database server, web server, directory services server, virtualisation host, or hybrid

### Phase 2: Classification (Pengkelasan Keperluan)

4. Categorise each collected requirement as Business, Technical, or Compliance
5. Tag each requirement with a priority: **Must Have** (M), **Should Have** (S), or **Nice to Have** (N) using MoSCoW prioritisation
6. Identify dependencies between requirements (e.g. "high availability" depends on "redundant power supply" and "network bonding")

### Phase 3: Validation (Pengesahan)

7. Cross-check technical specifications against business requirements: does the specified CPU and RAM actually support the stated concurrent user count?
8. Verify that compliance requirements are addressed: are data encryption, audit logging, and access control mechanisms specified?
9. Identify gaps: requirements that cannot be fulfilled within the stated budget or timeline, and escalate for stakeholder decision

### Phase 4: Documentation (Dokumentasi)

10. Produce a verified Requirements Summary document (Ringkasan Keperluan Pelayan) containing: stakeholder list, categorised requirements table, MoSCoW priorities, dependency matrix, identified gaps, and sign-off from the authorising manager
11. Baseline the requirements: once signed off, changes must go through a formal change request process

---

## 5.0 Key Technical Parameters to Capture

The following technical parameters must be captured for every server configuration project:

| Parameter | Description | Typical Values / Notes |
|-----------|-------------|----------------------|
| **Workload Type** (Jenis Beban Kerja) | Characterises the server's primary function | OLTP, OLAP, file serving, web serving, virtualisation, mixed |
| **CPU Requirements** | Number of physical cores, clock speed, architecture | e.g. Minimum 16 cores @ 2.4 GHz, x86-64, ECC-capable |
| **RAM Requirements** | Total capacity, memory type, ECC | e.g. 64 GB ECC DDR5; identify if memory-intensive workload (database) |
| **Storage Capacity** | Total usable storage in TB, growth rate | e.g. 10 TB usable now, 30% annual growth; specify raw vs usable |
| **Storage Performance** | IOPS, throughput, latency targets | e.g. Minimum 50,000 IOPS sustained for database workload |
| **Storage Type** | NVMe SSD, SAS SSD, SATA HDD, tiered | Select based on performance-cost trade-off |
| **Network Requirements** | Interface speed, number of NICs, VLAN, redundancy | e.g. 2 x 10GbE bonded; VLAN 10 (production), VLAN 20 (management) |
| **Availability Target** | Uptime percentage, RTO, RPO | e.g. 99.9% = ≤8.76 hrs downtime/year; RTO 4hr, RPO 1hr |
| **Scalability** | Horizontal/vertical scale expectation | e.g. CPU and RAM upgradeable to 32 cores / 256 GB without OS reinstall |
| **OS and Software** | Operating system, edition, licensing model | e.g. Windows Server 2022 Standard; or RHEL 9 with subscription |
| **Virtualisation** | Whether the server will host VMs; hypervisor type | e.g. VMware vSphere 8, Hyper-V, Proxmox |
| **Security Requirements** | Encryption, hardening baseline, access model | e.g. BitLocker / dm-crypt at rest; CIS Level 1 hardening; MFA for admin |
| **Management Interface** | Out-of-band management, remote console | e.g. iDRAC9 Enterprise, iLO6, IPMI 2.0 |
| **Physical Constraints** | Rack space (U), power draw (W), cooling (BTU) | e.g. Maximum 2U; 800W TDP; data centre cooling capacity |

---

## 6.0 Requirements Traceability Matrix (RTM)

The Requirements Traceability Matrix (Matriks Keterjelajanaan Keperluan) links each requirement to its source, priority, and implementation artefact:

| Req ID | Requirement Description | Source | Category | Priority | Design Reference |
|--------|------------------------|--------|----------|----------|-----------------|
| R-001 | Support 500 concurrent users | Business Owner | Business | M | Hardware sizing report |
| R-002 | 99.9% uptime SLA | SLA Agreement | Business | M | HA/failover design |
| R-003 | 64 GB ECC RAM minimum | App Owner | Technical | M | Server hardware spec |
| R-004 | Data at rest encrypted (AES-256) | Security Officer | Compliance | M | OS security config |
| R-005 | Data residency: Malaysia only | Legal | Compliance | M | Data centre selection |
| R-006 | Automated daily backup to offsite | IT Policy | Compliance | M | Backup plan |
| R-007 | Remote management via iDRAC | IT Manager | Technical | S | Server hardware spec |

The RTM is maintained throughout the project lifecycle and updated when requirements change or are implemented.

---

## 7.0 Common Errors in Requirements Analysis

| Error | Consequence | Prevention |
|-------|-------------|------------|
| **Incomplete stakeholder engagement** — security or compliance stakeholders not consulted | Server deployed without encryption or audit logging; fails compliance audit | Include all stakeholder groups in the requirements plan; use a RACI matrix |
| **Vague performance requirements** — "fast" or "responsive" without numerical targets | Hardware undersized; SLA disputes after go-live | Require quantified targets: IOPS, latency, concurrent user count |
| **Ignoring growth projections** — sizing for current load only | Server undersized within 12–18 months; unplanned upgrade disrupts operations | Apply a 3-year growth factor (minimum 30% headroom above current peak) |
| **Conflating raw and usable storage** — specifying raw TB without accounting for RAID or filesystem overhead | Insufficient usable storage on day one | Always state usable TB; document RAID level and overhead calculation |
| **Missing compliance mapping** — requirements captured but not mapped to specific technical controls | Technical design does not implement a required control | Use RTM; have compliance officer review before sign-off |
| **Unvalidated assumptions** — administrator assumes budget is unlimited or downtime is acceptable | Scope creep or conflict at procurement | Document all assumptions; get stakeholder sign-off on the Requirements Summary |

---

## Rujukan / References

- NOSS IT-020-4:2013 Computer Systems Administration — CoCu 1: Server Configuration
- Microsoft Windows Server documentation: https://docs.microsoft.com/en-us/windows-server/
- Red Hat Enterprise Linux Administration Guide: https://access.redhat.com/documentation/
- PDPA 2010 (Personal Data Protection Act 2010), Malaysia
- ISO/IEC 27001:2022 Information Security Management
- CompTIA Server+ Study Guide — Requirements and Planning Chapter