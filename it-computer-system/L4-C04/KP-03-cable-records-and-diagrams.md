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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C04 NETWORK CABLING MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. PLAN CABLING LAYOUT AND STANDARDS<br>2. MANAGE CABLE INSTALLATION AND LABELLING<br>3. MAINTAIN CABLE RECORDS AND DIAGRAMS<br>4. COORDINATE WITH FACILITIES AND CONTRACTORS<br>5. DOCUMENT CABLING CHANGES |
| NO. KOD | IT-020-4:2013-C04/KP(3/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-03-cable-records-and-diagrams

**TUJUAN:** Kertas rujukan untuk KP-03-cable-records-and-diagrams.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the purpose and content of cable records (rekod kabel) in a structured cabling system
2. Produce and maintain as-built drawings that accurately reflect the installed infrastructure
3. Use a cable administration system (database or spreadsheet) to record and retrieve cable information
4. Conduct periodic audits of cable records against the physical installation
5. Describe the requirements for record retention and version control

---

## 1.0 Importance of Cable Records

Cable records are the documentary backbone of any network cabling system. Without accurate records, the following problems arise:

- Technicians cannot identify which cable connects a specific outlet to a specific patch panel port — troubleshooting becomes guesswork
- Moves, adds, and changes (MACs) are performed incorrectly, creating undocumented connections
- During faults, the wrong cable may be disconnected, causing unplanned outages
- Audits and compliance reviews cannot be completed

TIA-606-B mandates that a record-keeping system be established and maintained for the life of the cabling infrastructure. This is a contractual and regulatory requirement in most commercial building projects in Malaysia.

---

## 2.0 Types of Cable Records

### 2.1 Cable Schedule (Jadual Kabel)

The cable schedule is a tabular record of every cable in the installation:

| Field | Description |
|-------|-------------|
| Cable ID | Unique identifier per TIA-606-B convention (e.g. HC-B1-01-001) |
| Cable type | Cat6A UTP, OM4 fibre, etc. |
| Origin | TR room ID + patch panel port number |
| Destination | Wall outlet ID / faceplate position |
| Length (m) | Measured or calculated cable length |
| Installation date | Date the cable was pulled and terminated |
| Test result | Pass/Fail; test report reference number |
| Status | Active / Spare / Decommissioned |
| Notes | Any deviations from plan; splices; repairs |

### 2.2 Port Assignment Record (Rekod Peruntukan Port)

Documents how each patch panel port is assigned:

| Field | Description |
|-------|-------------|
| Panel ID | Identifier of the patch panel (e.g. TR-B1-01-PP01) |
| Port number | Port 01–48 |
| Cable ID | Horizontal cable terminated at this port |
| Connected to switch | Switch ID + switch port number |
| VLAN assignment | Network VLAN if applicable |
| User/device | End device or user assigned to this port |
| Last updated | Date of last change |

### 2.3 Fibre Record (Rekod Gentian)

For fibre backbone cables, additional fields are required:

| Field | Description |
|-------|-------------|
| Fibre ID | Backbone cable + individual fibre strand number |
| Fibre type | OM3, OM4, OS2 |
| Origin and destination | TR IDs or ER |
| Connector type | LC, SC, ST |
| Insertion loss (dB) | OTDR or power meter measurement |
| OTDR trace reference | File name of stored OTDR trace |
| Splice points | Location and loss of each splice |

---

## 3.0 As-Built Drawings (Lukisan Sebina Bina)

As-built drawings reflect the cabling system as it was actually installed, including any deviations from the original design. They are distinct from the design drawings (which show the intended layout).

### 3.1 Required Drawings

| Drawing Type | Content |
|-------------|---------|
| Floor plan — cabling layout | Outlet positions, cable runs, TR locations, pathway routes |
| TR elevation drawing | Rack layout: patch panels, switches, cable managers, PDUs — numbered from top to bottom |
| Backbone schematic | Inter-floor or inter-building fibre/copper backbone routes |
| Conduit/pathway schedule | Conduit sizes, fill ratios, routing descriptions |

### 3.2 Drawing Standards

- Scale: minimum 1:50 for floor plans; 1:20 for TR elevations
- All elements must use standardised symbols (TIA-606-B Annex B or ISO/IEC 14763-2)
- Title block must include: project name, drawing number, revision, date, drawn by, checked by, approved by
- Revisions must be tracked using a revision table; superseded revisions archived (not deleted)

### 3.3 Revision Control

| Version | Description |
|---------|-------------|
| Rev 0 | As-designed (pre-installation design drawing) |
| Rev A | First as-built revision after initial installation |
| Rev B, C... | Subsequent revisions after each change |

---

## 4.0 Cable Administration Systems

### 4.1 Spreadsheet-Based Records

For small installations (under 200 outlets), a spreadsheet is acceptable:
- One sheet per record type (cable schedule, port assignment, fibre record)
- Protected columns to prevent accidental editing
- Access controlled (shared read; change-controlled write)
- Version tracked with date stamp in filename (e.g. `Cable-Schedule-B1-Rev-A-20260101.xlsx`)

### 4.2 Database-Based Administration

For larger installations, dedicated cable administration software is preferred:

| Software | Features |
|----------|----------|
| Nlyte DCIM | End-to-end connectivity tracking; visual rack views |
| CommScope imVision | Physical layer intelligence; real-time port tracking |
| Sunbird DCIM | Cable management, port tracking, capacity planning |
| Custom database (MS Access/SQL) | Tailored to organisation's needs; lower cost |

Key requirements for any system:
- Unique ID for every record
- Search and filter by any field
- Audit trail (who changed what, when)
- Export to CSV or PDF for reporting

---

## 5.0 Conducting Cable Record Audits

Periodic audits verify that the cable records match the physical installation:

### 5.1 Audit Procedure

1. **Schedule the audit** — notify affected users; plan for brief service interruptions if tracing is required
2. **Select scope** — full audit (all cables) or targeted (specific TR or floor)
3. **Physical trace** — physically trace each cable from outlet to patch panel using a cable tracer/tone generator
4. **Compare with records** — verify cable ID labels match the cable schedule
5. **Test** — perform a continuity or link test on cables where records are uncertain
6. **Update records** — correct all discrepancies found; update the as-built drawing if physical layout differs
7. **Document audit** — produce an audit report: scope, date, discrepancies found and corrected, sign-off

### 5.2 Audit Frequency Recommendation

| Installation Size | Audit Frequency |
|------------------|-----------------|
| Small (< 100 outlets) | Annually |
| Medium (100–500 outlets) | Every 6 months |
| Large (> 500 outlets) | Quarterly or continuous monitoring system |

---

## 6.0 Record Retention Requirements

| Record Type | Minimum Retention Period | Format |
|-------------|--------------------------|--------|
| Cable schedule | Life of installation | Electronic + hardcopy |
| As-built drawings | Life of installation + 7 years after decommission | Electronic + hardcopy |
| Test reports (certification) | Life of installation | Electronic |
| Audit reports | 7 years | Electronic |
| Change orders | Life of installation | Electronic + hardcopy |

> **Note:** Malaysian construction contracts and MS ISO 45001 guidelines require that infrastructure records be maintained and producible on demand for regulatory inspection or insurance claims.

---

## 7.0 Common Errors in Cable Record Maintenance

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Not updating records after MACs | Records become inaccurate; future faults cannot be resolved | Require change approval form + record update before and after every MAC |
| Using handwritten labels and corrections | Illegible records; mismatch between label and database | All changes must be machine-printed and entered into the database on the same day |
| No version control on drawings | Superseded drawings used for fault-finding | Use revision table; file old revisions in archive folder |
| Storing records only locally | Records lost if computer fails | Use shared network drive or cloud storage with daily backup |
| No audit process | Undetected discrepancies accumulate | Schedule formal audits; make audit completion a KPI |

---

## Rujukan / References

- ANSI/TIA-606-B: Administration Standard for Telecommunications Infrastructure
- ANSI/TIA-568.2-D: Balanced Twisted-Pair Telecommunications Cabling and Components Standard
- ISO/IEC 14763-2: Implementation and Operation of Customer Premises Cabling — Planning and Installation
- BICSI TDMM (Telecommunications Distribution Methods Manual), 14th Edition
- NOSS IT-020-4:2013 Computer Systems Administration — CoCu 4: Network Cabling Management