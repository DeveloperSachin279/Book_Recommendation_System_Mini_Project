"""
Configuration file for Book Recommendation System
"""

import os

# Base Directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Data
DATA_PATH = os.path.join(BASE_DIR, "data", "book_data.csv")

# Database
DATABASE_PATH = os.path.join(BASE_DIR, "database", "books.db")

# Reports
REPORT_PATH = os.path.join(BASE_DIR, "reports", "genre_rating.png")

# Log File
LOG_FILE = os.path.join(BASE_DIR, "logs", "app.log")