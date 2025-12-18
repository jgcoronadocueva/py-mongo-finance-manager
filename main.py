from app.database.mongodb import connect_db
from app.menu import run_menu


def main():
    """
    Connect to the database and run the main CLI menu.
    """
    try:
        connect_db()
        print("Database connected")
    except Exception as e:
        print("Database unavailable:", e)
        return

    # Display the CLI menu
    run_menu()


if __name__ == "__main__":
    main()
