import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ttest_ind, norm


def get_distribution_values(series):

    mean = series.mean()
    standardDeviation = series.std()

    xValues = np.linspace(series.min(), series.max(), 1000)

    yValues = norm.pdf(xValues, loc=mean, scale=standardDeviation)

    return xValues, yValues, mean


def plot_distributions(softstop, hs1):

    softstopX, softstopY, softstopMean = get_distribution_values(softstop)
    hs1X, hs1Y, hs1Mean = get_distribution_values(hs1)

    figure, axes = plt.subplots(1, 2, figsize=(16, 6))

    axes[0].plot(softstopX, softstopY, linewidth=2)

    axes[0].axvline(
        softstopMean, linestyle="--", linewidth=2, label=f"Mean = {softstopMean:.2f}"
    )

    axes[0].set_title("Softstop_Offset")
    axes[0].set_xlabel("Parameter Value")
    axes[0].set_ylabel("Probability Density")
    axes[0].legend()
    axes[0].grid(True, alpha=0.4)

    axes[1].plot(hs1X, hs1Y, linewidth=2)

    axes[1].axvline(hs1Mean, linestyle="--", linewidth=2, label=f"Mean = {hs1Mean:.2f}")

    axes[1].set_title("HS1_Act")
    axes[1].set_xlabel("Parameter Value")
    axes[1].set_ylabel("Probability Density")
    axes[1].legend()
    axes[1].grid(True, alpha=0.4)

    figure.subplots_adjust(left=0.08, right=0.97, top=0.90, bottom=0.12, wspace=0.25)

    figure.suptitle("Parameter Distribution")

    plt.show()


def plot_correlation(corr):

    plt.figure(figsize=(6, 5))

    plt.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)

    plt.colorbar(label="Correlation")

    plt.xticks(range(len(corr.columns)), corr.columns)

    plt.yticks(range(len(corr.columns)), corr.columns)

    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()


def main():

    df = pd.read_excel(
        "./Minflow Data@202.xlsx", sheet_name="104339022020_202", skiprows=12
    )

    df = df[["Softstop_Offset", "HS1_Act"]]

    softstop = df["Softstop_Offset"].dropna()
    hs1 = df["HS1_Act"].dropna()

    softstopMean = softstop.mean()
    softstopStd = softstop.std()

    hs1Mean = hs1.mean()
    hs1Std = hs1.std()

    print("Mean & Standard Deviation :")
    print(f"Softstop_Offset Mean: {softstopMean:.4f}")
    print(f"Softstop_Offset Standard Deviation: {softstopStd:.4f}")
    print(f"HS1_Act Mean: {hs1Mean:.4f}")
    print(f"HS1_Act Standard Deviation: {hs1Std:.4f}")

    plot_distributions(softstop, hs1)

    tStatistic, pValue = ttest_ind(softstop, hs1, equal_var=False)

    print(f"t-statistic: {tStatistic:.4f}")
    print(f"p-value: {pValue:.6f}")

    alpha = 0.05

    print("\n===== Hypothesis Result =====")
    print("H0: The means are equal")
    print("H1: The means are different")

    if pValue < alpha:
        print("Reject H0")
    else:
        print("Fail to reject H0")

    corr = df.corr()

    plot_correlation(corr)


main()
