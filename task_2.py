import pandas as pd

# PART-A

# Count rows, check columns, and see data types (dtypes) for each file.


def getCountOfRowsAndColumns(customersDf, ordersDf):

    countOfCustomerRows = len(customersDf)
    countOfCustomerColumns = len(customersDf.columns)

    countOfOrderRows = len(ordersDf)
    countOfOrderColumns = len(ordersDf.columns)

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

    ordersDf["order_date"] = ordersDf["order_date"] = pd.to_datetime(
        ordersDf["order_date"], format="mixed", dayfirst=True, errors="coerce"
    )

    ordersDf["product"] = ordersDf["product"].str.strip().str.capitalize()

    return ordersDf


def customersDataClean(customersDf):

    customersDf["customer_id"]=customersDf["customer_id"].str.strip().str.upper()

    customersDf["customer_name"]=customersDf["customer_name"].str.strip().str.title()

    customersDf["city"]=customersDf["city"].str.strip().str.title()

    customersDf["segment"]=customersDf["segment"].str.strip().str.capitalize()
    
    customersDf["signup_date"] = customersDf["signup_date"] = pd.to_datetime(
            customersDf["signup_date"], format="mixed", dayfirst=True, errors="coerce"
        )

    return customersDf
    

    
    


# Merge orders with customers.
# You must choose the merge type (how=): would inner, left, right, or outer be correct here,
# given the goal is a revenue report that accounts for every order? Defend the choice in a # WHY:.


def mergeOrderWithCustomer(ordersDf, customersDf):

    merged = ordersDf.merge(customersDf, how="left", indicator=True)

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


def main():

    customersDf = pd.read_csv("customers.csv")

    ordersDf = pd.read_csv("orders.csv")

    ordersDf = ordersDataClean(ordersDf)

    customersDf = customersDataClean(customersDf)

    getCountOfRowsAndColumns(customersDf, ordersDf)

    findProblemsInOrdersCustomerId(ordersDf)

    checkCustomerIdIsUnique(customersDf)

    # PART-B

    mergedDf = mergeOrderWithCustomer(ordersDf, customersDf)

    unmatchedOrders(mergedDf)

    check_many_to_one_merge(ordersDf, customersDf)

    processUnattributedRevenue(ordersDf)


if __name__ == "__main__":
    main()
