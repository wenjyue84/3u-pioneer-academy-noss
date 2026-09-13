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
| KOD DAN NAMA PROGRAM | IT-020-5:2013 PENGURUSAN SISTEM KOMPUTER |
| TAHAP | 5 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-C04 DISASTER RECOVERY MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE DISASTER RECOVERY REQUIREMENTS<br>2. DEVELOP DISASTER RECOVERY MANAGEMENT PLAN<br>3. IMPLEMENT COMPUTER NETWORK DISASTER RECOVERY MANAGEMENT PLAN<br>4. PRODUCE DISASTER RECOVERY MANAGEMENT REPORT |
| NO. KOD | IT-020-5:2013-C04/KP(2/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-02-disaster-recovery-plan-development

**TUJUAN:** Kertas rujukan untuk KP-02-disaster-recovery-plan-development.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Describe the structure and mandatory components of a Disaster Recovery Plan (DRP)
2. Select an appropriate DR strategy based on RTO, RPO, and budget constraints
3. Define DR site types (hot, warm, cold) and select the appropriate type for different system tiers
4. Design a backup and data replication strategy aligned with RPO requirements
5. Develop a DR team structure with defined roles, responsibilities, and escalation procedures

---

## 1.0 Disaster Recovery Plan (DRP) Overview

### 1.1 Definition and Scope

A **Disaster Recovery Plan (DRP) / Pelan Pemulihan Bencana** is a documented, structured, and tested set of procedures that enables an organisation to restore IT systems and data following a disruptive event. The DRP is formally approved by senior management and is reviewed at defined intervals (typically annually or after any significant infrastructure change).

The DRP is distinct from — but aligned with — the **Business Continuity Plan (BCP)**. The BCP addresses how the entire organisation continues to operate (people, premises, processes), while the DRP specifically addresses IT systems, data, and technical infrastructure recovery.

### 1.2 DRP Lifecycle / Kitaran Hayat DRP

```
[Requirements Analysis] → [Strategy Selection] → [Plan Development]
         ↑                                                ↓
    [Review and Update] ← [Testing and Drills] ← [Implementation]
```

The DRP is a living document — it must be updated whenever significant changes occur in infrastructure, personnel, or business requirements.

---

## 2.0 DRP Structure and Components / Struktur dan Komponen DRP

A compliant DRP contains the following sections:

### 2.1 Mandatory Sections / Bahagian Wajib

| Section No. | Section Title | Content |
|-------------|--------------|---------|
| 1 | Purpose and Scope | What the plan covers, what it does not cover |
| 2 | Objectives | RTO and RPO targets for each system tier |
| 3 | Assumptions | Pre-conditions for plan activation |
| 4 | Roles and Responsibilities | DR team structure, contact list, escalation chain |
| 5 | Risk and BIA Summary | Key findings from the requirements analysis phase |
| 6 | System Inventory | Prioritised list of all systems with recovery tiers |
| 7 | DR Strategy | Selected strategy for each tier (hot/warm/cold site, cloud) |
| 8 | Backup and Replication Plan | Backup schedule, media, offsite storage, replication method |
| 9 | Activation Procedures | How and when the plan is invoked; declaration authority |
| 10 | Recovery Procedures | Step-by-step technical recovery procedures per system |
| 11 | Restoration Procedures | Return to normal operations; failback plan |
| 12 | Communication Plan | Internal and external communication during and after disaster |
| 13 | Testing Schedule | Frequency, type, and responsibility for DR tests |
| 14 | Appendices | Contact lists, vendor contracts, network diagrams, system credentials (secured) |

---

## 3.0 DR Strategy Selection / Pemilihan Strategi DR

### 3.1 DR Site Types / Jenis Tapak DR

The primary DR strategy decision is the choice of recovery site:

| Site Type | Description | RTO Achievable | Relative Cost |
|-----------|-------------|---------------|---------------|
| **Hot Site / Tapak Panas** | Fully equipped facility with live, synchronised systems. Immediate failover possible. | Minutes to 1 hour | Highest |
| **Warm Site / Tapak Suam** | Pre-configured hardware and network; systems need data restoration and application startup. | 4–24 hours | Medium |
| **Cold Site / Tapak Sejuk** | Facility with basic utilities (power, cooling, network) but no pre-installed systems. Equipment and data must be shipped or rebuilt. | 24–72 hours or more | Lowest |
| **Cloud DR / DR Awan** | Recovery environment hosted in a public/private cloud (e.g. AWS, Azure, Alibaba Cloud Malaysia). Scales on demand. | Minutes to hours (depends on plan) | Usage-based |
| **Reciprocal Agreement / Perjanjian Timbal Balik** | Arrangement with another organisation to use each other's facilities in case of disaster. | Variable | Low (but unreliable) |

### 3.2 Strategy Selection Matrix

| System Tier | RTO | RPO | Recommended Strategy |
|-------------|-----|-----|---------------------|
| Tier 1 — Critical | < 4 hours | < 1 hour | Hot site or cloud DR with real-time replication |
| Tier 2 — Important | 4–24 hours | 1–4 hours | Warm site with daily incremental backup + log shipping |
| Tier 3 — Normal | 24–48 hours | 24 hours | Cold site or cloud with daily backup |
| Tier 4 — Low | > 48 hours | 24–72 hours | Tape/cloud archive; restore on demand |

### 3.3 Cloud DR Strategies / Strategi DR Awan

Cloud DR offers four main approaches:

| Cloud DR Model | Description | RTO | Cost |
|---------------|-------------|-----|------|
| **Backup and Restore** | Data backed up to cloud; systems rebuilt in cloud when disaster occurs | Hours to days | Low |
| **Pilot Light** | Minimal core infrastructure pre-provisioned in cloud; scaled up at disaster time | Hours | Low–Medium |
| **Warm Standby** | Scaled-down version of full environment running in cloud continuously | Minutes to hours | Medium |
| **Multi-site Active-Active** | Full production running simultaneously in cloud and on-premises; instant failover | Near zero | Highest |

---

## 4.0 Backup and Data Replication Strategy / Strategi Sandaran dan Replikasi Data

### 4.1 Backup Types / Jenis Sandaran

| Backup Type | Description | Advantage | Disadvantage |
|-------------|-------------|-----------|--------------|
| Full Backup / Sandaran Penuh | Complete copy of all selected data | Fastest restore; simple | Longest backup time; most storage |
| Incremental Backup / Sandaran Inkremental | Only data changed since last backup (full or incremental) | Fastest backup; least storage | Slowest restore (requires all incrementals + base) |
| Differential Backup / Sandaran Diferensial | All data changed since last full backup | Moderate backup time; faster restore than incremental | More storage than incremental |
| Continuous Data Protection (CDP) | Every write operation is captured in real time | Near-zero RPO | High cost; performance overhead |

### 4.2 Backup Schedule — Grandfather-Father-Son (GFS) Method

The **GFS rotation scheme** is the standard backup schedule for organisations requiring multiple recovery points:

| Backup Set | Frequency | Retention | Storage Location |
|-----------|-----------|-----------|-----------------|
| Son (Daily) | Every business day | 7 days | On-site NAS / cloud |
| Father (Weekly) | Every Friday (full backup) | 4 weeks | Offsite / cloud |
| Grandfather (Monthly) | Last Friday of month | 12 months | Offsite tape / cloud archive |

### 4.3 Data Replication / Replikasi Data

For Tier 1 and Tier 2 systems requiring RPO < 4 hours, backup alone is insufficient. **Data replication** must be implemented:

| Replication Type | Description | RPO | Use Case |
|-----------------|-------------|-----|---------|
| Synchronous / Segerak | Every write is simultaneously committed to both primary and replica; acknowledgement only after both are written | Zero (0) | Mission-critical databases, financial transaction systems |
| Asynchronous / Tak Segerak | Writes committed to primary first; replica updated at intervals | Minutes | Most enterprise systems; acceptable for most Tier 1 |
| Log Shipping | Database transaction logs copied to standby at intervals and applied | Configurable (minutes to hours) | SQL Server, Oracle; cost-effective for Tier 2 |
| Snapshot Replication | Point-in-time snapshots copied to replica at intervals | Hours | File servers, less critical databases |

### 4.4 Offsite Storage Requirements / Keperluan Penyimpanan Luar Tapak

All backup media must be stored offsite or in the cloud to protect against site-wide disasters:

- **Physical media:** Transported to a secure offsite vault (minimum 10 km from primary site)
- **Cloud backup:** Encrypted during transit (TLS 1.2+) and at rest (AES-256)
- **3-2-1 Rule:** Maintain **3** copies of data, on **2** different media types, with **1** copy offsite

---

## 5.0 DR Team Structure / Struktur Pasukan DR

### 5.1 DR Team Roles / Peranan Pasukan DR

A well-defined DR team is essential for effective plan execution:

| Role | Responsibility |
|------|---------------|
| **DR Coordinator / Penyelaras DR** | Overall accountability for DR plan; declares disaster; coordinates all teams; reports to senior management |
| **IT Infrastructure Lead** | Leads recovery of servers, storage, and network infrastructure |
| **Database Administrator (DBA)** | Responsible for database recovery, replication health, and data validation |
| **Network Engineer** | Restores network connectivity, firewall rules, DNS, and VPN |
| **Application Owner** | Verifies application functionality post-recovery; manages user acceptance testing |
| **Security Officer** | Ensures security controls are maintained during and after recovery |
| **Communication Officer** | Manages internal and external communications; liaises with vendors and regulators |
| **End-user Liaison** | Coordinates with business units; manages user expectations |

### 5.2 Escalation Procedures / Prosedur Eskalasi

Escalation must be defined for each alert level:

| Alert Level | Trigger | Escalation Action |
|-------------|---------|------------------|
| Level 1 — Alert | Single system outage; within normal SLA | IT Operations; no DR activation |
| Level 2 — Warning | Multiple system impact; approaching MTD | IT Manager notified; DR team on standby |
| Level 3 — Critical | MTD breached or imminent breach | DR Coordinator declares disaster; DRP activated |
| Level 4 — Catastrophe | Complete site loss | Senior management, Board, regulators notified; full DR site activation |

### 5.3 Communication Plan / Pelan Komunikasi

During a disaster event, structured communication is critical:

- **Internal:** DR Coordinator → Departmental Heads → Staff (via pre-agreed channels: SMS tree, WhatsApp group, email blast)
- **External:** CEO/Board → Regulators (e.g. CyberSecurity Malaysia, Bank Negara if applicable) → Customers (via website, email) → Media (via Corporate Communications)
- All communications must be logged with timestamp for post-incident review

---

## 6.0 Plan Approval and Maintenance / Kelulusan dan Penyelenggaraan Pelan

### 6.1 Approval Process / Proses Kelulusan

The DRP must be formally approved by:
1. **IT Director / CIO** — technical adequacy
2. **CEO / Managing Director** — organisational commitment and resource allocation
3. **Internal Auditor** — compliance with regulatory requirements

### 6.2 Plan Maintenance / Penyelenggaraan Pelan

The DRP must be reviewed and updated:

| Trigger | Action |
|---------|--------|
| Annual scheduled review | Full review; update contacts, system inventory, RTO/RPO |
| Major infrastructure change (new system, cloud migration) | Update affected sections |
| Personnel change (key DR team member) | Update contact list and role assignments |
| Post-incident review | Update based on lessons learnt |
| Failed DR test | Identify and remediate gaps; re-test |

---

## Rujukan / References

- ISO 22301:2019 — Business Continuity Management Systems — Requirements
- ISO/IEC 27031:2011 — ICT Readiness for Business Continuity
- NIST SP 800-34 Rev.1 — Contingency Planning Guide for Federal Information Systems
- AWS Disaster Recovery Whitepaper (2023)
- Microsoft Azure Business Continuity and Disaster Recovery Guide
- NOSS IT-020-5:2013 CoCU 4 — Disaster Recovery Management