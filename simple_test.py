"""
Simple test to verify imports work
"""
try:
    from parser import extract_sections
    print("✓ Parser import successful")
except Exception as e:
    print(f"✗ Parser import failed: {e}")

try:
    from matcher import analyze_resume
    print("✓ Matcher import successful")
except Exception as e:
    print(f"✗ Matcher import failed: {e}")

try:
    from job_specific_scorer import JobSpecificScorer
    print("✓ JobSpecificScorer import successful")
except Exception as e:
    print(f"✗ JobSpecificScorer import failed: {e}")

try:
    import streamlit
    print("✓ Streamlit import successful")
except Exception as e:
    print(f"✗ Streamlit import failed: {e}")

try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
    print("✓ SpaCy model loaded successfully")
except Exception as e:
    print(f"✗ SpaCy model failed: {e}")

print("\nTesting basic functionality...")
try:
    # Test with simple text
    test_text = "Experience\nSoftware Engineer\nPython, Java"
    sections = extract_sections(test_text)
    print(f"✓ Section extraction works: {sections}")
except Exception as e:
    print(f"✗ Section extraction failed: {e}")
