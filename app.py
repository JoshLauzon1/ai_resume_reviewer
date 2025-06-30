import streamlit as st
from parser import extract_text_from_pdf, extract_sections
from matcher import analyze_resume

st.set_page_config(page_title="AI Resume Reviewer", layout="wide")

def display_results(analysis):
    """Displays the analysis results in a user-friendly format."""
    st.subheader("Analysis Results")

    score = analysis['total_score'] * 100
    st.progress(int(score), text=f"Overall Match Score: {score:.2f}%")

    col1, col2 = st.columns(2)

    with col1:
        st.info("Score Breakdown")
        st.markdown(f"- **Keyword/Semantic Match:** {analysis['keyword_score']*100:.2f}%")
        st.markdown(f"- **Skill Match:** {analysis['skill_match_score']*100:.2f}%")
        st.markdown(f"- **Structure & Readability:** {analysis['structure_score']*100:.2f}%")

    with col2:
        st.info("Resume Structure")
        if analysis['missing_sections']:
            st.warning(f"**Missing Sections:** {', '.join(analysis['missing_sections']).title()}")
        if analysis['present_sections']:
            st.success(f"**Detected Sections:** {', '.join(analysis['present_sections']).title()}")

    st.info("Feedback & Suggestions")
    if analysis['missing_keywords']:
        st.warning("**Keywords to Consider Adding:**")
        st.markdown(f"`{', '.join(analysis['missing_keywords'])}`")
    else:
        st.success("Excellent keyword coverage!")

    st.markdown(
        "**Tip:** Ensure your resume uses clear bullet points (•) under your experience to improve clarity."
    )


def main():
    st.title("📄 AI Resume Reviewer")
    st.markdown("Upload your resume and paste a job description to get an instant analysis and improvement tips.")

    resume_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
    job_desc = st.text_area("Paste the Job Description here", height=300)

    if st.button("Analyze Resume", type="primary"):
        if resume_file is not None and job_desc:
            with st.spinner("Analyzing... This may take a moment."):
                try:
                    resume_text = extract_text_from_pdf(resume_file)
                    resume_sections = extract_sections(resume_text)
                    
                    analysis_results = analyze_resume(resume_text, job_desc, resume_sections)
                    
                    display_results(analysis_results)

                except Exception as e:
                    st.error(f"An error occurred during analysis: {e}")
        else:
            st.warning("Please upload a resume and paste a job description.")

if __name__ == "__main__":
    main()