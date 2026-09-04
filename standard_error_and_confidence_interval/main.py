import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


def getCriticalValue(confidenceLevel):

    alpha = 1 - (confidenceLevel / 100)
    cumulativeProbability = 1 - (alpha / 2)

    criticalValue = norm.ppf(cumulativeProbability)

    return criticalValue


def main():

    df = pd.read_csv("./student_height_data.csv")

    randomDatas_1 = df.sample(n=10)
    randomDatas_2 = df.sample(n=10)
    randomDatas_3 = df.sample(n=10)

    mean_1 = np.mean(randomDatas_1["height"])
    mean_2 = np.mean(randomDatas_2["height"])
    mean_3 = np.mean(randomDatas_3["height"])

    print(" ")
    print("Sample 1 Mean:", mean_1)
    print("Sample 2 Mean:", mean_2)
    print("Sample 3 Mean:", mean_3)
    print(" ")

    print(" ")
    print("Get one sample data only:")
    print(randomDatas_1)
    print(" ")

    df = randomDatas_1

    mean = np.mean(df["height"])

    print(" ")
    print("Selcted data mean value : ", mean)
    print(" ")

    standardDeviation = np.std(df["height"], ddof=1)

    standardError = standardDeviation / np.sqrt(len(df))

    print(" ")
    print("Sample data Standard Error:", standardError)
    print(" ")

    print(" ")
    print("In this sample, the Standard Error is:", round(standardError, 2), "cm")
    print(" ")

    confidenceLevel = 95

    criticalValue = getCriticalValue(confidenceLevel)

    marginOfError = criticalValue * standardError

    lowerLimit = mean - marginOfError
    upperLimit = mean + marginOfError

    print(" ")
    print("Confidence Level:", confidenceLevel, "%")
    print("Critical Value:", round(criticalValue, 2))
    print("Margin of Error:", round(marginOfError, 2), "cm")
    print("Lower Limit:", round(lowerLimit, 2), "cm")
    print("Upper Limit:", round(upperLimit, 2), "cm")
    print(" ")

    print("Sample 1 Standard Deviation:", round(standardDeviation, 2))

    series = df["height"]

    minValue = series.min()
    maxValue = series.max()

    xValues = np.linspace(minValue, maxValue, 1000)

    yValues = norm.pdf(xValues, loc=mean, scale=standardDeviation)

    print("Minimum Height:", minValue)
    print("Maximum Height:", maxValue)

    plt.figure(figsize=(10, 6))

    plt.plot(xValues, yValues, linewidth=2)

    # Mean
    plt.axvline(mean, linestyle="--", linewidth=2)

    # Lower Limit
    plt.axvline(lowerLimit, linestyle="--", linewidth=2)

    # Upper Limit
    plt.axvline(upperLimit, linestyle="--", linewidth=2)

    plt.xlabel("Height")
    plt.ylabel("Density")

    plt.title("95% Confidence Interval")

    plt.grid(True, alpha=0.5)

    plt.show()


main()
