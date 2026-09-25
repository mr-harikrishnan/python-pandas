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
    passDistributionDataFrames,
    failDistributionDataFrames,
    passDf,
    failDf,
    columns,
    fileName,
):

    fileNameWithoutExtension = os.path.splitext(os.path.basename(fileName))[0]

    outputFolder = f"./distribution_plots/{fileNameWithoutExtension}"

    os.makedirs(outputFolder, exist_ok=True)

    for i in range(0, len(columns), 4):

        currentColumns = columns[i : i + 4]

        figure, axes = plt.subplots(len(currentColumns), 2, figsize=(16, 32))

        if len(currentColumns) == 1:
            axes = np.array([axes])

        for row, column in enumerate(currentColumns):

            passDataFrame = passDistributionDataFrames[column]["data"]
            passMean = passDistributionDataFrames[column]["mean"]

            failDataFrame = failDistributionDataFrames[column]["data"]
            failMean = failDistributionDataFrames[column]["mean"]

            # Distribution Plot

            axes[row, 0].plot(
                passDataFrame["X"],
                passDataFrame["Y"],
                color="darkgreen",
                linewidth=2,
                label="Pass",
            )

            axes[row, 0].plot(
                failDataFrame["X"],
                failDataFrame["Y"],
                color="red",
                linewidth=2,
                label="Fail",
            )

            axes[row, 0].axvline(
                passMean, color="darkgreen", linestyle="--", linewidth=2, label="Mean"
            )

            axes[row, 0].axvline(failMean, color="red", linestyle="--", linewidth=2)

            axes[row, 0].set_title(f"{column} - Distribution")

            axes[row, 0].legend()

            axes[row, 0].grid(True, alpha=0.4)

            # Box Plot

            passValues = pd.to_numeric(passDf[column], errors="coerce").dropna()

            failValues = pd.to_numeric(failDf[column], errors="coerce").dropna()

            axes[row, 1].boxplot([passValues, failValues])

            axes[row, 1].plot(
                [0.85, 1.15],
                [passValues.mean(), passValues.mean()],
                color="blue",
                linewidth=1,
                label="Mean",
            )

            axes[row, 1].plot(
                [1.85, 2.15],
                [failValues.mean(), failValues.mean()],
                color="blue",
                linewidth=1,
            )

            axes[row, 1].set_title(f"{column} - Box Plot")

            axes[row, 1].legend()

            axes[row, 1].grid(True, axis="y", alpha=0.4)

        figure.suptitle(
            "Pass vs Fail Distribution and Box Plot - Medium and Large Effect Size",
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

    print(columnsList)

    passDf = passDf[columnsList]
    failDf = failDf[columnsList]

    passDf.to_csv("medium_large_drifted_columns_pass_datas.csv",index=False)
    failDf.to_csv("medium_large_drifted_columns_fail_datas.csv",index=False)

    # passDistributionDataFrames = createDistributionDataFrames(passDf, columnsList)

    # failDistributionDataFrames = createDistributionDataFrames(failDf, columnsList)

    # plotDistributions(
    #     passDistributionDataFrames,
    #     failDistributionDataFrames,
    #     passDf,
    #     failDf,
    #     columnsList,
    #     "medium-large-effect",
    # )


main()
