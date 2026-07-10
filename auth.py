# auth.py - User Authentication Module

import hashlib
import re
from datetime import datetime

users_db = {}  # Simulated database: {email: {password_hash, name, created_at}}
login_attempts = {}  # Track failed logins: {email: count}

MAX_LOGIN_ATTEMPTS = 5

def hash_password(password: str) -> str:
    """Hash a password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(name: str, email: str, password: str) -> dict:
    """Register a new user."""
    if email in users_db:
        return {"success": False, "message": "Email already registered."}

    if len(password) < 6:
        return {"success": False, "message": "Password must be at least 6 characters."}

    users_db[email] = {
        "name": name,
        "password_hash": hash_password(password),
        "created_at": datetime.now().isoformat()
    }
    return {"success": True, "message": "Registration successful."}

def login_user(email: str, password: str) -> dict:
    """Login a user with email and password."""
    if email not in users_db:
        return {"success": False, "message": "User not found."}

    user = users_db[email]

    if hash_password(password) != user["password_hash"]:
        return {"success": False, "message": "Invalid password."}

    return {"success": True, "message": "Login successful.", "name": user["name"]}

def reset_password(email: str, new_password: str) -> dict:
    """Reset password for an existing user."""
    if email not in users_db:
        return {"success": False, "message": "User not found."}

    users_db[email]["password_hash"] = hash_password(new_password)
    return {"success": True, "message": "Password reset successful."}
