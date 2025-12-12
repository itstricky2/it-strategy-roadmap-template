# 5-Year IT Strategic Roadmap Questionnaire
## Government & Municipal Clients – vCIO Internal Version

> **Purpose**: This is the vCIO's working copy of the strategic roadmap questionnaire. It contains the same questions as the client-facing version plus embedded context, strategic implications, red flags, and follow-up probes.
>
> **Usage**: Use this during stakeholder interviews. The `💡 CONTEXT` blocks explain why each question matters. The `⚠️ RED FLAGS` highlight concerning responses. The `🔍 PROBE` sections suggest follow-up questions.

---

## Pre-Interview Preparation Checklist

- [ ] Review client's public CIP documents (usually on city website)
- [ ] Check council/board meeting minutes for recent IT discussions
- [ ] Review insurance certificate if available
- [ ] Research any public breach/incident disclosures
- [ ] Identify budget adoption timeline from public records
- [ ] Note upcoming election cycles (leadership turnover risk)

---

## Section 1: Organization & Mission

### 1.1 Mission & Vision

**1. What is your organization's primary mission or service objective?**

```
[Response]
```

> 💡 **CONTEXT**: The mission statement should inform all technology decisions. If the response is vague, help them articulate it. Look for keywords that indicate priorities: "public safety," "economic development," "citizen services," etc.

---

**2. What outcomes would define success for your organization over the next five years?**

```
1.
2.
3.
4.
5.
```

> 💡 **CONTEXT**: These become the "North Star" metrics for the roadmap. Every initiative should trace back to one of these outcomes. If they can't articulate outcomes, this is a governance maturity issue.
>
> 🔍 **PROBE**: "If the local paper wrote a story about your success in 2029, what would the headline say?"

---

**3. Are there any anticipated changes in organizational leadership within the next 2-3 years?**

- [ ] Yes
- [ ] No
- [ ] Uncertain

```
[Details]
```

> ⚠️ **RED FLAG**: Leadership transitions often stall or kill IT initiatives. If a City Manager is retiring, get executive sponsorship documented NOW before they leave. New leadership may have different priorities.
>
> 💡 **CONTEXT**: If there's an upcoming election, treat all "Horizon 1" projects as at-risk of political reprioritization.

---

### 1.2 Fiscal Planning & Budget Cycles

**4. What month does your fiscal year begin?**

```
[Month]
```

**5. In which quarter is your annual budget typically adopted?**

```
[Quarter]
```

> 💡 **CONTEXT – CRITICAL**: This is the single most important operational detail for a government vCIO.
>
> **BUDGET CIRCULAR TIMING**: If budget is adopted in June (Q2), project proposals MUST be submitted to Finance by January/February to make the budget cycle. Missing this window delays projects by 12 months.
>
> **ALIGNMENT RULE**: All Horizon 1 initiatives must be submitted before the next Budget Circular deadline, or they become Horizon 2 by default.

---

**6. Does your organization maintain a Capital Improvement Plan (CIP)?**

- [ ] Yes → Planning horizon: _____ years
- [ ] No
- [ ] In development

> 💡 **CONTEXT – CAPEX vs OPEX**:
> - **CapEx** (capital) can be funded by bonds, levies, and CIP funds – preferred for large purchases
> - **OpEx** (operational) comes from General Fund (competes with police/fire salaries)
>
> **STRATEGY**: Structure multi-year projects and hardware refreshes as CapEx whenever possible. A $200K server refresh as CapEx protects the General Fund. Same purchase as OpEx creates political friction.
>
> 🔍 **PROBE**: "Is there an IT line item in your current CIP, or would we need to advocate for adding one?"

---

**7. Are there any active federal or state grants with technology-eligible uses?**

| Grant Name | Amount | Obligation Deadline | Allowable IT Uses |
|------------|--------|---------------------|-------------------|
|            |        |                     |                   |

