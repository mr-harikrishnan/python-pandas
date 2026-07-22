import pandas as pd

# Remove exact duplicate rows. How many did you remove

def removeDuplicatesAndGetCount(df):

    duplicateRows = df[df.duplicated()]

    print("Duplicate rows removed.")
    

    # print(duplicateRows)

    removedCount = len(duplicateRows)

    df = df.drop_duplicates()

    print("Duplicate rows removed count is:", removedCount)

    return df


# Fix the city column: remove extra spaces and make the 
# casing consistent (e.g., “CHENNAI”, “chennai”, “  Chennai “ should all become “Chennai”).

def correctityNames(df):

    df["city"] = df["city"].astype(str).str.strip().str.capitalize()
    print("City names cleaned successfully.")

    return df

# Fix the product column casing the same way.

def correctProductNames(df):

    df["product"] = df["product"].str.strip().str.title()

    print("Product names corrected successfully.")

    return df

# The unit_price column has some values like Rs.2038. 
# Strip the prefix and convert the whole column to a numeric type.

def correcUnitPriceColumn(df):

    df["unit_price"] = df["unit_price"].str.removeprefix("Rs.").str.lstrip().astype(int)

    print("Unit price column corrected successfully.")

    return df

# Convert quantity to a numeric type. Decide what to do with the missing 
# values — drop or fill — and justify your choice in a comment.

def correctQuantityColumn(df):

    df["quantity"] = df["quantity"].fillna(1)

    print("Quantity column corrected successfully.")

    return df

# Convert order_date to a proper datetime column. (Hint: the dates are in more
# than one format. Look at the data before choosing your approach.)

def convertOrderDateColumn(df):
    df["order_date"] = pd.to_datetime(
        df["order_date"], format="mixed", dayfirst=True, errors="coerce"
    ).dt.strftime("%d/%m/%Y")

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

    df = df[
        (df["quantity"] < 0)
        | (df["quantity"] > largeQuantityValue)
        | (df["unit_price"] == 0)
    ]
    print("Found rows with impossible values.")
    return df


def main():

    df = pd.read_csv("sales_data_raw.csv")

    df = removeDuplicatesAndGetCount(df)

    df = correctityNames(df)

    df = correctProductNames(df)

    df = correcUnitPriceColumn(df)

    df = correctQuantityColumn(df)

    df = convertOrderDateColumn(df)

    df = fillMissingPaymentMode(df)
    
    print("DataFrame created.")

    print(df)

    df = findRowsWithImpossibleValues(df)

    print(df)


if __name__ == "__main__":
    main()
