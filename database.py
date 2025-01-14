import sqlite3

def connect():
    conn = sqlite3.connect('UserData.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Email TEXT NOT NULL,
        User TEXT NOT NULL,
        Password TEXT NOT NULL
    );
    """)
    conn.commit()
    return conn, cursor

def close(conn):
    conn.close()
