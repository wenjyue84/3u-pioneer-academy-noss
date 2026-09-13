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
| KOD DAN NAMA PROGRAM | IT-020-4:2013 PENTADBIRAN SISTEM KOMPUTER |
| TAHAP | 4 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C01 SERVER CONFIGURATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE SERVER CONFIGURATION REQUIREMENTS<br>2. PLAN SERVER ROLES AND SERVICES<br>3. CONFIGURE SERVER HARDWARE AND STORAGE<br>4. CONFIGURE SERVER OS AND ROLES<br>5. IMPLEMENT SERVER SECURITY SETTINGS<br>6. DOCUMENT SERVER CONFIGURATION |
| NO. KOD | IT-020-4:2013-C01/KK(4/6) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-04-configuring-server-os-and-roles

**TUJUAN:** Kertas rujukan untuk KK-04-configuring-server-os-and-roles.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

Install Windows Server 2022 on the configured server, apply all required post-installation settings, promote the server to a domain controller with Active Directory Domain Services and DNS, configure the DHCP server role, and verify all roles using diagnostic commands.

---

## Tempoh / Duration

10 hours (practical session)

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Server with RAID configured (from KK-03) | 1 |
| 2 | Bootable USB with Windows Server 2022 ISO | 1 |
| 3 | Volume licence key or evaluation activation access | 1 |
| 4 | Network switch with VLAN configuration (Production and Management) | 1 (shared) |
| 5 | Management workstation with RSAT tools installed | 1 (shared) |
| 6 | IP address assignment sheet (from Server Role Plan) | 1 |
| 7 | Post-installation configuration checklist (from KP-04) | 1 |
| 8 | PowerShell reference card | 1 |

---

## Langkah Keselamatan / Safety Precautions

- Do NOT join the domain before completing all post-installation hardening steps
- Do NOT use a privileged domain account for non-administrative tasks
- Record every PowerShell command executed and its result — this forms part of the evidence for assessment
- Verify the RAID logical drive target before starting OS installation — selecting the wrong disk is irreversible during installation

---

