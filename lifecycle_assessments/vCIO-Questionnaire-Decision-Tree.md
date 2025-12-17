# vCIO Questionnaire Decision Tree

*Document Version: 2.0*

Use this guide to determine which assessment to run based on client lifecycle stage or trigger events.

---

## 1. Decision Flowchart

```mermaid
flowchart TD
    Start[🎯 Start Here] --> Q_New{New Client?}
    
    Q_New -- Yes --> A_Onboard[🚀 Onboarding]
    A_Onboard --> A_Baseline[📊 Tech Maturity Baseline]
    A_Baseline --> A_Risk[🛡️ Exec Risk Tolerance]
    A_Risk --> A_Keys[👥 Key Person Dependency]
    A_Keys --> A_Roadmap[📋 5-Year Roadmap]
    
    Q_New -- No --> Q_Annual{Annual Review?}
    
    Q_Annual -- Yes --> A_Refresh[🔄 Annual Refresher]
    A_Refresh --> A_Baseline2[📊 Tech Maturity Baseline]
    
    Q_Annual -- No --> Q_QBR{QBR Time?}
    
    Q_QBR -- Yes --> A_Health[🩺 Quarterly Health]
    
    Q_QBR -- No --> Q_Renewal{Major Renewal?}
    Q_Renewal -- Yes --> A_Vendor[💰 Vendor ROI]
    
    Q_Renewal -- No --> Q_Incident{Recent Incident?}
    Q_Incident -- Yes --> A_Post[🚨 Incident Postmortem]
    
    Q_Incident -- No --> Q_Turnover{Key Staff Change?}
    Q_Turnover -- Yes --> A_Keys2[👥 Key Person Dependency]
    
    Q_Turnover -- No --> Default[✅ Default Cadence]
    
    style Start fill:#a855f7,stroke:#7c3aed,stroke-width:2px,color:#fff
    style Default fill:#10b981,stroke:#059669,stroke-width:2px,color:#fff
    style A_Post fill:#ef4444,stroke:#dc2626,stroke-width:2px,color:#fff
    style A_Onboard fill:#3b82f6,stroke:#2563eb,stroke-width:2px,color:#fff
    style A_Roadmap fill:#3b82f6,stroke:#2563eb,stroke-width:2px,color:#fff
```

---

## 2. vCIO Engagement Model (Lifecycle Graphic)

```mermaid
flowchart LR
    vCIO((Strategic vCIO)) --> Quarterly
    vCIO -.-> Annual
    vCIO -.-> Event
    
    subgraph Quarterly[Quarterly Cadence]
        Q1[Q1: Health & Roadmap]
        Q2[Q2: Health & Risk]
        Q3[Q3: Health & Budget]
        Q4[Q4: Health & Strategy]
    end
    
    subgraph Annual[Annual Specific]
        AB[Annual Budget Planning]
        MB[Maturity Baseline]
    end
    
    subgraph Event[Event Driven]
        IR[Incident Response]
        VR[Vendor/Audit Renewal]
        LC[Leadership Change]
    end
    
    style vCIO fill:#3b82f6,stroke:#2563eb,stroke-width:2px,color:#fff
```

---

## 3. Deliverable Checklist Mapping

| Questionnaire / Assessment | Primary Deliverable | Secondary Outcome |
|---|---|---|
| Technology Maturity Baseline | Current State Report (Scores) | Gap Analysis for Roadmap |
| Executive Risk Tolerance | Risk Tolerance Statement | IT Policy Adjustments |
| Quarterly Health & Alignment | QBR Deck / Satisfaction Score | Priority Readjustment |
| Key Person Dependency | Knowledge Transfer Plan | Access Control Audit |
| Vendor Consolidation ROI | Savings Proposal | Shadow IT Discovery |
| Incident Postmortem | Root Cause Analysis (RCA) | Process Improvement Plan |
| Annual Budget Planning | 1-3 Year Budget Forecast | Capital Improvement Plan |

---

## 4. All Available Assessments

### Core Strategy
| Assessment | Description |
|---|---|
| 📋 5-Year Strategic Roadmap | Long-term IT vision & roadmap |
| 🚀 Onboarding / Account Takeover | New client discovery & baseline |
| 🔄 Annual Strategy Refresher | Yearly check-in on priorities |

### Lifecycle Assessments
| Assessment | Description |
|---|---|
| 🩺 Quarterly Health & Alignment | QBR alignment check |
| 📊 Technology Maturity Baseline | Technical posture scoring |
| 🛡️ Executive Risk Tolerance | Define risk appetite |
| 👥 Key Person Dependency | Bus factor analysis |
| 💰 Vendor Consolidation & ROI | License/vendor optimization |
| 🚨 Incident Postmortem | Root cause analysis |
