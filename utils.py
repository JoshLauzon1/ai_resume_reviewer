import re

# Mapping of canonical resume section names to their common synonyms. Each
# canonical key should appear only once in the parsed output regardless of
# which synonym is used in the resume.
RESUME_SECTIONS = {
    "contact information": ["contact", "contact information", "personal information"],
    "summary": ["summary", "professional summary", "executive summary", "profile"],
    "objective": ["objective", "career objective", "professional objective"],
    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment",
        "employment history",
    ],
    "education": [
        "education",
        "academic background",
        "qualifications",
        "academic qualifications",
    ],
    "skills": [
        "skills",
        "technical skills",
        "core competencies",
        "technologies",
        "technical competencies",
    ],
    "projects": [
        "projects",
        "personal projects",
        "side projects",
        "portfolio",
        "notable projects",
    ],
    "certifications": ["certifications", "certificates", "professional certifications"],
}


def clean_text(text):
    """Removes extra whitespace and lowercases text."""
    return re.sub(r"\s+", " ", text).strip().lower()

