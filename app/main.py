from fastapi import FastAPI
from pydantic import BaseModel

from app.matcher import compare_skills
from app.schemas import MatchRequest
from app.bert_matcher import semantic_match
from pydantic import BaseModel
from app.routes import router  # 🧠 This will now work

app = FastAPI()
app.include_router(router)     # ✅ This registers your routes

app = FastAPI(title="Resume Parser API")

# Request schema
class ResumeInput(BaseModel):
    resume_text: str

class SemanticMatchRequest(BaseModel):
    resume_text: str
    job_description: str
 
# Welcome route
@app.get("/")
def read_root():
    return {"message": "Welcome to Resume Parser API!"}

# Request schema for matching skills
class MatchRequest(BaseModel):
    resume_text: str
    job_description: str

# Prediction route
@app.post("/predict")
def predict(input: ResumeInput):
    result = predict_resume(input.resume_text)
    return {"prediction": result}

@app.post("/match")
def match_skills(data: MatchRequest):
    result = compare_skills(data.resume_text, data.job_description)
    return result



@app.post("/semantic-match")
def match_semantically(data: SemanticMatchRequest):
    # Semantic match using BERT
    semantic_score = semantic_match(data.resume_text, data.job_description)

    # Skill match
    skill_result = compare_skills(data.resume_text, data.job_description)
    skill_score = skill_result["match_percentage"]

    # Combine scores (adjust weights as needed)
    final_score = round((0.7 * semantic_score + 0.3 * skill_score), 2)

    return {
        "semantic_match_score": semantic_score,
        "skill_match_score": skill_score,
        "combined_score": final_score,
        "matched_skills": skill_result["matched_skills"],
        "missing_skills": skill_result["missing_skills"],
        "suggestions": skill_result["suggestions"]
    }
