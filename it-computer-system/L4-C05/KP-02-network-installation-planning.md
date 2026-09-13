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
| NO. KOD | IT-020-4:2013-C05/KP(2/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-02-network-installation-planning

**TUJUAN:** Kertas rujukan untuk KP-02-network-installation-planning.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Produce a Bill of Quantities (BoQ) for a network installation project
2. Develop a project schedule using work breakdown structure (WBS) and Gantt chart techniques
3. Plan human resource allocation for network installation works
4. Identify procurement requirements and lead times for network equipment and materials
5. Develop a risk management plan and contingency measures for network installation projects

---

## 1.0 Introduction to Network Installation Planning

Planning is the management layer between specification analysis and physical installation. A well-constructed plan transforms the approved specification into a coordinated set of tasks, resources, timelines, and controls. At Level 4, the network administrator is responsible for producing planning documents that:

- Define precisely what work must be done (scope)
- Identify the resources required (materials, labour, equipment)
- Establish the sequence and schedule of work (time)
- Allocate costs to each work element (budget)
- Assign accountability (responsibility matrix)
- Anticipate and mitigate risks (risk plan)

These documents form the Project Plan — the administrator's authority to proceed and the baseline against which actual progress is measured.

---

## 2.0 Bill of Quantities (BoQ) / Senarai Kuantiti Kerja

The Bill of Quantities (BoQ) is a structured cost document listing every item of material, equipment, and labour required for the network installation. It is derived directly from the approved specification and the site survey.

### 2.1 BoQ Structure

| Section | Item | Unit | Quantity | Unit Rate (RM) | Total (RM) |
|---------|------|------|----------|---------------|------------|
| **A. Active Equipment** | Core switch (Layer 3, 24-port SFP+) | Unit | 1 | — | — |
| | Distribution switch (Layer 2, 48-port PoE+) | Unit | 4 | — | — |
| | Wireless access point (Wi-Fi 6, indoor) | Unit | 20 | — | — |
| | Firewall / UTM appliance | Unit | 1 | — | — |
| **B. Passive Infrastructure** | Cat6A UTP cable (305 m box) | Box | 12 | — | — |
| | OM3 multimode fibre (per metre) | Metre | 200 | — | — |
| | 24-port patch panel (Cat6A) | Unit | 8 | — | — |
| | 42U floor-standing rack | Unit | 2 | — | — |
| | PVC conduit 25 mm (per metre) | Metre | 600 | — | — |
| **C. Power** | UPS (2000 VA, network-managed) | Unit | 2 | — | — |
| | PDU (rack-mounted, 16-outlet) | Unit | 4 | — | — |
| **D. Labour** | Network infrastructure technician (days) | Day | 15 | — | — |
| | Cable puller / installer helper (days) | Day | 20 | — | — |
| | Cabling certification testing (points) | Point | 180 | — | — |
| **E. Miscellaneous** | Cable ties, labels, cable markers | Lot | 1 | — | — |
| | Conduit fittings, junction boxes | Lot | 1 | — | — |
| **JUMLAH / TOTAL** | | | | | **—** |

**Notes on BoQ preparation:**
- All quantities include a minimum 10% waste allowance for cable and conduit
- Unit rates are to be obtained from at least three (3) quotations from approved suppliers
- The completed BoQ forms the basis of the project budget and purchase orders
- Any variation from the approved BoQ requires a Variation Order (VO) signed by the authorised representative

### 2.2 Quantity Take-Off Process

The quantity take-off is the systematic measurement process used to derive BoQ quantities from the site plan:

1. Obtain confirmed floor plans (as-built drawings preferred; architectural drawings acceptable)
2. Measure each cable run from the network point to the nearest distribution patch panel — record on a cable schedule
3. Add 20% to each measured run for routing allowances, service loops, and termination tails
4. Count all active equipment items from the specification; verify against rack elevation drawings
5. Measure conduit runs from the floor plan; add 15% for bends and offsets
6. Compile all measurements into the BoQ table and verify totals

---

## 3.0 Work Breakdown Structure (WBS) / Struktur Pecahan Kerja

The WBS decomposes the total project scope into manageable work packages. Each work package has a defined deliverable, responsible party, duration, and dependencies.

### 3.1 Level 4-C05 WBS

| WBS Code | Work Package | Deliverable | Responsible |
|----------|-------------|-------------|-------------|
| 1.0 | Specification Analysis | Approved specification + gap register | Network Administrator |
| 2.0 | Planning | Approved project plan, BoQ, schedule | Network Administrator |
| 2.1 | BoQ preparation | Signed BoQ | Network Administrator |
| 2.2 | Schedule development | Approved Gantt chart | Network Administrator |
| 2.3 | Procurement plan | Purchase orders issued | Network Administrator |
| 3.0 | Site Preparation | Ready-for-installation site | Site Supervisor |
| 3.1 | Conduit and trunking installation | All conduit installed and tested | Installation Technician |
| 3.2 | Rack and cabinet installation | Racks secured, earthed, power connected | Installation Technician |
| 4.0 | Cable Installation | All cables pulled and labelled | Cable Crew |
| 4.1 | Horizontal copper cabling | All copper runs installed | Cable Crew |
| 4.2 | Backbone fibre cabling | All fibre runs installed | Fibre Specialist |
| 4.3 | Cable termination | All patch panels and outlet plates terminated | Termination Technician |
| 5.0 | Active Equipment Installation | All active equipment rack-mounted and powered | Network Technician |
| 6.0 | Configuration | All devices configured per IP plan | Network Administrator |
| 7.0 | Testing and Acceptance | Signed acceptance report | Network Administrator + Client |
| 8.0 | Management Report | Final installation management report | Network Administrator |

---

## 4.0 Project Schedule / Jadual Projek

### 4.1 Gantt Chart Development

The project schedule is represented as a Gantt chart — a bar chart showing each work package against a calendar timeline. Key scheduling principles:

| Principle | Application |
|-----------|-------------|
| Sequencing | Identify dependencies: conduit must be installed before cabling; cabling before termination; termination before active equipment configuration |
| Critical path | Identify the longest chain of dependent tasks — any delay on the critical path delays the entire project |
| Float | Tasks not on the critical path have float (slack) — they can be delayed without affecting the project end date |
| Resource levelling | Adjust task timing to avoid over-allocating any single resource (e.g., one cable crew cannot work in two locations simultaneously) |
| Milestones | Mark key decision points: site readiness, cabling complete, configuration complete, acceptance sign-off |

### 4.2 Sample Schedule Structure (indicative — 60 hrs WA2)

| Phase | Duration | Key Activities |
|-------|----------|---------------|
| Planning and procurement | Week 1–2 | BoQ approval, purchase orders, resource mobilisation |
| Site preparation | Week 3 | Conduit, rack and cabinet installation, power provisioning |
| Cabling installation | Week 4–5 | Copper and fibre cable pulling, labelling |
| Termination and patching | Week 6 | Punch-down, fibre splicing/termination, patch cord connections |
| Active equipment installation | Week 7 | Rack mounting, power connection, initial boot |
| Configuration | Week 7–8 | Switch, router, AP, firewall configuration per IP plan |
| Testing | Week 8–9 | Cable certification, connectivity testing, performance testing |
| Acceptance | Week 9 | Acceptance walkthrough, sign-off, report |

---

## 5.0 Resource Planning / Perancangan Sumber

### 5.1 Human Resource Plan

| Role | Responsibilities | Quantity | Estimated Duration |
|------|-----------------|----------|--------------------|
| Network Administrator (Pentadbir Rangkaian) | Overall project management, specification, configuration, acceptance | 1 | Full project |
| Network Installation Technician (Juruteknik Pemasangan) | Active equipment installation, configuration support | 2 | Weeks 5–9 |
| Cable Installation Crew (Pasukan Pendawaian) | Conduit, cable pulling, labelling | 3–4 | Weeks 3–6 |
| Termination Specialist (Pakar Penamatan Kabel) | Punch-down termination, fibre splicing | 1–2 | Weeks 6 |
| Testing / Certification Technician (Juruteknik Pensijilan) | Fluke cable certification, test documentation | 1 | Weeks 8 |

### 5.2 Equipment and Tool Requirements

| Item | Purpose | Source |
|------|---------|--------|
| Cable certification tester (e.g., Fluke DSX-8000) | Certify Cat6A and fibre runs to TIA-568 standard | Hire or contractor-supplied |
| OTDR (Optical Time Domain Reflectometer) | Test fibre continuity and loss | Hire or contractor-supplied |
| Fish tape and cable pulling lubricant | Pull cables through conduit | Purchase |
| Punch-down tool (110-type) | Terminate Cat6A at patch panels and outlets | Purchase |
| Fusion splicer | Join fibre optic cables | Hire or contractor-supplied |
| Laptop with network management software | Configure and monitor network equipment | Network Administrator's own |
| Rack screws, cage nuts, cable management rings | Rack installation | Purchase with racks |

---

## 6.0 Procurement Plan / Pelan Perolehan

| Item | Lead Time (estimated) | Action Required |
|------|----------------------|----------------|
| Core and distribution switches | 4–8 weeks | Issue PO immediately after BoQ approval |
| Wireless access points | 2–4 weeks | Issue PO after BoQ approval |
| Firewall appliance | 4–6 weeks | Issue PO immediately; requires licensing |
| Structured cabling materials (cable, conduit, patch panels) | 1–2 weeks | Issue PO after site survey confirmed |
| Racks and cabinets | 2–3 weeks | Issue PO early; required for site preparation |
| UPS | 2–3 weeks | Issue PO after confirmed power specifications |

**Procurement rules:**
- All purchases above RM10,000 require a minimum of three (3) quotations and management approval
- Approved suppliers must be on the organisation's vendor register
- All equipment must be delivered and inspected against the BoQ before installation commences

---

## 7.0 Risk Management Plan / Pelan Pengurusan Risiko

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Equipment delivery delay | Medium | High | Order critical items early; identify alternative suppliers |
| Site not ready (civil works incomplete) | Medium | High | Confirm site readiness milestone with client; include a site readiness acceptance gate |
| Cable run exceeds 100 m limit (discovery during installation) | Low | High | Measure all runs during site survey; flag any runs >80 m for review |
| Specification change during installation | High | Medium | Implement change control process; all changes require signed Variation Order |
| Skilled resource unavailability | Low | Medium | Identify backup contractors; maintain a resource register |
| Power failure during configuration | Low | Low | Use UPS during configuration; save configuration frequently |
| Fibre damage during pulling | Low | High | Use appropriate pulling tension limits; deploy cable pulling lubricant |

---

## Rujukan / References

- NOSS IT-020-4:2013 Computer Systems Administration — CoCU 5
- Project Management Institute (PMI): PMBOK Guide — Project Planning Process Group
- TIA-568.2-D: Balanced Twisted-Pair Telecommunications Cabling and Components Standard
- Malaysian Standard MS ISO 21500: Guidance on Project Management
- Cisco Design Guide: Enterprise Network Design