from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    # Other configurations...

    # Apply CORS to the app
    CORS(app)

    # Import and register blueprints
    from .views import main
    app.register_blueprint(main)

    return app