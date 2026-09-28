import pandas as pd

excelFile = pd.ExcelFile("./raw_data/Core Vs Balancing_Corelation.xlsx")

CEMB_df = pd.read_excel(excelFile, sheet_name="CEMB", header=1)