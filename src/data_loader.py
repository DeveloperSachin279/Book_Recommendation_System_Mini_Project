"""
Data Loader Module
Reads CSV file and returns Pandas DataFrame
"""

import pandas as pd
import os


def load_data(file_path):
    """
    Load CSV dataset.

    Parameters:
        file_path (str): Path of CSV file.

    Returns:
        pandas.DataFrame
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file not found: {file_path}")

    try:
        data = pd.read_csv(file_path)

        if data.empty:
            raise ValueError("CSV file is empty.")

        print("Dataset loaded successfully.")
        return data

    except Exception as error:
        raise Exception(f"Error while loading dataset: {error}")