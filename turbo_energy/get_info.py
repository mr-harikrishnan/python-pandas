import pandas as pd


def main():

    excelFile = pd.ExcelFile("./Core Vs Balancing_Corelation.xlsx")

    for sheetName in excelFile.sheet_names:

        if sheetName == "CEMB":
            # Row 2 contains the actual column names
            df = pd.read_excel(excelFile, sheet_name=sheetName, header=1)
        else:
            df = pd.read_excel(excelFile, sheet_name=sheetName)

        print("\n" + "=" * 80)

        print(f"Sheet Name       : {sheetName}")
        print(f"Number of Rows   : {len(df)}")
        print(f"Number of Columns: {len(df.columns)}")
        print(f"Columns List     : {df.columns.tolist()}")


main()
