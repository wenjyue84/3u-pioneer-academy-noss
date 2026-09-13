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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C01 SERVER CONFIGURATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE SERVER CONFIGURATION REQUIREMENTS<br>2. PLAN SERVER ROLES AND SERVICES<br>3. CONFIGURE SERVER HARDWARE AND STORAGE<br>4. CONFIGURE SERVER OS AND ROLES<br>5. IMPLEMENT SERVER SECURITY SETTINGS<br>6. DOCUMENT SERVER CONFIGURATION |
| NO. KOD | IT-020-4:2013-C01/KP(2/6) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-02-server-roles-and-services-planning

**TUJUAN:** Kertas rujukan untuk KP-02-server-roles-and-services-planning.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Define and distinguish between common server roles (Peranan Pelayan) and the services each role provides
2. Apply capacity planning principles to determine the number and type of servers required
3. Design a server role architecture appropriate to the organisation's size, budget, and availability requirements
4. Evaluate the trade-offs between role consolidation on fewer servers versus role separation on dedicated servers
5. Produce a documented Server Role Plan (Pelan Peranan Pelayan) ready for hardware procurement and configuration

---

## 1.0 Introduction to Server Role Planning

Server role planning (Perancangan Peranan Pelayan) is the process of determining which services the server infrastructure must provide, which server will host each service, and how those servers will be sized and interconnected. It translates the verified requirements from Work Activity 1 into a concrete infrastructure design.

At Level 4, the administrator must consider not only the immediate technical requirements but also long-term manageability, redundancy, and cost of ownership. A poorly planned server role architecture results in bottlenecks, single points of failure, and costly redesign.

---

## 2.0 Common Server Roles (Peranan Pelayan Lazim)

### 2.1 Directory Services / Domain Controller (Pelayan Direktori)

A domain controller (DC) manages authentication, authorisation, and group policy for all computers and users in an Active Directory (AD) domain or an LDAP directory.

- **Windows Server:** Active Directory Domain Services (AD DS)
- **Linux equivalent:** OpenLDAP, FreeIPA, Samba 4
- **Key planning rule:** Always deploy a minimum of TWO domain controllers for redundancy. The loss of the sole DC prevents all domain logins.
- **FSMO roles** (Flexible Single Master Operations): PDC Emulator, RID Master, Infrastructure Master, Schema Master, Domain Naming Master — distributed across DCs.

### 2.2 File and Print Server (Pelayan Fail dan Cetak)

Provides centralised file storage via network shares (SMB/NFS) and print queue management.

- **Windows Server:** File Server role + DFS (Distributed File System) for namespace and replication
- **Linux:** Samba, NFS server
- **Key planning rule:** Capacity plan based on total shared data volume + annual growth rate; implement DFS Replication for redundancy across sites.

### 2.3 Web Server (Pelayan Web)

Hosts HTTP/HTTPS applications and websites.

- **Windows Server:** IIS (Internet Information Services)
- **Linux:** Apache HTTPD, Nginx
- **Key planning rule:** Plan for peak concurrent connections; consider reverse proxy and load balancer topology for scalability.

### 2.4 Database Server (Pelayan Pangkalan Data)

Manages structured data using a relational or non-relational database engine.

- **Engines:** Microsoft SQL Server, MySQL, MariaDB, PostgreSQL, Oracle Database
- **Key planning rule:** Database servers are I/O intensive — specify NVMe SSD storage and high RAM for buffer pool; isolate on dedicated servers where possible to prevent resource contention.

### 2.5 Application Server (Pelayan Aplikasi)

Hosts business applications: ERP, CRM, line-of-business (LOB) software.

- **Examples:** SAP NetWeaver, Oracle Application Server, JBoss/WildFly, .NET application hosting
- **Key planning rule:** Application server requirements are driven by vendor specifications; always consult the software vendor's sizing guide.

### 2.6 Mail Server (Pelayan E-mel)

Handles email delivery, storage, and retrieval.

- **Windows Server:** Microsoft Exchange Server
- **Linux:** Postfix + Dovecot, Zimbra
- **Cloud alternative:** Microsoft 365 / Google Workspace (reduces on-premise server load)
- **Key planning rule:** Plan for mailbox storage growth; implement anti-spam and antivirus at the gateway level.

### 2.7 DHCP and DNS Server (Pelayan DHCP dan DNS)

- **DHCP:** Dynamic Host Configuration Protocol — automatically assigns IP addresses, subnet mask, default gateway, and DNS server addresses to network clients
- **DNS:** Domain Name System — resolves hostnames to IP addresses within the organisation and for internet resources
- **Windows Server:** DHCP Server role + DNS Server role (typically co-located with AD DS)
- **Key planning rule:** DNS is critical infrastructure — deploy redundant DNS servers; misconfigured DNS disrupts all network services.

### 2.8 Virtualisation Host (Hos Virtualisasi)

Hosts multiple virtual machines (VMs) on a single physical server using a hypervisor.

- **Type 1 (Bare-metal) hypervisors:** VMware ESXi, Microsoft Hyper-V, Proxmox VE, KVM
- **Type 2 (Hosted) hypervisors:** VMware Workstation, Oracle VirtualBox (not for production)
- **Key planning rule:** Virtualisation host requires high RAM (to overcommit across VMs), fast NVMe or SAN storage, and high-speed NICs; plan for VM sprawl management.

### 2.9 Backup Server (Pelayan Sandaran)

Manages scheduled backups of all servers and data to local disk, tape, or cloud.

- **Software:** Veeam Backup & Replication, Acronis Cyber Backup, Windows Server Backup, Bacula
- **Key planning rule:** Backup server must have storage capacity for the full backup set × retention period × number of copies (3-2-1 rule).

### 2.10 Monitoring and Management Server (Pelayan Pemantauan)

