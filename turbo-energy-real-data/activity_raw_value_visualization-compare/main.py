import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from scipy.stats import norm


def main():

    rawDf = pd.read_csv("./clickhouse_drift_calculation_computed.csv")

    df = rawDf[["source_timestamp", "activity_value", "mean","drift"]].copy()

    mean = 1.027288

    df["source_timestamp"] = pd.to_datetime(df["source_timestamp"])

    df = df.drop_duplicates(keep="first").reset_index(drop=True)

    df = df.sort_values("source_timestamp").reset_index(drop=True)

    plt.figure(figsize=(16, 6))

    x = range(len(df))
    y = df["activity_value"]

    # True = red, False = blue
    point_colors = df["drift"].map({1: "red", 0: "blue"})

    # Line
    plt.plot(x, y, alpha=0.5)

    # Points
    plt.scatter(x, y, c=point_colors, s=50, zorder=3)

    plt.xlabel("Time")
    plt.ylabel("Activity Raw Value")
    plt.title("Activity Raw Value Over Time")
    plt.axhline(mean, linestyle="--", label=f"Mean = {mean}")

    num_labels = 10

    step = max(len(df) // num_labels, 1)

    tick_positions = list(range(0, len(df), step))

    plt.xticks(
        tick_positions,
        df["source_timestamp"].iloc[tick_positions].dt.strftime("%Y-%m-%d %H:%M:%S"),
        rotation=45,
    )

    plt.tight_layout()
    plt.show()


main()
