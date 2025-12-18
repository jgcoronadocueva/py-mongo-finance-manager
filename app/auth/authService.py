# app/auth/authService.py
import bcrypt
from app.models.User import create_user, get_user_by_username
from app.auth.jwt import create_token


def register(username, password, first_name, last_name, email):
    """
    Register a new user with a hashed password.
    """
    # Check if username is already taken
    if get_user_by_username(username):
        print("Username already taken")
        return False

    # Hash the password
    password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    # Create the user in the database
    create_user(username, password_hash, first_name, last_name, email)
    print("Account created! Thanks for joining us")
    return True


def login(username, password):
    """
    Log in a user by verifying username and password.
    """
    # Get user from database
    user = get_user_by_username(username)

    # Check if username exists
    if not user:
        print("Username does not exist")
        return None

    # Check if password is correct
    if not bcrypt.checkpw(password.encode("utf-8"), user["passwordHash"]):
        print("Invalid password")
        return None

    # Return JWT token and user ID (tuple)
    return create_token(user["_id"]), user["_id"]
