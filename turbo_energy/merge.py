import pandas as pd


def main():
    CEMB_df = pd.read_csv("./cleaned_csvs/CEMB_cleaned.csv")
    oneFourOneE_df = pd.read_csv("./cleaned_csvs/141_cleaned.csv")

    merged_df = pd.merge(
        CEMB_df, oneFourOneE_df, left_on="LGNR", right_on="Serial_CA", how="left"
    )
    merged_df.to_csv("./merged/merged_data.csv", index=False)


main()
