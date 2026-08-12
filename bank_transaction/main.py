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

    plt.bar(
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

    ax = ax.flatten() # Converts the 2D array of subplot axes into a 1D array, so we can access each chart easily using ax[i].

    print(ax)

    for i in range(numberOfCategories):

        category = categories[i]

        categoryData = categorySubcategory[category]

        for subCategory in categoryData.index:

            amount = categoryData[subCategory]

            ax[i].bar(subCategory, amount)

        ax[i].set_title(category, fontsize=12, pad=10)

        ax[i].set_ylabel("Total Paid")

        ax[i].tick_params(axis="x", rotation=30)

        ax[i].grid(axis="y", alpha=0.3)

    fig.suptitle("Total Expenses by Category and Subcategory", fontsize=16)

    # Hide unused chart spaces
    for i in range(numberOfCategories, len(ax)):

        ax[i].set_visible(False)

    plt.show()


def main():

    df = pd.read_csv("./transaction_data.csv")

    df = dataclean(df)

    df = addOpeningBalanceAndClosingColumns(df)

    df.to_csv("clean_data_with_balance.csv", index=False)

    # 1 .Category Expenses: Draw a chart showing the total amount paid per category, ranked from highest to lowest.

    # plotExpensesByCategory(df)

    # 2.Daily Cash Flow: Create a chart displaying the total amount paid and received for each day.

    # dailyCashFlow(df)

    # 3.Daily Transaction Volume:Plot a chart showing the total number of transactions made each day.

    # countDailyTransaction(df)

    # 4.Top Payees:Generate a chart showing the highest-paid merchants or users, ranked by total amount paid from highest to lowest.

    # topPayees(df)

    # 5.Subcategory Breakdown: Draw a chart showing the total amount paid for each subcategory, grouped by its main category.

    expensesByCategoryAndSubcategory(df)


main()
