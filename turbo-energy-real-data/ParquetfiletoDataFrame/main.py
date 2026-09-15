import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# pip install pandas fastparquet

# df = pd.read_parquet("./Parquiet-11-09.parquet")

# df.to_csv("Parquiet-11-09.csv", index=False)


df = pd.read_csv("./Parquiet-11-09.csv")

df = df[df["drift"] == 1]

df = df.head(10)

df.to_csv("Parquiet-11-09-datas-10-drift-true.csv",index=False)




