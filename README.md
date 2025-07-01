# 📄 AI Resume Reviewer

An intelligent tool built with Python and Streamlit to help job seekers optimize their resumes for specific job descriptions. This application analyzes your resume against a job posting, provides a match score, and offers actionable feedback for improvement with **job-specific scoring algorithms**.

 
*(Note: You can replace the above URL with a real screenshot of your app)*

---

## ✨ Features

### 🎯 **Job-Specific Analysis**
- **Software Engineering Mode**: Specialized scoring based on industry best practices and ATS requirements
- **General Analysis**: Traditional resume scoring for all other job types
- **Expandable Framework**: Easy to add new job categories (Data Science, Product Management, etc.)

### 📊 **Advanced Scoring System**
- **Industry-Specific Criteria**: Uses real hiring manager priorities and ATS optimization
- **Weighted Categories**: 
  - **Software Engineering**: Technical skills (35%), bullet quality (20%), structure (25%), formatting/readability (20%)
  - **General**: Keyword match (40%), skill match (30%), structure & readability (30%)
- **Detailed Feedback**: Category-specific improvement recommendations with priority weights

### 🔍 **Comprehensive Analysis**
- **PDF Resume Parsing**: Extracts text directly from your uploaded PDF resume
- **Enhanced Section Detection**: Identifies all major resume sections with multiple naming variants
- **Keyword Matching**: Uses TF-IDF to calculate semantic similarity between resume and job description
- **Technical Skill Analysis**: Specialized detection for programming languages, frameworks, and tools
- **ATS Optimization**: Checks for ATS-friendly formatting and structure
- **Quantified Achievement Detection**: Identifies and scores measurable accomplishments

### 💡 **Smart Recommendations**
- **Action Verb Analysis**: Ensures bullet points start with strong action verbs
- **Missing Keywords**: Identifies important terms from job descriptions not in your resume
- **Structure Optimization**: Recommends improvements for resume organization
- **Industry Best Practices**: Provides role-specific suggestions for improvement

### 🖥️ **User Experience**
- **Interactive UI**: Clean, intuitive web interface built with Streamlit
- **Real-time Analysis**: Instant feedback upon upload and analysis
- **Detailed Reports**: Expandable sections for in-depth improvement guidance
- **Progress Tracking**: Visual score breakdown by category

---

## 🛠️ Tech Stack

- **Backend**: Python 3.8+
- **Web Framework**: Streamlit
- **NLP & ML**: spaCy, Scikit-learn
- **PDF Processing**: pdfminer.six
- **Data Processing**: JSON-based scoring criteria
- **Text Analysis**: TF-IDF vectorization, cosine similarity
- **Language Models**: spaCy English model (en_core_web_sm)

---

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### 1. Prerequisites

- Python 3.8+ (recommended: Python 3.9+)
- Git (for cloning the repository)

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/ai-resume-reviewer.git
cd ai-resume-reviewer
```

### 3. Create and Activate a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
# For Windows
python -m venv .venv
.\.venv\Scripts\activate

# For macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies

Install all the required packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 5. Download spaCy Model

The application uses a spaCy model for natural language processing. Download it with the following command:

```bash
python -m spacy download en_core_web_sm
```

---

## ▶️ How to Run

Once the setup is complete, you can run the Streamlit application with a single command:

```bash
streamlit run app.py
```

Your web browser should automatically open to `http://localhost:8501` where you can access the application.

---

## 📖 How to Use

### For Software Engineering Positions:

1. **Select Job Type**: Choose "Software Engineering" from the dropdown menu
2. **Upload Resume**: Upload your PDF resume file
3. **Paste Job Description**: Copy and paste the complete job posting
4. **Analyze**: Click "Analyze Resume" to get detailed, industry-specific feedback

### Analysis Results Include:

- **Overall Match Score**: Comprehensive score based on industry criteria
- **Technical Skills Assessment**: Programming languages, frameworks, tools evaluation
- **Project Experience Review**: Analysis of personal/professional projects
- **ATS Optimization Score**: Formatting and keyword optimization for applicant tracking systems
- **Detailed Improvement Suggestions**: Categorized recommendations with priority levels

### For General Positions:

- Follow the same steps but select "General (Default Analysis)"
- Receive traditional resume analysis with keyword matching and structure evaluation

---

## 📊 Scoring Methodology

### Software Engineering Mode:
- **Technical Keywords (35%)**: Programming languages, frameworks, cloud technologies
- **Bullet Quality (20%)**: Action verbs, quantified achievements
- **Section Structure (25%)**: Presence and quality of key sections
- **Formatting & ATS (20%)**: Readability, ATS-friendly formatting

### General Mode:
- **Keyword/Semantic Match (40%)**: TF-IDF similarity between resume and job description
- **Skill Match (30%)**: Common keywords and skills identification
- **Structure & Readability (30%)**: Resume organization and clarity

---

## 📂 Project Structure

```
ai_resume_reviewer/
├── app.py                          # Main Streamlit application file
├── matcher.py                      # Core logic for scoring and matching
├── parser.py                       # Functions for PDF and text parsing
├── utils.py                        # Helper functions and constants
├── job_specific_scorer.py          # Job-specific scoring algorithms
├── requirements.txt                # Project dependencies
├── README.md                       # This file
├── FEATURES.md                     # Detailed feature documentation
├── test_scoring.py                 # Test script for validation
└── data/                           # Data files and examples
    ├── resume_scoring_criteria.json   # Software engineering scoring criteria
    ├── resume_scoring_criteria.csv    # Scoring criteria in CSV format
    ├── good_resume.txt                # Example of well-structured resume
    └── bad_resume.txt                 # Example of poorly-structured resume
```

---

## 🎯 Key Improvements for Software Engineering Resumes

Based on industry analysis and ATS requirements, the most impactful improvements are:

1. **🚀 Action Verbs**: Start bullet points with strong verbs
   - ✅ "Developed microservices architecture reducing response time by 40%"
   - ❌ "Was responsible for backend development"

2. **📈 Quantified Metrics**: Include specific numbers and impacts
   - ✅ "Optimized database queries, improving performance by 60%"
   - ❌ "Made database improvements"

3. **🔧 Technical Keywords**: Match job description technologies
   - Include: Programming languages, frameworks, cloud platforms, databases
   - Example: Python, React, AWS, PostgreSQL, Docker, Kubernetes

4. **💼 Project Section**: Showcase practical experience
   - Personal projects demonstrate passion and skill application
   - Include GitHub links and live demos when possible

5. **📋 Clear Structure**: Use consistent formatting
   - Clear section headers
   - Bullet points for achievements
   - Consistent date formats and spacing

---

## 🔮 Future Enhancements

The application is designed with extensibility in mind:

- **Additional Job Types**: Data Science, Product Management, Marketing, Design
- **Advanced NLP**: Sentiment analysis, writing quality assessment
- **Integration Options**: ATS simulation, LinkedIn optimization
- **Machine Learning**: Personalized recommendations based on successful resumes
- **Multi-language Support**: Resume analysis in multiple languages

---

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

1. **Add New Job Types**: Create scoring criteria for additional industries
2. **Improve Analysis**: Enhance NLP algorithms for better text understanding
3. **UI/UX**: Improve the user interface and experience
4. **Testing**: Add comprehensive test coverage
5. **Documentation**: Improve documentation and examples

### Development Setup:

```bash
# Clone and setup
git clone https://github.com/your-username/ai-resume-reviewer.git
cd ai-resume-reviewer
python -m venv .venv
source .venv/bin/activate  # or .\.venv\Scripts\activate on Windows
pip install -r requirements.txt
python -m spacy download en_core_web_sm

# Run tests
python test_scoring.py

# Start development server
streamlit run app.py
```

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the [FEATURES.md](FEATURES.md) for detailed documentation
2. Review the project structure and example files in the `data/` directory
3. Open an issue on GitHub with detailed information about your problem

---

## 🙏 Acknowledgments

- **spaCy**: For excellent NLP capabilities
- **Streamlit**: For making web app development simple and elegant
- **Scikit-learn**: For machine learning tools and TF-IDF implementation
- **Industry Experts**: For insights into ATS systems and hiring practices