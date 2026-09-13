# CoCu 1: Server Configuration (L4, 200 hrs)


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-4:2013 COMPUTER SYSTEMS ADMINISTRATION (Pentadbiran Sistem Komputer) | IT-020-4:2013 COMPUTER SYSTEMS ADMINISTRATION (Pentadbiran Sistem Komputer) |
| LEVEL | L4 | L4 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 1: Server Configuration (Konfigurasi Pelayan) | CoCu 1: Server Configuration (Konfigurasi Pelayan) |
| NO. AND WORK ACTIVITY STATEMENT | ANALYSE SERVER CONFIGURATION REQUIREMENTS · PLAN SERVER ROLES AND SERVICES · CONFIGURE SERVER HARDWARE AND STORAGE · CONFIGURE SERVER OS AND ROLES · IMPLEMENT SERVER SECURITY SETTINGS · DOCUMENT SERVER CONFIGURATION | ANALYSE SERVER CONFIGURATION REQUIREMENTS · PLAN SERVER ROLES AND SERVICES · CONFIGURE SERVER HARDWARE AND STORAGE · CONFIGURE SERVER OS AND ROLES · IMPLEMENT SERVER SECURITY SETTINGS · DOCUMENT SERVER CONFIGURATION |
| NO. CODE | IT-020-4:2013 - CoCu 1 / P(1/6) | PAGE: 1 - 14 |


| SET-UP CONTEXT | SINGLE SERVER / STANDALONE ENVIRONMENT | MULTI-SERVER / DOMAIN ENVIRONMENT |
|----------------|----------------------------------------|-------------------------------------|
| Scope and trigger | Single physical or virtual server deployed for a small office or branch. Roles are consolidated on one machine (e.g. file server, DHCP, DNS). Requirements are gathered from a single department or site manager and the configuration follows a straightforward checklist. | Multiple physical and virtual servers deployed across a domain or enterprise environment. Roles are distributed for performance and redundancy (e.g. dedicated domain controller, separate file server, Hyper-V host). Requirements involve multiple stakeholders, capacity planning, and high-availability considerations. |
| Tools and equipment | Server Manager, BIOS/UEFI setup utility, RAID controller utility (hardware or software RAID), basic networking tools (ping, ipconfig). One server chassis with internal storage, single UPS, and KVM or direct console access. | Server Manager, Active Directory Users and Computers, Group Policy Management Console, Hyper-V Manager, Remote Desktop, out-of-band management (iDRAC/iLO/IPMI), centralised monitoring. Multiple server chassis, SAN/NAS storage, redundant UPS, and rack infrastructure. |
| Documentation and reporting | Configuration record documenting IP address, installed roles, storage layout, and administrator credentials. Single sign-off by site manager. Record filed per organisational document management system. | Comprehensive configuration documentation covering domain topology, role distribution, IP scheme, storage architecture, Group Policy structure, backup schedule, and change history. Sign-off from IT manager and stakeholders. Documentation maintained in a centralised IT knowledge base for handover and audit. |


