import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm


def main():

    df = pd.read_csv("./fail-1011-16_merged_CEMB_141E_141C_141A_141B_and_141D.csv")

    df["OEL_TEMPERATUR"] = (
        df["OEL_TEMPERATUR"].str.replace(",", ".", regex=False).astype(float)
    )

    mean = np.mean(df["OEL_TEMPERATUR"])

    standardDeviation = np.std(df["OEL_TEMPERATUR"])

    print("Std", standardDeviation)

    minValue = df["OEL_TEMPERATUR"].min()

    maxValue = df["OEL_TEMPERATUR"].max()

    # xValues = np.arange(-3, 4) * standardDeviation + mean
    xValues = np.linspace(minValue, maxValue, 1000)

    yValues = norm.pdf(xValues, loc=mean, scale=standardDeviation)

    plotDataFrame = pd.DataFrame(
        {"X": np.round(xValues, 4), "Y": np.round(yValues, 10)}
    )

    plt.figure(figsize=(10, 6))

    plt.plot(plotDataFrame["X"], plotDataFrame["Y"], linewidth=2, markersize=6)

    plt.axvline(mean, linestyle="--", linewidth=2, label=f"Mean = {mean:.2f}")

    plt.legend()

    # for i in range(len(plotDataFrame)):
    #     plt.text(
    #         plotDataFrame["X"][i],
    #         plotDataFrame["Y"][i],
    #         f"{plotDataFrame['Y'][i]:.10f}",
    #     )

    plt.xlabel("OEL_TEMPERATUR")

    plt.ylabel("Probability Density")

    plt.title("Normal Distribution of OEL Temperature Fail Data")

    plt.grid(True, alpha=0.5)

    plt.show()


main()
