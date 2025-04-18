# app/bert_matcher.py
from sentence_transformers import SentenceTransformer, util

# Load a small but powerful model
model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_match(resume_text, job_description):
    # Get BERT embeddings
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_embedding = model.encode(job_description, convert_to_tensor=True)

    # Compute cosine similarity
    similarity = util.cos_sim(resume_embedding, job_embedding)

    # Return percentage score
    return round(float(similarity.item()) * 100, 2)
