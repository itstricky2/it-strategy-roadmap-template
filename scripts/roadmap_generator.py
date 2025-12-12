#!/usr/bin/env python3
"""
IT Strategic Roadmap Generator

Transforms YAML questionnaire answers into:
- Mermaid Gantt strategic roadmap (strategic_roadmap.mmd)
- Mermaid Gantt tactical roadmap (tactical_roadmap.mmd)
- Initiative markdown files

Usage:
    python roadmap_generator.py --input answers.yaml --output-dir ./roadmap/
    python roadmap_generator.py --validate-schema ./schemas/roadmap_answers.yaml
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional
import yaml
import re


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
    if not answers.get('metadata', {}).get('client_type'):
        errors.append("Missing metadata.client_type")
    
    # Check horizons
    horizons = answers.get('horizons', {})
    if not horizons.get('horizon_1_stabilization'):
        errors.append("Missing horizons.horizon_1_stabilization")
    
    # Check for at least some initiatives
    initiatives = answers.get('initiatives', {}).get('identified_initiatives', [])
    if not initiatives:
        errors.append("No initiatives identified - cannot generate roadmap")
    
    return errors


def sanitize_id(text: str) -> str:
    """Convert text to a valid Mermaid ID (alphanumeric + underscore)."""
    # Replace spaces and special chars with underscores
    sanitized = re.sub(r'[^a-zA-Z0-9]', '_', text.lower())
    # Remove consecutive underscores
    sanitized = re.sub(r'_+', '_', sanitized)
    # Remove leading/trailing underscores
    sanitized = sanitized.strip('_')
    # Ensure it starts with a letter
    if sanitized and not sanitized[0].isalpha():
        sanitized = 'init_' + sanitized
    return sanitized[:30]  # Limit length


def get_fiscal_year_start(answers: dict) -> datetime:
    """Determine the fiscal year start based on client type and answers."""
    org = answers.get('organization', {})
    fiscal_month = org.get('fiscal_year_start_month')
    
    if fiscal_month:
        # Use specified fiscal year
        current_year = datetime.now().year
        return datetime(current_year, fiscal_month, 1)
    else:
        # Default to calendar year
        return datetime(datetime.now().year, 1, 1)


def assign_horizon_dates(horizon: int, fiscal_start: datetime) -> tuple[datetime, datetime]:
    """
    Assign start and end dates based on horizon.
    
    Horizon 1: 0-18 months
    Horizon 2: 18-36 months (years 2-3)
    Horizon 3: 36-60 months (years 3-5)
    """
    if horizon == 1:
        start = fiscal_start
        end = fiscal_start + timedelta(days=540)  # 18 months
    elif horizon == 2:
        start = fiscal_start + timedelta(days=540)  # 18 months
        end = fiscal_start + timedelta(days=1095)  # 3 years
    else:  # Horizon 3
        start = fiscal_start + timedelta(days=1095)  # 3 years
        end = fiscal_start + timedelta(days=1825)  # 5 years
    
    return start, end


def categorize_initiatives(answers: dict) -> dict:
    """Organize initiatives into categories for the Gantt chart."""
    categories = {
        'infrastructure': [],
        'security': [],
        'applications': [],
        'data': [],
        'workforce': [],
        'other': []
    }
    
    initiatives = answers.get('initiatives', {}).get('identified_initiatives', [])
    
    # Also pull from horizon sections
    h1 = answers.get('horizons', {}).get('horizon_1_stabilization', {})
    h2 = answers.get('horizons', {}).get('horizon_2_scale', {})
    h3 = answers.get('horizons', {}).get('horizon_3_innovation', {})
    
    # Process explicit initiatives
    for init in initiatives:
        if not init.get('name'):
            continue
            
        name = init['name']
        horizon = init.get('horizon', 1)
        priority = init.get('priority', 'medium')
        
        # Categorize based on name keywords
        name_lower = name.lower()
        if any(kw in name_lower for kw in ['server', 'network', 'cloud', 'infrastructure', 'migration']):
            category = 'infrastructure'
        elif any(kw in name_lower for kw in ['security', 'mfa', 'backup', 'compliance', 'audit']):
            category = 'security'
        elif any(kw in name_lower for kw in ['application', 'erp', 'crm', 'software']):
            category = 'applications'
        elif any(kw in name_lower for kw in ['data', 'analytics', 'reporting', 'ai']):
            category = 'data'
        elif any(kw in name_lower for kw in ['training', 'user', 'workforce', 'hiring']):
            category = 'workforce'
        else:
            category = 'other'
        
        categories[category].append({
            'name': name,
            'horizon': horizon,
            'priority': priority,
            'category': category,
            'details': init
        })
    
    # Process horizon-specific items as backup
    for item in h1.get('technical_debt_items', []):
        if item.get('item') and not any(i['name'] == item['item'] for cat in categories.values() for i in cat):
            categories['infrastructure'].append({
                'name': item['item'],
                'horizon': 1,
                'priority': item.get('urgency', 'high'),
                'category': 'infrastructure',
                'details': item
            })
    
    for item in h1.get('security_gaps', []):
        if item and not any(i['name'] == item for cat in categories.values() for i in cat):
            categories['security'].append({
                'name': item,
                'horizon': 1,
                'priority': 'high',
                'category': 'security',
                'details': {}
            })
    
    return categories


def generate_strategic_roadmap(answers: dict, fiscal_start: datetime) -> str:
    """Generate the strategic (5-year) Mermaid Gantt chart."""
    client_name = answers.get('metadata', {}).get('client_name', 'Client')
    start_year = fiscal_start.year
    
    lines = [
        "gantt",
        "    dateFormat YYYY",
        f"    title {client_name} IT Strategy 5-Year Roadmap",
        "    axisFormat %Y",
        ""
    ]
    
    categories = categorize_initiatives(answers)
    
    # Horizon 1 section
    lines.append("    section Horizon 1: Stabilization")
    h1_items = [i for cat in categories.values() for i in cat if i['horizon'] == 1]
    for idx, item in enumerate(h1_items[:4]):  # Limit to top 4 per horizon
        item_id = f"h1_{idx}"
        crit = ",crit" if item['priority'] == 'critical' else ""
        lines.append(f"    {item['name'][:40]}    :{crit}{item_id}, {start_year}, 1y")
    
    if not h1_items:
        lines.append(f"    Foundation Phase    :h1_1, {start_year}, 1y")
    
    lines.append("")
    
    # Horizon 2 section
    lines.append("    section Horizon 2: Scale")
    h2_items = [i for cat in categories.values() for i in cat if i['horizon'] == 2]
    for idx, item in enumerate(h2_items[:4]):
        item_id = f"h2_{idx}"
        lines.append(f"    {item['name'][:40]}    :{item_id}, {start_year + 1}, 2y")
    
    if not h2_items:
        lines.append(f"    Scaling Phase    :h2_1, {start_year + 1}, 2y")
    
    lines.append("")
    
    # Horizon 3 section
    lines.append("    section Horizon 3: Innovation")
    h3_items = [i for cat in categories.values() for i in cat if i['horizon'] == 3]
    for idx, item in enumerate(h3_items[:4]):
        item_id = f"h3_{idx}"
        lines.append(f"    {item['name'][:40]}    :{item_id}, {start_year + 3}, 2y")
    
    if not h3_items:
        lines.append(f"    Innovation Phase    :h3_1, {start_year + 3}, 2y")
    
    lines.append("")
    
    return "\n".join(lines)


def generate_tactical_roadmap(answers: dict, fiscal_start: datetime) -> str:
    """Generate the tactical (18-month) Mermaid Gantt chart."""
    client_name = answers.get('metadata', {}).get('client_name', 'Client')
    start_date = fiscal_start.strftime('%Y-%m-%d')
    
    lines = [
        "gantt",
        "    dateFormat  YYYY-MM-DD",
        f"    title       {client_name} - Horizon 1: Operational Excellence (18 Months)",
        "    excludes    weekends",
        ""
    ]
    
    categories = categorize_initiatives(answers)
    
    # Group by category
    category_names = {
        'infrastructure': 'Infrastructure',
        'security': 'Security',
        'applications': 'Applications',
        'data': 'Data & Analytics',
        'workforce': 'Workforce',
        'other': 'Other Initiatives'
    }
    
    prev_item_id = None
    
    for cat_key, cat_name in category_names.items():
        items = [i for i in categories.get(cat_key, []) if i['horizon'] == 1]
        
        if not items:
            continue
        
        lines.append(f"    section {cat_name}")
        
        for idx, item in enumerate(items):
            item_id = sanitize_id(f"{cat_key}_{idx}_{item['name'][:10]}")
            
            # Determine status and timing
            if item['priority'] == 'critical':
                status = "crit,"
            elif item['priority'] == 'high':
                status = "active,"
            else:
                status = ""
            
            # Estimate duration based on complexity (default 60 days)
            duration = "60d"
            
            # Chain dependencies or use start date
            if prev_item_id and idx > 0:
                timing = f"after {prev_item_id}, {duration}"
            else:
                # Stagger start dates
                offset_days = idx * 30
                item_start = fiscal_start + timedelta(days=offset_days)
                timing = f"{item_start.strftime('%Y-%m-%d')}, {duration}"
            
            lines.append(f"    {item['name'][:40]}    :{status}{item_id}, {timing}")
            prev_item_id = item_id
        
        lines.append("")
    
    return "\n".join(lines)


def generate_initiative_file(initiative: dict, output_dir: Path, idx: int) -> Path:
    """Generate a markdown file for an individual initiative."""
    name = initiative.get('name', f'Initiative {idx}')
    details = initiative.get('details', {})
    
    # Generate filename
    filename = f"{idx:03d}-{sanitize_id(name)}.md"
    filepath = output_dir / filename
    
    horizon_map = {1: 'Stabilization', 2: 'Scale', 3: 'Innovation'}
    horizon = initiative.get('horizon', 1)
    
    content = f"""# Initiative: {name}

