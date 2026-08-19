import pandas as pd


def main():

    excelFile = pd.ExcelFile("./Core Vs Balancing_Corelation.xlsx")

    oneFourOneE_df = pd.read_excel(excelFile, sheet_name="141E")

    oneFourOneE_df = oneFourOneE_df.sort_values(
        by=["Serial_CA", "DateTime_S5"], ascending=[True, False]
    )

    cleaned_oneFourOneE_df = oneFourOneE_df.drop_duplicates(
        subset="Serial_CA", keep="first"
    ).reset_index(drop=True)

    cleaned_oneFourOneE_df.to_csv("./cleaned_csvs/141_cleaned.csv",index=False)

    print(f"Original rows : {len(oneFourOneE_df)}")  #30541
    print(f"Cleaned rows  : {len(cleaned_oneFourOneE_df)}") #29085


main()
