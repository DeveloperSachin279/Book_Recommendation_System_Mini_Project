"""
Logger Module
"""

import logging
import os
from config import LOG_FILE

# Create logs directory if it doesn't exist
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def log_info(message):
    logging.info(message)


def log_error(message):
    logging.error(message)