| Attribute | Details |
| :--- | :--- |
| **Status** | Draft |
| **Horizon** | {horizon} ({horizon_map.get(horizon, 'Unknown')}) |
| **Priority** | {initiative.get('priority', 'Medium').title()} |
| **Owner** | [To be assigned] |
| **Sponsor** | {details.get('sponsor', '[To be identified]')} |

## 1. Executive Summary

{name} is a Horizon {horizon} initiative focused on [describe objective].

## 2. Business Case

### Problem Statement
[What happens if we don't do this?]

### Strategic Alignment
*   **Business Goal**: {details.get('business_goal_alignment', '[Map to business goal]')}
*   **IT Strategy Pillar**: [e.g., Operational Excellence, Security, Innovation]

## 3. ROI & Financial Impact

| Metric | Value |
| :--- | :--- |
| **Estimated Cost** | ${details.get('estimated_cost', '[TBD]')} |
| **Projected Savings/Revenue** | ${details.get('estimated_savings', '[TBD]')} |
| **Payback Period** | [Calculate] |

## 4. Risk Profile

| Risk | Probability | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
"""
    
    # Add risks if available
    risks = details.get('risks', [])
    if risks:
        for risk in risks[:3]:
            content += f"| {risk} | Medium | Medium | [Define mitigation] |\n"
    else:
        content += "| [Identify risks] | Low/Med/High | Low/Med/High | [Define mitigation] |\n"
    
    content += """
## 5. Dependencies

"""
    
    deps = details.get('dependencies', [])
    if deps:
        for dep in deps:
            content += f"- {dep}\n"
    else:
        content += "- [List dependencies]\n"
    
    content += """
## 6. Timeline

See [Tactical Roadmap](../roadmap/tactical_roadmap.mmd) for live tracking.

*   **Planning Phase**: [Date]
*   **Implementation Phase**: [Date]
*   **Validation Phase**: [Date]
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filepath


def main():
    parser = argparse.ArgumentParser(
        description='Generate IT Strategic Roadmap from questionnaire answers'
    )
    parser.add_argument(
        '--input', '-i',
        type=Path,
        help='Path to YAML file with questionnaire answers'
    )
    parser.add_argument(
        '--output-dir', '-o',
        type=Path,
        default=Path('./roadmap'),
        help='Output directory for generated files'
    )
    parser.add_argument(
        '--initiatives-dir',
        type=Path,
        default=Path('./initiatives'),
        help='Output directory for initiative files'
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
            
            # Check for required sections
            required_sections = ['metadata', 'organization', 'horizons', 'initiatives']
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
    
    # Regular generation mode
    if not args.input:
        parser.error("--input is required for roadmap generation")
    
    if not args.input.exists():
        print(f"Error: Input file not found: {args.input}")
        return 1
    
    # Load answers
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
    
    # Determine fiscal year
    fiscal_start = get_fiscal_year_start(answers)
    print(f"Using fiscal year start: {fiscal_start.strftime('%B %Y')}")
    
    # Generate strategic roadmap
    strategic_mmd = generate_strategic_roadmap(answers, fiscal_start)
    
    # Generate tactical roadmap
    tactical_mmd = generate_tactical_roadmap(answers, fiscal_start)
    
    if args.dry_run:
        print("\n=== Strategic Roadmap ===")
        print(strategic_mmd)
        print("\n=== Tactical Roadmap ===")
        print(tactical_mmd)
        return 0
    
    # Ensure output directories exist
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.initiatives_dir.mkdir(parents=True, exist_ok=True)
    
    # Write roadmap files
    strategic_path = args.output_dir / 'strategic_roadmap.mmd'
    with open(strategic_path, 'w', encoding='utf-8') as f:
        f.write(strategic_mmd)
    print(f"✓ Generated: {strategic_path}")
    
    tactical_path = args.output_dir / 'tactical_roadmap.mmd'
    with open(tactical_path, 'w', encoding='utf-8') as f:
        f.write(tactical_mmd)
    print(f"✓ Generated: {tactical_path}")
    
    # Generate initiative files
    categories = categorize_initiatives(answers)
    all_initiatives = [i for cat in categories.values() for i in cat]
    
    print(f"\nGenerating {len(all_initiatives)} initiative files...")
    for idx, init in enumerate(all_initiatives, start=1):
        filepath = generate_initiative_file(init, args.initiatives_dir, idx)
        print(f"  ✓ {filepath.name}")
    
    print(f"\n✓ Generation complete!")
    print(f"  Strategic Roadmap: {strategic_path}")
    print(f"  Tactical Roadmap: {tactical_path}")
    print(f"  Initiatives: {len(all_initiatives)} files in {args.initiatives_dir}")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
