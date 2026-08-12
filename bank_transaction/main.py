import pandas as pd
import matplotlib.pyplot as plt


def dataclean(df):

    df = df.copy()

    print(df.info())

    df["Date"] = df["Date"].str.strip()

    df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")

    df["Time"] = df["Time"].str.strip()

    df["Time"] = df["Time"] = pd.to_datetime(df["Time"], format="mixed").dt.time

    df["Transaction Name"] = df["Transaction Name"].str.strip().str.title()

    df["Direction"] = df["Direction"].str.strip().str.title()

    df["Amount"] = df["Amount"].fillna(0)

    df["Debit"] = df["Debit"].fillna(0)

    df["Credit"] = df["Credit"].fillna(0)

    df["Debit"] = df["Debit"].fillna(0)

    df["Sender / Payer"] = df["Sender / Payer"].str.strip().str.title()

    df["Receiver / Payee"] = df["Receiver / Payee"].str.strip().str.title()

    df["Category"] = df["Category"].str.strip().str.title()

    df["Subcategory"] = df["Subcategory"].str.strip().str.title()

    return df


def addOpeningBalanceAndClosingColumns(df):

    df = df.sort_values(["Date", "Time"]).copy()

    df["Month"] = df["Date"].dt.month_name()

    months = df["Month"].unique()

    openingBalance = 30000

    df["Opening Balance"] = 0.0

    df["Closing Balance"] = 0.0

    for month in months:

        monthlyData = df[df["Month"] == month]

        totalDebit = monthlyData["Debit"].sum()

        totalCredit = monthlyData["Credit"].sum()

        closingBalance = openingBalance + totalCredit - totalDebit

        firstRowIndex = monthlyData.index[0]

        lastRowIndex = monthlyData.index[-1]

        df.loc[firstRowIndex, "Opening Balance"] = openingBalance

        df.loc[lastRowIndex, "Closing Balance"] = closingBalance

        openingBalance = closingBalance

    return df


def plotExpensesByCategory(df):

    totalAmountByCategory = (
        df.groupby("Category")["Debit"].sum().sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 6))

    bars = plt.bar(
        totalAmountByCategory.index,
        totalAmountByCategory.values,
        color="red",
        edgecolor="black",
        linewidth=1.2,
        alpha=0.6,
    )

    plt.xlabel("Category")

    plt.ylabel("Paid Amount")

    plt.grid(alpha=0.3)

    for bar in bars:

        y = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width() / 2,
            y,
            f"{y:,.0f}",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    plt.title("total amount paid per category")

    plt.show()


def dailyCashFlow(df):
    dailyCashFlow = df.groupby("Date")[["Credit", "Debit"]].sum().reset_index()

    dailyCashFlow["Date"] = dailyCashFlow["Date"].dt.strftime("%d-%m")

    ax = dailyCashFlow.plot(
        x="Date", y=["Credit", "Debit"], kind="bar", figsize=(14, 6), width=0.8
    )

    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Daily Cash Flow")

    for container in ax.containers:

        ax.bar_label(
            container, fmt="%.0f", padding=3, fontsize=8
        )  # This gets the height of each bar and adds it as a label.

    ax.set_xticks(range(0, len(dailyCashFlow), 5))
    ax.set_xticklabels(dailyCashFlow["Date"].iloc[::5], rotation=45)

    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()


def countDailyTransaction(df):

    dailyTransactionCount = (
        df.groupby("Date").size().reset_index(name="transaction_count")
    )

    print(dailyTransactionCount)

    plt.figure(figsize=(12, 6))

    plt.plot(
        dailyTransactionCount["Date"],
        dailyTransactionCount["transaction_count"],
        linewidth=0.6,
        color="purple",
        marker="o",
    )

    for i in range(len(dailyTransactionCount)):
        x = dailyTransactionCount["Date"].iloc[i]
        y = dailyTransactionCount["transaction_count"].iloc[i]

        plt.text(x, y + 0.5, f"{int(y):,}", ha="center", fontsize=8)

    plt.xlabel("Date")
    plt.ylabel("Transaction Count")
    plt.xticks(rotation=25)
    plt.title("Daily Transaction Count")
    plt.grid(alpha=0.3)
    plt.show()


