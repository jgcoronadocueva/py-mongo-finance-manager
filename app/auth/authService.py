# app/auth/authService.py
import bcrypt
from app.models.User import create_user, get_user_by_username
from app.auth.jwt import create_token


def register(username, password, first_name, last_name, email):

    if get_user_by_username(username):
        print("Username already taken")
        return False

    password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    create_user(username, password_hash, first_name, last_name, email)
    print("Account created! Thanks for joining us")
    return True


def login(username, password):
    user = get_user_by_username(username)

    if not user:
        print("Username does not exist")
        return None

    if not bcrypt.checkpw(password.encode(), user["passwordHash"]):
        print("Invalid password")
        return None

    return create_token(user["_id"]), user["_id"]
