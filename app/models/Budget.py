# app/models/Budget.py
from app.database.mongodb import get_db
from bson import ObjectId


def _budgets():
    return get_db()["budgets"]  # Reference to the "budgets" collection


def set_budget(user_id, category, limit_amount):
    """
    Set or update the budget limit for a specific category of a user.
    """
    _budgets().update_one(
        {"userId": ObjectId(user_id), "category": category},
        {"$set": {"limit_amount": limit_amount}},
        upsert=True,  # If the category doesn't exist, it will be created
    )


def get_budgets(user_id):
    """
    Retrieve all budget limits for a specific user.
    """
    return list(_budgets().find({"userId": ObjectId(user_id)}))
