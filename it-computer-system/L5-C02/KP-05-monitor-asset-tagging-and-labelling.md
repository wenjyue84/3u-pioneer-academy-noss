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
| NO. KOD | IT-020-5:2013-C02/KP(5/7) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-05-monitor-asset-tagging-and-labelling

**TUJUAN:** Kertas rujukan untuk KP-05-monitor-asset-tagging-and-labelling.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the purpose and governance principles of asset tagging and labelling
2. Describe the types of asset tags used in IT asset management
3. Define a standard asset tag format and naming convention for an organisation
4. Describe the asset tagging workflow from procurement through deployment
5. Explain how to monitor tag compliance across the asset population
6. Identify common tagging failures and the corrective actions required

---

## 1.0 Purpose of Asset Tagging and Labelling

Asset tagging is the process of physically affixing a unique identifier to every IT asset. Together with the asset register, tags form the physical link between a real-world device and its digital record. Without effective tagging:

- Physical audits cannot be conducted efficiently
- Assets cannot be located or tracked during moves or repairs
- Theft and loss go undetected
- Asset register data becomes unreliable

At Level 5, the asset manager does not merely apply tags but designs and monitors the tagging system, ensuring consistency, coverage, and auditability across all asset categories and locations.

---

## 2.0 Types of Asset Tags

| Tag Type | Description | Advantages | Limitations |
|----------|-------------|-----------|------------|
| **Barcode (1D)** | Linear barcode encoding a numeric or alphanumeric asset ID | Low cost; widely supported by scanners | Limited data capacity; must be scanned line-of-sight |
| **QR Code (2D)** | Two-dimensional matrix code; encodes more data than 1D barcode | Higher data density; scannable with smartphones | Slightly larger; can be damaged more easily |
| **RFID (Radio Frequency ID)** | Electronic tag read by radio waves; no line-of-sight required | Fast bulk scanning; readable without opening drawers/doors | Higher cost; metallic surfaces can interfere with signal |
| **NFC (Near Field Communication)** | Short-range RFID variant; readable by NFC-enabled smartphones | No dedicated scanner needed | Very short read range (< 4 cm); lower data transfer rate |
| **Tamper-evident label** | Leaves a "VOID" pattern if removed; used on high-value assets | Deters theft; indicates tampering clearly | Cannot be repositioned; single-use |
| **Engraved / etched tag** | Permanent metal or polymer plate affixed by screws or adhesive | Highly durable; cannot be removed easily | Expensive; not suitable for small devices |

**Selection guide:**
- Standard office equipment (desktops, monitors, printers): polyester barcode or QR code label with tamper-evident adhesive
- Servers and network equipment in racks: RFID tags on the front bezel for automated rack scanning
- High-value portable assets (laptops, tablets): tamper-evident QR code with NFC chip
- Assets in harsh environments (workshops, outdoor): engraved metal plate

---

## 3.0 Asset Tag Format and Naming Convention

A standardised tag format enables consistent identification across the organisation. The format must be defined in the IT Asset Management Policy and applied without exception.

### 3.1 Recommended Tag Format

```
[ORG CODE]-[ASSET TYPE CODE]-[YEAR]-[SEQUENCE NUMBER]
```

**Example:** `PRISMA-DT-2024-00347`

| Field | Description | Example |
|-------|-------------|---------|
| ORG CODE | Organisation or department abbreviation (2–6 characters) | PRISMA, JKR, UTEM |
| ASSET TYPE CODE | Two-letter code for the asset category | DT (Desktop), LT (Laptop), SV (Server), NW (Network), PR (Printer), MN (Monitor), TB (Tablet) |
| YEAR | Four-digit year of procurement | 2024 |
| SEQUENCE NUMBER | Five-digit zero-padded sequential number, unique per asset type per year | 00347 |

### 3.2 Asset Type Codes

| Code | Asset Type | Code | Asset Type |
|------|-----------|------|-----------|
| DT | Desktop PC | UPS | Uninterruptible Power Supply |
| LT | Laptop | KM | Keyboard / Mouse set |
| SV | Server | TB | Tablet / iPad |
| NW | Network equipment | PJ | Projector |
| PR | Printer / MFP | SC | Scanner |
| MN | Monitor | PH | Desk phone / IP phone |

---

## 4.0 Asset Tagging Workflow

Tags must be applied at the point of receipt — before an asset is deployed to any user or location. This ensures 100% tag coverage from day one.

| Step | Action | Responsible Party |
|------|--------|------------------|
| 1 | Asset received from vendor; delivery order (DO) verified against purchase order (PO) | Store / Receiving Officer |
| 2 | Asset unpacked; serial number and model verified | Store Officer |
| 3 | Asset ID generated in ITAM system; tag printed | Asset Manager / IT Officer |
| 4 | Tag affixed to the designated location on the asset (see Section 4.1) | IT Officer |
| 5 | Asset record created in ITAM system with tag number, serial number, model, purchase date, cost | Asset Manager |
| 6 | Tagged asset stored in IT store or deployed to user; location updated in ITAM system | IT Officer |
| 7 | User acknowledges receipt; Asset Acknowledgement Form (Borang Penerimaan Aset) signed | User and IT Officer |

