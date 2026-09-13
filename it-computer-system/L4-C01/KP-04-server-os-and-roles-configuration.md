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
| NO. KOD | IT-020-4:2013-C01/KP(4/6) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** Install the AD DS role and management tools

**TUJUAN:** Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools ```

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Perform a production-ready installation of Windows Server or Linux for a server environment
2. Apply post-installation configuration steps required before enabling server roles
3. Install and configure Active Directory Domain Services (AD DS) and DNS
4. Install and configure the File Services role including DFS Namespace
5. Configure remote management tools for ongoing server administration
6. Verify role functionality using appropriate diagnostic tools and commands

---

## 1.0 OS Selection for Production Servers

The choice of server operating system is driven by the application requirements, existing infrastructure, licensing budget, and the organisation's skills profile:

| OS | Edition | Typical Use Case |
|----|---------|-----------------|
| **Windows Server 2022 Standard** | Up to 2 VMs per license | General-purpose; small-medium virtualisation |
| **Windows Server 2022 Datacenter** | Unlimited VMs per license | Large-scale virtualisation; high-density VM farms |
| **Windows Server 2022 Essentials** | ≤25 users, ≤50 devices | SMB; replaces SBS; no VMs included |
| **Red Hat Enterprise Linux (RHEL) 9** | Subscription-based | Enterprise Linux; vendor-certified; paid support |
| **Ubuntu Server 22.04 LTS** | Free; Canonical support available | Web, database, containerised workloads; cloud-native |
| **Rocky Linux / AlmaLinux** | Free RHEL-compatible | RHEL-compatible without subscription cost |

**Key rule:** Select Server Core (GUI-less) for Windows Server where possible — smaller attack surface, lower memory footprint, fewer patches required.

---

## 2.0 Windows Server Installation Procedure

### 2.1 Pre-Installation Checklist

| Item | Action |
|------|--------|
| BIOS/UEFI settings | Verified (Secure Boot, VT-x, boot order) — see KP-03 |
| RAID configured | Logical drives created and initialised |
| Installation media | Bootable USB or PXE server ready |
| Product key | Available (or KMS server configured for volume activation) |
| IP address plan | Static IP, subnet, gateway, DNS assigned |
| Hostname | Naming convention agreed (e.g. SRV-DC01, SRV-FILE01) |

### 2.2 Installation Steps

1. Boot from installation media; select language, time, and keyboard
2. Choose edition: **Windows Server 2022 Standard (Desktop Experience)** or **Server Core**
3. Accept licence terms; choose **Custom: Install Windows only**
4. Select the target logical drive (verify it is the correct RAID volume by size)
5. Installation proceeds and server reboots automatically
6. Set the local Administrator password (minimum 14 characters: upper, lower, number, symbol)
7. **Do NOT join domain** at this stage — complete all post-installation steps first

### 2.3 Post-Installation Configuration (Server Manager / PowerShell)

Perform these steps in order before enabling any roles:

| Step | Action | Command (PowerShell) |
|------|--------|---------------------|
| 1 | Set static IP address | `New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress 10.0.1.10 -PrefixLength 24 -DefaultGateway 10.0.1.1` |
| 2 | Set DNS server | `Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses 10.0.1.1,8.8.8.8` |
| 3 | Rename the computer | `Rename-Computer -NewName "SRV-DC01" -Restart` |
| 4 | Set timezone | `Set-TimeZone -Name "Malay Peninsula Standard Time"` |
| 5 | Sync time to NTP | `w32tm /config /manualpeerlist:"time.windows.com" /syncfromflags:manual /reliable:yes /update` |
| 6 | Enable Remote Desktop | `Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name "fDenyTSConnections" -Value 0` |
| 7 | Enable Windows Firewall exception for RDP | `Enable-NetFirewallRule -DisplayGroup "Remote Desktop"` |
| 8 | Install Windows Updates | `Install-Module PSWindowsUpdate; Get-WindowsUpdate -Install -AcceptAll` |
| 9 | Enable Windows Remote Management (WinRM) | `Enable-PSRemoting -Force` |

---

## 3.0 Configuring Active Directory Domain Services (AD DS)

### 3.1 Overview

Active Directory Domain Services (AD DS) provides centralised authentication, authorisation, and policy management for all domain-joined computers and users. The server hosting AD DS is called a **Domain Controller (DC)**.

### 3.2 Installing the AD DS Role

```powershell
# Install the AD DS role and management tools
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools
```

### 3.3 Promoting the Server to Domain Controller

For a **new forest and domain:**

```powershell
Install-ADDSForest `
  -DomainName "pioneer.edu.my" `
  -DomainNetbiosName "PIONEER" `
  -ForestMode "WinThreshold" `
  -DomainMode "WinThreshold" `
  -InstallDns:$true `
  -SafeModeAdministratorPassword (ConvertTo-SecureString "P@ssw0rd!2026" -AsPlainText -Force) `
  -Force
```

