# file database.py

import sqlite3
import hashlib
from datetime import datetime

def init_db():
    """Initialize the database and create tables."""
    conn = sqlite3.connect('portal.db')
    cursor = conn.cursor()

    # Messages table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Comments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Database initialized successfully!")

def add_message(name, email, message):
    """Add a new message to the database."""
    conn = sqlite3.connect('portal.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO user_messages (name, email, message)
        VALUES (?, ?, ?)
    ''', (name, email, message))
    conn.commit()
    conn.close()

def get_all_messages():
    """Retrieve all messages from the database."""
    conn = sqlite3.connect('portal.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, name, email, message, timestamp
        FROM user_messages
        ORDER BY timestamp DESC
    ''')
    messages = cursor.fetchall()
    conn.close()
    return messages

def register_user(username, password):
    """Add a new user with hashed password to the database."""
    conn = sqlite3.connect('portal.db')
    cursor = conn.cursor()

    password_hash = hashlib.sha256(password.encode()).hexdigest()

    try:
        cursor.execute('''
            INSERT INTO users (username, password_hash)
            VALUES (?, ?)
        ''', (username, password_hash))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def verify_user(username, password):
    """Verify user login by checking password hash."""
    conn = sqlite3.connect('portal.db')
    cursor = conn.cursor()

    cursor.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()
    conn.close()

    if result:
        stored_hash = result[0]
        return hashlib.sha256(password.encode()).hexdigest() == stored_hash
    return False

if __name__ == '__main__':
    init_db()

