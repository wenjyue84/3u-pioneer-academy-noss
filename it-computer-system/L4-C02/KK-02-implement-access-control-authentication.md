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
| NO. KOD | IT-020-4:2013-C02/KK(2/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-02-implement-access-control-authentication

**TUJUAN:** Kertas rujukan untuk KK-02-implement-access-control-authentication.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

Configure user accounts, security groups, RBAC permissions, password policy, and account lockout policy on a Windows Server domain environment in accordance with the principle of least privilege.

---

## Tempoh / Duration

4 hours

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Windows Server 2022 (physical or VM, domain controller role installed) | 1 |
| 2 | Windows 11 workstation joined to the domain | 1 |
| 3 | Role-based access requirements sheet (provided by instructor) | 1 |
| 4 | Group Policy Management Console (GPMC) | Pre-installed |
| 5 | Active Directory Users and Computers (ADUC) | Pre-installed |
| 6 | Administrator credentials for domain | Provided by instructor |

---

## Langkah Keselamatan / Safety Precautions

- Do not delete any pre-existing production accounts — work only in the designated training Organisational Unit (OU)
- Record all changes made before and after each configuration step
- Log off the server console when not actively working
- Do not share administrator credentials with other trainees

---

## Prosedur / Procedures

**Scenario:** The IT manager of Syarikat Maju Jaya has provided the following role requirements. Configure Active Directory to implement RBAC for these roles using the principle of least privilege.

| Role | Required Access |
|------|----------------|
| Finance User | Read/write to `\\server\Finance` shared folder; no access to HR or IT folders |
| HR Manager | Read/write to `\\server\HR`; read-only to `\\server\Finance` reports subfolder |
| IT Administrator | Full access to all shared folders; local administrator on all workstations |
| Guest / Visitor | Read-only access to `\\server\Public` only |

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 1 | Open Active Directory Users and Computers (ADUC). In the Training OU provided, create the following Organisational Units: `Training\Users`, `Training\Groups`, `Training\Computers`. |
| 2 | Create four user accounts in `Training\Users`: `fin.user1` (Finance User), `hr.manager1` (HR Manager), `it.admin1` (IT Administrator), `guest.visitor1` (Guest). Set initial password `P@ssword123!` and require password change at next login. |
| 3 | Create four security groups in `Training\Groups`: `GRP-Finance-RW`, `GRP-HR-RW`, `GRP-Finance-RO`, `GRP-IT-Admin`, `GRP-Guest-Public`. Add each user to the appropriate group(s) according to the role requirements table. |
| 4 | On the file server, create the shared folder structure: `Finance`, `HR`, `IT`, `Public`. Set NTFS permissions on each folder so that only the corresponding security group has the required access. Remove all other permissions including `Everyone`. |
| 5 | Open Group Policy Management Console (GPMC). Create a new GPO named `Training-Password-Policy` and link it to the `Training` OU. Configure: minimum password length = 12, complexity enabled, max age = 90 days, history = 10. |
| 6 | In the same GPO, configure account lockout: threshold = 5 attempts, duration = 30 minutes, reset counter = 15 minutes. |
| 7 | Create a second GPO named `Training-Logon-Restrictions`. Configure the `Deny log on locally` setting for the `guest.visitor1` account (service/guest accounts should not have interactive logon). |
| 8 | On the Windows 11 workstation, log in as `fin.user1`. Verify: can access `\\server\Finance` (read/write); cannot access `\\server\HR` or `\\server\IT`. Document the test result with screenshots or written observation. |
| 9 | Test account lockout: attempt to log in as `fin.user1` with a wrong password 5 times. Verify the account is locked. Unlock the account from ADUC and document the procedure. |
| 10 | Record all configurations made (OU structure, accounts, groups, GPO settings, folder permissions) in the configuration record form provided by the instructor. |

---

## Hasil Jangkaan / Expected Outcome

- Four user accounts created in correct OU with required password settings
- Five security groups created with correct group memberships
- NTFS folder permissions correctly restricting each role to its authorised resources
- Password policy GPO applied and verifiable via `gpresult /r` on a workstation
- Account lockout confirmed to trigger at 5 failed attempts
- Configuration record completed and signed

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | OU structure created correctly in ADUC | [ ] Yes  [ ] No |
| 2 | All user accounts created with correct settings | [ ] Yes  [ ] No |
| 3 | Security groups created and users assigned correctly | [ ] Yes  [ ] No |
| 4 | NTFS folder permissions configured per role requirements | [ ] Yes  [ ] No |
| 5 | Password policy GPO configured and linked | [ ] Yes  [ ] No |
| 6 | Account lockout policy configured correctly | [ ] Yes  [ ] No |
| 7 | Access control verified by logging in as test users | [ ] Yes  [ ] No |
| 8 | Account lockout triggered and unlock procedure demonstrated | [ ] Yes  [ ] No |
| 9 | Configuration record completed and accurate | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |