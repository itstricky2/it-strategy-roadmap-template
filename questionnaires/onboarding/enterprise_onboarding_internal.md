# IT Onboarding & Account Transition Questionnaire
## Medium Enterprise Clients – vCIO Internal Version

> **Purpose**: This is the forensic, tactical questionnaire for the First 30 Days of an enterprise engagement, often involving MSP displacement. The objective is to secure control, identify hidden risks, establish a liability baseline, and demonstrate value quickly.
>
> **Usage**: Use during initial discovery and onsite assessments. The `⚠️ CRITICAL` blocks highlight show-stopper risks. The `💡 PROBE` sections help uncover what clients may not volunteer. The `📋 ACTION` blocks specify immediate steps.

---

## Pre-Engagement Checklist

- [ ] Master Services Agreement executed
- [ ] Scope of services clearly defined
- [ ] Liability limitations documented
- [ ] Insurance certificates exchanged
- [ ] Current provider termination confirmed
- [ ] Emergency contact list obtained
- [ ] Discovery session scheduled

---

## Section 1: Administrative Access & Control

### 1.1 Credential Inventory

**1. Does the organization have credential documentation?**

```
[Response]
```

> ⚠️ **CRITICAL – CONTROL ASSESSMENT**: Enterprises often have no idea what they own vs. what their MSP controls. Day 1 objective: verify the client can survive without the previous provider.
>
> 📋 **ACTION**: Before going live, verify client possesses:
> - [ ] At least ONE cloud admin account they control directly
> - [ ] Domain registrar access
> - [ ] Physical server room/data center access
> - [ ] Network device credentials

---

**2. Microsoft 365 / Google Workspace:**

| Platform | Admin Account | Controlled By | MFA Status |
|----------|---------------|---------------|------------|
|          |               |               |            |

> ⚠️ **CRITICAL – CSP TRAP**: Enterprise M365 is often purchased through the MSP's Cloud Solution Provider (CSP) agreement. This means:
> - MSP can view usage, potentially content
> - MSP can reduce/revoke licenses
> - MSP may own the tenant administratively
>
> 📋 **IMMEDIATE ACTIONS**:
> 1. Azure AD → Roles → Global Administrator – list ALL
> 2. Partner Relationships – identify and review
> 3. Create client-controlled break-glass Global Admin
> 4. Plan CSP transfer if needed (2-4 week process)
>
> 💡 **PROBE**: "Who set up your Microsoft 365 originally? Was it done under [previous MSP]'s account?"

---

**3. Cloud Platform Access (Azure/AWS/GCP):**

| Platform | Root/Owner Account | Controlled By |
|----------|-------------------|---------------|
|          |                   |               |

> ⚠️ **CRITICAL – ROOT ACCOUNT OWNERSHIP**:
> - **AWS**: If the root email is @previousmsp.com, they control everything
> - **Azure**: Check subscription ownership and directory roles
> - **GCP**: Organization admin vs. billing account owner
>
> 📋 **ACTION**: If root/owner is MSP:
> 1. Document all resources running
> 2. Plan migration to client-owned tenancy
> 3. This is a significant project – scope and price separately

---

**4. On-Premise Infrastructure:**

| System | Admin Account | Password Known? |
|--------|---------------|-----------------|
|        |               |                 |

> 💡 **PROBE**: "If I asked you to log into the main server right now with Domain Admin credentials, could you do it without calling anyone?"
>
> ⚠️ **RED FLAG**: If all passwords are "with [previous MSP]," prepare for credential recovery project.
>
> 📋 **ACTION**: Identify all service accounts before resetting passwords – many apps break when domain passwords change.

---

### 1.2 Domain & DNS Control

**5-6. Domain and DNS ownership:**

| Domain | Registrar | Access Verified? |
|--------|-----------|------------------|
|        |           |                  |

> ⚠️ **CRITICAL – BUSINESS CONTINUITY CHOKEPOINT**: DNS is the single most critical control point. Without it:
> - Email stops working (MX records)
> - Website goes down
> - SaaS app integrations break
> - SSL certificates can't renew
>
> 📋 **WEEK 1 ACTIONS**:
> 1. Log into registrar directly (not via MSP portal)
> 2. Verify client is listed as registrant in WHOIS
> 3. Update contact email to client-controlled address
> 4. Enable registrar lock
> 5. Document all DNS records (export zone file)
>
> 💡 **PROBE**: "Have you personally ever logged into your domain registrar? Do you know what registrar you use?"

---

### 1.3 Network & Security Equipment

**7. Network equipment ownership:**

| Device | Make/Model | Owned/Leased | Admin Access? |
|--------|------------|--------------|---------------|
|        |            |              |               |

