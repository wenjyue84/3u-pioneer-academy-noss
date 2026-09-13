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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C06 COMPUTER SYSTEM MAINTENANCE MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE COMPUTER SYSTEM MAINTENANCE REQUIREMENTS<br>2. DEVELOP COMPUTER SYSTEM MAINTENANCE PLAN<br>3. MANAGE COMPUTER SYSTEM MAINTENANCE WORK<br>4. MANAGE COMPUTER SYSTEM TROUBLESHOOTING ISSUES/FAILURES<br>5. PRODUCE COMPUTER SYSTEM MAINTENANCE MANAGEMENT REPORT |
| NO. KOD | IT-020-4:2013-C06/KP(2/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-02-maintenance-plan-development

**TUJUAN:** Kertas rujukan untuk KP-02-maintenance-plan-development.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Develop a comprehensive computer system maintenance plan from a requirements analysis
2. Define maintenance schedules, frequency, and resource requirements for all asset classes
3. Prepare preventive maintenance checklists and standard operating procedures
4. Establish a maintenance calendar aligned with SLA and operational constraints
5. Obtain stakeholder approval and communicate the plan to the maintenance team

---

## 1.0 Purpose of a Maintenance Plan

A Computer System Maintenance Plan (Pelan Penyelenggaraan Sistem Komputer) is a formal, approved document that specifies:

- What maintenance activities will be performed
- When each activity will be performed (schedule and frequency)
- Who is responsible for each activity (roles and assignments)
- What resources (tools, spare parts, budget) are required
- How the activity will be performed (referenced procedures or SOPs)
- How completion will be verified and recorded

The maintenance plan transforms the findings of the Maintenance Requirements Analysis (KP-01) into an actionable operational schedule. Without a plan, maintenance activities become reactive, ad hoc, and difficult to audit or improve.

---

## 2.0 Structure of a Computer System Maintenance Plan

A complete maintenance plan contains the following sections:

| Section | Content |
|---------|---------|
| 1. Scope | Assets, locations, and systems covered by the plan |
| 2. Objectives | Uptime targets, SLA obligations, maintenance goals |
| 3. Maintenance Strategy | PM/PdM/CBM approach; rationale |
| 4. Asset Register | Full inventory with criticality, age, and maintenance history |
| 5. Maintenance Schedule | Calendar view of all scheduled activities |
| 6. Task Descriptions | SOP reference for each maintenance activity |
| 7. Resource Plan | Staffing, tools, spare parts, contractor engagement |
| 8. Budget | Estimated cost of all planned activities |
| 9. KPI and Reporting | Metrics to be tracked; reporting frequency and format |
| 10. Review and Update | Plan review schedule (typically annual or after major incidents) |

---

## 3.0 Developing the Maintenance Schedule

### 3.1 Schedule Frequency Determination

Maintenance frequency is determined by:

- Manufacturer-recommended intervals (from technical manuals)
- Failure history (higher MTBF = less frequent PM needed)
- Criticality tier (Tier 1 assets receive more frequent maintenance)
- SLA obligations (PM must not exceed permitted downtime)
- Regulatory requirements (if applicable — e.g. government data centre standards)

| Asset Class | Recommended PM Frequency | Key Activities |
|-------------|--------------------------|----------------|
| Servers (mission-critical) | Monthly physical check; quarterly full PM | Dust removal, fan inspection, thermal paste check, firmware update, RAID health check, UPS battery test |
| Desktop workstations | Semi-annual | Dust removal, hardware diagnostic, OS health check, software update |
| Network switches and routers | Quarterly | Firmware update, port inspection, log review, cable management |
| UPS and power protection | Monthly battery test; annual full inspection | Battery capacity, charge time, load test |
| Printers and peripherals | Semi-annual | Roller cleaning, firmware update, consumable levels |

### 3.2 Maintenance Window Planning

A maintenance window (tetingkap penyelenggaraan) is a pre-approved period during which disruptive maintenance activities may be performed. The maintenance manager must:

1. Identify operational periods when systems cannot be taken offline (e.g. month-end financial processing, public examination periods)
2. Negotiate maintenance windows with business unit managers
3. Publish the agreed windows in the maintenance calendar
4. Ensure all planned disruptive activities fall within approved windows

| Window Type | Typical Schedule | Suitable For |
|-------------|-----------------|--------------|
| Standard | Weekly, Saturday 01:00–05:00 | Patch application, minor hardware checks |
| Extended | Monthly, last Sunday 22:00–06:00 | Firmware updates, RAID rebuilds, full server PM |
| Emergency | As required (< 4 hours notice) | Critical fault response only |

### 3.3 Maintenance Calendar Format

The maintenance calendar is typically presented as a 12-month Gantt-style chart:

| Asset | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|-------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Server farm (full PM) | ✓ | | | ✓ | | | ✓ | | | ✓ | | |
| Server farm (monthly check) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Desktop workstations | ✓ | | | | | ✓ | | | | | | ✓ |
| Network devices | | ✓ | | | ✓ | | | ✓ | | | ✓ | |
| UPS systems | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

---

## 4.0 Standard Operating Procedures (SOP) for Maintenance Tasks

Each maintenance activity in the plan must be supported by a written SOP (Prosedur Operasi Standard). The SOP specifies:

1. **Purpose:** What the procedure achieves
2. **Scope:** Which assets and systems are covered
3. **Prerequisites:** Tools, parts, access rights, and approvals needed before starting
4. **Safety precautions:** ESD, electrical isolation, data backup requirements
5. **Step-by-step procedure:** Numbered actions with decision points
6. **Acceptance criteria:** How to confirm the task was completed successfully
7. **Documentation:** What to record and where

SOPs must be version-controlled, approved by the IT Manager, and accessible to all maintenance technicians.

---

## 5.0 Resource Planning

### 5.1 Staffing Plan

| Role | Responsibility |
|------|----------------|
| Maintenance Manager (L4) | Plan development, resource allocation, contractor management, reporting |
| Senior Technician | Complex PM tasks, mentoring, SOP execution for Tier 1 assets |
| Technician (L3) | Routine PM tasks, helpdesk escalation, basic troubleshooting |
| On-call Technician | After-hours response for critical faults |

### 5.2 Spare Parts Inventory

A maintenance plan must specify a minimum spare parts holding:

| Part | Minimum Stock | Justification |
|------|---------------|---------------|
| Server RAM modules | 4 units | High failure risk; replacement required within SLA window |
| SSD/HDD (server grade) | 2 units per RAID set | RAID rebuild must begin within 24 hours of drive failure |
| Network switch (managed, equivalent spec) | 1 unit | Hot standby for mission-critical switches |
| UPS batteries | 2 sets | Battery replacement is time-critical for power protection |
| Power supply units (server) | 1 per server model | PSU failure is common and time-sensitive |

### 5.3 Budget Estimation

| Cost Category | Estimation Basis |
|---------------|-----------------|
| Labour (internal) | Technician hours × hourly rate × planned tasks |
| Spare parts | Spare parts inventory value + estimated consumption |
| Contractor services | Quoted rates × service visits planned |
| Software licences | Renewal costs for monitoring, antivirus, backup tools |
| Training | Upskilling for new technologies in the environment |

---

## 6.0 Plan Approval and Communication

The completed maintenance plan must be:

1. **Reviewed** by the IT Manager and relevant business unit representatives
2. **Approved** formally by the organisation's management (signed and dated)
3. **Communicated** to all maintenance technicians — via team briefing, intranet, or printed distribution
4. **Filed** in the IT management document register with version control

The plan must also include a **change management clause** specifying how changes to the plan are proposed, reviewed, and approved during the plan period.

---

## 7.0 Plan Review and Continuous Improvement

The maintenance plan is a living document. It must be reviewed:

- **Annually** as part of the IT planning cycle
- **After a major incident** to incorporate lessons learned
- **When significant new assets are added** to the environment
- **When SLA terms change**

Review findings are recorded in the maintenance log and incorporated into the next plan revision.

---

## Rujukan / References

- NOSS IT-020-4:2013 Computer Systems Administration — CoCU 6
- ISO 55001:2014 Asset Management — Requirements
- ITIL 4 — Problem Management and Continual Improvement practices
- British Standard BS EN 13306:2017 — Maintenance Terminology
- Jabatan Perkhidmatan Awam Malaysia — Pekeliling ICT Bil. 1/2013