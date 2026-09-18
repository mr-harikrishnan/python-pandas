import pandas as pd
from scipy.stats import ttest_ind
import pingouin as pg
from column_meanings import COLUMN_MEANINGS


def get_column_meaning(column):

    for item in COLUMN_MEANINGS:
        if item["columnName"] == column:
            return item["meaning"]

    return "Meaning not found"


def normalize_decimal(value):

    if pd.isna(value):
        return value

    # Already numeric
    if isinstance(value, (int, float)):
        return value

    value = str(value).strip()

    # Empty value
    if value == "":
        return pd.NA

    # German decimal separator
    if "," in value:
        value = value.replace(",", ".")

    # Try converting to numeric
    try:
        return float(value)
    except ValueError:
        # Keep non-numeric values unchanged
        return value


def main():

    passDf = pd.read_csv(
        "./status_code-1001-dok_code-0-merged_CEMB_141E_141C_141A_141B_and_141D.csv"
    )

    failDf = pd.read_csv(
        "./status_code-1011-dok_code-16-merged_CEMB_141E_141C_141A_141B_and_141D copy.csv"
    )

    selectedColumns = [
        "MD1_DREH",
        "MD3_DREH",
        "WUCHTVERS_ANZ",
        "MD1_ANLIEF_MG",
        "MD1_ANLIEF_G",
        "MD1_AUSLIEF_MG",
        "MD1_AUSLIEF_G",
        "MD2_ANLIEF_MG",
        "MD2_ANLIEF_G",
        "MD2_AUSLIEF_MG",
        "MD2_AUSLIEF_G",
        "MD3_ANLIEF_MG",
        "MD3_ANLIEF_G",
        "MD3_AUSLIEF_MG",
        "MD3_AUSLIEF_G",
        "EB1_ANLIEF_MG",
        "EB1_ANLIEF_G",
        "EB1_AUSLIEF_MG",
        "EB1_AUSLIEF_G",
        "EB2_ANLIEF_MG",
        "EB2_ANLIEF_G",
        "EB2_AUSLIEF_MG",
        "EB2_AUSLIEF_G",
        "PD1_ANLIEF_1_MV",
        "PD1_ANLIEF_1_G",
        "PD1_AUSLIEF_1_MV",
        "PD1_AUSLIEF_1_G",
        "OEL_DURCHFLUSS",
        "OEL_DRUCK",
        "OEL_TEMPERATUR",
        "PF_SET",
        "PF_TORQUE",
        "PF_ANGLE",
        "SPANN_DRUCK",
        "Val_Pressure_Bhsg",
        "Val_Pressure_CS",
        "Val_Pressure_TS",
        "Val_flow_System",
        "Val_flow_CS",
        "Val_flow_TS",
        "Val_LVDT_Width_PR1",
        "Val_LVDT_Width_PR2",
        "Min_Val_Load_BHsg_W1",
        "Max_Val_Load_BHsg_W1",
        "Min_Val_Distance_BHsg_W1",
        "Max_Val_Distance_BHsg_W1",
        "Min_Val_Load_BHsg_W2",
        "Max_Val_Load_BHsg_W2",
        "Min_Val_Distance_BHsg_W2",
        "Max_Val_Distance_BHsg_W2",
        "Min_Val_Load_BHsg_W3",
        "Max_Val_Load_BHsg_W3",
        "Min_Val_Distance_BHsg_W3",
        "Max_Val_Distance_BHsg_W3",
        "Val_Temp_CWHeat",
        "Val_CWHeat_Cycletime",
        "CW_Pick_Val_Distance_Servo1",
        "CW_Pick_Val_Distance_Servo2",
        "CW_Place_HIM_Val_Distance_Servo2",
        "CW_Place_TW_Val_Distance_Servo1",
        "Pick_SN_Val_Distance_Servo1",
        "Place_SN_Val_Distance_Servo1",
        "Min_Val_Load_CW_W1",
        "Max_Val_Load_CW_W1",
        "Min_Val_Distance_CW_W1",
        "Max_Val_Distance_CW_W1",
        "Min_Val_Load_CW_W2",
        "Max_Val_Load_CW_W2",
        "Min_Val_Distance_CW_W2",
        "Max_Val_Distance_CW_W2",
        "Val_PreTrq_Shaftnut",
        "Val_PreTrqAng_Shaftnut",
        "Torque_Retry_Count",
    ]

    passDf = passDf[selectedColumns]
    failDf = failDf[selectedColumns]

    for column in selectedColumns:
        passDf[column] = passDf[column].apply(normalize_decimal)

    for column in selectedColumns:
        failDf[column] = failDf[column].apply(normalize_decimal)

    alpha = 0.05

    results = []

    for column in selectedColumns:
        passValues = passDf[column].dropna()
        failValues = failDf[column].dropna()

        result = ttest_ind(passValues, failValues, equal_var=False)

        pValue = result.pvalue
        tValue = result.statistic

        if pValue < alpha:
            decision = "Rejected"
        else:
            decision = "Accepted"

        cohensD = pg.compute_effsize(passValues, failValues, eftype="cohen")

        absoluteCohensD = abs(cohensD)

        meaning = get_column_meaning(column)

        if absoluteCohensD < 0.2:
            effectSize = "Very Small"
        elif absoluteCohensD < 0.5:
            effectSize = "Small"
        elif absoluteCohensD < 0.8:
            effectSize = "Medium"
        else:
            effectSize = "Large"

        results.append(
            {
                "Column": column,
                "Maeaning": meaning,
                "T_Value": tValue,
                "P_Value": pValue,
                "Alpha": alpha,
                "Decision": decision,
                "Cohens_D": cohensD,
                "Effect_Size": effectSize,
            }
        )

    resultDf = pd.DataFrame(results)

    resultDf.to_csv("./welch_ttest_results-with-cohens-d-value.csv", index=False)

    print("Results saved to welch_ttest_results.csv")


main()
