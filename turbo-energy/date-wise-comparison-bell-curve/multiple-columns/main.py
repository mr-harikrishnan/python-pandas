import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm


def get_distribution_values(series):

    mean = np.mean(series)
    standardDeviation = np.std(series)

    minValue = series.min()
    maxValue = series.max()

    xValues = np.linspace(minValue, maxValue, 1000)

    yValues = norm.pdf(xValues, loc=mean, scale=standardDeviation)

    return xValues, yValues, mean


def convert_to_float(series):

    return (
        series.astype(str)
        .str.strip()
        .str.replace(",", ".", regex=False)
        .astype(float)
        .dropna()
    )


def plot_distributions(pass_data, fail_data, columns, inputDate):

    maximumColumnsPerFigure = 7

    for i in range(0, len(columns), maximumColumnsPerFigure):

        currentColumns = columns[i : i + maximumColumnsPerFigure]

        figure, axes = plt.subplots(len(currentColumns), 2, figsize=(16, 32))

        # Make axes always 2D
        axes = np.atleast_2d(axes)

        for row in range(len(currentColumns)):

            column = currentColumns[row]

            currentPassData = pass_data[column]

            pass_xValues, pass_yValues, pass_mean = get_distribution_values(
                currentPassData
            )

            axes[row, 0].plot(pass_xValues, pass_yValues, linewidth=2)

            axes[row, 0].axvline(
                pass_mean, linestyle="--", linewidth=2, label=f"Mean = {pass_mean:.2f}"
            )

            axes[row, 0].set_title(f"{column} - Pass")

            axes[row, 0].legend()
            axes[row, 0].grid(True, alpha=0.4)

            currentFailData = fail_data[column]

            fail_xValues, fail_yValues, fail_mean = get_distribution_values(
                currentFailData
            )

            axes[row, 1].plot(fail_xValues, fail_yValues, linewidth=2)

            axes[row, 1].axvline(
                fail_mean, linestyle="--", linewidth=2, label=f"Mean = {fail_mean:.2f}"
            )

            axes[row, 1].set_title(f"{column} - Fail")

            axes[row, 1].legend()
            axes[row, 1].grid(True, alpha=0.4)

        figure.supxlabel("Parameter Value")
        figure.supylabel("Probability Density")

        figure.suptitle(f"Pass vs Fail Distribution - {inputDate}", fontsize=16)

        figure.subplots_adjust(
            left=0.08, right=0.97, top=0.91, bottom=0.06, hspace=1.0, wspace=0.25
        )

        figureNumber = (i // maximumColumnsPerFigure) + 1

        outputFileName = f"distribution_{figureNumber:02d}.png"

        figure.savefig(outputFileName, dpi=300, bbox_inches="tight")

        plt.show()

        plt.close(figure)

        print(f"Created: {outputFileName}")


def main():

    pass_folder_path = (
        "./merged-pass-data/"
        "status_code-1001-dok_code-0-"
        "merged_CEMB_141E_141C_141A_141B_and_141D.csv"
    )

    fail_folder_path = (
        "./merged-fail-data/"
        "status_code-1011-dok_code-16-"
        "merged_CEMB_141E_141C_141A_141B_and_141D.csv"
    )

    inputDate = "2026-06-03"

    columns = [
        "MD1_ANLIEF_MG",
        "MD1_AUSLIEF_MG",
        "MD2_ANLIEF_MG",
        "MD2_AUSLIEF_MG",
        "MD3_ANLIEF_MG",
        "MD3_AUSLIEF_MG",
        "EB1_ANLIEF_MG",
        "EB1_AUSLIEF_MG",
        "OEL_DURCHFLUSS",
        "OEL_DRUCK",
        "OEL_TEMPERATUR",
        "PF_TORQUE",
        "SPANN_DRUCK",
        "Val_Pressure_Bhsg",
        "Val_Pressure_CS",
    ]

    date = pd.to_datetime(inputDate).date()

    pass_df = pd.read_csv(pass_folder_path, parse_dates=["DATUM"])

    fail_df = pd.read_csv(fail_folder_path, parse_dates=["DATUM"])

    pass_df = pass_df[pass_df["DATUM"].dt.date == date]

    fail_df = fail_df[fail_df["DATUM"].dt.date == date]

    pass_data = {}
    fail_data = {}

    for column in columns:

        pass_data[column] = convert_to_float(pass_df[column])

        fail_data[column] = convert_to_float(fail_df[column])

        print(
            f"{column} - "
            f"Pass Count: {len(pass_data[column])}, "
            f"Fail Count: {len(fail_data[column])}"
        )

    plot_distributions(pass_data, fail_data, columns, inputDate)


main()
