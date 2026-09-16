import pandas as pd
from scipy.stats import ttest_ind


def main():

    passDf = pd.read_csv(
        "./status_code-1001-err_code-0-merged_CEMB_141E_141C_141A_141B_and_141D.csv"
    )
    failDf = pd.read_csv(
        "./status_code-1011-dok_code-16-merged_CEMB_141E_141C_141A_141B_and_141D.csv"
    )

    print(f"passDf {passDf.shape}")
    print(f"failDf {failDf.shape}")

    pass_OEL_TEMPERATUR = (
        passDf["OEL_TEMPERATUR"]
        .str.strip()
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

    fail_OEL_TEMPERATUR = (
        failDf["OEL_TEMPERATUR"]
        .str.strip()
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

    result = ttest_ind(pass_OEL_TEMPERATUR, fail_OEL_TEMPERATUR, equal_var=False)

    t_value = result.statistic
    p_value = result.pvalue

    print("t-value:", t_value)
    print("p-value:", f"{p_value:.10f}")

    alpha = 0.05

    # Decision
    if p_value < alpha:
        print("Reject H0")
        print("The two means are statistically different.")
    else:
        print("Fail to reject H0")
        print("There is insufficient evidence that the two means are different.")


main()
