# app/__init__.py
from flask import Flask
from openai import OpenAI
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)

    # Load environment variables from .env file
    load_dotenv()

    # Load the OpenAI API key from environment variables
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    client = OpenAI(api_key=OPENAI_API_KEY)

    # Register blueprints or routes
    from app.routes import main
    app.register_blueprint(main)

    return app, client
