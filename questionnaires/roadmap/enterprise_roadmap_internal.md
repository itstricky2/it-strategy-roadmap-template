# 5-Year IT Strategic Roadmap Questionnaire
## Medium Enterprise Clients – vCIO Internal Version

> **Purpose**: This is the vCIO's working copy of the strategic roadmap questionnaire for enterprise clients. It contains the same questions as the client-facing version plus embedded context, strategic implications, red flags, and follow-up probes.
>
> **Usage**: Use this during stakeholder interviews. The `💡 CONTEXT` blocks explain why each question matters. The `⚠️ RED FLAGS` highlight concerning responses. The `🔍 PROBE` sections suggest follow-up questions.

---

## Pre-Interview Preparation Checklist

- [ ] Review company website and recent press releases
- [ ] Check LinkedIn for leadership changes/hiring patterns
- [ ] Research industry trends and competitive landscape
- [ ] Review any available financial information (if public/shared)
- [ ] Identify key industry compliance requirements
- [ ] Note recent M&A activity in their sector

---

## Section 1: Organization & Business Strategy

### 1.1 Mission & Vision

**1. What is your organization's primary mission or value proposition?**

```
[Response]
```

> 💡 **CONTEXT**: Understanding the value proposition helps position IT as an enabler. If they're a "low-cost provider," expect cost pressure. If "innovation leader," expect appetite for emerging tech.

---

**2. Top 3-5 strategic business goals for the next five years:**

| Goal | Target Metric | Timeline |
|------|---------------|----------|
|      |               |          |

> 💡 **CONTEXT**: These goals become your "IT Alignment Matrix." Every initiative must map to at least one business goal. If IT can't articulate how it supports these, it's seen as overhead.
>
> 🔍 **PROBE**: "Which of these goals is the CEO most personally invested in? That's where IT investment will get the fastest approval."

---

**3. Planned leadership changes:**

```
[Response]
```

> ⚠️ **RED FLAG**: If the CEO/COO/CFO is changing, expect IT priorities to shift. Get executive sponsorship documented and approved BEFORE transitions. New leadership = 90-day pause on discretionary projects.
>
> 💡 **CONTEXT**: If owned by PE (private equity), there's usually a 3-5 year exit timeline. All IT investments need to show value accretion or cost reduction that improves sale price.

---

### 1.2 Growth & Expansion

**4. Revenue growth projection:**

```
[Response]
```

> 💡 **CONTEXT – GROWTH ALIGNMENT**:
> - **Aggressive growth (>25%)**: Infrastructure must scale. Expect cloud, automation, integration priorities.
> - **Moderate growth (5-15%)**: Optimization focus. Efficiency, cost control, standardization.
> - **Contraction**: Cost cutting. Consolidation, vendor negotiation, headcount impact.
>
> **RULE**: IT budget should grow proportionally with revenue. If they want 25% growth with flat IT spend, that's a red flag discussion.

---

**5. Geographic expansion or new market entry:**

```
[Response]
```

> 💡 **CONTEXT**: New markets = new compliance requirements.
> - **EU expansion** → GDPR mandatory (€20M+ fines possible)
> - **California customers** → CCPA considerations
> - **International** → Data residency, latency, local support
>
> 🔍 **PROBE**: "Have you consulted legal about data residency requirements in target markets?"

---

**6. M&A activity anticipated:**

| Activity | Likelihood | Timeline | IT Impact |
|----------|------------|----------|-----------|
|          |            |          |           |

> ⚠️ **RED FLAG**: If acquisition is likely, IT due diligence reveals skeletons. Clean up:
> - License compliance (audit risk)
> - Security posture (liability)
> - Technical debt (valuation impact)
>
> 💡 **CONTEXT**: PE-backed companies likely to acquire = need integration playbook. Companies likely to BE acquired = need clean documentation and defensible security.
>
> 🔍 **PROBE**: "Has IT ever been part of M&A due diligence? What did the last acquisition's IT integration look like?"

---

### 1.3 Workforce Dynamics

**9. Current workplace model:**

```
[Response]
```

> 💡 **CONTEXT – HYBRID REALITY**:
> - Hybrid = most complex IT environment (must support both)
> - Need strong identity management, VPN/ZTNA, and collaboration tools
> - Physical security changes (fewer badge-ins = harder to detect compromise)
>
> 🔍 **PROBE**: "What happens when a remote employee is terminated? How fast is access revoked?"

---

**10. Technology skill gaps:**

```
[Response]
```

