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
| NO. KOD | IT-020-5:2013-C02/KP(2/7) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-02-define-operational-status-of-assets

**TUJUAN:** Kertas rujukan untuk KP-02-define-operational-status-of-assets.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Define the standard operational status categories applied to IT assets
2. Explain the criteria used to classify an asset's operational status
3. Describe the process of conducting an operational status assessment
4. Identify the impact of operational status on depreciation, maintenance scheduling, and disposal decisions
5. Apply status classification to a sample asset population and update the asset register accordingly

---

## 1.0 Introduction to Operational Status Classification

Operational status (also called asset condition status) is a formal classification that describes the current functional state of an IT asset. Accurate status classification is essential for:

- Financial reporting: only active and in-use assets are depreciated at full rate
- Maintenance planning: only operational assets require scheduled preventive maintenance
- Capacity planning: idle and excess assets can be redeployed before new procurement is approved
- Disposal decisions: end-of-life assets trigger the disposal workflow
- Audit compliance: regulators and auditors verify that status classifications are consistent and evidence-based

---

## 2.0 Standard Operational Status Categories

The following status categories are aligned with Malaysian public sector asset management guidelines (Pekeliling Perbendaharaan) and international ITAM best practices:

| Status | Malay Term | Description |
|--------|-----------|-------------|
| **Active / In Use** | Aktif / Sedang Digunakan | Asset is deployed, assigned to a user or service, and functioning within normal parameters |
| **Idle / Unassigned** | Terbiar / Tidak Ditugaskan | Asset is functional but not currently assigned; held in stock or awaiting redeployment |
| **In Repair / Under Maintenance** | Dalam Baik Pulih | Asset has a fault and is undergoing repair, either in-house or by an external vendor |
| **Reserved** | Ditempah | Asset is functional and earmarked for a specific upcoming deployment or project |
| **End of Life / Obsolete** | Hujung Hayat / Usang | Asset is no longer fit for its intended purpose due to age, performance degradation, or vendor end-of-support |
| **Pending Disposal** | Menunggu Pelupusan | Asset has been approved for disposal but the disposal process has not yet been completed |
| **Disposed** | Dilupuskan | Asset has been formally removed from service through an authorised disposal process |
| **Lost / Stolen** | Hilang / Dicuri | Asset cannot be located; police report or internal incident report filed |
| **Damaged / Uneconomical to Repair** | Rosak / Tidak Ekonomi Dibaiki | Asset has sustained damage where the cost of repair exceeds the asset's remaining value |

---

## 3.0 Criteria for Status Classification

Classifying an asset's status requires evidence-based assessment against defined criteria:

### 3.1 Active / In Use

- Asset is physically present at the assigned location
- Asset powers on and completes POST (Power-On Self-Test) without errors
- Asset is assigned to a named user or a shared service with a defined owner
- Asset appears in automated discovery scans within the past 30 days

### 3.2 Idle / Unassigned

- Asset is physically present in the IT store or a secure holding area
- Asset is functional (passes basic power-on test)
- No user assignment exists in the asset register
- Asset has been unassigned for more than 14 consecutive days

### 3.3 In Repair

- A fault report (Laporan Kerosakan / Service Request) has been raised
- Asset has been handed over to the repair team or external service centre
- A repair tracking reference number is recorded in the asset register
- Estimated return date is documented

### 3.4 End of Life / Obsolete

Criteria requiring at least two of the following:

| Criterion | Threshold |
|-----------|----------|
| Age | Hardware: ≥ 5 years from purchase date; servers: ≥ 7 years |
| Manufacturer support | Vendor end-of-support or end-of-life date has passed |
| Performance | Asset cannot run the current standard operating environment (SOE) or required applications |
| Repair cost | Cost of repair exceeds 50% of current replacement value |
| Software compatibility | Operating system or critical application no longer supports the hardware |

### 3.5 Pending Disposal

- End-of-life or uneconomical-to-repair status confirmed by the asset manager
- Disposal approval obtained from the authorising committee (e.g. Lembaga Pelupusan Aset)
- Asset physically segregated in the disposal holding area
- Disposal method selected (auction, destruction, donation, recycling)

---

## 4.0 Operational Status Assessment Process

