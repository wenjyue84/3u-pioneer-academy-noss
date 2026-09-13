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
| NO. KOD | IT-020-4:2013-C04/KP(2/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-02-cable-installation-and-labelling

**TUJUAN:** Kertas rujukan untuk KP-02-cable-installation-and-labelling.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Describe the correct sequence and methods for pulling and routing copper and fibre optic cables
2. Apply proper termination techniques for RJ-45 keystone jacks, patch panels, and fibre connectors
3. Implement TIA-606-B compliant labelling on cables, outlets, patch panels, and pathways
4. Identify and apply cable management hardware in telecommunications rooms and work areas
5. Specify safety precautions and quality checkpoints during cable installation

---

## 1.0 Introduction to Cable Installation Management

Cable installation management encompasses the planning, coordination, and execution of all activities required to physically install cabling infrastructure in accordance with the approved layout plan and applicable standards. A poorly managed installation results in cabling that fails certification tests, is difficult to maintain, and may violate building or fire codes.

The network cabling administrator at Level 4 is responsible for supervising installation teams, enforcing standards compliance, conducting quality checks at each stage, and maintaining complete documentation of the installed infrastructure.

---

## 2.0 Pre-Installation Preparation

Before cables are pulled, the following preparations must be completed:

| Preparation Activity | Detail |
|---------------------|--------|
| Verify layout plan approval | Confirm the as-planned drawings are signed off by the project manager and client |
| Mark pathways | Mark conduit entry points, cable tray routes, and outlet positions on the physical walls/floor |
| Install cable trays and conduits | Completed before cable pulling begins; all hangers and brackets secured |
| Prepare pull strings | Pre-thread pull strings through all conduits |
| Stage materials | Cables, patch panels, keystone jacks, face plates, labels, cable ties staged at TR |
| Conduct safety briefing | Review working-at-height, electrical isolation, and PPE requirements with installation team |

---

## 3.0 Cable Pulling Procedures

### 3.1 General Rules for Copper Cable Pulling

| Rule | Specification |
|------|--------------|
| Maximum pulling tension | Cat6: 110 N (25 lbf); Cat6A: 110 N — check manufacturer's specification |
| Minimum bend radius | 4× cable diameter for Cat6; 8× for Cat6A (STP); check data sheet |
| Cable fill ratio (conduit) | Maximum 40% fill for cable conduits per NEC/MS standards |
| Bundle size | Maximum 24 cables per tie wrap; loose ties (not crushing) |
| Tie-wrap spacing | Every 300–450 mm along horizontal runs; every 600 mm on vertical backbone runs |
| Slack at TR | Minimum 3 m coiled at patch panel; 1 m at outlet |

### 3.2 Fibre Optic Cable Pulling

Fibre optic cable requires additional care:

| Rule | Specification |
|------|--------------|
| Maximum tensile load | Typically 600–2700 N (depends on cable type) — always check manufacturer spec |
| Minimum bend radius (installation) | 20× cable diameter |
| Minimum bend radius (installed) | 10× cable diameter |
| Do not kink or crush | Fibre strands break under kink stress — irreversible damage |
| Pull from a reel stand | Never drag cable across the floor or over sharp edges |
| Use fibre-specific lubricant | Where required for long conduit runs |

### 3.3 Pathway Management

Cables must be routed through approved pathways only:

- **Cable tray** — for large bundles in ceiling voids; must be supported every 1.5 m
- **Conduit** — for protection in exposed areas, wall penetrations, and outdoor runs
- **J-hooks** — used in ceiling voids where trays are not installed; rated for cable weight
- **Firestop sleeves** — required wherever cabling passes through a fire-rated wall or floor slab; installed by a qualified firestop contractor

---

## 4.0 Termination Techniques

### 4.1 RJ-45 Keystone Jack Termination (T568B Wiring Standard)

TIA-568 specifies two wiring standards: **T568A** and **T568B**. T568B is the most widely used in commercial installations in Malaysia.

**T568B pair assignments:**

| Pin | Colour | Pair |
|-----|--------|------|
| 1 | White/Orange | 2 |
| 2 | Orange | 2 |
| 3 | White/Green | 3 |
| 4 | Blue | 1 |
| 5 | White/Blue | 1 |
| 6 | Green | 3 |
| 7 | White/Brown | 4 |
| 8 | Brown | 4 |

**Termination procedure:**
1. Strip outer jacket 25–30 mm — do not nick the pair insulation
2. Untwist each pair only as far as needed to reach the termination point (max 13 mm untwist for Cat6; 6 mm for Cat6A)
3. Seat each conductor into the IDC (Insulation Displacement Contact) slot in the correct colour position
4. Punch down using a 110-type punch-down tool; use the cut side facing away from the conductor
5. Trim excess conductor flush with the jack body
6. Snap the jack into the keystone faceplate or patch panel port

### 4.2 Patch Panel Termination

- Use manufacturer-supplied punch-down tool to avoid over-compression
- Maintain pair twist as close as possible to the termination point
- Label patch panel port with a machine-printed label immediately after termination
- Document port number against cable ID in the cable records

### 4.3 Fibre Optic Connector Termination

For field-terminated fibre:
- Use the manufacturer's field-termination kit (e.g. LC, SC, ST connectors)
- Cleave fibre using a precision cleaver; inspect end-face under a fibre microscope (200–400×)
- Insert end-face into connector; cure epoxy (factory or no-epoxy pre-polished types)
- Polish end-face with lapping film in sequence (2 µm → 1 µm → 0.3 µm)
- Inspect final end-face: no cracks, chips, or contamination
- Test insertion loss with an OTDR or optical power meter

> **Note:** Pre-polished/push-on connectors (e.g. UniCam) reduce field termination time and require no polishing.

---

## 5.0 Cable Labelling System

### 5.1 Labelling Requirements (TIA-606-B)

Every component in the cabling system must be uniquely identified and labelled:

| Component | Label Location | Label Content |
|-----------|---------------|---------------|
| Horizontal cable — TR end | Within 150 mm of termination | Cable ID (e.g. HC-B1-01-001) |
| Horizontal cable — outlet end | Within 150 mm of termination | Same Cable ID |
| Patch panel port | On the panel faceplate | Panel port number + cable ID |
| Wall outlet (faceplate) | On the outlet or faceplate | Outlet ID (e.g. WA-B1-F101-A) |
| Fibre backbone — both ends | Within 150 mm of splice/connector | Backbone ID + fibre number |
| Cable tray / conduit | Every 3 m and at changes of direction | Pathway ID |

### 5.2 Label Specifications

| Requirement | Specification |
|-------------|---------------|
| Print method | Machine-printed (thermal transfer or laser) — not handwritten |
| Material | Polyester or vinyl; rated for temperature range of installation environment |
| Adhesive | Permanent adhesive for cable labels; wrap-around style for round cables |
| Colour coding (optional) | Colour-coded per subsystem: blue = data; red = voice; yellow = fibre |
| Legibility | Minimum font size 6 pt; black text on white or colour-coded background |
| Durability | Must remain legible for the expected life of the installation (minimum 10 years) |

---

## 6.0 Cable Management Hardware

| Hardware | Purpose | Standard |
|----------|---------|--------|
| Horizontal cable manager (1U/2U) | Routes patch cords from patch panels to switch ports; prevents cable sag | 1U above and below each patch panel row |
| Vertical cable manager | Manages vertical patch cord runs on the side of the rack | At least one per rack |
| Velcro tie wraps | Secure cable bundles in trays and on J-hooks | Preferred over plastic tie wraps inside TR (allows removal without cutting) |
| Cable tray radius drops | Guides cables from tray into rack without exceeding bend radius | At tray-to-rack entry points |
| Cable labels and holders | Identify individual cables at each end | Per TIA-606-B |
| Blanking panels | Fill unused rack spaces to maintain airflow | 1U per unused rack unit |

---

## 7.0 Quality Checkpoints During Installation

At each stage of installation, the following checks must be performed and recorded:

| Stage | Quality Check |
|-------|--------------|
| Before pulling | Conduit/tray in place; pull strings installed; cable drums staged and inspected for damage |
| During pulling | Pulling tension not exceeded; no kinking; slack maintained |
| After pulling | Cable ends labelled at both ends before termination |
| After termination | Visual inspection: pair untwist within spec; no conductors misrouted; jacket intact |
| After labelling | All labels present, legible, and match the cable schedule |
| Final | Certification test pass (see KP-03 for records) |

---

## 8.0 Common Errors in Cable Installation and Labelling

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Exceeding pair untwist limit | Near-end crosstalk (NEXT) failure | Minimise untwist; use Cat6A to allow more tolerance |
| Pulling cable around sharp corners | Jacket damage; pair deformation | Use corner guides; maintain bend radius |
| Labelling after termination (from memory) | Labels attached to wrong cables | Label at both ends before termination |
| Using the wrong wiring standard at one end | Crossed pair; link failure | Confirm T568B at both ends; use colour-coded jacks |
| Overtightening tie wraps | Cable deformation; pair compression → test failure | Tie wraps finger-tight only; use velcro where possible |
| Skipping quality checks | Failures found only at final certification; expensive rework | Check at each stage; do not proceed until passed |

---

## Rujukan / References

- ANSI/TIA-568.2-D: Balanced Twisted-Pair Telecommunications Cabling and Components Standard
- ANSI/TIA-606-B: Administration Standard for Telecommunications Infrastructure
- ANSI/TIA-569-D: Telecommunications Pathways and Spaces
- BICSI TDMM (Telecommunications Distribution Methods Manual), 14th Edition
- NOSS IT-020-4:2013 Computer Systems Administration — CoCu 4: Network Cabling Management