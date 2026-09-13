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
| KOD DAN NAMA PROGRAM | IT-020-3:2013 OPERASI SISTEM KOMPUTER |
| TAHAP | 3 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C04 SERVER INSTALLATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE JOB ORDER/CHANGE REQUEST<br>2. EXECUTE HARDWARE INSTALLATION<br>3. CARRY OUT SOFTWARE INSTALLATION<br>4. PERFORM SERVER FUNCTIONALITY TEST<br>5. PREPARE SERVER INSTALLATION SET-UP REPORT |
| NO. KOD | IT-020-3:2013-C04/KP(3/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-03-server-software-installation

**TUJUAN:** Kertas rujukan untuk KP-03-server-software-installation.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Identify the major server operating systems and select the appropriate edition for the deployment scenario
2. Prepare installation media and configure BIOS/UEFI boot settings for OS installation
3. Perform a clean installation of Windows Server and a Linux server distribution
4. Configure post-installation settings — hostname, IP address, domain membership, time zone, and updates
5. Install and configure common server roles and services (AD DS, DNS, DHCP, File Server, Web Server)
6. Harden the server OS against common security threats following post-installation best practices

---

## 1.0 Server Operating Systems Overview

A **server operating system (sistem operasi pelayan)** is designed to manage network resources, provide services to client computers, handle multi-user workloads, and operate continuously without interruption. Server OSes differ from desktop OSes in stability, security, licensing model, and feature set.

### 1.1 Major Server OS Families

| Operating System | Publisher | Kernel | Typical Use Case |
|-----------------|-----------|--------|-----------------|
| Windows Server 2022 | Microsoft | Windows NT | Active Directory, enterprise applications, hybrid cloud (Azure Arc) |
| Windows Server 2019 | Microsoft | Windows NT | General enterprise; long-term servicing channel |
| Windows Server 2016 | Microsoft | Windows NT | Legacy enterprise; upgrading to 2019/2022 recommended |
| Red Hat Enterprise Linux (RHEL) | Red Hat (IBM) | Linux | Enterprise workloads, SAP, Oracle DB; commercial support |
| Ubuntu Server LTS | Canonical | Linux | Web hosting, DevOps, cloud-native, open-source workloads |
| Rocky Linux / AlmaLinux | Community | Linux | Free RHEL-compatible; replaces CentOS in many deployments |
| SUSE Linux Enterprise Server (SLES) | SUSE | Linux | SAP workloads, European enterprise market |
| VMware ESXi | Broadcom | VMkernel | Bare-metal hypervisor; hosts multiple VMs |

### 1.2 Windows Server Editions

| Edition | Virtualisation Rights | Target Deployment |
|---------|----------------------|------------------|
| Essentials | 1 VM | Small organisations; ≤25 users, ≤50 devices |
| Standard | 2 VMs per licence | Physical or lightly virtualised deployments |
| Datacenter | Unlimited VMs per licence | Highly virtualised data centres; cloud-ready |

> **Note:** Windows Server requires **Client Access Licences (CALs)** for each user or device that accesses server services. The number of CALs must match the organisation's user/device count.

---

## 2.0 Pre-Installation Preparation

### 2.1 BIOS/UEFI Configuration

Before installing the OS, configure the server BIOS/UEFI settings:

| Setting | Recommended Configuration |
|---------|--------------------------|
| Boot mode | UEFI (preferred for Windows Server 2016+ and modern Linux); Legacy BIOS only if specifically required |
| Secure Boot | Enable for Windows Server; verify Linux distribution supports Secure Boot if enabling |
| Boot order | Set first boot device to USB/DVD for installation; revert to HDD/SSD after OS installation |
| Virtualisation extensions | Enable Intel VT-x / AMD-V and Intel VT-d / AMD-Vi if deploying a hypervisor or Hyper-V |
| RAID mode | Set storage controller to RAID mode (not AHCI/HBA) if using hardware RAID |
| Date and time | Set to correct local time; configure NTP server address if available in BIOS |
| Hyperthreading | Enable (default); disable only for specific workloads that require physical core isolation |

### 2.2 Installation Media Preparation

| Method | Procedure |
|--------|-----------|
| USB bootable drive | Use Rufus (Windows) or `dd` (Linux) to write the OS ISO to a USB drive (minimum 8 GB, USB 3.0 recommended). For Windows Server, use UEFI-compatible ISO writing mode. |
| PXE (Preboot eXecution Environment) | Boot server from network; OS image served from a WDS (Windows Deployment Services) or PXE server. Requires PXE-enabled NIC and DHCP/TFTP infrastructure. |
| Virtual media (BMC) | Mount ISO from the administrator's PC via iDRAC/iLO virtual media — no physical USB required. Useful for remote installations. |
| DVD optical media | Least common; use only if no USB or network boot is available |

---

## 3.0 Windows Server Installation

### 3.1 Installation Procedure

| Step | Action |
|------|--------|
| 1 | Boot from installation media; select language, time format, and keyboard input method |
| 2 | Click **Install now**; enter product key (or skip and activate later for volume licence environments) |
| 3 | Select edition: Standard (Desktop Experience) or Datacenter (Desktop Experience); choose **Desktop Experience** for GUI or **Core** for command-line only installation |
| 4 | Accept the licence agreement |
| 5 | Select **Custom: Install Windows only (advanced)** for a clean installation |
| 6 | Select the target disk; if using hardware RAID, the RAID logical volume appears as a single disk. If the disk is not visible, load the RAID controller driver using **Load driver** |
| 7 | Partition the disk: Windows requires a System Reserved partition (EFI, ~100 MB), an MSR partition (~16 MB), and the primary OS partition (minimum 40 GB; recommended 100 GB+) |
| 8 | Proceed with installation; server reboots multiple times |
| 9 | Set the local Administrator password on first boot |

### 3.2 Post-Installation Configuration (Windows Server)

After the OS installation completes, perform the following configuration steps in sequence:

**Step 1: Set Computer Name (Nama Komputer)**
- Server Manager → Local Server → Computer Name → Change
- Use a standardised naming convention (e.g. `SRV-AD-01`, `SRV-FILE-02`)
- Reboot after renaming

**Step 2: Configure IP Address (Alamat IP)**
- Network and Sharing Centre → Change adapter settings → Right-click NIC → Properties → IPv4
- Assign static IP address, subnet mask, default gateway, and DNS server addresses as per job order
- For server NICs: always use static IP; do not rely on DHCP

**Step 3: Set Time Zone (Zon Masa)**
- Server Manager → Local Server → Time Zone → Set to Asia/Kuala_Lumpur (UTC+8)
- Configure Windows Time service to sync with an NTP server (domain member servers sync with domain controller)

**Step 4: Activate Windows**
- Settings → Update & Security → Activation → Activate with product key (or via KMS for volume licence)
- Verify activation status before proceeding

**Step 5: Install Updates (Kemas Kini)**
- Windows Update → Check for updates → Install all critical and security updates
- Reboot as required

**Step 6: Install Hardware Drivers**
- Install vendor-specific drivers for RAID controller, NIC, BMC/iDRAC management agent, and any additional expansion cards
- Use the vendor's System Update utility (e.g. Dell OpenManage, HPE Service Pack for ProLiant) to batch-install all recommended drivers and firmware

---

## 4.0 Linux Server Installation (Ubuntu Server LTS)

### 4.1 Installation Procedure

| Step | Action |
|------|--------|
| 1 | Boot from Ubuntu Server ISO; select language |
| 2 | Choose keyboard layout |
| 3 | Select installation type: **Ubuntu Server** (standard) or **Ubuntu Server (minimized)** |
| 4 | Configure network interfaces: set static IP or DHCP as per job order. Ubuntu Server uses **Netplan** for network configuration |
| 5 | Configure proxy if required by the organisation's network |
| 6 | Proceed with default Ubuntu archive mirror (or set to a local mirror for faster downloads) |
| 7 | Configure guided storage layout: use entire disk, optionally enable LVM (Logical Volume Manager) for flexible disk management. Set up RAID at OS level (mdadm) or rely on hardware RAID controller |
| 8 | Create the primary administrator user account (username and password) |
| 9 | Enable **OpenSSH server** installation during setup — this allows remote management via SSH immediately after installation |
| 10 | Select additional snaps if required (none required for a minimal server base) |
| 11 | Confirm and proceed; server reboots after installation |

### 4.2 Post-Installation Configuration (Ubuntu Server)

**Step 1: Update all packages**
```bash
sudo apt update && sudo apt upgrade -y
```

**Step 2: Set hostname**
```bash
sudo hostnamectl set-hostname srv-file-01
```

**Step 3: Configure static IP (Netplan)**

Edit `/etc/netplan/00-installer-config.yaml`:
```yaml
network:
  version: 2
  ethernets:
    ens3:
      addresses:
        - 192.168.10.20/24
      gateway4: 192.168.10.1
      nameservers:
        addresses: [192.168.10.10, 8.8.8.8]
```
Apply: `sudo netplan apply`

**Step 4: Set time zone**
```bash
sudo timedatectl set-timezone Asia/Kuala_Lumpur
```

**Step 5: Configure NTP**
```bash
sudo systemctl enable systemd-timesyncd
sudo timedatectl set-ntp true
```

**Step 6: Configure firewall (UFW)**
```bash
sudo ufw allow OpenSSH
sudo ufw enable
```

---

## 5.0 Server Roles and Services

Server roles are specific functions the server is configured to provide to the network. The roles to install are specified in the job order.

### 5.1 Active Directory Domain Services (AD DS)

**Active Directory Domain Services (AD DS)** is the directory service used in Windows networks to manage users, computers, and policies centrally. A server running AD DS is called a **Domain Controller (DC / Pengawal Domain)**.

| Concept | Description |
|---------|-------------|
| Domain (Domain) | A logical grouping of network objects (users, computers, groups) managed under a single administrative authority |
| Forest (Hutan) | The top-level container in AD; a collection of one or more domains sharing a common schema |
| Organisational Unit (OU) | A container within a domain used to organise objects and apply Group Policy |
| Group Policy (Dasar Kumpulan) | Settings applied to users and computers in an OU; controls security, software deployment, and desktop configuration |
| FSMO Roles | Flexible Single Master Operation roles — five special DC roles (PDC Emulator, RID Master, Infrastructure Master, Schema Master, Domain Naming Master) |

**Installing AD DS on Windows Server:**
1. Server Manager → Add Roles and Features → Server Roles → **Active Directory Domain Services**
2. After installation, click **Promote this server to a domain controller**
3. Select: Add a new forest (for first DC) or Add a DC to an existing domain
4. Set Forest Functional Level and Domain Functional Level
5. Set Directory Services Restore Mode (DSRM) password
6. Verify DNS delegation and NetBIOS domain name
7. Review prerequisites and proceed; server reboots as a domain controller

### 5.2 DNS (Domain Name System)

**DNS** resolves hostnames to IP addresses. It is installed automatically with AD DS. For standalone DNS:

- Server Manager → Add Roles and Features → **DNS Server**
- Configure forward lookup zones (hostname → IP) and reverse lookup zones (IP → hostname)
- Set forwarders to upstream DNS servers (e.g. 8.8.8.8 for internet resolution)

On Linux (Ubuntu):
```bash
sudo apt install bind9 bind9utils -y
```
Configure zones in `/etc/bind/named.conf.local`

### 5.3 DHCP (Dynamic Host Configuration Protocol)

**DHCP** automatically assigns IP addresses to client devices.

**Windows Server DHCP installation:**
1. Server Manager → Add Roles and Features → **DHCP Server**
2. Post-install: Authorise DHCP server in Active Directory (prevents rogue DHCP servers)
3. Create a DHCP scope: define IP address range, subnet mask, default gateway, DNS server, and lease duration

**DHCP scope best practices:**
- Exclude the first 20 addresses for static assignments (servers, printers, network devices)
- Set lease duration to 8 hours for office environments (24 hours for stable environments)
- Enable DHCP failover for high-availability deployments (pair with a second DHCP server)

### 5.4 File Server and File Server Resource Manager (FSRM)

**File Server** role enables shared folders accessible by network users.

| Feature | Function |
|---------|----------|
| Shared Folders (Folder Dikongsi) | Network-accessible folders; permissions set via NTFS and share-level permissions |
| DFS (Distributed File System) | Provides a unified namespace for shares across multiple servers; supports replication |
| FSRM (File Server Resource Manager) | Quota management, file screening (block executable uploads), storage reports |
| Shadow Copies (Salinan Bayangan) | Scheduled snapshots of shared folders; allows users to self-recover previous file versions |

### 5.5 Web Server (IIS — Internet Information Services)

**IIS** is Microsoft's web server for hosting websites and web applications.

- Server Manager → Add Roles and Features → **Web Server (IIS)**
- Default website accessible at `http://<server-ip>/`
- Configure site bindings (IP, port, hostname), application pools, and authentication as required

On Linux (Ubuntu):
```bash
sudo apt install apache2 -y          # Apache HTTP Server
sudo apt install nginx -y            # Nginx (alternative)
sudo systemctl enable apache2
sudo systemctl start apache2
```

---

## 6.0 Post-Installation Security Hardening

After all roles are installed and configured, apply the following security hardening measures:

| Hardening Action | Windows Server | Linux (Ubuntu) |
|-----------------|---------------|----------------|
| Rename or disable default admin account | Rename built-in Administrator account; disable Guest account | Lock root account: `sudo passwd -l root`; use sudo for admin tasks |
| Set strong password policy | Group Policy → Password Policy: min. 12 chars, complexity, 90-day expiry | Configure via PAM: `/etc/pam.d/common-password`; install `libpam-pwquality` |
| Enable firewall | Windows Defender Firewall: allow only required ports | UFW: allow only required services; deny all by default |
| Disable unnecessary services | Server Manager: remove unused roles; Services: set unnecessary services to Disabled | `sudo systemctl disable <service>`; remove unused packages |
| Configure automatic updates | Windows Update: enable automatic security updates; or use WSUS for enterprise | `sudo apt install unattended-upgrades`; configure for security updates only |
| Enable audit logging | Local Security Policy → Audit Policy: enable logon, object access, privilege use events | Enable auditd: `sudo apt install auditd`; configure rules in `/etc/audit/audit.rules` |
| NTP synchronisation | Configure W32tm to sync with domain or external NTP server | `timedatectl set-ntp true`; configure NTP servers in `/etc/systemd/timesyncd.conf` |
| SSH hardening (Linux) | N/A | Edit `/etc/ssh/sshd_config`: disable root login (`PermitRootLogin no`), disable password auth if using key-based auth, change default port if required |

---

## 7.0 Common Errors in Server Software Installation

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Installing GUI (Desktop Experience) when Core was required | Unnecessary attack surface; more patching required | Confirm edition and installation type with job order before starting |
| Using static IP on the wrong NIC | Server unreachable from the network | Identify NIC port assignments before configuring — check MAC address or cable labelling |
| Not activating Windows before configuring roles | Reduced functionality after grace period (180 days); some features restricted | Activate immediately after installation or confirm KMS activation is working |
| Promoting DC without setting correct domain functional level | Cannot use newer AD features; incompatible with existing domain | Confirm forest/domain functional level with job order and existing AD environment |
| Not installing latest drivers before OS roles | NIC or RAID instability; blue screen or storage errors | Install all vendor drivers and firmware updates before adding server roles |
| Skipping firewall configuration | Server exposed to network attacks | Configure firewall as part of standard post-installation hardening — do not skip |
| Wrong time zone or NTP misconfiguration | Kerberos authentication failures (AD DS requires clocks within 5 minutes of each other) | Set time zone and NTP before promoting to domain controller |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCU 4: Server Installation
- Microsoft Learn — Windows Server documentation: https://docs.microsoft.com/en-us/windows-server/
- Ubuntu Server Guide: https://ubuntu.com/server/docs
- CompTIA Server+ Study Guide (SK0-005) — Chapter on Server OS Installation and Configuration
- CIS Benchmarks for Windows Server 2022 and Ubuntu Server LTS (Centre for Internet Security)
- Microsoft Active Directory Best Practices Guide