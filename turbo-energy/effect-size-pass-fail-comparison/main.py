import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np


def getDistributionValues(series):

    mean = series.mean()
    standardDeviation = series.std(ddof=1)

    minValue = series.min()
    maxValue = series.max()

    xValues = np.linspace(minValue, maxValue, 1000)

    yValues = norm.pdf(xValues, loc=mean, scale=standardDeviation)

    return xValues, yValues, mean


def createDistributionDataFrames(df, columns):

    distributionDataFrames = {}

    for column in columns:

        xValues, yValues, mean = getDistributionValues(df[column])

        distributionDataFrames[column] = {
            "data": pd.DataFrame(
                {"X": np.round(xValues, 4), "Y": np.round(yValues, 10)}
            ),
            "mean": mean,
        }

    return distributionDataFrames


def plotDistributions(
    passDistributionDataFrames, failDistributionDataFrames, columns, fileName
):

    fileNameWithoutExtension = os.path.splitext(os.path.basename(fileName))[0]

    outputFolder = f"./distribution_plots/{fileNameWithoutExtension}"

    os.makedirs(outputFolder, exist_ok=True)

    for i in range(0, len(columns), 7):

        currentColumns = columns[i : i + 7]

        figure, axes = plt.subplots(len(currentColumns), 2, figsize=(16, 32))

        # If there is only one column,
        # axes will not be 2-dimensional.
        if len(currentColumns) == 1:
            axes = np.array([axes])

        for row, column in enumerate(currentColumns):

            # Pass
            passDataFrame = passDistributionDataFrames[column]["data"]
            passMean = passDistributionDataFrames[column]["mean"]

            axes[row, 0].plot(passDataFrame["X"], passDataFrame["Y"], linewidth=2)

            axes[row, 0].axvline(
                passMean, linestyle="--", linewidth=2, label=f"Mean = {passMean:.2f}"
            )

            axes[row, 0].set_title(f"{column} - Pass")
            axes[row, 0].legend()
            axes[row, 0].grid(True, alpha=0.4)

            # Fail
            failDataFrame = failDistributionDataFrames[column]["data"]
            failMean = failDistributionDataFrames[column]["mean"]

            axes[row, 1].plot(failDataFrame["X"], failDataFrame["Y"], linewidth=2)

            axes[row, 1].axvline(
                failMean, linestyle="--", linewidth=2, label=f"Mean = {failMean:.2f}"
            )

            axes[row, 1].set_title(f"{column} - Fail")
            axes[row, 1].legend()
            axes[row, 1].grid(True, alpha=0.4)

        figure.suptitle(
            "Pass vs Fail Distribution - Medium and Large Effect Size",
            fontsize=13,
        )

        figure.supxlabel("Parameter Value")
        figure.supylabel("Probability Density")

        figure.subplots_adjust(
            left=0.08, right=0.97, top=0.93, bottom=0.06, hspace=1.0, wspace=0.25
        )

        outputFileName = f"distribution_{(i // 7) + 1:02d}.png"

        figure.savefig(
            os.path.join(outputFolder, outputFileName), dpi=300, bbox_inches="tight"
        )

        plt.show()
        plt.close(figure)


def main():

    finalCohenDEffectDf = pd.read_csv("./welch_ttest_results-with-cohens-d-effect.csv")

    passDf = pd.read_csv(
        "./IND-value-status_code-1001-dok_code-0-merged_CEMB_141E_141C_141A_141B_and_141D.csv"
    )

    failDf = pd.read_csv(
        "./IND-value-status_code-1011-dok_code-16-merged_CEMB_141E_141C_141A_141B_and_141D.csv"
    )

    columnsList = finalCohenDEffectDf[
        (finalCohenDEffectDf["Effect_Size"] == "Medium")
        | (finalCohenDEffectDf["Effect_Size"] == "Large")
    ]["Column"].tolist()

    passDf = passDf[columnsList]
    failDf = failDf[columnsList]

    passDistributionDataFrames = createDistributionDataFrames(passDf, columnsList)

    failDistributionDataFrames = createDistributionDataFrames(failDf, columnsList)

    plotDistributions(
        passDistributionDataFrames,
        failDistributionDataFrames,
        columnsList,
        "medium-large-effect",
    )


main()
