import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, ttest_ind, t


def get_standard_error(series):

    standardDeviation = series.std()
    sampleSize = series.count()

    standardError = standardDeviation / np.sqrt(sampleSize)

    return standardError


def get_confidence_interval(series):

    mean = series.mean()
    standardError = get_standard_error(series)
    sampleSize = series.count()

    degreesOfFreedom = sampleSize - 1
    criticalValue = t.ppf(0.975, degreesOfFreedom)

    marginOfError = criticalValue * standardError

    lowerBound = mean - marginOfError
    upperBound = mean + marginOfError

    return lowerBound, upperBound


def welchs_test(df):

    firstColumn = df.columns[0]

    welchResults = {}

    for index in range(1, len(df.columns)):

        secondColumn = df.columns[index]

        firstData = df[firstColumn].dropna()
        secondData = df[secondColumn].dropna()

        tValue, pValue = ttest_ind(firstData, secondData, equal_var=False)

        if pValue < 0.05:
            decision = "Reject the null hypothesis (H₀)"
        else:
            decision = "Fail to reject the null hypothesis (H₀)"

        welchResults[secondColumn] = {
            "tValue": tValue,
            "pValue": pValue,
            "decision": decision,
        }

    return welchResults


def get_cohens_d(firstSeries, secondSeries):

    firstData = firstSeries.dropna()
    secondData = secondSeries.dropna()

    firstMean = firstData.mean()
    secondMean = secondData.mean()

    firstStandardDeviation = firstData.std()
    secondStandardDeviation = secondData.std()

    firstSampleSize = firstData.count()
    secondSampleSize = secondData.count()

    pooledStandardDeviation = np.sqrt(
        (
            (firstSampleSize - 1) * firstStandardDeviation**2
            + (secondSampleSize - 1) * secondStandardDeviation**2
        )
        / (firstSampleSize + secondSampleSize - 2)
    )

    cohensD = (firstMean - secondMean) / pooledStandardDeviation

    return cohensD


def cohens_d_test(df):

    firstColumn = df.columns[0]

    cohensDResults = {}

    for index in range(1, len(df.columns)):

        secondColumn = df.columns[index]

        cohensD = get_cohens_d(df[firstColumn], df[secondColumn])

        absoluteCohensD = abs(cohensD)

        if absoluteCohensD < 0.2:
            effect = "Negligible"
        elif absoluteCohensD < 0.5:
            effect = "Small"
        elif absoluteCohensD < 0.8:
            effect = "Medium"
        else:
            effect = "Large"

        cohensDResults[secondColumn] = {
            "cohensD": cohensD,
            "absoluteCohensD": absoluteCohensD,
            "effect": effect,
        }

    return cohensDResults


def get_distribution_values(series):

    mean = series.mean()
    standardDeviation = series.std()

    xValues = np.linspace(series.min(), series.max(), 1000)

    yValues = norm.pdf(xValues, loc=mean, scale=standardDeviation)

    return xValues, yValues, mean


