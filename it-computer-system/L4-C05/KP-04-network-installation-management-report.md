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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C05 COMPUTER NETWORK INSTALLATION MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE COMPUTER NETWORK SET-UP SPECIFICATION<br>2. PLAN COMPUTER NETWORK INSTALLATION<br>3. MANAGE COMPUTER NETWORK INSTALLATION WORK<br>4. PRODUCE COMPUTER NETWORK INSTALLATION MANAGEMENT REPORT |
| NO. KOD | IT-020-4:2013-C05/KP(4/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-04-network-installation-management-report

**TUJUAN:** Kertas rujukan untuk KP-04-network-installation-management-report.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Identify the required sections and content of a network installation management report
2. Compile technical test results and as-built documentation into a structured report
3. Produce an executive summary suitable for management and non-technical stakeholders
4. Develop handover documentation for the client's ongoing network operations
5. Apply professional report writing standards appropriate for a government-standard technical document

---

## 1.0 Introduction to the Network Installation Management Report

The Network Installation Management Report (Laporan Pengurusan Pemasangan Rangkaian Komputer) is the final deliverable of the network installation management process. It serves multiple purposes:

| Purpose | Audience |
|---------|---------|
| Document that the installation was completed in accordance with the specification | Client management; project sponsor |
| Provide a technical record of the as-installed network for future maintenance and upgrades | IT operations team; future network administrators |
| Confirm that all acceptance criteria were met (or document agreed deviations) | Client; JPK / regulatory body |
| Formally close the project and transfer responsibility to the client | Project manager; finance (for final payment) |
| Serve as a lessons-learned record for future similar projects | Network administrator's organisation |

The report is a professional document that represents the quality of the network administrator's work. It must be accurate, complete, clearly structured, and free of technical errors.

---

## 2.0 Report Structure / Struktur Laporan

A Network Installation Management Report must contain the following sections:

### 2.1 Cover Page (Muka Hadapan)

| Element | Content |
|---------|---------|
| Report title | "Computer Network Installation Management Report" / "Laporan Pengurusan Pemasangan Rangkaian Komputer" |
| Project reference | Project number, site name, and client organisation |
| Prepared by | Name, designation, and organisation of the network administrator |
| Date | Report date |
| Version | Version number and status (e.g., v1.0 — Final) |
| Distribution list | Names and designations of all report recipients |
| Classification | e.g., SULIT, TERHAD, or UNTUK KEGUNAAN RASMI SAHAJA if applicable |

### 2.2 Executive Summary (Ringkasan Eksekutif)

The executive summary is a maximum two-page non-technical summary intended for senior management and the client's leadership. It must cover:

- Project objectives and scope (in plain language)
- Start date and completion date; planned vs actual comparison
- Total number of network points installed and certified
- Summary of test results (e.g., "180 of 180 cable points PASS; 0 FAIL")
- Any approved variations to original scope
- Overall project outcome (on time / delayed; within budget / over budget)
- Formal statement that the network is ready for operational use

### 2.3 Project Background (Latar Belakang Projek)

| Subsection | Content |
|-----------|---------|
| Client and site description | Organisation name, site address, building description |
| Project objectives | What the installation was designed to achieve (e.g., replace legacy 100 Mbps network with 1/10 Gbps infrastructure to support 250 users) |
| Scope of work | Summary of what was installed: number of floors, network points, equipment types |
| Project team | Names and roles of all personnel involved |
| Contractual basis | Reference to the contract or purchase order; specification document reference |

### 2.4 Installation Summary (Ringkasan Pemasangan)

| Subsection | Content |
|-----------|---------|
| Cabling works summary | Total cable metres installed by type; total conduit metres; total network points terminated and labelled |
| Active equipment summary | List of all active equipment installed (brand, model, serial number, rack location, firmware version) |
| IP addressing summary | Summary of VLAN design, IP subnets assigned, DHCP scopes configured |
| Variations from specification | List of all approved Variation Orders with description, reason, and cost impact |
| Schedule performance | Planned vs actual dates for each major milestone; explanation of any delays |

### 2.5 Test Results Summary (Ringkasan Keputusan Ujian)

This section presents the results of all acceptance testing:

#### Copper Cable Test Summary

| Parameter | Total Points | PASS | FAIL | Pass Rate |
|-----------|-------------|------|------|-----------|
| Wire map | 180 | 180 | 0 | 100% |
| Length | 180 | 180 | 0 | 100% |
| Insertion loss | 180 | 178 | 2* | 98.9%* |
| NEXT | 180 | 180 | 0 | 100% |
| Overall (all parameters) | 180 | 180 | 0 | 100% |

*Example: failures rectified by re-termination; re-test result: PASS. Final result: 100%.*

#### Fibre Cable Test Summary

| Link | Type | Measured Loss (dB) | Maximum Allowed (dB) | Result |
|------|------|--------------------|---------------------|--------|
| MDF to IDF-1 (Floor 1) | OM3, 6-core | 1.2 | 3.5 | PASS |
| MDF to IDF-2 (Floor 2) | OM3, 6-core | 1.4 | 3.5 | PASS |

#### Network Connectivity Test Summary

| Test Category | Tests Performed | Passed | Failed | Result |
|--------------|----------------|--------|--------|--------|
| Ping (end-to-end) | 50 | 50 | 0 | PASS |
| VLAN segregation | 8 | 8 | 0 | PASS |
| DHCP | 20 | 20 | 0 | PASS |
| Wireless coverage | 25 zones | 25 | 0 | PASS |
| Internet connectivity | 5 VLANs | 5 | 0 | PASS |

### 2.6 As-Built Documentation (Dokumentasi Sebagaimana Dibina)

As-built documentation records the network exactly as it was installed — which may differ from the original specification due to approved variations. This section must include:

| Document | Content |
|----------|---------|
| As-built floor plan | Floor plan with network points, conduit routes, rack locations, and AP locations marked and labelled as installed |
| Cable schedule | Complete list of all cable runs: cable ID, origin (patch panel port), destination (outlet location), cable type, length, and test result reference |
| Rack elevation drawings | Front and rear views of each rack/cabinet showing equipment positions and patch cord connections |
| IP address plan (as-built) | Final IP scheme: VLANs, subnets, DHCP scopes, static assignments, DNS, gateway — as configured |
| Equipment register | All active equipment: brand, model, serial number, MAC address, IP address, firmware version, warranty expiry |
| Configuration backup | Confirmation that running configuration of all managed devices has been saved and stored in the client's designated location |
| Cable certification reports | Full Fluke test reports (electronic format on USB drive; summary printed in appendix) |

### 2.7 Issues and Non-Conformances (Isu dan Ketidakpatuhan)

| Item | Description | Action Taken | Status |
|------|-------------|-------------|--------|
| NCR-001 | Cable run to Room 203 tested FAIL (insertion loss) on first test — identified as poor termination at patch panel | Re-terminated at patch panel; re-tested | Closed — PASS |
| VO-001 | Client requested 5 additional network points in the newly partitioned server room | Variation Order VO-001 approved; RM 1,200 additional cost; 1 day schedule impact | Closed |

### 2.8 Handover Documentation (Dokumentasi Serah Terima)

The handover section provides the client's IT team with everything needed to operate and maintain the network from Day 1:

| Document | Purpose |
|----------|---------|
| Network administrator's contact details | First point of contact for warranty and post-installation queries |
| Equipment warranty summary | Warranty period and support level for each equipment item; vendor support contact |
| Username and password register (sealed) | Default and configured credentials for all managed devices; to be stored securely by client |
| Network diagram (logical and physical) | Current network topology diagrams in editable format (Visio or equivalent) |
| VLAN and IP address plan | Reference document for future IP address assignments and VLAN changes |
| Recommended maintenance schedule | Annual cable inspection, switch firmware updates, UPS battery replacement schedule |
| Spares recommendation | Recommended spare parts to stock: patch cords (5%), keystone jacks (2%), spare switch (1 unit) |

### 2.9 Conclusion and Sign-Off (Kesimpulan dan Pengesahan)

The final section contains:

- Formal statement of project completion
- Confirmation that the network meets all acceptance criteria
- Statement of outstanding items (if any) with agreed resolution dates
- Signatures of the network administrator (prepared by), client representative (accepted by), and the organisation's authorised signatory

#### Network Installation Acceptance Certificate (Sijil Penerimaan)

| | Name | Designation | Signature | Date |
|---|------|-------------|-----------|------|
| Prepared by (Network Administrator) | | | | |
| Accepted by (Client Representative) | | | | |
| Witnessed by (Management) | | | | |

---

## 3.0 Professional Report Writing Standards / Piawaian Penulisan Laporan Profesional

### 3.1 Language and Tone

- Use formal Bahasa Malaysia or English (or bilingual as required by the client)
- Use third person and passive voice for technical descriptions (e.g., "Cabling works were completed on 15 June 2026" — not "I completed cabling on 15 June 2026")
- Avoid jargon that is not explained; define technical abbreviations on first use
- Use consistent terminology throughout (do not alternate between "network point" and "data point" or "cable outlet")

### 3.2 Formatting Standards

| Element | Requirement |
|---------|------------|
| Font | Times New Roman 12pt or Arial 11pt |
| Margins | 25 mm all sides |
| Page numbering | Bottom centre; format "Page X of Y" |
| Section numbering | Hierarchical (1.0, 1.1, 1.2, 2.0...) |
| Tables | All tables have headers; borders visible; data aligned consistently |
| Figures | All figures numbered and captioned (e.g., "Figure 1: As-Built Network Diagram, Ground Floor") |
| Appendices | Lettered (Appendix A, B, C...); referenced in the main body |

### 3.3 Report Version Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| v0.1 | Draft | Network Administrator | First draft for internal review |
| v0.2 | Draft | Network Administrator | Corrections from internal review |
| v1.0 | Final | Network Administrator | Approved and issued to client |

---

## 4.0 Common Report Deficiencies and How to Avoid Them

| Deficiency | Consequence | Prevention |
|-----------|-------------|-----------|
| Missing as-built drawings | Client cannot maintain or extend the network accurately | Update drawings throughout the project; never rely on pre-installation drawings for the final report |
| Test results presented as summaries only without evidence | Client cannot verify claims; disputes at handover | Attach full Fluke test reports as appendix |
| Equipment serial numbers missing from equipment register | Warranty claims cannot be processed | Record serial numbers during unpacking and installation |
| No password register | Client locked out of managed equipment | Maintain a sealed credential register; hand over at acceptance |
| Variations not documented | Disputed invoices; scope creep arguments | Issue a Variation Order for every change before work starts |
| Report issued before all tests are passed | Client accepts a defective network | Adopt a policy: no report issued until all test failures are resolved |

---

## Rujukan / References

- NOSS IT-020-4:2013 Computer Systems Administration — CoCU 5
- Jabatan Perkhidmatan Awam (JPA) Malaysia — Panduan Penulisan Laporan Teknikal
- Project Management Institute (PMI): PMBOK Guide — Project Closure
- TIA-606-C: Administration Standard for Telecommunications Infrastructure
- Malaysian Standard MS ISO 9001: Quality Management Systems (Documentation requirements)