import json
import logging
import re
import spacy
from typing import Dict, List, Tuple
from utils import clean_text

logger = logging.getLogger(__name__)

nlp = spacy.load("en_core_web_sm")

class JobSpecificScorer:
    def __init__(self):
        self.criteria = self._load_scoring_criteria()
        
    def _load_scoring_criteria(self) -> List[Dict]:
        """Load scoring criteria from JSON file."""
        try:
            with open('data/resume_scoring_criteria.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error("Scoring criteria file not found at data/resume_scoring_criteria.json")
            return []
        except json.JSONDecodeError as e:
            logger.error("Failed to decode scoring criteria JSON: %s", e)
            return []
    
    def score_software_engineering_resume(self, resume_text: str, resume_sections: Dict) -> Dict:
        """Score a resume specifically for software engineering roles."""
        scores = {
            'section_scores': {},
            'keyword_scores': {},
            'formatting_scores': {},
            'bullet_quality_scores': {},
            'readability_scores': {},
            'ats_friendly_scores': {},
            'total_score': 0.0,
            'detailed_feedback': []
        }
        
        total_weight = 0.0
        weighted_score = 0.0

        if not self.criteria:
            logger.warning("No scoring criteria loaded. Returning default scores.")
            return scores

        for criterion in self.criteria:
            category = criterion['Category']
            criterion_type = criterion['Type']
            pattern = criterion['Keyword/Pattern']
            weight = criterion['Weight']
            notes = criterion['Notes']
            
            score = self._evaluate_criterion(resume_text, resume_sections, criterion)
            
            # Map category to the correct scores key
            category_key = category.lower().replace(" ", "_") + "_scores"
            if category_key not in scores:
                scores[category_key] = {}
            
            scores[category_key][pattern] = {
                'score': score,
                'weight': weight,
                'notes': notes
            }
            
            weighted_score += score * weight
            total_weight += weight
            
            # Add feedback for failed criteria
            if score < 0.5:
                scores['detailed_feedback'].append({
                    'category': category,
                    'issue': pattern,
                    'suggestion': self._get_suggestion(criterion),
                    'weight': weight
                })
        
        scores['total_score'] = weighted_score / total_weight if total_weight > 0 else 0.0
        return scores
    
    def _evaluate_criterion(self, resume_text: str, resume_sections: Dict, criterion: Dict) -> float:
        """Evaluate a single scoring criterion."""
        category = criterion['Category']
        criterion_type = criterion['Type']
        pattern = criterion['Keyword/Pattern']
        
        if category == 'Section':
            return self._check_section_presence(resume_sections, pattern)
        elif category == 'Bullet Quality':
            return self._check_bullet_quality(resume_text, pattern)
        elif category == 'Keywords':
            return self._check_keyword_match(resume_text, pattern)
        elif category == 'Formatting':
            return self._check_formatting(resume_text, pattern)
        elif category == 'Readability':
            return self._check_readability(resume_text, pattern)
        elif category == 'ATS Friendly':
            return self._check_ats_friendly(resume_text, pattern)
        
        return 0.0
    
    def _check_section_presence(self, resume_sections: Dict, section_name: str) -> float:
        """Check if a required section is present."""
        section_variants = {
            'Education': ['education', 'academic background', 'qualifications'],
            'Experience': ['experience', 'work experience', 'professional experience', 'employment'],
            'Skills': ['skills', 'technical skills', 'core competencies', 'technologies'],
            'Projects': ['projects', 'personal projects', 'side projects', 'portfolio']
        }
        
        variants = section_variants.get(section_name, [section_name.lower()])
        
        for variant in variants:
            if any(variant in key.lower() for key in resume_sections.keys() if resume_sections[key]):
                return 1.0
        
        return 0.0
    
    def _check_bullet_quality(self, resume_text: str, pattern: str) -> float:
        """Check bullet point quality."""
        if "action verb" in pattern.lower():
            return self._check_action_verbs(resume_text)
        elif "number" in pattern.lower() or "metric" in pattern.lower():
            return self._check_quantified_metrics(resume_text)
        
        return 0.0
    
    def _check_action_verbs(self, resume_text: str) -> float:
        """Check if bullet points start with action verbs."""
        action_verbs = [
            'developed', 'implemented', 'designed', 'built', 'created', 'led', 'managed',
            'optimized', 'improved', 'reduced', 'increased', 'deployed', 'migrated',
            'collaborated', 'architected', 'engineered', 'programmed', 'automated'
        ]
        
        # Find bullet points (lines starting with • or -)
        bullet_pattern = r'^[\s]*[-•]\s*(.+)$'
        bullets = re.findall(bullet_pattern, resume_text, re.MULTILINE | re.IGNORECASE)
        
        if not bullets:
            return 0.0
        
        action_verb_count = 0
        for bullet in bullets:
            first_word = bullet.strip().split()[0].lower() if bullet.strip() else ""
            if first_word in action_verbs:
                action_verb_count += 1
        
        return min(action_verb_count / len(bullets), 1.0)
    
    def _check_quantified_metrics(self, resume_text: str) -> float:
        """Check if bullet points contain quantified metrics."""
        # Patterns for numbers, percentages, time periods, etc.
        metric_patterns = [
            r'\d+%',  # percentages
            r'\d+[kK]',  # thousands (10k)
            r'\d+\s*(hours?|days?|weeks?|months?|years?)',  # time
            r'\d+\s*(million|billion|thousand)',  # large numbers
            r'\$\d+',  # money
            r'\d+\.\d+',  # decimals
            r'\d+x',  # multipliers
            r'\d+\s*(users?|customers?|clients?|requests?)'  # quantities
        ]
        
        bullet_pattern = r'^[\s]*[-•]\s*(.+)$'
        bullets = re.findall(bullet_pattern, resume_text, re.MULTILINE | re.IGNORECASE)
        
        if not bullets:
            return 0.0
        
        quantified_count = 0
        for bullet in bullets:
            for pattern in metric_patterns:
                if re.search(pattern, bullet, re.IGNORECASE):
                    quantified_count += 1
                    break
        
        return min(quantified_count / len(bullets), 1.0)
    
    def _check_keyword_match(self, resume_text: str, keywords: str) -> float:
        """Check for presence of specific keywords."""
        keyword_list = [k.strip().lower() for k in keywords.split(',')]
        resume_lower = resume_text.lower()
        
        found_keywords = sum(1 for keyword in keyword_list if keyword in resume_lower)
        return found_keywords / len(keyword_list) if keyword_list else 0.0
    
    def _check_formatting(self, resume_text: str, pattern: str) -> float:
        """Check formatting criteria."""
        if "bullet count" in pattern.lower():
            return self._check_bullet_count(resume_text)
        elif "sentence length" in pattern.lower():
            return self._check_sentence_length(resume_text)
        
        return 0.5  # Default moderate score
    
    def _check_bullet_count(self, resume_text: str) -> float:
        """Check if sections have appropriate number of bullets (2-5)."""
        bullet_pattern = r'^[\s]*[-•]\s*(.+)$'
        bullets = re.findall(bullet_pattern, resume_text, re.MULTILINE)
        
        # This is a simplified check - ideally we'd check per section
        if 2 <= len(bullets) <= 15:  # Reasonable total for entire resume
            return 1.0
        elif len(bullets) > 0:
            return 0.7
        else:
            return 0.0
    
    def _check_sentence_length(self, resume_text: str) -> float:
        """Check if sentences are reasonably short (<30 words)."""
        sentences = re.split(r'[.!?]+', resume_text)
        if not sentences:
            return 0.0
        
        good_length_count = 0
        for sentence in sentences:
            word_count = len(sentence.split())
            if 1 <= word_count <= 30:
                good_length_count += 1
        
        return good_length_count / len(sentences)
    
    def _check_readability(self, resume_text: str, pattern: str) -> float:
        """Check readability criteria."""
        if "passive voice" in pattern.lower():
            return self._check_passive_voice(resume_text)
        
        return 0.7  # Default moderate score
    
    def _check_passive_voice(self, resume_text: str) -> float:
        """Check for passive voice usage (lower is better)."""
        doc = nlp(resume_text)
        total_sentences = 0
        passive_sentences = 0
        
        for sent in doc.sents:
            total_sentences += 1
            # Simple heuristic: look for "was/were + past participle"
            tokens = [token for token in sent]
            for i, token in enumerate(tokens[:-1]):
                if token.lemma_ in ['be'] and tokens[i+1].tag_ in ['VBN']:
                    passive_sentences += 1
                    break
        
        if total_sentences == 0:
            return 1.0
        
        passive_ratio = passive_sentences / total_sentences
        return max(0.0, 1.0 - passive_ratio)  # Higher score for less passive voice
    
    def _check_ats_friendly(self, resume_text: str, pattern: str) -> float:
        """Check ATS-friendly formatting."""
        # These are placeholder checks - in a real system you'd need more sophisticated analysis
        if "standard fonts" in pattern.lower():
            return 0.8  # Assume good unless we can detect otherwise
        elif "graphics" in pattern.lower():
            # Check for common graphic indicators
            graphic_indicators = ['[image]', '[graphic]', '[chart]', '█', '▪', '▫']
            has_graphics = any(indicator in resume_text for indicator in graphic_indicators)
            return 0.3 if has_graphics else 1.0
        
        return 0.8
    
    def _get_suggestion(self, criterion: Dict) -> str:
        """Get improvement suggestions based on failed criteria."""
        category = criterion['Category']
        pattern = criterion['Keyword/Pattern']
        
        suggestions = {
            'Section': {
                'Education': 'Add an Education section with your degree, institution, and graduation year.',
                'Experience': 'Include a detailed Work Experience section with your professional roles.',
                'Skills': 'Add a Skills section listing your technical competencies.',
                'Projects': 'Include a Projects section showcasing your work outside of employment.'
            },
            'Bullet Quality': {
                'Starts with action verb': 'Start each bullet point with a strong action verb like "Developed", "Implemented", or "Led".',
                'Contains a number/quantified metric': 'Include specific numbers and metrics in your bullet points (e.g., "Improved performance by 40%").'
            },
            'Keywords': {
                'Python, Java, C++, Go': 'Include relevant programming languages mentioned in the job description.',
                'SQL, NoSQL, MongoDB, PostgreSQL': 'Mention database technologies you\'ve worked with.',
                'AWS, GCP, Azure, Docker, Kubernetes': 'Include cloud and DevOps technologies from your experience.',
                'REST, gRPC, GraphQL': 'Mention API technologies you\'ve used.',
                'React, Node.js, Express, TypeScript': 'Include web development frameworks and technologies.'
            }
        }
        
        return suggestions.get(category, {}).get(pattern, 'Consider improving this area based on job requirements.')
