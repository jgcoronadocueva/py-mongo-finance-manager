from app.models.Transaction import get_transactions

def monthly_summary(user_id):
    transactions = get_transactions(user_id)

    total = sum(t["amount"] for t in transactions)
    print(f"Monthly total spending: ${total}")