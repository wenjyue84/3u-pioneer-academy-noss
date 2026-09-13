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
| NO. KOD | IT-020-4:2013-C04/KP(5/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-05-cabling-change-documentation

**TUJUAN:** Kertas rujukan untuk KP-05-cabling-change-documentation.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the change management process (proses pengurusan perubahan) as applied to network cabling
2. Complete a cabling change request form and obtain the required approvals
3. Update cable records, as-built drawings, and labelling following a change
4. Produce a change completion report that satisfies internal audit requirements
5. Identify the consequences of undocumented cabling changes

---

## 1.0 The Need for Change Documentation

Network cabling changes occur frequently during the operational life of a building: new workstations are added, offices are reorganised, equipment is upgraded, or cables are repaired after faults. Without formal documentation of these changes:

- As-built drawings become inaccurate — future technicians work from wrong information
- Cable records no longer reflect the actual installation
- Fault-finding becomes very difficult (the wrong cable may be identified)
- Warranty claims may be invalidated (manufacturer warranties require all changes to be documented and performed by qualified installers)
- Regulatory audits identify an uncontrolled infrastructure

Documenting changes is therefore not optional — it is a fundamental part of the cabling administrator's duty of care.

---

## 2.0 Types of Cabling Changes

| Change Type | Malay Term | Description |
|-------------|------------|-------------|
| Move (Pindah) | Pindah | An existing cable or device is relocated to a different position |
| Add (Tambah) | Tambah | New cables or outlets are installed |
| Change (Ubah) | Ubah | An existing cable or component is replaced with a different specification |
| Remove / Decommission (Buang) | Nyahaktifkan | A cable or outlet is taken out of service |
| Repair (Baiki) | Baiki | A damaged cable or connector is repaired or replaced |

Each type requires a different set of documentation actions, but all require a change request before work begins.

---

## 3.0 Change Management Process

### 3.1 Step-by-Step Process

| Step | Action | Responsible Party |
|------|--------|-------------------|
| 1 | Identify the need for a change | Requestor (user, network admin, facilities) |
| 2 | Complete a Cabling Change Request Form | Requestor |
| 3 | Review and approve the change (technical and budget) | IT administrator + department head |
| 4 | Schedule the change (time, duration, affected users) | IT administrator + facilities manager |
| 5 | Execute the change — install, terminate, label | Qualified installer / IT team |
| 6 | Test the changed link (certification or link test) | IT administrator |
| 7 | Update cable records, port assignment records | IT administrator |
| 8 | Update as-built drawings (revision increment) | Drafter / IT administrator |
| 9 | Update physical labels if outlet IDs change | Installer |
| 10 | Complete the Change Completion Report | IT administrator |
| 11 | File all documentation (change request, test result, report) | IT administrator |

### 3.2 Emergency Changes

In rare cases, a cabling change may need to be performed urgently (e.g. a critical cable is damaged and must be repaired immediately). Emergency change procedure:

1. Obtain verbal or email approval from the IT manager before work begins
2. Execute the minimum change needed to restore service
3. Complete full documentation (change form, test result, record update) within 24 hours of the emergency change
4. Review at next change management meeting

---

## 4.0 Cabling Change Request Form

Every cabling change must be initiated with a completed Cabling Change Request Form:

| Field | Content Required |
|-------|-----------------|
| Change request number | Sequential unique number (e.g. CCR-2026-001) |
| Date requested | |
| Requested by | Name, department, contact |
| Change type | Move / Add / Change / Remove / Repair |
| Description of change | What needs to be done and why |
| Cables / outlets affected | List of cable IDs and outlet IDs affected |
| Impact assessment | Will any service be interrupted? Duration? Who is affected? |
| Technical specification | Cable type, connector, labelling convention to be used |
| Estimated cost | Labour + materials |
| Priority | Routine / Urgent / Emergency |
| Approved by | IT manager signature + date |
| Scheduled date/time | |

---

## 5.0 Updating Records After a Change

### 5.1 Cable Schedule Update

For every cable that is added, moved, or decommissioned:
- Add a new row (for adds) with all required fields
- Update the status column (Active / Spare / Decommissioned)
- Update the length, origin, destination, and test result fields as applicable
- Record the change request number in the Notes field for traceability

### 5.2 As-Built Drawing Update

| Change Type | Drawing Update Required |
|-------------|------------------------|
| Add new outlet | Add outlet symbol to floor plan; add cable run line; update cable count in title block |
| Move outlet | Update outlet position on floor plan; update cable run origin/destination |
| Add patch panel | Update TR elevation drawing; add port assignments |
| Backbone change | Update backbone schematic |
| Any change | Increment drawing revision (Rev B → Rev C); update revision table with date and description |

All drawing updates must be completed within **5 working days** of the physical change. Updated drawings must be stored in the shared document repository and the superseded revision moved to the archive folder.

### 5.3 Label Updates

If a cable ID, outlet ID, or patch panel port assignment changes:
- Print new machine-generated labels
- Physically replace the old labels at both ends of the cable
- Replace the patch panel port label
- Replace the faceplate outlet label
- Dispose of the old labels — do not leave old labels alongside new ones

---

## 6.0 Change Completion Report (Laporan Penyiapan Perubahan)

After all work is done and records are updated, the IT administrator completes a Change Completion Report:

| Section | Content |
|---------|---------|
| Change request reference | CCR number cross-reference |
| Summary of work performed | What was physically done |
| Cables installed / removed | List of cable IDs with before/after status |
| Test results | Pass/Fail per cable; attach certification report |
| Records updated | Confirm cable schedule, port assignment, drawing revision updated |
| Labels updated | Confirm all labels replaced where required |
| Completed by | Name, signature, date |
| Verified by | IT manager or supervisor name, signature, date |

The completed report is filed with the original change request form and test results in the project change management folder.

---

## 7.0 Change Log

A change log provides a chronological summary of all changes made to the cabling infrastructure. It is the "history" of the installation after practical completion:

| Field | Example |
|-------|---------|
| CCR number | CCR-2026-007 |
| Date completed | 15 Jun 2026 |
| Change type | Add |
| Description | 4 new outlets added in Room B1-108 (new staff) |
| Cables added | HC-B1-01-049 to HC-B1-01-052 |
| Drawing revision | Rev D |
| Completed by | Ahmad bin Rashid |

The change log is appended to the cable records folder and reviewed during periodic audits.

---

## 8.0 Consequences of Undocumented Changes

| Undocumented Change | Consequence |
|--------------------|-------------|
| Cable added without record | Next expansion cannot reuse spare capacity correctly; may exceed conduit fill |
| Outlet moved without drawing update | Floor plan shows outlet in old location; technician connects wrong outlet during fault-find |
| Label not replaced after move | Two cables with same label → cannot distinguish them during fault |
| As-built not revised | Installation effectively undocumented — all benefits of record-keeping lost |
| No change request approval | Unauthorised work; no budget tracking; no impact assessment → unplanned outage possible |

---

## 9.0 Common Errors in Cabling Change Documentation

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Performing work before change request is approved | Unauthorised changes; no impact assessment; possible outage | Enforce mandatory approval before any physical work |
| Updating records days or weeks after the change | Records temporarily incorrect; risk of a second change being based on wrong info | Set a policy: records updated same day or next working day |
| Not filing test results with the change record | Cannot prove the link was certified after the change | Attach test result PDF to every change completion report |
| Using verbal instructions only | No paper trail; disputes over what was agreed | All changes documented; verbal instructions followed up in writing |
| Incrementing drawing revision without updating revision table | Confusing revision history; audit failure | Always update revision table with date, description, and drafter |

---

## Rujukan / References

- ANSI/TIA-606-B: Administration Standard for Telecommunications Infrastructure
- ISO/IEC 14763-2: Implementation and Operation of Customer Premises Cabling — Planning and Installation
- ITIL Service Transition — Change Management Process (reference framework)
- BICSI TDMM (Telecommunications Distribution Methods Manual), 14th Edition
- NOSS IT-020-4:2013 Computer Systems Administration — CoCu 4: Network Cabling Management