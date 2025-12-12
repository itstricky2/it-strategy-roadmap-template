# IT Strategy & Roadmap Template

## Executive Summary

This repository provides an **enterprise-grade framework** for IT strategy development and client onboarding. It includes questionnaires, automation scripts, and visualization tools to build comprehensive 5-year IT roadmaps.

**Designed for**: vCIOs, MSPs, and IT consultants serving government agencies and medium enterprises.

## Quick Start

### For New 5-Year Strategy Engagements

1. Select appropriate questionnaire:
   - Government/Municipal: [`questionnaires/roadmap/govt_roadmap_client.md`](questionnaires/roadmap/govt_roadmap_client.md)
   - Enterprise: [`questionnaires/roadmap/enterprise_roadmap_client.md`](questionnaires/roadmap/enterprise_roadmap_client.md)

2. Complete questionnaire with client (use internal versions for vCIO context)

3. Transfer answers to YAML: [`questionnaires/schemas/roadmap_answers.yaml`](questionnaires/schemas/roadmap_answers.yaml)

4. Generate roadmap:
   ```bash
   python3 scripts/roadmap_generator.py --input client_answers.yaml --output-dir roadmap/
   ```

### For Account Takeover/Onboarding

1. Select appropriate questionnaire:
   - Government/Municipal: [`questionnaires/onboarding/govt_onboarding_client.md`](questionnaires/onboarding/govt_onboarding_client.md)
   - Enterprise: [`questionnaires/onboarding/enterprise_onboarding_client.md`](questionnaires/onboarding/enterprise_onboarding_client.md)

2. Complete during first 30 days of engagement

3. Generate reports:
   ```bash
   python3 scripts/onboarding_processor.py --input onboarding_answers.yaml --output-dir reports/
   ```

## Repository Structure

```
├── questionnaires/
│   ├── roadmap/                    # 5-Year Strategy Questionnaires
│   │   ├── govt_roadmap_client.md      # Government - Client facing
│   │   ├── govt_roadmap_internal.md    # Government - vCIO version
│   │   ├── enterprise_roadmap_client.md    # Enterprise - Client facing
│   │   └── enterprise_roadmap_internal.md  # Enterprise - vCIO version
│   ├── onboarding/                 # Account Takeover Questionnaires
│   │   ├── govt_onboarding_client.md
│   │   ├── govt_onboarding_internal.md
│   │   ├── enterprise_onboarding_client.md
│   │   └── enterprise_onboarding_internal.md
│   └── schemas/                    # YAML answer templates for automation
│       ├── roadmap_answers.yaml
│       └── onboarding_answers.yaml
├── scripts/                        # Python automation
│   ├── roadmap_generator.py        # Generates Mermaid roadmaps from answers
│   ├── onboarding_processor.py     # Generates risk reports from answers
│   └── utils/
├── roadmap/                        # Mermaid.js visualizations
│   ├── strategic_roadmap.mmd       # 5-year high-level view
│   └── tactical_roadmap.mmd        # 18-month detailed Gantt
├── initiatives/                    # Initiative detail documents
├── docs/
│   └── FORM_CONVERSION.md          # Guide for fillable forms
├── QUESTIONNAIRE.md                # Legacy (deprecated)
└── CONTRIBUTING.md                 # Governance process
```

## Questionnaire System

### Client-Facing Versions
Designed for clients to complete independently. Clean formatting, clear instructions, professional presentation.

### Internal vCIO Versions
Include the same questions plus:
- **💡 CONTEXT**: Strategic implications of each question
- **⚠️ RED FLAGS**: Warning signs to watch for
- **🔍 PROBE**: Follow-up questions to uncover hidden issues
- **📋 ACTION**: Immediate steps required

### Coverage

| Domain | Roadmap | Onboarding |
|--------|---------|------------|
| Organization & Mission | ✅ | |
| IT Strategy & Governance | ✅ | |
| Digital Service Delivery | ✅ | |
| Infrastructure & Legacy | ✅ | ✅ |
| Cybersecurity & Compliance | ✅ | ✅ |
| Budget & Financial | ✅ | |
| Vendor & Partner Strategy | ✅ | ✅ |
| Three Horizons Planning | ✅ | |
| Access & Credentialing | | ✅ |
| Shadow IT Detection | | ✅ |
| Liability Baseline | | ✅ |
| 30-60-90 Day Planning | | ✅ |

## Automation Scripts

### Roadmap Generator
Transforms questionnaire answers into:
- `strategic_roadmap.mmd` - 5-year Mermaid Gantt
- `tactical_roadmap.mmd` - 18-month execution plan
- Individual initiative markdown files

### Onboarding Processor
Generates:
- Risk assessment report with scores
- Immediate action items (prioritized)
- 30-60-90 day stabilization plan
- Credential handover checklist

## Framework

Uses the **Three Horizons Model**:
- **Horizon 1 (0-18 months)**: Stabilization & Quick Wins
- **Horizon 2 (18-36 months)**: Scale & Optimization
- **Horizon 3 (36-60 months)**: Innovation & Transformation

## Form Conversion

Questionnaires can be converted to fillable formats. See [`docs/FORM_CONVERSION.md`](docs/FORM_CONVERSION.md) for:
- Microsoft Forms
- Google Forms
- Adobe Acrobat fillable PDF
- Premium options (Typeform, Jotform)

---

*Template Version: 2.0 | Last Updated: December 2024*
