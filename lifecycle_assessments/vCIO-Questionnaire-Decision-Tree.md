# vCIO Questionnaire Decision Tree

**Goal**: Quickly choose the right questionnaire at the right time across the client lifecycle.
**Rule**: If more than one condition matches, **run the highest-risk questionnaire first**.

---

## 1. Are we onboarding or taking over the account?

**Yes** - Run these in order:
1.  **[Technology Maturity Baseline](vCIO-Technology-Maturity-Baseline.md)**
    *   _Establish current state across identity, endpoints, backups, network, and process._
2.  **[Executive Risk Tolerance](vCIO-Executive-Risk-Tolerance.md)**
    *   _Document acceptable downtime, data loss, security tradeoffs, and escalation thresholds._
3.  **[Key Person Dependency](vCIO-Key-Person-Dependency.md)**
    *   _Identify single points of human failure, undocumented systems, credential fragility._

*Then schedule:*
*   Quarterly Health & Alignment for the next QBR cycle
*   Annual Budget & Capital Planning based on fiscal calendar

**No** - Go to section 2.

---

## 2. Is it time for a Quarterly Business Review?

**Yes** - Run:
*   **[Quarterly Health & Alignment](vCIO-Quarterly-Health-Alignment.md)**

*Then ask:*
*   “Did priorities shift materially?”
*   If yes, consider rerunning **Executive Risk Tolerance** (if last run was >18 months ago) and updating the roadmap.

**No** - Go to section 3.

---

## 3. Are we within budget planning season?
*Trigger signals: Budget circular window, Dept requests, Fiscal year-end approaching.*

**Yes** - Run:
*   **Annual Budget & Capital Planning** (Use Core Roadmap Template)

*Then check:*
*   Are there major renewals in next 90–120 days?
*   If yes, also run **[Vendor Consolidation ROI](vCIO-Vendor-Consolidation-ROI.md)**

**No** - Go to section 4.

---

## 4. Are we within 90 days of an audit, renewal, or insurance event?
*Trigger signals: Cyber insurance renewal, Compliance review, Audit.*

**Yes** - Run:
*   **Pre-Audit & Insurance Renewal Checklist** (Use Refresher)

*Then check:*
*   Was there a material incident in the last 6–12 months?
*   If yes, also run **[Incident Postmortem](vCIO-Incident-Postmortem.md)** and link corrective actions to the renewal narrative.

**No** - Go to section 5.

---

## 5. Is there a facility change, buildout, or expansion?
*Trigger signals: New office, renovation, expansion.*

**Yes** - Run:
*   **New Build & Expansion Scoping** (Custom Scoping)

*Then check:*
*   Does the expansion require new users, data, or system integration?
*   If yes, add a mini-assessment using:
    *   **Technology Maturity Baseline** (impacted sections)
    *   **Vendor Consolidation ROI** (if new vendors introduced)

**No** - Go to section 6.

---

## 6. Are we approaching major vendor renewals or tool sprawl is suspected?
*Trigger signals: M365/Security stack renewal, overlapping tools.*

**Yes** - Run:
*   **[Vendor Consolidation ROI](vCIO-Vendor-Consolidation-ROI.md)**

*Then check:*
*   Is leadership pushing back on IT spend?
*   If yes, pair this with **Quarterly Health & Alignment** to re-anchor value.

**No** - Go to section 7.

---

## 7. Did a material incident occur?
*Trigger signals: Outage, Ransomware, Breach, DR event.*

**Yes** - Run:
*   **[Incident Postmortem](vCIO-Incident-Postmortem.md)**

*Then check:*
*   Is insurance renewal or audit within 90 days?
*   If yes, immediately also run **Pre-Audit & Insurance Renewal Checklist**.

**No** - Go to section 8.

---

## 8. Is there organizational instability or staffing change?
*Trigger signals: IT leader departure, Key person exits, M&A.*

**Yes** - Run:
*   **[Key Person Dependency](vCIO-Key-Person-Dependency.md)**

*Then check:*
*   Are there changes in risk appetite or leadership expectations?
*   If yes, rerun **Executive Risk Tolerance**.

**No** - Go to section 9.

---

## 9. Default Operating Cadence

If none of the above triggers apply, run on schedule:
*   **Quarterly Health & Alignment**: Every Quarter
*   **Annual Budget**: Annually (Fiscal)
*   **Technology Maturity Baseline**: Annually
*   **Executive Risk Tolerance**: Every 18–24 Months
*   **Vendor Consolidation ROI**: Annually or before big renewals

---

## Risk Priority Rule
*If multiple triggers hit at once, run in this order:*

1.  **Incident Postmortem** (Critical)
2.  **Pre-Audit & Insurance Renewal** (Compliance/Legal)
3.  **Annual Budget** (Financial)
4.  **New Build** (Project)
5.  **Technology Maturity** (Foundational)
6.  **Executive Risk** (Strategic)
7.  **Key Person Dependency** (Risk)
8.  **Vendor Consolidation** (Efficiency)
9.  **Quarterly Health** (Relationship)

