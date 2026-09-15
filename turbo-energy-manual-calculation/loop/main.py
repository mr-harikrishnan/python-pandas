import numpy as np
import pandas as pd

# ============================================================
# CONFIGURATION
# ============================================================

CSV_FILE = "./Parquiet-11-09-datas-10.csv"
OUTPUT_FILE = "activity_calculation_result.csv"

# CSV column containing activity values
ACTIVITY_COLUMN = "activity_value"

# Calculation variables
mean = 2.148216
std = 0.122471
lambda_value = 0.02
l = 2


# ============================================================
# READ CSV FILE
# ============================================================

df = pd.read_csv(CSV_FILE)

print("CSV file loaded successfully.")
print(f"Total rows: {len(df)}")


# ============================================================
# CHECK ACTIVITY COLUMN
# ============================================================

if ACTIVITY_COLUMN not in df.columns:
    raise ValueError(
        f"Column '{ACTIVITY_COLUMN}' was not found in the CSV file. "
        f"Available columns: {list(df.columns)}"
    )


# ============================================================
# GET ACTIVITY VALUES
# ============================================================

activity_values = df[ACTIVITY_COLUMN]


# ============================================================
# RESULT DATA
# ============================================================

results = []


# ============================================================
# PREV Z
# ============================================================
# First iteration:
# prevZ = mean
#
# After the first iteration:
# prevZ = previous calculated Z value
# ============================================================

prevZ = mean


# ============================================================
# LOOP THROUGH ACTIVITY VALUES
# ============================================================

for iteration, value in enumerate(activity_values, start=1):

    # --------------------------------------------------------
    # Convert activity value to number
    # --------------------------------------------------------

    value = float(value)

    # ========================================================
    # Z CALCULATION
    # ========================================================
    #
    # Z = lambda * value + (1 - lambda) * prevZ
    # ========================================================

    stepone = lambda_value * value

    stepTwo = 1 - lambda_value

    stepThree = stepTwo * prevZ

    stepFour = stepone + stepThree

    z_value = stepFour

    # ========================================================
    # SIGMA CALCULATION
    # ========================================================
    #
    # Sigma =
    # std * sqrt(
    #     lambda / (2 - lambda)
    #     *
    #     [1 - (1 - lambda) ^ (2 * iteration)]
    # )
    # ========================================================

    stepFive = 2 - lambda_value

    stepSix = 1 - lambda_value

    stepSeven = 2 * iteration

    stepTen = lambda_value / stepFive

    stepEight = stepSix**stepSeven

    stepNine = 1 - stepEight

    stepEleven = stepTen * stepNine

    stepTwelve = np.sqrt(stepEleven)

    stepThirteen = std * stepTwelve

    sigma = stepThirteen

    # ========================================================
    # UCL
    # ========================================================
    #
    # UCL = Mean + (L * Sigma)
    # ========================================================

    stepFourteen = l * sigma

    stepFifteen = mean + stepFourteen

    ucl = stepFifteen

    # ========================================================
    # LCL
    # ========================================================
    #
    # LCL = Mean - (L * Sigma)
    # ========================================================

    stepSixteen = mean - stepFourteen

    lcl = stepSixteen

    # ========================================================
    # DRIFT
    # ========================================================
    #
    # Drift = True if Z is outside UCL or LCL
    # ========================================================

    drift = z_value > ucl or z_value < lcl

    # ========================================================
    # SAVE RESULT
    # ========================================================

    results.append(
        {
            "Iteration": iteration,
            "Activity": value,
            "Previous_Z": prevZ,
            "Z_Value": z_value,
            "Sigma": sigma,
            "UCL": ucl,
            "LCL": lcl,
            "Drift": drift,
        }
    )

    # ========================================================
    # IMPORTANT:
    # Use current Z as prevZ for the NEXT iteration.
    # ========================================================

    prevZ = z_value


# ============================================================
# CREATE RESULT DATAFRAME
# ============================================================

result_df = pd.DataFrame(results)


# ============================================================
# SAVE RESULT CSV
# ============================================================

result_df.to_csv(OUTPUT_FILE, index=False)


# ============================================================
# DISPLAY RESULT
# ============================================================

print("\nCalculation completed.")
print(f"Result saved to: {OUTPUT_FILE}")
print("\nResult:")
print(result_df.to_string(index=False))