Collects performance metrics, logs, and alerts from all servers and network devices.

- **Tools:** Zabbix, Nagios, PRTG, Prometheus + Grafana, Microsoft System Center
- **Key planning rule:** Deploy monitoring as an early priority; it provides visibility for all other server roles.

---

## 3.0 Role Consolidation vs. Role Separation

### 3.1 Dedicated Server Model (Model Pelayan Khusus)

Each server role is deployed on a separate physical server.

| Advantage | Disadvantage |
|-----------|-------------|
| No resource contention between roles | Higher hardware and licensing cost |
| Failure of one role does not affect others | More physical space and power consumption |
| Easier to optimise hardware per role | More servers to manage and patch |

**Suitable for:** Large organisations, production environments with strict SLA, roles with high resource demand (database, virtualisation host)

### 3.2 Role Consolidation Model (Model Penyatuan Peranan)

Multiple server roles are hosted on a single physical or virtual server.

| Advantage | Disadvantage |
|-----------|-------------|
| Lower hardware and licensing cost | Resource contention may affect performance |
| Fewer physical servers to manage | Failure of one role may cascade to others |
| Suitable for smaller deployments | Harder to right-size hardware for multiple workloads |

**Suitable for:** Small-medium organisations, branch offices, development and test environments

### 3.3 Virtualisation as a Consolidation Strategy

Virtualisation resolves the tension between role separation (for isolation) and cost efficiency (fewer physical servers). Each role runs in its own VM on shared physical hardware, providing:

- Logical isolation between roles
- Flexible resource allocation (vCPU, vRAM, vDisk)
- Rapid VM deployment and snapshot capability
- Live migration for zero-downtime maintenance

**Decision guide for Level 4 administrators:**

| Organisation Size | Recommended Approach |
|------------------|---------------------|
| < 50 users | Consolidated physical or small VM cluster |
| 50–500 users | Virtualised server farm (2–3 physical hosts) |
| > 500 users | Dedicated physical servers for database and DC; virtualisation for remaining roles; consider clustering |

---

## 4.0 Capacity Planning Fundamentals

Capacity planning (Perancangan Kapasiti) ensures that the server can handle current and projected workload:

### 4.1 CPU Sizing

- Identify the peak CPU utilisation target: plan for **no more than 70–80%** average utilisation at peak load (leaving headroom for spikes)
- Formula: `Required vCPUs = (Peak concurrent tasks × CPU time per task) / Target utilisation`
- For physical CPUs: account for NUMA topology, hyperthreading, and OS overhead

### 4.2 RAM Sizing

| Workload Type | RAM Planning Rule |
|--------------|------------------|
| Domain Controller | 8–16 GB per DC (small/medium domain) |
| File Server | 4–8 GB + read cache as needed |
| Database Server | RAM = working dataset size + OS + buffer pool (as large as possible) |
| Web/Application Server | Per-vendor spec × concurrent session count |
| Virtualisation Host | Sum of all VM RAM allocations + 10–15% hypervisor overhead |

### 4.3 Storage Sizing

- **Usable capacity = Raw capacity − RAID overhead − filesystem overhead**
- RAID 5 overhead: 1 disk worth of parity; RAID 6: 2 disks; RAID 10: 50% of raw
- Add 20–30% free space buffer to ensure consistent IOPS performance on SSDs
- Apply annual growth rate: `3-year capacity = Current × (1 + growth rate)³`

### 4.4 Network Bandwidth

- Measure or estimate peak aggregate throughput in Gbps
- Account for simultaneous backup traffic, replication, and user traffic
- Recommend NIC bonding (802.3ad LACP) for bandwidth aggregation and redundancy

---

## 5.0 Server Role Plan Document

The Server Role Plan (Pelan Peranan Pelayan) produced at the end of this work activity contains:

| Section | Content |
|---------|---------|
| 1. Role Inventory | Table of all server roles required, with justification |
| 2. Server Allocation | Which physical or virtual server hosts each role |
| 3. Hardware Specifications | CPU, RAM, storage, NICs per server |
| 4. Network Topology | IP addressing, VLANs, firewall zones |
| 5. Availability Design | Redundancy, failover, clustering plan |
| 6. OS and Licensing | OS version, edition, licensing model per server |
| 7. Timeline | Procurement, installation, and commissioning dates |
| 8. Sign-off | Authorised by IT Manager or Project Sponsor |

---

## 6.0 Common Errors in Role Planning

| Error | Consequence | Prevention |
|-------|-------------|------------|
| **Deploying a single domain controller** | Loss of DC = complete loss of domain authentication | Always deploy minimum 2 DCs in different physical locations or failure domains |
| **Undersizing database server RAM** | Database buffer pool cannot cache working data set; high disk I/O; slow queries | Size RAM to the database working set; consult vendor sizing guide |
| **Co-locating DC and backup server** | Ransomware compromise of DC gives attacker access to backup files | Separate backup server; apply least-privilege access; offline/immutable backup copy |
| **Ignoring NUMA topology on multi-socket servers** | VM or application pinned to remote NUMA node suffers memory latency penalties | Pin VMs to NUMA nodes; configure NUMA-aware memory in hypervisor |
| **Planning roles without OS licensing** | Budget shortfall; legal non-compliance; inability to activate software | Include OS licensing cost and model in the Server Role Plan |

---

## Rujukan / References

- NOSS IT-020-4:2013 Computer Systems Administration — CoCu 1: Server Configuration
- Microsoft Windows Server Roles and Features documentation: https://docs.microsoft.com/en-us/windows-server/
- VMware vSphere Resource Management Guide
- CompTIA Server+ Exam Objectives — Server Architecture and Planning
- ISO/IEC 27001:2022 Annex A — Information Security Controls