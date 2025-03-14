from flask import Blueprint, request, jsonify

main = Blueprint("main", __name__)

@main.route("/")  # Homepage route
def home():
    return "Flask is running! Available API: /upload (POST), /match (POST)"

@main.route("/upload", methods=["POST"])  # Resume upload API (Already exists)
def upload_resume():
    return jsonify({"message": "Upload API is working!"})

@main.route("/match", methods=["POST"])  # ADD THIS: Resume Matching API
def match_resume():
    return jsonify({"message": "Match API is working!"})
