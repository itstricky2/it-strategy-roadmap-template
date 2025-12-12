"""
Shared utilities for questionnaire processing.
"""

import re
from datetime import datetime
from pathlib import Path


def sanitize_filename(text: str) -> str:
    """Convert text to a valid filename."""
    sanitized = re.sub(r'[^a-zA-Z0-9\-_]', '_', text.lower())
    sanitized = re.sub(r'_+', '_', sanitized)
    return sanitized.strip('_')[:50]


def sanitize_mermaid_id(text: str) -> str:
    """Convert text to a valid Mermaid node ID."""
    sanitized = re.sub(r'[^a-zA-Z0-9]', '_', text.lower())
    sanitized = re.sub(r'_+', '_', sanitized)
    sanitized = sanitized.strip('_')
    if sanitized and not sanitized[0].isalpha():
        sanitized = 'id_' + sanitized
    return sanitized[:30]


def format_currency(amount: float | int | None) -> str:
    """Format a number as currency."""
    if amount is None:
        return "TBD"
    return f"${amount:,.0f}"


def format_date(date_str: str | None, format_out: str = '%B %d, %Y') -> str:
    """Format a date string."""
    if not date_str:
        return "TBD"
    try:
        dt = datetime.fromisoformat(date_str)
        return dt.strftime(format_out)
    except ValueError:
        return date_str


def priority_to_color(priority: str) -> str:
    """Convert priority to color indicator."""
    priority_colors = {
        'critical': '🔴',
        'high': '🟠',
        'medium': '🟡',
        'low': '🟢'
    }
    return priority_colors.get(priority.lower(), '⚪')


def score_to_status(score: int, max_score: int = 10) -> str:
    """Convert a numeric score to status indicator."""
    percentage = (score / max_score) * 100
    if percentage >= 70:
        return "🟢 Good"
    elif percentage >= 40:
        return "🟡 Needs Attention"
    else:
        return "🔴 Critical"


def ensure_directory(path: Path) -> Path:
    """Ensure a directory exists, creating if necessary."""
    path.mkdir(parents=True, exist_ok=True)
    return path