| Type | Description |
|------|-------------|
| Server roles and services (DNS, DHCP, AD, File Server, Hyper-V, Print Server) | Functional capabilities installed on a server operating system to provide specific network services. DNS resolves hostnames to IP addresses and is a prerequisite for Active Directory. DHCP automates IP address assignment to clients. Active Directory (AD) provides centralised authentication, authorisation, and directory services for a domain. File Server manages shared folders and permissions. Hyper-V enables virtualisation of multiple guest operating systems on a single host. The administrator must plan role dependencies, installation order, and resource allocation to ensure stability. |
| RAID storage configuration (RAID 0, 1, 5, 6, 10) | Redundant Array of Independent Disks technology that combines multiple physical drives for performance, redundancy, or both. RAID 0 stripes data for speed but offers no fault tolerance. RAID 1 mirrors data across two drives for redundancy. RAID 5 stripes with distributed parity, tolerating one drive failure. RAID 6 uses double parity, tolerating two drive failures. RAID 10 combines mirroring and striping for both performance and redundancy. The administrator selects the RAID level based on criticality, performance requirements, and available disk count, then configures it through the RAID controller utility before OS installation. |
| Out-of-band management (iDRAC, iLO, IPMI) | Remote management interfaces built into enterprise server hardware that operate independently of the main operating system. Dell iDRAC, HP iLO, and generic IPMI allow the administrator to power on/off the server, access the BIOS/UEFI, mount virtual media, and view hardware health from a web browser -- even when the OS is unresponsive. This is critical for servers in locked data centres or remote sites where physical console access is impractical. The administrator configures the management IP, credentials, and alert notifications during initial server setup. |
| Group Policy (GPO) | A centralised management framework in Windows Server Active Directory that allows the administrator to define and enforce security settings, software deployment, desktop configuration, and login scripts across all domain-joined computers and users. Policies are linked to organisational units (OUs) and applied automatically at login or startup. The administrator must plan the GPO structure, test policies in a non-production OU before deployment, and document all policy objects for audit and troubleshooting. |
| Server security hardening | The process of reducing the attack surface of a server by disabling unnecessary services, closing unused ports, applying the latest security patches, configuring firewall rules, and enforcing password and audit policies. Hardening baselines such as CIS Benchmarks or vendor security guides provide a checklist of recommended settings. The administrator applies hardening during initial configuration and verifies compliance using security scanning tools. Failure to harden a server exposes it to known vulnerabilities and potential compromise. |
| Configuration documentation and change management | A formal record of all server settings including hostname, IP address, installed roles, storage layout, administrator accounts, licence keys, and security configuration. Change management requires that any modification to the server (role addition, patch, hardware upgrade) is recorded with date, reason, and responsible person. Documentation is essential for troubleshooting, disaster recovery, handover, and compliance audit. The administrator maintains documentation in a centralised system and updates it after every change. |


| % | Hrs | Work activity | Knowledge 30% | Performance 70% | Total |
|---|-----|---------------|---------------|-----------------|-------|
| 15% | 30 | Analyse server configuration requirements | 9.0 | 21.0 | 30.0 |
| 15% | 30 | Plan server roles and services | 9.0 | 21.0 | 30.0 |
| 25% | 50 | Configure server hardware and storage | 15.0 | 35.0 | 50.0 |
| 25% | 50 | Configure server OS and roles | 15.0 | 35.0 | 50.0 |
| 15% | 30 | Implement server security settings | 9.0 | 21.0 | 30.0 |
| 5% | 10 | Document server configuration | 3.0 | 7.0 | 10.0 |
| **100%** | **200** | | **60.0** | **140.0** | **200.0** |


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-4:2013 COMPUTER SYSTEMS ADMINISTRATION (Pentadbiran Sistem Komputer) | IT-020-4:2013 COMPUTER SYSTEMS ADMINISTRATION (Pentadbiran Sistem Komputer) |
| LEVEL | L4 | L4 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 1: Server Configuration (Konfigurasi Pelayan) | CoCu 1: Server Configuration (Konfigurasi Pelayan) |
| NO. AND WORK ACTIVITY STATEMENT | ANALYSE SERVER CONFIGURATION REQUIREMENTS · PLAN SERVER ROLES AND SERVICES · CONFIGURE SERVER HARDWARE AND STORAGE · CONFIGURE SERVER OS AND ROLES · IMPLEMENT SERVER SECURITY SETTINGS · DOCUMENT SERVER CONFIGURATION | ANALYSE SERVER CONFIGURATION REQUIREMENTS · PLAN SERVER ROLES AND SERVICES · CONFIGURE SERVER HARDWARE AND STORAGE · CONFIGURE SERVER OS AND ROLES · IMPLEMENT SERVER SECURITY SETTINGS · DOCUMENT SERVER CONFIGURATION |
| NO. CODE | IT-020-4:2013 - CoCu 1 / P(1/6) | PAGE: 15 - 24 |