> ⚠️ **RED FLAG – MSP-OWNED INFRASTRUCTURE**: Many MSPs deploy their firewall/equipment as Hardware-as-a-Service. Risk:
> - Equipment may be removed on termination
> - Remote management access may persist
> - Configurations may be wiped remotely
>
> 📋 **IMMEDIATE ACTIONS**:
> 1. Determine ownership of every network device
> 2. For owned: Change all admin passwords immediately
> 3. For leased: Review contract, understand terms
> 4. Check for any VPN tunnels to previous MSP – **DISABLE**
> 5. Audit firewall rules for any previous MSP IP addresses
>
> 💡 **PROBE**: "Is there a monthly rental charge for any of your network equipment?"

---

## Section 2: Software & Licensing

**9. Microsoft 365 licensing ownership:**

| Question | Response |
|----------|----------|
| Direct/CSP |  |
| CSP Partner |  |

> 💡 **CONTEXT – LICENSE TRANSITION**:
>
> | Scenario | Action Required |
> |----------|-----------------|
> | Direct with Microsoft | Simple – just add our admin access |
> | Our CSP | Perfect – we manage billing |
> | Previous MSP CSP | Need CSP transfer (2-4 weeks) |
> | Unknown | Investigate immediately |
>
> **WARNING**: CSP transfer requires coordination with BOTH outgoing and incoming partners. Budget 30 days.

---

**10. Business software subscriptions:**

| Software | Purpose | Owner | Access? |
|----------|---------|-------|---------|
|          |         |       |         |

> 📋 **ACTION – VENDOR PORTAL INVENTORY**:
> Create master list of all vendor portals:
> - Login credentials
> - Account owner email
> - Support entitlement status
> - Contract expiration
>
> **COMMON DISCOVERY**: Half of support contracts are expired or registered to departed employees.

---

## Section 3: Current IT Provider Relationship

**13. Relationship status:**

```
[Response]
```

> 💡 **TRIAGE – TRANSITION TYPES**:
>
> | Type | Approach | Timeline |
> |------|----------|----------|
> | Cooperative | Joint handover meeting, documentation transfer | 2-4 weeks |
> | Neutral | Written requests only, minimal help | 4-6 weeks |
> | Hostile | Assume zero cooperation, rebuild from scratch | 6-8 weeks |
>
> **HOSTILE INDICATORS**:
> - Disputes outstanding invoices
> - Won't respond to emails
> - "Policies" prevent information sharing
> - Threatens to remove equipment
>
> 📋 **ACTION FOR HOSTILE**:
> 1. Get everything in writing
> 2. CC client on all communications
> 3. Assume backdoors exist – audit immediately
> 4. Block their IP ranges at firewall
> 5. Prepare emergency replacement for any MSP-owned equipment

---

**14. Outstanding disputes:**

```
[Response]
```

> ⚠️ **CRITICAL – RANSOM SCENARIOS**:
> - MSP withholds passwords until invoices paid
> - MSP claims ownership of custom scripts/configurations
> - MSP refuses to provide documentation
>
> **RESPONSE**: In most jurisdictions, credential handover is required regardless of disputes. Document everything. Involve client's legal counsel if needed.
>
> 💡 **PROBE**: "Is there any possibility [previous MSP] might withhold access to anything?"

---

## Section 4: Documentation Inventory

**15. Documentation availability:**

| Document | Available? | Location |
|----------|------------|----------|
|          |            |          |

> 💡 **REALITY CHECK**: Most transitions have minimal documentation. Plan to create everything from scratch.
>
> 📋 **DOCUMENTATION PROJECT** (billable):
> - Week 1: Network discovery, asset inventory
> - Week 2: Credential vault population
> - Week 3: Critical system runbooks
> - Week 4: DR procedures
>
> **Set expectation**: Documentation creation is project work, not included in standard MSA.

---

## Section 5: Current Security Posture

**16-18. Security inventory and incidents:**

| Tool | Product | Managed By |
|------|---------|------------|
|      |         |            |

> ⚠️ **CRITICAL – LIABILITY BASELINE**: Document current security state BEFORE assuming responsibility.
>
> 📋 **BASELINE ASSESSMENT**:
> 1. Run vulnerability scan (with written permission)
> 2. Document all findings with timestamps
> 3. Get client acknowledgment of current state
> 4. Create "Inherited Risk Register"
>
> **LIABILITY PROTECTION**: If breach occurs in month 2, documentation proves pre-existing conditions.
>
> 💡 **PROBE**: "Have there been any unusual events – suspicious emails, unauthorized access, ransomware scares – even if they turned out to be nothing?"

---

**19. Offboarding process:**

```
[Response]
```

> ⚠️ **RED FLAG – ORPHANED ACCOUNTS**: Enterprises notoriously fail at timely termination.
>
> 📋 **IMMEDIATE AUDIT**:
> 1. Get termination list from HR (last 12 months)
> 2. Compare against Active Directory enabled users
> 3. Compare against M365/SaaS accounts
> 4. Compare against VPN/remote access
> 5. Disable any orphaned accounts
> 6. Report findings to client (this is a deliverable)
>
> **COMMON FINDING**: 20-30% of terminated employees still have some form of access.

---

## Section 6: Backup & Recovery

**20. Backup status:**

