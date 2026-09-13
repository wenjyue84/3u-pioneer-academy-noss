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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-C04 DISASTER RECOVERY MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE DISASTER RECOVERY REQUIREMENTS<br>2. DEVELOP DISASTER RECOVERY MANAGEMENT PLAN<br>3. IMPLEMENT COMPUTER NETWORK DISASTER RECOVERY MANAGEMENT PLAN<br>4. PRODUCE DISASTER RECOVERY MANAGEMENT REPORT |
| NO. KOD | IT-020-5:2013-C04/KK(3/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-03-implementing-network-disaster-recovery-plan

**TUJUAN:** Kertas rujukan untuk KK-03-implementing-network-disaster-recovery-plan.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
**TUJUAN:** Execute a simulated DR plan implementation including network failover, server and data restoration, DR testing procedures, and recovery validation in a controlled lab environment.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

---

## Objektif / Objective

Implement a disaster recovery scenario in a virtualised lab environment: execute network failover, restore a simulated database from backup, conduct a tabletop DR drill, and validate recovery against defined acceptance criteria.

---

## Tempoh / Duration

8 hours (distributed across WA3 practical sessions — use virtualised lab environment)

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Virtualised lab environment (VMware Workstation or Hyper-V with pre-configured VMs) | 1 per trainee/pair |
| 2 | Completed DRP from KK(2/4) | 1 |
| 3 | Lab network diagram (simulated primary and DR site topology) | 1 |
| 4 | Simulated backup files (database backup, VM snapshot) pre-loaded on lab server | 1 set |
| 5 | DR test report template | 1 |
| 6 | Recovery validation checklist | 1 |
| 7 | Tabletop exercise scenario cards (provided by instructor) | 1 set |

---

## Langkah Keselamatan / Safety Precautions

- Work only within the designated virtualised lab environment — do not connect lab VMs to production networks
- Do not shut down the instructor's host server without explicit authorisation
- All configuration changes must be documented in real time — do not rely on memory
- If a lab VM becomes unresponsive, notify the instructor before attempting a force restart

---

## Senario / Scenario

**Lab Setup:** The lab environment simulates Syarikat Logistik Sejahtera's IT infrastructure:

| VM | Role | IP (Simulated) |
|----|------|----------------|
| DC-01 | Windows Server — Active Directory, DNS | 192.168.10.1 |
| DB-01 | SQL Server — WMS database (primary) | 192.168.10.10 |
| APP-01 | WMS application server | 192.168.10.20 |
| DR-DB-01 | SQL Server standby — DR site | 192.168.20.10 |
| DR-APP-01 | WMS application server — DR site | 192.168.20.20 |
| FW-01 | pfSense firewall (simulated primary site) | 192.168.10.254 |
| FW-DR | pfSense firewall (simulated DR site) | 192.168.20.254 |

**Disaster Scenario:** At 09:00, a simulated fire alert at the primary data centre causes the primary site (192.168.10.x) to be isolated. The DR Coordinator has declared a Level 3 disaster. You are the IT Infrastructure Lead. Your task is to execute the DR plan.

---

## Prosedur / Procedures

### Bahagian A: Network Failover / Kegagalihan Rangkaian (2 hours)

| Langkah | Arahan / Instruction |
|---------|---------------------|
| A1 | Confirm primary site isolation: ping DC-01 and DB-01 from DR site VMs — verify no response. Document timestamp. |
| A2 | Log in to FW-DR (pfSense). Verify DR site network is operational: ping DR-DB-01 and DR-APP-01 from FW-DR. |
| A3 | Update DNS records on DR-DC (if available) or edit hosts files on DR-APP-01 to resolve WMS database hostname to DR-DB-01 IP (192.168.20.10). Document changes made. |
| A4 | Verify internet connectivity from DR site: ping 8.8.8.8 and browse to a test URL. Document result. |
| A5 | Record all network recovery steps in the DR implementation log with timestamps. |

### Bahagian B: Database Restoration / Pemulihan Pangkalan Data (2 hours)

| Langkah | Arahan / Instruction |
|---------|---------------------|
| B1 | Log in to DR-DB-01. Open SQL Server Management Studio (SSMS). Verify the SQL Server service is running. |
| B2 | Locate the latest WMS database backup file in the pre-configured backup share (\\LAB-BACKUP\WMS\). Note the backup timestamp — this determines the RPO achieved. |
| B3 | Restore the full database backup to DR-DB-01. Use the RESTORE DATABASE command or SSMS restore wizard. Document the exact restore command used. |
| B4 | Apply all available differential and transaction log backups in sequence. Record each file applied and its timestamp. |
| B5 | Run DBCC CHECKDB on the restored database. Record the result. |
| B6 | Verify key data: query the top 10 records from the main inventory table. Screenshot the result. |
| B7 | Calculate actual RPO achieved: (time of incident) − (timestamp of latest applied backup). Record value. |

### Bahagian C: Application Recovery / Pemulihan Aplikasi (1 hour)

| Langkah | Arahan / Instruction |
|---------|---------------------|
| C1 | Log in to DR-APP-01. Update the WMS application configuration file (config.ini or web.config) — change the database connection string to point to DR-DB-01 (192.168.20.10). |
| C2 | Start the WMS application service on DR-APP-01 (use Services panel or net start command). Verify service status. |
| C3 | Open a browser on DR-APP-01 and access the WMS web interface. Verify login succeeds with a test account. |
| C4 | Perform smoke tests: add a simulated inventory item, view a transport route, and generate a summary report. Document each test result (pass/fail). |
| C5 | Record the time at which WMS is declared operational. Calculate actual RTO: (current time) − (disaster declaration time at 09:00). |

### Bahagian D: Tabletop DR Drill / Latihan Meja DR (1 hour)

| Langkah | Arahan / Instruction |
|---------|---------------------|
| D1 | Instructor distributes scenario complication cards (e.g. "Key DBA is unreachable"; "DR site ISP reports intermittent connectivity"; "Backup file is corrupted"). |
| D2 | As a team, walk through how you would respond to each complication within the context of the DRP. Assign the action to the relevant DR team role. |
| D3 | Document each complication, the proposed response, the time estimated, and any gaps in the DRP that the complication exposed. |
| D4 | As a group, identify the single most critical gap discovered during the tabletop drill. Propose a corrective action. |

### Bahagian E: Recovery Validation and Report / Pengesahan Pemulihan dan Laporan (2 hours)

| Langkah | Arahan / Instruction |
|---------|---------------------|
| E1 | Complete the Recovery Validation Checklist for all systems recovered (network, database, application). Record pass/fail for each item. |
| E2 | Calculate final RTO and RPO achieved. Compare against targets from the DRP. Classify as: Pass (within target) / Minor variance / Major variance. |
| E3 | Complete the DR Test Report using the provided template. Include: test details, scenario, objectives, results (actual RTO/RPO), issues found, and recommendations. |
| E4 | Document minimum THREE (3) corrective action items in the CAP table within the DR Test Report. Assign a simulated owner and target date for each. |
| E5 | Submit completed DR Test Report to the instructor. Be prepared to present key findings in a 5-minute debrief. |

---

## Hasil Jangkaan / Expected Outcome

- Network failover completed and documented with timestamps
- WMS database restored from backup; DBCC CHECKDB passed; actual RPO calculated
- WMS application operational on DR site; smoke tests passed; actual RTO calculated
- Tabletop drill completed; minimum 3 gaps documented with corrective actions
- Completed DR Test Report with RTO/RPO variance analysis and CAP table

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Primary site isolation confirmed; network failover executed and documented | [ ] Yes  [ ] No |
| 2 | DNS/hostname update completed correctly; DR site network verified | [ ] Yes  [ ] No |
| 3 | Database restored from correct backup; DBCC CHECKDB passed | [ ] Yes  [ ] No |
| 4 | Transaction log backups applied in correct sequence; RPO calculated | [ ] Yes  [ ] No |
| 5 | WMS application connection string updated; service started; smoke tests passed | [ ] Yes  [ ] No |
| 6 | Actual RTO calculated and compared against target | [ ] Yes  [ ] No |
| 7 | Tabletop drill conducted; minimum 3 gaps documented | [ ] Yes  [ ] No |
| 8 | DR Test Report completed with RTO/RPO analysis and CAP table (minimum 3 items) | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |