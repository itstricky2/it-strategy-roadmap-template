#!/usr/bin/env python3
"""
IT Onboarding/Account Takeover Processor

Transforms YAML onboarding questionnaire answers into:
- Risk assessment summary report
- Immediate action items list
- 30-60-90 day stabilization plan
- Credential/access handover checklist

Usage:
    python onboarding_processor.py --input answers.yaml --output-dir ./reports/
    python onboarding_processor.py --validate-schema ./schemas/onboarding_answers.yaml
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional
import yaml


def load_yaml(file_path: Path) -> dict:
    """Load and parse a YAML file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def validate_answers(answers: dict) -> list[str]:
    """Validate that required fields are present in answers."""
    errors = []
    
    # Check metadata
    if not answers.get('metadata', {}).get('client_name'):
        errors.append("Missing metadata.client_name")
    
    # Check critical sections
    if not answers.get('access_sovereignty'):
        errors.append("Missing access_sovereignty section")
    
    return errors


def calculate_risk_score(answers: dict) -> dict:
    """Calculate overall risk scores based on answers."""
    scores = {
        'access_control': 0,
        'security_posture': 0,
        'compliance': 0,
        'documentation': 0,
        'vendor': 0,
        'backup': 0
    }
    
    max_score = 10  # Per category
    
    # Access Control Risk
    access = answers.get('access_sovereignty', {})
    if access.get('break_glass_credentials', {}).get('documented'):
        scores['access_control'] += 3
    
    admin_accounts = access.get('global_admin_accounts', [])
    client_controlled = sum(1 for acc in admin_accounts if acc.get('account_owner') == 'client_named_user')
    if client_controlled > 0:
        scores['access_control'] += 4
    
    dns = access.get('domain_dns_control', {})
    if dns.get('registrar_login_verified') and dns.get('dns_login_verified'):
        scores['access_control'] += 3
    
    # Security Posture Risk
    liability = answers.get('liability_baseline', {})
    vulns = liability.get('known_vulnerabilities', [])
    critical_vulns = sum(1 for v in vulns if v.get('severity') == 'critical')
    scores['security_posture'] = max(0, 10 - (critical_vulns * 3))
    
    # Compliance Risk
    compliance = answers.get('compliance_status', {})
    audits = compliance.get('last_audits', [])
    passed_audits = sum(1 for a in audits if a.get('result') == 'passed')
    if audits:
        scores['compliance'] = int((passed_audits / len(audits)) * 10)
    else:
        scores['compliance'] = 5  # Unknown
    
    # Documentation Risk
    docs = answers.get('documentation', {})
    doc_items = [
        docs.get('network_diagram', {}).get('exists'),
        docs.get('ip_address_scheme', {}).get('documented'),
        docs.get('dr_documentation', {}).get('dr_plan_exists'),
        docs.get('asset_inventory', {}).get('exists'),
        docs.get('password_vault', {}).get('exists')
    ]
    doc_score = sum(1 for d in doc_items if d)
    scores['documentation'] = doc_score * 2
    
    # Vendor Risk
    vendor_deps = answers.get('vendor_dependencies', {})
    outgoing_msp = vendor_deps.get('outgoing_msp', {})
    if outgoing_msp.get('relationship_status') == 'cooperative':
        scores['vendor'] = 10
    elif outgoing_msp.get('relationship_status') == 'unresponsive':
        scores['vendor'] = 5
    elif outgoing_msp.get('relationship_status') == 'hostile':
        scores['vendor'] = 2
    else:
        scores['vendor'] = 7
    
    # Backup Risk
    critical = answers.get('critical_systems', {})
    backup = critical.get('backup_status', {})
    if backup.get('last_successful_backup'):
        scores['backup'] += 3
    if backup.get('offsite_copy'):
        scores['backup'] += 3
    if backup.get('immutable'):
        scores['backup'] += 2
    if backup.get('restore_test_successful'):
        scores['backup'] += 2
    
    # Calculate overall
    total = sum(scores.values())
    max_total = max_score * len(scores)
    scores['overall'] = round((total / max_total) * 100)
    scores['overall_rating'] = 'GREEN' if scores['overall'] >= 70 else 'YELLOW' if scores['overall'] >= 40 else 'RED'
    
    return scores


def extract_immediate_actions(answers: dict) -> list[dict]:
    """Extract and prioritize immediate action items."""
    actions = []
    
    # Check access control
    access = answers.get('access_sovereignty', {})
    
    if not access.get('break_glass_credentials', {}).get('documented'):
        actions.append({
            'action': 'Document all administrative credentials',
            'priority': 'CRITICAL',
            'category': 'Access Control',
            'timeline': 'Day 1'
        })
    
    # Check for MSP-controlled admin accounts
    admin_accounts = access.get('global_admin_accounts', [])
    for acc in admin_accounts:
        if acc.get('account_owner') in ['delegated_partner', 'previous_msp']:
            actions.append({
                'action': f"Create client-controlled admin account for {acc.get('platform', 'Unknown Platform')}",
                'priority': 'CRITICAL',
                'category': 'Access Control',
                'timeline': 'Day 1'
            })
            break
    
    # Check DNS control
    dns = access.get('domain_dns_control', {})
    if not dns.get('registrar_login_verified'):
        actions.append({
            'action': 'Verify domain registrar access and update credentials',
            'priority': 'CRITICAL',
            'category': 'Access Control',
            'timeline': 'Day 1'
        })
    
    # Check for leased equipment
    hardware = access.get('hardware_ownership', {})
    if hardware.get('firewall', {}).get('owned_by') in ['previous_msp', 'leased']:
        actions.append({
            'action': 'Assess firewall ownership and plan for transition/replacement',
            'priority': 'HIGH',
            'category': 'Infrastructure',
            'timeline': 'Week 1'
        })
    
    # Check shadow IT
    shadow = answers.get('shadow_it', {})
    unsanctioned = shadow.get('unsanctioned_saas', [])
    high_risk = [s for s in unsanctioned if s.get('data_sensitivity') in ['high', 'critical']]
    if high_risk:
        actions.append({
            'action': f"Address {len(high_risk)} high-risk unsanctioned SaaS applications",
            'priority': 'HIGH',
            'category': 'Security',
            'timeline': 'Week 1'
        })
    
    # Check vulnerabilities
    liability = answers.get('liability_baseline', {})
    vulns = liability.get('known_vulnerabilities', [])
    critical_vulns = [v for v in vulns if v.get('severity') == 'critical']
    if critical_vulns:
        actions.append({
            'action': f"Remediate {len(critical_vulns)} critical vulnerabilities",
            'priority': 'CRITICAL',
            'category': 'Security',
            'timeline': 'Week 1'
        })
    
    # Check backup
    critical = answers.get('critical_systems', {})
    backup = critical.get('backup_status', {})
    if not backup.get('restore_test_successful'):
        actions.append({
            'action': 'Verify backup functionality with test restore',
            'priority': 'HIGH',
            'category': 'Backup & Recovery',
            'timeline': 'Week 1'
        })
    
    # Check compliance gaps
    compliance = answers.get('compliance_status', {})
    gaps = compliance.get('compliance_gaps', [])
    if gaps:
        actions.append({
            'action': f"Develop remediation plan for {len(gaps)} compliance gaps",
            'priority': 'MEDIUM',
            'category': 'Compliance',
            'timeline': 'Month 1'
        })
    
    # Check cyber insurance
    insurance = compliance.get('cyber_insurance', {})
    if not insurance.get('current_requirements_met'):
        actions.append({
            'action': 'Address cyber insurance requirement gaps before renewal',
            'priority': 'HIGH',
            'category': 'Compliance',
            'timeline': 'Before renewal date'
        })
    
    # Sort by priority
    priority_order = {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}
    actions.sort(key=lambda x: priority_order.get(x['priority'], 99))
    
    return actions


def generate_risk_report(answers: dict, scores: dict, actions: list) -> str:
    """Generate the risk assessment summary report."""
    metadata = answers.get('metadata', {})
    client_name = metadata.get('client_name', 'Unknown Client')
    engagement_date = metadata.get('engagement_date', datetime.now().strftime('%Y-%m-%d'))
    transition_type = metadata.get('transition_type', 'standard')
    previous_msp = metadata.get('previous_msp', 'Unknown')
    
    report = f"""# Onboarding Risk Assessment Report
## {client_name}

| Field | Value |
|-------|-------|
| **Assessment Date** | {datetime.now().strftime('%Y-%m-%d')} |
| **Engagement Date** | {engagement_date} |
| **Previous Provider** | {previous_msp} |
| **Transition Type** | {transition_type.replace('_', ' ').title()} |

---

## Executive Summary

### Overall Risk Score: {scores['overall']}% ({scores['overall_rating']})

"""
    
    if scores['overall_rating'] == 'RED':
        report += """> ⚠️ **HIGH RISK TRANSITION**
> 
> This engagement has significant risks that require immediate attention. Critical action items must be addressed within the first week to prevent service disruption or security incidents.

"""
    elif scores['overall_rating'] == 'YELLOW':
        report += """> ⚡ **MODERATE RISK TRANSITION**
> 
> This engagement has manageable risks. Follow the action plan closely and monitor for escalation.

"""
    else:
        report += """> ✅ **LOW RISK TRANSITION**
> 
> This engagement appears well-positioned for a smooth transition. Maintain standard onboarding procedures.

"""

    report += """---

## Risk Category Breakdown

| Category | Score (0-10) | Status |
|----------|--------------|--------|
"""
    
    category_names = {
        'access_control': 'Access Control',
        'security_posture': 'Security Posture',
        'compliance': 'Compliance',
        'documentation': 'Documentation',
        'vendor': 'Vendor Relationship',
        'backup': 'Backup & Recovery'
    }
    
    for key, name in category_names.items():
        score = scores.get(key, 0)
        if score >= 7:
            status = "🟢 Good"
        elif score >= 4:
            status = "🟡 Needs Attention"
        else:
            status = "🔴 Critical"
        report += f"| {name} | {score}/10 | {status} |\n"
    
    report += """
---

## Immediate Action Items

"""
    
    # Group actions by priority
    for priority in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
        priority_actions = [a for a in actions if a['priority'] == priority]
        if priority_actions:
            emoji = {'CRITICAL': '🔴', 'HIGH': '🟠', 'MEDIUM': '🟡', 'LOW': '🟢'}[priority]
            report += f"### {emoji} {priority} Priority\n\n"
            for action in priority_actions:
                report += f"- [ ] **{action['action']}** ({action['category']}) - {action['timeline']}\n"
            report += "\n"
    
    report += """---

## Identified Risks

"""
    
    # List known vulnerabilities
    liability = answers.get('liability_baseline', {})
    vulns = liability.get('known_vulnerabilities', [])
    if vulns:
        report += "### Known Vulnerabilities\n\n"
        report += "| Description | Severity | Date Discovered |\n"
        report += "|-------------|----------|----------------|\n"
        for vuln in vulns[:10]:
            report += f"| {vuln.get('description', 'Unknown')[:50]} | {vuln.get('severity', 'Unknown').upper()} | {vuln.get('date_discovered', 'Unknown')} |\n"
        report += "\n"
    
    # List shadow IT
    shadow = answers.get('shadow_it', {})
    unsanctioned = shadow.get('unsanctioned_saas', [])
    if unsanctioned:
        report += "### Shadow IT Discovered\n\n"
        report += "| Service | Category | Data Risk | Action |\n"
        report += "|---------|----------|-----------|--------|\n"
        for svc in unsanctioned[:10]:
            report += f"| {svc.get('service_name', 'Unknown')} | {svc.get('category', 'Unknown')} | {svc.get('data_sensitivity', 'Unknown').upper()} | {svc.get('action_required', 'Review')} |\n"
        report += "\n"
    
    report += """---

## Liability Documentation

This report serves as baseline documentation of the environment state at takeover. Any pre-existing issues identified above are recorded as of the assessment date and were not introduced by the new provider.

| Acknowledgment | |
|----------------|---|
| Client Representative | _________________________ |
| Date | _________________________ |
| vCIO | _________________________ |

---

*Report Generated: """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "*\n"
    
    return report


def generate_stabilization_plan(answers: dict, actions: list) -> str:
    """Generate the 30-60-90 day stabilization plan."""
    metadata = answers.get('metadata', {})
    client_name = metadata.get('client_name', 'Unknown Client')
    
    plan = f"""# 30-60-90 Day Stabilization Plan
## {client_name}

*Generated: {datetime.now().strftime('%Y-%m-%d')}*

---

## Day 30 Objectives: Secure Foundation

### Primary Goals
- Secure all administrative credentials
- Revoke previous provider access
- Deploy monitoring on all systems
- Verify backup functionality
- Document critical security gaps
- Establish regular communication cadence

### Deliverables

| Deliverable | Owner | Status |
|-------------|-------|--------|
| Credential vault populated | | ☐ |
| Previous MSP access audit complete | | ☐ |
| RMM deployed to all endpoints | | ☐ |
| Backup test restore completed | | ☐ |
| Baseline security assessment delivered | | ☐ |
| Initial risk report delivered | | ☐ |
| Emergency contact list established | | ☐ |

### Critical Actions (from assessment)

"""
    
    critical_actions = [a for a in actions if a['priority'] == 'CRITICAL']
    for action in critical_actions:
        plan += f"- [ ] {action['action']}\n"
    
    if not critical_actions:
        plan += "- [ ] [No critical actions identified]\n"
    
    plan += """
---

## Day 60 Objectives: Stabilization

### Primary Goals
- Remediate security vulnerabilities
- Complete documentation creation
- Transfer all vendor relationships
- Establish service level baseline
- Address recurring issues

### Deliverables

| Deliverable | Owner | Status |
|-------------|-------|--------|
| Vulnerability remediation in progress | | ☐ |
| Network documentation complete | | ☐ |
| Vendor contact list finalized | | ☐ |
| SOP documentation started | | ☐ |
| Recurring issue patterns identified | | ☐ |
| Staff introduction meetings complete | | ☐ |

### High Priority Actions

"""
    
    high_actions = [a for a in actions if a['priority'] == 'HIGH']
    for action in high_actions[:5]:
        plan += f"- [ ] {action['action']}\n"
    
    plan += """
---

## Day 90 Objectives: Optimization

### Primary Goals
- Present strategic roadmap
- Deliver proactive recommendations
- Implement process improvements
- Validate client satisfaction
- Transition to steady-state management

### Deliverables

| Deliverable | Owner | Status |
|-------------|-------|--------|
| Strategic roadmap presentation | | ☐ |
| QBR schedule established | | ☐ |
| Budget recommendations delivered | | ☐ |
| Client satisfaction survey completed | | ☐ |
| Steady-state procedures documented | | ☐ |
| First QBR scheduled | | ☐ |

---

## Success Metrics

| Metric | Day 30 Target | Day 60 Target | Day 90 Target |
|--------|---------------|---------------|---------------|
| Tickets resolved in SLA | 80% | 90% | 95% |
| Critical vulnerabilities | Identified | 50% remediated | 100% remediated |
| Documentation completeness | 25% | 60% | 90% |
| Client satisfaction | Baseline | Improving | >8/10 |

---

## Weekly Check-in Agenda

1. Open ticket review
2. Security/compliance updates
3. Project status
4. Upcoming deadlines
5. Resource needs
6. Client concerns

---

*Plan Version: 1.0*
"""
    
    return plan


def generate_credential_checklist(answers: dict) -> str:
    """Generate the credential handover checklist."""
    metadata = answers.get('metadata', {})
    client_name = metadata.get('client_name', 'Unknown Client')
    
    checklist = f"""# Credential & Access Handover Checklist
## {client_name}

*Generated: {datetime.now().strftime('%Y-%m-%d')}*

---

## Cloud Platform Access

| Platform | Admin Account | Status | Verified Date |
|----------|---------------|--------|---------------|
"""
    
    access = answers.get('access_sovereignty', {})
    admin_accounts = access.get('global_admin_accounts', [])
    
    for acc in admin_accounts:
        platform = acc.get('platform', 'Unknown')
        account = acc.get('account_email', 'Unknown')
        verified = "✅" if acc.get('verified') else "☐ Pending"
        checklist += f"| {platform} | {account} | {verified} | |\n"
    
    if not admin_accounts:
        checklist += "| Microsoft 365 | [TBD] | ☐ Pending | |\n"
        checklist += "| Azure/AWS/GCP | [TBD] | ☐ Pending | |\n"
    
    checklist += """
---

## Domain & DNS

| Asset | Provider | Access Status | Verified Date |
|-------|----------|---------------|---------------|
"""
    
    dns = access.get('domain_dns_control', {})
    registrar = dns.get('registrar', 'Unknown')
    reg_status = "✅" if dns.get('registrar_login_verified') else "☐ Pending"
    dns_provider = dns.get('dns_provider', 'Unknown')
    dns_status = "✅" if dns.get('dns_login_verified') else "☐ Pending"
    
    checklist += f"| Domain Registrar | {registrar} | {reg_status} | |\n"
    checklist += f"| DNS Hosting | {dns_provider} | {dns_status} | |\n"
    
    checklist += """
---

## Network Equipment

| Device | Type | Admin Access | Password Changed |
|--------|------|--------------|------------------|
"""
    
    hardware = access.get('hardware_ownership', {})
    firewall = hardware.get('firewall', {})
    if firewall:
        checklist += f"| Firewall | {firewall.get('make_model', 'Unknown')} | ☐ Pending | ☐ |\n"
    
    checklist += """
---

## Vendor Portals

| Vendor | Portal URL | Access Status |
|--------|------------|---------------|
"""
    
    vendor_portals = access.get('vendor_portals', [])
    for portal in vendor_portals:
        status = "✅" if portal.get('access_verified') else "☐ Pending"
        checklist += f"| {portal.get('vendor_name', 'Unknown')} | {portal.get('portal_url', 'Unknown')} | {status} |\n"
    
    if not vendor_portals:
        checklist += "| [Vendor 1] | [URL] | ☐ Pending |\n"
    
    checklist += """
---

## Previous Provider Handover Items

| Item | Received | Notes |
|------|----------|-------|
| Network documentation | ☐ | |
| Password vault export | ☐ | |
| Backup configurations | ☐ | |
| License keys | ☐ | |
| SSL certificates | ☐ | |
| RMM agent removal | ☐ | |

---

## Verification Sign-off

| Milestone | Date | Verified By |
|-----------|------|-------------|
| All critical credentials secured | | |
| Previous MSP access revoked | | |
| Our monitoring deployed | | |
| Credential vault complete | | |

---

*Checklist Version: 1.0*
"""
    
    return checklist


