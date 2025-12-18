# app/models/Budget.py
from app.database.mongodb import get_db
from bson import ObjectId

db = get_db()
budgets = db["budgets"]

def set_budget(user_id, category, limit_amount):
    budgets.update_one(
        {"userId": ObjectId(user_id), "category": category},
        {"$set": {"limit": limit_amount}},
        upsert=True
    )

def get_budgets(user_id):
    return list(budgets.find({"userId": ObjectId(user_id)}))