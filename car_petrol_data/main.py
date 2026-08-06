import pandas as pd
import matplotlib.pyplot as plt


def loadCsv():

    df = pd.read_csv("./car_petrol_log.csv")

    return df


def dataClean(df):

    df["date"] = df["date"].str.strip()

    df["date"] = pd.to_datetime(df["date"], format="mixed", dayfirst=True)

    df = df.set_index("date")

    serviceRows = df["price_inr"].isna()

    df["odometer_km"] = df["odometer_km"].interpolate(
        method="time", limit_area="inside"
    )

    df["odometer_km"] = df["odometer_km"].round()

    df.loc[serviceRows, "odometer_km"] = pd.NA

    df = df.reset_index()

    return df


def monthlyFuelSpendChart(df):

    df["month"] = df["date"].dt.strftime("%b %y")

    monthlySpend = df.groupby("month", sort=False)["price_inr"].sum()

    highestMonth = monthlySpend.idxmax()
    highestSpend = monthlySpend.max()

    barColors = []

    for months in monthlySpend.index:

        if months == highestMonth:
            barColors.append("tomato")
        else:
            barColors.append("skyblue")

    fig, ax = plt.subplots(figsize=(12, 6))

    bars = ax.bar(monthlySpend.index, monthlySpend.values, color=barColors)

    for bar in bars:

        height = bar.get_height()

        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 100,
            f"₹{height:,.0f}",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    monthData = df[df["month"] == highestMonth]

    refillCount = len(monthData)

    highestIndex = monthlySpend.index.get_loc(highestMonth)

    ax.annotate(
        f"Highest spend\n{refillCount} refills this month",
        xy=(highestIndex, highestSpend - 100),
        xytext=(highestIndex + 1.5, highestSpend + 1200),
        arrowprops=dict(arrowstyle="->", color="black"),
        fontsize=10,
        bbox=dict(boxstyle="round", fc="white", ec="black"),
    )

    ax.set_xlabel("Month")

    ax.grid(True, alpha=0.2)

    ax.set_ylabel("Fuel Spend (INR)")

    plt.show()


def odometerChart(df):

    odometerData = df.copy()

    odometerData = odometerData.dropna(subset=["odometer_km"])

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(
        odometerData["date"],
        odometerData["odometer_km"],
        marker="o",
        color="royalblue",
        linewidth=2,
    )

    for i in range(len(odometerData)):

        x = odometerData.iloc[i]["date"]

        y = odometerData.iloc[i]["odometer_km"]

        if pd.notna(y):
            ax.text(
                x,
                y + 150,
                f"{int(y):,}",
                ha="center",
                fontsize=8,
            )

    ax.set_title("Car odometer reading over time")

    ax.set_xlabel("date")
    ax.set_ylabel("Odometer (km)")

    ax.grid(True, alpha=0.3)

    plt.xticks(rotation=25)

    plt.show()


def drivingIntensityChart(df):

    drivingData = df.copy()

    drivingData = drivingData.dropna(subset=["odometer_km"])

    drivingData["kmDriven"] = drivingData["odometer_km"].diff()

    drivingData["dayCount"] = drivingData["date"].diff().dt.days

    drivingData["kmPerDay"] = (
        drivingData["kmDriven"] / drivingData["dayCount"]
    ).round()

    drivingData = drivingData.dropna(subset=["kmPerDay"])

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(
        drivingData["date"],
        drivingData["kmPerDay"],
        marker="o",
        color="cyan",
        linewidth=2,
    )

    for i in range(len(drivingData)):

        x = drivingData.iloc[i]["date"]

        y = drivingData.iloc[i]["kmPerDay"]

        ax.text(
            x,
            y + 1,
            f"{y:.1f}",
            ha="center",
            fontsize=8,
        )

    highestIndex = drivingData["kmPerDay"].idxmax()

    highestData = drivingData.loc[highestIndex]

    ax.annotate(
        "Highest km/day",
        xy=(highestData["date"], highestData["kmPerDay"]),
        xytext=(highestData["date"], highestData["kmPerDay"] + 10),
        arrowprops=dict(arrowstyle="->"),
        bbox=dict(boxstyle="round", fc="white"),
    )

    lowestIndex = drivingData["kmPerDay"].idxmin()

    lowestData = drivingData.loc[lowestIndex]
    ax.annotate(
        "Lowest km/day",
        xy=(lowestData["date"], lowestData["kmPerDay"]),
        xytext=(lowestData["date"], lowestData["kmPerDay"] + 10),
        arrowprops=dict(arrowstyle="->"),
        bbox=dict(boxstyle="round", fc="white"),
    )

    ax.set_title("Driving intensity (km per day between refills)")

    ax.set_xlabel("Date")

    ax.set_ylabel("Distance (km/day)")

    ax.grid(True, alpha=0.3)

    plt.xticks(rotation=25)

    plt.show()


def monthlyDistanceVsFuelSpendChart(df):

    df = df.copy()

    df["month"] = df["date"].dt.strftime("%b %y")

    monthlySpend = df.groupby("month", sort=False)["price_inr"].sum()

    df = df.dropna(subset=["odometer_km"]).copy()

    df["kmDriven"] = df["odometer_km"].diff()

    df = df.dropna(subset=["kmDriven"])

    monthlyDrivenKm = df.groupby("month", sort=False)["kmDriven"].sum()

    monthlyDrivenKm = monthlyDrivenKm.reindex(monthlySpend.index)

    chartData = pd.DataFrame({"Fuel_Spend": monthlySpend, "Distance": monthlyDrivenKm}).dropna()

    chartData = chartData.reindex(monthlySpend.index).dropna()

    fig , ax1 = plt.subplots(figsize=(12,6))

    bars = ax1.bar(
        chartData.index,
        chartData["Fuel_Spend"],
        color="skyblue",
        alpha=0.3,
        edgecolor="black",
        linewidth=0.2
    )

    for bar in bars:
        height = bar.get_height()

        ax1.text(
            bar.get_x()+bar.get_width()/2,
            height+100,
            f"{height:,.0f}",
            ha="center",
            fontsize=8
        )

    ax1.set_xlabel("Month")
    ax1.set_ylabel("Fuel Spend (₹) BAR_CHARt")
    ax1.grid(True, alpha=0.3)

    ax2 = ax1.twinx()

    ax2.plot(
        chartData.index,
        chartData["Distance"],
        marker="o",
        color="grey",
        linewidth=2
    )

    for i in range(len(chartData)):
        x = chartData.index[i]
        y=chartData["Distance"].iloc[i]

        ax2.text(
            x,
            y-50,
            f"{y:,.0f}",
            ha="center",
            fontsize=8
        )

    ax2.set_ylabel("Distance Driven (km) LINE CHART")

    ax1.set_title("Monthly fuel spend vs Monthly distance driven")

    plt.xticks(rotation=25)

    plt.show()



def checkOdometerColumnIsIncreasing(df):
    df = df.copy()

    result = (df["odometer_km"].dropna().diff().dropna() > 0).all()

    if result:
        print("PASS - All available odometer readings are strictly increasing.")

    else:
        print("Result is Fail")
        
    return result


def checkMOnthlySpendData(df):

    df["month"] = df["date"].dt.strftime("%b %y")

    monthlySpend = df.groupby("month",sort=False)["price_inr"].sum()

    print(monthlySpend)

    return monthlySpend


def checkKmPerDayIsPlausible(df):

    df = df.copy()

    df = df.dropna(subset=["odometer_km"]).copy()

    df["kmDriven"] = df["odometer_km"].diff()

    df["daysElapsed"] = df["date"].diff().dt.days

    df = df.dropna(subset=["daysElapsed"])

    df["kmPerDay"] = (df["kmDriven"] / df["daysElapsed"])

    averageOneDayKm = 300

    failedRows = df[(df["kmPerDay"] < 0 ) | ( df["kmPerDay"] > averageOneDayKm)]

    if failedRows.empty:
        print("PASS - All km/day values are physically plausible.")
    else:
        print("FAIL - Implausible km/day values found:")
        print(failedRows)    



def main():

    ## Part 1 — Load and prepare-----------------------------------------------------------------------------------

    # 1. Load the CSV. Parse `date` into a proper datetime column.
    # Note the dates are in mixed text formats ("June 1 2025", "Sept 5 2025", "March 1 2026") — handle this in code,
    # not by editing the CSV.

    df = loadCsv()

    df = dataClean(df)

    # 2. Identify every data quality issue you can find and list them in a markdown cell.
    # For each one, state **what you will do about it and why**.

    # Any row you exclude or
    # any value you estimate must be documented with a `# WHY:` comment. A `# WHY:` comment defends a decision — it
    # does not restate the operation.











    ## Part 2 — Required charts --------------------------------------------------------------------------------------

    # **Chart 1 — Monthly fuel spend (bar chart).**

    # One bar per month, value labels on top of each bar
    # (use a loop with `ax.text()` or `ax.annotate()`, not `bar_label` alone).
    # Highlight the highest-spend month in a different color and annotate *why* it might be high
    # (look at the individual fills in that month before you guess).

    # monthlyFuelSpendChart(df)

    #  **Chart 2 — Odometer over time (line chart).**

    # Plot the odometer reading against date.
    # Your chart must honestly handle the fact that the first 10 refills have **no odometer reading** —
    # decide how to show or exclude that period and defend it in a `# WHY:` comment.

    # odometerChart(df)

    # **Chart 3 — Driving intensity (km per day between refills).**

    # Compute km driven between consecutive odometer readings,
    # divide by days elapsed, and plot it over time. At least
    # **two data points on this chart require an `ax.annotate()` with an arrow** explaining what happened.
    # Finding *which* two points need explanation is part of the assignment.

    # drivingIntensityChart(df)

    #  **Chart 4 — Your story chart (free choice).**
    # One chart that combines at least two quantities (for example spend vs distance, or cost per km over time)
    # and makes a single clear point. This is the chart you would show the car owner first.
    # A twin-axis chart (`ax.twinx()`) is acceptable if you can defend it.

    # monthlyDistanceVsFuelSpendChart(df)







    ## Part 3 — Mandatory verification section (20%)------------------------------------------------------------------
    # Write at least **three coded checks** that run and print PASS/FAIL, 
    # for example (you may design your own, but they must be real checks against the data, not comments):

    # - Check that the odometer column is strictly increasing wherever it exists.

    # checkOdometerColumnIsIncreasing(df)

    # - Check that the sum of your monthly spend chart equals the sum of the raw `price_inr` column. 
    # If your chart totals don't match the raw data, your chart is lying.

    # checkMOnthlySpendData(df)

    # - Check that every km-per-day value is physically plausible for a personal car, 
    # and **print any rows that fail**. Then look at the failures and decide: data error, 
    # or real event? Your answer goes in the story summary.

    checkKmPerDayIsPlausible(df)




main()
