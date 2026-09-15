# EWMA Calculation Loop

## Folder Purpose
This folder applies the EWMA drift calculation iteratively over a series of records loaded from a CSV file.

## What this folder does
- Reads time-series activity data (`Parquiet-11-09-datas-10.csv`).
- Iterates row by row, updating the smoothed Z-value using EWMA.
- Calculates dynamic standard deviation `sigma_z`, Upper Control Limit (`UCL`), and Lower Control Limit (`LCL`).
- Flags drift conditions (`True`/`False`) when the smoothed value crosses control limits.
- Exports calculated results to `activity_calculation_result.csv`.

## Main files/components and their purpose
- `main.py`: Python script executing the iterative EWMA and drift calculation loop.
- `Parquiet-11-09-datas-10.csv`: Input CSV containing sample activity values.
- `activity_calculation_result.csv`: Output CSV storing input data along with calculated `z_value`, `sigma_z`, `ucl`, `lcl`, and `drift` flag.

## How it works
1. Loads CSV and verifies the presence of the activity column.
2. Initializes `prev_z = mean`.
3. For each iteration `t`:
   - `z = lambda_value * x_t + (1 - lambda_value) * prev_z`
   - `sigma_z = std * sqrt((lambda_value / (2 - lambda_value)) * (1 - (1 - lambda_value)**(2 * t)))`
   - `UCL = mean + l * sigma_z`
   - `LCL = mean - l * sigma_z`
   - `drift = (z > UCL) or (z < LCL)`
4. Appends calculated values and saves the resulting DataFrame.

## Important notes or dependencies
- Requires `numpy` and `pandas`.
- Serves as a reference implementation for streaming or row-by-row drift detection.
