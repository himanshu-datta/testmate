# payments.py - Payment Processing Module

from datetime import datetime

transactions = []  # List of all transactions

def process_payment(user_email: str, amount: float, card_number: str, cart_items: list) -> dict:
    """Process a payment for the given amount."""
    if amount <= 0:
        return {"success": False, "message": "Payment amount must be greater than zero."}

    if len(card_number) != 16 or not card_number.isdigit():
        return {"success": False, "message": "Invalid card number."}

    # Simulate payment gateway
    transaction = {
        "transaction_id": f"TXN{len(transactions)+1:05d}",
        "user_email": user_email,
        "amount": amount,
        "status": "success",
        "items": cart_items,
        "timestamp": datetime.now().isoformat()
    }
    transactions.append(transaction)

    return {
        "success": True,
        "transaction_id": transaction["transaction_id"],
        "message": f"Payment of ${amount} successful."
    }

def get_transaction_history(user_email: str) -> list:
    """Get all transactions for a user."""
    return [t for t in transactions if t["user_email"] == user_email]

def refund_transaction(transaction_id: str) -> dict:
    """Refund a transaction."""
    for t in transactions:
        if t["transaction_id"] == transaction_id:
            if t["status"] == "refunded":
                return {"success": False, "message": "Already refunded."}
            t["status"] = "refunded"
            return {"success": True, "message": f"Transaction {transaction_id} refunded."}

    return {"success": False, "message": "Transaction not found."}
