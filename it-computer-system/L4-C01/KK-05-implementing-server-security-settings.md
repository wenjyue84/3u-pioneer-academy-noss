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
| NO. KOD | IT-020-4:2013-C01/KK(5/6) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-05-implementing-server-security-settings

**TUJUAN:** Kertas rujukan untuk KK-05-implementing-server-security-settings.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

Apply a structured set of security controls to a configured Windows Server: configure Windows Firewall, implement a password and account lockout policy via GPO, enable and verify audit logging, and enable BitLocker encryption on the data volume.

---

## Tempoh / Duration

6 hours (practical session)

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Configured Windows Server (from KK-04) — domain controller or member server | 1 |
| 2 | Management workstation with RSAT and Group Policy Management Console (GPMC) | 1 |
| 3 | Microsoft Security Baseline GPO backup (downloaded from Microsoft Security Compliance Toolkit) | 1 |
| 4 | Security configuration worksheet | 1 |
| 5 | CIS Benchmark for Windows Server 2022 (reference PDF) | 1 |
| 6 | PowerShell reference card | 1 |

---

## Langkah Keselamatan / Safety Precautions

- Apply security settings in the correct order — firewall rules before account lockout; test RDP connectivity after each firewall change to avoid locking yourself out
- Before enabling BitLocker, verify the BitLocker recovery key backup location is accessible and functional — loss of the recovery key without a backup means permanent data loss
- Do not apply security baselines to production systems during business hours — schedule for maintenance window
- Record every GPO change; GPO misconfigurations can lock all users out of the domain

---

## Prosedur / Procedures

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 1 | **Baseline firewall review:** On the server, open Windows Firewall with Advanced Security (`wf.msc`). Document the current state: which profiles are active, current default inbound and outbound policies. Run `Get-NetFirewallProfile` in PowerShell and record the output. |
| 2 | **Set default-deny inbound:** Run: `Set-NetFirewallProfile -Profile Domain,Private,Public -DefaultInboundAction Block -DefaultOutboundAction Allow`. Verify: `Get-NetFirewallProfile | Select Name, DefaultInboundAction`. Confirm all three profiles show Block. |
| 3 | **Create role-specific inbound rules:** Using the port table from KP-05 Section 3.3, create inbound allow rules for the server's active roles. For a Domain Controller, minimum rules required: LDAP (TCP 389), Kerberos (TCP/UDP 88), DNS (TCP/UDP 53), SMB (TCP 445), RPC Endpoint Mapper (TCP 135), Dynamic RPC (TCP 49152–65535). For RDP: restrict source to management VLAN only. Use the commands from KP-05 Section 3.3 as reference. After each rule, verify from the management workstation that the corresponding service is still reachable. |
| 4 | **Create a Domain Security GPO:** In Group Policy Management Console (GPMC), create a new GPO named "SEC-Domain-Security-Baseline". Link it to the domain root. Ensure it is applied before (higher precedence than) the Default Domain Policy. |
| 5 | **Configure password and lockout policy:** In the GPO, navigate to Computer Configuration > Windows Settings > Security Settings > Account Policies. Set: Minimum password length = 14, Complexity = Enabled, Max password age = 90 days, Password history = 24. Under Account Lockout Policy: Threshold = 5 attempts, Duration = 30 minutes, Observation window = 30 minutes. Run `gpupdate /force` on the server. Verify with `net accounts`. |
| 6 | **Configure advanced audit policy (via GPO):** In the same GPO, navigate to Computer Configuration > Windows Settings > Security Settings > Advanced Audit Policy Configuration. Enable the categories from KP-05 Section 5.2: Account Logon (Success, Failure), Logon/Logoff (Success, Failure), Account Management (Success, Failure), Policy Change (Success, Failure), Privilege Use (Success, Failure). Run `gpupdate /force`. Verify audit policy with `auditpol /get /category:*` — confirm the required subcategories are enabled. |
| 7 | **Configure Security Event Log size:** Run: `Limit-EventLog -LogName Security -MaximumSize 524288KB -OverflowAction OverwriteOlder`. Verify: `Get-EventLog -LogName Security -Newest 1 | Select MaximumKilobytes`. Generate a test event: lock and unlock the server. In Event Viewer, verify the logon events (Event ID 4624 = successful logon, 4634 = logoff) are recorded. |
| 8 | **Rename and disable built-in Administrator account:** Via GPO (Computer Config > Windows Settings > Security Settings > Local Policies > Security Options): set "Accounts: Rename administrator account" to a custom name (e.g. "sysadmin-pioneer"). Set "Accounts: Guest account status" = Disabled. Verify via `net user` command on the server. |
| 9 | **Configure NTLMv2-only authentication:** In the GPO, navigate to Computer Config > Windows Settings > Security Settings > Local Policies > Security Options. Set "Network security: LAN Manager authentication level" = "Send NTLMv2 response only; refuse LM and NTLM". Run `gpupdate /force`. Verify from the management workstation that domain logon still functions correctly. |
| 10 | **Enable BitLocker on the data volume:** Verify TPM is ready: run `tpm.msc` and confirm TPM is enabled and activated. Enable BitLocker on the D: (DATA) volume: `Enable-BitLocker -MountPoint "D:" -EncryptionMethod XtsAes256 -RecoveryKeyProtector`. Note the recovery key ID displayed. Back up the recovery key: `Backup-BitLockerKeyProtector -MountPoint "D:" -KeyProtectorId <ID>`. To back up to AD: `Backup-BitLockerKeyProtector` requires the `msTPM-OwnerInformation` AD attribute — verify with your instructor if AD schema has been extended. Alternatively, save the recovery key to a network share on the management server. |
| 11 | **Verify BitLocker encryption:** Run `Get-BitLockerVolume -MountPoint "D:"`. Confirm: EncryptionMethod = XtsAes256, ProtectionStatus = On, EncryptionPercentage progressing. Record the KeyProtector ID and the location where the recovery key is stored. |
| 12 | **Security verification summary:** Run the following and record all outputs: `auditpol /get /category:*`, `Get-NetFirewallProfile`, `net accounts`, `Get-BitLockerVolume`. Verify that a test logon failure generates Event ID 4625 in the Security event log. |
| 13 | **Complete the assessment checklist** and submit all recorded command outputs and the security configuration worksheet. |

