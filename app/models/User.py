# app/models/User.py
from app.database.mongodb import get_db
from bson import ObjectId


def _users():
    return get_db()["users"]  # Reference to the "users" collection


def create_user(username, password_hash, first_name, last_name, email):
    """
    Insert a new user into the database.
    """
    return _users().insert_one(
        {
            "username": username,
            "passwordHash": password_hash,
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    )


def get_user_by_username(username):
    """
    Retrieve a single user by their username.
    """
    return _users().find_one({"username": username})


def update_user(user_id, updates: dict):
    """
    Update fields of a user by their ID.
    """
    result = _users().update_one({"_id": ObjectId(user_id)}, {"$set": updates})
    return result.modified_count > 0


def delete_user(user_id):
    """
    Delete a user by their ID.
    """
    result = _users().delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count > 0
