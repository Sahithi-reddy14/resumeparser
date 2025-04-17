from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
def hello():
    return {"message": "This is from routes.py"}