---

## Hasil Dijangka / Expected Outcome

- Windows Firewall set to default-deny inbound on all profiles; role-specific rules verified
- Password policy: 14-char minimum, complexity, 90-day max age, 24-history enforced
- Account lockout: 5 attempts, 30-minute duration configured and verified
- Advanced audit policy enabled for all required categories; Event IDs 4624/4625 visible in Security log
- Security Event Log set to 512 MB
- Built-in Administrator account renamed; Guest disabled
- NTLMv2-only authentication enforced
- BitLocker encryption enabled and in progress on D: volume; recovery key backed up

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Default-deny inbound configured on all three firewall profiles | [ ] Yes  [ ] No |
| 2 | Role-specific firewall rules created; service still reachable from management workstation | [ ] Yes  [ ] No |
| 3 | Password and lockout policy GPO applied; verified with `net accounts` | [ ] Yes  [ ] No |
| 4 | Advanced audit policy enabled for all required categories | [ ] Yes  [ ] No |
| 5 | Test logon failure generates Event ID 4625 in Security log | [ ] Yes  [ ] No |
| 6 | Security event log size set to 512 MB | [ ] Yes  [ ] No |
| 7 | Built-in Administrator renamed; Guest disabled | [ ] Yes  [ ] No |
| 8 | NTLMv2-only authentication enforced via GPO | [ ] Yes  [ ] No |
| 9 | BitLocker enabled on D: volume; encryption in progress | [ ] Yes  [ ] No |
| 10 | BitLocker recovery key backed up and location documented | [ ] Yes  [ ] No |
| 11 | All command outputs recorded and submitted | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |