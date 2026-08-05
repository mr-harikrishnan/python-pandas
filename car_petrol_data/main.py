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
        method="time",
        limit_area="inside"
    )

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


def main():

    ## Part 1 — Load and prepare------------------------------------

    # 1. Load the CSV. Parse `date` into a proper datetime column.
    # Note the dates are in mixed text formats ("June 1 2025", "Sept 5 2025", "March 1 2026") — handle this in code,
    # not by editing the CSV.

    df = loadCsv()

    df = dataClean(df)

    # 2. Identify every data quality issue you can find and list them in a markdown cell.
    # For each one, state **what you will do about it and why**.

    # 3. Any row you exclude or
    # any value you estimate must be documented with a `# WHY:` comment. A `# WHY:` comment defends a decision — it
    # does not restate the operation.

    # completed task 2 and 3 data-quality-issue.md

    ## Part 2 — Required charts --------------------------------------

    # **Chart 1 — Monthly fuel spend (bar chart).**

    # One bar per month, value labels on top of each bar
    # (use a loop with `ax.text()` or `ax.annotate()`, not `bar_label` alone).
    # Highlight the highest-spend month in a different color and annotate *why* it might be high
    # (look at the individual fills in that month before you guess).

    monthlyFuelSpendChart(df)

    #  **Chart 2 — Odometer over time (line chart).**

    # Plot the odometer reading against date.
    # Your chart must honestly handle the fact that the first 10 refills have **no odometer reading** —
    # decide how to show or exclude that period and defend it in a `# WHY:` comment.

    odometerChart(df)


main()
