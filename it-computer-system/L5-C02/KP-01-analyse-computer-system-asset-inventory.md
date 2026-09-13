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
| NO. KOD | IT-020-5:2013-C02/KP(1/7) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-01-analyse-computer-system-asset-inventory

**TUJUAN:** Kertas rujukan untuk KP-01-analyse-computer-system-asset-inventory.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Define IT Asset Management (ITAM) and explain its role in organisational governance
2. Identify categories of computer system assets within an enterprise environment
3. Describe the components and purpose of an IT asset inventory register
4. Apply systematic methods to conduct a physical and logical asset inventory
5. Distinguish between hardware assets, software assets, and digital licences in an inventory context
6. Explain the relationship between asset inventory and the Configuration Management Database (CMDB)

---

## 1.0 Introduction to IT Asset Management (ITAM)

IT Asset Management (ITAM) is a business discipline that combines financial, contractual, and inventory functions to support the full lifecycle management of IT assets. At Level 5, the asset manager is responsible not merely for recording assets but for ensuring that the asset inventory is accurate, current, and strategically aligned to organisational needs.

**Key definitions:**

| Term | Definition |
|------|-----------|
| IT Asset | Any item of technology — hardware, software, licence, or digital service — that has quantifiable value and supports organisational operations |
| Asset Inventory | A structured register of all IT assets, their attributes, location, status, and assigned owner |
| ITAM | The discipline of tracking, governing, and optimising IT assets throughout their lifecycle |
| CMDB (Configuration Management Database) | A repository that stores information about all IT configuration items (CIs) and their relationships; the authoritative source of truth for the IT environment |
| Asset Lifecycle | The stages an asset passes through: Procurement → Deployment → Operation → Maintenance → Retirement/Disposal |

---

## 2.0 Categories of Computer System Assets

An enterprise IT asset inventory classifies assets into distinct categories to support financial reporting, licence compliance, and operational management.

| Category | Sub-category | Examples |
|----------|-------------|---------|
| Hardware | End-user devices | Desktop PCs, laptops, tablets, thin clients |
| Hardware | Servers and infrastructure | Rack servers, blade servers, NAS, SAN |
| Hardware | Network equipment | Switches, routers, firewalls, access points |
| Hardware | Peripherals | Monitors, printers, scanners, UPS units |
| Software | Operating systems | Windows Server, Ubuntu, macOS |
| Software | Productivity applications | Microsoft 365, LibreOffice |
| Software | Enterprise systems | ERP, CRM, CMMS platforms |
| Licences | Perpetual licences | One-time purchase, tied to hardware (OEM) or organisation (retail) |
| Licences | Subscription licences | Annual or monthly — Microsoft 365, Adobe Creative Cloud |
| Licences | Concurrent licences | Shared pool — used by a defined number of users simultaneously |
| Digital services | Cloud subscriptions | AWS, Azure, Google Workspace tenancies |

---

## 3.0 The Asset Inventory Register

The asset inventory register is the primary operational document of ITAM. Every asset must have a unique identifier and a complete record of its attributes.

### 3.1 Mandatory Fields in an Asset Record

| Field | Description | Example |
|-------|-------------|---------|
| Asset ID / Tag Number | Unique identifier, typically bar-coded or QR-coded | AST-2024-00347 |
| Asset Category | Hardware / Software / Licence / Service | Hardware |
| Asset Type | More specific classification | Desktop PC |
| Manufacturer | Brand of the asset | Dell |
| Model | Product model name/number | OptiPlex 7010 |
| Serial Number | Manufacturer's unique serial | 7G4J9X3 |
| Purchase Date | Date of procurement | 15 March 2023 |
| Purchase Cost (RM) | Acquisition cost | RM 3,200 |
| Assigned Department | Organisational unit | Finance Division |
| Assigned User | Name and staff ID of primary user | Ahmad bin Kamal (S-0421) |
| Physical Location | Building, floor, room | Block A, Level 3, Finance Wing |
| Operational Status | Current functional state | Active / In Repair / Idle / Retired |
| Warranty Expiry | End of manufacturer or extended warranty | 14 March 2026 |
| Next Maintenance Date | Scheduled preventive maintenance date | 1 September 2025 |
| Disposal Date | Date of authorised disposal (if applicable) | — |
| Remarks | Additional notes | Pending RAM upgrade |

### 3.2 Optional but Recommended Fields

- MAC address (for network-connected hardware)
- IP address (static assignment)
- Operating system version and licence key
- Depreciation rate and current book value
- Linked software licences

---

## 4.0 Methods of Conducting an Asset Inventory

