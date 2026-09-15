import numpy as np
import pandas as pd

# CONFIGURATION

CSV_FILE = "./oil_pressure.csv"
OUTPUT_FILE = "manual-cal-oil_pressure.csv"

ACTIVITY_COLUMN = "activity_value"

mean = 4.9272619047619
std = 0.0616122898700961
lambda_value = 0.02
l = 2


# READ CSV FILE

df = pd.read_csv(CSV_FILE)

print("CSV file loaded successfully.")
print(f"Total rows: {len(df)}")


# CHECK REQUIRED COLUMNS

if ACTIVITY_COLUMN not in df.columns:
    raise ValueError(
        f"Column '{ACTIVITY_COLUMN}' was not found in the CSV file. "
        f"Available columns: {list(df.columns)}"
    )

if "source_timestamp" not in df.columns:
    raise ValueError("Column 'source_timestamp' was not found in the CSV file.")


activity_values = df[ACTIVITY_COLUMN]

results = []

prevZ = mean

for iteration, value in enumerate(activity_values, start=1):

    value = float(value)

    z_value = lambda_value * value + (1 - lambda_value) * prevZ

    sigma_ewma = std * np.sqrt(
        (lambda_value / (2 - lambda_value))
        * (1 - (1 - lambda_value) ** (2 * iteration))
    )

    ucl = mean + (l * sigma_ewma)

    lcl = mean - (l * sigma_ewma)

    drift = z_value > ucl or z_value < lcl

    results.append(
        {
            "source_timestamp": df.loc[iteration - 1, "source_timestamp"],
            "activity_value": value,
            "mean": mean,
            "stddev": std,
            "z_prev": prevZ,
            "L": l,
            "lambda_": lambda_value,
            "sigma_ewma": sigma_ewma,
            "ucl": ucl,
            "lcl": lcl,
            "drift": drift,
        }
    )

    prevZ = z_value

result_df = pd.DataFrame(results)

result_df.to_csv(OUTPUT_FILE, index=False)

print("\nCalculation completed.")
print(f"Result saved to: {OUTPUT_FILE}")

print("\nResult:")
print(result_df.to_string(index=False))
