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
| NO. KOD | IT-020-4:2013-C05/KP(3/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-03-managing-network-installation-work

**TUJUAN:** Kertas rujukan untuk KP-03-managing-network-installation-work.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Supervise and coordinate network cabling and active equipment installation activities
2. Monitor progress against the project schedule and implement corrective actions
3. Manage contractors and installation teams to ensure quality and safety compliance
4. Conduct acceptance testing for installed cabling infrastructure and network equipment
5. Apply change control procedures when scope deviations are identified during installation

---

## 1.0 Introduction to Network Installation Work Management

Managing the physical installation of a computer network requires the network administrator to shift from a planning role to an active supervisory and coordination role. During the installation phase, the administrator must ensure that:

- All work is executed in accordance with the approved project plan and specification
- Quality standards (cabling standards, configuration standards) are maintained throughout
- Safety procedures are observed by all installation personnel
- Progress is tracked and deviations are identified and corrected promptly
- Changes to scope are controlled through a formal change management process
- Stakeholders (client, management, contractors) receive timely and accurate progress information

The three principal management activities during installation are: **supervising site works**, **managing contractors**, and **conducting acceptance testing**.

---

## 2.0 Supervising Cabling Installation Works

### 2.1 Cable Installation Supervision

The network administrator or a designated site supervisor must be present or conduct regular site inspections during cabling installation. The following elements must be verified at each inspection:

| Inspection Item | Compliance Requirement |
|----------------|----------------------|
| Cable type | Cables installed match the specification (Cat6A UTP, OM3 fibre, etc.) |
| Cable routing | Cables follow approved conduit routes; not laid on floors, over ceiling tiles, or in unauthorised areas |
| Bend radius | Minimum bend radius maintained (Cat6A: 4× cable diameter; fibre: 15× cable diameter for installation) |
| Conduit fill | Conduit fill does not exceed 40% capacity; pulling lubricant used where necessary |
| Separation from power | Copper data cables maintain minimum 200 mm separation from power cables; 500 mm near transformers |
| Labelling | Each cable labelled at both ends immediately after installation — do not defer labelling |
| Damage | No kinks, crushed sections, or excessive tension marks on cable jacket |

### 2.2 Termination Supervision

Termination quality directly determines the performance of the installed cabling:

| Termination Item | Requirement |
|----------------|------------|
| Untwist length | Cat6A: maximum 13 mm untwist at RJ45 plug; Cat6A panel: as short as possible (< 8 mm) |
| Pair order | Verify TIA-568-B wiring standard at all outlets and patch panels |
| Strain relief | Cable tie or clamp used at termination point; jacket not stripped excessively |
| Outlet plate | Keystone jack clicks fully into outlet plate; face plate flush with wall |
| Fibre connector | LC/SC connectors polished and cleaned before insertion; APC connectors (green) not mixed with UPC (blue) |
| Patch panel labelling | Every port labelled with the cable schedule reference number |

### 2.3 Active Equipment Installation Supervision

| Item | Requirement |
|------|------------|
| Rack mounting | Equipment mounted with cage nuts; rack unit positions as per rack elevation drawing |
| Cable management | Patch cords dressed through horizontal and vertical cable managers; not draped loose |
| Power connection | Active equipment powered from UPS-protected circuits; load balanced across PDU outlets |
| Earthing (grounding) | Rack bonded to building earth; active equipment earthed via rack |
| Ventilation | 1U blanking panels installed in all unused rack positions; hot/cold aisle maintained |
| Console access | Console port accessible; console cable connected for initial configuration |

---

## 3.0 Contractor Management / Pengurusan Kontraktor

### 3.1 Contractor Briefing and Induction

Before any contractor begins work on site, the network administrator must conduct a contractor induction covering:

1. Project scope and boundaries — what is in scope and what is explicitly excluded
2. Site safety rules — personal protective equipment (PPE), permit-to-work, emergency procedures
3. Quality standards — the cabling standard and workmanship requirements
4. Reporting structure — who the contractor's daily supervisor is; who has authority to issue instructions
5. Change control — contractors must not make any changes to scope without written approval

### 3.2 Contractor Performance Monitoring

| Performance Area | Monitoring Method | Frequency |
|-----------------|-------------------|-----------|
| Work progress | Daily site inspection; compare completed cable points against schedule | Daily |
| Workmanship quality | Random inspection of terminations and cable routes | Per phase |
| Safety compliance | Observation during site inspection; review of safety incident log | Daily |
| Resource attendance | Daily headcount; compare against resource plan | Daily |
| Material usage | Reconcile materials issued vs quantities installed | Weekly |

### 3.3 Non-Compliance Management

When a contractor fails to meet quality or safety requirements, the network administrator must:

1. **Document** the non-compliance with photographs and a written description
2. **Issue** a Non-Conformance Report (NCR) to the contractor in writing
3. **Set** a deadline for corrective action and re-inspection
4. **Escalate** to management if the contractor fails to rectify within the agreed timeline
5. **Record** all NCRs and their resolution in the project log

---

## 4.0 Progress Monitoring and Reporting / Pemantauan dan Pelaporan Kemajuan

### 4.1 Progress Measurement

Progress is measured against the approved project schedule (Gantt chart). The network administrator must track:

| Metric | How Measured |
|--------|-------------|
| Cable points installed | Count of points where cables are pulled and labelled (both ends), expressed as % of total BoQ |
| Points terminated | Count of points where termination is complete at both ends |
| Points certified | Count of points that have passed cable certification testing |
| Active equipment installed | Count of rack-mounted and powered devices vs BoQ total |
| Devices configured | Count of configured devices vs total |

### 4.2 Earned Value Concepts (simplified)

At Level 4, the network administrator applies simplified Earned Value Management (EVM) to monitor project health:

| Concept | Definition | Interpretation |
|---------|-----------|---------------|
| Planned Value (PV) | The budgeted cost of work scheduled to be done by a given date | What should have been done |
| Earned Value (EV) | The budgeted cost of work actually completed by that date | What has been done |
| Actual Cost (AC) | The actual cost incurred for work completed | What it cost |
| Schedule Variance (SV) | EV − PV | Negative = behind schedule |
| Cost Variance (CV) | EV − AC | Negative = over budget |

### 4.3 Progress Report

A weekly progress report must be submitted to the client and management, covering:

- Summary of work completed in the reporting period
- Comparison of actual vs planned progress (by WBS work package)
- Issues and risks encountered; actions taken or planned
- Anticipated completion status for the next reporting period
- Photographs of completed works
- Updated schedule (highlighting any changes from baseline)

---

## 5.0 Acceptance Testing / Ujian Penerimaan

Acceptance testing verifies that the installed network infrastructure meets the specification and relevant standards before handover to the client.

### 5.1 Copper Cable Certification

All copper cable runs must be tested with a certified cable tester (e.g., Fluke DSX-8000 or equivalent) to the applicable standard:

| Test Parameter | Requirement (Cat6A Channel, TIA-568-C.2) |
|---------------|------------------------------------------|
| Wire map | Correct TIA-568-B pin-out; no opens, shorts, reverses, or splits |
| Length | ≤ 100 m channel (permanent link ≤ 90 m) |
| Insertion loss (IL) | ≤ 20.9 dB at 500 MHz |
| NEXT (Near-End Crosstalk) | ≥ 39.9 dB at 500 MHz |
| PSNEXT | ≥ 37.9 dB at 500 MHz |
| Return Loss (RL) | ≥ 20.1 dB at 500 MHz |
| Alien Crosstalk (PSANEXT) | ≥ 60.0 dB at 500 MHz |

Test results must be saved electronically on the tester and exported to a test report. All passes (PASS) are accepted. Any failure (FAIL) must be investigated and rectified before re-testing.

### 5.2 Fibre Optic Testing

| Test | Equipment | Acceptance Criterion |
|------|-----------|---------------------|
| End-to-end loss (insertion loss) | Light source and power meter (LSPM) | Per TIA-526-14 / IEC 14763-3; connector loss ≤ 0.75 dB each, splice loss ≤ 0.3 dB, total link loss within calculated budget |
| Reflectance | OTDR | No reflections exceeding specified limit |
| Continuity | Visual fault locator (VFL) | Light visible at far end; no breaks |
| Polarity | LSPM with known source | Correct polarity (A–A, B–B) |

### 5.3 Network Connectivity Testing

After cable certification, network connectivity testing is performed:

| Test | Method | Acceptance Criterion |
|------|--------|---------------------|
| Switch port to switch port connectivity | Ping between known IP addresses | 0% packet loss over 100 pings |
| VLAN segregation | Attempt to ping between VLANs that should be isolated | No response = pass |
| DHCP | Connect test device to each access port; verify IP assignment | Correct IP, subnet, gateway, DNS received |
| Wireless coverage | Wi-Fi analyser at all intended coverage areas | Signal strength ≥ −70 dBm; SNR ≥ 25 dB |
| Internet connectivity | HTTP/HTTPS access from multiple VLANs | Pages load successfully |
| VoIP QoS (if applicable) | Test call quality; measure jitter, latency, packet loss | Jitter < 30 ms; latency < 150 ms; packet loss < 1% |
| Firewall rules | Test access from each VLAN to verify permit/deny rules | Rules enforced as per security policy |

### 5.4 User Acceptance Testing (UAT)

After technical acceptance testing, a formal User Acceptance Test (UAT) is conducted with the client's representative:

1. Walk through each floor/zone; demonstrate network connectivity at sample points
2. Demonstrate wireless coverage in all specified areas
3. Demonstrate internet access, email, and key business application connectivity
4. Present cable test reports and summarise pass/fail statistics
5. Obtain client sign-off on the Network Installation Acceptance Certificate (Sijil Penerimaan Pemasangan Rangkaian)

---

## 6.0 Change Control During Installation / Kawalan Perubahan Semasa Pemasangan

Changes to the approved scope, design, or specification are inevitable in complex installation projects. A formal change control process prevents unauthorised work and cost overruns.

### 6.1 Change Control Process

| Step | Action |
|------|--------|
| 1. Identify change | Installer or administrator identifies that the approved design cannot be executed as planned (e.g., obstacle in conduit route, additional network points requested by client) |
| 2. Document change request | Raise a Change Request (CR) form: describe the change, reason, impact on cost and schedule |
| 3. Assess impact | Network administrator estimates the cost and schedule impact of the change |
| 4. Obtain approval | Client and management sign the CR; or reject and revert to original scope |
| 5. Issue Variation Order | Issue a Variation Order (VO) to the contractor authorising the additional work |
| 6. Update project documents | Update the BoQ, schedule, and drawings to reflect the change |
| 7. Record in project log | All approved changes are recorded chronologically |

**Important:** No variation work may commence without a signed Variation Order (VO). Verbal instructions are not sufficient.

---

## Rujukan / References

- NOSS IT-020-4:2013 Computer Systems Administration — CoCU 5
- TIA-568.2-D: Balanced Twisted-Pair Telecommunications Cabling and Components Standard
- IEC 14763-3: Implementation and Operation of Customer Premises Cabling — Optical Fibre Cabling
- IEEE 802.1Q: Virtual LANs (VLANs)
- Fluke Networks: DSX CableAnalyzer Series User Documentation
- CIDB Malaysia: Construction Industry Development Board — Site Management and Safety Guidelines