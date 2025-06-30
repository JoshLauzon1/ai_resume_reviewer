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
    text_cleaned = clean_text(text)
    
    for section in RESUME_SECTIONS:
        match = re.search(r'\b' + section + r'\b', text, re.IGNORECASE)
        if match:
            sections[section] = True # Mark section as present
    return sections