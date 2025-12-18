# app/models/Transaction.py
from app.database.mongodb import get_db
from bson import ObjectId


def _transactions():
    return get_db()["transactions"]  # Reference to the "transactions" collection


def create_transaction(user_id, amount, category):
    """
    Insert a new transaction for a user into the database.
    """
    return _transactions().insert_one(
        {
            "userId": ObjectId(user_id),  # Link transaction to user
            "amount": amount,
            "category": category,
        }
    )


def get_transactions(user_id):
    """
    Retrieve all transactions for a specific user as a list.
    """
    return list(_transactions().find({"userId": ObjectId(user_id)}))


def update_transaction(transaction_id, updates: dict):
    """
    Update fields of a transaction.
    """
    result = _transactions().update_one(
        {"_id": ObjectId(transaction_id)}, {"$set": updates}
    )
    return result.modified_count > 0


def delete_transaction(transaction_id):
    """
    Delete a transaction by its ID.
    """
    result = _transactions().delete_one({"_id": ObjectId(transaction_id)})
    return result.deleted_count > 0