| Hardware Component | Description |
|--------------------|-------------|
| Server chassis (tower, rack-mount, blade) | The physical enclosure that houses all server components. Tower servers are standalone units suited for small offices with limited rack infrastructure. Rack-mount servers (1U, 2U, 4U) are designed for standard 19-inch racks and are the most common in data centres, allowing dense deployment. Blade servers fit into a shared chassis with common power and cooling, maximising density for large-scale environments. The administrator selects the form factor based on data centre capacity, cooling requirements, growth plans, and budget. |
| RAID controller (hardware / software) | A dedicated controller card or chipset that manages the RAID array. Hardware RAID controllers have their own processor and cache memory, offloading RAID calculations from the server CPU and providing better performance and battery-backed cache for write protection during power loss. Software RAID uses the server OS and CPU to manage the array, which is simpler and cheaper but slower. The administrator configures the RAID controller through its BIOS utility before installing the operating system, selecting the RAID level, stripe size, and hot-spare assignment. |
| Server network interfaces (NIC, NIC teaming) | Ethernet adapters that connect the server to the network. Enterprise servers typically have multiple NICs (dual or quad port, 1 Gbps or 10 Gbps). NIC teaming (also called bonding or link aggregation) combines two or more NICs into a single logical interface for increased throughput and fault tolerance -- if one NIC or cable fails, traffic automatically fails over to the remaining link. The administrator configures NIC teaming through the server OS or management utility and assigns VLANs where required. |
| Uninterruptible Power Supply (UPS) | A battery-backed power device that provides temporary power during mains electricity failure, protecting the server from unexpected shutdowns and data corruption. Online/double-conversion UPS provides the highest level of protection by continuously powering the server from the battery and inverter. The UPS management software communicates with the server OS to initiate a graceful shutdown if battery runtime is critically low. The administrator sizes the UPS based on server power consumption (VA/Watts) and required runtime, and schedules regular battery health tests. |
| KVM switch / console | A Keyboard-Video-Mouse switch that allows the administrator to control multiple servers from a single keyboard, monitor, and mouse. Rack-mount KVM switches with LCD displays save space in the data centre. IP-based KVM (KVM over IP) allows remote console access over the network. The administrator uses the KVM for initial BIOS/UEFI configuration, OS installation, and troubleshooting when remote desktop or out-of-band management is unavailable. |
| Server memory (ECC RAM) | Error-Correcting Code memory that detects and corrects single-bit memory errors automatically, preventing data corruption and system crashes. ECC RAM is standard in enterprise servers (DDR5 preferred for high-end systems) and is required by server-class motherboards. The administrator must match memory type (DDR5), speed, and capacity to the motherboard specifications and workload requirements. Memory is installed in matched pairs or sets according to the manufacturer's population rules for optimal performance. |

![RAID Level Comparison](images/raid-levels.png)

![Standard 42U Server Rack Layout](images/server-rack-layout.png)


