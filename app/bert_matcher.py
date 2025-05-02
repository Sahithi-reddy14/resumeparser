

# app/bert_matcher.py
from sentence_transformers import SentenceTransformer, util
import re

# Load a small but powerful model
model = SentenceTransformer('all-MiniLM-L6-v2')

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text.strip()

def semantic_match(resume_text, job_description):
    # Preprocess inputs
    resume_text_clean = clean_text(resume_text)
    job_description_clean = clean_text(job_description)

    # Batch encode
    embeddings = model.encode([resume_text_clean, job_description_clean], convert_to_tensor=True)

    # Compute cosine similarity
    similarity = util.cos_sim(embeddings[0], embeddings[1])

    # Return percentage score
    return round(float(similarity.item()) * 100, 2)

