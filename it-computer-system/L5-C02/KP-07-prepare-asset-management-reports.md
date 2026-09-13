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
| NO. KOD | IT-020-5:2013-C02/KP(7/7) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-07-prepare-asset-management-reports

**TUJUAN:** Kertas rujukan untuk KP-07-prepare-asset-management-reports.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Identify the types of asset management reports required for operational, financial, and compliance purposes
2. Describe the data sources and methods used to compile asset reports
3. Structure a comprehensive asset management report appropriate for management review
4. Interpret key ITAM metrics and KPIs and present findings with recommendations
5. Prepare a disposal report, licence compliance report, and annual asset audit report
6. Apply data visualisation techniques appropriate for asset reporting

---

## 1.0 Purpose of Asset Management Reporting

Asset management reporting transforms raw asset register data into actionable information for management decision-making. Reports serve three primary audiences:

| Audience | Information Need |
|---------|----------------|
| **Senior Management / Board** | Strategic overview: total asset value, asset age profile, replacement budget forecast, compliance status |
| **IT Management** | Operational detail: asset status distribution, repair turnaround times, licence utilisation, disposal pipeline |
| **Finance / Audit** | Financial detail: depreciation schedules, asset write-offs, disposal proceeds, TCO analysis, compliance with accounting standards |

At Level 5, the asset manager is responsible for designing the reporting framework, compiling data from multiple sources, and presenting findings with evidence-based recommendations.

---

## 2.0 Types of Asset Management Reports

### 2.1 Operational Reports (Recurring)

| Report | Frequency | Key Content |
|--------|-----------|------------|
| Asset Status Summary | Monthly | Distribution of assets by status (Active, Idle, In Repair, Pending Disposal) per department |
| Repair Tracking Report | Monthly | Open repair tickets; asset in repair > SLA threshold; repair cost YTD |
| New Asset Deployment Report | Monthly | Assets received and deployed in the month; pending deployment |
| Asset Movement Report | Monthly | Assets relocated; user reassignments; custody changes |
| Warranty Expiry Report | Quarterly | Assets with warranty expiring in next 30/60/90 days |

### 2.2 Financial Reports (Recurring)

| Report | Frequency | Key Content |
|--------|-----------|------------|
| Depreciation Schedule | Annually (or as required) | Asset-by-asset depreciation charge for the financial year; accumulated depreciation; net book value |
| Asset Valuation Report | Annually | Total gross asset value; accumulated depreciation; net book value by asset category |
| Asset Write-Off Report | As required | Assets written off (fully depreciated or damaged); value removed from books |
| Disposal Proceeds Report | As required | Revenue from asset disposals; comparison with book value; gain or loss on disposal |
| Capital Expenditure vs Budget | Quarterly | Actual asset procurement spend vs approved capital budget |

### 2.3 Compliance Reports

| Report | Frequency | Key Content |
|--------|-----------|------------|
| Software Licence Compliance Report | Quarterly | Licences purchased vs deployed; over-deployment risk; under-utilisation opportunities |
| Asset Audit Report | Annually | Physical audit findings; reconciliation with asset register; ghost and phantom asset count; corrective actions |
| E-Waste Disposal Report | Annually | Assets disposed via e-waste channels; contractor licence numbers; consignment note references |
| Data Destruction Certificate Register | As required | Summary of all data destruction events; certificate references |
| PDPA Compliance Report | Annually | Confirmation that all disposed media containing personal data was securely sanitised |

---

## 3.0 Data Sources for Asset Reports

| Data Source | Information Provided |
|------------|---------------------|
| ITAM system (Snipe-IT, GLPI, ManageEngine) | Asset register data: status, location, assignment, purchase date, cost |
| Financial system (accounting software) | Purchase orders, invoices, depreciation records, disposal proceeds |
| Procurement records | PO numbers, vendor invoices, delivery orders |
| Service desk / helpdesk system | Repair tickets, repair costs, downtime records |
| Automated discovery tool | Network-detected devices; software installed; hardware specifications |
| Physical audit forms | Verified asset locations, conditions, and tag status |
| Vendor portals | Warranty status, software licence portal (e.g. Microsoft Volume Licensing Centre) |
| Consignment notes | E-waste disposal records from DOE-licensed contractors |

---

## 4.0 Structure of an Annual Asset Management Report

The Annual Asset Management Report is the primary governance document for ITAM. It consolidates all asset-related data for the financial year and provides management with a complete picture of the organisation's IT asset portfolio.

### 4.1 Report Structure

| Section | Content |
|---------|---------|
| **1. Executive Summary** | One-page overview: total assets, total value, key findings, significant changes, recommendations |
| **2. Asset Portfolio Overview** | Total asset count by category; total gross and net book value; asset age distribution chart |
| **3. Asset Status Analysis** | Status distribution (Active, Idle, In Repair, End of Life, Disposed); trend vs prior year |
| **4. New Assets and Deployments** | Assets acquired in the year; total procurement cost vs budget; deployment completion rate |
| **5. Maintenance and Repair Summary** | Total repair events; average repair cost; assets repaired vs written off; top recurring faults |
| **6. Depreciation and Valuation** | Depreciation schedule summary; net book value movement; write-offs in the year |
| **7. Asset Disposal Report** | Assets disposed; disposal method; proceeds received; data destruction confirmation |
| **8. Software Licence Compliance** | Licence compliance summary by product; over/under-deployment status; actions taken |
| **9. Physical Audit Results** | Audit coverage; reconciliation results; ghost and phantom asset resolution; tag compliance rate |
| **10. Recommendations** | Replacement priorities; budget requirements; policy improvements; system enhancements |
| **11. Appendices** | Full asset register extract; depreciation schedules; disposal certificates; audit working papers |

