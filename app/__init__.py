from flask import Flask
from .routes import router  # ✅ Correct import

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes)  # Register routes
    return app
