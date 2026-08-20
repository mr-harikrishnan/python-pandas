import pandas as pd


def write_report(text):

    with open("./report.md", "a") as file:
        file.write(text + "\n")


def clean_CEMB(df, status_code, error_code):

    write_report("")
    write_report("==================================================")
    write_report("CEMB CLEANING")
    write_report("==================================================")

    write_report(f"Before cleaning : {df.shape}")

    df = df[(df["STATUS"] == status_code) & (df["DOK"] == error_code)]

    df["DATUM"] = pd.to_datetime(df["DATUM"], errors="coerce")

    df = df.sort_values(by=["LGNR", "DATUM"], ascending=[True, False])

    df = df.drop_duplicates(subset="LGNR", keep="first").reset_index(drop=True)

    write_report(f"After cleaning  : {df.shape}")

    df.to_csv("./cleaned_csvs/CEMB_cleaned.csv", index=False)

    return df


def clean_141E(df):

    write_report("")
    write_report("==================================================")
    write_report("141E CLEANING")
    write_report("==================================================")

    write_report(f"Before cleaning : {df.shape}")

    df = df.sort_values(by=["Serial_CA", "DateTime_S5"], ascending=[True, False])

    df = df.drop_duplicates(subset="Serial_CA", keep="first").reset_index(drop=True)

    write_report(f"After cleaning  : {df.shape}")

    df.to_csv("./cleaned_csvs/141E_cleaned.csv", index=False)

    return df


def merge_CEMB_141E(cleaned_CEMB, cleaned_141E):

    # ---------------LEFT-MERGE-CEMB-141E---------------

    write_report("")
    write_report("==================================================")
    write_report("LEFT MERGE - CEMB AND 141E")
    write_report("==================================================")

    left_merged_CEMB_141E_df = pd.merge(
        cleaned_CEMB,
        cleaned_141E,
        left_on="LGNR",
        right_on="Serial_CA",
        how="left",
    )

    write_report(f"Left merged CEMB and 141E : " f"{left_merged_CEMB_141E_df.shape}")

    missing_141E_df = left_merged_CEMB_141E_df[
        left_merged_CEMB_141E_df["Serial_CA"].isna()
    ]

    write_report(f"CEMB records not found in 141E : " f"{len(missing_141E_df)}")

    write_report("First 10 missing LGNR values:")

    for lgnr in missing_141E_df["LGNR"].head(10):
        write_report(str(lgnr))

    # ---------------RIGHT-MERGE-CEMB-141E---------------

    write_report("")
    write_report("==================================================")
    write_report("RIGHT MERGE - CEMB AND 141E")
    write_report("==================================================")

    right_merged_CEMB_141E_df = pd.merge(
        cleaned_CEMB,
        cleaned_141E,
        left_on="LGNR",
        right_on="Serial_CA",
        how="right",
    )

    missing_CEMB_df = right_merged_CEMB_141E_df[
        right_merged_CEMB_141E_df["LGNR"].isna()
    ]

    write_report(f"141E records not found in CEMB : " f"{len(missing_CEMB_df)}")

    write_report("First 10 missing Serial_CA values:")

    for serial_ca in missing_CEMB_df["Serial_CA"].head(10):
        write_report(str(serial_ca))

    # ---------------INNER-MERGE-CEMB-141E---------------

    write_report("")
    write_report("==================================================")
    write_report("INNER MERGE - CEMB AND 141E")
    write_report("==================================================")

    merged_df = pd.merge(
        cleaned_CEMB,
        cleaned_141E,
        left_on="LGNR",
        right_on="Serial_CA",
        how="inner",
    )

    write_report(f"Inner merged data : " f"{merged_df.shape}")

    merged_df.to_csv("./merged_csvs/merged_CEMB_141.csv", index=False)

    return merged_df


def clean_141C(df):

    write_report("")
    write_report("==================================================")
    write_report("141C CLEANING")
    write_report("==================================================")

    write_report(f"Before cleaning : {df.shape}")

    df["DateTime_S3"] = pd.to_datetime(df["DateTime_S3"], errors="coerce")

    df = df.sort_values(
        by=["Serial_Backplate_S3", "DateTime_S3"], ascending=[True, False]
    )

    df = df.drop_duplicates(subset="Serial_Backplate_S3", keep="first").reset_index(
        drop=True
    )

    write_report(f"After cleaning  : {df.shape}")

    df.to_csv("./cleaned_csvs/141C_cleaned.csv", index=False)

    return df


