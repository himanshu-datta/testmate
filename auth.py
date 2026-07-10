# CHANGE 1: login_user function — add lockout logic

# OLD version (what's currently in the file):
def login_user(email: str, password: str) -> dict:
    if email not in users_db:
        return {"success": False, "message": "User not found."}

    user = users_db[email]

    if hash_password(password) != user["password_hash"]:
        return {"success": False, "message": "Invalid password."}

    return {"success": True, "message": "Login successful.", "name": user["name"]}

# NEW version (what you change it to in the PR):
def login_user(email: str, password: str) -> dict:
    if email not in users_db:
        return {"success": False, "message": "User not found."}

    # NEW: Check if account is locked
    attempts = login_attempts.get(email, 0)
    if attempts >= MAX_LOGIN_ATTEMPTS:
        return {"success": False, "message": "Account locked. Too many failed attempts."}

    user = users_db[email]

    if hash_password(password) != user["password_hash"]:
        # NEW: Track failed attempts
        login_attempts[email] = attempts + 1
        remaining = MAX_LOGIN_ATTEMPTS - login_attempts[email]
        return {"success": False, "message": f"Invalid password. {remaining} attempts remaining."}

    # NEW: Reset attempts on successful login
    login_attempts[email] = 0
    return {"success": True, "message": "Login successful.", "name": user["name"]}