| Question | Response |
|----------|----------|
| Product |  |
| Last Success |  |
| Last Test |  |

> ⚠️ **CRITICAL – ASSUME BROKEN UNTIL VERIFIED**:
> - Backup jobs may be failing silently
> - Retention may be shorter than claimed
> - Ransomware could encrypt backup
> - Restore has likely never been tested
>
> 📋 **WEEK 1 VERIFICATION**:
> 1. Log into backup solution directly
> 2. Verify last successful job with own eyes
> 3. Perform test restore of sample data
> 4. Check for offsite/immutable copies
> 5. Document findings
>
> 💡 **PROBE**: "When was the last time you actually needed to restore something from backup? Did it work?"

---

## Section 7: Critical Business Systems

**22. Critical systems:**

| System | Vendor | Support Status |
|--------|--------|----------------|
|        |        |                |

> 📋 **ACTION – VENDOR RELATIONSHIP TRANSFER**:
> 1. Obtain portal logins for all critical vendors
> 2. Verify support contracts are active
> 3. Add our team as authorized contacts
> 4. Document escalation procedures
>
> **WATCH FOR**:
> - Support contracts registered to previous MSP
> - Expired maintenance agreements
> - Vendor requiring "reseller authorization"

---

## Section 8: Shadow IT Detection

> ⚠️ **THIS SECTION COMPLETED BY vCIO THROUGH INVESTIGATION**

### 8.1 Unsanctioned SaaS Discovery

**Discovery Methods**:
- Review expense reports for software charges
- Check DNS queries for unauthorized domains
- Interview department heads about tools
- Review email headers for third-party services

| Service Found | Department | Users | Data Risk | Action |
|---------------|------------|-------|-----------|--------|
|               |            |       |           |        |

**Common Enterprise Shadow IT**:
- Personal Dropbox/Google Drive (file sharing)
- Slack/Discord (communication)
- Trello/Asana (project management)
- Expensify/Concur (finance)
- ChatGPT/AI tools (data leakage risk)
- Personal email for business
- Unapproved CRM or sales tools

### 8.2 Rogue Infrastructure

| Finding | Location | Owner | Risk | Action |
|---------|----------|-------|------|--------|
|         |          |       |      |        |

**Look For**:
- Consumer routers/switches
- Unapproved wireless access points
- Personal NAS devices
- Shadow cloud servers (personal AWS/Azure)

### 8.3 Personal Account Usage

| Platform | Business Data? | User | Migration Required? |
|----------|----------------|------|---------------------|
|          |                |      |                     |

---

## Section 9: Quick Win Identification

> **Objective**: Identify 3-5 quick wins for first 30 days to demonstrate value.

### 9.1 Pain Points (from client interview)

| Pain Point | Urgency | Fix Complexity | Quick Win? |
|------------|---------|----------------|------------|
|            |         |                |            |

### 9.2 Low-Hanging Fruit (from discovery)

| Finding | Impact | Effort | Quick Win? |
|---------|--------|--------|------------|
|         |        |        |            |

**Quick Win Categories**:
- Obvious security gaps (MFA not enabled)
- Application frustrations (easy fix)
- Cost optimization (redundant licenses)
- Performance issues (simple tuning)
- Documentation gaps (visible deliverable)

---

## 30-60-90 Day Stabilization Plan

### Day 30 – Secure Foundation
- [ ] All critical credentials secured and documented
- [ ] Previous provider access revoked
- [ ] Our monitoring deployed on all systems
- [ ] Backup functionality verified
- [ ] Critical vulnerabilities identified
- [ ] Baseline documentation complete
- [ ] 3 quick wins delivered
- [ ] Regular reporting established

### Day 60 – Stabilization
- [ ] Vulnerability remediation in progress
- [ ] All vendor relationships transferred
- [ ] Full asset inventory complete
- [ ] Staff relationship building underway
- [ ] Recurring issues identified and addressed
- [ ] SLA performance baseline established

### Day 90 – Optimization
- [ ] Strategic roadmap presented
- [ ] Proactive recommendations delivered
- [ ] Process optimizations implemented
- [ ] Client satisfaction validated
- [ ] Transition to steady-state management
- [ ] QBR schedule established

---

## Risk Register (Complete During Discovery)

| Risk | Discovery Date | Severity | Pre-Existing? | Client Notified | Remediation |
|------|----------------|----------|---------------|-----------------|-------------|
|      |                |          |               |                 |             |

---

## Transition Health Scorecard

| Category | Status | Notes |
|----------|--------|-------|
| Credential Control | 🔴🟡🟢 |  |
| Previous MSP Cooperation | 🔴🟡🟢 |  |
| Documentation Quality | 🔴🟡🟢 |  |
| Security Posture | 🔴🟡🟢 |  |
| Backup Reliability | 🔴🟡🟢 |  |
| Compliance Status | 🔴🟡🟢 |  |
| Client Engagement | 🔴🟡🟢 |  |

---
*Document Version: 1.0 | Internal Use Only | Last Updated: December 2024*