| Software / Configuration Tool | Description |
|-------------------------------|-------------|
| Windows Server / Linux Server OS | The operating system installed on the server hardware to provide the platform for server roles and services. Windows Server editions (Standard, Datacenter) support Active Directory, Hyper-V, and Microsoft-specific roles. Linux distributions (RHEL, Ubuntu Server, CentOS) are used for web servers, database servers, and open-source environments. The administrator selects the OS based on organisational requirements, licensing, application compatibility, and support availability. |
| Server Manager | A built-in Windows Server management console that provides a single interface for adding and removing roles and features, managing local and remote servers, viewing events and performance data, and running Best Practices Analyser. The administrator uses Server Manager as the primary tool for initial role installation and ongoing server management. Dashboard view provides at-a-glance status of all managed servers. |
| Active Directory Users and Computers (ADUC) | A Microsoft Management Console (MMC) snap-in for managing Active Directory objects -- users, groups, computers, and organisational units (OUs). The administrator creates user accounts, assigns group memberships, resets passwords, and moves objects between OUs. ADUC is the primary tool for day-to-day identity and access management in a Windows domain environment. |
| Hyper-V Manager | The management console for Microsoft Hyper-V virtualisation. Used to create, configure, start, stop, and snapshot virtual machines (VMs). The administrator allocates CPU, memory, storage, and virtual network adapters to each VM based on workload requirements. Hyper-V Manager also supports live migration between hosts and replication for disaster recovery. |
| Remote Desktop (RDP) and Remote Server Administration Tools (RSAT) | Remote Desktop Protocol allows the administrator to connect to and control the server desktop session over the network. RSAT is a collection of management tools (ADUC, DNS Manager, DHCP Manager, Group Policy Management) that can be installed on a workstation to manage servers remotely without logging into the server console. Both reduce the need for physical data centre access and improve administrator efficiency. |
| Backup agent / Windows Server Backup | Software that creates scheduled backups of server data, system state, and virtual machines to local storage, network share, or cloud target. Windows Server Backup is a built-in feature; third-party agents (e.g. Veeam, Acronis) offer advanced features such as deduplication, incremental forever, and granular restore. The administrator configures backup schedules, retention policies, and verifies restore capability through regular test restores. |


| Common Fault | Cause | Action |
|--------------|-------|--------|
| RAID array fails to build or shows degraded status | Incompatible drive (different firmware, capacity, or speed); failed drive not detected; RAID controller firmware outdated | Verify all drives match specifications; reseat drives; update RAID controller firmware; replace failed drive and initiate rebuild; monitor rebuild progress |
| Server role installation fails or role becomes unresponsive | Missing prerequisite role or feature (e.g. AD requires DNS); insufficient disk space or memory; conflicting configuration from previous installation attempt | Check role dependencies in Server Manager; verify system resources; remove incomplete role installation and retry; review event logs for specific error codes |
| DNS misconfiguration causes domain join failure or name resolution issues | Wrong DNS server address configured on clients; forward/reverse lookup zones not created; DNS service not started after AD installation | Verify DNS server IP on all clients; create required DNS zones; check DNS service status; use nslookup and dcdiag to diagnose; flush DNS cache on affected clients |
| Server security hardening blocks legitimate services | Firewall rule blocks required port; unnecessary service disabled that is a dependency for an installed role; overly restrictive Group Policy | Review firewall rules and enable required ports; identify service dependencies using Server Manager; test GPO changes in a test OU before production deployment; document all hardening changes |
| Out-of-band management (iDRAC/iLO) inaccessible | Management NIC not connected to network; management IP not configured or conflicts with another device; default credentials not changed and account locked | Verify physical network connection to management port; configure or correct management IP via BIOS/UEFI; reset credentials using physical server console; ensure management VLAN is correct |


## Learning Outcome Matrix

| Work Activity | Knowledge Outcome | Performance Outcome | Assessment Method | Evidence Required |
|---|---|---|---|---|
| Analyse server configuration requirements | Identify and interpret requirements | Analyse requirements and extract key priorities | Written test on requirement analysis; oral questions on decision criteria | Completed analysis checklist; documented decision rationale |
| Plan server roles and services | Understand concepts related to: Plan server roles and services | Successfully execute: Plan server roles and services | Practical demonstration and documentation review | Completed task documentation and supervisor sign-off |
| Configure server hardware and storage | Understand configuration options and best practices | Configure systems correctly according to requirements | Practical configuration; verification against requirements | Configuration screenshots; settings verification; test proof |
| Configure server OS and roles | Understand configuration options and best practices | Configure systems correctly according to requirements | Practical configuration; verification against requirements | Configuration screenshots; settings verification; test proof |
| Implement server security settings | Understand concepts related to: Implement server security settings | Successfully execute: Implement server security settings | Practical demonstration and documentation review | Completed task documentation and supervisor sign-off |
| Document server configuration | Know documentation standards and requirements | Create complete and accurate documentation | Documentation review; accuracy verification | Completed documentation; review checklist |

