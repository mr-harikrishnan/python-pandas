import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm


def main():

    iceCreamShopData = [4800,5200,5500,5700,5900,6000,6200,6400,6700,7000]

    df = pd.DataFrame({"sale_data": iceCreamShopData})

    mean = np.mean(df["sale_data"])

    standardDeviation = np.std(df["sale_data"])

    xValues = np.arange(-3, 4) * standardDeviation + mean

    yValues = norm.pdf(xValues, loc=mean, scale=standardDeviation)

    plotDataFrame = pd.DataFrame(
        {"X": np.round(xValues, 4), "Y": np.round(yValues, 10)}
    )

    plt.figure(figsize=(10, 6))

    plt.plot(
        plotDataFrame["X"],
        plotDataFrame["Y"],
        marker="o",
        linewidth=2,
        markersize=6
    )

    plt.axvline(mean, linestyle="--", linewidth=2)

    for i in range(len(plotDataFrame)):
        plt.text(
            plotDataFrame["X"][i], plotDataFrame["Y"][i], f"{plotDataFrame['Y'][i]:.10f}"
        )

    plt.xlabel("Height (X Values)")
    plt.ylabel("Density (Y Values)")

    plt.title("Standard Deviation")

    plt.grid(True, alpha=0.5)

    plt.show()


main()
