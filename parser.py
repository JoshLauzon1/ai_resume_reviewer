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
    text_lines = text.split('\n')
    current_section = None
    section_content = []
    
    # Enhanced section patterns
    section_patterns = {
        'contact information': r'^\s*(contact|contact information|personal information)\s*$',
        'summary': r'^\s*(summary|professional summary|executive summary|profile)\s*$',
        'objective': r'^\s*(objective|career objective|professional objective)\s*$',
        'experience': r'^\s*(experience|work experience|professional experience|employment|employment history)\s*$',
        'education': r'^\s*(education|academic background|qualifications|academic qualifications)\s*$',
        'skills': r'^\s*(skills|technical skills|core competencies|technologies|technical competencies)\s*$',
        'projects': r'^\s*(projects|personal projects|side projects|portfolio|notable projects)\s*$',
        'certifications': r'^\s*(certifications|certificates|professional certifications)\s*$'
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
                sections[current_section] = '\n'.join(section_content).strip()
            
            # Start new section
            current_section = section_found
            section_content = []
        elif current_section:
            # Add content to current section
            section_content.append(line)
    
    # Save the last section
    if current_section and section_content:
        sections[current_section] = '\n'.join(section_content).strip()
    
    # Also check for implicit sections (for backward compatibility)
    text_cleaned = clean_text(text)
    for section in RESUME_SECTIONS:
        if section not in sections:
            match = re.search(r'\b' + section + r'\b', text_cleaned, re.IGNORECASE)
            if match:
                sections[section] = True # Mark section as present

    return sections
