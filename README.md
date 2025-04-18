# 🚀 AI-Powered Resume Matcher & Optimizer

A smart resume enhancement tool that analyzes resumes, extracts skills, compares them with job descriptions, calculates match percentage, and gives improvement suggestions — powered by FastAPI, Streamlit, and Machine Learning.

---

## 🔍 What It Does

- 🧠 Classifies resumes by job category using ML
- 🧾 Extracts relevant skills from resumes & job descriptions
- 🧮 Calculates match percentage (how well a resume fits a job)
- ❌ Shows missing skills
- 💡 Gives actionable suggestions to improve your resume
- 📄 Accepts both **text input** and **PDF uploads**

---

## ⚙️ How It Works

1. Resumes and job descriptions are input via text or file
2. Text is preprocessed and compared using a custom skill matcher
3. A match percentage is calculated based on skill overlap
4. Suggestions are generated to improve the match
5. Results are displayed in a beautiful Streamlit UI

---

## 📦 Technologies Used

| Layer | Tech |
|-------|------|
| 💻 Backend | FastAPI (Python) |
| 🤖 ML Model | TF-IDF + Classifier (`resume_classifier.pkl`) |
| 📊 Matching Logic | Custom skill extractor & matcher |
| 🎨 Frontend | Streamlit |
| 📄 File Processing | PyMuPDF for PDF parsing |
| 📚 Skills DB | Hardcoded list (extensible to file/DB) |

---

## 🚀 How to run the project

▶️ Start the Backend (FastAPI)

uvicorn app.main:app --reload

🖼️ Start the Frontend (Streamlit UI)
Open a new terminal: 

streamlit run streamlit_ui/app.py

---

## ✨ Final Output

Once everything runs: Upload or paste a resume and job description
Get:

✅ Match Percentage (with a progress bar)

🎯 Matched Skills

❌ Missing Skills

💡 Suggestions to Improve

----
