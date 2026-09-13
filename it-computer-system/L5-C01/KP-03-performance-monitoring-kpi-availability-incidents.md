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
| NO. KOD | IT-020-5:2013-C01/KP(3/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-03-performance-monitoring-kpi-availability-incidents

**TUJUAN:** Kertas rujukan untuk KP-03-performance-monitoring-kpi-availability-incidents.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Define and apply key IT performance indicators (KPIs) relevant to systems management at Level 5.
2. Calculate and interpret system availability and reliability metrics including MTTR, MTBF, and uptime percentage.
3. Design an IT monitoring framework that covers infrastructure, services, and security events.
4. Analyse incident trends and identify systemic issues requiring management intervention.
5. Produce a performance dashboard and monitoring report suitable for management review.

---

## 1.0 Introduction to IT Performance Monitoring

IT performance monitoring (Pemantauan Prestasi IT) is the systematic process of collecting, analysing, and reporting on metrics that describe how well IT systems and services are performing relative to agreed targets. At Level 5, performance monitoring is a management function — the IT Manager designs the monitoring framework, defines KPIs, reviews dashboards, and uses performance data to make evidence-based decisions about resource allocation, improvement actions, and escalations.

Performance monitoring serves three purposes:
1. **Operational** — Detect anomalies before they cause service disruption.
2. **Compliance** — Demonstrate SLA adherence to users and management.
3. **Strategic** — Identify trends that inform future capacity and budget planning.

---

## 2.0 Key Performance Indicators (KPIs) for IT Systems Management

### 2.1 KPI Design Principles

A well-designed KPI is **SMART**:

| Attribute | Meaning | Example |
|-----------|---------|---------|
| Specific | Clearly defined; no ambiguity | "Server CPU utilisation" not "server performance" |
| Measurable | Can be quantified and tracked over time | Percentage (%) or count |
| Achievable | Realistic given current infrastructure | 99.5% availability (not 100%) |
| Relevant | Aligned to business outcomes and SLA commitments | Directly linked to a service level target |
| Time-bound | Measured over a defined period | Monthly average; quarterly trend |

### 2.2 Core IT KPIs

| KPI Category | KPI | Definition | Target (Typical) |
|-------------|-----|-----------|-----------------|
| Availability | System availability | Actual uptime as % of scheduled service hours | ≥ 99.5% per month |
| Availability | Mean Time Between Failures (MTBF) | Average time between successive failures | Maximise (higher is better) |
| Availability | Mean Time to Restore (MTTR) | Average time to restore service after a failure | Minimise (lower is better) |
| Incident | Total incidents per month | Number of incidents logged in the period | Track trend; target reduction |
| Incident | First-contact resolution rate (FCR) | Incidents resolved at L1 without escalation | ≥ 70% |
| Incident | SLA breach rate | Percentage of incidents not resolved within SLA target | ≤ 5% |
| Incident | Repeat incidents | Number of incidents with the same root cause | Target zero (via Problem Management) |
| Performance | Server CPU utilisation | Average CPU load across production servers | < 75% peak |
| Performance | Server memory utilisation | Average RAM usage across production servers | < 80% peak |
| Performance | Storage utilisation | Used storage as % of total provisioned capacity | < 80% |
| Performance | Network bandwidth utilisation | Average link utilisation during business hours | < 70% of provisioned bandwidth |
| Service desk | Average resolution time | Average time from ticket open to closure | Per priority class (see SLA) |
| Service desk | User satisfaction score (CSAT) | Post-closure survey rating | ≥ 4.0 / 5.0 |
| Change | Change success rate | Percentage of changes implemented without causing an incident | ≥ 95% |
| Change | Unauthorised change rate | Changes implemented without a valid change record | Target 0% |

---

## 3.0 Availability and Reliability Metrics

### 3.1 System Availability Calculation

Availability is the proportion of time that a service is operational and accessible to users within the agreed service window.

**Formula:**

> Availability (%) = [(Total Service Hours − Downtime Hours) ÷ Total Service Hours] × 100

**Example:**
- Monthly service window: 730 hours (24×7)
- Total downtime in month: 3.5 hours
- Availability = [(730 − 3.5) ÷ 730] × 100 = **99.52%**

**Availability Target Reference:**

| Availability Target | Maximum Allowable Downtime per Month |
|--------------------|-------------------------------------|
| 99.0% | 7.3 hours |
| 99.5% | 3.65 hours |
| 99.9% ("three nines") | 43.8 minutes |
| 99.95% | 21.9 minutes |
| 99.99% ("four nines") | 4.4 minutes |

### 3.2 MTBF — Mean Time Between Failures

MTBF measures the reliability of a system — how long, on average, the system operates before experiencing a failure.

**Formula:**

> MTBF = Total Operating Time ÷ Number of Failures

**Example:** A server operated for 2,160 hours in a quarter and experienced 3 failures.
> MTBF = 2,160 ÷ 3 = **720 hours** (30 days)

A declining MTBF trend signals that a system is becoming less reliable — a trigger for hardware review or replacement planning.

### 3.3 MTTR — Mean Time to Restore Service

MTTR measures the efficiency of the IT team's restoration process.

**Formula:**

> MTTR = Total Downtime ÷ Number of Failures

**Example:** Three failures resulted in total downtime of 6 hours.
> MTTR = 6 ÷ 3 = **2 hours per failure**

A rising MTTR indicates that incidents are taking longer to resolve — which may signal skill gaps, tool deficiencies, or inadequate runbooks.

### 3.4 Availability vs. Reliability

| Metric | What It Measures | Management Use |
|--------|----------------|---------------|
| Availability | Overall service uptime | SLA compliance reporting; user impact |
| MTBF | How often failures occur | Reliability trend; refresh planning |
| MTTR | How quickly failures are resolved | Team efficiency; runbook adequacy |

---

## 4.0 IT Monitoring Framework

### 4.1 Monitoring Layers

A comprehensive monitoring framework covers all layers of the IT stack:

| Layer | What Is Monitored | Tools (Examples) |
|-------|-----------------|-----------------|
| Infrastructure | Server hardware health: CPU, RAM, disk, temperature, fan, PSU | IPMI/iDRAC, Zabbix, PRTG |
| Operating system | OS-level metrics: CPU utilisation, memory, disk I/O, running processes | Zabbix, Nagios, Prometheus |
| Network | Bandwidth utilisation, latency, packet loss, interface errors, routing | PRTG, SolarWinds, Grafana/SNMP |
| Application | Application response time, transaction success rate, error rate, queue depth | APM tools (Dynatrace, AppDynamics, Elastic APM) |
| Database | Query response time, connection pool utilisation, replication lag, deadlocks | MySQL Enterprise Monitor, SQL Server Profiler |
| Security | Failed login attempts, firewall rule violations, intrusion detection alerts | SIEM (Splunk, IBM QRadar, Microsoft Sentinel) |
| Backup | Backup job success/failure, backup duration, recovery point currency | Veeam, Veritas Backup Exec |
| Cloud | Cloud resource utilisation, billing anomalies, service health events | AWS CloudWatch, Azure Monitor |

### 4.2 Monitoring Thresholds and Alert Levels

| Alert Level | Threshold Breach | Action Required |
|------------|----------------|----------------|
| Informational | Minor threshold; no immediate impact | Log and review in next report |
| Warning | Approaching critical threshold | Investigate; no immediate service impact |
| Critical | Service at risk; intervention required | Open incident ticket; notify on-call engineer |
| Emergency | Service has failed or is imminently failing | Declare Major Incident; invoke escalation |

### 4.3 Dashboard Design

An effective monitoring dashboard at management level displays:

| Dashboard Element | Purpose |
|------------------|---------|
| Service health summary | RAG (Red/Amber/Green) status for each critical service |
| Current active incidents | Count and priority of open incidents |
| Availability trend (30-day) | Line chart showing service availability vs. SLA target |
| Capacity utilisation gauges | CPU, RAM, storage, bandwidth — current vs. threshold |
| Top incident categories | Bar chart of incident volume by category (network, server, application, user) |
| Change calendar | Upcoming planned changes that may affect service |

---

## 5.0 Incident Trend Analysis

### 5.1 Why Trend Analysis Matters

Individual incidents are operational events. Trends reveal systemic issues that cannot be resolved by fixing individual incidents. Trend analysis answers:
- Are incidents increasing or decreasing over time?
- Which systems generate the most incidents?
- Which incident categories are most common?
- Are the same users or departments experiencing disproportionate incidents?
- Are incidents linked to a specific change or infrastructure component?

### 5.2 Trend Analysis Methods

| Method | Description | Output |
|--------|-------------|--------|
| Volume trend | Plot total incidents per week/month over 6–12 months | Identify seasonal patterns or deteriorating trends |
| Category breakdown | Classify incidents by type (network, server, application, user error) | Identify highest-impact categories for targeted improvement |
| Repeat incident analysis | Identify incidents with identical root cause | Input to Problem Management for permanent fix |
| Time-to-resolve analysis | Track MTTR by priority over time | Identify whether team efficiency is improving or degrading |
| Top-10 incident sources | Rank systems or services by incident count | Prioritise stability improvement or refresh investment |

### 5.3 Escalation Triggers Based on Performance Data

| Trigger Condition | Action |
|-------------------|--------|
| SLA breach rate > 5% in a month | Issue SLA breach notification; convene improvement review |
| MTTR increasing for 3 consecutive months | Review runbooks, tool availability, and team skill gaps |
| Same root cause incident recurs 3+ times | Raise a Problem Record; assign a Problem Manager |
| Storage utilisation > 80% | Trigger capacity plan review; initiate procurement process |
| Availability drops below SLA target for 2 consecutive months | Escalate to senior management; invoke service improvement plan |

---

## 6.0 Common Errors in Performance Monitoring

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Monitoring infrastructure but not services | Servers appear healthy but users report degraded service experience | Implement end-to-end synthetic monitoring that tests services from a user perspective |
| Setting alert thresholds too low | Alert fatigue — engineers ignore alerts; critical alerts missed | Tune thresholds based on baseline data; separate informational alerts from actionable alerts |
| No trend analysis — only point-in-time reports | Systemic issues not detected until a major failure occurs | Schedule monthly trend review; include 6–12 month trend charts in management reports |
| KPIs not linked to SLA targets | Metrics reported but not connected to service commitments | Map every reported KPI to a specific SLA clause or management objective |
| Monitoring data not acted upon | Warnings accumulate without response until threshold breaches cause incidents | Define a documented response procedure for every alert type |

---

## Rujukan / References

- NOSS IT-020-5:2013 Computer Systems Management — CoCu 1
- ITIL 4: Monitoring and Event Management Practice — Axelos (2019)
- ISO/IEC 20000-1:2018 — IT Service Management: Performance Monitoring Requirements
- Zabbix Documentation: Threshold Configuration and Dashboard Design (docs.zabbix.com)
- Microsoft Azure Monitor: Metrics and Alerts Best Practices
- ISACA COBIT 2019 — APO09 Managed Service Agreements, DSS04 Managed Continuity
- Gartner IT Metrics and Benchmarking: Mean Time to Restore Industry Reference Data