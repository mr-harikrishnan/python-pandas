import pandas as pd


def main():

    excelFile = pd.ExcelFile("./Core Vs Balancing_Corelation.xlsx")

    CEMB_df = pd.read_excel(excelFile, sheet_name="CEMB", header=1)

    CEMB_df["DATUM"] = pd.to_datetime(CEMB_df["DATUM"], errors="coerce")

    CEMB_df = CEMB_df.sort_values(by=["LGNR", "DATUM"], ascending=[True, False])

    cleaned_CEMB_df = CEMB_df.drop_duplicates(subset="LGNR", keep="first").reset_index(
        drop=True
    )

    cleaned_CEMB_df.to_csv("./CEMB_cleaned.csv", index=False)

    print(f"Original rows : {len(CEMB_df)}")  #31284
    print(f"Cleaned rows  : {len(cleaned_CEMB_df)}") #29059

main()