For **adding a second DC to an existing domain:**

```powershell
Install-ADDSDomainController `
  -DomainName "pioneer.edu.my" `
  -InstallDns:$true `
  -Credential (Get-Credential) `
  -SafeModeAdministratorPassword (ConvertTo-SecureString "P@ssw0rd!2026" -AsPlainText -Force) `
  -Force
```

### 3.4 Verifying AD DS and DNS

```powershell
# Verify DC replication
repadmin /showrepl

# Verify DNS zones
Get-DnsServerZone

# Test AD DS
dcdiag /test:dns /v

# List domain controllers
Get-ADDomainController -Filter *
```

### 3.5 Organisational Unit (OU) Design

Plan the OU structure before creating accounts:

```
pioneer.edu.my
├── _Computers
│   ├── Servers
│   ├── Workstations
│   └── Laptops
├── _Users
│   ├── Staff
│   ├── Students
│   └── Service Accounts
└── _Groups
    ├── Security
    └── Distribution
```

**Key rule:** Group Policy Objects (GPOs) are linked at the OU level. Design the OU structure to align with how GPOs will be applied (by department, function, or location).

---

## 4.0 Configuring DNS Server Role

DNS (Domain Name System / Sistem Nama Domain) is automatically installed with AD DS. Additional configuration:

| Task | Detail |
|------|--------|
| **Forward Lookup Zone** | Created automatically during AD DS promotion (e.g. `pioneer.edu.my`) |
| **Reverse Lookup Zone** | Must be created manually: right-click Reverse Lookup Zones → New Zone → enter network ID (e.g. 10.0.1) |
| **Conditional Forwarders** | Forward DNS queries for external zones (e.g. `vendor.com`) to specific DNS servers |
| **Root Hints or Forwarders** | Configure forwarders to public DNS (8.8.8.8, 1.1.1.1) for internet name resolution |
| **Scavenging** | Enable DNS scavenging to remove stale records: `Set-DnsServerScavenging -ScavengingState $true -ScavengingInterval 7.00:00:00` |

---

## 5.0 Configuring File Services Role

### 5.1 Installing File Services

```powershell
Install-WindowsFeature -Name FS-FileServer, FS-DFS-Namespace, FS-DFS-Replication -IncludeManagementTools
```

### 5.2 Creating Shared Folders

```powershell
# Create folder
New-Item -ItemType Directory -Path "D:\Shares\Departments"

# Create SMB share
New-SmbShare -Name "Departments" -Path "D:\Shares\Departments" `
  -FullAccess "PIONEER\Domain Admins" `
  -ChangeAccess "PIONEER\Domain Users" `
  -Description "Departmental shared folders"
```

### 5.3 NTFS Permissions vs Share Permissions

| Permission Type | Scope | Notes |
|----------------|-------|-------|
| **Share Permissions** | Apply only when accessing over the network | Keep simple: Domain Users = Change; Domain Admins = Full Control |
| **NTFS Permissions** | Apply always (local and network access) | Use NTFS permissions for fine-grained access control; inheritance is key |

**Best practice:** Set Share Permissions to "Everyone = Full Control" and control access exclusively through NTFS permissions. This simplifies management.

### 5.4 DFS Namespace Configuration

DFS Namespace (Ruang Nama DFS) provides a unified namespace for shared folders distributed across multiple servers:

```
\\pioneer.edu.my\Shares\Departments  →  \\SRV-FILE01\Departments
\\pioneer.edu.my\Shares\IT            →  \\SRV-FILE01\IT
\\pioneer.edu.my\Shares\HR            →  \\SRV-FILE02\HR
```