### 4.1 Standard Tag Placement by Asset Type

| Asset Type | Tag Location |
|------------|-------------|
| Desktop PC (tower) | Left side panel, lower rear quadrant |
| Desktop PC (SFF/USFF) | Bottom panel |
| Laptop | Bottom panel, lower right corner |
| Monitor | Rear panel, lower right corner |
| Server (1U/2U) | Front bezel, right side |
| Network switch | Front panel, right side |
| Printer / MFP | Top panel, rear left corner |
| Tablet | Rear panel, lower right corner |
| UPS | Top panel |

**Rule:** Tag must be visible without moving the asset and must not obstruct ventilation ports, serial number labels, or regulatory compliance markings.

---

## 5.0 Monitoring Tag Compliance

At Level 5, the asset manager must operate a monitoring programme to ensure ongoing tag compliance, not merely a one-time tagging exercise.

### 5.1 Monitoring Activities

| Activity | Frequency | Method |
|----------|-----------|--------|
| New asset tagging verification | At receipt (100% of new assets) | Receiving officer checklist; ITAM system record |
| Spot-check audit | Monthly (10% of asset population) | Random selection; physical scan against ITAM register |
| Full physical audit | Annually | All assets scanned; reconciled against ITAM register |
| Post-repair tag verification | After every repair | Technician checklist; verify tag before returning asset |
| Relocation tag verification | After every location change | Move-request checklist; update location in ITAM system |

### 5.2 Tag Compliance Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| Tag Coverage Rate | (Assets with valid tag / Total assets) × 100% | ≥ 99% |
| Tag Readability Rate | (Tags successfully scanned / Total tags attempted) × 100% | ≥ 98% |
| Register Accuracy Rate | (Assets with correct ITAM record / Total assets scanned) × 100% | ≥ 97% |
| Tagging Cycle Time | Average time from asset receipt to tag affixed and record created | ≤ 1 business day |

### 5.3 Tag Non-Compliance Report

When a non-compliance is detected, it must be documented and resolved within a defined timeframe:

| Non-Compliance Type | Corrective Action | Resolution Target |
|--------------------|-------------------|------------------|
| Missing tag | Generate and affix new tag; update ITAM record | 2 business days |
| Damaged / unreadable tag | Replace tag; verify ITAM record | 2 business days |
| Tag number not in ITAM system | Investigate; create or update ITAM record | 3 business days |
| Tag affixed incorrectly (wrong location) | Reapply tag at correct location | 2 business days |
| Tamper-evident label voided | Investigate potential tampering; escalate to security if warranted | Immediate |

---

## 6.0 Asset Label Content Requirements

In addition to the machine-readable tag, assets may carry a printed label with human-readable information:

| Field | Purpose |
|-------|---------|
| Asset ID | Matches the tag number in the ITAM system |
| Organisation logo | Identifies the asset as organisational property |
| Helpdesk contact number | Enables users to report issues without knowing the asset ID |
| "PROPERTY OF [ORGANISATION]" text | Deters theft; assists police identification if recovered |
| QR code | Links to the asset's self-service record page (if the ITAM system has a user portal) |

---

## 7.0 Common Errors in Asset Tagging and Labelling

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Tagging after deployment | Assets already in use cannot be easily located for tagging; some may never be tagged | Enforce tagging as a mandatory step in the receiving process; assets cannot be deployed without a tag |
| Tag affixed over ventilation slots | Overheating; void warranty | Publish and enforce the standard placement guide |
| Duplicate tag numbers | Two assets with the same ID create register confusion | ITAM system must enforce unique tag number constraint; use sequential number generation |
| Tag applied to packaging, not asset | Asset cannot be identified once packaging is discarded | Inspector must verify tag is on the asset body before signing off |
| No tamper-evident tag on high-value assets | Tags removed and moved between assets to disguise theft | Policy must specify tamper-evident tags for assets above a defined value threshold (e.g. > RM 1,000) |
| RFID tags on metal surfaces without proper mounting | Tag signal blocked by metal; unreadable | Use RFID tags rated for metal surfaces (on-metal tags) for servers and network equipment |

---

## Rujukan / References

- NOSS IT-020-5:2013 Computer Systems Management — CoCu 2
- Pekeliling Perbendaharaan Malaysia — Tatacara Pengurusan Aset Alih Kerajaan (Pendaftaran dan Pelabelan)
- ISO/IEC 19770-1:2017 — IT Asset Management Systems
- GS1 Malaysia — Barcode and QR Code Standards: https://www.gs1my.org/
- Jabatan Akauntan Negara Malaysia (JANM) — Asset Management Guidelines