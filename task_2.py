import pandas as pd

# PART-A

# Count rows, check columns, and see data types (dtypes) for each file.


def getCountOfRowsAndColumns(customersDf, ordersDf):

    countOfCustomerRows = customersDf.shape[0]
    countOfCustomerColumns = customersDf.shape[1]

    countOfOrderRows = ordersDf.shape[0]
    countOfOrderColumns = ordersDf.shape[1]

    print("\nCount rows, check columns, and see data types for each file.\n")
    print(
        "Count of customer row : ",
        countOfCustomerRows,
        " Count of customer Columns : ",
        countOfCustomerColumns,
    )
    print(
        "Count of order row : ",
        countOfOrderRows,
        " Count of order Columns : ",
        countOfOrderColumns,
    )

    print("\nCustomer Data Types:\n")
    print(customersDf.dtypes)
    print("\nOrder Data Types:\n")
    print(ordersDf.dtypes)

    return


# Look closely at raw values in orders.customer_id.List all problems found in that key column.


def findProblemsInOrdersCustomerId(ordersDf):

    rowsWithExtraSpaces = ordersDf[
        (ordersDf["customer_id"].notna())
        & (ordersDf["customer_id"].str.strip() != ordersDf["customer_id"])
    ]

    print("\nRows with leading or trailing spaces:\n")

    print(rowsWithExtraSpaces)

    rowsWithLowerCaseOrMixedCase = ordersDf[
        (ordersDf["customer_id"].notna())
        & (ordersDf["customer_id"] != ordersDf["customer_id"].str.upper())
    ]

    print("\nRows with lowercase or mixed-case values:\n")

    print(rowsWithLowerCaseOrMixedCase)

    rowsWithNullCustomerId = ordersDf[ordersDf["customer_id"].isnull()]

    print("\nRows with NULL customer_id values:\n")

    print(rowsWithNullCustomerId)

    return


# Check if customers.customer_id values are unique


def checkCustomerIdIsUnique(customersDf):

    repeatedCustomerIds = customersDf[
        customersDf.duplicated(subset=["customer_id"], keep=False)
    ]

    print("\nDuplicate customer_id values found:\n")

    print(repeatedCustomerIds)

    return


# PART - B

# DATA-CLEAN


def ordersDataClean(ordersDf):

    ordersDf["order_id"] = ordersDf["order_id"].str.strip().str.upper()

    ordersDf["customer_id"] = ordersDf["customer_id"].str.strip().str.upper()

    ordersDf["order_date"] = ordersDf["order_date"] = pd.to_datetime(
        ordersDf["order_date"], format="mixed", dayfirst=True, errors="coerce"
    )

    ordersDf["product"] = ordersDf["product"].str.strip().str.capitalize()

    return ordersDf


def customersDataClean(customersDf):

    customersDf["customer_id"] = customersDf["customer_id"].str.strip().str.upper()

    customersDf["customer_name"] = customersDf["customer_name"].str.strip().str.title()

    customersDf["city"] = customersDf["city"].str.strip().str.title()

    customersDf["segment"] = customersDf["segment"].str.strip().str.capitalize()

    customersDf["signup_date"] = customersDf["signup_date"] = pd.to_datetime(
        customersDf["signup_date"], format="mixed", dayfirst=True, errors="coerce"
    )

    return customersDf


# Merge orders with customers.
# You must choose the merge type (how=): would inner, left, right, or outer be correct here,
# given the goal is a revenue report that accounts for every order? Defend the choice in a # WHY:.


def mergeOrderWithCustomer(ordersDf, customersDf):

    merged = ordersDf.merge(customersDf, how="left", indicator=True)

    # Highest order number

    maxOrderNo = merged["order_id"].str.replace("ORD", "", regex=False).astype(int).max()

    newOrderNo = maxOrderNo + 1

    # Duplicate order_id rows
    duplicateMask = merged["order_id"].duplicated(keep="first")

    # Change only second (and later) duplicate rows
    for idx in merged[duplicateMask].index:
     merged.loc[idx, "order_id"] = f"ORD{newOrderNo:04d}"
     newOrderNo += 1

    print("Orders merged with customers successfully.")

    print(merged)

    return merged

    # Reason

    # We chose a left join because we need all order records to generate an accurate revenue report.


# Use indicator=True in your merge. How many orders failed to match a customer?
# List their order_ids and explain the two different reasons they failed


def unmatchedOrders(mergedDf):

    df = mergedDf[mergedDf["_merge"] == "left_only"]

    # print(df)

    df = df["order_id"]

    print("Count of orders failed to match a customer : \n", len(df))

    print("\n Successfully generated the unmatched orders report.\n")

    print("\nList of order_ids :")

    print(df)

    return

    # Reason

    # 1.Some orders have a customer ID, but there is no matching customer record in the customers table.

    # 2.Some orders do not have a customer ID (NULL/NaN).


# Use validate="many_to_one" in your merge. In one comment: what does it protect against,
# and at which line would your script have crashed if you had skipped step 5?


