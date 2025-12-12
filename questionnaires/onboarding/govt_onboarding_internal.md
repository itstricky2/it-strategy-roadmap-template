# IT Onboarding & Account Transition Questionnaire
## Government & Municipal Clients – vCIO Internal Version

> **Purpose**: This is the forensic, tactical questionnaire for the First 30 Days of an engagement, often involving MSP displacement. The objective is to secure the "Keys to the Kingdom," identify hidden risks (Shadow IT), and establish a liability baseline.
>
> **Usage**: Use during initial discovery calls and onsite assessments. The `⚠️ CRITICAL` blocks highlight show-stopper risks. The `💡 PROBE` sections help uncover what clients may not volunteer. The `📋 ACTION` blocks specify immediate steps.

---

## Pre-Engagement Checklist

- [ ] Engagement letter signed and dated
- [ ] Scope of responsibility clearly documented
- [ ] Liability limitations acknowledged by client
- [ ] Previous MSP termination notice confirmed sent
- [ ] Emergency contact list obtained
- [ ] Initial onsite/virtual discovery scheduled

---

## Section 1: Administrative Access & Control

### 1.1 Credential Inventory

**1. Does the organization possess "Break Glass" credential documentation?**

```
[Response]
```

> ⚠️ **CRITICAL – HOSTAGE RISK**: If no documentation exists and the previous MSP controls all accounts, you are walking into a potential hostage situation. The previous provider may:
> - Delay or refuse credential handover
> - Require payment of disputed invoices
> - Claim ownership of configurations/scripts
>
> 📋 **ACTION**: Before signing engagement, verify client has:
> - [ ] At least ONE Global Admin account they control
> - [ ] DNS registrar login credentials
> - [ ] Physical access to server room/closets

---

**2. Microsoft 365 / Google Workspace Administration:**

| Platform | Global Admin | Controlled By | MFA Status |
|----------|--------------|---------------|------------|
|          |              |               |            |

