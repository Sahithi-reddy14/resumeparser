from fastapi import FastAPI
from pydantic import BaseModel
from app.predict import predict_resume, compare_skills
from app.matcher import compare_skills
from app.schemas import MatchRequest


from app.routes import router  # 🧠 This will now work

app = FastAPI()
app.include_router(router)     # ✅ This registers your routes

app = FastAPI(title="Resume Parser API")

# Request schema
class ResumeInput(BaseModel):
    resume_text: str

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

