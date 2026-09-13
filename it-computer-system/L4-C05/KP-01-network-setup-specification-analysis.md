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
| NO. KOD | IT-020-4:2013-C05/KP(1/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-01-network-setup-specification-analysis

**TUJUAN:** Kertas rujukan untuk KP-01-network-setup-specification-analysis.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the purpose and components of a computer network set-up specification document
2. Identify and interpret network topology, cabling, and equipment specifications from client requirements
3. Conduct a site survey to verify physical and environmental suitability for network installation
4. Analyse bandwidth, scalability, and security requirements from business needs
5. Identify gaps, ambiguities, and risks in a network specification before planning commences

---

## 1.0 Introduction to Network Set-Up Specification Analysis

A computer network set-up specification (spesifikasi persediaan rangkaian) is the foundational document that defines all technical, physical, and operational requirements for a network installation project. At Level 4, the network administrator does not merely receive and execute a specification — they are responsible for critically analysing it, verifying its completeness, identifying gaps, and ensuring it aligns with the organisation's current and future operational requirements.

Specification analysis is the first and most critical step in the network installation management cycle. Errors or omissions identified at this stage cost comparatively little to correct. The same errors discovered during or after installation result in rework, downtime, and significant cost overruns.

The specification analysis process covers four domains:

| Domain | Description |
|--------|-------------|
| Technical requirements | Network topology, protocols, equipment models, cabling standards, IP addressing |
| Physical / site requirements | Building layout, conduit routes, rack locations, power supply, cooling |
| Business requirements | Number of users, bandwidth needs, availability targets, growth projections |
| Regulatory / compliance requirements | Data Protection Act, ISO 27001, industry-specific standards |

---

## 2.0 Network Set-Up Specification Document Structure

A complete network set-up specification should contain the following sections:

| Section | Contents |
|---------|----------|
| Project identification | Project name, client organisation, site address, project reference number, date issued, authorised by |
| Scope of work | Number of floors/buildings, number of network points, area coverage (m²), included and excluded works |
| Network topology | Logical topology (star, mesh, hybrid), physical topology, core/distribution/access layer design |
| Equipment list | Switches (layer 2/3), routers, access points, servers, patch panels, racks, UPS — with model numbers and quantities |
| Cabling specification | Cable category (Cat6, Cat6A, Cat7, fibre optic type), conduit type and size, maximum run lengths, labelling standard |
| IP addressing plan | Subnet design, VLAN configuration, DHCP scope, DNS, gateway addresses |
| Security requirements | Firewall placement, network access control (NAC), VLAN segmentation, wireless security (WPA3), physical security of network rooms |
| Power and environment | Power socket requirements, UPS capacity, rack cooling, ambient temperature limits |
| Acceptance criteria | Test standards (TIA-568, ISO 11801), performance benchmarks, sign-off conditions |
| Timeline and milestones | Key dates, phasing plan if multi-phase |

---

## 3.0 Network Topology Analysis

Before accepting a specification for planning, the network administrator must verify that the proposed topology is fit for purpose.

### 3.1 Common Topologies and Their Implications

| Topology | Characteristics | Typical Use Case |
|----------|----------------|-----------------|
| Star | All nodes connect to a central switch; easy to manage and troubleshoot; single point of failure at switch | Office LAN, most enterprise environments |
| Hierarchical (Core-Distribution-Access) | Three-tier design; highly scalable; provides redundancy at each tier | Large enterprise, campus networks |
| Mesh (partial/full) | Multiple redundant paths; high resilience; complex to manage | Data centres, critical infrastructure |
| Hybrid | Combination of topologies; tailored to site layout | Multi-building campuses |

### 3.2 Topology Verification Checklist

When analysing the specified topology, the network administrator must confirm:

- The topology matches the physical building layout (single floor, multi-floor, multi-building)
- Redundancy requirements are met (dual uplinks, spanning tree or link aggregation)
- The number of switch ports at each layer is sufficient for current device count plus projected growth (typically +20% capacity buffer)
- Wireless access point placement aligns with coverage requirements and interference mitigation

---

## 4.0 Cabling Specification Analysis

Cabling is the physical foundation of the network and is the most difficult and expensive element to retrofit. The specification must be analysed thoroughly before any cable is pulled.

### 4.1 Copper Cabling Standards

| Category | Bandwidth | Max Segment Length | Application |
|----------|-----------|--------------------|-------------|
| Cat5e | 1 Gbps | 100 m | Legacy; not recommended for new installations |
| Cat6 | 1 Gbps (up to 10 Gbps at ≤55 m) | 100 m | Standard office LAN |
| Cat6A | 10 Gbps | 100 m | High-density office, data centre access |
| Cat7 | 10 Gbps | 100 m | Shielded; for high EMI environments |

### 4.2 Fibre Optic Standards

| Type | Mode | Distance | Application |
|------|------|----------|-------------|
| OM3 (50/125 µm) | Multimode | Up to 300 m (10GbE) | Intra-building backbone |
| OM4 (50/125 µm) | Multimode | Up to 400 m (10GbE) | Campus backbone |
| OS2 (9/125 µm) | Single-mode | Up to 10 km | Inter-building, WAN links |

### 4.3 Cabling Specification Verification

The administrator must verify the following from the specification:

1. **Cable category** matches the required bandwidth and future upgrade path
2. **Maximum run lengths** do not exceed standard limits (account for patch cord lengths at both ends — total channel length ≤ 100 m for copper)
3. **Conduit sizing** is adequate (maximum 40% fill ratio for copper cables)
4. **Cable routes** avoid sources of electromagnetic interference (EMI): power cables, fluorescent lighting, electric motors, lift shafts
5. **Fire rating** of cables meets building regulations (e.g., LSZH — Low Smoke Zero Halogen — in public buildings)
6. **Labelling standard** is defined (TIA-606-C or equivalent)

---

## 5.0 Equipment Specification Analysis

### 5.1 Key Equipment Parameters to Verify

| Equipment | Key Parameters |
|-----------|---------------|
| Layer 2 switch | Port count, PoE budget (watts), switching capacity (Gbps), stacking capability, management features (SNMP, RSPAN) |
| Layer 3 switch / router | Routing protocols supported (OSPF, BGP), throughput, VPN support, QoS capability |
| Wireless access point | Frequency bands (2.4 GHz, 5 GHz, 6 GHz), IEEE standard (Wi-Fi 6E = 802.11ax), PoE class requirement, maximum concurrent clients |
| Server / NAS | CPU, RAM, storage capacity, RAID configuration, NIC speed (1G/10G) |
| UPS | Capacity (VA/W), runtime at full load, battery type, network management card |
| Patch panel | Port count, cable category compatibility, IDC punch-down type |

### 5.2 Compatibility Verification

The administrator must cross-check compatibility across all equipment in the specification:

- Switch uplink ports match the required fibre/copper transceiver type
- PoE switch budget is sufficient for all PoE devices (APs, IP cameras, VoIP phones) simultaneously
- All equipment is from compatible vendor ecosystems (or interoperability is explicitly tested)
- Firmware versions support required features (e.g., VLAN tagging, RSTP, 802.1X)

---

## 6.0 Site Survey and Physical Verification

A specification document alone is insufficient — the network administrator must conduct or commission a physical site survey to verify:

| Survey Item | What to Check |
|-------------|--------------|
| Building plan / floor layout | Confirm wall types (drywall vs concrete), ceiling type (suspended vs solid), room dimensions, door/window positions |
| Cable routes | Walk proposed conduit routes; identify obstacles (structural beams, asbestos, service ducts); measure actual cable run lengths |
| Network/server room | Dimensions, door width (for equipment delivery), existing power sockets, grounding point, ventilation/air-conditioning status |
| Power supply | Number and location of power sockets for network equipment; dedicated circuit availability; generator backup coverage |
| Existing infrastructure | Existing conduits, cable trays, junction boxes that can be reused; existing cabling that must be decommissioned |
| Environmental hazards | Temperature, humidity, dust, vibration, flood risk in areas where equipment will be installed |

Site survey findings must be documented in a Site Survey Report and compared against the specification. Discrepancies must be raised with the client before planning proceeds.

---

## 7.0 Business and Scalability Requirements Analysis

Beyond the technical specification, the network administrator must understand the business context:

| Business Requirement | Analysis Questions |
|---------------------|-------------------|
| Number of users | Current count and projected 3–5 year growth — is the port count and IP address space sufficient? |
| Bandwidth requirements | What applications will run? (VoIP, video conferencing, cloud ERP, large file transfers) — is the WAN link sized accordingly? |
| Availability requirements | What is the acceptable downtime? (e.g., 99.9% = <9 hours/year) — does the design include adequate redundancy? |
| Security requirements | Are there compliance mandates (PCI-DSS, HIPAA, PDPA)? Are VLANs required to segregate traffic types? |
| Remote access | Are VPN requirements specified? Site-to-site and/or remote user VPN? |
| Wireless coverage | Are there areas with special coverage requirements (warehouses, outdoor, high-density meeting rooms)? |

---

## 8.0 Gap and Risk Analysis

After reviewing all specification sections and the site survey, the administrator must produce a Gap and Risk Register:

| Item | Description | Action Required |
|------|-------------|----------------|
| Gap | A specification element that is missing, incomplete, or insufficiently detailed | Request clarification from client; do not proceed with planning until resolved |
| Risk | A known uncertainty that could affect cost, timeline, or quality | Document likelihood and impact; develop mitigation strategy |
| Assumption | A decision made in the absence of explicit guidance | Document and obtain written client approval |

Common gaps found in network specifications:

- IP addressing plan not provided (only quantity of addresses stated)
- Cable category specified but conduit type and routing not described
- Wireless coverage requirement stated but no site RF survey conducted
- UPS runtime requirement not specified
- Acceptance test criteria not defined

---

## Rujukan / References

- NOSS IT-020-4:2013 Computer Systems Administration — CoCU 5
- TIA-568.2-D: Balanced Twisted-Pair Telecommunications Cabling and Components Standard
- ISO/IEC 11801:2017 Information Technology — Generic Cabling for Customer Premises
- IEEE 802.11ax (Wi-Fi 6/6E) Standard
- Cisco Networking Academy: CCNA — Network Fundamentals
- Malaysian Communications and Multimedia Commission (MCMC) — Technical Code for Structured Cabling