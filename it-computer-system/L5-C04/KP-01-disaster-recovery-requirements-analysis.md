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
| NO. KOD | IT-020-5:2013-C04/KP(1/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-01-disaster-recovery-requirements-analysis

**TUJUAN:** Kertas rujukan untuk KP-01-disaster-recovery-requirements-analysis.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Define disaster recovery (DR), business continuity (BC), and their relationship to organisational resilience
2. Conduct a Business Impact Analysis (BIA) to identify critical systems, processes, and recovery priorities
3. Define and calculate Recovery Time Objective (RTO) and Recovery Point Objective (RPO) for critical systems
4. Identify threats, vulnerabilities, and risk exposure relevant to IT infrastructure disaster scenarios
5. Document DR requirements in a structured format compliant with ISO 22301:2019

---

## 1.0 Introduction to Disaster Recovery Management

### 1.1 Definitions / Takrifan

**Disaster Recovery (DR) / Pemulihan Bencana** is the set of policies, tools, and procedures that enable the recovery or continuation of vital IT infrastructure and systems following a natural or human-induced disaster. DR is a subset of the broader discipline of **Business Continuity Management (BCM)**.

**Business Continuity (BC) / Kesinambungan Perniagaan** refers to the capability of an organisation to continue delivery of products or services at acceptable predefined levels following a disruptive incident. While BC addresses the entire organisation (including people, facilities, and supply chains), DR focuses specifically on IT systems, data, and network infrastructure.

**ISO 22301:2019** is the international standard for Business Continuity Management Systems (BCMS). It provides the framework for planning, establishing, implementing, operating, monitoring, reviewing, and continually improving a BCMS. Malaysian organisations seeking formal certification must comply with this standard.

| Term / Istilah | Definition |
|---------------|------------|
| Disaster / Bencana | Any event that disrupts normal operations and exceeds the organisation's capacity to respond with existing resources |
| Recovery / Pemulihan | The process of restoring IT systems, data, and operations to a defined minimum service level |
| Residual Risk / Risiko Baki | Risk remaining after controls have been applied |
| Maximum Tolerable Downtime (MTD) / Masa Henti Tertanggung Maksimum | The maximum time an organisation can tolerate the absence of a critical function before suffering unacceptable consequences |

### 1.2 Why DR Planning is Critical / Kepentingan Perancangan DR

Organisations are exposed to an increasingly complex threat landscape:

- **Natural disasters / Bencana alam:** Flooding (banjir), fire (kebakaran), earthquake (gempa bumi), lightning strikes (petir)
- **Technical failures / Kegagalan teknikal:** Hardware failure, power outage (gangguan bekalan kuasa), network failure, storage corruption
- **Human-induced incidents / Insiden manusia:** Cyberattacks (ransomware, DDoS), accidental deletion (pemadaman tidak sengaja), insider threats (ancaman dalaman)
- **Pandemic or mass-absence events:** Key personnel unavailability affecting operations

Without a tested DR plan, organisations risk extended downtime (masa henti yang panjang), data loss (kehilangan data), financial loss (kerugian kewangan), regulatory penalties (penalti kawal selia), and reputational damage (kerosakan reputasi).

---

## 2.0 Business Impact Analysis (BIA) / Analisis Impak Perniagaan

### 2.1 Purpose of BIA

A **Business Impact Analysis (BIA)** is the foundational step in DR requirements analysis. It systematically identifies business functions and processes, the IT systems that support them, and the impact of their disruption over time. The BIA output directly drives RTO and RPO values.

### 2.2 BIA Methodology / Kaedah BIA

The BIA process follows these steps:

1. **Identify business functions / Kenal pasti fungsi perniagaan:** Enumerate all organisational processes and departments (e.g. payroll, customer service, production control, inventory management)
2. **Map IT dependencies / Petakan kebergantungan IT:** For each business function, identify the supporting IT systems, applications, databases, and network components
3. **Assess impact over time / Nilai impak mengikut masa:** For each function, determine the financial, operational, regulatory, and reputational impact of non-availability at intervals: 1 hour, 4 hours, 8 hours, 24 hours, 72 hours
4. **Determine MTD / Tentukan MTD:** The point at which impact becomes unacceptable — this defines the outer boundary for recovery
5. **Prioritise / Utamakan:** Rank systems by criticality to establish recovery priority tiers

### 2.3 Impact Categories / Kategori Impak

| Impact Category | Description / Huraian |
|----------------|-----------------------|
| Financial / Kewangan | Revenue loss, penalty payments, contractual claims |
| Operational / Operasi | Inability to deliver services or products; staff unable to work |
| Regulatory / Kawal Selia | Breaches of legal or regulatory requirements (e.g. PDPA, Bank Negara guidelines) |
| Reputational / Reputasi | Customer and stakeholder confidence loss |
| Health and Safety / Keselamatan | Risk to personnel if life-safety systems are affected |

### 2.4 Sample BIA Table / Contoh Jadual BIA

| Business Function | Supporting IT System | MTD | Financial Impact (RM/hr) | Priority Tier |
|------------------|---------------------|-----|--------------------------|--------------|
| Online sales platform | E-commerce application + database | 4 hours | RM 50,000 | Tier 1 (Critical) |
| Payroll processing | HR/payroll system | 72 hours | RM 10,000 | Tier 2 (Important) |
| Internal email | Mail server | 24 hours | RM 2,000 | Tier 3 (Normal) |
| Staff training portal | LMS | 1 week | RM 500 | Tier 4 (Low) |

---

## 3.0 Recovery Time Objective (RTO) and Recovery Point Objective (RPO)

### 3.1 RTO / Objektif Masa Pemulihan

**RTO (Recovery Time Objective)** is the maximum acceptable duration of time within which a system must be restored after a disaster occurs, before the consequences become unacceptable to the organisation.

- RTO is derived from the BIA: RTO ≤ MTD
- A Tier 1 critical system may have an RTO of 1–4 hours
- A Tier 3 system may have an RTO of 24–48 hours

**Formula:** RTO = Maximum Tolerable Downtime − Recovery Preparation Time

### 3.2 RPO / Objektif Titik Pemulihan

**RPO (Recovery Point Objective)** is the maximum acceptable amount of data loss measured in time. It defines how old the recovered data may be.

- RPO drives backup frequency decisions
- An RPO of 1 hour means backups must occur at least every hour
- An RPO of 0 (zero) requires continuous real-time replication

| RPO Value | Backup Strategy Required |
|-----------|-------------------------|
| 0 (zero data loss) | Synchronous real-time replication |
| < 1 hour | Continuous data protection (CDP) or log shipping |
| 1–4 hours | Scheduled incremental backup every 1–4 hours |
| 4–24 hours | Daily incremental backup |
| > 24 hours | Full daily backup (offline acceptable) |

### 3.3 RTO vs RPO Relationship

```
Disaster Event
     │
     ▼
[Data lost since last backup = RPO]
     │
     ▼
[Recovery begins — IT team activates DR plan]
     │
     ▼
[System restored to minimum service level = RTO]
```

Both RTO and RPO must be formally agreed upon by senior management and documented in the DR Plan. They represent a cost-benefit trade-off: shorter RTO/RPO requires more expensive infrastructure (e.g. hot standby site, real-time replication).

---

## 4.0 Threat and Risk Assessment / Penilaian Ancaman dan Risiko

### 4.1 Threat Identification / Pengenalpastian Ancaman

A threat is any potential cause of an unwanted incident that may result in harm to the organisation or its IT systems. Threats are categorised as:

| Threat Type | Examples |
|-------------|---------|
| Environmental / Persekitaran | Flood, fire, storm, power failure |
| Technical / Teknikal | Hardware failure, software bug, storage media failure, network outage |
| Cyber / Siber | Ransomware, DDoS attack, data breach, phishing |
| Human / Manusia | Accidental deletion, misconfiguration, insider attack, sabotage |
| Supply chain / Rantaian Bekalan | Vendor failure, ISP outage, cloud provider disruption |

### 4.2 Risk Assessment / Penilaian Risiko

Risk is assessed using the formula:

**Risk = Likelihood × Impact**

| Likelihood | Rating | Description |
|-----------|--------|-------------|
| Rare | 1 | Once in 10 years or more |
| Unlikely | 2 | Once in 5 years |
| Possible | 3 | Once in 2 years |
| Likely | 4 | Once per year |
| Almost Certain | 5 | Multiple times per year |

| Impact | Rating | Description |
|--------|--------|-------------|
| Negligible | 1 | Minimal disruption; <1 hour downtime |
| Minor | 2 | Localised disruption; 1–4 hours downtime |
| Moderate | 3 | Significant disruption; 4–24 hours; financial loss |
| Major | 4 | Extended outage; major financial/regulatory impact |
| Catastrophic | 5 | Total system failure; regulatory action; severe data loss |

Risk scores of 15–25 are **HIGH RISK** and require immediate mitigation. Scores of 8–14 are **MEDIUM RISK**. Scores of 1–7 are **LOW RISK**.

### 4.3 Gap Analysis / Analisis Jurang

After identifying risks, the DR analyst compares existing controls against the required level of protection. Gaps are documented and form the basis of DR investment recommendations:

- **No backup solution** → HIGH gap; immediate action required
- **Backup present but untested** → MEDIUM gap; test schedule required
- **No offsite backup** → HIGH gap; implement offsite/cloud backup
- **Single point of failure (SPOF)** in network or power → HIGH gap; redundancy required

---

## 5.0 DR Requirements Documentation / Dokumentasi Keperluan DR

### 5.1 DR Requirements Report Structure

The output of the requirements analysis phase is a formal **DR Requirements Report** containing:

1. **Executive Summary / Ringkasan Eksekutif** — scope, objectives, key findings
2. **BIA Results / Keputusan BIA** — prioritised system list with MTD, RTO, RPO values
3. **Threat and Risk Register / Daftar Ancaman dan Risiko** — all identified threats, likelihood, impact, risk scores
4. **Gap Analysis / Analisis Jurang** — current state vs. required state
5. **Recovery Tier Classification / Pengelasan Peringkat Pemulihan** — Tier 1–4 system classification
6. **Recommendations / Cadangan** — DR strategy options with cost-benefit analysis
7. **Assumptions and Constraints / Andaian dan Kekangan** — budget, staffing, technology limitations

### 5.2 ISO 22301:2019 Alignment

Requirements documentation must align with Clause 8.2 (Business Impact Analysis and Risk Assessment) of ISO 22301:2019. Key elements:

- The organisation shall determine the impacts of disruptions over time
- The organisation shall set prioritised timeframes for resuming activities
- The organisation shall identify dependencies between activities and resources

---

## Rujukan / References

- ISO 22301:2019 — Business Continuity Management Systems — Requirements
- NIST SP 800-34 Rev.1 — Contingency Planning Guide for Federal Information Systems
- NOSS IT-020-5:2013 CoCU 4 — Disaster Recovery Management
- Department of Statistics Malaysia — Risk Management Guidelines
- MAMPU — Malaysian Public Sector ICT Strategic Plan