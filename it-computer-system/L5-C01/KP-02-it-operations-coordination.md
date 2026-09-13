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
| KOD DAN NAMA PROGRAM | IT-020-5:2013 PENGURUSAN SISTEM KOMPUTER |
| TAHAP | 5 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-C01 COMPUTER SYSTEMS PLANNING AND OPERATIONS MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. PLAN RESOURCES<br>2. COORDINATE OPERATIONS<br>3. MONITOR PERFORMANCE<br>4. REPORT TO MANAGEMENT |
| NO. KOD | IT-020-5:2013-C01/KP(2/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-02-it-operations-coordination

**TUJUAN:** Kertas rujukan untuk KP-02-it-operations-coordination.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Describe the roles, responsibilities, and interfaces between IT operations teams, user communities, and external vendors.
2. Apply ITIL Service Operation principles to coordinate incident, problem, change, and request fulfilment processes.
3. Develop and manage Service Level Agreements (SLAs) and Operational Level Agreements (OLAs) as coordination instruments.
4. Manage vendor relationships through structured governance including contract management, performance review, and escalation.
5. Design communication plans that ensure effective information flow across IT, users, and vendors.

---

## 1.0 Introduction to IT Operations Coordination

IT Operations Coordination (Penyelarasan Operasi IT) refers to the management discipline of orchestrating the activities of multiple parties — internal IT teams, end-users, and external service providers — to deliver consistent, reliable IT services. At Level 5, the IT Manager functions as the primary coordination authority, responsible for defining interfaces between teams, enforcing service commitments, and resolving cross-party conflicts.

Coordination is not merely reactive (resolving incidents when they occur) but also proactive — establishing the structures, agreements, and communication channels that prevent misalignment before it becomes a service disruption.

---

## 2.0 Organisational Roles in IT Operations

### 2.1 Internal IT Structure

| Role | Function | Coordination Responsibility |
|------|----------|---------------------------|
| IT Manager (Level 5) | Strategic and operational oversight of all IT services | Primary coordinator between IT, users, and vendors; accountable for SLA compliance |
| System Administrator | Day-to-day server, network, and infrastructure management | Escalation point from L1/L2 support; vendor interface for infrastructure issues |
| Service Desk (Helpdesk) | First point of contact (SPOC) for user requests and incidents | Logs, categorises, and routes all tickets; communicates status to users |
| Network Engineer | Manages LAN, WAN, Wi-Fi, and security infrastructure | Coordinates with ISP and network equipment vendors |
| Security Officer | Manages information security policies and controls | Coordinates vulnerability responses; interfaces with security vendors |
| Database Administrator | Manages organisational databases | Coordinates with application vendors and backup systems |

### 2.2 User Community

Users (end-users / pengguna akhir) are the consumers of IT services. Effective coordination with users requires:

- A clearly defined **Service Request process** (Proses Permintaan Perkhidmatan) so users know how to request new services, changes, or support.
- A published **Service Catalogue** (Katalog Perkhidmatan) describing available IT services, response times, and eligibility.
- Regular **user satisfaction surveys** (minimum annually) to identify service gaps.
- **User communication protocols** for planned maintenance windows, major incidents, and system changes.

### 2.3 Vendor and Third-Party Providers

| Vendor Category | Examples | Coordination Mechanism |
|----------------|---------|----------------------|
| Hardware OEM | Dell, HP, Lenovo, Cisco | Annual Maintenance Contract (AMC); vendor escalation contacts |
| Software vendor | Microsoft, Oracle, SAP | Licence management; technical support portal; version update planning |
| Internet Service Provider (ISP) | Telekom Malaysia, Maxis, TIME | ISP SLA; fault reporting hotline; peering and bandwidth upgrade requests |
| Cloud service provider | AWS, Microsoft Azure, Google Cloud | Cloud support tier (Basic/Business/Enterprise); billing governance |
| Managed service provider (MSP) | Outsourced IT management | MSP SLA; monthly service review meeting; RACI matrix |
| Security vendor | Fortinet, Palo Alto, CrowdStrike | Threat intelligence updates; incident response support |

---

## 3.0 ITIL Service Operation Processes

ITIL Service Operation provides a structured framework for day-to-day coordination. The five key processes are:

### 3.1 Incident Management (Pengurusan Insiden)

An incident is any unplanned interruption or reduction in quality of an IT service. The Incident Management process restores normal service operation as quickly as possible.

| Stage | Activities |
|-------|-----------|
| Detection and logging | User reports incident via service desk; incident ticket created with category, priority, and initial description |
| Categorisation and prioritisation | Classify by service affected and business impact; assign priority (P1–P4) based on urgency × impact matrix |
| Investigation and diagnosis | L1 service desk attempts first-contact resolution; escalate to L2/L3 if unresolved within time target |
| Resolution and recovery | Apply fix; verify service restored; update ticket |
| Closure | Confirm resolution with user; close ticket; update known-error database if applicable |

**Priority Matrix:**

| Impact \ Urgency | High | Medium | Low |
|-----------------|------|--------|-----|
| High | P1 (Critical) — 1 hr | P2 (High) — 4 hrs | P3 (Medium) — 8 hrs |
| Medium | P2 (High) — 4 hrs | P3 (Medium) — 8 hrs | P4 (Low) — 24 hrs |
| Low | P3 (Medium) — 8 hrs | P4 (Low) — 24 hrs | P4 (Low) — 48 hrs |

### 3.2 Problem Management (Pengurusan Masalah)

Problem Management identifies and eliminates the root causes of recurring incidents. A Problem Record is raised when:
- The same incident recurs three or more times within 30 days.
- A Major Incident (P1) has been resolved and root cause analysis (RCA) is required.

Root cause analysis methods used at Level 5 include:
- **5 Whys** — iterative questioning to reach the root cause
- **Fishbone / Ishikawa diagram** — categorising causes (People, Process, Technology, Environment)
- **Fault tree analysis** — structured diagram of cause-and-effect chains

### 3.3 Change Management (Pengurusan Perubahan)

All changes to the IT production environment must pass through Change Management to minimise risk of service disruption.

| Change Type | Definition | Approval Required |
|------------|-----------|------------------|
| Standard change | Pre-approved, low-risk, frequently repeated (e.g., user account creation) | No CAB approval needed; follows pre-defined procedure |
| Normal change | Requires assessment and approval (e.g., server OS upgrade) | Change Advisory Board (CAB) review; IT Manager approval |
| Emergency change | Urgent fix to restore service or prevent critical failure | ECAB (Emergency CAB) approval; post-implementation review mandatory |

### 3.4 Request Fulfilment (Pemenuhan Permintaan)

Service requests (Permintaan Perkhidmatan) are user requests for standard services — new user account, software installation, password reset. Request Fulfilment manages these through a defined workflow with:
- Agreed fulfilment times per request type (published in the Service Catalogue)
- Approval gates for requests above a cost or access threshold
- Automated workflows in the ITSM platform for common request types

### 3.5 Event Management (Pengurusan Peristiwa)

Events are changes of state in the IT environment detected by monitoring tools (e.g., CPU threshold breached, disk space warning, service health check failure). Event Management:
- Filters events into: informational, warning, or exception
- Routes exception events to Incident Management automatically
- Provides audit trail for compliance and post-incident review

---

## 4.0 Service Level Agreements and Operational Level Agreements

### 4.1 Service Level Agreement (SLA)

An SLA is a formal agreement between the IT department (or service provider) and the user/customer defining the expected level of service. Key SLA components:

| Component | Description |
|-----------|-------------|
| Service scope | What services are covered; what is excluded |
| Service hours | When the service is available (e.g., 8 AM–6 PM weekdays; 24×7 for critical systems) |
| Availability target | Minimum uptime percentage (e.g., 99.5% per month) |
| Performance targets | Response time, throughput, or transaction success rate targets |
| Incident response times | Time-to-respond and time-to-resolve by priority level |
| Reporting | Frequency and format of SLA compliance reports |
| Review and revision | How the SLA is reviewed and updated |
| Penalties and remedies | Financial penalties or service credits for SLA breaches |

### 4.2 Operational Level Agreement (OLA)

An OLA is an internal agreement between IT teams that supports the delivery of the SLA. For example:
- The Service Desk commits to resolving P4 tickets within 24 hours (SLA).
- The Network team commits to responding to Service Desk escalation within 2 hours (OLA).
- The server team commits to restoring a failed VM within 4 hours (OLA).

OLAs ensure each IT sub-team understands their specific contribution to the overall service commitment.

### 4.3 Underpinning Contract (UC)

A UC is an agreement with an external vendor that supports the IT department's ability to meet its SLA. For example, the hardware AMC must commit to on-site engineer response within 4 hours if the SLA requires server restoration within 8 hours.

---

## 5.0 Vendor Relationship Management

### 5.1 Vendor Governance Framework

| Governance Element | Frequency | Participants |
|-------------------|-----------|-------------|
| Monthly performance review | Monthly | IT Manager, vendor account manager; review SLA metrics, open tickets, upcoming renewals |
| Quarterly business review (QBR) | Quarterly | Senior IT management, vendor senior management; review strategic alignment, roadmap, and pricing |
| Contract renewal assessment | 6 months before expiry | IT Manager, Procurement; assess vendor performance, market alternatives, renewal terms |
| Escalation matrix | As needed | Defined escalation path from operational contact → account manager → regional director |

### 5.2 Vendor Performance Scorecard

Vendors are evaluated on a regular scorecard covering:

| KPI | Measurement |
|-----|------------|
| SLA compliance rate | Percentage of incidents resolved within contracted SLA time |
| First-time fix rate | Percentage of issues resolved without requiring a second visit or call |
| Change success rate | Percentage of vendor-executed changes that were implemented without incident |
| Response to escalations | Average time to respond to formal escalation |
| Invoice accuracy | Percentage of invoices received without errors |

---

## 6.0 Communication Planning

Effective coordination requires a formal Communication Plan (Pelan Komunikasi) that defines:

| Communication Type | Audience | Channel | Frequency |
|-------------------|---------|---------|-----------|
| IT service status | All users | Intranet portal; email | As required (incidents); planned (maintenance windows) |
| Incident updates | Affected users | Email; ITSM portal notification | Every 30 min for P1; every 2 hrs for P2 |
| Change notifications | Affected departments | Email; IT bulletin | Minimum 5 business days before implementation |
| IT management report | Senior management | Formal report; presentation | Monthly |
| Vendor review meetings | Vendors | Meeting with minutes | Monthly / Quarterly |

---

## 7.0 Common Errors in Operations Coordination

| Error | Consequence | Prevention |
|-------|-------------|------------|
| No single point of contact (SPOC) for users | Users contact individual IT staff directly; incidents logged inconsistently | Enforce all requests through the service desk; communicate SPOC to all users |
| SLA targets not aligned with OLAs | IT sub-teams commit to timelines that cannot meet the SLA | Map each SLA commitment to specific OLA obligations for each team before signing the SLA |
| Vendor SLAs not verified against UC terms | IT promises users a service level that vendors cannot support | Ensure UC response times are stricter than the SLA to provide buffer |
| Poor communication during major incidents | Users receive no updates; management escalates unnecessarily | Activate incident communication plan immediately upon P1 declaration; assign a dedicated communications officer |
| No governance calendar for vendor reviews | Vendor performance issues discovered only at contract renewal | Schedule all vendor review meetings at the start of the financial year and maintain a governance calendar |

---

## Rujukan / References

- NOSS IT-020-5:2013 Computer Systems Management — CoCu 1
- ITIL 4: Service Operation — Axelos (2019)
- ISO/IEC 20000-1:2018 — IT Service Management System Requirements
- Malaysian Digital Economy Corporation (MDEC) — ICT Vendor Management Guidelines
- ISACA COBIT 2019 — DSS01 Managed Operations, DSS02 Managed Service Requests and Incidents
- Microsoft ITPRO: Service Level Agreement Templates and Best Practices