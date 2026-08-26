import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import os


def write_report(text):

    with open("./report.md", "a") as file:
        file.write(text + "\n")


def find_value_columns(df, columns, value):

    foundColumns = []

    for column in columns:

        if (df[column] == value).any():
            foundColumns.append(column)

    write_report(f"## {value} Value")
    write_report("")
    write_report(f"{value} was found in the following columns:")
    write_report("")

    for column in foundColumns:
        write_report(f"- {column}")

    write_report("")

    return foundColumns


def get_distribution_values(series):

    mean = np.mean(series)
    standardDeviation = np.std(series)

    minValue = series.min()
    maxValue = series.max()

    xValues = np.linspace(minValue, maxValue, 1000)

    yValues = norm.pdf(xValues, loc=mean, scale=standardDeviation)

    return xValues, yValues, mean


def create_distribution_dataframes(df, columns):

    distributionDataFrames = {}

    for column in columns:

        xValues, yValues, mean = get_distribution_values(df[column])

        distributionDataFrames[column] = {
            "data": pd.DataFrame(
                {"X": np.round(xValues, 4), "Y": np.round(yValues, 10)}
            ),
            "mean": mean,
        }

    return distributionDataFrames


def plot_distributions(
    passDistributionDataFrames, failDistributionDataFrames, columns, failFile
):

    failFileName = os.path.splitext(os.path.basename(failFile))[0]

    outputFolder = f"./distribution_plots/{failFileName}"
    os.makedirs(outputFolder, exist_ok=True)

    for i in range(0, len(columns), 7):

        currentColumns = columns[i : i + 7]

        figure, axes = plt.subplots(len(currentColumns), 2, figsize=(16, 32))

        for row in range(len(currentColumns)):

            column = currentColumns[row]

            # passs
            passDataFrame = passDistributionDataFrames[column]["data"]
            passMean = passDistributionDataFrames[column]["mean"]

            axes[row, 0].plot(passDataFrame["X"], passDataFrame["Y"], linewidth=2)

            axes[row, 0].axvline(
                passMean, linestyle="--", linewidth=2, label=f"Mean = {passMean:.2f}"
            )

            axes[row, 0].set_title(f"{column} - Pass")

            axes[row, 0].legend()
            axes[row, 0].grid(True, alpha=0.4)

            # fail
            failDataFrame = failDistributionDataFrames[column]["data"]
            failMean = failDistributionDataFrames[column]["mean"]

            axes[row, 1].plot(failDataFrame["X"], failDataFrame["Y"], linewidth=2)

            axes[row, 1].axvline(
                failMean, linestyle="--", linewidth=2, label=f"Mean = {failMean:.2f}"
            )

            axes[row, 1].set_title(f"{column} - Fail")

            axes[row, 1].legend()
            axes[row, 1].grid(True, alpha=0.4)

        figure.supxlabel("Parameter Value")
        figure.supylabel("Probability Density")

        figure.subplots_adjust(
            left=0.08, right=0.97, top=0.95, bottom=0.06, hspace=1.0, wspace=0.25
        )

        outputFileName = f"distribution_{(i // 7) + 1:02d}.png"

        figure.savefig(
            os.path.join(outputFolder, outputFileName),
            dpi=300,
            bbox_inches="tight",
        )

        plt.show()

        plt.close(figure)


def find_mean_difference_columns(
    passDistributionDataFrames,
    failDistributionDataFrames,
    columns,
):

    write_report("## Deviation Analysis")
    write_report("")
    write_report("| Column Name | Pass Mean | Fail Mean | Deviation |")
    write_report("|---|---:|---:|---:|")

    for column in columns:

        passMean = passDistributionDataFrames[column]["mean"]
        failMean = failDistributionDataFrames[column]["mean"]

        # Remove decimal values
        passWholeMean = int(passMean)
        failWholeMean = int(failMean)

        # Ignore if integer values are the same
        if passWholeMean == failWholeMean:
            continue

        # Calculate difference
        difference = abs(passWholeMean - failWholeMean)

        write_report(
            f"| {column} | {passWholeMean} | " f"{failWholeMean} | {difference} |"
        )

    write_report("")