A reliable asset inventory requires a combination of physical verification and automated discovery tools.

### 4.1 Physical Inventory (Manual)

Physical inventory involves a trained team walking the premises and physically locating, examining, and recording each asset.

**Procedure:**

| Step | Action |
|------|--------|
| 1 | Obtain the existing asset register (if any) as a baseline |
| 2 | Divide the facility into zones (by floor, department, or room) |
| 3 | Assign inventory teams with barcode/QR scanners or printed checklists |
| 4 | Physically locate each asset; verify tag number, serial number, and model |
| 5 | Record discrepancies: assets found but not in register (ghost assets); assets in register but not found (phantom assets) |
| 6 | Update the register with actual findings |
| 7 | Reconcile discrepancies and escalate unresolved issues to the asset manager |

### 4.2 Automated Discovery (Logical Inventory)

Automated tools scan the network and collect asset data without manual intervention.

| Tool Type | Function | Examples |
|-----------|----------|---------|
| Network Discovery Tools | Scan IP ranges; detect connected devices by MAC and IP | Advanced IP Scanner, Angry IP Scanner |
| ITAM Software | Comprehensive asset tracking with auto-discovery agents | GLPI, Snipe-IT, ManageEngine AssetExplorer |
| SCCM / Endpoint Manager | Microsoft tool for enterprise device inventory and software deployment | Microsoft SCCM, Microsoft Intune |
| SNMP Polling | Queries network devices for hardware and software information | PRTG, Nagios |

### 4.3 Reconciliation

After combining physical and logical inventory results, the asset manager reconciles:

- **Ghost assets:** Physical assets not in the system → Add to register; investigate procurement history
- **Phantom assets:** Assets in system not physically found → Investigate; may be stolen, lost, or disposed without authorisation
- **Mismatched attributes:** Serial number or location differs between physical and system records → Correct the register; document the discrepancy

---

## 5.0 Relationship Between Asset Inventory and CMDB

The asset inventory and CMDB serve complementary but distinct purposes:

| Dimension | Asset Inventory | CMDB |
|-----------|----------------|------|
| Primary focus | Financial and physical tracking | Configuration and relationships |
| Records | Assets with financial value | Configuration Items (CIs) — any component that affects service delivery |
| Attributes tracked | Cost, location, owner, status, warranty | CI relationships, service dependencies, change history |
| Governance | Finance and procurement teams | IT operations and service management teams |
| Standards | ITAM best practices, GAAP/MFRS for depreciation | ITIL Configuration Management |

At Level 5, the asset manager must ensure that hardware assets in the inventory are synchronised with CIs in the CMDB, particularly for servers, network equipment, and shared infrastructure.

---

## 6.0 Inventory Audit and Compliance

A periodic asset inventory audit verifies the accuracy of the register and demonstrates compliance with:

- **Organisational policy:** Internal IT governance and asset management policy
- **Financial regulations:** Malaysian Financial Reporting Standards (MFRS 116) — property, plant and equipment; MFRS 138 — intangible assets
- **Licence compliance:** Software licence audits (e.g. Microsoft SAM audit readiness)
- **Government procurement regulations:** Arahan Perbendaharaan (Treasury Instructions) for public sector organisations

**Audit frequency:**
- Full physical audit: annually
- Spot-check audits: quarterly
- Automated logical audit: continuous (via ITAM software)

---

## 7.0 Common Errors in Asset Inventory Management

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Incomplete asset tagging | Assets cannot be tracked or located | Tag every asset at point of receipt, before deployment |
| Outdated register | Register does not reflect actual environment | Update register on every move, change, or disposal |
| No reconciliation process | Ghost and phantom assets accumulate undetected | Conduct quarterly spot checks; run automated scans monthly |
| Manual data entry errors | Incorrect serial numbers or costs lead to audit failures | Use barcode/QR scanners; validate against purchase orders |
| Siloed asset data | Finance, IT, and procurement use different records | Implement a single ITAM platform as the system of record |
| Ignoring software assets | Licence over-use leads to compliance penalties | Include software and licence assets in every inventory cycle |

---

## Rujukan / References

- NOSS IT-020-5:2013 Computer Systems Management — CoCu 2: Computer System Asset Management
- ISO/IEC 19770-1:2017 — IT Asset Management Systems — Requirements
- ITIL 4 Foundation — Service Asset and Configuration Management
- Malaysian Financial Reporting Standard (MFRS) 116 — Property, Plant and Equipment
- Jabatan Perbendaharaan Malaysia — Arahan Perbendaharaan (Treasury Instructions)
- Snipe-IT Documentation — Open Source Asset Management: https://snipe-it.io/docs/