import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# pip install pandas fastparquet

# df = pd.read_parquet("./final_torque_computed_drifting.parquet")

# df.to_csv("converted_final_torque_computed_drifting.csv", index=False)


df = pd.read_csv("./converted_final_torque_computed_drifting.csv")

df = df.head(10)

df.to_csv("10-drift-dats.csv",index=False)


