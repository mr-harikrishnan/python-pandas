import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm


def main():

    schoolStudentData = [150, 155, 160, 165, 170]

    df = pd.DataFrame({"height": schoolStudentData})

    mean = np.mean(df["height"])

    standardDeviation = np.std(df["height"])

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
            plotDataFrame["X"][i], plotDataFrame["Y"][i], f"{plotDataFrame['X'][i]}"
        )

    plt.xlabel("Height (X Values)")
    plt.ylabel("Density (Y Values)")

    plt.title("Standard Deviation")

    plt.grid(True, alpha=0.5)

    plt.show()


main()
