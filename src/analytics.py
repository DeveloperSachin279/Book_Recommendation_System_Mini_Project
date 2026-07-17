"""
Analytics Module
Performs descriptive analytics.
"""

import pandas as pd


def calculate_genre_summary(df: pd.DataFrame) -> pd.Series:
    """
    Calculate average rating by genre.

    Parameters:
        df (DataFrame)

    Returns:
        Genre-wise average ratings
    """

    genre_summary = (
        df.groupby("genre")["rating"]
        .mean()
        .sort_values(ascending=False)
    )

    print("Analytics completed successfully.")

    return genre_summary