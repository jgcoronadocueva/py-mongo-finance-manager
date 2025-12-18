# app/models/Category.py
from app.database.mongodb import get_db
from bson import ObjectId

db = get_db()
categories = db["categories"]


def create_category(user_id, name, category_type):
    categories.insert_one(
        {"userId": ObjectId(user_id), "name": name, "type": category_type}
    )


def get_categories(user_id):
    return list(categories.find({"userId": ObjectId(user_id)}))
