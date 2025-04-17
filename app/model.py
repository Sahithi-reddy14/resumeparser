import joblib

model = joblib.load("models/resume_classifier.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

def get_model():
    return model, vectorizer

