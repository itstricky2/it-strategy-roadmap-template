# Form Conversion Guide

This guide provides instructions for converting the markdown questionnaires into fillable digital forms for client self-service.

---

## Option 1: Microsoft Forms (Recommended for M365 Clients)

Microsoft Forms integrates seamlessly with Microsoft 365 and provides branching logic for conditional sections.

### Step-by-Step Conversion

1. **Access Microsoft Forms**: Go to [forms.microsoft.com](https://forms.microsoft.com)

2. **Create New Form**: Click "+ New Form"

3. **Structure Sections**:
   - Use "Section" elements to replicate the questionnaire sections
   - Add section titles matching the markdown headers

4. **Question Types Mapping**:

   | Markdown Format | Microsoft Forms Type |
   |-----------------|----------------------|
   | Text response `[Your response]` | "Text" (Long answer) |
   | Checkbox `- [ ] Option` | "Choice" (Multiple answers) |
   | Radio button lists | "Choice" (Single answer) |
   | Tables | "Ranking" or multiple "Choice" questions |
   | Yes/No | "Choice" with two options |

5. **Branching Logic**:
   - Click the "..." menu on a question
   - Select "Add branching"
   - Route to different sections based on responses
   - Example: If "CJIS applicable = Yes", branch to CJIS-specific questions

6. **Settings**:
   - Enable "Responses can be anonymous" for external clients
   - Consider requiring sign-in for enterprise accounts
   - Set notification for form completion

7. **Templates**: Save as template for reuse with different clients

### Exporting Responses

- Click "Responses" tab → "Open in Excel"
- Exports to Excel for use with automation scripts
- Can be converted to YAML using provided converter (see below)

---

## Option 2: Google Forms

Google Forms is free and accessible to all clients without Microsoft 365.

### Step-by-Step Conversion

1. **Access Google Forms**: Go to [forms.google.com](https://forms.google.com)

2. **Create Structure**:
   - Use "Add section" to create page breaks by questionnaire section
   - Name sections to match questionnaire headers

3. **Question Types**:

   | Markdown Format | Google Forms Type |
   |-----------------|-------------------|
   | Text response | "Short answer" or "Paragraph" |
   | Checkbox lists | "Checkboxes" |
   | Radio options | "Multiple choice" |
   | Tables | "Multiple choice grid" or "Checkbox grid" |
   | Dropdown | "Dropdown" |

4. **Conditional Logic**:
   - Select "Go to section based on answer"
   - Available on "Multiple choice" and "Dropdown" types
   - Use to skip irrelevant sections (e.g., skip government-specific if enterprise)

5. **Settings** (gear icon):
   - Collect email addresses (optional)
   - Limit to one response (optional)
   - Show progress bar (recommended)

### Exporting Responses

- Click "Responses" → three-dot menu → "Download responses (.csv)"
- Use provided converter to transform to YAML

---

## Option 3: Adobe Acrobat Fillable PDF

Best for formal document presentation and controlled distribution.

### Creating Fillable PDFs

1. **Convert Markdown to PDF**:
   ```bash
   # Using pandoc
   pandoc questionnaire.md -o questionnaire.pdf --pdf-engine=wkhtmltopdf
   ```

2. **Open in Adobe Acrobat Pro**:
   - Tools → Prepare Form
   - Acrobat auto-detects form fields

3. **Field Types**:
   - Text fields for open responses
   - Checkboxes for checkbox items
   - Radio buttons for single-choice
   - Dropdown for long option lists

4. **Form Properties**:
   - Set tab order for accessibility
   - Add calculation fields if needed
   - Enable digital signature field for sign-off

5. **Distribution**:
   - Save as "Reader Extended PDF" for clients without Acrobat Pro
   - Distribute via email or secure portal

### Collecting Responses

- Use "Distribute Form" in Acrobat
- Aggregate responses in Acrobat's tracker
- Export to spreadsheet format

---

## Option 4: Premium Form Builders

For advanced features like payment integration, complex logic, or branded experiences.

### Typeform

**Best for**: Beautiful, conversational forms that increase completion rates

- Pricing: Starts at $25/month
- Features: Conditional logic, file uploads, calculations
- Integration: Webhooks, Zapier, direct API

### Jotform

**Best for**: Complex forms with many question types

- Pricing: Free tier available, paid from $34/month
- Features: 100+ widgets, e-signature, payment forms
- Healthcare: HIPAA-compliant plans available

### Formstack

**Best for**: Enterprise compliance requirements

- Pricing: Starts at $50/month
- Features: HIPAA compliance, advanced security
- Integration: Salesforce, HubSpot, direct API

---

## YAML Conversion Script

After collecting form responses, convert to YAML for automation processing:

```python
#!/usr/bin/env python3
"""
Convert form export (CSV/Excel) to YAML for roadmap/onboarding processors.

Usage:
    python form_to_yaml.py --input responses.csv --output answers.yaml --type roadmap
"""

import argparse
import csv
import yaml
from pathlib import Path


def csv_to_roadmap_yaml(csv_path: Path, output_path: Path):
    """Convert Microsoft Forms/Google Forms CSV to roadmap YAML."""
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    if not rows:
        raise ValueError("No data in CSV")
    
    # Take first row (most recent response)
    data = rows[0]
    
    # Map CSV columns to YAML structure
    # Customize this mapping based on your form's column names
    yaml_data = {
        'metadata': {
            'client_name': data.get('Client Name', ''),
            'client_type': data.get('Client Type', 'enterprise'),
            'engagement_date': data.get('Date', ''),
            'vcio_name': '',
            'version': '1.0'
        },
        'organization': {
            'primary_mission': data.get('Primary Mission', ''),
            # ... map other fields
        },
        # ... continue mapping
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True)
    
    print(f"Converted {csv_path} to {output_path}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--type', choices=['roadmap', 'onboarding'], required=True)
    args = parser.parse_args()
    
    if args.type == 'roadmap':
        csv_to_roadmap_yaml(args.input, args.output)
    else:
        # Implement onboarding conversion
        pass
```

---

## Recommended Workflow

1. **Client Self-Service** (Optional):
   - Send Microsoft Forms or Google Forms link
   - Client completes independently
   - Export responses

2. **vCIO Interview**:
   - Use internal questionnaire version (markdown)
   - Fill in responses during meeting
   - Capture context and clarifications

3. **Data Entry**:
   - Transcribe to YAML answer template
   - Or use form export + converter

4. **Automation**:
   - Run `roadmap_generator.py` or `onboarding_processor.py`
   - Review generated outputs
   - Customize before client presentation

---

## Security Considerations

- **PII Handling**: Forms may contain sensitive data
- **Access Control**: Restrict form response access to authorized personnel
- **Data Retention**: Establish retention policy for completed forms
- **Encryption**: Use HTTPS and encrypted storage for responses
- **Compliance**: Ensure form platform meets client compliance requirements (HIPAA, etc.)

---

*Document Version: 1.0 | Last Updated: December 2024*
