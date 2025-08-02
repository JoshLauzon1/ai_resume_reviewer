import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import pytest
from parser import extract_sections
from matcher import analyze_resume

JOB_DESC = """
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


def _analyze_resume(path: str):
    with open(path, "r") as f:
        resume = f.read()
    sections = extract_sections(resume)
    return analyze_resume(resume, JOB_DESC, sections, "software_engineering")


def test_good_resume_scoring_and_sections():
    analysis = _analyze_resume("data/good_resume.txt")
    assert analysis["total_score"] == pytest.approx(0.7738809523809524, rel=1e-3)
    assert analysis["present_sections"] == ["experience", "education", "skills", "projects"]
    assert analysis["missing_sections"] == []


def test_bad_resume_scoring_and_sections():
    analysis = _analyze_resume("data/bad_resume.txt")
    assert analysis["total_score"] == pytest.approx(0.4773333333333332, rel=1e-3)
    assert analysis["present_sections"] == ["experience", "education", "skills", "projects"]
    assert analysis["missing_sections"] == []
