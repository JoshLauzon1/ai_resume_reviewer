import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import spacy
from parser import extract_sections
from matcher import analyze_resume
from job_specific_scorer import JobSpecificScorer


def test_module_imports_and_spacy_model_loads():
    """Ensure key modules and spaCy model load without errors."""
    nlp = spacy.load("en_core_web_sm")
    assert nlp.meta["name"].endswith("core_web_sm")
    assert callable(extract_sections)
    assert callable(analyze_resume)
    assert JobSpecificScorer() is not None


def test_extract_sections_basic():
    """Check that extract_sections parses simple resume text."""
    text = "Experience\nSoftware Engineer\nPython, Java"
    sections = extract_sections(text)
    assert "experience" in sections
    assert "Software Engineer" in sections["experience"]
