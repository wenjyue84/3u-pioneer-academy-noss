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
| NO. KOD | IT-020-4:2013-C04/KP(1/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-01-cabling-layout-planning-and-standards

**TUJUAN:** Kertas rujukan untuk KP-01-cabling-layout-planning-and-standards.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the principal structured cabling standards (TIA/EIA-568, ISO/IEC 11801) and their application in network design
2. Describe the components of a structured cabling system and their roles
3. Select appropriate cable categories (Cat5e, Cat6, Cat6A, fibre) based on application requirements
4. Produce a cabling layout plan that includes topology, cable runs, pathways, and telecommunications rooms
5. Apply TIA-606 labelling conventions to a planned installation

---

## 1.0 Introduction to Structured Cabling

Structured cabling (kabel berstruktur) is a standardised approach to building telecommunication infrastructure using a set of cabling and connectivity products that integrate voice, data, video, and building management systems. A well-planned structured cabling system supports current and future network requirements, simplifies moves, adds, and changes (MACs), and reduces downtime caused by cabling faults.

The primary reference standard in Malaysia and internationally is **ANSI/TIA-568** (published by the Telecommunications Industry Association) which defines:
- Recognised cable types and their performance categories
- Topology and maximum distances for horizontal and backbone cabling
- Connector types and termination requirements
- Testing parameters and limits

**ISO/IEC 11801** is the international equivalent and is fully harmonised with TIA-568 at Category 6A and above.

---

## 2.0 Structured Cabling System Components

A structured cabling system consists of six subsystems:

| Subsystem | Malay Term | Description |
|-----------|------------|-------------|
| Entrance Facility (EF) | Kemudahan Masukan | The point where external cabling (from ISP or other buildings) enters the building |
| Equipment Room (ER) | Bilik Peralatan | Houses major equipment such as core switches, servers, and PBX |
| Backbone Cabling | Kabel Tulang Belakang | Interconnects the ER, TRs, and EF; typically fibre optic or high-category copper |
| Telecommunications Room (TR) | Bilik Telekomunikasi | Floor-level distribution point; houses patch panels, distribution switches |
| Horizontal Cabling | Kabel Mendatar | Runs from the TR to the work area outlet; maximum 90 m permanent link |
| Work Area (WA) | Kawasan Kerja | End-user space; includes wall outlets, patch cords, and end devices |

---

## 3.0 Cable Categories and Selection

### 3.1 Copper Twisted-Pair Categories

| Category | Standard | Bandwidth | Max Speed (100 m) | Typical Application |
|----------|----------|-----------|-------------------|---------------------|
| Cat5e | TIA-568-C.2 | 100 MHz | 1 Gbps (1000BASE-T) | Legacy LAN, VoIP |
| Cat6 | TIA-568-C.2 | 250 MHz | 10 Gbps up to 55 m | Standard office LAN |
| Cat6A | TIA-568-C.2 | 500 MHz | 10 Gbps at 100 m | High-density, data centre edge |
| Cat8 | TIA-568-C.2-1 | 2000 MHz | 40 Gbps up to 30 m | Data centre top-of-rack |

> **Note:** For new installations, Cat6A is the minimum recommended standard for horizontal cabling. Cat6 is acceptable for low-density office environments where 10GBASE-T at full 100 m is not required.

### 3.2 Fibre Optic Cable Types

| Type | Core/Cladding | Bandwidth | Typical Application |
|------|---------------|-----------|---------------------|
| OM3 Multimode | 50/125 µm | 2000 MHz·km | Short backbone ≤ 300 m (10G) |
| OM4 Multimode | 50/125 µm | 4700 MHz·km | Backbone ≤ 550 m (10G) |
| OS2 Single-mode | 9/125 µm | Unlimited (distance-limited by loss) | Campus/inter-building backbone |

### 3.3 Selection Criteria

When selecting cable type, consider:
- **Application bandwidth** — current and projected traffic demands
- **Distance** — copper horizontal cabling must not exceed 90 m permanent link + 10 m patch cords (total channel ≤ 100 m)
- **Environment** — plenum (CMP) rated cable for air-handling spaces; riser (CMR) for vertical shafts; outdoor-rated for exposed runs
- **Future-proofing** — Cat6A supports 10 Gbps at full horizontal distance and is preferred for new builds

---

## 4.0 Cabling Layout Planning Process

### 4.1 Site Survey

Before producing a layout plan, a thorough site survey must be completed:

1. Obtain building floor plans (architectural drawings)
2. Identify all work area locations and user counts per floor
3. Locate existing conduit runs, cable trays, and pathways
4. Determine telecommunications room (TR) locations (one TR per floor, max 90 m from furthest outlet)
5. Identify backbone pathway between TR and equipment room (ER)
6. Note obstacles: concrete beams, fire breaks, mechanical services, restricted access zones

### 4.2 Topology Design

Standard horizontal topology is a **star topology**: every outlet runs a dedicated cable from the TR. No daisy-chaining or branching of horizontal cabling is permitted.

Backbone topology may be **hierarchical star**: ER → TR (floor distributors) using fibre for long distances.

### 4.3 Cable Count Calculation

| Parameter | Value |
|-----------|-------|
| Outlets per work area | Minimum 2 (TIA-568 recommendation) |
| Add 10–15% spare capacity | For future growth |
| Cable length per run | Measured along the actual path (not straight-line distance) + 3 m slack at each end |

**Example calculation:**
- 20 workstations × 2 outlets = 40 outlets
- Add 15% spare = 46 outlets (round up to 48 for panel organisation)
- Average cable run = 45 m + 6 m slack = 51 m per cable
- Total cable = 48 × 51 m = 2,448 m → order 2,600 m (6% overage for waste)

### 4.4 Telecommunications Room (TR) Layout

Each TR should contain:
- **Patch panel** — 24-port or 48-port, 1U or 2U, rack-mounted
- **Distribution switch** — port count matched to outlet count + uplinks
- **Horizontal cable management** — 1U or 2U rings above and below each patch panel row
- **Grounding/bonding bar** — bonded to building ground per TIA-607
- **Power distribution unit (PDU)**
- **Cable entry through fireproofed openings**

Minimum TR room dimensions: 3 m × 2.4 m (TIA-569 guideline); temperature 18–27°C, humidity 30–55% RH.

---

## 5.0 TIA-606 Labelling Standard

TIA-606-B defines an administration system for telecommunications infrastructure. Every cable, outlet, patch panel port, and pathway must be uniquely identified.

### 5.1 Label Format Conventions

| Element | Label Format Example | Description |
|---------|----------------------|-------------|
| Telecommunications Room | TR-B1-01 | Building B, Floor 1, TR number 01 |
| Patch panel port | TR-B1-01-PP01-01 | TR > Patch Panel 01 > Port 01 |
| Horizontal cable | HC-B1-01-001 | Horizontal Cable, Building 1, Floor 1, Cable 001 |
| Wall outlet (faceplate) | WA-B1-F101-A | Work Area, Building 1, Room F101, Outlet A |
| Fibre backbone | BB-B1-ER-TR01-F01 | Backbone, ER to TR01, Fibre 01 |

### 5.2 Label Requirements

- Labels must be machine-printed (not handwritten) and affixed within 150 mm of each termination point
- Label material must be heat-resistant and chemical-resistant (Brady or equivalent)
- All labels recorded in the cable administration database or as-built drawing

---

## 6.0 Layout Drawing Standards

Cabling layout plans must include:

1. **Floor plan base** — to scale, showing room boundaries, doors, and dimensions
2. **Outlet symbols** — standardised symbols per TIA-606 or ISO/IEC 14763
3. **Cable run lines** — showing pathway (conduit or cable tray) with direction arrows
4. **TR location** — clearly marked with room number
5. **Cable IDs** — each run labelled with its unique identifier
6. **Legend and title block** — project name, revision, date, drawn by, approved by

Software tools used: AutoCAD, Visio, or specialist tools such as NetBrain or Ekahau (for wireless overlap planning).

---

## 7.0 Common Errors in Cabling Layout Planning

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Exceeding 90 m horizontal limit | Link fails certification test; reduced performance | Measure all paths; reposition TR if distance exceeded |
| Insufficient TR capacity | Cannot accommodate future outlets | Plan for 15–20% spare panel ports |
| Missing spare conduit | Impossible to add cables without disruption | Install at least one empty conduit per pathway |
| Not using plenum cable in air ducts | Fire code violation; safety hazard | Confirm with M&E drawings; specify CMP-rated cable |
| Labelling done after installation | Incorrect or missing labels; rework cost | Label cable at both ends before pulling |
| No as-built drawing update | Infrastructure becomes unmanageable | Update drawings within 5 working days of completion |

---

## Rujukan / References

- ANSI/TIA-568.2-D: Balanced Twisted-Pair Telecommunications Cabling and Components Standard
- ANSI/TIA-568.3-D: Optical Fiber Cabling Components Standard
- ANSI/TIA-606-B: Administration Standard for Telecommunications Infrastructure
- ANSI/TIA-569-D: Telecommunications Pathways and Spaces
- ISO/IEC 11801-1:2017 Generic Cabling for Customer Premises
- NOSS IT-020-4:2013 Computer Systems Administration — CoCu 4: Network Cabling Management