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


def plot_distributions(pass_data, fail_data, column_name,inputDate):

    pass_xValues, pass_yValues, pass_mean = get_distribution_values(pass_data)

    fail_xValues, fail_yValues, fail_mean = get_distribution_values(fail_data)

    figure, axes = plt.subplots(1, 2, figsize=(16, 7))

    # ---------------- PASS ----------------

    axes[0].plot(pass_xValues, pass_yValues, linewidth=2)

    axes[0].axvline(
        pass_mean, linestyle="--", linewidth=2, label=f"Mean = {pass_mean:.2f}"
    )

    axes[0].set_title(f"{column_name} - Pass")

    axes[0].set_xlabel("Parameter Value")
    axes[0].set_ylabel("Probability Density")

    axes[0].legend()
    axes[0].grid(True, alpha=0.4)

    # ---------------- FAIL ----------------

    axes[1].plot(fail_xValues, fail_yValues, linewidth=2)

    axes[1].axvline(
        fail_mean, linestyle="--", linewidth=2, label=f"Mean = {fail_mean:.2f}"
    )

    axes[1].set_title(f"{column_name} - Fail")

    axes[1].set_xlabel("Parameter Value")
    axes[1].set_ylabel("Probability Density")

    axes[1].legend()
    axes[1].grid(True, alpha=0.4)

    # ---------------- TITLE ----------------

    figure.suptitle(f"{column_name} - Pass vs Fail Distribution - {inputDate}", fontsize=16)

    figure.subplots_adjust(left=0.08, right=0.97, top=0.88, bottom=0.10, wspace=0.25)

    plt.show()

    plt.close(figure)


def main():

    pass_folder_path = "./merged-pass-data/status_code-1001-dok_code-0-merged_CEMB_141E_141C_141A_141B_and_141D.csv"

    fail_folder_path = "./merged-fail-data/status_code-1011-dok_code-16-merged_CEMB_141E_141C_141A_141B_and_141D.csv"

    inputDate = "2026-06-03"
    column_name = "OEL_TEMPERATUR"

    date = pd.to_datetime(inputDate).date()

    pass_df = pd.read_csv(pass_folder_path, parse_dates=["DATUM"])

    fail_df = pd.read_csv(fail_folder_path, parse_dates=["DATUM"])

    # ---------------- PASS DATA ----------------

    pass_data = pass_df[pass_df["DATUM"].dt.date == date][column_name]


    # ---------------- FAIL DATA ----------------

    fail_data = fail_df[fail_df["DATUM"].dt.date == date][column_name]

    # ---------------- CONVERT TO FLOAT ----------------

    pass_data = (
        pass_data.astype(str)
        .str.strip()
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

    fail_data = (
        fail_data.astype(str)
        .str.strip()
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

    # ---------------- REMOVE INVALID VALUES ----------------

    pass_data = pass_data.dropna()
    fail_data = fail_data.dropna()

    print("PASS DATA COUNT:", len(pass_data))
    print("FAIL DATA COUNT:", len(fail_data))

    print(
        "=========================================================================================================================="
    )

    # ---------------- PLOT ----------------

    plot_distributions(pass_data, fail_data, column_name,inputDate)


main()
