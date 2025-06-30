import re

RESUME_SECTIONS = [
    'contact information', 'summary', 'objective', 'experience',
    'work experience', 'professional experience', 'education', 'skills',
    'technical skills', 'certifications', 'projects'
]

def clean_text(text):
    """Removes extra whitespace and lowercases text."""
    return re.sub(r'\s+', ' ', text).strip().lower()