def topPayees(df):

    df = df[df["Debit"] > 0]

    topPayees = (
        df.groupby("Receiver / Payee")["Debit"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(12, 6))

    plt.bar(
        topPayees.index,
        topPayees.values,
        edgecolor="black",
        linewidth=1.2,
        alpha=0.6,
        color="darkorange",
    )

    plt.xlabel("Payee")

    plt.ylabel("Total Amount Paid")

    plt.title("Top 10 Payees by Total Amount Paid")

    plt.xticks(rotation=45, ha="right")

    plt.grid(axis="y", alpha=0.3)

    for i in range(len(topPayees)):

        x = topPayees.index[i]
        y = topPayees.values[i]

        plt.text(x, y, f"{y:,.0f}", ha="center", va="bottom", fontsize=9)

    plt.tight_layout()

    plt.show()


def expensesByCategoryAndSubcategory(df):

    df = df[df["Amount"] > 0]

    categorySubcategory = df.groupby(["Category", "Subcategory"])["Debit"].sum()

    categories = categorySubcategory.index.get_level_values("Category").unique()

    numberOfCategories = len(categories)

    eachRowColumn = 3

    rowCount = numberOfCategories // eachRowColumn

    if numberOfCategories % eachRowColumn != 0:
        rowCount = rowCount + 1

    fig, ax = plt.subplots(
        rowCount,
        eachRowColumn,
        figsize=(18, rowCount * 5),
        constrained_layout=True,  # each chart auto space adjust
    )

    ax = (
        ax.flatten()
    )  # Converts the 2D array of subplot axes into a 1D array, so we can access each chart easily using ax[i].

    print(ax)

    for i in range(numberOfCategories):

        category = categories[i]

        categoryData = categorySubcategory[category]

        for subCategory in categoryData.index:

            amount = categoryData[subCategory]

            bars = ax[i].bar(subCategory, amount)

            for bar in bars:

                y = bar.get_height()

                ax[i].text(
                    bar.get_x() + bar.get_width() / 2,
                    y,
                    f"{y:,.0f}",
                    ha="center",
                    va="bottom",
                    fontsize=8,
                )

        ax[i].set_title(category, fontsize=12, pad=10)

        ax[i].set_ylabel("Total Paid")

        ax[i].tick_params(axis="x", rotation=30)

        ax[i].grid(axis="y", alpha=0.3)

    fig.suptitle("Total Expenses by Category and Subcategory", fontsize=16)

    # Hide unused chart spaces
    for i in range(numberOfCategories, len(ax)):

        ax[i].set_visible(False)

    plt.show()


def monthlyCashFlow(df):

    df = df.sort_values("Date")

    df = df[df["Amount"] > 0]

    creditAndDebitByMonthWise = (
        df.groupby("Month", sort=False)[["Credit", "Debit"]].sum().reset_index()
    )

    ax = creditAndDebitByMonthWise.plot(
        x="Month",
        y=["Credit", "Debit"],
        kind="bar",
        figsize=(14, 6),
        width=0.8,
        edgecolor="black",
    )

    for container in ax.containers:

        ax.bar_label(
            container, fmt="%.0f", padding=3, fontsize=9
        )  # This gets the height of each bar and adds it as a label.

    plt.xlabel("Month")
    plt.xlabel("Amount")
    plt.title("Monthly Cash Flow")

    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()


def weeklyPaidPercentage(df):

    df = df[df["Debit"] > 0].copy()

    df["Day"] = df["Date"].dt.day_name()

    dayOrder = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    weeklyPaidCount = df.groupby("Day").size().reindex(dayOrder).fillna(0)

    print(weeklyPaidCount)

    plt.figure(figsize=(9, 9))

    plt.pie(
        weeklyPaidCount.values,
        autopct="%.1f%%",
        startangle=90,
        textprops={"color": "white"},
        wedgeprops={"edgecolor": "white", "linewidth": 2},
    )

    plt.legend(weeklyPaidCount.index, title="Day", loc="upper right")

    plt.title("Paid Transaction Count by Day of Week", fontsize=16, pad=15)

    plt.tight_layout()

    plt.show()


def hourlyAverageSpending(df):

    df = df[df["Debit"] > 0].copy()

    df["Hour"] = df["Time"].apply(lambda x: x.hour)

    averageSpendingByHour = (
        df.groupby("Hour")["Debit"].mean().reindex(range(24), fill_value=0)
    )

    plt.figure(figsize=(14, 6))

    plt.bar(range(24), averageSpendingByHour.values, width=1.0, edgecolor="white")

    plt.xlabel("Hour")
    plt.ylabel("Average Amount Paid")

    plt.title("Hourly Average Spending", fontsize=16, pad=15)

    # Show every hour from 00:00 to 23:00
    plt.xticks(range(24), [f"{hour:02d}:00" for hour in range(24)], rotation=45)

    plt.grid(axis="y", alpha=0.3)

    for i in range(24):

        x = i
        y = averageSpendingByHour.values[i]

        plt.text(x, y, f"{y:.0f}", ha="center", va="bottom", fontsize=8)

    plt.tight_layout()

    plt.show()


def runningBalance(df):

    monthlyBalance = (
        df.groupby("Month", sort=False)[["Opening Balance", "Closing Balance"]]
        .max()
        .reset_index()
    )

    fig, ax = plt.subplots(1, 2, figsize=(14, 6))

    ax[0].plot(monthlyBalance["Month"], monthlyBalance["Opening Balance"], marker="o")

    ax[0].set_title("Opening Balance")
    ax[0].set_xlabel("Month")
    ax[0].set_ylabel("Balance")
    ax[0].grid(alpha=0.3)

    ax[1].plot(monthlyBalance["Month"], monthlyBalance["Closing Balance"], marker="o")

    ax[1].set_title("Closing Balance")
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("Balance")
    ax[1].grid(alpha=0.3)

    for i in range(len(monthlyBalance)):

        ax[0].text(
            i,
            monthlyBalance["Opening Balance"].iloc[i],
            f"{monthlyBalance['Opening Balance'].iloc[i]:.0f}",
            ha="center",
        )

        ax[1].text(
            i,
            monthlyBalance["Closing Balance"].iloc[i],
            f"{monthlyBalance['Closing Balance'].iloc[i]:.0f}",
            ha="center",
        )

    fig.suptitle("Monthly Running Balance")

    plt.tight_layout()
    plt.show()


def monthlyExpensePercentage(df):

    df = df[df["Debit"] > 0].copy()

    monthlyExpenses = df.groupby("Month", sort=False)["Debit"].sum()

    plt.figure(figsize=(9, 9))

    plt.pie(
        monthlyExpenses.values,
        autopct="%.1f%%",
        startangle=90,
        textprops={"color": "white"},
        wedgeprops={"edgecolor": "white", "linewidth": 2},
    )

    plt.legend(monthlyExpenses.index, title="Month", loc="upper right")

    plt.title("Monthly Expense Distribution", fontsize=16, pad=15)

    plt.tight_layout()

    plt.show()


def main():

    df = pd.read_csv("./transaction_data.csv")

    df = dataclean(df)

    df = addOpeningBalanceAndClosingColumns(df)

    df.to_csv("clean_data_with_balance.csv", index=False)

    # 1 .Category Expenses: Draw a chart showing the total amount paid per category, ranked from highest to lowest.

    plotExpensesByCategory(df)

    # 2.Daily Cash Flow: Create a chart displaying the total amount paid and received for each day.

    dailyCashFlow(df)

    # 3.Daily Transaction Volume:Plot a chart showing the total number of transactions made each day.

    countDailyTransaction(df)

    # 4.Top Payees:Generate a chart showing the highest-paid merchants or users,
    # ranked by total amount paid from highest to lowest.

    topPayees(df)

    # 5.Subcategory Breakdown: Draw a chart showing the total amount paid for each subcategory, grouped by its main category.

    expensesByCategoryAndSubcategory(df)

    # 6.Monthly Cash Flow:Plot a chart comparing the total amount paid and received for each month.

    monthlyCashFlow(df)

    # 7.Weekly Paid Transaction Distribution: Create a pie chart showing the percentage of paid
    # transaction counts for each day of the week (Monday to Sunday) across the entire dataset.

    weeklyPaidPercentage(df)

    # 8.Hourly Average Spending: Create a chart showing the average amount paid per
    #  transaction for each one-hour interval from 00:00–01:00 through 23:00–00:00 across the entire dataset.

    hourlyAverageSpending(df)

    # 9.Running Balance: Using the existing opening and closing balance values,
    # create a single figure with two charts showing the monthly opening balance and closing balance for all months.

    runningBalance(df)

    # 10. Monthly Expense Distribution: Create a pie chart showing the percentage share
    #  of the total paid amount contributed by each month.

    monthlyExpensePercentage(df)


main()