> 💡 **CONTEXT – THE GRANT CLIFF**: Federal grants (ARPA, JAG, UASI) have "obligation deadlines." Unspent funds revert. This is FREE MONEY for infrastructure hardening.
>
> **STRATEGY**: Identify grant funds immediately. Propose "one-time" infrastructure projects (hardware refreshes, perpetual licenses) that utilize these before expiration. This gets the client infrastructure essentially for free.
>
> ⚠️ **RED FLAG**: If they have significant unobligated grant funds within 6 months of deadline, escalate immediately. This is a quick-win opportunity.

---

### 1.3 Structural Changes

**8. Are there plans for construction of new municipal facilities, annexation, or new service locations?**

```
[Details]
```

> 💡 **CONTEXT – HIDDEN COSTS OF ANNEXATION**: New facilities are planned by architects who forget "low voltage."
>
> **ACTION REQUIRED**: Inject yourself into the architectural review process EARLY to ensure:
> - Fiber conduits in construction plans
> - Proper server room cooling/power
> - Physical security (cameras, access control)
> - Network drops and WiFi coverage
>
> Getting these into construction budget is 10x cheaper than IT afterthought retrofitting.
>
> 🔍 **PROBE**: "Are there any capital construction projects in the CIP where IT hasn't been formally consulted yet?"

---

**9. Are there planned mergers, consolidations, or shared services agreements?**

```
[Details]
```

> 💡 **CONTEXT**: Shared services (e.g., combined dispatch center, joint purchasing) create identity management and data sovereignty complexity. Factor in integration costs.

---

### 1.4 Workforce Dynamics

**10. Current total headcount:**

```
[Number]
```

**11. Projected headcount by 2030:**

```
[Growth trajectory]
```

**12. Significant retirements anticipated (Silver Tsunami)?**

```
[Departments affected]
```

> 💡 **CONTEXT – SILVER TSUNAMI**: Government workforce skews older. Mass retirements = institutional knowledge loss.
>
> **ROADMAP IMPLICATIONS**:
> - Include "Knowledge Capture" initiatives (documentation, process recording)
> - Prioritize automating manual processes before the experts leave
> - Consider "Digital Twin" approaches for complex municipal processes
>
> ⚠️ **RED FLAG**: If the only person who knows how a critical system works is 2 years from retirement, that's a Horizon 1 emergency.

---

## Section 2: IT Strategy & Governance

**13. Does a documented IT strategy exist?**

```
[Response]
```

> 💡 **CONTEXT**: If no formal strategy exists, that's actually an opportunity – you're starting fresh. If one exists but is outdated, get a copy and note which recommendations were never implemented (and why).

---

**14. How are IT priorities approved and funded?**

```
[Process description]
```

> 🔍 **PROBE**: "Walk me through how a $50,000 project would get approved. Who are the gatekeepers? What documentation is required?"
>
> 💡 **CONTEXT**: Understanding the approval chain prevents proposal rejections. Know if you need Finance Director sign-off, Council approval thresholds, etc.

---

**15. How does leadership view the IT function?**

- [ ] Cost center
- [ ] Business enabler
- [ ] Strategic partner

> 💡 **CONTEXT**: This determines your positioning strategy:
> - **Cost center** → Lead with TCO reduction, efficiency, consolidation
> - **Business enabler** → Lead with automation, citizen experience
> - **Strategic partner** → Lead with transformation, competitive positioning
>
> If they say "cost center," your roadmap presentation must emphasize ROI and savings. Avoid visionary language that will be dismissed.

---

**16. IT Steering Committee exists?**

```
[Response]
```

> 💡 **CONTEXT**: If no committee exists, recommend establishing one. This creates governance structure and ensures IT decisions have executive visibility. Monthly meetings with department heads = political capital.

---

## Section 3: Digital Service Delivery & Citizen Experience

### 3.1 Service Digitization

**17. High-volume services still requiring paper/physical presence:**