---

## 5.0 Key Performance Indicators (KPIs) for ITAM

KPIs enable management to assess the effectiveness of the asset management function over time.

| KPI | Formula | Target |
|-----|---------|--------|
| Asset Register Accuracy | (Assets verified / Total assets in register) × 100% | ≥ 97% |
| Tag Compliance Rate | (Assets with valid tag / Total assets) × 100% | ≥ 99% |
| Active Asset Utilisation | (Active assets / Total non-disposed assets) × 100% | ≥ 85% |
| Idle Asset Rate | (Idle assets / Total non-disposed assets) × 100% | ≤ 10% |
| Mean Time to Repair (MTTR) | Total repair time (days) / Number of repairs | ≤ 5 business days |
| Disposal Cycle Time | Average days from disposal trigger to completed disposal | ≤ 30 days |
| Licence Compliance Rate | (Licences in use / Licences purchased) × 100% | 90–100% (no over-deployment) |
| Warranty Coverage Rate | (Assets within warranty / Total active assets) × 100% | ≥ 60% |
| Replacement Budget Accuracy | (Actual replacement spend / Budgeted amount) × 100% | 90–110% |

---

## 6.0 Presenting Asset Reports to Management

### 6.1 Data Visualisation Techniques

| Chart Type | Best Used For |
|-----------|--------------|
| Pie chart / Donut chart | Asset distribution by category or by status (proportion view) |
| Bar chart (grouped or stacked) | Comparison across departments or time periods |
| Line chart | Trend analysis over time (e.g. idle asset rate, monthly repair count) |
| Heat map | Asset age or risk distribution across departments |
| Table with conditional formatting | Licence compliance by product; highlight over-deployment in red |
| Gantt chart | Disposal project timeline; replacement programme schedule |

### 6.2 Executive Summary Writing Guidelines

The executive summary must be:
- **Self-contained:** A reader who reads only this section must understand the asset portfolio position
- **Action-oriented:** Each key finding must be followed by a recommendation
- **Quantified:** Use numbers, percentages, and trends — avoid vague language
- **Concise:** Maximum one page (A4); bullet points or numbered list preferred

**Template for executive summary finding:**

```
Finding: [Specific observation with metric]
Impact: [Consequence if not addressed]
Recommendation: [Specific action required, by whom, by when]
```

---

## 7.0 Licence Compliance Report

The software licence compliance report is a critical compliance document that demonstrates the organisation is legally licensed for all deployed software.

### 7.1 Licence Compliance Report Structure

| Column | Content |
|--------|---------|
| Software Product | Name and version |
| Publisher | Software vendor |
| Licence Type | Perpetual / Subscription / Concurrent / OEM |
| Licences Purchased | Number of licences owned |
| Licences Deployed | Number of active installations (from discovery scan) |
| Variance | Deployed − Purchased (positive = over-deployed = non-compliant) |
| Compliance Status | Compliant / At Risk / Non-Compliant |
| Action Required | Procure additional licences / Uninstall / Review |

### 7.2 Software Audit Readiness

When a software publisher (e.g. Microsoft, Adobe, Oracle) conducts a licence audit, the organisation must produce:
- Proof of purchase (licence agreement, purchase order, invoice)
- Deployment evidence (installation scan report from ITAM or SCCM)
- Reconciliation showing compliance or a remediation plan if non-compliant

---

## 8.0 Common Errors in Asset Reporting

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Reporting without data validation | Inaccurate figures presented to management; loss of credibility | Validate source data against physical audit before compiling report |
| No trend analysis | Management cannot see whether the situation is improving or deteriorating | Always include comparative data (current period vs prior period) |
| Missing recommendations | Report informs but does not guide action | Every finding must be paired with a specific, actionable recommendation |
| Inconsistent definitions across reports | KPIs change meaning between periods; comparison invalid | Define all KPIs in the report glossary; apply definitions consistently |
| Licence compliance data from manual count | Manual count is unreliable; misses shadow IT | Use automated discovery data for deployment count; never rely on self-reporting |

---

## Rujukan / References

- NOSS IT-020-5:2013 Computer Systems Management — CoCu 2
- ISO/IEC 19770-1:2017 — IT Asset Management Systems
- ITIL 4 — Continual Improvement and Service Reporting
- Malaysian Financial Reporting Standard (MFRS) 116 — Property, Plant and Equipment
- Microsoft Licence Compliance and SAM: https://www.microsoft.com/en-us/licensing/
- Jabatan Akauntan Negara Malaysia (JANM) — Government Asset Reporting Guidelines
- Pekeliling Perbendaharaan Malaysia — Penyata Aset Alih Kerajaan