import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# pip install pandas fastparquet

df = pd.read_parquet("./clickhouse_drift_calculation_computed.parquet")

df.to_csv("clickhouse_drift_calculation_computed.csv", index=False)


