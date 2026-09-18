import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm


def main():

    final_cohencd_effect_df = pd.read_csv(
        "./welch_ttest_results-with-cohens-d-effect.csv"
    )

    passDf = pd.read_csv(
        "./IND-value-status_code-1001-dok_code-0-merged_CEMB_141E_141C_141A_141B_and_141D.csv"
    )

    failDf = pd.read_csv(
        "./IND-value-status_code-1011-dok_code-16-merged_CEMB_141E_141C_141A_141B_and_141D.csv"
    )

    columnsList = final_cohencd_effect_df[
        (final_cohencd_effect_df["Effect_Size"] == "Medium")
        | (final_cohencd_effect_df["Effect_Size"] == "Large")
    ]["Column"].tolist()

    passDf = passDf[columnsList]

    failDf = failDf[columnsList]

    print(passDf.head())


main()
