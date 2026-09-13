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
| NO. KOD | IT-020-4:2013-C06/KP(3/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-03-maintenance-work-management

**TUJUAN:** Kertas rujukan untuk KP-03-maintenance-work-management.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Coordinate and direct a team of maintenance technicians in executing the maintenance plan
2. Apply work order management principles to control, track, and close maintenance tasks
3. Manage internal and external (contractor) maintenance resources effectively
4. Monitor maintenance work in progress and intervene when quality or schedule deviates
5. Ensure all completed maintenance activities are correctly documented

---

## 1.0 The Maintenance Manager's Operational Role

While the Level 3 technician executes maintenance tasks, the Level 4 maintenance manager's role is to orchestrate the work — assigning tasks, monitoring progress, resolving resource conflicts, managing contractors, and ensuring quality. This is a supervisory and administrative function requiring both technical knowledge and management skills.

The maintenance manager operates at the intersection of:

- The maintenance plan (what must be done and when)
- The team (who does the work and how)
- The organisation (SLA obligations, budget, safety compliance)
- The technology (understanding what the technicians are doing and why)

---

## 2.0 Work Order Management

A work order (Pesanan Kerja) is the formal instruction that authorises and tracks a specific maintenance activity. All maintenance work — planned or unplanned — should be governed by a work order.

### 2.1 Work Order Lifecycle

```
Raised → Assigned → In Progress → Completed → Verified → Closed
```

| Stage | Description | Responsible Party |
|-------|-------------|-------------------|
| Raised | Work order created (from schedule, helpdesk ticket, or incident) | Maintenance Manager / System |
| Assigned | Technician and schedule confirmed | Maintenance Manager |
| In Progress | Technician executes the task | Technician |
| Completed | Technician marks task done and submits documentation | Technician |
| Verified | Manager reviews work quality and documentation | Maintenance Manager |
| Closed | Work order formally closed in CMMS | Maintenance Manager |

### 2.2 Work Order Contents

| Field | Description |
|-------|-------------|
| Work order number | Unique reference (e.g. WO-2026-0412) |
| Asset ID | System or device the work is performed on |
| Maintenance type | PM / CM / PdM / Emergency |
| Description | What needs to be done |
| Priority | P1 (Critical) to P4 (Routine) |
| Assigned technician | Name and role |
| Scheduled date/time | Planned start and completion |
| SOP reference | Procedure to be followed |
| Parts required | Spare parts to be drawn from inventory |
| Safety precautions | Applicable safety requirements |
| Completion notes | Technician's findings and actions taken |
| Time spent | Actual hours worked |
| Sign-off | Technician and manager signatures |

### 2.3 Computerised Maintenance Management System (CMMS)

In a well-managed IT department, work orders are managed through a CMMS (Sistem Pengurusan Penyelenggaraan Berkomputer) or IT Service Management (ITSM) tool such as ServiceNow, Freshservice, or JIRA Service Management. Key CMMS functions:

- Automatic generation of scheduled PM work orders
- Real-time work order status tracking
- Spare parts inventory management
- Maintenance history recording per asset
- KPI reporting and dashboard
- Escalation alerts for overdue work orders

---

## 3.0 Team Management in Maintenance Operations

### 3.1 Task Assignment

When assigning maintenance tasks, the manager considers:

- **Competency match:** Is the technician qualified and experienced for this task?
- **Workload balance:** Is the technician available, or already overloaded?
- **Geographical proximity:** Is the technician near the asset location?
- **Urgency:** For P1/P2 tasks, assign immediately without waiting for shift schedules

### 3.2 Briefing Technicians

Before each maintenance session, the manager should brief the assigned technician(s):

1. Review the work order objectives and scope
2. Confirm SOP to be followed
3. Review safety requirements for the specific task
4. Confirm spare parts and tools are available
5. Establish communication protocol during the work (e.g. check-in every 30 minutes for critical systems)
6. Clarify escalation trigger — when to call the manager

### 3.3 Monitoring Work in Progress

The manager monitors maintenance work through:

- Regular check-ins with technicians (by phone, radio, or CMMS update)
- Review of intermediate milestones (e.g. system taken offline, backup verified before proceeding)
- On-site supervision for complex or high-risk activities
- CMMS dashboard for real-time work order status

### 3.4 Handling Work Deviations

When a technician encounters a situation not covered by the SOP:

| Situation | Manager Action |
|-----------|---------------|
| Unexpected fault discovered during PM | Log as new work order; assess priority; decide to fix now or schedule |
| Required spare part not available | Source emergency procurement; escalate if P1/P2; defer if P3/P4 |
| Work taking longer than planned | Reassess impact on other scheduled work; adjust schedule; notify stakeholders if SLA at risk |
| Safety concern identified | Stop work immediately; secure the area; escalate to safety officer |

---

## 4.0 Contractor Management

Many organisations engage external vendors or contractors for specialised maintenance activities (e.g. UPS servicing, air-conditioning maintenance for server rooms, hardware warranty repairs). The maintenance manager is responsible for managing these relationships.

### 4.1 Contractor Engagement Process

1. **Scope of work definition:** Prepare a clear written scope of work (SOW) for the contractor
2. **Vendor selection:** Evaluate vendors based on competency, certifications, price, and track record
3. **Contract / Purchase Order:** Ensure a signed contract or PO is in place before work begins
4. **Induction:** Brief the contractor on site safety rules, access procedures, and documentation requirements
5. **Supervision:** Assign an internal technician to accompany and supervise the contractor
6. **Acceptance:** Verify and sign off completed work against the SOW
7. **Performance review:** Record contractor performance for future procurement decisions

### 4.2 Contractor Control Points

| Control Point | Purpose |
|---------------|---------|
| Site access authorisation | Prevent unauthorised access to server rooms and sensitive areas |
| Work permit (for high-risk activities) | Formal approval before carrying out electrical or equipment isolation work |
| Data security undertaking | Ensure contractor personnel understand data confidentiality obligations |
| Insurance verification | Confirm contractor holds valid public liability and professional indemnity insurance |

---

## 5.0 Escalation Management

The maintenance manager establishes an escalation matrix so that the team knows exactly when and to whom to escalate:

| Scenario | Escalation Level | Action |
|----------|-----------------|--------|
| Maintenance task cannot be completed within scheduled window | Manager | Extend window or reschedule; notify affected users |
| System failure during PM (induced fault) | Manager → IT Manager | Initiate incident response; prioritise restoration |
| Contractor fails to deliver on schedule | Manager → Procurement | Issue formal notice; activate backup vendor |
| Safety incident during maintenance | Manager → Safety Officer → Senior Management | Stop all work; initiate incident report |

---

## 6.0 Quality Assurance for Completed Maintenance

Before closing a work order, the maintenance manager verifies:

- Work was performed as per the SOP
- System functionality was tested and confirmed after maintenance
- All pre-maintenance backups were verified
- Documentation is complete, accurate, and signed
- Spare parts used are correctly recorded in inventory
- Any findings or deviations are noted in the work order

---

## Rujukan / References

- NOSS IT-020-4:2013 Computer Systems Administration — CoCU 6
- ITIL 4 — Change Enablement and Service Request Management
- ISO 9001:2015 Quality Management Systems — Requirements
- Microsoft System Center / ServiceNow ITSM documentation
- Jabatan Perkhidmatan Awam Malaysia — Pekeliling Perkhidmatan ICT