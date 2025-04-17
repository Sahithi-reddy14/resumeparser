from app.model import get_model

model, vectorizer = get_model()

def predict_resume(resume_text: str):
    features = vectorizer.transform([resume_text])
    prediction = model.predict(features)
    return prediction[0]

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