import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


def get_distribution_values(series):

    mean = np.mean(series)
    standardDeviation = np.std(series)

    minValue = series.min()
    maxValue = series.max()

    xValues = np.linspace(minValue, maxValue, 1000)

    yValues = norm.pdf(xValues, loc=mean, scale=standardDeviation)

    return xValues, yValues, mean


def create_distribution_dataframes(df, columns):

    distributionDataFrames = {}

    for column in columns:

        xValues, yValues, mean = get_distribution_values(df[column])

        distributionDataFrames[column] = {
            "data": pd.DataFrame(
                {"X": np.round(xValues, 4), "Y": np.round(yValues, 10)}
            ),
            "mean": mean,
        }

    return distributionDataFrames


def plot_distributions(passDistributionDataFrames, failDistributionDataFrames, columns):

    figure, axes = plt.subplots(len(columns), 2, figsize=(16, 32))

    for row, column in enumerate(columns):

        # ---------------- PASS ----------------

        passDataFrame = passDistributionDataFrames[column]["data"]
        passMean = passDistributionDataFrames[column]["mean"]

        axes[row, 0].plot(passDataFrame["X"], passDataFrame["Y"], linewidth=2)

        axes[row, 0].axvline(
            passMean, linestyle="--", linewidth=2, label=f"Mean = {passMean:.2f}"
        )

        axes[row, 0].set_title(f"{column} - Pass", fontsize=12, pad=8)

        axes[row, 0].legend(loc="upper right", fontsize=9)

        axes[row, 0].grid(True, alpha=0.4)

        # ---------------- FAIL ----------------

        failDataFrame = failDistributionDataFrames[column]["data"]
        failMean = failDistributionDataFrames[column]["mean"]

        axes[row, 1].plot(failDataFrame["X"], failDataFrame["Y"], linewidth=2)

        axes[row, 1].axvline(
            failMean, linestyle="--", linewidth=2, label=f"Mean = {failMean:.2f}"
        )

        axes[row, 1].set_title(f"{column} - Fail", fontsize=12, pad=8)

        axes[row, 1].legend(loc="upper right", fontsize=9)

        axes[row, 1].grid(True, alpha=0.4)

    # Common X/Y labels
    figure.supxlabel("Parameter Value", fontsize=13)

    figure.supylabel("Probability Density", fontsize=13)

    figure.subplots_adjust(
        left=0.08, right=0.97, top=0.95, bottom=0.04, hspace=1.0, wspace=0.25,
    )

    plt.show()


def main():

    pass_df = pd.read_csv("./pass-01001-0_merged_CEMB_141E_141C_141A_141B_and_141D.csv")

    fail_df = pd.read_csv("./fail-1011-16_merged_CEMB_141E_141C_141A_141B_and_141D.csv")

    columns = [
        "OEL_TEMPERATUR",
        "MD1_ANLIEF_MG",
        "MD1_AUSLIEF_MG",
        "MD2_ANLIEF_MG",
        "MD2_AUSLIEF_MG",
        "MD3_ANLIEF_MG",
        "MD3_AUSLIEF_MG",
    ]

    pass_df = pass_df[columns].apply(
        lambda x: x.str.replace(",", ".", regex=False).astype(float)
    )

    fail_df = fail_df[columns].apply(
        lambda x: x.str.replace(",", ".", regex=False).astype(float)
    )

    passDistributionDataFrames = create_distribution_dataframes(pass_df, columns)

    failDistributionDataFrames = create_distribution_dataframes(fail_df, columns)

    plot_distributions(passDistributionDataFrames, failDistributionDataFrames, columns)


main()