Users access `\\pioneer.edu.my\Shares` regardless of which physical file server hosts the data.

---

## 6.0 Configuring DHCP Server Role

```powershell
# Install DHCP role
Install-WindowsFeature -Name DHCP -IncludeManagementTools

# Authorise DHCP server in AD
Add-DhcpServerInDC -DnsName "SRV-DC01.pioneer.edu.my" -IPAddress 10.0.1.10

# Create DHCP scope
Add-DhcpServerv4Scope -Name "LAN-Scope" -StartRange 10.0.1.100 `
  -EndRange 10.0.1.250 -SubnetMask 255.255.255.0

# Configure scope options
Set-DhcpServerv4OptionValue -ScopeId 10.0.1.0 `
  -Router 10.0.1.1 -DnsServer 10.0.1.10 -DnsDomain "pioneer.edu.my"
```

---

## 7.0 Remote Management Configuration

### 7.1 Windows Admin Center (WAC)

Windows Admin Center is a browser-based management tool for Windows Server that replaces many legacy MMC snap-ins. Install on a management workstation or a dedicated gateway server.

- Download from: https://aka.ms/windowsadmincenter
- Manage servers, failover clusters, and Hyper-V hosts without RDP

### 7.2 PowerShell Remoting

```powershell
# From management workstation: establish remote session
Enter-PSSession -ComputerName SRV-DC01 -Credential (Get-Credential)

# Run command on remote server
Invoke-Command -ComputerName SRV-DC01 -ScriptBlock { Get-Service -Name NTDS }
```

### 7.3 Remote Server Administration Tools (RSAT)

Install RSAT on the administrator's workstation to manage AD, DNS, DHCP, and File Services without logging on to each server:

```powershell
Get-WindowsCapability -Name RSAT* -Online | Add-WindowsCapability -Online
```

---

## 8.0 Verification After Role Configuration

| Verification Test | Tool / Command | Expected Result |
|------------------|---------------|----------------|
| Domain Controller promotion successful | `dcdiag /v` | All tests PASSED |
| DNS resolution working | `nslookup pioneer.edu.my 10.0.1.10` | Returns DC IP address |
| AD replication healthy | `repadmin /replsummary` | No errors; replication delta < 15 min |
| DHCP scope active and leasing | DHCP Manager → Scope Statistics | Leases being assigned |
| File share accessible | `net use * \\pioneer.edu.my\Shares\Departments /user:PIONEER\testuser` | Drive mapped successfully |
| WinRM accessible | `Test-WSMan -ComputerName SRV-DC01` | Returns WinRM configuration |

---

## 9.0 Common Errors in OS and Role Configuration

| Error | Consequence | Prevention |
|-------|-------------|------------|
| **Joining domain before OS hardening** | Domain join registers unhardened computer object; policies applied too late | Complete all post-install steps and patching before domain join |
| **Single DNS server configured** | If DNS server fails, all domain lookups fail; network appears down | Always configure two DNS servers (primary and secondary DC) |
| **DHCP server not authorised in AD** | Rogue DHCP server protection: unauthorised DHCP is silenced by AD | Authorise DHCP server using `Add-DhcpServerInDC` |
| **NTFS permissions set incorrectly** | Excessive access (security risk) or insufficient access (helpdesk calls) | Follow least-privilege principle; test with a standard user account |
| **No reverse DNS zone** | Some applications (SMTP, Kerberos) fail reverse lookups; diagnostic tools show IP instead of hostname | Create reverse lookup zone immediately after AD DS promotion |
| **Windows Updates not applied before go-live** | Known vulnerabilities exploitable from day one | Apply all available updates; reboot; verify via `Get-HotFix` before go-live |

---

## Rujukan / References

- NOSS IT-020-4:2013 Computer Systems Administration — CoCu 1: Server Configuration
- Microsoft Learn — Install and Configure Active Directory: https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/
- Microsoft Learn — Windows Server 2022 Documentation: https://docs.microsoft.com/en-us/windows-server/
- DHCP Server Role — Microsoft Docs: https://docs.microsoft.com/en-us/windows-server/networking/technologies/dhcp/
- Windows Admin Center Documentation: https://docs.microsoft.com/en-us/windows-server/manage/windows-admin-center/