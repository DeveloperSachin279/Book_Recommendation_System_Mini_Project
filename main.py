"""
Main Module
Book Recommendation System
"""

from config import DATA_PATH

from src.data_loader import load_data
from src.validator import validate_data
from src.analytics import calculate_genre_summary
from src.visualization import generate_chart
from src.database import create_database, save_summary
from src.logger import log_info, log_error


def main():

    try:
        log_info("Application Started")

        # -----------------------------
        # Load Dataset
        # -----------------------------
        data = load_data(DATA_PATH)
        log_info("Dataset Loaded Successfully")

        # -----------------------------
        # Validate Dataset
        # -----------------------------
        data = validate_data(data)
        log_info("Dataset Validation Completed")

        # -----------------------------
        # Analytics
        # -----------------------------
        summary = calculate_genre_summary(data)
        log_info("Analytics Completed")

        # -----------------------------
        # Database
        # -----------------------------
        create_database()
        save_summary(summary)
        log_info("Summary Saved into Database")

        # -----------------------------
        # Visualization
        # -----------------------------
        generate_chart(summary)
        log_info("Visualization Generated Successfully")

        print("\nProject Executed Successfully.\n")

    except Exception as error:

        log_error(str(error))
        print(f"\nApplication Error : {error}")


if __name__ == "__main__":
    main()