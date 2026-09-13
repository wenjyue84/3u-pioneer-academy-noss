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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-C01 COMPUTER SYSTEMS PLANNING AND OPERATIONS MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. PLAN RESOURCES<br>2. COORDINATE OPERATIONS<br>3. MONITOR PERFORMANCE<br>4. REPORT TO MANAGEMENT |
| NO. KOD | IT-020-5:2013-C01/KP(1/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-01-resource-planning-capacity-budget-lifecycle

**TUJUAN:** Kertas rujukan untuk KP-01-resource-planning-capacity-budget-lifecycle.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the principles of IT capacity planning and the methods used to forecast resource requirements at an organisational level.
2. Develop and manage an IT capital and operational budget aligned with organisational strategy.
3. Apply IT asset lifecycle management concepts to plan refresh, retirement, and disposal cycles.
4. Evaluate resource planning frameworks including ITIL Capacity Management and ISO 55000 Asset Management.
5. Produce a resource plan that integrates capacity, budget, and lifecycle considerations.

---

## 1.0 Introduction to IT Resource Planning

IT resource planning (Perancangan Sumber IT) is a strategic management function that ensures an organisation has the right computing infrastructure — in the right quantity, at the right cost, and for the right duration — to support its business objectives. At Level 5, the IT Manager is responsible not only for day-to-day operations but for forward-looking plans that align technology investment with organisational direction.

Resource planning encompasses three interdependent domains:

| Domain | Definition | Planning Horizon |
|--------|-----------|-----------------|
| Capacity Planning (Perancangan Kapasiti) | Ensuring sufficient computing, storage, and network resources to meet current and projected demand | 1–3 years |
| Budget Planning (Perancangan Bajet) | Allocating financial resources for IT acquisition, operations, maintenance, and projects | Annual (OPEX) + 3–5 years (CAPEX) |
| Lifecycle Management (Pengurusan Kitaran Hayat) | Managing assets from procurement through operation to retirement and disposal | 3–7 years per asset class |

Failure to integrate these three domains results in over-provisioning (wasted expenditure), under-provisioning (service degradation), or premature/deferred asset replacement (increased risk and cost).

---

## 2.0 Capacity Planning

### 2.1 Concepts and Terminology

| Term | Definition (EN) | Istilah (BM) |
|------|----------------|-------------|
| Capacity | The maximum throughput or volume a system can handle under normal conditions | Kapasiti |
| Demand | The actual or projected workload placed on a system | Permintaan |
| Utilisation | Current usage as a percentage of total capacity | Penggunaan |
| Headroom | Spare capacity reserved to absorb demand spikes | Ruang simpanan |
| Throughput | The volume of transactions or data processed per unit time | Daya pemprosesan |
| Scalability | The ability to increase capacity without redesigning the system | Skalabiliti |

### 2.2 ITIL Capacity Management Process

ITIL (IT Infrastructure Library) defines Capacity Management as a process within Service Design. It comprises three sub-processes:

| Sub-Process | Focus | Key Activities |
|-------------|-------|---------------|
| Business Capacity Management | Translating business plans into IT capacity requirements | Review strategic plans; model future demand scenarios |
| Service Capacity Management | Ensuring IT services have sufficient capacity for agreed SLAs | Monitor service throughput; tune performance; plan upgrades |
| Component Capacity Management | Monitoring and managing individual infrastructure components | Track CPU, RAM, disk I/O, network bandwidth utilisation |

### 2.3 Capacity Planning Methodology

A structured capacity planning cycle consists of the following steps:

1. **Baseline measurement** — Collect historical utilisation data (minimum 3–6 months) for all critical systems: servers, storage, network links, and applications.
2. **Demand forecasting** — Project future demand based on business growth plans, new projects, seasonal patterns, and trend analysis. Use regression analysis or vendor-provided modelling tools.
3. **Gap analysis** — Compare projected demand against current and planned capacity. Identify shortfalls (deficit) and surpluses.
4. **Option evaluation** — Assess options: expand on-premises infrastructure, migrate workloads to cloud (IaaS/PaaS), virtualise, or decommission under-used resources.
5. **Recommendation and approval** — Prepare a Capacity Plan document with recommendations, cost estimates, risk assessment, and a preferred option for management approval.
6. **Implementation and review** — Implement approved changes; schedule quarterly reviews to compare actual vs. planned utilisation.

### 2.4 Capacity Thresholds and Alerting

| Threshold | Recommended Action |
|----------|--------------------|
| Utilisation < 40% | Review for consolidation or virtualisation opportunities |
| Utilisation 40–70% | Normal operating range; continue monitoring |
| Utilisation 70–80% | Issue capacity alert; begin planning expansion |
| Utilisation > 80% | Critical threshold; initiate procurement or cloud burst |

---

## 3.0 Budget Planning

### 3.1 Types of IT Expenditure

IT expenditure is classified into two categories that are managed through different approval and accounting processes:

| Category | Full Name | Examples | Accounting Treatment |
|----------|-----------|---------|---------------------|
| CAPEX | Capital Expenditure (Perbelanjaan Modal) | Servers, network switches, storage arrays, software licences (perpetual) | Capitalised; depreciated over asset life (3–5 years) |
| OPEX | Operational Expenditure (Perbelanjaan Operasi) | Cloud subscriptions, maintenance contracts, internet bandwidth, staff salaries, consumables | Expensed in the period incurred |

### 3.2 IT Budget Development Process

| Phase | Activities |
|-------|-----------|
| 1. Requirements gathering | Identify planned projects, hardware refresh needs, new services, and increased operational costs from department heads and IT sub-units |
| 2. Cost estimation | Obtain vendor quotations; apply depreciation schedules; estimate resource consumption (cloud, power, facilities) |
| 3. Prioritisation | Rank requests by strategic alignment, risk impact, and regulatory compliance requirement |
| 4. Budget submission | Prepare the IT budget proposal in the required format (line-item budget); submit to Finance and Senior Management for approval |
| 5. Monitoring and control | Track actual expenditure monthly against approved budget; report variances; manage re-allocation requests |
| 6. Year-end review | Analyse budget vs. actuals; document lessons learned; carry forward multi-year CAPEX commitments |

### 3.3 Key Budget Line Items

| Budget Line | Description |
|------------|-------------|
| Hardware acquisition | New servers, workstations, network equipment, storage |
| Software licences | Operating systems, productivity suites, security tools, ERP/business applications |
| Cloud services | IaaS, PaaS, SaaS subscriptions; data transfer costs |
| Maintenance and support | Annual maintenance contracts (AMC) with OEMs and resellers |
| Staff and training | IT staff salaries, contractor fees, professional development |
| Security | Firewalls, endpoint protection, penetration testing, compliance audits |
| Disaster recovery | Backup infrastructure, DR site costs, BCP testing |
| Contingency | Typically 5–10% of total IT budget for unplanned expenditure |

### 3.4 Total Cost of Ownership (TCO)

TCO analysis evaluates all costs associated with an asset over its full lifecycle, not only the purchase price. The TCO formula is:

**TCO = Acquisition Cost + Installation Cost + Annual Operating Cost × Asset Life + Disposal Cost**

TCO is essential when comparing procurement options (e.g., on-premises server vs. cloud subscription) to ensure like-for-like financial comparison.

---

## 4.0 IT Asset Lifecycle Management

### 4.1 Lifecycle Phases

| Phase | Activities | Key Decision Point |
|-------|-----------|-------------------|
| Plan | Define requirements; evaluate options; budget approval | Approve or defer acquisition |
| Procure | Tender process; vendor selection; purchase order | Award contract to vendor |
| Deploy | Receive, configure, test, and commission the asset | Accept and register in CMDB |
| Operate | Provide service; monitor performance; apply patches and updates | Ongoing SLA compliance |
| Refresh/Upgrade | Assess upgrade options when capacity or support approaches end | Upgrade vs. replace decision |
| Retire | Decommission; migrate workloads; data sanitisation | Approve retirement |
| Dispose | Physical disposal: e-waste recycling, resale, or destruction | Certificate of destruction issued |

### 4.2 Asset Lifecycle Timelines

| Asset Class | Typical Useful Life | Refresh Trigger |
|------------|--------------------|--------------------|
| Desktop / Laptop PCs | 3–5 years | End of OS support; performance degradation |
| Servers | 5–7 years | End of vendor hardware support; capacity limitation |
| Network switches and routers | 7–10 years | End of firmware support; throughput limitation |
| Storage arrays | 5–7 years | End of support; capacity exhaustion |
| UPS / Power infrastructure | 5–10 years | Battery replacement cycle; load capacity |
| Software licences (perpetual) | Until end-of-support | Vendor EOL announcement |

### 4.3 CMDB and Asset Register

The Configuration Management Database (CMDB / Pangkalan Data Pengurusan Konfigurasi) is the authoritative record of all IT assets (Configuration Items, CIs). Each CI record contains:

| Field | Description |
|-------|-------------|
| Asset ID | Unique identifier (barcode or RFID tag) |
| Asset name and model | Manufacturer, model number, serial number |
| Location | Physical rack, room, building, or cloud region |
| Owner and custodian | Department owner; IT team custodian |
| Purchase date and cost | Procurement date; invoice value |
| Warranty and support expiry | End of warranty; end of vendor support contract |
| Current status | Active, spare, under maintenance, retired |
| Linked CIs | Dependencies (e.g., server linked to storage, network switch, applications) |

A well-maintained CMDB enables automated lifecycle alerts (e.g., 6-month warning before warranty expiry) and supports accurate budget planning.

---

## 5.0 Integrated Resource Planning

Effective resource planning integrates all three domains into a single planning document — the IT Resource Plan — which is reviewed annually and updated quarterly:

| Section | Content |
|---------|---------|
| Executive Summary | Key findings, recommendations, and financial impact |
| Current State Assessment | Utilisation baseline, asset register snapshot, budget actuals |
| Demand Forecast | Business growth projections; new IT requirements from departments |
| Capacity Plan | Gap analysis; recommended expansions, consolidations, or migrations |
| Asset Lifecycle Schedule | Assets due for refresh or retirement in the next 1–3 years |
| Budget Plan | CAPEX and OPEX projections by year; prioritised investment list |
| Risk Assessment | Risks of under-investment, over-investment, or deferred refresh |
| Governance | Approval authority, review schedule, escalation path |

---

## 6.0 Common Errors in Resource Planning

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Planning capacity in isolation (no link to business demand) | Over- or under-provisioning; misaligned investment | Conduct business capacity management review with all department heads before finalising the plan |
| Ignoring TCO; comparing only acquisition costs | Cloud or refresh decisions based on incomplete financial data | Always present full TCO analysis covering at least 3–5 years |
| Not updating the CMDB when assets are deployed or retired | Asset register inaccurate; lifecycle alerts missed | Enforce CMDB update as a mandatory step in the change management process |
| Treating the IT budget as a fixed allocation without variance tracking | Overspending discovered only at year-end | Implement monthly budget vs. actuals reporting with escalation triggers |
| Deferring asset refresh beyond vendor end-of-support dates | Security vulnerabilities; inability to obtain patches | Include vendor support expiry dates in CMDB and trigger refresh planning 12 months before EOL |

---

## Rujukan / References

- NOSS IT-020-5:2013 Computer Systems Management — CoCu 1
- ITIL 4 Foundation: AXELOS (2019) — Capacity and Performance Management Practice
- ISO 55000:2014 — Asset Management: Overview, Principles and Terminology
- Malaysian Government ICT Strategic Plan (PITA) — Ministry of Communications and Digital
- Microsoft Azure Well-Architected Framework — Cost Optimisation Pillar
- ISACA COBIT 2019 — APO06 Managed IT Budget and Costs