# app/database/mongodb.py
from pymongo import MongoClient
from app.config.settings import MONGO_URI, DB_NAME

# Global private variable to store the MongoClient instance
_client = None


def connect_db():
    """
    Connect to MongoDB and return the database instance.
    Uses the global client to avoid multiple connections.
    """
    global _client

    # If already connected, return the existing database instance
    if _client:
        return _client[DB_NAME]

    # Create a new MongoDB client
    _client = MongoClient(MONGO_URI)

    # Ensure connection is alive
    _client.admin.command("ping")
    print("MongoDB connected")

    # Return the database instance
    return _client[DB_NAME]


def get_db():
    """
    Get the MongoDB database instance.
    """
    return connect_db()
