"""
Visualization Module
Generates and saves the genre-wise average rating chart.
"""

import os
import matplotlib.pyplot as plt
from config import REPORT_PATH


def generate_chart(summary):
    """
    Generate professional bar chart for genre-wise average ratings.
    """

    try:
        # Create reports folder if it doesn't exist
        os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)

        plt.figure(figsize=(12, 7))

        # Create Bars
        bars = plt.bar(
            summary.index,
            summary.values,
            color="steelblue",
            edgecolor="black",
            linewidth=1.2
        )

        # Add Value Labels on Top
        for bar in bars:
            height = bar.get_height()

            plt.text(
                bar.get_x() + bar.get_width()/2,
                height + 0.03,
                f"{height:.2f}",
                ha='center',
                fontsize=10,
                fontweight='bold'
            )

        # Title
        plt.title(
            "Average Book Rating by Genre",
            fontsize=16,
            fontweight="bold",
            pad=15
        )

        # Axis Labels
        plt.xlabel("Book Genre", fontsize=12, fontweight="bold")
        plt.ylabel("Average Rating", fontsize=12, fontweight="bold")

        # Grid
        plt.grid(axis='y', linestyle='--', alpha=0.5)

        # Rotate Labels
        plt.xticks(rotation=35, ha="right")

        # Rating Scale
        plt.ylim(0, 5)

        # Save Chart
        plt.tight_layout()
        plt.savefig(REPORT_PATH, dpi=300)

        # Show Chart
        plt.show()

        print(f"Chart saved successfully at:\n{REPORT_PATH}")

    except Exception as e:
        print(f"Visualization Error: {e}")