## Practical Exercises

The following administrative and supervisory exercise scenarios develop the competencies required for Server Configuration. Each exercise is designed for L4 administrative/supervisory professionals and includes simulation scenarios, planning templates, documentation requirements, and assessment criteria aligned with NOSS standards.

### Lab 1.1: Analysing Server Requirements and Planning

**Objective:** Analyse business requirements and plan a server configuration strategy

**Duration:** 90 minutes

**Resources Required:**
Requirements document template, Server sizing calculator, Active Directory planning worksheet, Hardware specification checklist

**Procedures:**
1. Receive a simulated business requirement: expand file services to 200 users across 3 sites
2. Analyse requirements: identify number of users, storage needs, performance targets, availability requirements, budget
3. Consult vendor documentation for server CPU, memory, storage recommendations
4. Calculate required resources and identify single vs multi-server architecture
5. Design the server configuration including RAID level, backup strategy, and security baseline
6. Create a requirements specification document for stakeholder approval
7. Present recommendation with cost-benefit analysis

**Expected Outcome:**
Approved server configuration specification with justified architectural decisions

**Assessment Checklist:**
[ ] Business requirements clearly documented
[ ] Hardware sizing calculated with vendor specifications
[ ] Architecture decision (single/multi-server) justified
[ ] Cost estimates provided
[ ] Risk assessment completed
[ ] Stakeholder approval obtained

### Lab 1.2: Planning Active Directory and Server Roles

**Objective:** Design an Active Directory structure and plan role distribution across servers

**Duration:** 120 minutes

**Resources Required:**
Active Directory planning template, GPO worksheet, Organisational unit (OU) hierarchy diagram, Role dependency matrix

**Procedures:**
1. Review organisational structure: departments, teams, geographic locations
2. Design OU hierarchy reflecting company structure and delegated administration model
3. Plan role distribution: which server hosts DNS, DHCP, AD, file services, backup
4. Identify role dependencies and installation order
5. Create Group Policy strategy for security and compliance
6. Document naming conventions for computers, users, groups, OUs
7. Design site topology if multi-site deployment
8. Review plan with IT manager and stakeholders

**Expected Outcome:**
Comprehensive AD and role planning document with OU hierarchy, GPO strategy, and implementation roadmap

**Assessment Checklist:**
[ ] OU hierarchy defined and documented
[ ] Role distribution planned with justification
[ ] Role dependencies identified
[ ] Naming conventions defined
[ ] GPO strategy documented
[ ] Implementation sequence planned
[ ] Plan reviewed and approved

### Lab 1.3: Hands-on Server Hardware Configuration

**Objective:** Configure RAID storage and install server components in a lab environment

**Duration:** 120 minutes

**Resources Required:**
Lab server hardware, RAID controller utility, Multiple hard drives, System utilities, Configuration log sheet

**Procedures:**
1. Power on the lab server and enter BIOS/UEFI setup
2. Verify processor, memory, and storage detection
3. Access RAID controller and configure RAID 5 with appropriate stripe size
4. Assign hot spare drive
5. Set boot order and enable/disable secure boot based on requirements
6. Configure power settings (wake-on-LAN, power loss recovery)
7. Record all BIOS settings that deviate from defaults
8. Document hardware configuration for reference

**Expected Outcome:**
Configured server hardware with RAID array built and documented settings

**Assessment Checklist:**
[ ] BIOS/UEFI settings verified and customized
[ ] RAID array successfully built and configured
[ ] Hot spare assigned
[ ] Boot sequence set correctly
[ ] Security features enabled/disabled per requirement
[ ] Configuration documented with photos/screenshots

### Lab 1.4: Installing Windows Server and Adding Roles

**Objective:** Install Windows Server OS and add required server roles following the configuration plan

**Duration:** 180 minutes

**Resources Required:**
Configured lab server, Windows Server installer media, Server roles installation checklist, Configuration documentation

