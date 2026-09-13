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

## KERTAS KERJA

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-5:2013 PENGURUSAN SISTEM KOMPUTER |
| TAHAP | 5 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-C01 COMPUTER SYSTEMS PLANNING AND OPERATIONS MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. PLAN RESOURCES<br>2. COORDINATE OPERATIONS<br>3. MONITOR PERFORMANCE<br>4. REPORT TO MANAGEMENT |
| NO. KOD | IT-020-5:2013-C01/KK(3/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-03-performance-monitoring-dashboard-simulation

**TUJUAN:** Kertas rujukan untuk KK-03-performance-monitoring-dashboard-simulation.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

Apply IT performance monitoring principles by analysing simulated operational data, designing a management KPI dashboard, computing availability and reliability metrics, and producing a trend analysis report with management recommendations.

---

## Tempoh / Duration

2.5 hours (individual; desk-based analytical exercise)

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | 6-month IT performance data set (simulated — provided as handout) | 1 |
| 2 | Incident log extract (6 months; simulated — provided as handout) | 1 |
| 3 | SLA document extract showing targets (provided as handout) | 1 |
| 4 | Spreadsheet application (Microsoft Excel or equivalent) | 1 workstation per trainee |
| 5 | Dashboard design template (blank — provided by instructor) | 1 |

---

## Langkah Keselamatan / Safety Precautions

- This is a desk-based analytical exercise. Standard office safety practices apply.
- Save spreadsheet work regularly.
- All data sets are simulated and confidential to the training context.

---

## Data Set Provided (Simulated — Summary)

The instructor will provide a detailed 6-month data extract. The summary below describes the data structure:

| Data Set | Content |
|----------|---------|
| Server utilisation (monthly) | Average CPU %, RAM %, Storage % for 5 production servers (Jan–Jun) |
| Network utilisation (monthly) | Average bandwidth % for 3 WAN links (Jan–Jun) |
| Incident log | 180 incident records with: date, category, priority, time-to-resolve, status |
| Service availability log | Downtime events per service per month (service name, start time, duration) |
| Change log | 45 change records with: date, type, status (successful/failed), associated incidents |
| User satisfaction surveys | Monthly average CSAT score (scale 1–5) for 6 months |

---

## Prosedur / Procedures

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 1 | **KPI Review and SLA Mapping (20 min):** Review the SLA document provided. List all SLA targets. Create a KPI tracking table mapping each SLA target to the corresponding data set column. Identify which KPIs can be calculated from the provided data and which would require additional monitoring tools. |
| 2 | **Availability Calculation (30 min):** For each of the 4 services listed in the availability log, calculate: (a) Monthly availability % for each of the 6 months; (b) 6-month average availability; (c) Whether each month and the 6-month average met the SLA target; (d) Total allowable downtime per month vs. actual downtime. Present findings in a table. Identify any months with SLA breaches. |
| 3 | **MTBF and MTTR Calculation (20 min):** Using the incident log, for the service with the highest incident count: (a) Calculate MTBF for the 6-month period; (b) Calculate MTTR for the 6-month period; (c) Calculate whether MTTR is trending upward or downward over the 6 months (plot or tabulate monthly MTTR). Interpret what the MTTR trend means for the IT team's performance. |
| 4 | **Incident Trend Analysis (30 min):** Analyse the full 6-month incident log: (a) Calculate total incidents per month — plot the monthly trend; (b) Break down incidents by category (network, server, application, user); (c) Identify the top 3 incident categories by volume; (d) Identify the top 3 repeat incidents (same root cause); (e) Calculate SLA breach rate per month (incidents not resolved within SLA time); (f) Write a 200-word trend analysis commentary interpreting the findings and recommending 2–3 management actions. |
| 5 | **Capacity Utilisation Review (20 min):** Review the server and network utilisation data: (a) Identify any server or network link that has exceeded 80% utilisation in any month; (b) Calculate the monthly average and the 6-month trend for each resource; (c) Flag any resource where the trend indicates it will exceed 85% within the next 3 months (based on the trend slope); (d) Recommend an action for each flagged resource. |
| 6 | **Dashboard Design (30 min):** Using the dashboard design template provided, design a one-page IT Performance Management Dashboard for monthly presentation to senior management. The dashboard must include: (a) Service health RAG status table (one row per service); (b) Monthly availability trend chart (6-month line chart vs. SLA target); (c) Incident volume by category (bar chart); (d) Capacity utilisation gauges (CPU, storage, bandwidth); (e) Key metrics summary box (MTTR, CSAT, Change success rate). |
| 7 | **Monitoring Gap Analysis (10 min):** Review the data sets provided. Identify TWO gaps in the monitoring data — i.e., important IT performance dimensions that are NOT covered by the current data sets. For each gap, recommend a monitoring tool or method that would address it. |

---

## Hasil Jangkaan / Expected Outcome

- Completed KPI tracking table with SLA mapping
- Availability calculation table (6 months × 4 services) with SLA compliance status
- MTBF and MTTR calculations with trend interpretation
- Incident trend analysis with charts/tables and 200-word commentary
- Capacity utilisation trend analysis with flagged resources and recommended actions
- Completed management KPI dashboard (one page)
- Monitoring gap analysis (2 gaps identified with recommended solutions)

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | All availability calculations are mathematically correct | [ ] Yes  [ ] No |
| 2 | MTBF and MTTR correctly computed and trend direction correctly interpreted | [ ] Yes  [ ] No |
| 3 | Incident trend analysis covers volume, category breakdown, repeat incidents, and SLA breach rate | [ ] Yes  [ ] No |
| 4 | Capacity utilisation identifies all resources exceeding 80% threshold | [ ] Yes  [ ] No |
| 5 | Dashboard is suitable for management audience (visual, concise, RAG-coded) | [ ] Yes  [ ] No |
| 6 | Trend commentary includes management-level recommendations (not just data description) | [ ] Yes  [ ] No |
| 7 | Monitoring gap analysis identifies genuine gaps with practical solutions | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |