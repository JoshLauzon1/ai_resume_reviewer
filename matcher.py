import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils import RESUME_SECTIONS
from job_specific_scorer import JobSpecificScorer

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    """Extracts keywords (nouns, proper nouns, and noun chunks) from text."""
    doc = nlp(text.lower())
    keywords = set()
    for token in doc:
        if token.pos_ in ['NOUN', 'PROPN']:
            keywords.add(token.lemma_)
    for chunk in doc.noun_chunks:
        keywords.add(chunk.text)
    return list(keywords)

def calculate_tfidf_similarity(resume_text, job_desc_text):
    """Calculates cosine similarity using TF-IDF."""
    if not resume_text or not job_desc_text:
        return 0.0
    
    corpus = [resume_text, job_desc_text]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(corpus)
    
    # The matrix has resume at index 0 and job_desc at index 1
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity[0][0]

def analyze_resume(resume_text, job_desc_text, resume_sections, job_type="general"):
    """
    Performs a full analysis of the resume against the job description.
    
    Args:
        resume_text: The extracted resume text
        job_desc_text: The job description text
        resume_sections: Dictionary of detected resume sections
        job_type: The type of job being applied for (default: "general")
    
    Returns:
        A dictionary containing scores and feedback.
    """
    if job_type == "software_engineering":
        # Use job-specific scoring for software engineering
        scorer = JobSpecificScorer()
        job_specific_results = scorer.score_software_engineering_resume(resume_text, resume_sections)
        
        # Still calculate traditional metrics for comparison
        keyword_score = calculate_tfidf_similarity(resume_text, job_desc_text)
        resume_keywords = extract_keywords(resume_text)
        job_desc_keywords = extract_keywords(job_desc_text)
        common_keywords = set(resume_keywords) & set(job_desc_keywords)
        missing_keywords = set(job_desc_keywords) - set(resume_keywords)
        
        return {
            "total_score": job_specific_results['total_score'],
            "job_specific_score": job_specific_results['total_score'],
            "keyword_score": keyword_score,
            "skill_match_score": len(common_keywords) / len(job_desc_keywords) if job_desc_keywords else 0,
            "structure_score": job_specific_results.get('section_scores', {}),
            "missing_keywords": sorted(list(missing_keywords))[:10],
            "present_sections": [s for s in RESUME_SECTIONS.keys() if resume_sections.get(s)],
            "missing_sections": [s for s in ['experience', 'education', 'skills'] if s not in [k for k in resume_sections.keys() if resume_sections[k]]],
            "detailed_feedback": job_specific_results.get('detailed_feedback', []),
            "job_type": job_type,
            "formatting_scores": job_specific_results.get('formatting_scores', {}),
            "keyword_scores": job_specific_results.get('keyword_scores', {})
        }
    else:
        # Original general analysis
        # 1. Keyword/Semantic Match Score (40%)
        keyword_score = calculate_tfidf_similarity(resume_text, job_desc_text)

        # 2. Skill Match Score (30%)
        resume_keywords = extract_keywords(resume_text)
        job_desc_keywords = extract_keywords(job_desc_text)
        
        common_keywords = set(resume_keywords) & set(job_desc_keywords)
        missing_keywords = set(job_desc_keywords) - set(resume_keywords)
        
        skill_match_score = len(common_keywords) / len(job_desc_keywords) if job_desc_keywords else 0

        # 3. Structure Score (20%)
        present_sections = [s for s in RESUME_SECTIONS.keys() if resume_sections.get(s)]
        # Give points for having key sections
        key_sections_present = sum(1 for s in ['experience', 'education', 'skills'] if s in present_sections)
        structure_score = key_sections_present / 3.0

        # 4. Clarity Score (10%) - Simple placeholder
        # A more advanced check could analyze sentence length, action verbs, etc.
        clarity_score = 1.0 if '•' in resume_text or '*' in resume_text else 0.5 # Bonus for using bullet points

        # Calculate final weighted score
        total_score = (
            keyword_score * 0.40 +
            skill_match_score * 0.30 +
            structure_score * 0.20 +
            clarity_score * 0.10
        )

        return {
            "total_score": total_score,
            "keyword_score": keyword_score,
            "skill_match_score": skill_match_score,
            "structure_score": structure_score,
            "missing_keywords": sorted(list(missing_keywords))[:10], # Show top 10 missing
            "present_sections": present_sections,
            "missing_sections": [s for s in ['experience', 'education', 'skills'] if s not in present_sections],
            "job_type": job_type
        }