The status assessment is conducted as part of the annual inventory cycle and whenever a significant event occurs (relocation, fault, return from repair).

| Step | Action | Responsible Party |
|------|--------|------------------|
| 1 | Extract the asset register for the target department or asset category | Asset Manager |
| 2 | Conduct physical inspection: locate each asset, power it on, verify tag number | Inventory Team |
| 3 | Run automated discovery scan to capture network-connected assets | IT Administrator |
| 4 | Cross-reference physical findings with automated data | Asset Manager |
| 5 | Classify each asset against the status criteria in Section 3 | Asset Manager |
| 6 | Record the assessed status in the asset register with date and assessor name | Asset Manager |
| 7 | Flag discrepancies (status differs from previous record) for investigation | Asset Manager |
| 8 | Generate status summary report for management review | Asset Manager |

---

## 5.0 Impact of Operational Status on Asset Management Decisions

| Decision Area | How Status Affects the Decision |
|--------------|--------------------------------|
| **Depreciation** | Active assets are depreciated at the standard rate. Idle assets continue to depreciate. Assets classified as uneconomical to repair may be written off immediately. |
| **Maintenance scheduling** | Only Active and Idle assets are included in preventive maintenance schedules. Assets In Repair are tracked separately. End-of-Life assets are excluded. |
| **Procurement justification** | Idle assets must be checked before new procurement is approved. A high idle count indicates poor capacity management. |
| **Redeployment** | Idle assets in good condition are redeployed to meet new requirements before purchase is considered. |
| **Disposal** | End-of-Life and Damaged/Uneconomical assets trigger the disposal workflow. Disposed status closes the asset lifecycle record. |
| **Insurance** | Active and Idle assets must be listed in the organisation's IT asset insurance schedule. |
| **Audit** | Auditors verify that the declared status matches physical evidence and financial records. Mismatches are audit findings. |

---

## 6.0 Status Transition Workflow

Assets move between statuses in a controlled manner. Each transition must be documented in the asset register with date, reason, and approver.

```
Procurement
    ↓
[Active / In Use]
    ↓           ↘
[Idle]      [In Repair]
    ↓           ↓
[Reserved]  [Active] (if repaired)
    ↓       ↓
[End of Life / Obsolete]
    ↓
[Pending Disposal]
    ↓
[Disposed]
```

Special transitions:
- Any status → **Lost/Stolen**: Triggered by a missing asset report; requires incident report and police report
- **In Repair** → **Damaged/Uneconomical to Repair**: Triggered by repair quotation exceeding the threshold
- **Damaged** → **Pending Disposal**: Requires management approval

---

## 7.0 Documenting Status in the Asset Register

Each status change entry in the asset register must include:

| Field | Example |
|-------|---------|
| Previous Status | Active |
| New Status | In Repair |
| Date of Change | 10 June 2025 |
| Reason | Hard disk failure; CrystalDiskInfo shows reallocated sector count critical |
| Fault Reference No. | FR-2025-00112 |
| Authorised By | Encik Razif bin Othman (IT Manager) |
| Remarks | Sent to Dell Service Centre; estimated return 20 June 2025 |

---

## 8.0 Common Errors in Operational Status Management

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Not updating status after repair | Asset recorded as "In Repair" but already redeployed | Enforce status update as part of asset return checklist |
| Classifying old assets as "Active" without assessment | Inflated active asset count; incorrect depreciation | Apply age and performance criteria annually |
| No evidence recorded for status change | Audit finding; status disputed | Require authorised signature and reference number for every change |
| Idle assets not identified for redeployment | Unnecessary new procurement | Run idle asset report monthly; escalate to procurement committee |
| Missing Lost/Stolen reports | Asset not removed from insurance or register | Mandate incident report within 24 hours of discovery |

---

## Rujukan / References

- NOSS IT-020-5:2013 Computer Systems Management — CoCu 2
- Pekeliling Perbendaharaan Malaysia — Tatacara Pengurusan Aset Alih Kerajaan
- ISO/IEC 19770-1:2017 — IT Asset Management Systems
- ITIL 4 — Asset and Configuration Management Practice
- Malaysian Financial Reporting Standard (MFRS) 136 — Impairment of Assets