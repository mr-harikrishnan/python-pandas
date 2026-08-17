import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm


def main():

    youtubeVeiwsCount = [1200,1500,1800,2100,2400]

    df = pd.DataFrame({"veiws": youtubeVeiwsCount})

    mean = np.mean(df["veiws"])

    standardDeviation = np.std(df["veiws"])

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

    plt.xlabel("Veiws (X Values)")
    plt.ylabel("Density (Y Values)")

    plt.title("Standard Deviation")

    plt.grid(True, alpha=0.5)

    plt.show()


main()
