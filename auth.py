id="o1v3js"
import sqlite3


# Register user
def register_user(username, password):

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    try:

        cursor.execute(
            "INSERT INTO users(username, password) VALUES(?, ?)",
            (username, password)
        )

        conn.commit()

        print("User registered successfully!")

        conn.close()

        return True

    except sqlite3.IntegrityError:

        print("Username already exists!")

        conn.close()

        return False


# Login user
def login_user(username, password):

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    if user:

        print("Login successful!")

        return True

    else:

        print("Invalid username or password!")

        return False