def plot_distributions(
    df, standardErrors, confidenceIntervals, welchResults, cohensDResults
):

    figure, axes = plt.subplots(
        len(df.columns) - 1,
        3,
        figsize=(16, 24),
        gridspec_kw={"width_ratios": [4.5, 4.5, 1]},
    )

    for index in range(1, len(df.columns)):

        firstColumn = df.columns[0]
        secondColumn = df.columns[index]

        firstX, firstY, firstMean = get_distribution_values(df[firstColumn])
        secondX, secondY, secondMean = get_distribution_values(df[secondColumn])

        firstStandardError = standardErrors[firstColumn]
        secondStandardError = standardErrors[secondColumn]

        firstLowerBound = confidenceIntervals[firstColumn]["lower"]
        firstUpperBound = confidenceIntervals[firstColumn]["upper"]

        secondLowerBound = confidenceIntervals[secondColumn]["lower"]
        secondUpperBound = confidenceIntervals[secondColumn]["upper"]

        row = index - 1

        axes[row, 0].plot(firstX, firstY)
        axes[row, 0].axvline(firstMean, linestyle="--")

        axes[row, 0].set_title(firstColumn)
        axes[row, 0].legend(
            [
                f"Mean = {firstMean:.6f}\n"
                f"SE = {firstStandardError:.6f}\n"
                f"95% CI = [{firstLowerBound:.6f}, {firstUpperBound:.6f}]"
            ]
        )
        axes[row, 0].grid(True, alpha=0.4)

        axes[row, 1].plot(secondX, secondY)
        axes[row, 1].axvline(secondMean, linestyle="--")

        axes[row, 1].set_title(secondColumn)
        axes[row, 1].legend(
            [
                f"Mean = {secondMean:.6f}\n"
                f"SE = {secondStandardError:.6f}\n"
                f"95% CI = [{secondLowerBound:.6f}, {secondUpperBound:.6f}]"
            ]
        )
        axes[row, 1].grid(True, alpha=0.4)

        axes[row, 2].axis("off")

        axes[row, 2].text(0, 0.75, "Welch's t-test", fontsize=11, fontweight="bold")

        welchResult = welchResults[secondColumn]
        cohensDResult = cohensDResults[secondColumn]

        axes[row, 2].axis("off")

        axes[row, 2].text(
            0, 0.85, "Welch's t-test", fontsize=11, fontweight="bold", va="top"
        )

        axes[row, 2].text(
            0,
            0.68,
            f"t = {welchResult['tValue']:.4f}  p = {welchResult['pValue']:.4f} \n",
            fontsize=9,
            va="top",
        )

        decisionText = (
            "Reject H₀" if welchResult["pValue"] < 0.05 else "Fail to reject H₀"
        )

        axes[row, 2].text(0, 0.50, f"{decisionText} \n", fontsize=9, va="top")

        axes[row, 2].text(
            0, 0.32, f"Cohen's d\n", fontsize=11, fontweight="bold", va="top"
        )

        axes[row, 2].text(
            0,
            0.15,
            f"d = {cohensDResult['cohensD']:.4f}\n"
            f"Effect = {cohensDResult['effect']}",
            fontsize=9,
            va="top",
        )

    figure.supxlabel("Parameter Value")
    figure.supylabel("Probability Density")

    figure.suptitle("Parameter Distribution Comparison", fontsize=16)

    figure.subplots_adjust(top=0.94, bottom=0.06, hspace=0.8)

    plt.savefig("distribution.png", dpi=300, bbox_inches="tight")

    plt.show()


def plot_correlation(df):

    correlation = df.corr()

    figure, axis = plt.subplots(figsize=(8, 6))

    image = axis.imshow(correlation, cmap="coolwarm", vmin=-1, vmax=1)

    axis.set_xticks(range(len(correlation.columns)))
    axis.set_xticklabels(correlation.columns, rotation=45, ha="right")

    axis.set_yticks(range(len(correlation.columns)))
    axis.set_yticklabels(correlation.columns)

    for i in range(len(correlation.columns)):
        for j in range(len(correlation.columns)):
            axis.text(j, i, f"{correlation.iloc[i, j]:.2f}", ha="center", va="center")

    figure.colorbar(image, ax=axis, label="Correlation")

    axis.set_title("Correlation Heatmap")

    plt.tight_layout()

    plt.savefig("correlation.png", dpi=300, bbox_inches="tight")

    plt.show()


def main():

    df = pd.read_excel(
        "./Minflow Data@202.xlsx", sheet_name="104339022020_202", skiprows=12
    )

    print("Softstop_Offset :")
    print(df["Softstop_Offset"].to_string())

    columnsList = [
        "Softstop_Offset",
        "HS1_Act",
        "HS2_Act",
        "ForRespTime_Act",
        "RevRespTime_Act",
    ]

    df = df[columnsList]

    for column in columnsList:

        df[column] = df[column].dropna()

        print(f"{df[column].dtype}")

    standardErrors = {}

    for column in columnsList:

        standardError = get_standard_error(df[column])

        standardErrors[column] = standardError

    confidenceIntervals = {}

    for column in columnsList:

        lowerBound, upperBound = get_confidence_interval(df[column])

        confidenceIntervals[column] = {"lower": lowerBound, "upper": upperBound}

    welchResults = welchs_test(df)

    cohensDResults = cohens_d_test(df)

    plot_distributions(
        df, standardErrors, confidenceIntervals, welchResults, cohensDResults
    )

    plot_correlation(df)


main()
