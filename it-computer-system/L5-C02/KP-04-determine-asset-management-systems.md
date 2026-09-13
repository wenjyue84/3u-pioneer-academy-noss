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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-C02 COMPUTER SYSTEM ASSET MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE COMPUTER SYSTEM ASSET INVENTORY<br>2. DEFINE OPERATIONAL STATUS OF ASSETS<br>3. ESTIMATE COSTS AND SPACE REQUIREMENTS<br>4. DETERMINE ASSET MANAGEMENT SYSTEMS<br>5. MONITOR ASSET TAGGING AND LABELLING<br>6. EXECUTE ASSET DISPOSAL<br>7. PREPARE ASSET MANAGEMENT REPORTS |
| NO. KOD | IT-020-5:2013-C02/KP(4/7) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-04-determine-asset-management-systems

**TUJUAN:** Kertas rujukan untuk KP-04-determine-asset-management-systems.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Describe the functional requirements of an IT Asset Management (ITAM) system
2. Compare and evaluate different ITAM software platforms (open source vs commercial)
3. Explain the architecture and key modules of an enterprise ITAM system
4. Define the criteria for selecting an appropriate ITAM system for an organisation
5. Describe the implementation process for deploying an ITAM system
6. Explain the integration of ITAM with CMDB, procurement, and financial systems

---

## 1.0 What Is an Asset Management System?

An IT Asset Management (ITAM) system is a software platform that provides a centralised repository and workflow engine for tracking, managing, and reporting on IT assets throughout their lifecycle. At Level 5, the asset manager is responsible for evaluating, selecting, and overseeing the implementation of an ITAM system.

A mature ITAM system supports:
- Asset discovery (automatic network scanning and agent-based detection)
- Asset register management (CRUD operations on asset records)
- Licence management (software licence tracking and compliance)
- Contract management (vendor contracts, warranty, support agreements)
- Financial management (depreciation, TCO, budget forecasting)
- Workflow management (procurement requests, repair tickets, disposal approvals)
- Reporting and dashboards (management reports, audit exports)

---

## 2.0 Functional Requirements of an ITAM System

Before selecting an ITAM platform, the organisation must define its functional requirements:

| Requirement Category | Specific Requirements |
|---------------------|----------------------|
| **Asset Discovery** | Auto-discovery via network scan (SNMP, WMI, SSH); agent-based discovery for endpoints; integration with Active Directory |
| **Asset Register** | Custom fields; mandatory field enforcement; asset history log; bulk import/export (CSV, Excel) |
| **Licence Management** | Software licence tracking; compliance dashboard (purchased vs deployed); alert for over-deployment or approaching renewal |
| **Contract Management** | Vendor contract repository; warranty tracking; renewal reminders; SLA tracking |
| **Financial Management** | Depreciation calculation (straight-line, reducing balance); TCO tracking; integration with accounting system |
| **Workflows** | Configurable approval workflows for procurement, repair, and disposal; email notifications |
| **Reporting** | Standard reports (asset list, status summary, licence compliance); custom report builder; scheduled report delivery |
| **Security and Access Control** | Role-based access control (RBAC); audit trail; data encryption at rest and in transit |
| **Integration** | API connectivity to CMDB, procurement, HR, and financial systems |
| **Scalability** | Support for organisation's current asset count with room to grow; multi-site capability |

---

## 3.0 ITAM Software Platforms

### 3.1 Open Source Platforms

| Platform | Key Features | Suitable For |
|----------|-------------|-------------|
| **Snipe-IT** | Web-based; asset and accessory tracking; check-in/check-out; REST API; licence management; active development community | SMEs, educational institutions, public sector with limited budget |
| **GLPI** | Comprehensive ITAM + helpdesk; network auto-discovery (FusionInventory plugin); contract and document management; multilingual | Mid-size organisations; IT departments managing both assets and service requests |
| **OCS Inventory NG** | Lightweight agent-based inventory; integrates with GLPI; hardware and software discovery | Supplementary discovery tool; used alongside a full ITAM platform |
| **Ralph** | Django-based; data centre and back office ITAM; rack and data centre visualisation | Organisations with significant data centre infrastructure |

### 3.2 Commercial Platforms

| Platform | Key Features | Suitable For |
|----------|-------------|-------------|
| **ManageEngine AssetExplorer** | Full lifecycle ITAM; software licence management; purchase order management; integration with ServiceDesk Plus | Mid-size to large enterprises |
| **ServiceNow ITAM** | Enterprise-grade; deep CMDB integration; SAM Pro for software asset management; HAM Pro for hardware | Large enterprises; organisations already on ServiceNow ITSM |
| **Lansweeper** | Strong network discovery; hardware and software inventory; IT asset reporting; cloud-based option | Enterprises prioritising comprehensive discovery |
| **IBM Maximo** | Enterprise asset management (EAM); includes IT, facilities, and physical assets; advanced maintenance management | Large organisations managing mixed IT and non-IT assets |
| **Flexera One** | Strong SAM (Software Asset Management); licence optimisation; cloud cost management | Organisations with complex software licence portfolios |

### 3.3 Comparison Matrix

| Criterion | Snipe-IT | GLPI | ManageEngine | ServiceNow ITAM |
|-----------|---------|------|-------------|----------------|
| Cost | Free (self-hosted) | Free (self-hosted) | RM 15,000–60,000/yr | RM 100,000+/yr |
| Auto-discovery | Limited (plugin) | Yes (FusionInventory) | Yes | Yes |
| SAM (Software AM) | Basic | Basic | Comprehensive | Comprehensive |
| CMDB integration | Via API | Via API | Native | Native (same platform) |
| Financial reporting | Basic | Moderate | Advanced | Advanced |
| Implementation complexity | Low | Moderate | Moderate | High |
| Vendor support | Community | Community | Commercial | Commercial |
| Malaysian language | Partial | Partial | English only | English only |

