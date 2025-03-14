from flask import Flask, request, jsonify
from app.routes import main
import PyPDF2
import docx2txt
import spacy
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


nltk.download('stopwords')
from nltk.corpus import stopwords

app = Flask(__name__)
app.register_blueprint(main)

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Function to extract text from PDF
def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
    return text

# Function to extract text from DOCX
def extract_text_from_docx(file):
    return docx2txt.process(file)

# Function to extract important keywords (skills, experience, education)
def extract_keywords(text):
    doc = nlp(text)
    skills = []
    experience_years = []
    education = []
    
    # Example skills list (you can expand this)
    predefined_skills = {"python", "java", "machine learning", "deep learning", "sql", "data science", "flask", "django"}
    
    for ent in doc.ents:
        if ent.label_ == "ORG" and ent.text.lower() in predefined_skills:
            skills.append(ent.text)
        elif ent.label_ in ["DATE", "TIME"] and "year" in ent.text.lower():
            experience_years.append(ent.text)
        elif ent.label_ in ["EDUCATION", "DEGREE"]:
            education.append(ent.text)

    return {
        "skills": list(set(skills)),
        "experience": list(set(experience_years)),
        "education": list(set(education))
    }

# Function to clean text for similarity calculation
def clean_text(text):
    words = text.lower().split()
    words = [word for word in words if word not in stopwords.words("english")]
    return " ".join(words)

# Function to calculate similarity between resume & job description
def calculate_similarity(resume_text, job_desc_text):
    resume_text_clean = clean_text(resume_text)
    job_desc_text_clean = clean_text(job_desc_text)
    
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text_clean, job_desc_text_clean])
    similarity_score = cosine_similarity(vectors)[0][1] * 100  # Convert to percentage
    return round(similarity_score, 2)

# API to handle resume & job description upload
@app.route("/match", methods=["POST"])
def match_resume():
    if "resume" not in request.files or "job_desc" not in request.files:
        return jsonify({"error": "Both resume and job description must be uploaded"}), 400
    
    resume_file = request.files["resume"]
    job_desc_file = request.files["job_desc"]
    
    resume_ext = resume_file.filename.split(".")[-1].lower()
    job_desc_ext = job_desc_file.filename.split(".")[-1].lower()

    # Extract text from resume
    if resume_ext == "pdf":
        resume_text = extract_text_from_pdf(resume_file)
    elif resume_ext in ["doc", "docx"]:
        resume_text = extract_text_from_docx(resume_file)
    else:
        return jsonify({"error": "Unsupported resume file format"}), 400

    # Extract text from job description
    if job_desc_ext == "pdf":
        job_desc_text = extract_text_from_pdf(job_desc_file)
    elif job_desc_ext in ["doc", "docx"]:
        job_desc_text = extract_text_from_docx(job_desc_file)
    else:
        return jsonify({"error": "Unsupported job description file format"}), 400

    # Extract keywords (skills, experience, education)
    resume_keywords = extract_keywords(resume_text)
    job_desc_keywords = extract_keywords(job_desc_text)

    # Calculate match percentage
    match_percentage = calculate_similarity(resume_text, job_desc_text)

    return jsonify({
        "match_percentage": match_percentage,
        "resume_keywords": resume_keywords,
        "job_description_keywords": job_desc_keywords
    })

if __name__ == "__main__":
    app.run(debug=True)
