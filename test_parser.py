from parser import extract_sections


def test_extract_sections_uses_canonical_names():
    text = (
        "Work Experience\nDid stuff here\n\n"
        "Technical Skills\nPython, Java\n"
    )
    sections = extract_sections(text)
    assert "experience" in sections
    assert "skills" in sections
    assert "work experience" not in sections
    assert "technical skills" not in sections

