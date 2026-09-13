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
| KOD DAN NAMA PROGRAM | IT-020-3:2013 OPERASI SISTEM KOMPUTER |
| TAHAP | 3 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C04 SERVER INSTALLATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE JOB ORDER/CHANGE REQUEST<br>2. EXECUTE HARDWARE INSTALLATION<br>3. CARRY OUT SOFTWARE INSTALLATION<br>4. PERFORM SERVER FUNCTIONALITY TEST<br>5. PREPARE SERVER INSTALLATION SET-UP REPORT |
| NO. KOD | IT-020-3:2013-C04/KP(1/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-01-analyse-server-job-order

**TUJUAN:** Kertas rujukan untuk KP-01-analyse-server-job-order.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the purpose and structure of a server job order and change request
2. Identify and interpret server hardware, software, and configuration requirements from a job order
3. Distinguish between server deployment scenarios (new installation, upgrade, migration)
4. Verify technical feasibility and resource availability before commencing server installation
5. Document analysis findings and escalate discrepancies through proper channels

---

## 1.0 Introduction to Server Job Order Analysis

A server job order (also called a server work order or server deployment request) is the formal authorisation document that initiates a server installation task. It is issued by the IT manager, project manager, or client and specifies the server type, hardware configuration, software requirements, and operational objectives the technician must fulfil.

Server installations differ significantly from desktop set-ups in scale, criticality, and consequence of error. A misconfigured server affects multiple users simultaneously, may cause service outages, and can result in data loss. Thorough job order analysis before any physical work begins is therefore a professional and operational requirement.

A **change request (Permintaan Perubahan)** is a formal modification to an existing server deployment order. Change requests arise when business requirements evolve, budget revisions occur, or technical constraints are discovered during site survey. All change requests must be reviewed, approved, and documented before implementation.

---

## 2.0 Types of Server Deployment Scenarios

Understanding the deployment scenario determines the scope of work and the risks involved.

| Scenario | Description | Key Considerations |
|----------|-------------|-------------------|
| New installation (Pemasangan baharu) | A server is being deployed for the first time in the organisation or data centre | Rack space, power feed, cooling capacity, network cabling, OS licensing |
| Hardware upgrade (Naik taraf perkakasan) | Adding RAM, storage, or expansion cards to an existing server | Compatibility with existing components, downtime window, backup before work |
| OS migration (Migrasi OS) | Moving from one server OS version to another (e.g. Windows Server 2016 → 2022) | Application compatibility testing, rollback plan, licence validity |
| Server replacement (Penggantian pelayan) | Decommissioning an old server and commissioning a new one | Data migration, IP address reassignment, DNS/AD record updates |
| Virtualisation deployment | Installing a hypervisor (e.g. VMware ESXi, Hyper-V) on bare-metal hardware | CPU virtualisation support (VT-x/AMD-V), RAM allocation per VM, storage pool planning |

---

## 3.0 Server Job Order Structure

A complete server job order contains the following fields. Every field must be reviewed and verified before work commences.

| Field | Description | Example |
|-------|-------------|---------|
| Job order number | Unique tracking identifier | JO-2024-0042 |
| Date issued | Date the order was raised | 15 March 2024 |
| Requested by | Name, designation, and department | Ahmad bin Razali, IT Manager, Finance Division |
| Priority level | Urgency classification | Critical / High / Normal / Low |
| Deployment scenario | Type of installation (see Section 2.0) | New installation |
| Server form factor | Physical type | Tower / Rack-mount (1U, 2U, 4U) / Blade |
| Processor specification | CPU model, socket, core count, clock speed | Intel Xeon Silver 4314, LGA4189, 16-core, 2.4 GHz |
| Memory specification | RAM type, capacity, speed, number of DIMMs | 4 × 32 GB DDR4 ECC RDIMM, 3200 MHz |
| Storage specification | Drive type, capacity, RAID level | 4 × 1.92 TB SSD SAS, RAID 10 |
| Network interface | NIC count, speed, bonding/teaming | 2 × 10GbE onboard + 2 × 25GbE PCIe card, LACP teaming |
| Operating system | OS name, version, edition, licensing model | Windows Server 2022 Datacenter, volume licence |
| Server roles / services | Planned server roles to be configured | Active Directory Domain Services (AD DS), DNS, DHCP |
| IP addressing | Static IP, subnet mask, default gateway, DNS servers | 192.168.10.10 / 255.255.255.0 / 192.168.10.1 |
| Rack location | Data centre, rack ID, rack unit (U) position | DC-1, Rack R-05, U 12–15 |
| Power requirements | Required power (watts), redundant PSU | 800 W, dual PSU (redundant) |
| Delivery/completion date | Required completion date | 22 March 2024 |
| Approver | Authorising signatory | Encik Hafiz, Head of IT Infrastructure |
| Budget reference | Purchase order or budget code | PO-2024-IT-0088 |

---

## 4.0 Technical Feasibility Assessment

Before accepting a job order, the technician must assess whether the installation can be completed as specified. This is called a **technical feasibility assessment (penilaian kebolehlaksanaan teknikal)**.

### 4.1 Hardware Compatibility Check

| Check Item | What to Verify |
|------------|---------------|
| CPU socket compatibility | Processor model matches motherboard socket (e.g. LGA4189 for Intel Xeon Scalable 3rd Gen) |
| RAM type and speed | DDR4 ECC RDIMM / LRDIMM as specified by motherboard vendor QVL (Qualified Vendor List) |
| Storage interface | SAS / SATA / NVMe drives match the RAID controller or onboard HBA |
| RAID controller compatibility | RAID level requested (0, 1, 5, 6, 10) is supported by the installed RAID controller |
| PCIe expansion slots | Sufficient free PCIe slots of the required generation (Gen 3/4/5) and lane width (x4, x8, x16) |
| Power supply capacity | Total system wattage (CPU TDP + RAM + drives + GPUs) does not exceed PSU capacity |
| Form factor fit | Server chassis fits within the allocated rack units (U) and rack depth |

### 4.2 Site Readiness Check

| Check Item | What to Verify |
|------------|---------------|
| Rack space availability | Required U positions are free and accessible |
| Power feed | Sufficient PDU (Power Distribution Unit) outlets with correct amperage (e.g. 16 A C13/C14) |
| Cooling capacity | Room/rack cooling can handle additional heat load (watts) |
| Network patching | Sufficient patch panel ports and switch ports at the required speed |
| Cable management | Cable runs are within acceptable length limits; labelling plan in place |

### 4.3 Software and Licensing Check

| Check Item | What to Verify |
|------------|---------------|
| OS licence type | OEM, Retail, or Volume Licence; valid product key or KMS activation available |
| CAL requirements | Client Access Licences (CALs) required for Windows Server roles (e.g. RDS CAL, AD CAL) |
| Application licences | Third-party software licences obtained before installation |
| Firmware/driver versions | Latest BIOS, BMC (Baseboard Management Controller), RAID firmware, and NIC drivers available |

---

## 5.0 Requirements Extraction Process

When analysing a server job order, apply the following systematic procedure:

1. **Read the entire job order** from start to finish before taking any action. Note incomplete or ambiguous fields.
2. **Classify the deployment scenario** (Section 2.0) to determine the scope and risk level.
3. **Perform technical feasibility assessment** (Section 4.0) — hardware, site, and licensing.
4. **Cross-reference the server vendor documentation.** Consult the server vendor's Hardware Compatibility List (HCL) and the OS vendor's Server Catalogue for confirmed support.
5. **Identify gaps and discrepancies.** Document any field that is missing, contradictory, or technically infeasible.
6. **Raise queries or change requests.** Communicate gaps to the requestor or supervisor in writing before proceeding. Do not make assumptions.
7. **Record the analysis outcome.** Produce a written feasibility summary and file it with the job order for audit purposes.

---

## 6.0 Change Request Management

When a change request is received against an existing job order:

| Step | Action |
|------|--------|
| 1 | Record the change request number, date, and originator |
| 2 | Identify which fields of the original job order are being modified |
| 3 | Assess the technical and schedule impact of the change |
| 4 | Obtain written approval from the authorised approver before implementing the change |
| 5 | Update the job order document to reflect the approved change |
| 6 | Communicate the change and its impact to all affected parties (team members, helpdesk, end-users) |
| 7 | Proceed with implementation only after approval is confirmed |

---

## 7.0 Common Errors in Server Job Order Analysis

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Proceeding without full job order | Missing requirements discovered mid-installation; service delay | Read and verify all fields before starting; use a pre-installation checklist |
| Assuming hardware compatibility | Components ordered that are incompatible (wrong RAM type, unsupported RAID level) | Cross-check against vendor HCL and QVL |
| Ignoring site readiness | Server cannot be racked due to insufficient space, power, or cooling | Conduct a site survey before procurement |
| Implementing change requests without approval | Unauthorised configuration changes; audit non-compliance | Obtain written approval for all change requests; never act on verbal instructions alone |
| Insufficient licensing review | OS or application activation failure after installation | Confirm licence keys and CAL counts before installation day |
| Not documenting the analysis | No audit trail; inability to reconstruct decisions if issues arise | File the feasibility summary with the job order record |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCU 4: Server Installation
- Microsoft Windows Server documentation: https://docs.microsoft.com/en-us/windows-server/
- CompTIA Server+ Study Guide (SK0-005) — Chapter on Server Deployment Planning
- Organisational IT infrastructure change management policy
- Server vendor Hardware Compatibility List (HCL) — applicable model