# app/database/mongodb.py
from pymongo import MongoClient
from app.config.settings import MONGO_URI, DB_NAME

_client = None

def connect_db():
    global _client

    if _client:
        return _client[DB_NAME]

    _client = MongoClient(MONGO_URI)

    # Ensure connection is alive
    _client.admin.command("ping")
    print("MongoDB connected")
    return _client[DB_NAME]


def get_db():
    return connect_db()