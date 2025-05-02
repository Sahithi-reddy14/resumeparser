import streamlit as st
import requests
import tempfile
from file_utils import extract_text_from_pdf

# Title
st.title("AI Resume Matcher (BERT-Powered)")

# 📝 Resume Input
st.markdown("Paste Resume Text ")
resume_text_input = st.text_area("Resume Text", height=200, key="resume_input")

st.markdown("### 📎 Upload Resume File (PDF)")
resume_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"], key="resume_upload")

st.markdown("---")

#  Job Description Input
st.markdown("### Paste Job Description")
job_text_input = st.text_area("📄 Job Description Text", height=200, key="job_input")

st.markdown("### 📎 Upload Job Description File (PDF)")
job_file = st.file_uploader("Upload job description (PDF)", type=["pdf"], key="job_upload")

st.markdown("---")

#  Semantic Match Button
if st.button(" Semantic Match (BERT)"):
    # Load from text areas
    resume_text = resume_text_input.strip()
    job_text = job_text_input.strip()

    # If text is missing, try extracting from files
    if not resume_text and resume_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(resume_file.read())
            resume_text = extract_text_from_pdf(tmp.name)

    if not job_text and job_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(job_file.read())
            job_text = extract_text_from_pdf(tmp.name)

    # Validate final input
    if not resume_text or not job_text:
        st.error("❗ Please provide both resume and job description (via text or file).")
    else:
        # Send to BERT-based matcher
        payload = {
            "resume_text": resume_text,
            "job_description": job_text
        }

        response = requests.post("http://127.0.0.1:8000/semantic-match", json=payload)

        if response.status_code == 200:
            result = response.json()
            semantic_score = result.get("semantic_match_score", 0)
            skill_score = result.get("skill_match_score", 0)
            combined_score = result.get("combined_score", 0)

            st.markdown("### Match Scores")
            st.metric("🔍 Semantic Match:", f"{semantic_score}%")
            st.metric("🛠️ Skill Match:", f"{skill_score}%")
            st.success(f"✅ **Combined Score:** {combined_score}%")


            # Optional: Show detailed feedback if backend includes it
            if "matched_skills" in result:
                matched = result.get("matched_skills", [])
                missing = result.get("missing_skills", [])
                suggestions = result.get("suggestions", [])

                st.markdown(f"**🎯 Matched Skills:** {', '.join(matched) if matched else 'None'}")
                st.markdown(f"**❌ Missing Skills:** {', '.join(missing) if missing else 'None'}")

                if suggestions:
                    st.markdown("### 💡 Suggestions to Improve:")
                    for s in suggestions:
                        st.markdown(f"- {s}")
        else:
            st.error("🚫 Could not connect to the backend. Is FastAPI running?")
