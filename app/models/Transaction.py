# app/models/Transaction.py
from app.database.mongodb import get_db
from bson import ObjectId

def _transactions():
    return get_db()["transactions"]

# CREATE (Insert)
def add_transaction(user_id, amount, category):
    return _transactions().insert_one({
        "userId": ObjectId(user_id),
        "amount": amount,
        "category": category
    })

# READ (Retrieve / Query)
def get_transactions(user_id):
    return list(_transactions().find({"userId": ObjectId(user_id)}))

# UPDATE (Modify)
def update_transaction(transaction_id, amount=None, category=None):
    updates = {}

    if amount is not None:
        updates["amount"] = amount
    if category is not None:
        updates["category"] = category

    if not updates:
        return False

    result = _transactions().update_one(
        {"_id": ObjectId(transaction_id)},
        {"$set": updates}
    )
    return result.modified_count > 0

# DELETE
def delete_transaction(transaction_id):
    result = _transactions().delete_one(
        {"_id": ObjectId(transaction_id)}
    )
    return result.deleted_count > 0