**Procedures:**
1. Boot from Windows Server installer media
2. Perform clean OS installation with appropriate partitioning
3. Configure networking (IP address, DNS, gateway) per plan
4. Install and configure Active Directory Domain Services
5. Install DHCP and configure scope with appropriate settings
6. Install DNS and create zones
7. Add file server role and create shares with permissions
8. Join additional test clients to the domain
9. Verify all roles are functioning correctly

**Expected Outcome:**
Fully functional server with all planned roles installed and verified working

**Assessment Checklist:**
[ ] OS installed successfully
[ ] Network configuration correct
[ ] AD installed and forest/domain created
[ ] DHCP scope functional
[ ] DNS resolving correctly
[ ] File shares accessible with correct permissions
[ ] Client domain join successful
[ ] All roles verified in Server Manager

### Lab 1.5: Server Security Hardening and Group Policy

**Objective:** Apply security hardening baselines and create initial Group Policy Objects

**Duration:** 120 minutes

**Resources Required:**
Server running with roles, Security Compliance Toolkit (Microsoft), Group Policy Management Console, Hardening checklist

**Procedures:**
1. Review CIS Benchmark for Windows Server baseline
2. Disable unnecessary services and features
3. Configure local Group Policy for password policy and account lockout
4. Configure audit policy for account logon, privilege use, and system events
5. Create first-run GPOs for domain-joined computers (eg. antivirus deployment)
6. Configure Windows Defender exclusions and update schedule
7. Enable Windows Firewall rules for required services
8. Configure BitLocker for sensitive partitions
9. Run security baseline scanning tool to identify remaining gaps

**Expected Outcome:**
Hardened server with baseline security controls and initial GPO infrastructure in place

**Assessment Checklist:**
[ ] CIS Benchmark reviewed and documented
[ ] Unnecessary services disabled
[ ] Password policy configured
[ ] Audit policy enabled
[ ] Initial GPOs created and linked
[ ] Firewall rules enabled for services
[ ] Antivirus configured
[ ] Security baseline scan shows improvement

### Lab 1.6: Creating Configuration Documentation and Runbooks

**Objective:** Complete comprehensive documentation for operations and disaster recovery

**Duration:** 90 minutes

**Resources Required:**
Configured and hardened server, Documentation template, Runbook template, Network diagram tool

**Procedures:**
1. Create server asset record with hostname, IP, OS version, serial numbers
2. Document all installed roles and features with versions
3. Create network diagram showing server, network segments, and connectivity
4. Document Active Directory structure (forest, domains, OUs, trust relationships)
5. Create DHCP scope and DNS zone documentation
6. Create troubleshooting runbook for common issues
7. Create disaster recovery runbook for rebuilding the server
8. Document change history and approval signatures
9. Store documentation in a centralized location with version control

**Expected Outcome:**
Complete documentation package including asset record, network diagram, runbooks, and change history

**Assessment Checklist:**
[ ] Asset information recorded
[ ] All roles and features documented
[ ] Network topology diagram created
[ ] AD structure documented
[ ] Troubleshooting runbook completed
[ ] Disaster recovery runbook completed
[ ] Change history and approvals recorded
[ ] Documentation stored and indexed



## Employability Skills

This CoCu develops the following employability skills through the work activities:

### 1. Communication Skills
- **Mapping:** Document planning and implementation decisions; present recommendations to management; communicate with stakeholders and project teams

### 2. Teamwork & Collaboration
- **Mapping:** Lead technical teams on implementation; coordinate across departments; share knowledge on best practices and systems management

### 3. Problem-solving
- **Mapping:** Diagnose complex system issues; evaluate solution options; implement sustainable fixes and preventive measures

### 4. Initiative & Self-reliance
- **Mapping:** Take responsibility for technical decisions; manage implementation projects; supervise technical staff

### 5. Planning & Organizing
- **Mapping:** Plan system implementations and configurations; organize resources and schedules; manage project timelines and budgets