def main():

    passFile = "./pass-datas/pass-01001-0_merged_CEMB_141E_141C_141A_141B_and_141D.csv"
    failFile = "./fail-datas/status_code-1011-err_code-16-merged_CEMB_141E_141C_141A_141B_and_141D.csv"
    # failFile = "./fail-datas/status_code-1002-err_code-513-merged_CEMB_141E_141C_141A_141B_and_141D.csv"
    # failFile = "./fail-datas/status_code-1002-err_code-555-merged_CEMB_141E_141C_141A_141B_and_141D.csv"
    # failFile = "./fail-datas/status_code-1002-err_code-503-merged_CEMB_141E_141C_141A_141B_and_141D.csv"

    pass_df = pd.read_csv(passFile)
    fail_df = pd.read_csv(failFile)

    # Clear old report
    with open("./report.md", "w") as file:
        file.write("# Pass Fail Distribution Report\n\n")

    write_report("## Data Files")
    write_report("")
    write_report(f"**Pass Data File Name:** `{os.path.basename(passFile)}`")
    write_report(f"**Fail Data File Name:** `{os.path.basename(failFile)}`")
    write_report("")

    columns = [
        "MD1_ANLIEF_MG",
        "MD1_AUSLIEF_MG",
        "MD2_ANLIEF_MG",
        "MD2_AUSLIEF_MG",
        "MD3_ANLIEF_MG",
        "MD3_AUSLIEF_MG",
        "EB1_ANLIEF_MG",
        "EB1_AUSLIEF_MG",
        "EB2_ANLIEF_MG",
        "EB2_AUSLIEF_MG",
        "PD1_ANLIEF_1_MV",
        "PD1_AUSLIEF_1_MV",
        "OEL_DURCHFLUSS",
        "OEL_DRUCK",
        "OEL_TEMPERATUR",
        "PF_TORQUE",
        "SPANN_DRUCK",
        "Val_Pressure_Bhsg",
        "Val_Pressure_CS",
        "Val_Pressure_TS",
        "Val_flow_System",
        "Val_flow_CS",
        "Val_flow_TS",
        "Max_Pressure_Bhsg",
        "Min_Pressure_CS",
        "Max_Pressure_CS",
        "Max_Pressure_TS",
        "Min_flow_System",
        "Min_flow_CS",
        "Min_flow_TS",
        "Min_LVDT_Width_PR1",
        "Val_LVDT_Width_PR1",
        "Max_LVDT_Width_PR1",
        "Min_LVDT_Width_PR2",
        "Val_LVDT_Width_PR2",
        "Max_LVDT_Width_PR2",
        "Pick_Val_Distance_Servo1",
        "Pick_Val_Distance_Servo2",
        "Place_Val_Distance_Servo1",
        "Place_Val_Distance_Servo2",
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
        "Min_Val_Load_BHsg_W4",
        "Max_Val_Load_BHsg_W4",
        "Min_Val_Distance_BHsg_W4",
        "Max_Val_Distance_BHsg_W4",
        "Val_Temp_CWHeat",
        "Val_CWHeat_Cycletime",
        "CW_Pick_Val_Distance_Servo1",
        "CW_Pick_Val_Distance_Servo2",
        "CW_Place_HIM_Val_Distance_Servo2",
        "CW_Place_TW_Val_Distance_Servo1",
        "CW_Place_TW_Val_Distance_Servo2",
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
    ]

    write_report("## Column Information")
    write_report("")
    write_report(f"**Total Column Count:** {len(columns)}")
    write_report("")
    write_report("**Columns:**")
    write_report("")

    for count, column in enumerate(columns, start=1):
        write_report(f"{count}. {column}")

    write_report("")

    cleaned_pass_df = pass_df[columns].apply(
        lambda x: x.astype(str)
        .str.strip()
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

    cleaned_fail_df = fail_df[columns].apply(
        lambda x: x.astype(str)
        .str.strip()
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

    passDistributionDataFrames = create_distribution_dataframes(
        cleaned_pass_df, columns
    )

    failDistributionDataFrames = create_distribution_dataframes(
        cleaned_fail_df, columns
    )

    plot_distributions(
        passDistributionDataFrames, failDistributionDataFrames, columns, failFile
    )

    find_mean_difference_columns(
        passDistributionDataFrames,
        failDistributionDataFrames,
        columns,
    )

    find_value_columns(
        cleaned_pass_df,
        columns,
        909090,
    )

    find_value_columns(
        cleaned_fail_df,
        columns,
        909090,
    )


main()