| Service | Current Process | Priority |
|---------|-----------------|----------|
|         |                 |          |

> 💡 **CONTEXT – THE DIGITAL GOVERNMENT WIN**: Moving processes like Building Permits from paper to digital is the HIGHEST-ROI activity. Benefits:
> - Reduces internal labor costs
> - Improves citizen satisfaction scores (political gold for City Managers)
> - Creates audit trails
>
> **FRAMING**: Never call these "IT upgrades." Call them "Citizen Service Improvements" or "Operational Efficiency Projects."

---

### 3.3 Smart Infrastructure

**21. Smart City / IoT initiatives planned:**

| Initiative | Technology | Segmented? |
|------------|------------|------------|
|            |            |            |

> ⚠️ **RED FLAG – THE SMART CITY TRAP**: Municipalities are sold IoT devices by vendors who ignore security. A smart water meter not on a segmented network = backdoor into financial systems.
>
> **MANDATORY for any IoT deployment**:
> - Network segmentation (VLANs/VRFs)
> - Separate management plane
> - Vendor security assessment
>
> If they're deploying IoT without segmentation, this is a Horizon 1 security remediation.

---

### 3.4 Data Governance

**23. AI/Automation interest level:**

```
[Response]
```

> 💡 **CONTEXT**: Government AI adoption is politically sensitive. Frame carefully:
> - Avoid terms like "replace workers" – use "augment staff"
> - Start with back-office automation (invoice processing, records requests)
> - Avoid public-facing AI chatbots until proven internally
>
> 🔍 **PROBE**: "What's the one repetitive task your staff complains about most? That's usually the best automation candidate."

---

## Section 4: Infrastructure & Legacy Systems

### 4.2 Legacy Risk

**26. End-of-Life systems in use:**

| System | OS Version | EoL Date | Replacement Funded? |
|--------|------------|----------|---------------------|
|        |            |          |                     |

> ⚠️ **RED FLAG – THE "RED-RATED" RISK**: Any EoL/unsupported system is a "Red Risk" per Legacy IT Risk Assessment Framework.
>
> **IF REPLACEMENT IS NOT FUNDED** (client refuses due to cost), the roadmap must shift to **Containment Strategy**:
> - Air-gap the server (no internet access)
> - Restrict user permissions to minimum necessary
> - Document the risk acceptance in writing (signed by department head)
>
> **LIABILITY PROTECTION**: Get written acknowledgment that the client is accepting this risk. This shifts liability of failure back to client.

---

### 4.3 Cloud Strategy

**29. Sensitive data cloud compliance:**

```
[Response]
```

> ⚠️ **RED FLAG – THE GOVCLOUD PREMIUM**: If client has CJIS data, they CANNOT legally use standard commercial Azure/AWS without a CJIS Security Addendum.
>
> **BUDGET IMPACT**: Government Community Cloud (GCC) licenses are typically **30-40% more expensive** than commercial. If the current budget assumes commercial pricing, there's a massive shortfall coming.
>
> 🔍 **PROBE**: "Are your current Microsoft 365 licenses GCC or commercial? Let's verify the tenant."

---

## Section 5: Cybersecurity & Compliance

### 5.1 Regulatory Frameworks

**34. CJIS Compliance details:**

| Last Audit | Findings | Remediated? |
|------------|----------|-------------|
|            |          |             |

> 💡 **CONTEXT – CJIS AUDIT CYCLES**: FBI/State CJIS audits occur on a fixed 3-year cycle. The roadmap must work BACKWARD from the next audit date.
>
> **STRATEGY**: A failed CJIS audit is a public relations disaster for Police Chiefs. Use this as leverage for security investment: "Chief, if we don't implement Advanced Authentication by [date], we risk failing the audit."
>
> Common CJIS findings:
> - Advanced Authentication (MFA) not on all CJI access points
> - Encryption gaps
> - Training documentation missing

---

### 5.3 Cyber Insurance

