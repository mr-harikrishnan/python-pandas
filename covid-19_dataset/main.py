import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt


def plotConfirmedCasesDistribution(df):

    data = df["Confirmed"]

    mean = np.mean(data)

    standardDeviation = np.std(data)

    xValues = np.linspace(
        mean - 3 * standardDeviation, mean + 3 * standardDeviation, 300
    )

    yValues = norm.pdf(xValues, loc=mean, scale=standardDeviation)

    plotDataFrame = pd.DataFrame(
        {"X": np.round(xValues, 4), "Y": np.round(yValues, 10)}
    )

    plt.figure(figsize=(10, 6))

    plt.plot(plotDataFrame["X"], plotDataFrame["Y"], linewidth=2)

    plt.axvline(mean, linestyle="--", linewidth=2, label=f"Mean = {mean:,.2f}")

    plt.legend()

    plt.xlabel("Confirmed Cases")

    plt.ylabel("Density (Y Values)")

    plt.title("Normal Distribution of Confirmed Cases")

    plt.grid(True, alpha=0.5)

    plt.show()


def main():

    df = pd.read_csv("./country_wise_latest.csv")

    plotConfirmedCasesDistribution(df)


main()
