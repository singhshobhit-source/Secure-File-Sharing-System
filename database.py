
import sqlite3


# ================= CREATE DATABASE =================
def create_database():

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # Files table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS files(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        encrypted_filename TEXT
    )
    """)

    conn.commit()
    conn.close()


create_database()


# ================= REGISTER USER =================
def register_user(username, password):

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    try:

        cursor.execute(
            "INSERT INTO users(username, password) VALUES(?, ?)",
            (username, password)
        )

        conn.commit()
        conn.close()

        return True

    except:

        conn.close()

        return False


# ================= LOGIN USER =================
def login_user(username, password):

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    return user


# ================= SAVE FILE =================
def save_file(filename, encrypted_filename):

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO files(filename, encrypted_filename) VALUES(?, ?)",
        (filename, encrypted_filename)
    )

    conn.commit()
    conn.close()

    print("File information saved.")


# ================= GET FILES =================
def get_files():

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT filename, encrypted_filename FROM files"
    )

    files = cursor.fetchall()

    conn.close()

    return files


# ================= GET ENCRYPTED FILES =================
def get_encrypted_files():

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT encrypted_filename FROM files"
    )

    files = cursor.fetchall()

    conn.close()

    return files


# ================= DELETE FILE =================
def delete_latest_file():

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT encrypted_filename FROM files ORDER BY id DESC LIMIT 1"
    )

    file = cursor.fetchone()

    if file:

        cursor.execute(
            "DELETE FROM files WHERE encrypted_filename=?",
            (file[0],)
        )

    conn.commit()
    conn.close()

    return file


# ================= TOTAL FILES =================
def get_total_files():

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM files"
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total

