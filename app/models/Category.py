# app/models/Category.py
from app.database.mongodb import get_db
from bson import ObjectId


def _categories():
    return get_db()["categories"]  # Reference to the "categories" collection


def create_category(user_id, name, category_type):
    """
    Insert a new category for a user into the database
    """
    return _categories().insert_one(
        {
            "userId": ObjectId(user_id),  # Link category to user
            "name": name,
            "type": category_type,
        }
    )


def get_categories(user_id):
    """
    Retrieve all categories for a specific user as a list.
    """
    return list(_categories().find({"userId": ObjectId(user_id)}))
