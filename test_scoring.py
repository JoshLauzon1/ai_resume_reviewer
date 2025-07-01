"""
Demo script to test the new job-specific scoring functionality
"""
from parser import extract_sections
from matcher import analyze_resume

# Test with the good resume example
def test_software_engineering_scoring():
    print("Testing Software Engineering Resume Scoring...")
    
    # Load the good resume example
    with open('data/good_resume.txt', 'r') as f:
        good_resume = f.read()
    
    # Load the bad resume example
    with open('data/bad_resume.txt', 'r') as f:
        bad_resume = f.read()
    
    # Sample job description for software engineering
    job_desc = """
    We are looking for a Software Engineer to join our team.
    
    Requirements:
    - Bachelor's degree in Computer Science or related field
    - 2+ years of experience in software development
    - Proficiency in Python, Java, or C++
    - Experience with REST APIs and microservices
    - Knowledge of AWS, Docker, and containerization
    - Experience with SQL databases like PostgreSQL
    - Familiarity with React and Node.js
    - Strong problem-solving skills
    - Excellent communication skills
    
    Responsibilities:
    - Develop and maintain web applications
    - Design and implement REST APIs
    - Collaborate with frontend and backend teams
    - Write unit tests and maintain code quality
    - Deploy applications using CI/CD pipelines
    """
    
    print("\n=== GOOD RESUME ANALYSIS (Software Engineering) ===")
    good_sections = extract_sections(good_resume)
    good_analysis = analyze_resume(good_resume, job_desc, good_sections, "software_engineering")
    
    print(f"Total Score: {good_analysis['total_score']*100:.2f}%")
    print(f"Job-Specific Score: {good_analysis.get('job_specific_score', 0)*100:.2f}%")
    print(f"Keyword Score: {good_analysis['keyword_score']*100:.2f}%")
    print(f"Present Sections: {good_analysis['present_sections']}")
    print(f"Missing Sections: {good_analysis['missing_sections']}")
    print(f"Number of Improvement Suggestions: {len(good_analysis.get('detailed_feedback', []))}")
    
    print("\n=== BAD RESUME ANALYSIS (Software Engineering) ===")
    bad_sections = extract_sections(bad_resume)
    bad_analysis = analyze_resume(bad_resume, job_desc, bad_sections, "software_engineering")
    
    print(f"Total Score: {bad_analysis['total_score']*100:.2f}%")
    print(f"Job-Specific Score: {bad_analysis.get('job_specific_score', 0)*100:.2f}%")
    print(f"Keyword Score: {bad_analysis['keyword_score']*100:.2f}%")
    print(f"Present Sections: {bad_analysis['present_sections']}")
    print(f"Missing Sections: {bad_analysis['missing_sections']}")
    print(f"Number of Improvement Suggestions: {len(bad_analysis.get('detailed_feedback', []))}")
    
    print("\n=== SAMPLE IMPROVEMENT SUGGESTIONS FOR BAD RESUME ===")
    for i, feedback in enumerate(bad_analysis.get('detailed_feedback', [])[:5], 1):
        print(f"{i}. {feedback['category']}: {feedback['issue']}")
        print(f"   Suggestion: {feedback['suggestion']}")
        print(f"   Weight: {feedback['weight']*100:.0f}%\n")

if __name__ == "__main__":
    test_software_engineering_scoring()
