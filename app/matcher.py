import re

COMMON_SKILLS = {
    'python', 'java', 'sql', 'excel', 'fastapi', 'django', 'tensorflow', 'pandas',
    'numpy', 'git', 'docker', 'aws', 'machine learning', 'communication', 'teamwork'
}

def extract_skills(text):
    text = text.lower()
    return [skill for skill in COMMON_SKILLS if skill in text]

def compare_skills(resume_text, job_description):
    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_description))

    missing_skills = job_skills - resume_skills
    matched_skills = resume_skills & job_skills

    match_percent = (len(matched_skills) / len(job_skills)) * 100 if job_skills else 0

    return {
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills),
        "match_percentage": round(match_percent, 2)
    }

