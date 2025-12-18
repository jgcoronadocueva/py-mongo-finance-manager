# app/models/User.py
from app.database.mongodb import get_db
from bson import ObjectId


def _users():
    db = get_db()
    return db["users"]


def create_user(username, password_hash, first_name, last_name, email):
    users = _users()

    return users.insert_one(
        {
            "username": username,
            "passwordHash": password_hash,
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    )


def get_user_by_username(username):
    users = _users()

    return users.find_one({"username": username})


def update_user(user_id, updates: dict):
    users = _users()

    result = users.update_one({"_id": ObjectId(user_id)}, {"$set": updates})
    return result.modified_count > 0


def delete_user(user_id):
    users = _users()

    result = users.delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count > 0