def check_many_to_one_merge(ordersDf, customersDf):

    dublicateCustomer = customersDf[
        customersDf.duplicated(subset="customer_id", keep=False)
    ]["customer_id"]

    dublicateCustomerIdx = customersDf[
        customersDf.duplicated(subset="customer_id", keep=False)
    ]["customer_id"].index

    dublicateCustomerInOrdersIdx = ordersDf[
        ordersDf["customer_id"].isin(dublicateCustomer)
    ].index

    customersDf = customersDf.drop(dublicateCustomerIdx)

    ordersDf = ordersDf.drop(dublicateCustomerInOrdersIdx)

    merged = ordersDf.merge(customersDf, validate="many_to_one")

    print("\nMany-to-one merge validated successfully.\n")

    print(merged)

    return

    # If we received the money, I will calculate it in the total revenue.
    # But I will label it as 'Unattributed' so we don't lose track of it.
    # This way, the financial total is correct, and I can look into the mismatched data later to fix it.


# Decide what to do with the unmatched orders in the revenue report.
# Whatever you choose — drop, keep in an "Unattributed" bucket, or something else — defend it.


def processUnattributedRevenue(df):
    df["order_id"] = df["order_id"].fillna("Unattributed")
    return df


# reason:
# "If we received the money, I will calculate it in the total revenue. "
# "But I will label it as 'Unattributed' so we don't lose track of it.
# This way, the financial total is correct, and I can look into the mismatched data later to fix it.

# PART-D

# Total revenue by customer city (from the customers table, not any other city column).


def addTotalRevenueColumn(mergedDf):

    mergedDf["total_amount"] = mergedDf["quantity"] * mergedDf["unit_price"]

    print("Total amount column added successfully.")

    print(mergedDf)

    return mergedDf


# Total revenue by customer city


def totalRevenueBycity(mergedDf):

    revenueByCity = mergedDf.groupby("city")["total_amount"].sum()

    print("\nTotal Revenue by Customer City:\n")

    print(revenueByCity)

    return


def mostSpentCustomer(mergedDf):

    index = mergedDf["total_amount"].idxmax()
    cost = mergedDf["total_amount"].max()

    highAmountCustomer = mergedDf.loc[index, "customer_name"]

    print("\nName : ", highAmountCustomer, " Cost : ", cost)

    print(" ")

    return


# Total revenue by segment (Regular vs Premium).


def totalRevenueBySegment(mergedDf):

    print(mergedDf.groupby("segment")["total_amount"].sum())

    print(" ")

    return


# Which customers have never placed an order? (Think: which merge direction answers this?)


def customersNeverPlacedOrder(ordersDf, customersDf):

    mergedDf = customersDf.merge(ordersDf, how="left", indicator=True)

    noOrders = mergedDf[mergedDf["_merge"] == "left_only"]

    print(noOrders[["customer_id", "customer_name", "city"]])


 # PART-E

    # Every assignment from now on ends with a verification section: 3 checks, written as code, proving your own output is correct.
    # For this assignment the three checks are:

 # V1 — Row conservation: prove your merge did not create or destroy orders (150 in → how many out? assert it).

def verifyRowConservation(ordersDf, mergedDf):

    assert len(ordersDf) == len(mergedDf), "Merge changed the number of orders."

    print("V1 Passed - Row conservation verified.")



 # V2 — Revenue conservation: total revenue of all orders must equal matched revenue + unmatched revenue, exactly. Assert it.

def verifyRevenueConservation(ordersDf, mergedDf):

    originalRevenue = (ordersDf["quantity"] * ordersDf["unit_price"]).sum()

    matchedRevenue = (mergedDf[mergedDf["_merge"] == "both"]["total_amount"]).sum()

    unmatchedRevenue = (mergedDf[mergedDf["_merge"] == "left_only"]["total_amount"]).sum()

    assert (
        originalRevenue == matchedRevenue + unmatchedRevenue
    ), "Revenue is not conserved."

    print("V2 Passed - Revenue conservation verified.")


# V3 — Sanity check of your own choosing: invent one more check and explain what failure it would catch.

def verifySanityChecks(mergedDf):

    assert (
        (mergedDf["quantity"] >= 0).all()
        and (mergedDf["unit_price"] >= 0).all()
        and (mergedDf["total_amount"] >= 0).all()
    ), "Found negative quantity, price, or revenue."

    assert (
        mergedDf["total_amount"].notna().all()
    ), "Some orders have missing total_amount."

    assert (
        mergedDf.loc[mergedDf["_merge"] == "both", "order_date"]
        >= mergedDf.loc[mergedDf["_merge"] == "both", "signup_date"]
    ).all(), "Found orders placed before customer signup."

    print("V3 Passed - verified Sanity Checks")


def main():

    customersDf = pd.read_csv("customers.csv")

    ordersDf = pd.read_csv("orders.csv")

    ordersDf = ordersDataClean(ordersDf)

    customersDf = customersDataClean(customersDf)

    # getCountOfRowsAndColumns(customersDf, ordersDf)

    # findProblemsInOrdersCustomerId(ordersDf)

    # checkCustomerIdIsUnique(customersDf)

    # PART-B

    mergedDf = mergeOrderWithCustomer(ordersDf, customersDf)

    mergedDf.to_csv("merged_data.csv", index=False)


    # unmatchedOrders(mergedDf)

    # check_many_to_one_merge(ordersDf, customersDf)

    # processUnattributedRevenue(ordersDf)

    # PART-D

    addTotalRevenueColumn(mergedDf)

    totalRevenueBycity(mergedDf)

    mostSpentCustomer(mergedDf)

    totalRevenueBySegment(mergedDf)

    customersNeverPlacedOrder(ordersDf, customersDf)

    # PART-E

    verifyRowConservation(ordersDf, mergedDf)

    verifyRevenueConservation(ordersDf, mergedDf)

    verifySanityChecks(mergedDf)

   

   



    


if __name__ == "__main__":
    main()
