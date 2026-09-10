import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from scipy.stats import norm


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():

    rawDf = pd.read_csv("./output.csv")

    df = rawDf[["source_timestamp", "activity_raw_value"]].copy()

    df["source_timestamp"] = pd.to_datetime(df["source_timestamp"])

    # print("\nDuplicate rows:", df.duplicated().sum())

    df = df.drop_duplicates(keep="first").reset_index(drop=True)

    df = df.sort_values("source_timestamp").reset_index(drop=True)

    # df = df.head(500)

    # print(df)

    mean = 1.0273

    std = 0.013782

    lambda_value = 0.04


    l = 3

    prev_z = mean

    min_value = df["activity_raw_value"].min()

    max_value = df["activity_raw_value"].max()

    for t, data in enumerate(df["activity_raw_value"]):

        z = lambda_value * data + (1 - lambda_value) * prev_z

        sigma = std * np.sqrt(
            (lambda_value / (2 - lambda_value))
            * (1 - (1 - lambda_value) ** (2 * (t + 1)))
        )

        ucl = mean + l * sigma
        lcl = mean - l * sigma

        drift = z > ucl or z < lcl

        # Use t, not t - 1
        df.loc[t, "drift"] = drift

        # print(" ")
        # print(f"itration {t+1} ")
        # print(f"Z value {z} ")
        # print(f"Sigma value {sigma} ")
        # print(f"UCL {ucl} ")
        # print(f"LCL {lcl} ")
        # print(f"Drift {drift} ")
        # print(" ")

        prev_z = z

    plt.figure(figsize=(16, 6))

    x = range(len(df))
    y = df["activity_raw_value"]

    # True = red, False = blue
    point_colors = df["drift"].map({True: "red", False: "blue"})

    # Line
    plt.plot(x, y, alpha=0.5)

    # Points
    plt.scatter(x, y, c=point_colors, s=50, zorder=3)

    plt.xlabel("Time")
    plt.ylabel("Activity Raw Value")
    plt.title("Activity Raw Value Over Time")
    plt.axhline(min_value, linestyle="--", label=f"Min = {min_value}")
    plt.axhline(max_value, linestyle="--", label=f"Max = {max_value}")
    plt.axhline(mean, linestyle="--", label=f"Mean = {mean}")

    num_labels = 10

    step = max(len(df) // num_labels, 1)

    tick_positions = list(range(0, len(df), step))

    plt.xticks(
        tick_positions,
        df["source_timestamp"].iloc[tick_positions].dt.strftime("%Y-%m-%d %H:%M:%S"),
        rotation=45,
    )

    legend_items = [
        Patch(facecolor="none", edgecolor="none", label=f"Mean (μ): {mean}"),
        Patch(facecolor="none", edgecolor="none", label=f"Lambda (λ): {lambda_value}"),
        Patch(facecolor="none", edgecolor="none", label=f"L: {l}"),
    ]

    plt.legend(
        handles=legend_items,
        loc="upper left",
        frameon=True,
        fancybox=True,
        framealpha=0.9,
        edgecolor="black",
        handlelength=0,
        handletextpad=0,
    )

    plt.tight_layout()
    plt.show()


main()
