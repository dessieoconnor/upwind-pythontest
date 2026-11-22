
import sqlite3

def find_user(username):
    with sqlite3.connect(":memory:") as conn:
        conn.execute(
            "CREATE TABLE users (username TEXT)"
        )
        cursor = conn.execute(
            "SELECT username FROM users WHERE username = ?",
            (username,)
        )
        return cursor.fetchall()
