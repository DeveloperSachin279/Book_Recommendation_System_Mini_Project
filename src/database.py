"""
Database Module
Stores Analytics Summary in SQLite
"""

import sqlite3
from config import DATABASE_PATH
import os

# Create database directory if needed
os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)


def create_database():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS genre_summary(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            genre TEXT,
            average_rating REAL
        )
    """)

    conn.commit()
    conn.close()


def save_summary(summary):

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM genre_summary")

    for genre, rating in summary.items():
        cursor.execute(
            "INSERT INTO genre_summary(genre, average_rating) VALUES (?, ?)",
            (genre, float(rating))
        )

    conn.commit()
    conn.close()