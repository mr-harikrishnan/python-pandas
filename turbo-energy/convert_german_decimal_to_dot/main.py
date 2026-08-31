import os
import pandas as pd

input_file = "./data_files/status_code-1011-err_code-16-merged_CEMB_141E_141C_141A_141B_and_141D.csv"


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


def main():

    output_file_name = input("Enter output CSV file name: ").strip()

    if not output_file_name.endswith(".csv"):

        output_file_name = output_file_name + ".csv"

    output_file = os.path.join("./converted_files", output_file_name)

    if not os.path.exists(input_file):

        print("")
        print(f"Input file not found : {input_file}")

        return

    os.makedirs("./converted_files", exist_ok=True)

    df = pd.read_csv(input_file)

    converted_columns = []
    skipped_columns = []

    for column in columns:

        if column in df.columns:

            df[column] = df[column].map(
                lambda value: (
                    value.replace(",", ".").strip() if isinstance(value, str) else value
                )
            )

            converted_columns.append(column)

        else:

            skipped_columns.append(column)

    df.to_csv(output_file, index=False)

    print("")
    print("==========================================")
    print("CONVERSION COMPLETED")
    print("==========================================")
    print(f"Input file  : {input_file}")
    print(f"Output file : {output_file}")
    print("")
    print(f"Columns converted : {len(converted_columns)}")
    print(f"Columns skipped   : {len(skipped_columns)}")

    if skipped_columns:

        print("")
        print("Skipped columns:")

        for column in skipped_columns:

            print(f" - {column}")

    print("")
    print("Final stored CSV shape:")
    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")
    print(f"Shape   : {df.shape}")


main()