def main():
    parser = argparse.ArgumentParser(
        description='Process onboarding questionnaire answers into reports'
    )
    parser.add_argument(
        '--input', '-i',
        type=Path,
        help='Path to YAML file with questionnaire answers'
    )
    parser.add_argument(
        '--output-dir', '-o',
        type=Path,
        default=Path('./reports'),
        help='Output directory for generated reports'
    )
    parser.add_argument(
        '--validate-schema',
        type=Path,
        help='Validate a YAML schema file'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be generated without writing files'
    )
    
    args = parser.parse_args()
    
    # Schema validation mode
    if args.validate_schema:
        print(f"Validating schema: {args.validate_schema}")
        try:
            schema = load_yaml(args.validate_schema)
            print("✓ YAML syntax valid")
            
            required_sections = ['metadata', 'access_sovereignty', 'liability_baseline', 'critical_systems']
            for section in required_sections:
                if section in schema:
                    print(f"✓ Section '{section}' present")
                else:
                    print(f"✗ Section '{section}' missing")
            
            print("\nSchema validation complete.")
            return 0
        except Exception as e:
            print(f"✗ Validation failed: {e}")
            return 1
    
    # Regular processing mode
    if not args.input:
        parser.error("--input is required for report generation")
    
    if not args.input.exists():
        print(f"Error: Input file not found: {args.input}")
        return 1
    
    print(f"Loading answers from: {args.input}")
    answers = load_yaml(args.input)
    
    # Validate
    errors = validate_answers(answers)
    if errors:
        print("Validation errors:")
        for error in errors:
            print(f"  - {error}")
        return 1
    
    print("✓ Answers validated")
    
    # Calculate risk scores
    print("Calculating risk scores...")
    scores = calculate_risk_score(answers)
    print(f"  Overall Score: {scores['overall']}% ({scores['overall_rating']})")
    
    # Extract action items
    print("Extracting action items...")
    actions = extract_immediate_actions(answers)
    print(f"  Found {len(actions)} action items")
    
    # Generate reports
    risk_report = generate_risk_report(answers, scores, actions)
    stab_plan = generate_stabilization_plan(answers, actions)
    cred_checklist = generate_credential_checklist(answers)
    
    if args.dry_run:
        print("\n=== Risk Assessment Report ===")
        print(risk_report[:2000] + "...[truncated]")
        return 0
    
    # Ensure output directory exists
    args.output_dir.mkdir(parents=True, exist_ok=True)
    
    client_name = answers.get('metadata', {}).get('client_name', 'client')
    client_slug = client_name.lower().replace(' ', '_')[:20]
    
    # Write reports
    risk_path = args.output_dir / f'{client_slug}_risk_assessment.md'
    with open(risk_path, 'w', encoding='utf-8') as f:
        f.write(risk_report)
    print(f"✓ Generated: {risk_path}")
    
    stab_path = args.output_dir / f'{client_slug}_stabilization_plan.md'
    with open(stab_path, 'w', encoding='utf-8') as f:
        f.write(stab_plan)
    print(f"✓ Generated: {stab_path}")
    
    cred_path = args.output_dir / f'{client_slug}_credential_checklist.md'
    with open(cred_path, 'w', encoding='utf-8') as f:
        f.write(cred_checklist)
    print(f"✓ Generated: {cred_path}")
    
    print(f"\n✓ Processing complete!")
    print(f"  Risk Assessment: {risk_path}")
    print(f"  Stabilization Plan: {stab_path}")
    print(f"  Credential Checklist: {cred_path}")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