> ⚠️ **CRITICAL – DELEGATED ADMIN TRAP**: Many MSPs provision Microsoft 365 through their own CSP tenancy and maintain "delegated admin" access. In hostile transitions:
> - The MSP may revoke delegated access (fine) but may have created BACKDOOR admin accounts
> - The "Global Admin" may actually be a delegated partner relationship, not a user account
>
> 📋 **IMMEDIATE ACTION**:
> 1. Log into Azure AD/Entra → Roles and Administrators → Global Administrator
> 2. List ALL Global Administrators – are any from previous MSP domains?
> 3. Check Partner Relationships and revoke previous MSP's delegated admin
> 4. Create a NEW Global Admin account with a client-controlled email
> 5. Require MFA setup using CLIENT-owned device (not previous MSP's Duo/authenticator)
>
> 💡 **PROBE**: "Has anyone from [previous MSP] ever logged into your Microsoft 365 admin center using their own email address?"

---

**3. Cloud Platform Administration:**

| Platform | Admin Account | Controlled By |
|----------|---------------|---------------|
|          |               |               |

> ⚠️ **CRITICAL – AWS/AZURE ROOT ACCOUNTS**: If previous MSP created the cloud tenancy, the ROOT account email might be theirs. Check:
> - AWS: Root user email
> - Azure: First Global Admin / subscription owner
>
> 📋 **ACTION**: If root/owner is previous MSP, this is a major issue requiring formal transfer request.

---

**4. On-Premise Server Administration:**

| Server | Admin Account | Password Known? |
|--------|---------------|-----------------|
|        |               |                 |

> 💡 **PROBE**: "If the previous IT provider disappeared today, could you log into any server with administrative rights?"
>
> ⚠️ **RED FLAG**: If all domain admin passwords are unknown to client, this is Day 1 priority – reset all privileged credentials.
>
> 📋 **ACTION**: Plan for service account password resets – identify all service dependencies first.

---

### 1.2 Domain & DNS Control

**5. Primary domains and registrar access:**

| Domain | Registrar | Access Verified? |
|--------|-----------|------------------|
|        |           |                  |

> ⚠️ **CRITICAL – DNS HOSTAGE**: Domain/DNS is the ultimate control point. Without it:
> - Email can be rerouted
> - Websites can be redirected
> - SSL certificates cannot be renewed
>
> 📋 **IMMEDIATE ACTION**:
> 1. Log into registrar directly (not via previous MSP portal)
> 2. Verify WHOIS shows client as registrant
> 3. Check if 2FA recovery email/phone is client-controlled
> 4. Set domain to "Transfer Lock"
> 5. Update registrant contact to client-controlled email
>
> 💡 **PROBE**: "When was the last time you personally logged into GoDaddy/Network Solutions? Do you know the password?"

---

### 1.3 Network & Security Equipment

**8. Firewall/Router ownership:**

| Device | Make/Model | Owned/Leased | Admin Access? |
|--------|------------|--------------|---------------|
|        |            |              |               |

> ⚠️ **CRITICAL – HARDWARE AS A SERVICE (HAAS)**: Many MSPs deploy firewalls/servers under HaaS agreements. In hostile transitions:
> - MSP may demand equipment return
> - MSP may remotely factory-reset their equipment
> - MSP may have perpetual VPN access configured
>
> 📋 **IMMEDIATE ACTIONS**:
> 1. Determine ownership of all network equipment
> 2. For leased equipment: Review contract terms, buyout options
> 3. For MSP-owned: Plan emergency replacement if hostile
> 4. Check for any VPN tunnels to previous MSP – DISABLE IMMEDIATELY
> 5. Change ALL network device admin passwords
>
> 💡 **PROBE**: "Is there a monthly cost for this firewall, or did you buy it outright?"

---

**10. Leased equipment details:**

| Equipment | Provider | Monthly Cost | Buyout |
|-----------|----------|--------------|--------|
|           |          |              |        |

> 💡 **CONTEXT**: If equipment must be returned, have replacement procurement ready. A municipality without a firewall = offline.

---

## Section 2: Software & Licensing

**11. Microsoft 365 licensing ownership:**

| Tenant | License Type | Owner (Direct/CSP) |
|--------|--------------|-------------------|
|        |              |                   |

> ⚠️ **CRITICAL – CSP LICENSE REVOCATION**: If licenses are through previous MSP's CSP, they can:
> - Revoke licenses immediately (users lose access)
> - Reduce license counts
> - Close the tenant entirely (rare but possible)
>
> 📋 **ACTION**: If CSP-based:
> 1. Identify a new CSP partner (us or Microsoft direct)
> 2. Initiate CSP transfer BEFORE terminating relationship
> 3. Document all current licenses and assign counts
>
> **GOVERNMENT SPECIFIC**: If CJIS/GCC licensing, transfer is more complex. Allow 30-45 days.

---

**12. Security tool ownership:**

| Tool | Product | Owned By |
|------|---------|----------|
| EDR  |         |          |
| Backup |       |          |
| Monitoring |  |          |

> ⚠️ **RED FLAG – MONITORING BLIND SPOT**: When previous MSP's RMM is removed, you lose visibility. Plan:
> - [ ] Deploy our RMM immediately upon engagement
> - [ ] Overlap monitoring for at least 2 weeks
> - [ ] Never leave a gap in monitoring coverage

---

## Section 3: Previous IT Provider Relationship

**13. Previous provider relationship status:**

| Provider | Contact | Status |
|----------|---------|--------|
|          |         |        |

> 💡 **TRIAGE – HOSTILE VS COOPERATIVE**:
>
> **COOPERATIVE** (Best case):
> - Will schedule handover meeting
> - Will provide documentation
> - Will answer questions during transition
>
> **UNRESPONSIVE** (Common):
> - No response to emails/calls
> - Delays everything
> - Minimum legal compliance only
>
> **HOSTILE** (Worst case):
> - Disputes invoices as leverage
> - Claims ownership of configurations
> - May have left backdoors or dead-man switches
>
> 📋 **ACTION FOR HOSTILE**:
> 1. Document everything in writing
> 2. Assume NO cooperation – plan to rebuild from scratch
> 3. Immediately audit for backdoor accounts
> 4. Block previous MSP IP ranges at firewall
> 5. Rotate ALL passwords within 48 hours
>
> 💡 **PROBE**: "Why did you decide to leave [previous provider]? Did they give you any pushback when you notified them?"

---

**15. Outstanding disputes:**

```
[Response]
```

> ⚠️ **CRITICAL – RANSOM RISK**: Previous MSPs sometimes withhold credentials until disputed invoices are paid. Document:
> - Any claimed outstanding amounts
> - Client's position on validity
> - Whether equipment/data is being held hostage
>
> **LEGAL NOTE**: In most jurisdictions, MSPs must provide credential handover regardless of payment disputes. But proving this takes time you don't have.

---

## Section 4: Documentation Inventory

**16. Documentation availability:**

| Document | Available | Location | Current? |
|----------|-----------|----------|----------|
| Network diagram |  |  |  |
| IP scheme |  |  |  |
| Passwords |  |  |  |
| DR plan |  |  |  |
| Backup procedures |  |  |  |

> 💡 **REALITY**: Most MSP transitions have ZERO documentation handed over. Plan accordingly.
>
> 📋 **ACTION – DOCUMENTATION GENERATION**:
> Week 1: Network discovery scan (create our own diagram)
> Week 2: Asset inventory audit
> Week 3: Password vault population
> Week 4: Runbook creation for critical systems
>
> **CHARGE FOR THIS**: Documentation recreation is billable project work, not included in standard managed services.

---

## Section 5: Current Security Posture

**17. Security tools deployed:**

| Tool Type | Product | Managed By | Coverage |
|-----------|---------|------------|----------|
|           |         |            |          |

> ⚠️ **CRITICAL – LIABILITY BASELINE**: Document current security state IN WRITING before assuming responsibility.
>
> 📋 **ACTION – BASELINE ASSESSMENT**:
> 1. Run vulnerability scan (with client permission)
> 2. Document findings with timestamps
> 3. Get client signature acknowledging current state
> 4. Identify any issues that predate our engagement
>
> **LIABILITY PROTECTION**: If a breach occurs in month 2, documentation proves what we inherited vs. what we introduced.

---

**19. Known security issues:**

```
[Response]
```

> ⚠️ **RED FLAG – SWEPT UNDER RUG**: Previous incidents may be hidden. Look for:
> - Unexplained password resets in Azure AD logs
> - Unusual firewall rules
> - Disabled logging
> - "Temporary" exceptions that are years old
>
> 💡 **PROBE**: "Has there ever been any incident where you suspected someone accessed something they shouldn't have? Even if it turned out to be nothing?"

---

**20. Terminated employee access removal:**

```
[Response]
```

> ⚠️ **CRITICAL – ORPHANED ACCOUNTS**: Government entities notoriously fail at timely termination.
>
> 📋 **IMMEDIATE ACTION**:
> 1. Get list of all terminations in past 12 months from HR
> 2. Cross-reference against Active Directory
> 3. Cross-reference against M365/Google
> 4. Cross-reference against VPN/remote access
> 5. Disable any accounts still active
>
> **DOCUMENT FINDINGS**: Report to client with recommendations.

---

## Section 6: Backup & Recovery

**21. Current backup status:**

| Question | Response |
|----------|----------|
| Product |  |
| Last Success |  |
| Last Test |  |
| Offsite? |  |
| Immutable? |  |

> ⚠️ **CRITICAL – ASSUME BACKUPS ARE BROKEN**: Until personally verified, assume:
> - Backups exist in name only
> - Restore has never been tested
> - Ransomware could encrypt backup too
>
> 📋 **WEEK 1 ACTION**:
> 1. Verify last successful backup with our eyes (not just reports)
> 2. Perform test restore of at least ONE file
> 3. Verify offsite copy is truly offsite (not just different folder)
> 4. Check for immutability (ransomware protection)
>
> 💡 **PROBE**: "When was the last time you actually recovered a file from backup? Did it work?"

---

## Section 7: Critical Systems & Vendors

**23. Critical system dependencies:**

| System | Vendor | Support Contact |
|--------|--------|-----------------|
|        |        |                 |

> 📋 **ACTION**: Obtain vendor portal logins and verify support contracts are active.
>
> **WATCH FOR**:
> - Expired maintenance agreements
> - Support contracts held by previous MSP
> - Vendors requiring MSP authorization for support

---

## Section 8: Compliance Requirements

**25-27. Compliance and Insurance status:**

> 💡 **CONTEXT – MUNICIPAL COMPLIANCE**:
> - **CJIS**: If Police Department, almost certainly applicable. Check for pending audit.
> - **HIPAA**: Fire/EMS, HR benefits. BAAs must be in place.
> - **Insurance**: Increasingly driving security requirements.
>
> 📋 **ACTION**:
> 1. Request copy of cyber insurance application
> 2. Verify attested controls are actually in place
> 3. Note policy renewal date – security roadmap should align
> 4. Identify any compliance audit deadlines

---

## Section 9: Shadow IT Detection

> ⚠️ **THIS SECTION TO BE COMPLETED BY vCIO THROUGH INVESTIGATION**
> (Not client-facing – fill out during discovery)

### 9.1 Unsanctioned Cloud Services

**Method**: Review expense reports, email headers, DNS queries

| Service Found | Category | Users | Risk Level | Action |
|---------------|----------|-------|------------|--------|
|               |          |       |            |        |

**Common Shadow IT in Government**:
- Personal Dropbox/Google Drive
- Unapproved project management (Trello, Asana)
- WhatsApp/Signal for business communication
- ChatGPT/AI tools with CJI data exposure
- Personal email for official business

### 9.2 Rogue Infrastructure

| Finding | Location | Owner | Risk | Action |
|---------|----------|-------|------|--------|
| Personal router |  |  |  |  |
| Unauthorized AP |  |  |  |  |
| Consumer NAS |  |  |  |  |

### 9.3 Personal Account Usage

| Platform | User | Business Data? | Migration Needed? |
|----------|------|----------------|-------------------|
|          |      |                |                   |

---

## 30-60-90 Day Stabilization Framework

### Day 30 Objectives
- [ ] All administrative credentials secured
- [ ] Previous MSP access revoked
- [ ] Our monitoring deployed on all systems
- [ ] Backup verified functional
- [ ] Critical security gaps identified
- [ ] Liability baseline documented and signed

### Day 60 Objectives
- [ ] Security gaps remediation in progress
- [ ] Documentation created for critical systems
- [ ] Vendor relationships transferred
- [ ] Staff introductions complete
- [ ] Regular reporting cadence established

### Day 90 Objectives
- [ ] Stabilization complete
- [ ] Strategic roadmap presented
- [ ] Quick wins delivered
- [ ] Client satisfaction validated
- [ ] Transition to steady-state management

---

## Risk Register (Complete During Discovery)

| Risk | Discovery Date | Severity | Client Notified | Remediation Plan |
|------|----------------|----------|-----------------|------------------|
|      |                |          |                 |                  |

---
*Document Version: 1.0 | Internal Use Only | Last Updated: December 2024*
