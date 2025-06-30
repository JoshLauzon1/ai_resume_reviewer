# 📄 AI Resume Reviewer

An intelligent tool built with Python and Streamlit to help job seekers optimize their resumes for specific job descriptions. This application analyzes your resume against a job posting, provides a match score, and offers actionable feedback for improvement.

 
*(Note: You can replace the above URL with a real screenshot of your app)*

---

## ✨ Features

- **PDF Resume Parsing**: Extracts text directly from your uploaded PDF resume.
- **Job Description Analysis**: Compares your resume content against the provided job description.
- **Keyword Matching**: Uses TF-IDF to calculate a semantic similarity score between the two documents.
- **Skill Gap Analysis**: Identifies important keywords from the job description that are missing from your resume.
- **Structure Check**: Verifies the presence of essential resume sections like "Experience," "Education," and "Skills."
- **Weighted Scoring**: Calculates an overall match score based on:
  - Keyword/Semantic Match (40%)
  - Skill Match (30%)
  - Structure & Readability (30%)
- **Interactive UI**: A simple and clean web interface built with Streamlit.

---

## 🛠️ Tech Stack

- **Backend**: Python
- **Web Framework**: Streamlit
- **NLP**: spaCy
- **Machine Learning**: Scikit-learn
- **PDF Parsing**: pdfminer.six

---

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### 1. Prerequisites

- Python 3.8+

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/ai-resume-reviewer.git
cd ai-resume-reviewer
```

### 3. Create and Activate a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
# For Windows
python -m venv env
.\env\Scripts\activate

# For macOS/Linux
python3 -m venv env
source env/bin/activate
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

Your web browser should automatically open to the application's UI.

---

## 📂 Project Structure

```
ai_resume_reviewer/
├── app.py             # Main Streamlit application file
├── matcher.py         # Core logic for scoring and matching
├── parser.py          # Functions for PDF and text parsing
├── utils.py           # Helper functions and constants
├── requirements.txt   # Project dependencies
└── README.md          # This file
```