---

## 4.0 Selection Criteria for an ITAM System

Selecting the right ITAM system requires a structured evaluation against organisational needs, budget, and technical capability.

### 4.1 Evaluation Framework

| Criterion | Weighting | Evaluation Method |
|-----------|-----------|-------------------|
| Functional coverage (meets requirements list) | 30% | Gap analysis against requirements |
| Total cost of ownership (5-year) | 25% | Vendor quotation + internal cost estimate |
| Ease of use (user acceptance) | 15% | Proof of Concept (PoC) with key users |
| Integration capability | 15% | API documentation review; integration test |
| Vendor support and community | 10% | Reference checks; support SLA review |
| Security and compliance | 5% | Security audit; data protection compliance |
| **Total** | **100%** | |

### 4.2 Proof of Concept (PoC) Process

Before committing to a platform, a PoC should be conducted:

1. Install or provision a trial instance of the shortlisted platform
2. Import a sample dataset (100–200 assets from the actual asset register)
3. Test key workflows: asset creation, discovery, licence tracking, report generation
4. Involve end users (IT administrators, finance staff) in evaluation
5. Document findings against the requirements list
6. Score each platform and present findings to the decision-making committee

---

## 5.0 ITAM System Architecture

A typical enterprise ITAM deployment includes:

| Component | Description |
|-----------|-------------|
| **Application Server** | Hosts the ITAM web application; may be on-premises or cloud (SaaS) |
| **Database Server** | Stores asset records, configuration, and history; typically MySQL, PostgreSQL, or MSSQL |
| **Discovery Agents** | Lightweight software installed on managed endpoints to report hardware and software inventory |
| **Network Scanner** | Agentless scan using SNMP, WMI, or SSH to discover network-connected devices |
| **Web Interface** | Browser-based portal for asset managers, users, and approvers |
| **API Layer** | RESTful API enabling integration with other systems (CMDB, ERP, HR) |
| **Notification Engine** | Email/SMS alerts for warranty expiry, licence renewal, approval requests |

---

## 6.0 ITAM Integration with Other Systems

| Integration | Purpose | Method |
|-------------|---------|--------|
| **CMDB** | Synchronise asset records with Configuration Items (CIs); ensure consistency between ITAM and ITSM | Bi-directional API sync |
| **Procurement System** | Auto-create asset records from approved purchase orders | API or CSV import |
| **HR System** | Auto-assign assets to new staff; trigger de-assignment on staff resignation | API integration with HR system |
| **Financial System** | Export depreciation schedules and asset write-offs to the accounting system | Scheduled export (CSV, API) |
| **Active Directory / LDAP** | Import user accounts for asset assignment; enforce SSO login | LDAP connector |
| **Service Desk** | Link repair tickets and service requests to asset records | Native integration or API |

---

## 7.0 ITAM System Implementation Process

| Phase | Activities | Duration (Typical) |
|-------|-----------|-------------------|
| **1. Planning** | Define scope, requirements, and success criteria; form implementation team | 2–4 weeks |
| **2. Procurement** | Obtain vendor quotation; seek approval; issue purchase order | 2–6 weeks |
| **3. Infrastructure Setup** | Provision server (on-premises or cloud); install application and database | 1–2 weeks |
| **4. Configuration** | Configure custom fields, workflows, roles, and notifications | 2–4 weeks |
| **5. Data Migration** | Import existing asset register; clean and validate data | 2–4 weeks |
| **6. Integration** | Connect to CMDB, HR, procurement, and financial systems | 2–6 weeks |
| **7. User Acceptance Testing (UAT)** | Test all workflows and reports with key users | 2–3 weeks |
| **8. Training** | Train IT administrators, asset managers, and end users | 1–2 weeks |
| **9. Go-Live** | Decommission legacy systems; switch to new ITAM platform | 1 week |
| **10. Post-Implementation Review** | Verify data accuracy, resolve issues, optimise configurations | 4 weeks |

---

## 8.0 Common Errors in ITAM System Selection and Implementation

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Selecting on price alone | Platform lacks key features; replacement required within 2–3 years | Use weighted scoring matrix against requirements |
| Skipping the PoC | Unknown issues discovered post-purchase | Always conduct a PoC with real data |
| No data cleansing before migration | Dirty data from old system imported into new system | Validate and clean asset register before migration |
| Insufficient user training | Low adoption; ITAM platform used incorrectly | Include training budget in implementation plan |
| No post-implementation review | Configuration issues linger; adoption stays low | Schedule 30-day and 90-day post-go-live reviews |
| ITAM and CMDB not synchronised | Conflicting records cause confusion and audit failures | Configure bi-directional sync with reconciliation rules |

---

## Rujukan / References

- NOSS IT-020-5:2013 Computer Systems Management — CoCu 2
- ISO/IEC 19770-1:2017 — IT Asset Management Systems — Requirements
- ISO/IEC 19770-2:2015 — Software Identification Tag (SWID)
- ITIL 4 — Service Asset and Configuration Management
- Snipe-IT Documentation: https://snipe-it.io/docs/
- GLPI Documentation: https://glpi-project.org/
- ManageEngine AssetExplorer: https://www.manageengine.com/products/asset-explorer/