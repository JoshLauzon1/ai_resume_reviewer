# AI Resume Reviewer - New Job-Specific Features

## Overview
This document describes the new job-specific scoring functionality added to the AI Resume Reviewer application.

## New Features

### 1. Job Type Dropdown Menu
- Added a dropdown in the Streamlit interface to select job types
- Currently supports:
  - General (Default Analysis) - uses the original scoring algorithm
  - Software Engineering - uses specialized scoring criteria

### 2. Software Engineering Specific Scoring
The software engineering mode uses a comprehensive scoring system based on industry best practices:

#### Scoring Categories:
1. **Section Structure (Weight varies)**
   - Education (5%)
   - Experience (10%) 
   - Skills (5%)
   - Projects (5%)

2. **Bullet Quality (20%)**
   - Action verb usage (10%)
   - Quantified metrics (10%)

3. **Keyword Matching (35%)**
   - Programming languages: Python, Java, C++, Go (10%)
   - Database technologies: SQL, NoSQL, MongoDB, PostgreSQL (5%)
   - Cloud/DevOps: AWS, GCP, Azure, Docker, Kubernetes (10%)
   - Communication protocols: REST, gRPC, GraphQL (5%)
   - Web stack: React, Node.js, Express, TypeScript (5%)

4. **Formatting (10%)**
   - Appropriate bullet count (5%)
   - Sentence length optimization (5%)

5. **Readability (5%)**
   - Passive voice detection (5%)

6. **ATS Friendly (5%)**
   - Standard fonts usage (3%)
   - Minimal graphics/icons (2%)

### 3. Enhanced Analysis Results
For software engineering resumes, the system provides:
- Detailed breakdown of scores by category
- Specific improvement recommendations
- Categorized feedback with priority weights
- Industry-specific suggestions

### 4. Improved Section Detection
Enhanced the parser to better detect resume sections including:
- Contact Information
- Summary/Professional Summary
- Experience/Work Experience
- Education/Academic Background
- Skills/Technical Skills
- Projects/Personal Projects
- Certifications

## Technical Implementation

### New Files:
- `job_specific_scorer.py` - Contains the JobSpecificScorer class with software engineering criteria
- `test_scoring.py` - Test script to validate the new functionality

### Modified Files:
- `app.py` - Added dropdown menu and enhanced results display
- `matcher.py` - Integrated job-specific scoring
- `parser.py` - Improved section extraction

### Data Files Used:
- `data/resume_scoring_criteria.json` - Contains the detailed scoring criteria
- `data/good_resume.txt` - Example of a well-structured resume
- `data/bad_resume.txt` - Example of a poorly-structured resume

## Usage

1. **Select Job Type**: Choose "Software Engineering" from the dropdown
2. **Upload Resume**: Upload your PDF resume
3. **Paste Job Description**: Add the job posting text
4. **Analyze**: Click "Analyze Resume" to get detailed feedback

## Benefits

### For Software Engineering Candidates:
- Industry-specific scoring based on actual ATS and hiring practices
- Detailed technical skill analysis
- Quantified achievement recommendations
- ATS optimization suggestions

### Scoring Accuracy:
- Uses weighted criteria based on hiring manager priorities
- Focuses on technical skills and project experience
- Emphasizes quantified achievements and action verbs
- Checks for ATS-friendly formatting

## Future Enhancements

The framework is designed to easily add more job types:
- Data Science
- Product Management
- Marketing
- Sales
- Design
- Finance

Each job type can have its own specialized scoring criteria and feedback system.

## Example Improvements for Software Engineering Resumes

Based on the scoring criteria, candidates typically need to improve:

1. **Action Verbs**: Start bullet points with strong verbs like "Developed", "Implemented", "Optimized"
2. **Quantified Metrics**: Include numbers like "Improved performance by 40%" or "Reduced load time by 2 seconds"
3. **Technical Keywords**: Ensure relevant technologies from the job description are mentioned
4. **Project Section**: Include personal or side projects demonstrating skills
5. **Clear Structure**: Use consistent formatting and clear section headers

## Running the Application

```bash
# Install dependencies
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm

# Run the Streamlit app
streamlit run app.py
```

The application will be available at http://localhost:8501
