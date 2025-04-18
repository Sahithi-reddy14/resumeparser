import streamlit as st
import requests
import tempfile
from file_utils import extract_text_from_pdf

# 🌟 Title
st.title("🚀 AI Resume Matcher with Suggestions")

# 📝 Text Inputs
st.markdown("### ✍️ Paste Resume Text ")
resume_text_input = st.text_area("🧾 Resume Text", height=200, key="resume_input")

st.markdown("### 📎 Upload Resume File (PDF)")
resume_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"], key="resume_upload")

st.markdown("---")

st.markdown("### ✍️ Paste Job Description")
job_text_input = st.text_area("📄 Job Description Text", height=200, key="job_input")


st.markdown("---")

# 🚀 Match button
if st.button("🔍 Analyze Match"):
    # 🔁 Read from text areas or PDF uploads
    resume_text = resume_text_input.strip()
    job_text = job_text_input.strip()

    # If resume text not given, try file
    if not resume_text and resume_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(resume_file.read())
            resume_text = extract_text_from_pdf(tmp.name)

    # If job text not given, try file
    if not job_text and job_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(job_file.read())
            job_text = extract_text_from_pdf(tmp.name)

    # ✅ Validate inputs
    if not resume_text or not job_text:
        st.error("❗ Please provide both resume and job description (via text or file).")
    else:
        payload = {
            "resume_text": resume_text,
            "job_description": job_text
        }

        response = requests.post("http://127.0.0.1:8000/match", json=payload)

        if response.status_code == 200:
            result = response.json()
            match_percentage = result["match_percentage"]
            matched = result["matched_skills"]
            missing = result["missing_skills"]
            suggestions = result["suggestions"]


           # 🟢 Show Match Score
            st.markdown(f"### ✅ Match Score: **{match_percentage}%**")
            if match_percentage >= 80:
                st.success("🟢 Excellent match! Your resume is highly relevant for this role.")
            elif match_percentage >= 60:
                st.warning("🟡 Decent match. Consider improving your resume with a few more keywords.")
            else:
                st.error("🔴 Low match. Your resume may not pass the ATS. Add missing skills!")
                
            st.markdown(f"**🎯 Matched Skills:** {', '.join(matched) if matched else 'None'}")
            st.markdown(f"**❌ Missing Skills:** {', '.join(missing) if missing else 'None'}")

            if result['suggestions']:
                st.markdown("### 💡 Suggestions to Improve:")
                for s in result['suggestions']:
                    st.markdown(f"- {s}")
        else:
            st.error("⚠️ Failed to connect to backend. Make sure FastAPI is running.")
