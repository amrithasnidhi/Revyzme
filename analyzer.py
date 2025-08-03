import spacy
import language_tool_python
from textstat import flesch_reading_ease

nlp = spacy.load("en_core_web_sm")
tool = language_tool_python.LanguageTool('en-US')

role_keywords = {
    "Backend Developer": ["Python", "Flask", "Django", "REST API", "SQL", "Git"],
    "Data Analyst": ["Excel", "SQL", "Power BI", "Tableau", "Python", "Pandas"]
}

def analyze_resume(text, role="Backend Developer"):
    doc = nlp(text)
    words = [token.text for token in doc if token.is_alpha]

    matched_keywords = [kw for kw in role_keywords[role] if kw.lower() in text.lower()]
    grammar_matches = tool.check(text)
    readability = flesch_reading_ease(text)

    return {
        "Total Words": len(words),
        "Matched Keywords": matched_keywords,
        "Grammar Issues": len(grammar_matches),
        "Readability Score": readability,
        "Suggestions": {
            "Missing Keywords": list(set(role_keywords[role]) - set(matched_keywords)),
            "Grammar Suggestions": [match.message for match in grammar_matches[:5]]
        },
        "Score": min(100, len(matched_keywords) * 10 - len(grammar_matches))
    }
