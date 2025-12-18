# app/config/settings.py
import os
from dotenv import load_dotenv

# Load values from .env into environment
load_dotenv()

ENV = os.getenv("ENV", "development")

JWT_SECRET = os.getenv("JWT_SECRET")
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")