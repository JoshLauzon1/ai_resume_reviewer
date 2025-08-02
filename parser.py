import re
from pdfminer.high_level import extract_text
from utils import RESUME_SECTIONS, clean_text


def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a PDF file-like object.

    Args:
        pdf_file: A file-like object representing the PDF.

    Returns:
        The extracted text as a string.
    """
    return extract_text(pdf_file)


def extract_sections(text):
    """
    Extracts sections from resume text based on predefined section headers.

    Args:
        text: The resume text.

    Returns:
        A dictionary with section headers as keys and section content as values.
    """
    sections = {}
    text_lines = text.split("\n")
    current_section = None
    section_content = []

    # Build regex patterns from the RESUME_SECTIONS mapping.
    section_patterns = {
        canonical: r"^\s*(?:" + "|".join(re.escape(s) for s in synonyms) + r")\s*$"
        for canonical, synonyms in RESUME_SECTIONS.items()
    }

    for line in text_lines:
        line_stripped = line.strip()
        if not line_stripped:
            continue

        # Check if this line is a section header
        section_found = None
        for section_name, pattern in section_patterns.items():
            if re.match(pattern, line_stripped, re.IGNORECASE):
                section_found = section_name
                break

        if section_found:
            # Save previous section if it exists
            if current_section and section_content:
                sections[current_section] = "\n".join(section_content).strip()

            # Start new section
            current_section = section_found
            section_content = []
        elif current_section:
            # Add content to current section
            section_content.append(line)

    # Save the last section
    if current_section and section_content:
        sections[current_section] = "\n".join(section_content).strip()

    # Also check for implicit sections using synonyms
    for canonical, synonyms in RESUME_SECTIONS.items():
        if canonical not in sections:
            for synonym in synonyms:
                if re.search(r"\b" + re.escape(synonym) + r"\b", text, re.IGNORECASE):
                    sections[canonical] = True  # Mark section as present
                    break

    return sections