def merge_CEMB_141E_141C(merged_CEMB_141E, cleaned_141C):

    # ---------------LEFT-MERGE-CEMB-141E-141C---------------

    write_report("")
    write_report("==================================================")
    write_report("LEFT MERGE - CEMB + 141E AND 141C")
    write_report("==================================================")

    left_merged_CEMB_141E_141C_df = pd.merge(
        merged_CEMB_141E,
        cleaned_141C,
        left_on="LGNR",
        right_on="Serial_Backplate_S3",
        how="left",
    )

    write_report(
        f"Left merged CEMB + 141E and 141C : " f"{left_merged_CEMB_141E_141C_df.shape}"
    )

    missing_141C_df = left_merged_CEMB_141E_141C_df[
        left_merged_CEMB_141E_141C_df["Serial_Backplate_S3"].isna()
    ]

    write_report(f"CEMB + 141E records not found in 141C : " f"{len(missing_141C_df)}")

    write_report("First 10 missing Serial_CA values:")

    for serial_ca in missing_141C_df["Serial_CA"].head(10):
        write_report(str(serial_ca))

    # ---------------RIGHT-MERGE-CEMB-141E-141C---------------

    write_report("")
    write_report("==================================================")
    write_report("RIGHT MERGE - CEMB + 141E AND 141C")
    write_report("==================================================")

    right_merged_CEMB_141E_141C_df = pd.merge(
        merged_CEMB_141E,
        cleaned_141C,
        left_on="LGNR",
        right_on="Serial_Backplate_S3",
        how="right",
    )

    missing_CEMB_141E_df = right_merged_CEMB_141E_141C_df[
        right_merged_CEMB_141E_141C_df["Serial_CA"].isna()
    ]

    write_report(
        f"141C records not found in CEMB + 141E : " f"{len(missing_CEMB_141E_df)}"
    )

    write_report("First 10 missing Serial_Backplate_S3 values:")

    for serial_backplate in missing_CEMB_141E_df["Serial_Backplate_S3"].head(10):
        write_report(str(serial_backplate))

    # ---------------INNER-MERGE-CEMB-141E-141C---------------

    write_report("")
    write_report("==================================================")
    write_report("INNER MERGE - CEMB + 141E AND 141C")
    write_report("==================================================")

    merged_CEMB_141E_and_141C = pd.merge(
        merged_CEMB_141E,
        cleaned_141C,
        left_on="LGNR",
        right_on="Serial_Backplate_S3",
        how="inner",
    )

    write_report(
        f"Inner merged CEMB + 141E + 141C : " f"{merged_CEMB_141E_and_141C.shape}"
    )

    merged_CEMB_141E_and_141C.to_csv(
        "./merged_csvs/merged_CEMB_141E_and_141C.csv", index=False
    )

    return merged_CEMB_141E_and_141C


def clean_141A(df):

    write_report("")
    write_report("==================================================")
    write_report("141A CLEANING")
    write_report("==================================================")

    write_report(f"Before cleaning : {df.shape}")

    df["DateTime_S1"] = pd.to_datetime(df["DateTime_S1"], errors="coerce")

    df = df.sort_values(by=["Unique_ID_S1", "DateTime_S1"], ascending=[True, False])

    df = df.drop_duplicates(subset="Unique_ID_S1", keep="first").reset_index(drop=True)

    write_report(f"After cleaning  : {df.shape}")

    df.to_csv("./cleaned_csvs/141A_cleaned.csv", index=False)

    print(f"141A cleaned data : {df.shape}")

    return df


