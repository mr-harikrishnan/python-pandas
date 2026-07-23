import pandas as pd

# Add a total_amount column = quantity × unit_price.


def addNewColumnTotalAmount(df):

    df["quantity"] = df["quantity"].fillna(1).astype(int)

    df["unit_price"] = (
        df["unit_price"].str.removeprefix("Rs.").str.strip().astype(int).fillna(0)
    )

    df["total_amount"] = df["quantity"] * df["unit_price"]

    print("Total amount column added successfully.")

    print(df)

    return df


# Which city has the highest total sales?


def findCityWithHighestSales(df):

    df["city"] = df["city"].str.strip().str.title()

    highestSaledCity = df.groupby("city")["total_amount"].sum()

    print("Highest sales city calculated successfully.")

    print(
        "Highest sales city  : ",
        highestSaledCity.idxmax(),
        " Total amount",
        highestSaledCity.max(),
    )

    return df


# What is the total revenue per product?


def calculateTotalRevenuePerProduct(df):

    df["product"] = df["product"].str.strip().str.capitalize()

    grouped = df.groupby("product")["total_amount"].sum()

    print("Total revenue per product calculated successfully.")

    print(grouped)

    return grouped


# How many orders were placed in each month?


def countOrdersInEachMonth(df):

    df["order_date"] = pd.to_datetime(
        df["order_date"], format="mixed", dayfirst=True, errors="coerce"
    )

    grouped = df.groupby(df["order_date"].dt.to_period("M"))["order_id"].count()

    print("Monthly order count calculated successfully.")

    print(grouped)

    return grouped


# Save the cleaned data to sales_data_clean.csv (without the index column).

def dataClean(df):

    df["city"] = df["city"].str.strip().str.title()

    df["product"] = df["product"].str.strip().str.capitalize()

    df["order_date"] = pd.to_datetime(
        df["order_date"], format="mixed", dayfirst=True, errors="coerce"
    )

    df.to_csv('sales_data_clean_part_c.csv', index=False)

    print("Data cleaned successfully.")

    print(df)

    return df


def main():

    df = pd.read_csv("sales_data_raw.csv")

    df = addNewColumnTotalAmount(df)

    findCityWithHighestSales(df)

    calculateTotalRevenuePerProduct(df)

    countOrdersInEachMonth(df)

    dataClean(df)


if __name__ == "__main__":
    main()
