import re
from functools import lru_cache
import spacy

RESUME_SECTIONS = [
    'contact information', 'summary', 'objective', 'experience',
    'work experience', 'professional experience', 'education', 'skills',
    'technical skills', 'certifications', 'projects'
]

def clean_text(text):
    """Removes extra whitespace and lowercases text."""
    return re.sub(r'\s+', ' ', text).strip().lower()


@lru_cache(maxsize=1)
def get_nlp():
    """Load and cache the spaCy English model."""
    return spacy.load("en_core_web_sm")
