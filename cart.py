# cart.py - Shopping Cart Module

cart_db = {}  # {user_email: [{product_id, name, price, quantity}]}

def add_to_cart(user_email: str, product_id: str, name: str, price: float, quantity: int = 1) -> dict:
    """Add a product to user's cart."""
    if user_email not in cart_db:
        cart_db[user_email] = []

    cart = cart_db[user_email]

    # If product already in cart, increase quantity
    for item in cart:
        if item["product_id"] == product_id:
            item["quantity"] += quantity
            return {"success": True, "message": "Quantity updated.", "cart": cart}

    cart.append({
        "product_id": product_id,
        "name": name,
        "price": price,
        "quantity": quantity
    })
    return {"success": True, "message": "Item added to cart.", "cart": cart}

def remove_from_cart(user_email: str, product_id: str) -> dict:
    """Remove a product from user's cart."""
    if user_email not in cart_db:
        return {"success": False, "message": "Cart not found."}

    cart = cart_db[user_email]
    cart_db[user_email] = [i for i in cart if i["product_id"] != product_id]
    return {"success": True, "message": "Item removed.", "cart": cart_db[user_email]}

def get_cart_total(user_email: str) -> dict:
    """Calculate total price of items in cart."""
    if user_email not in cart_db:
        return {"total": 0.0, "items": []}

    cart = cart_db[user_email]
    total = sum(item["price"] * item["quantity"] for item in cart)
    return {"total": round(total, 2), "items": cart}