**39. Insurance status and carrier requirements:**

```
[Response]
```

> 💡 **CONTEXT – THE INSURANCE HARD MARKET**: Cyber insurance is no longer a rubber stamp. Carriers now DEMAND specific controls (MFA everywhere, immutable backups, EDR) as conditions of binding.
>
> **STRATEGY**: Align "Year 1 Security Roadmap" with insurance renewal date. Use the broker as leverage: "If we don't do this, you may lose coverage or see premiums triple."
>
> 🔍 **PROBE**: "May I see a copy of your latest cyber insurance application? I want to verify we're compliant with what was represented to the carrier."
>
> ⚠️ **RED FLAG**: If the client answered "Yes" to controls on their application that aren't actually in place, they may have coverage denial risk.

---

### 5.4 Business Continuity

**42. RTO/RPO Requirements:**

| Metric | Current | Required |
|--------|---------|----------|
| RTO    |         |          |
| RPO    |         |          |

> 💡 **CONTEXT**: Most clients don't know their RTO/RPO until you ask.
>
> **CALCULATION GUIDE**:
> - **RTO**: "If City Hall burned down at 2 AM, when MUST payroll be processing again?"
> - **RPO**: "If we lose data, how far back can we go? Last night? Last hour? Would you lose a week of work?"
>
> **COST ALIGNMENT**: Lower RTO/RPO = higher cost. A 4-hour RTO requires different (expensive) infrastructure than 48-hour RTO. Make them commit to a number so you can cost the solution.

---

## Section 6: Budget & Financial Planning

**46. CapEx vs OpEx preference:**

```
[Response]
```

> 💡 **CONTEXT – STRUCTURING DEALS FOR CIP**:
> - Hardware refreshes = CapEx (goes to CIP)
> - 3-year managed services contracts can sometimes be capitalized
> - Major software implementations with multi-year licenses = CapEx potential
>
> **POLITICAL REALITY**: Ask the Finance Director how to structure proposals for CIP eligibility. They'll appreciate the partnership.

---

## Section 7: Vendor & Partner Strategy

**49. Procurement vehicle preferences:**

```
[Response]
```

> 💡 **CONTEXT – PROCUREMENT REALITIES**:
> - **Sole source limits**: Typically $25K-$50K in municipalities. Know the threshold.
> - **Cooperative purchasing** (TIPS, Sourcewell, NASPO): Pre-competed contracts that bypass RFP process. Huge time saver.
> - **RFP timeline**: A formal RFP can take 3-6 months. Factor this into project timelines.
>
> 🔍 **PROBE**: "What's your sole source threshold? What cooperatives are you already members of?"

---

## Section 8: Three Horizons Planning

### Horizon 1: Stabilization (0-18 Months)

**51. What is currently "on fire"?**

```
1.
2.
3.
```

> 💡 **CONTEXT**: These become your "quick wins." Address these first to build credibility before proposing larger transformational initiatives.
>
> **PRIORITIZATION FRAMEWORK**:
> 1. Compliance/audit deadlines (non-negotiable)
> 2. Insurance requirements (coverage at stake)
> 3. Business impact (revenue/service affecting)
> 4. User experience (political visibility)

---

## Post-Interview Actions

- [ ] Send thank-you email with summary of key findings (within 24 hours)
- [ ] Request copies of: CIP, insurance policy, latest audit results, org chart
- [ ] Verify budget adoption timeline and next submission deadline
- [ ] Calculate "days until" next CJIS audit, insurance renewal, grant deadline
- [ ] Draft initiative list with preliminary horizon assignments
- [ ] Schedule follow-up presentation (within 2 weeks)

---

## Risk Register Template (Start During Interview)

| Risk | Source Question | Urgency | Client Awareness |
|------|-----------------|---------|------------------|
|      |                 |         |                  |

---
*Document Version: 1.0 | Internal Use Only | Last Updated: December 2024*
