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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C02 COMPUTER SYSTEM MAINTENANCE |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. IDENTIFY COMPUTER MAINTENANCE REQUIREMENTS<br>2. CARRY OUT COMPUTER SCHEDULED PREVENTIVE MAINTENANCE<br>3. PERFORM COMPUTER CORRECTIVE MAINTENANCE<br>4. PREPARE COMPUTER MAINTENANCE REPORT |
| NO. KOD | IT-020-3:2013-C02/KP(1/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-01-identify-maintenance-requirements

**TUJUAN:** Kertas rujukan untuk KP-01-identify-maintenance-requirements.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the purpose and importance of identifying computer maintenance requirements before undertaking any maintenance task
2. Distinguish between preventive, corrective, and predictive maintenance types and identify which applies to a given situation
3. Interpret a maintenance request form (borang permintaan penyelenggaraan) and extract the key requirements
4. List the tools, materials, and safety precautions required for a given maintenance activity
5. Document identified maintenance requirements accurately in a maintenance checklist

---

## 1.0 Introduction to Computer Maintenance

Computer maintenance (penyelenggaraan komputer) refers to all actions taken to keep a computer system in optimal working condition and to prevent or remedy faults. A well-maintained system experiences fewer unplanned failures, has a longer service life, and delivers consistent performance.

Before any maintenance work begins, the technician must clearly identify what is required. Acting without a clear requirements assessment leads to wasted effort, use of incorrect tools, or introduction of new faults into a previously functional system.

There are three broad categories of computer maintenance:

| Type | Malay Term | Trigger | Example |
|------|-----------|---------|---------|
| Preventive Maintenance (PM) | Penyelenggaraan Pencegahan | Scheduled; proactive | Monthly dust cleaning, quarterly driver updates |
| Corrective Maintenance (CM) | Penyelenggaraan Pembetulan | Fault has occurred; reactive | Replacing a failed hard disk, fixing a blue screen error |
| Predictive Maintenance (PdM) | Penyelenggaraan Ramalan | Data-driven; condition monitoring | Acting on S.M.A.R.T. drive warnings before failure |

---

## 2.0 Reading and Interpreting a Maintenance Request Form

All maintenance activities in a managed environment are initiated by a **Maintenance Request Form** (Borang Permintaan Penyelenggaraan) or a help desk ticket. The technician must read and interpret this document carefully before proceeding.

A standard maintenance request form contains the following fields:

| Field | Description |
|-------|-------------|
| Request number | Unique identifier for tracking (nombor rujukan) |
| Date and time raised | When the request was submitted |
| Raised by | Name and department of the requestor |
| Asset tag / Serial number | Identifies the specific computer unit |
| Location | Physical location of the equipment (room, floor, building) |
| Type of maintenance | Preventive, corrective, or predictive |
| Problem description | Symptoms reported by the user (for CM) or schedule reference (for PM) |
| Priority | Urgency level — Critical, High, Normal, Low |
| Requested completion date | Deadline for the maintenance to be completed |
| Authorisation | Supervisor or IT manager sign-off |

The technician must verify all fields are complete. Missing or ambiguous information must be clarified with the requestor or supervisor before work begins.

---

## 3.0 Classifying the Maintenance Type

Once the request form has been read, the technician determines which type of maintenance applies. This classification drives all subsequent planning decisions.

### 3.1 Preventive Maintenance Requirements

Preventive maintenance is carried out on a fixed schedule regardless of whether a fault is present. Common triggers include:

- Monthly, quarterly, or annual maintenance schedule issued by the IT department
- Manufacturer's recommended service interval for hardware components
- Organisational policy requiring regular software and firmware updates

For PM, the technician needs to identify:
- Which systems are due for service (from the maintenance schedule)
- What the standard PM checklist covers (hardware cleaning, software updates, backup verification)
- Which consumables are required (compressed air, thermal paste, cleaning cloths)

### 3.2 Corrective Maintenance Requirements

Corrective maintenance is triggered by a reported fault or system failure. The technician must:

1. Review the problem description on the request form
2. Gather additional information from the user (when did it start? what changed recently?)
3. Identify whether the fault is hardware-related, software-related, or both
4. Determine whether the system can be taken offline or must remain in service during diagnosis

### 3.3 Predictive Maintenance Requirements

Predictive maintenance is triggered by monitoring data indicating that a component is approaching failure. Examples include:

- S.M.A.R.T. (Self-Monitoring, Analysis and Reporting Technology) data showing reallocated sectors on a hard disk drive
- CPU or GPU temperature logs consistently exceeding safe operating thresholds
- UPS (Uninterruptible Power Supply) battery capacity falling below 80%

---

## 4.0 Identifying Required Tools and Materials

After classifying the maintenance type, the technician prepares the appropriate tools and materials. Using incorrect or inadequate tools can damage components or cause injury.

| Tool / Material | Malay Term | Use |
|----------------|-----------|-----|
| Phillips head screwdriver (PH1, PH2) | Pemutar skru Philip | Removing and securing chassis screws |
| Anti-static wrist strap | Tali pergelangan anti-statik | Prevents electrostatic discharge (ESD) damage to components |
| Compressed air canister | Bekas udara termampat | Blowing dust from heatsinks, fans, and vents |
| Vacuum cleaner (low-voltage) | Penyedut habuk | Removing dust from the work area |
| Thermal paste | Pes haba | Re-applying CPU heatsink compound |
| Isopropyl alcohol (IPA 70–99%) | Alkohol isopropil | Cleaning contacts, removing old thermal paste |
| Lint-free cloth / cotton swab | Kain bebas serabut / swab kapas | Applying IPA without leaving residue |
| Multimeter | Multimeter | Checking power supply output voltages |
| USB bootable diagnostic drive | Pemacu USB diagnostik | Running hardware tests (Memtest86, CrystalDiskInfo) |
| Maintenance log / checklist form | Borang senarai semak penyelenggaraan | Recording all actions taken |

---

## 5.0 Safety and Environmental Precautions

Computer maintenance involves electrical equipment and chemical cleaning agents. The following precautions must be observed:

- **Power down and unplug** the computer before opening the chassis. For corrective maintenance requiring live diagnosis, use appropriate insulated tools and avoid contact with powered components.
- **Wear an anti-static wrist strap** connected to an earthed point before handling any internal component.
- **Handle components by the edges.** Never touch circuit board traces, processor pins, or RAM gold contacts with bare fingers.
- **Use compressed air in a ventilated area.** Dust dislodged from computers can contain fine particulates harmful when inhaled.
- **Dispose of consumables correctly.** Thermal paste, cleaning cloths, and old batteries must be disposed of in accordance with the organisation's waste management policy and applicable environmental regulations.
- **Label and isolate** any system taken out of service for corrective maintenance to prevent accidental use.

---

## 6.0 Documenting Identified Requirements

The final step before commencing work is to record the identified requirements in a maintenance checklist (senarai semak penyelenggaraan). This document serves as both a work guide during the maintenance activity and an evidence record upon completion.

A maintenance checklist should include:

| Section | Content |
|---------|---------|
| System identification | Asset tag, make/model, location |
| Maintenance type | Preventive / Corrective / Predictive |
| Scope of work | List of specific tasks to be performed |
| Required tools and materials | Items confirmed as available and serviceable |
| Safety notes | Specific hazards identified for this system |
| Technician name | Person responsible for the maintenance |
| Estimated time | Expected duration |
| Sign-off fields | Technician and supervisor signature upon completion |

---

## 7.0 Common Errors in Requirements Identification

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Skipping the request form; proceeding from verbal instruction only | Wrong scope of work; no audit trail | Always obtain a written or ticketed request before starting |
| Misclassifying corrective maintenance as preventive | Fault left unresolved; new problems introduced | Confirm with the user whether a fault is present |
| Not checking the asset tag against the maintenance schedule | Maintaining the wrong unit | Cross-check asset tag on the form against the physical label |
| Omitting required tools from the toolkit | Work interrupted; technician must leave the work area | Use a pre-departure checklist to verify all tools are present |
| Failing to document identified requirements | Scope creep; disputes about what was agreed | Complete the checklist before starting work, not after |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCU 2: Computer System Maintenance
- Jennifer's verified WIM reference: IT-020-3:2013-C02/P(1/16)
- CompTIA A+ Core 1 (220-1101) and Core 2 (220-1102) — Maintenance and Troubleshooting domains
- Organisational IT maintenance policy and asset management procedures