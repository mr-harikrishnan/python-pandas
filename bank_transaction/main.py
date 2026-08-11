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


def  plotExpensesByCategory(df):

    totalAmountByCategory = df.groupby("Category")["Debit"].sum().sort_values(ascending=False)

    plt.figure(figsize=(10,6))

    plt.bar(totalAmountByCategory.index,totalAmountByCategory.values,color="red",edgecolor="black",linewidth=1.2,alpha=0.6)

    plt.xlabel("Category")

    plt.ylabel("Paid Amount")

    plt.grid(alpha=0.3)

    plt.title("total amount paid per category")

    plt.show()


def dailyCashFlow(df):
    dailyCashFlow = (
        df.groupby("Date")[["Credit", "Debit"]]
        .sum()
        .reset_index()
    )

    dailyCashFlow["Date"] = dailyCashFlow["Date"].dt.strftime("%d-%m")

    ax = dailyCashFlow.plot(
        x="Date",
        y=["Credit","Debit"],
        kind="bar",
        figsize=(14, 6),
        width=0.8
    )

    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Daily Cash Flow")

    ax.set_xticks(range(0, len(dailyCashFlow), 5))
    ax.set_xticklabels(
        dailyCashFlow["Date"].iloc[::5],
        rotation=45
    )

    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()


def countDailyTransaction(df):

    dailyTransactionCount = df.groupby("Date").size().reset_index(name="transaction_count")

    print(dailyTransactionCount)

    plt.figure(figsize=(12,6))

    plt.plot(dailyTransactionCount["Date"],dailyTransactionCount["transaction_count"],linewidth=0.6,color="purple",marker="o")
 
    for x, y in zip(
        dailyTransactionCount["Date"],
        dailyTransactionCount["transaction_count"]
    ):
        plt.text(
            x,
            y+0.5,
            f"{int(y):,}",
            ha="center",
            fontsize=8
        )

    plt.xlabel("Date")
    plt.ylabel("Transaction Count")

    plt.title("Daily Transaction Count")
    plt.grid(alpha=0.3)
    plt.show()


def main():

    df = pd.read_csv("./transaction_data.csv")

    df = dataclean(df)

    df = addOpeningBalanceAndClosingColumns(df)

    df.to_csv("clean_data_with_balance.csv",index=False)

    # 1 .Category Expenses: Draw a chart showing the total amount paid per category, ranked from highest to lowest.

    # plotExpensesByCategory(df)


    # Daily Cash Flow: Create a chart displaying the total amount paid and received for each day.

    # dailyCashFlow(df)


    # Daily Transaction Volume:Plot a chart showing the total number of transactions made each day.

    countDailyTransaction(df)


main()

