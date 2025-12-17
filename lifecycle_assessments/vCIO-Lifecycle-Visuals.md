# vCIO Lifecycle Visuals & Toolkit

## 1. Internal vCIO Triage Flowchart
_Use this flowchart to quickly determine the correct assessment trigger._

```mermaid
flowchart TD
    Start[Triggers / Events] --> Q_Onboarding{Onboarding?}
    
    Q_Onboarding -- Yes --> A_Baseline[Tech Maturity Baseline]
    A_Baseline --> A_Risk[Exec Risk Tolerance]
    A_Risk --> A_Keys[Key Person Dependency]
    
    Q_Onboarding -- No --> Q_QBR{QBR Time?}
    
    Q_QBR -- Yes --> A_Health[Quarterly Health & Alignment]
    Q_QBR -- No --> Q_Budget{Budget Season?}
    
    Q_Budget -- Yes --> A_Budget[Annual Budget Planning]
    A_Budget --> Q_MajorRen{Major Renewals?}
    Q_MajorRen -- Yes --> A_Vendor[Vendor Consolidation ROI]
    
    Q_Budget -- No --> Q_Audit{Audit/Renewal <90 Days?}
    
    Q_Audit -- Yes --> A_PreAudit[Pre-Audit Checklist]
    A_PreAudit --> Q_Inc{Recent Incident?}
    Q_Inc -- Yes --> A_Post[Incident Postmortem]
    
    Q_Audit -- No --> Q_Fac{Facility Change?}
    Q_Fac -- Yes --> A_Build[New Build Scoping]
    
    Q_Fac -- No --> Q_Ind{Material Incident?}
    Q_Ind -- Yes --> A_Post2[Incident Postmortem]
    
    Q_Ind -- No --> Q_Stab{Org Instability?}
    Q_Stab -- Yes --> A_Keys2[Key Person Dependency]
    
    Q_Stab -- No --> Default[Default Cadence]
    
    style Start fill:#f9f,stroke:#333,stroke-width:2px
    style Default fill:#cfc,stroke:#333,stroke-width:2px
    style A_Post fill:#fcc,stroke:#f00,stroke-width:2px
    style A_Post2 fill:#fcc,stroke:#f00,stroke-width:2px
```

---

## 2. Client-Facing Lifecycle Graphic
_Share this to explain the vCIO engagement model._

```mermaid
graph LR
    subgraph Annual_Specific
    direction TB
    Budget[Annual Budget Planning]
    Maturity[Maturity Baseline]
    end
    
    subgraph Quarterly
    Q1[Q1: Health & Roadmap]
    Q2[Q2: Health & Risk]
    Q3[Q3: Health & Budget]
    Q4[Q4: Health & Strategy]
    end
    
    subgraph Event_Driven
    direction TB
    Incident[Incident Response]
    Renewal[Vendor/Audit Renewal]
    KeyPerson[Leadership Change]
    end
    
    Strategy((Strategic vCIO)) --> Quarterly
    Strategy --> Annual_Specific
    Strategy -.-> Event_Driven
    
    classDef strategic fill:#1f77b4,color:white;
    class Strategy strategic;
```

---

## 3. Deliverable Checklist Mapping

| Questionnaire / Assessment | Primary Deliverable | Secondary Outcome |
|----------------------------|---------------------|-------------------|
| **Technology Maturity Baseline** | Current State Report (Scores) | Gap Analysis for Roadmap |
| **Executive Risk Tolerance** | Risk Tolerance Statement | IT Policy Adjustments |
| **Quarterly Health & Alignment** | QBR Deck / Satisfaction Score | Priority Readjustment |
| **Key Person Dependency** | Knowledge Transfer Plan | Access Control Audit |
| **Vendor Consolidation ROI** | Savings Proposal | Shadow IT Discovery |
| **Incident Postmortem** | Root Cause Analysis (RCA) | Process Improvement Plan |
| **Annual Budget Planning** | 1-3 Year Budget Forecast | Capital Improvement Plan |

---
