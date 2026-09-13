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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C02 COMPUTER SYSTEM SECURITY CONTROL |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. IDENTIFY SECURITY REQUIREMENTS<br>2. IMPLEMENT ACCESS CONTROL AND AUTHENTICATION<br>3. CONFIGURE FIREWALL AND NETWORK SECURITY<br>4. MANAGE PATCHES AND SECURITY UPDATES<br>5. DOCUMENT SECURITY CONFIGURATION AND INCIDENTS |
| NO. KOD | IT-020-4:2013-C02/KK(3/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-03-configure-firewall-network-security

**TUJUAN:** Kertas rujukan untuk KK-03-configure-firewall-network-security.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

Configure Windows Defender Firewall with Advanced Security rules on a Windows Server, disable unnecessary services and protocols, and verify the resulting network security posture using port scanning and service enumeration tools.

---

## Tempoh / Duration

4 hours

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Windows Server 2022 (VM — isolated lab network) | 1 |
| 2 | Windows 11 workstation (same isolated lab network) | 1 |
| 3 | Kali Linux VM or equivalent (for port scanning — same isolated lab network) | 1 |
| 4 | Administrator credentials for the Windows Server | Provided by instructor |
| 5 | Firewall rule register template (blank) | 1 |
| 6 | Services review checklist (provided by instructor) | 1 |

---

## Langkah Keselamatan / Safety Precautions

- All activities must be conducted on the **isolated lab network only** — never scan or modify firewall rules on production systems
- Obtain instructor sign-off before conducting any port scan
- Do not disable critical services (Active Directory, DNS, DHCP) on a domain controller — work on a standalone member server for this exercise
- Document the pre-change state before disabling any service or applying any firewall rule

---

## Prosedur / Procedures

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 1 | **Baseline scan (pre-hardening).** From the Kali Linux VM, run `nmap -sV <server-IP>` against the Windows Server. Record all open ports, services detected, and version information in the firewall rule register template. This is the pre-hardening baseline. |
| 2 | **Review running services.** On the Windows Server, open `services.msc`. Identify all running services. Cross-reference with the services review checklist provided. Mark each service as: Required / Not Required / Uncertain. For uncertain services, research the service name before making a decision. |
| 3 | **Disable unnecessary services.** For each service marked "Not Required", stop the service and set its startup type to Disabled. Use PowerShell: `Set-Service -Name "<ServiceName>" -StartupType Disabled; Stop-Service -Name "<ServiceName>"`. Record each action. |
| 4 | **Open Windows Defender Firewall with Advanced Security** (`wf.msc`). Review the current inbound and outbound rules. Note any rules that use "Allow All" or have no source IP restriction. |
| 5 | **Configure inbound rules — create the following rules:** (a) Allow RDP (TCP 3389) from the admin workstation IP only — delete or disable the existing unrestricted RDP rule if present. (b) Allow HTTPS (TCP 443) from Any. (c) Allow DNS (TCP/UDP 53) from internal subnet only. (d) Block Telnet (TCP 23) from Any — create explicit block rule even if service is not running. (e) Block SMB (TCP 445) from external — allow only from internal subnet. |
| 6 | **Configure outbound rules:** Create a rule to block outbound traffic on port 23 (Telnet). Verify that Windows Update traffic (TCP 443 to Microsoft IPs) is permitted. |
| 7 | **Export the firewall policy** using: `netsh advfirewall export "C:\Temp\firewall-policy-after.wfw"`. This creates a backup of the configured rules. |
| 8 | **Post-hardening scan.** Repeat the Nmap scan from Kali Linux: `nmap -sV <server-IP>`. Compare the open ports and services with the pre-hardening baseline. Record which ports were closed and which remain open. |
| 9 | **Verify RDP restriction.** From the Kali Linux VM (not the admin workstation), attempt an RDP connection to the server. It should be blocked. From the Windows 11 admin workstation, RDP should succeed. Document the results. |
| 10 | **Complete the firewall rule register.** For every inbound and outbound rule configured, record: rule name, direction, protocol, port, source/destination, action, profile, and justification. Sign and submit to instructor. |

---

## Hasil Jangkaan / Expected Outcome

- Pre-hardening Nmap scan results documented
- Unnecessary services disabled with services.msc and PowerShell — recorded in service checklist
- Five inbound and two outbound firewall rules correctly configured in WDFAS
- Firewall policy exported as backup file
- Post-hardening Nmap scan shows reduced attack surface (fewer open ports)
- RDP access correctly restricted to admin workstation only
- Firewall rule register completed with justification for all rules

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Pre-hardening Nmap scan documented | [ ] Yes  [ ] No |
| 2 | Unnecessary services identified and disabled | [ ] Yes  [ ] No |
| 3 | RDP rule restricted to admin workstation IP | [ ] Yes  [ ] No |
| 4 | Block rules for Telnet and external SMB created | [ ] Yes  [ ] No |
| 5 | Firewall policy exported as backup | [ ] Yes  [ ] No |
| 6 | Post-hardening Nmap scan shows reduced open ports | [ ] Yes  [ ] No |
| 7 | RDP blocked from non-admin IP verified | [ ] Yes  [ ] No |
| 8 | Firewall rule register complete with justifications | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |