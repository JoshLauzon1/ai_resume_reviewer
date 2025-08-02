import streamlit as st
from parser import extract_text_from_pdf, extract_sections
from matcher import analyze_resume

st.set_page_config(page_title="AI Resume Reviewer", layout="wide")

def display_results(analysis):
    """Displays the analysis results in a user-friendly format."""
    st.subheader("Analysis Results")

    score = analysis['total_score'] * 100
    st.progress(int(score), text=f"Overall Match Score: {score:.2f}%")

    # Show job type specific information
    job_type = analysis.get('job_type', 'general')
    if job_type == 'software_engineering':
        st.info(f"📊 **Analysis Type:** Software Engineering Resume Scoring")
    else:
        st.info(f"📊 **Analysis Type:** General Resume Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.info("Score Breakdown")
        if job_type == 'software_engineering':
            st.markdown(f"- **Job-Specific Score:** {analysis.get('job_specific_score', 0)*100:.2f}%")
            st.markdown(f"- **Keyword/Semantic Match:** {analysis['keyword_score']*100:.2f}%")
            st.markdown(f"- **Skill Match:** {analysis['skill_match_score']*100:.2f}%")
        else:
            st.markdown(f"- **Keyword/Semantic Match:** {analysis['keyword_score']*100:.2f}%")
            st.markdown(f"- **Skill Match:** {analysis['skill_match_score']*100:.2f}%")
            st.markdown(f"- **Structure & Readability:** {analysis['structure_score']*100:.2f}%")

    with col2:
        st.info("Resume Structure")
        if job_type == 'software_engineering':
            section_scores = analysis.get('section_scores', {})
            if isinstance(section_scores, dict) and section_scores:
                st.markdown("**Section Scores:**")
                for section, result in section_scores.items():
                    score = result.get('score', 0) * 100
                    st.markdown(f"- {section}: {score:.0f}%")
        if analysis['missing_sections']:
            st.warning(f"**Missing Sections:** {', '.join(analysis['missing_sections']).title()}")
        if analysis['present_sections']:
            st.success(f"**Detected Sections:** {', '.join(analysis['present_sections']).title()}")

    # Show detailed feedback for software engineering
    if job_type == 'software_engineering' and analysis.get('detailed_feedback'):
        st.info("🎯 Detailed Improvement Recommendations")
        
        # Group feedback by category
        feedback_by_category = {}
        for feedback in analysis['detailed_feedback']:
            category = feedback['category']
            if category not in feedback_by_category:
                feedback_by_category[category] = []
            feedback_by_category[category].append(feedback)
        
        for category, feedbacks in feedback_by_category.items():
            with st.expander(f"🔍 {category} Issues ({len(feedbacks)} items)"):
                for feedback in feedbacks:
                    weight_indicator = "🔴" if feedback['weight'] >= 0.08 else "🟡" if feedback['weight'] >= 0.05 else "🟢"
                    st.markdown(f"{weight_indicator} **{feedback['issue']}** (Weight: {feedback['weight']*100:.0f}%)")
                    st.markdown(f"   💡 {feedback['suggestion']}")
                    st.markdown("---")
    
    st.info("Missing Keywords & Suggestions")
    if analysis['missing_keywords']:
        st.warning("**Keywords to Consider Adding:**")
        st.markdown(f"`{', '.join(analysis['missing_keywords'])}`")
    else:
        st.success("Excellent keyword coverage!")

    if job_type != 'software_engineering':
        st.markdown(
            "**Tip:** Ensure your resume uses clear bullet points (•) under your experience to improve clarity."
        )


def main():
    st.title("📄 AI Resume Reviewer")
    st.markdown("Upload your resume and paste a job description to get an instant analysis and improvement tips.")

    # Job type selection dropdown
    st.subheader("🎯 Select Job Type")
    job_type = st.selectbox(
        "Choose the type of position you're applying for:",
        options=[
            ("general", "General (Default Analysis)"),
            ("software_engineering", "Software Engineering")
        ],
        format_func=lambda x: x[1],
        index=0,
        help="Select the job type for specialized resume analysis with industry-specific criteria."
    )
    
    selected_job_type = job_type[0]
    
    if selected_job_type == "software_engineering":
        st.info("🚀 **Software Engineering Mode:** Your resume will be analyzed using specialized criteria including technical skills, project experience, quantified achievements, and ATS optimization.")

    resume_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
    job_desc = st.text_area("Paste the Job Description here", height=300)

    if st.button("Analyze Resume", type="primary"):
        if resume_file is not None and job_desc:
            with st.spinner("Analyzing... This may take a moment."):
                try:
                    resume_text = extract_text_from_pdf(resume_file)
                    resume_sections = extract_sections(resume_text)
                    
                    analysis_results = analyze_resume(resume_text, job_desc, resume_sections, selected_job_type)
                    
                    display_results(analysis_results)

                except Exception as e:
                    st.error(f"An error occurred during analysis: {e}")
        else:
            st.warning("Please upload a resume and paste a job description.")

if __name__ == "__main__":
    main()