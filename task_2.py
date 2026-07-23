import pandas as pd

# PART-A

# Count rows, check columns, and see data types (dtypes) for each file.

def getCountOfRowsAndColumns(customersDf,ordersDf):

    countOfCustomerRows = len(customersDf)
    countOfCustomerColumns = len(customersDf.columns)

    countOfOrderRows = len(ordersDf)
    countOfOrderColumns = len(ordersDf.columns)

    print("\nCount rows, check columns, and see data types for each file.\n")
    print("Count of customer row : ",countOfCustomerRows," Count of customer Columns : " ,countOfCustomerColumns)
    print("Count of order row : ",countOfOrderRows," Count of order Columns : " ,countOfOrderColumns)

    print("\nCustomer Data Types:\n")
    print(customersDf.dtypes)
    print("\nOrder Data Types:\n")
    print(ordersDf.dtypes)


# Look closely at raw values in orders.customer_id.List all problems found in that key column.

def findProblemsInOrdersCustomerId(ordersDf):


    rowsWithExtraSpaces = ordersDf[(ordersDf["customer_id"].notna())&(ordersDf["customer_id"].str.strip() != ordersDf["customer_id"] )]

    print("\nRows with leading or trailing spaces:\n")

    print(rowsWithExtraSpaces)

    rowsWithLowerCaseOrMixedCase = ordersDf[(ordersDf["customer_id"].notna())&(ordersDf["customer_id"] != ordersDf["customer_id"].str.upper())]

    print("\nRows with lowercase or mixed-case values:\n")

    print(rowsWithLowerCaseOrMixedCase)

    rowsWithNullCustomerId = ordersDf[ordersDf["customer_id"].isnull()]

    print("\nRows with NULL customer_id values:\n")


    print(rowsWithNullCustomerId)


def checkCustomerIdIsUnique(customersDf):

    repeatedCustomerIds=customersDf[customersDf.duplicated(subset=["customer_id"],keep=False)]

    print("\nDuplicate customer_id values found:\n")

    print(repeatedCustomerIds)




def main():

    customersDf=pd.read_csv("customers.csv")

    ordersDf=pd.read_csv("orders.csv")


    getCountOfRowsAndColumns(customersDf,ordersDf)

    findProblemsInOrdersCustomerId(ordersDf)

    checkCustomerIdIsUnique(customersDf)



if __name__ == "__main__":
    main()