> 💡 **CONTEXT**: Skill gaps = training budget OR outsourcing need. This is an opportunity to expand MSP services.
>
> **COMMON GAPS**:
> - Cloud (everyone's legacy team)
> - Security (specialized, expensive)
> - Data/Analytics (hot market)

---

## Section 2: IT Strategy & Governance

**13. How does executive leadership view IT?**

```
[Response]
```

> 💡 **CONTEXT – POSITIONING STRATEGY**:
> - **Cost center** → Lead with TCO reduction, consolidation, risk mitigation
> - **Business enabler** → Lead with efficiency, automation, user productivity
> - **Strategic differentiator** → Lead with innovation, competitive advantage, revenue enablement
>
> **WARNING**: If they say "strategic" but fund like "cost center," there's a disconnect. Watch for this.
>
> 🔍 **PROBE**: "When's the last time IT presented directly to the board? What was the topic?"

---

**14. IT budget as percentage of revenue:**

```
[Response]
```

> 💡 **CONTEXT – INDUSTRY BENCHMARKS**:
> - Manufacturing: 1-3%
> - Financial Services: 5-10%
> - Technology: 10-15%
> - Healthcare: 4-6%
> - Retail: 2-4%
>
> **If significantly below benchmark**: Either extremely efficient OR underinvested (risk accumulation).
>
> **If significantly above benchmark**: Either strategic investment OR inefficient (consolidation opportunity).

---

## Section 3: Digital Transformation & Customer Experience

### 3.1 Digital Maturity

**16. Digital maturity self-assessment:**

```
[Response]
```

> 💡 **CONTEXT**: Self-assessments skew optimistic. Validate with follow-up:
>
> 🔍 **PROBE**: "Walk me through how a customer order flows from website to fulfillment. How many manual handoffs are there?"
>
> **MATURITY INDICATORS**:
> - Laggard: Spreadsheets, email approvals, manual data entry
> - Aware: Some systems, but not integrated
> - Engaged: Integrated systems, dashboards
> - Leader: Predictive, automated, AI-augmented

---

### 3.3 Data & Analytics

**21. Single source of truth for business data:**

```
[Response]
```

> ⚠️ **RED FLAG**: "No – data siloed" = foundation must be fixed before any analytics/AI initiatives.
>
> 💡 **CONTEXT**: The #1 reason AI projects fail is data quality. If they want AI but don't have data governance, sequence correctly: Governance → Integration → Analytics → AI
>
> 🔍 **PROBE**: "If I asked Sales and Finance for 'last quarter's revenue,' would I get the same number?"

---

**22. AI/automation interest:**

```
[Response]
```

> 💡 **CONTEXT – AI HYPE MANAGEMENT**:
> - Everyone wants "AI" but few have the data foundation
> - Start with RPA (robotic process automation) for quick wins
> - Generative AI (ChatGPT-style) has real use cases but also real risks
>
> **ENTERPRISE AI READINESS CHECKLIST**:
> - [ ] Data quality validated
> - [ ] Data governance in place
> - [ ] Acceptable use policy exists
> - [ ] Legal reviewed IP/confidentiality
>
> ⚠️ **RED FLAG**: If employees are already using ChatGPT with company data without governance = immediate risk.

---

## Section 4: Infrastructure & Technology Stack

### 4.2 Critical Applications

**25. Mission-critical applications:**

| Application | Purpose | Hosting | Vendor | Contract End | Satisfaction |
|-------------|---------|---------|--------|--------------|--------------|
|             |         |         |        |              |              |

> 💡 **CONTEXT – CONTRACT TIMING**:
> - Note all contract end dates
> - Renegotiation/replacement projects need 6-12 month lead time
> - Expiring contracts = leverage for negotiation
>
> 🔍 **PROBE**: "Any applications getting acquired, sunset, or changing pricing models that concern you?"

---

**26. Applications causing user frustration:**

```
[Response]
```

> 💡 **CONTEXT**: User pain = political capital for fixing. These are "quick win" candidates.
>
> **CATEGORIZE**:
> - Training issue (fix with enablement)
> - Configuration issue (fix with optimization)
> - Fundamental mismatch (replace)

---

### 4.3 Legacy Systems

**27. Unsupported systems:**

| System | Issue | Business Risk | Replacement Planned? |
|--------|-------|---------------|---------------------|
|        |       |               |                     |

> ⚠️ **RED FLAG**: Unsupported = unpatched = breachable. Every SOC 2 auditor and insurance carrier asks about this.
>
> 💡 **CONTEXT**: If budget won't support replacement, document containment strategy:
> - Network isolation
> - Limited user access
> - Enhanced monitoring
> - Written risk acceptance from business owner

---

## Section 5: Cybersecurity & Compliance

### 5.1 Regulatory Requirements

**30. Applicable compliance frameworks:**

```
[Response]
```

> 💡 **CONTEXT – COMPLIANCE MAPPING**:
>
> | Framework | Who Needs It |
> |-----------|--------------|
> | SOC 2 | Anyone with enterprise customers asking for security assurance |
> | PCI-DSS | Anyone processing credit cards |
> | HIPAA | Healthcare data (including employee benefits sometimes) |
> | GDPR | Any EU customers or employees |
>
> 🔍 **PROBE**: "Have you lost any deals because you couldn't produce a SOC 2 report?"
>
> **SALES ENABLEMENT**: SOC 2 is increasingly a sales requirement. If prospects are asking and they don't have it, there's ROI in compliance.

---

### 5.2 Security Posture

**32. Security incidents in past 24 months:**

```
[Response]
```

> 💡 **CONTEXT**: Incident history informs priority. No incidents ≠ secure; sometimes means undetected.
>
> 🔍 **PROBE**: "Do you have security monitoring that would actually detect an intruder? How long could someone be in your network before you'd know?"

---

**33. Security controls in place:**

| Control | Status | Coverage |
|---------|--------|----------|
| MFA |  |  |
| EDR |  |  |

> ⚠️ **RED FLAG – INSURANCE REQUIREMENTS**: Cyber insurers now mandate:
> - MFA on all remote access and privileged accounts
> - EDR (not just antivirus)
> - Immutable/offsite backups
> - Phishing training
>
> **If missing these, they may not be able to get or renew cyber insurance.**
>
> 🔍 **PROBE**: "May I see your most recent cyber insurance application? I want to verify controls match what was attested."

---

### 5.4 Business Continuity

**37. Recovery requirements:**

| Requirement | Goal |
|-------------|------|
| RTO |  |
| RPO |  |

> 💡 **CONTEXT – COST CALIBRATION**:
>
> | RTO | Infrastructure Required | Cost Level |
> |-----|-------------------------|------------|
> | Minutes | Hot standby, auto-failover | $$$$$ |
> | 1-4 hours | Warm standby, quick recovery | $$$ |
> | 24 hours | Cold backup, restoration | $$ |
> | Days | Basic backup | $ |
>
> **QUESTION TO ASK CLIENT**: "If your systems were down for 24 hours, what would the business impact be in dollars?"
>
> That number justifies the DR investment.

---

## Section 6: Budget & Investment

**42. Appetite for increased IT investment:**

```
[Response]
```

> 💡 **CONTEXT – INVESTMENT FRAMING**:
> - **"Growth mindset"** → Full roadmap, innovation-forward
> - **"Need strong business case"** → ROI-focused, conservative timeline
> - **"Cost containment"** → Optimization, consolidation, efficiency gains
>
> 🔍 **PROBE**: "What was the last IT project that got killed and why? What would it have taken to get approved?"

---

## Section 7: Vendor & Partner Ecosystem

**44. Key technology vendors:**

| Vendor | Category | Contract End | Relationship |
|--------|----------|--------------|--------------|
|        |          |              |              |

> 💡 **CONTEXT – CONSOLIDATION OPPORTUNITY**:
> - Too many vendors = management overhead, integration complexity
> - Look for overlapping capabilities (two backup solutions, multiple security tools)
> - Contract timing alignment enables negotiation leverage

---

**46. Current MSP relationship:**

```
[Response]
```

> 💡 **CONTEXT – DISPLACEMENT INTELLIGENCE**:
> - Understand what the current provider does well (don't break it)
> - Understand pain points (your differentiator)
> - Check for hostility risk (see Onboarding questionnaire)
>
> 🔍 **PROBE**: "If you could change one thing about your current IT support, what would it be?"

---

## Section 8: Three Horizons Planning

### Horizon 1: Stabilization (0-18 Months)

**47. Technology issues impacting operations:**

```
1.
2.
3.
```

> 💡 **CONTEXT**: These are your "Day 1" priorities. Fix these first to build credibility.
>
> **PRIORITIZE BY**:
> 1. Revenue impact (anything affecting customers/sales)
> 2. Security/compliance risk
> 3. Employee productivity
> 4. Cost/efficiency

---

### Horizon 2: Scale (2-3 Years)

**49. Systems needed for growth targets:**

```
[Response]
```

> 💡 **CONTEXT**: Map these to growth goals from Section 1. If they want 25% growth but can't articulate infrastructure needs, they'll hit a wall.
>
> **COMMON SCALE REQUIREMENTS**:
> - ERP upgrade/replacement
> - Integration platform
> - Data warehouse
> - Security operations scaling

---

### Horizon 3: Innovation (3-5 Years)

**52. "Moonshot" technology initiative:**

```
[Response]
```

> 💡 **CONTEXT**: The moonshot reveals strategic ambition. But ground it:
>
> **REALITY CHECK QUESTIONS**:
> - "What percentage of budget would you allocate to experimentation?"
> - "Is there C-level sponsorship for this?"
> - "What competitors are doing this?"
>
> **Don't let Horizon 3 distract from Horizon 1 execution.**

---

## Post-Interview Actions

- [ ] Send thank-you and summary (within 24 hours)
- [ ] Request: Org chart, current IT budget, key vendor contracts
- [ ] Map business goals to IT initiatives
- [ ] Identify quick wins for first 90 days
- [ ] Draft initiative list with horizon assignments
- [ ] Prepare ROI models for key recommendations
- [ ] Schedule follow-up presentation (within 2 weeks)

---

## Opportunity Assessment Template

| Opportunity | Business Goal Link | Estimated Value | Effort | Priority |
|-------------|-------------------|-----------------|--------|----------|
|             |                   |                 |        |          |

---
*Document Version: 1.0 | Internal Use Only | Last Updated: December 2024*
