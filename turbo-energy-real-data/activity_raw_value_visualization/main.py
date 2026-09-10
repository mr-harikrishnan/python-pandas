import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


def main():

    rawDf = pd.read_csv("./output.csv")

    df = rawDf[["source_timestamp", "activity_raw_value"]]

    df["source_timestamp"] = pd.to_datetime(df["source_timestamp"], errors="coerce")

    print(df["source_timestamp"].head(5))

    print("\nDuplicate rows:", df.duplicated().sum())

    print("Duplicate timestamps:", df["source_timestamp"].duplicated().sum())

    df = df.sort_values("source_timestamp").reset_index(drop=True)

    df = df.drop_duplicates(keep="first").reset_index(drop=True)

    print("\nFinal shape:", df.shape)
    print("Total rows:", len(df))

    # plt.figure(figsize=(16, 6))

    # plt.plot(df["source_timestamp"], df["activity_raw_value"], alpha=0.5)

    # plt.xlabel("Source Timestamp")
    # plt.ylabel("Activity Raw Value")
    # plt.title("Activity Raw Value Over Time")

    # plt.xticks(rotation=45)
    # plt.tight_layout()

    # plt.show()

    plt.figure(figsize=(16, 6))

    plt.plot(range(len(df)), df["activity_raw_value"], marker="o", alpha=0.7)

    plt.xlabel("Time")
    plt.ylabel("Activity Raw Value")
    plt.title("Activity Raw Value Over Time")

    num_labels = 10
    step = max(len(df) // num_labels, 1)

    plt.xticks(
        range(0, len(df), step),
        df["source_timestamp"].iloc[::step].dt.strftime("%Y-%m-%d %H:%M:%S"),
        rotation=45,
    )

    plt.tight_layout()
    plt.show()


main()