### 6. Self-management & Safety Awareness
- **Mapping:** Follow change management and approval procedures; manage risk of system downtime; maintain security and compliance standards

### 7. Technology Use & Technical Proficiency
- **Mapping:** Configure complex systems; troubleshoot using advanced tools; manage system infrastructure and databases

### 8. Learning Skills & Continuous Improvement
- **Mapping:** Stay current on new technologies and standards; analyze implementation results; improve procedures and documentation



## Attitude, Safety and Environmental

### Workplace Safety
- **Change Management and Approval:** Always follow formal change management procedures before implementing server configurations or updates. Obtain required approvals and communicate changes to stakeholders to avoid unexpected downtime.
- **Risk Management:** Assess security risks when configuring server roles and implement hardening measures to protect against known vulnerabilities and attack vectors.
- **Data Protection Compliance:** Handle server security configuration in accordance with data protection regulations (e.g., PDPA, GDPR) and organisational security policies. Ensure proper access controls and audit logging are in place.
- **Documentation and Knowledge Sharing:** Maintain comprehensive documentation of all server configurations, changes, and troubleshooting procedures to support team knowledge and ensure continuity during staff transitions.

### Environmental Considerations
- **Sustainable IT Practices:** Plan for efficient resource utilisation (power, cooling, storage) when configuring server environments. Consider virtualisation and consolidation to reduce physical hardware footprint and energy consumption.
- **Responsible Asset Disposal:** Ensure decommissioned servers and storage devices are securely wiped and responsibly recycled through certified e-waste facilities.

### Professional Attitudes
- **Ethical Decision-Making:** Make recommendations based on technical merit and organisational benefit, not vendor preferences or personal convenience. Maintain transparency with stakeholders about trade-offs and costs.
- **Continuous Learning:** Stay current with new server technologies, security standards, and industry best practices to make informed decisions about infrastructure improvements.
- **Team Leadership:** Lead technical teams with respect and clear communication; ensure team members understand the rationale behind decisions and have opportunity to contribute expertise.
- **Accountability:** Take responsibility for system stability and performance; proactively monitor configurations and respond quickly to issues that could impact business operations.

## References

**Official Standards and Frameworks:**

- NOSS IT-020-4:2013 Computer System Administration Syllabus
- Microsoft Windows Server 2025 Administration and Deployment Guide
- Red Hat Enterprise Linux 9 System Administrator Reference (RHEL)
- Ubuntu Server 24.04 LTS Installation and Administration Guide
- Dell PowerEdge Server Administration Guide – iDRAC, iLO, BMC Configuration

**Technical References and Best Practices:**

- CompTIA Server+ Certification Study Guide – Advanced Server Administration
- Hyper-V Server Virtualization Administration and Cluster Configuration
- VMware vSphere 8 Installation, Configuration and Management
- Amazon Web Services (AWS) EC2 Instance Configuration and Best Practices
- Microsoft Azure Virtual Machines – Deployment and Administration

**Contact hour:** [[00_Contact-hour_IT-020-4-L4-Administration]]


---

↑ [README](../../README.md) · **IT-020-4** > CoCu 1 - Server Configuration

**In this level:** [00_Contact-hour](00_Contact-hour_IT-020-4-L4-Administration.md) · [00_standard-practice](00_standard-practice.md) · [02_CoCu-2](02_CoCu-2-Computer-System-Security-Control.md) · [03_CoCu-3](03_CoCu-3-System-Network-Procurement.md) · [04_CoCu-4](04_CoCu-4-Network-Cabling-Management.md) · [05_CoCu-5](05_CoCu-5-Computer-Network-Installation-Management.md) · [06_CoCu-6](06_CoCu-6-Computer-System-Maintenance-Management.md)

**Other levels:** [IT-020-3 (L3)](../IT-020-3/00_Contact-hour_IT-020-3-L3-Operation.md) · [IT-020-5 (L5)](../IT-020-5/00_Contact-hour_IT-020-5-L5-Management.md)