## Prosedur / Procedures

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 1 | **OS Installation:** Boot from the Windows Server 2022 USB. Select language: English, Time: Malay Peninsula Standard Time, Keyboard: US. Select edition: Windows Server 2022 Standard (Desktop Experience). Choose Custom install. Select the OS-RAID1 logical drive (verify size matches). Allow installation to complete and reboot. Set the local Administrator password (minimum 14 characters, complex). |
| 2 | **Static IP configuration (PowerShell):** Open PowerShell as Administrator. Run: `Get-NetAdapter` to identify the interface alias. Set the static IP per the IP assignment sheet: `New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress <IP> -PrefixLength 24 -DefaultGateway <GW>`. Set DNS: `Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses <DNS1>,<DNS2>`. Verify with `ipconfig /all`. |
| 3 | **Computer rename and timezone:** Rename: `Rename-Computer -NewName "SRV-DC01" -Restart`. After restart, set timezone: `Set-TimeZone -Name "Malay Peninsula Standard Time"`. Verify: `Get-TimeZone`. |
| 4 | **NTP configuration:** Configure time synchronisation: `w32tm /config /manualpeerlist:"time.windows.com" /syncfromflags:manual /reliable:yes /update` then `Restart-Service w32tm`. Verify: `w32tm /query /status`. Record stratum and source. |
| 5 | **Enable Remote Desktop and WinRM:** Enable RDP: `Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name "fDenyTSConnections" -Value 0`. Enable firewall rule: `Enable-NetFirewallRule -DisplayGroup "Remote Desktop"`. Enable WinRM: `Enable-PSRemoting -Force`. Verify RDP from management workstation. |
| 6 | **Windows Updates:** Run `sconfig` and select Windows Update, or use: `Install-Module PSWindowsUpdate -Force; Get-WindowsUpdate -Install -AcceptAll -AutoReboot`. Verify with `Get-HotFix | Sort-Object InstalledOn -Descending | Select -First 10`. Record the installed updates. |
| 7 | **Install AD DS role:** `Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools`. Verify installation: `Get-WindowsFeature AD-Domain-Services`. Confirm the role shows "Installed". |
| 8 | **Promote to Domain Controller:** Run the AD DS configuration wizard. For a new forest: `Install-ADDSForest -DomainName "pioneer.edu.my" -DomainNetbiosName "PIONEER" -ForestMode "WinThreshold" -DomainMode "WinThreshold" -InstallDns:$true -SafeModeAdministratorPassword (ConvertTo-SecureString "<DSRM_PASSWORD>" -AsPlainText -Force) -Force`. Server will reboot. Log in as PIONEER\Administrator after reboot. |
| 9 | **Verify AD DS and DNS:** Run `dcdiag /v` — all tests must PASS. Run `Get-ADDomainController -Filter *` — verify this server appears. Run `Get-DnsServerZone` — verify `pioneer.edu.my` forward zone exists. Create reverse lookup zone: open DNS Manager → Reverse Lookup Zones → New Zone → Primary zone, AD-integrated → enter network ID. |
| 10 | **Create OU structure:** Using Active Directory Users and Computers (ADUC) or PowerShell, create the OU structure: `New-ADOrganizationalUnit -Name "_Computers" -Path "DC=pioneer,DC=edu,DC=my"`, then sub-OUs for Servers, Workstations, Laptops; `New-ADOrganizationalUnit -Name "_Users" -Path "DC=pioneer,DC=edu,DC=my"`, then sub-OUs for Staff, Students, Service Accounts. |
| 11 | **Install and configure DHCP:** `Install-WindowsFeature -Name DHCP -IncludeManagementTools`. Authorise in AD: `Add-DhcpServerInDC -DnsName "SRV-DC01.pioneer.edu.my" -IPAddress <ServerIP>`. Create scope: `Add-DhcpServerv4Scope -Name "LAN-Scope" -StartRange 10.0.1.100 -EndRange 10.0.1.250 -SubnetMask 255.255.255.0`. Set options: `Set-DhcpServerv4OptionValue -ScopeId 10.0.1.0 -Router 10.0.1.1 -DnsServer <ServerIP> -DnsDomain "pioneer.edu.my"`. Verify from a client machine that a DHCP lease is received. |
| 12 | **Configure DNS forwarders:** In DNS Manager, right-click the server → Properties → Forwarders tab. Add 8.8.8.8 (Google) and 1.1.1.1 (Cloudflare) as forwarders. Test: `Resolve-DnsName google.com`. Verify resolution returns an IP address. |
| 13 | **Final verification:** Record the output of these commands: `dcdiag /test:dns /v`, `repadmin /showrepl`, `Get-DhcpServerv4ScopeStatistics`, `nslookup SRV-DC01.pioneer.edu.my`. All must show success. |
| 14 | **Complete the assessment checklist** and submit the command output log and checklist. |

---

## Hasil Dijangka / Expected Outcome

- Windows Server 2022 installed and activated on the OS-RAID1 logical drive
- Server renamed, IP configured, timezone set, NTP synchronised
- AD DS installed; server promoted to Domain Controller for pioneer.edu.my
- DNS forward and reverse zones configured; DNS forwarders set
- OU structure created per plan
- DHCP scope configured, authorised, and verified leasing to clients
- All dcdiag tests PASSED; repadmin shows no errors

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | OS installed on OS-RAID1 logical drive; complex Administrator password set | [ ] Yes  [ ] No |
| 2 | Static IP, DNS, hostname, and timezone configured; verified with ipconfig /all | [ ] Yes  [ ] No |
| 3 | NTP synchronised; w32tm /query /status shows stratum ≤ 3 | [ ] Yes  [ ] No |
| 4 | RDP and WinRM enabled and tested from management workstation | [ ] Yes  [ ] No |
| 5 | Windows Updates applied; patch list recorded | [ ] Yes  [ ] No |
| 6 | AD DS role installed and DC promoted for domain pioneer.edu.my | [ ] Yes  [ ] No |
| 7 | dcdiag /v — all tests PASSED | [ ] Yes  [ ] No |
| 8 | DNS forward and reverse zones present; forwarders configured | [ ] Yes  [ ] No |
| 9 | OU structure created as per plan | [ ] Yes  [ ] No |
| 10 | DHCP installed, authorised, scope active, and leasing verified | [ ] Yes  [ ] No |
| 11 | All verification command outputs recorded and submitted | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |