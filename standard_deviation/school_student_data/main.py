import math
import pandas as pd
import matplotlib.pyplot as plt


def calculateMean(total_value, total_count):
    return round(total_value / total_count, 4)


def calculateVariance(x_values, mean):
    total = 0

    for x in x_values:
        difference = x - mean
        squared_value = difference**2
        total = total + squared_value

    return round(total / len(x_values), 4)


def calculateStandardDeviation(variance):
    return round(math.sqrt(variance), 4)


def findXValues(mean, standardDeviation):

    xValues = []

    for i in range(-3, 4):
        value = i * standardDeviation
        xValue = round(float(mean + value), 4)
        xValues.append(xValue)

    return xValues


def calculateDensity(values, mean, variance, standardDeviation):

    outputArray = []

    for value in values:

        sqrt_two_pi = math.sqrt(2 * math.pi)
        standard_deviation_factor = standardDeviation * sqrt_two_pi
        density_constant = 1 / standard_deviation_factor

        squared_difference = (value - mean) ** 2
        variance_factor = 2 * variance
        exponent = squared_difference / variance_factor

        density = density_constant * math.exp(-exponent)

        outputArray.append(round(density, 10))

    return outputArray


def main():

    schoolStudentData = [150, 155, 160, 165, 170]

    df = pd.DataFrame({"height": schoolStudentData})

    totalValue = df["height"].sum()

    mean = calculateMean(totalValue, len(df["height"]))

    variance = calculateVariance(df["height"], mean)

    standardDeviation = calculateStandardDeviation(variance)

    xValues = findXValues(mean, standardDeviation)

    plotDataFrame = pd.DataFrame({"X": xValues})

    yValues = calculateDensity(plotDataFrame["X"], mean, variance, standardDeviation)

    plotDataFrame["Y"] = yValues

    print(plotDataFrame)

    plt.figure(figsize=(10, 6))

    plt.plot(
        plotDataFrame["X"],
        plotDataFrame["Y"],
        marker="o",
        linewidth=2,
        markersize=6,
        label="Density",
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
