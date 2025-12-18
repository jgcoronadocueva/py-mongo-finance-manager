# Overview

This project is a Personal Finance Manager designed to help users track and manage their expenses, budgets, and financial categories. The software allows users to create accounts, log in securely, add income or expense transactions, and set spending limits by category.

The program integrates with MongoDB Atlas to securely store user data, categories, budgets, and transactions. Users interact with the program via a command-line interface that shows a menu with multiple options.

How to use the program:

- Run `pip install -r requirements.txt` from your terminal to get all required libraries.
- Run the main script from your terminal: `python main.py`
- Register an account with a username, password, and personal info.
- Log in to receive a JWT token for authentication.
- Add, view, edit, or delete transactions linked to categories.
- Log out to invalidate the current session.

The purpose of this program was to learn how to use MongoDB with Python, continue improving my skills with cloud databases and securely managing user data in a cloud environment.

[Personal Finance Manager in Python tutorial](https://youtu.be/X8x9oYkDviE)

# Cloud Database

This project uses MongoDB Atlas, a cloud-hosted NoSQL database service.

**Database Structure:**

users – stores registered user accounts:

- username, passwordHash, firstName, lastName, email

categories – stores financial categories per user:

- userId, name, type

budgets – stores spending limits per category:

- userId, category, limit

transactions – stores all user transactions:

- userId, amount, category

**Note:** All collections are linked to a user via userId, making it easy to query data per user.

# Development Environment

**Programming Language:** Python 3.14

**Libraries:**

- `pymongo` for MongoDB interactions
- `bcrypt` for hashing passwords
- `jwt` for creating and verifying authentication tokens
- `python`-dotenv for environment variable management
- `bson` for handling MongoDB ObjectId

**Tools:**

- IDE: Visual Studio Code
- Database: MongoDB Atlas

# Useful Websites

- [How to Create and Use .env Files in Python](https://www.geeksforgeeks.org/python/how-to-create-and-use-env-files-in-python/)
- [Connecting MongoDB to Python](https://www.datacamp.com/de/tutorial/connecting-mongodb-to-python)
- [Hashing Passwords in Python with BCrypt](https://www.geeksforgeeks.org/python/hashing-passwords-in-python-with-bcrypt/)
- [Understanding JWT: A Beginner-Friendly Guide with Python](https://maazbinmustaqeem.medium.com/understanding-jwt-a-beginner-friendly-guide-with-python-71b29953f3ab)
- [Python and MongoDB: Connecting to NoSQL Databases](https://realpython.com/introduction-to-mongodb-and-python/)
- [PyMongo Driver - MongoDB Docs](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/crud/)

# Future Work

- Expand to a REST or GraphQL API
- Implement role-based access control
- Improve error handling and validation
- Include reports and visualizations