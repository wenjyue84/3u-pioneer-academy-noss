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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-C04 DISASTER RECOVERY MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE DISASTER RECOVERY REQUIREMENTS<br>2. DEVELOP DISASTER RECOVERY MANAGEMENT PLAN<br>3. IMPLEMENT COMPUTER NETWORK DISASTER RECOVERY MANAGEMENT PLAN<br>4. PRODUCE DISASTER RECOVERY MANAGEMENT REPORT |
| NO. KOD | IT-020-5:2013-C04/KP(3/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-03-disaster-recovery-plan-implementation

**TUJUAN:** Kertas rujukan untuk KP-03-disaster-recovery-plan-implementation.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Execute the technical steps required to activate and implement a DR plan for computer network infrastructure
2. Configure backup systems, replication technologies, and DR site infrastructure
3. Conduct DR testing and drills including tabletop exercises, functional tests, and full failover tests
4. Restore network services, servers, and critical applications to the DR site within defined RTO targets
5. Validate recovered systems against defined acceptance criteria before declaring recovery complete

---

## 1.0 DR Plan Activation / Pengaktifan Pelan DR

### 1.1 Activation Decision / Keputusan Pengaktifan

Plan activation is the formal declaration that a disaster has occurred and the DRP must be executed. The activation decision is made by the **DR Coordinator** based on:

- Confirmed disruption exceeding or approaching the system's MTD
- Failure of standard incident response procedures to restore service
- Site-wide event (fire, flood, power failure) rendering the primary site inoperable

**Activation is NOT automatic.** A defined authority (typically the DR Coordinator or IT Director) must formally declare the disaster event and authorise DRP activation.

### 1.2 Notification Tree / Pokok Pemberitahuan

Upon activation, the following notification sequence is executed within 30 minutes:

| Step | Action | Responsible |
|------|--------|-------------|
| 1 | DR Coordinator declares disaster; notifies IT Director and CEO | DR Coordinator |
| 2 | IT Infrastructure Lead, DBA, and Network Engineer are contacted | DR Coordinator |
| 3 | DR team assembles at designated command centre (physical or virtual) | All DR team members |
| 4 | Communication Officer notifies key stakeholders and affected departments | Communication Officer |
| 5 | Vendor contacts (ISP, cloud provider, hardware supplier) are alerted | IT Infrastructure Lead |

---

## 2.0 Network Infrastructure Recovery / Pemulihan Infrastruktur Rangkaian

### 2.1 Network Recovery Sequence / Urutan Pemulihan Rangkaian

Network infrastructure must be restored before servers and applications can be brought online. The recovery sequence is:

```
1. Physical connectivity (cabling, switches, routers)
       ↓
2. Core network services (DHCP, DNS)
       ↓
3. Internet connectivity and firewall rules
       ↓
4. VPN and remote access
       ↓
5. Internal network segmentation (VLANs, subnets)
       ↓
6. Monitoring and management access
```

### 2.2 DNS Recovery / Pemulihan DNS

DNS (Domain Name System) is critical — all services depend on name resolution:

- **Primary action:** Update DNS records to point to DR site IP addresses (DNS failover)
- **TTL consideration:** Low TTL values (300 seconds or less) must be pre-configured to allow rapid propagation during failover
- **Split-horizon DNS:** Maintain separate internal and external DNS configurations; update both during failover

### 2.3 Firewall and Security Policy Restoration

At the DR site, firewall rules and security policies must mirror the primary site:

| Step | Action |
|------|--------|
| 1 | Restore firewall configuration from secure backup (configuration file) |
| 2 | Verify ACLs (Access Control Lists) are correctly applied |
| 3 | Enable IDS/IPS at DR site |
| 4 | Verify VPN tunnels are active |
| 5 | Review and apply security patches if DR site systems have been idle |

---

## 3.0 Server and Storage Recovery / Pemulihan Pelayan dan Storan

### 3.1 Server Recovery Priority / Keutamaan Pemulihan Pelayan

Server recovery follows the priority tiers established in the BIA:

| Priority | System Type | Recovery Target |
|----------|-------------|----------------|
| 1 | Active Directory / LDAP, DNS | First — all other systems depend on authentication |
| 2 | Core business application servers (ERP, database) | Within RTO Tier 1 |
| 3 | File servers, email servers | Within RTO Tier 2 |
| 4 | Development, training, secondary systems | After Tier 1 and 2 are confirmed stable |

### 3.2 Virtual Machine Recovery / Pemulihan Mesin Maya

For virtualised environments (VMware, Hyper-V), recovery involves:

1. **Snapshot restoration / Pemulihan Syot Layar:** Restore the VM from the most recent snapshot meeting RPO requirements
2. **VM replication failover:** If using VMware Site Recovery Manager (SRM) or Azure Site Recovery, trigger the pre-tested failover runbook
3. **P2V (Physical to Virtual):** If physical servers must be converted, use Disk2VHD or similar tools to create VM images from physical backups
4. **Storage attachment:** Attach the correct datastore or storage volume; verify LUN mapping

### 3.3 Database Recovery / Pemulihan Pangkalan Data

Database recovery is the most technically sensitive step:

| Scenario | Recovery Method |
|----------|----------------|
| Backup restoration | Restore full backup; apply differential; apply transaction logs up to RPO point |
| Log shipping standby | Bring log shipping standby database online; apply pending logs; open for user access |
| Synchronous replica | Promote replica to primary; redirect application connection strings |
| Point-in-time recovery | Use transaction log backups to restore to a specific timestamp (e.g. before accidental deletion) |

**Database integrity checks / Semakan integriti pangkalan data must be performed after restoration:**
- Run `DBCC CHECKDB` (SQL Server) or equivalent
- Verify row counts against last known good counts
- Verify critical transactions against transaction logs

---

## 4.0 Application Recovery / Pemulihan Aplikasi

### 4.1 Application Startup Sequence

After infrastructure and database are confirmed operational:

1. Start application servers in dependency order (authentication → database → middleware → application tier → web tier)
2. Verify application services are running (check Windows Services / Linux systemd)
3. Perform smoke tests: login, basic CRUD operations, report generation
4. Verify integration points: API connections, third-party services, payment gateways

### 4.2 Connection String and Configuration Updates

Applications referencing the primary site's IP addresses or hostnames must be updated:

- **Connection strings:** Update database connection strings in application configuration files or environment variables
- **Load balancer configuration:** Update upstream server definitions
- **Email relay:** Update SMTP server references if mail server has moved
- **Certificate validation:** Ensure SSL/TLS certificates are valid for the DR site domain

---

## 5.0 DR Testing and Drills / Pengujian dan Latih Tubi DR

### 5.1 Types of DR Tests / Jenis Ujian DR

DR testing is mandatory. ISO 22301:2019 Clause 8.5 requires that the organisation conduct exercises at planned intervals. Four test types are used, in increasing complexity:

| Test Type | Description | Duration | Disruption to Production |
|-----------|-------------|----------|--------------------------|
| **Tabletop Exercise / Latihan Meja** | Discussion-based walkthrough of the DR plan with key stakeholders; no systems are activated | 2–4 hours | None |
| **Walkthrough / Simulation Test** | Each team member reviews and verifies their specific procedures; checklists are completed; no failover | 4–8 hours | None |
| **Functional Test / Ujian Berfungsi** | Selected systems or components are actually failed over and restored; not all systems at once | 1–2 days | Minimal (isolated systems) |
| **Full Interruption Test / Ujian Gangguan Penuh** | Complete failover of all production systems to DR site; production intentionally shut down | 1–3 days | High (production offline) |

### 5.2 Tabletop Exercise Procedure

1. DR Coordinator presents a disaster scenario (e.g. "Data centre flooded at 09:00 on a Monday")
2. Participants walk through their response actions step by step, referencing the DRP
3. Facilitator injects complications (e.g. "Key DBA is on leave; ISP also reports outage")
4. Gaps, ambiguities, and single points of failure are documented
5. Action items are assigned and tracked to closure

### 5.3 Functional Failover Test Procedure

1. **Pre-test preparation (T-2 weeks):**
   - Notify affected business units of test schedule
   - Verify DR site readiness: hardware powered on, network connectivity confirmed, backup media available
   - Assign roles to DR team members

2. **Test execution:**
   - Isolate test systems from production (to avoid data contamination)
   - Execute DR procedures as documented in the DRP
   - Record start time, actions taken, and any deviations from documented procedures
   - Measure actual RTO and RPO achieved vs. targets

3. **Post-test activities:**
   - Restore systems to primary site (if applicable)
   - Document actual RTO/RPO achieved
   - Identify gaps: steps that were missing, unclear, or took longer than expected
   - Update DRP based on findings

### 5.4 DR Test Report / Laporan Ujian DR

Every test must produce a formal test report:

| Section | Content |
|---------|---------|
| Test details | Date, type, scope, participants |
| Scenario used | Description of simulated disaster event |
| Objectives | RTO/RPO targets for the test |
| Results | Actual RTO/RPO achieved; pass/fail per system |
| Issues found | Gaps, failures, deviations from procedure |
| Recommendations | Corrective actions with assigned owner and due date |
| Sign-off | DR Coordinator and IT Director signatures |

---

## 6.0 Recovery Validation and Acceptance / Pengesahan dan Penerimaan Pemulihan

### 6.1 Validation Checklist / Senarai Semak Pengesahan

Before declaring recovery complete, the following must be verified:

| Validation Item | Verification Method |
|----------------|---------------------|
| All Tier 1 systems operational | System health dashboard; application team sign-off |
| Data integrity confirmed | Row count verification; transaction log review; spot-check queries |
| Network connectivity (LAN and WAN) | Ping tests; traceroute; bandwidth test |
| Security controls active | Firewall rule review; IDS/IPS status; authentication test |
| Backup system operational at DR site | Trigger a test backup; verify completion |
| User access verified | Sample users from each department log in and confirm access |
| Monitoring and alerting active | Verify alerts received for test events |

### 6.2 Recovery Declaration / Pengisytiharan Pemulihan

Formal recovery declaration is made by the DR Coordinator when:
- All Tier 1 and Tier 2 systems have passed validation
- Application owners have signed the acceptance checklist
- Security Officer has confirmed security posture

After declaration, the organisation operates from the DR site until the primary site is restored (**failback / faillik**).

---

## 7.0 Failback to Primary Site / Faillik ke Tapak Utama

Failback is the process of returning operations from the DR site to the primary site after the disaster is resolved:

1. **Assess primary site readiness:** Verify that the root cause of the disaster has been resolved and the primary site is structurally and technically safe
2. **Resynchronise data:** Replicate all data changes made at the DR site back to the primary site; verify consistency
3. **Schedule failback window:** Coordinate a low-impact maintenance window; notify all users
4. **Execute failback:** Reverse the failover steps; bring primary site systems online; redirect traffic
5. **Decommission DR site from active duty:** Return DR systems to standby state
6. **Post-failback review:** Document lessons learnt; update DRP

---

## Rujukan / References

- ISO 22301:2019 — Business Continuity Management Systems — Requirements
- VMware Site Recovery Manager Documentation
- Microsoft Azure Site Recovery Documentation
- NIST SP 800-34 Rev.1 — Contingency Planning Guide
- NOSS IT-020-5:2013 CoCU 4 — Disaster Recovery Management
- CyberSecurity Malaysia — Incident Response Guidelines