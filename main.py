import pandas as pd

# PART - B

# Remove exact duplicate rows. How many did you remove


def removeDuplicatesAndGetCount(df):

    duplicateRows = df[df.duplicated()]

    print("Duplicate rows removed.")

    removedCount = len(duplicateRows)

    df = df.drop_duplicates()

    print("Duplicate rows removed count is:", removedCount)

    return df


# Fix the city column: remove extra spaces and make the
# casing consistent (e.g., “CHENNAI”, “chennai”, “  Chennai “ should all become “Chennai”).


def correctityNames(df):

    df["city"] = df["city"].str.strip().str.title()
    print("City names cleaned successfully.")

    return df


# Fix the product column casing the same way.


def correctProductNames(df):

    df["product"] = df["product"].str.strip().str.capitalize()

    print("Product names corrected successfully.")

    return df


# The unit_price column has some values like Rs.2038.
# Strip the prefix and convert the whole column to a numeric type.


def correcUnitPriceColumn(df):

    df["unit_price"] = df["unit_price"].str.removeprefix("Rs.").str.strip().astype(int)

    print("Unit price column corrected successfully.")

    return df


# Convert quantity to a numeric type. Decide what to do with the missing
# values — drop or fill — and justify your choice in a comment.


def correctQuantityColumn(df):

    df["quantity"] = df["quantity"].fillna(1).astype(int)

    print("Quantity column corrected successfully.")

    return df


# Convert order_date to a proper datetime column. (Hint: the dates are in more
# than one format. Look at the data before choosing your approach.)


def convertOrderDateColumn(df):
    df["order_date"] = pd.to_datetime(
        df["order_date"], format="mixed", dayfirst=True, errors="coerce"
    )

    print("Order date column corrected successfully.")

    return df


# Fill missing payment_mode with the value "Unknown".


def fillMissingPaymentMode(df):

    df["payment_mode"] = df["payment_mode"].fillna("Unknown")

    print("Missing payment modes filled with 'Unknown'.")

    return df


# Find rows with impossible values (e.g., negative quantity, quantity that is unrealistically large, price of 0).
# Decide what to do with them and justify.


def findRowsWithImpossibleValues(df):

    largeQuantityValue = 100

    impossibleValues = df[
        (df["quantity"] < 0)
        | (df["quantity"] > largeQuantityValue)
        | (df["unit_price"] == 0)
    ]

    print("Found rows with impossible values.")

    # print(impossibleValues)

    return df


# PART - C

# Add a total_amount column = quantity × unit_price.

def addNewColumnTotalAmount(df):

    df["unit_price"] = df["unit_price"].fillna(0)

    df["total_amount"] = df["quantity"] * df["unit_price"]

    print("Total amount column added successfully.")

    return df


# Which city has the highest total sales?

def findCityWithHighestSales(df):

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

    grouped = df.groupby("product")["total_amount"].sum()

    print("Total revenue per product calculated successfully.")

    print(grouped)

    return df


# How many orders were placed in each month?


def countOrdersInEachMonth(df):

    grouped = df.groupby(df["order_date"].dt.to_period("M"))["order_id"].count()

    print("Monthly order count calculated successfully.")

    print(grouped)

    return df




def main():

    df = pd.read_csv("sales_data_raw.csv")

    # PART - B

    df = removeDuplicatesAndGetCount(df)

    df = correctityNames(df)

    df = correctProductNames(df)

    df = correcUnitPriceColumn(df)

    df = correctQuantityColumn(df)

    df = convertOrderDateColumn(df)

    df = fillMissingPaymentMode(df)

    df = findRowsWithImpossibleValues(df)

    # PART - C

    df = addNewColumnTotalAmount(df)

    df = findCityWithHighestSales(df)

    df = calculateTotalRevenuePerProduct(df)

    df = countOrdersInEachMonth(df)

    df.to_csv('sales_data_clean_part_c.csv', index=False)

    print(" ")

    print("Cleaned DataFrame created.")

    print(" ")

    print(df)


if __name__ == "__main__":
    main()
