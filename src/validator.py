"""
Validator Module
Validates and cleans the dataset.
"""

import pandas as pd


def validate_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validate dataset before analysis.

    Parameters:
        df (DataFrame)

    Returns:
        Clean DataFrame
    """

    required_columns = ["genre", "rating"]

    # Check required columns
    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing required column: {column}")

    # Remove missing values
    df = df.dropna(subset=["genre", "rating"])

    # Convert rating to numeric
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

    # Remove invalid ratings
    df = df.dropna(subset=["rating"])

    # Accept ratings only between 1 and 5
    df = df[(df["rating"] >= 1) & (df["rating"] <= 5)]

    # Remove duplicate rows
    df = df.drop_duplicates()

    print("Dataset validated successfully.")

    return df