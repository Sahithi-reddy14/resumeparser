
import streamlit as st
from PIL import Image

#Page Setup
st.set_page_config(
    page_title="Smart Resume Parser",
    page_icon="📝",
    layout="centered"
)

#CSS
st.markdown("""
    <style>
        .main {
            background-color: #f7f9fc;
            font-family: 'Segoe UI', sans-serif;
        }
        h1 {
            color: #2c3e50;
        }
        .stTextArea label, .stFileUploader label {
            font-weight: 600;
            color: #2c3e50;
        }
        .css-1aumxhk {
            background-color: #ecf0f1;
            border-radius: 10px;
            padding: 1rem;
        }
        .stButton button {
            background-color: #3498db;
            color: white;
            border-radius: 8px;
            padding: 0.5rem 1.5rem;
            font-weight: bold;
            border: none;
        }
        .stButton button:hover {
            background-color: #2980b9;
        }
    </style>
""", unsafe_allow_html=True)

#App Title
st.title("📄 Smart Resume Parser")

st.subheader("Optimize your resume to match job descriptions and beat the ATS!")

#Inputs
job_description = st.text_area("🔍 Job Description", height=200, placeholder="Paste the job description here...")

uploaded_resume = st.file_uploader("📎 Upload Your Resume (PDF/Text)", type=["pdf", "txt"])

or_resume_text = st.text_area("📝 Or Paste Your Resume Here", height=200, placeholder="Paste your resume text here...")

#Analyze Button
if st.button("🔍 Analyze Resume"):
    if not job_description:
        st.warning("Please enter a job description.")
    elif not uploaded_resume and not or_resume_text:
        st.warning("Please upload or paste your resume.")
    else:
        # Placeholder analysis result
        st.success("✅ Resume analyzed successfully!")
        st.markdown("### 🔧 Suggestions:")
        st.write("- Add more role-specific keywords from the job description.")
        st.write("- Highlight relevant technical and soft skills.")
        st.write("- Quantify achievements with metrics if possible.")
        st.write("- Tailor your professional summary to match the job.")

# ---------- Footer ----------
st.markdown("---")
st.markdown("<center><small>Built by Team 19</small></center>", unsafe_allow_html=True)