def merge_CEMB_141E_141C_141A(merged_CEMB_141E_141C, cleaned_141A):

    # ---------------LEFT-MERGE-CEMB-141E-141C-141A---------------

    write_report("")
    write_report("==================================================")
    write_report("LEFT MERGE - CEMB + 141E + 141C AND 141A")
    write_report("==================================================")

    left_merged_df = pd.merge(
        merged_CEMB_141E_141C,
        cleaned_141A,
        left_on="Unique_ID_S3",
        right_on="Unique_ID_S1",
        how="left",
    )

    write_report(
        f"Left merged CEMB + 141E + 141C and 141A : " f"{left_merged_df.shape}"
    )

    missing_141A_df = left_merged_df[left_merged_df["Unique_ID_S1"].isna()]

    write_report(
        f"CEMB + 141E + 141C records not found in 141A : " f"{len(missing_141A_df)}"
    )

    write_report("First 10 missing Unique_ID_S3 values:")

    for unique_id in missing_141A_df["Unique_ID_S3"].head(10):
        write_report(str(unique_id))

    # ---------------RIGHT-MERGE-CEMB-141E-141C-141A---------------

    write_report("")
    write_report("==================================================")
    write_report("RIGHT MERGE - CEMB + 141E + 141C AND 141A")
    write_report("==================================================")

    right_merged_df = pd.merge(
        merged_CEMB_141E_141C,
        cleaned_141A,
        left_on="Unique_ID_S3",
        right_on="Unique_ID_S1",
        how="right",
    )

    missing_previous_df = right_merged_df[right_merged_df["Unique_ID_S3"].isna()]

    write_report(
        f"141A records not found in CEMB + 141E + 141C : " f"{len(missing_previous_df)}"
    )

    write_report("First 10 missing Unique_ID_S1 values:")

    for unique_id in missing_previous_df["Unique_ID_S1"].head(10):
        write_report(str(unique_id))

    # ---------------INNER-MERGE-CEMB-141E-141C-141A---------------

    write_report("")
    write_report("==================================================")
    write_report("INNER MERGE - CEMB + 141E + 141C AND 141A")
    write_report("==================================================")

    merged_df = pd.merge(
        merged_CEMB_141E_141C,
        cleaned_141A,
        left_on="Unique_ID_S3",
        right_on="Unique_ID_S1",
        how="inner",
    )

    write_report(f"Inner merged CEMB + 141E + 141C + 141A : " f"{merged_df.shape}")

    return merged_df


def main():

    # Clear old report

    with open("./report.md", "w") as file:
        file.write("TURBO ENERGY DATA REPORT\n")

    excelFile = pd.ExcelFile("./raw_data/Core Vs Balancing_Corelation.xlsx")

    CEMB_df = pd.read_excel(excelFile, sheet_name="CEMB", header=1)

    oneFourOneE_df = pd.read_excel(excelFile, sheet_name="141E")

    oneFourOneC_df = pd.read_excel(excelFile, sheet_name="141C")

    oneFourOneA_df = pd.read_excel(excelFile, sheet_name="141A")

    oneFourOneB_df = pd.read_excel(excelFile, sheet_name="141B")

    oneFourOneD_df = pd.read_excel(excelFile, sheet_name="141D")

    # --------------CLEAN-CEMB-141E------------------

    cleaned_CEMB_df = clean_CEMB(CEMB_df, 1011, 16)

    cleaned_141E_df = clean_141E(oneFourOneE_df)

    # ----------------MERGE-CEMB-141E-----------------

    merged_CEMB_141E_df = merge_CEMB_141E(cleaned_CEMB_df, cleaned_141E_df)

    # ------------------CLEAN-141C----------------------

    cleaned_141C_df = clean_141C(oneFourOneC_df)

    # --------------------MERGE-(MERGED-CEMB-141E)-141C--

    merged_CEMB_141E_141C = merge_CEMB_141E_141C(merged_CEMB_141E_df, cleaned_141C_df)

    # ------------------------------------------------------

    print(
        oneFourOneA_df[oneFourOneA_df.duplicated(subset=["Unique_ID_S1"], keep=False)][
            "Unique_ID_S1"
        ]
    )

    # -----------------------CLEAN-141A----------------------

    cleaned_141A_df = clean_141A(oneFourOneA_df)

    # ------------------------MERGE-(MERGED-CEMB-141E-141C)-141A---

    merged_CEMB_141E_141C_141A = merge_CEMB_141E_141C_141A(merged_CEMB_141E_141C,cleaned_141A_df)


main()
