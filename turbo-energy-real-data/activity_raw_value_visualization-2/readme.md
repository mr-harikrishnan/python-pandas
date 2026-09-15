# Activity Raw Value Visualization & SPC Drift Detection

## Folder Purpose
This folder visualizes time-series activity measurements and detects process drift using Exponentially Weighted Moving Average (EWMA) and Statistical Process Control (SPC) control limits.

## What this folder does
- Reads time-series activity data (`output.csv`).
- Removes duplicates and sorts timestamps in chronological order.
- Calculates moving EWMA Z-values and dynamic control limits: Upper Control Limit (UCL) and Lower Control Limit (LCL).
- Detects drift events when values exceed control limits and renders an annotated multi-color plot.

## Main files/components and their purpose
- `main.py`: Python script implementing the EWMA calculation, dynamic UCL/LCL calculation, drift identification, and Matplotlib plotting.
- `readme.md`: Documentation notes outlining manual calculation parameters.
- `output.csv`: Full time-series dataset of sensor activity values.
- `output-500.csv`: Subset of 500 rows for quick testing.
- `output2.csv`: Alternative test dataset.

## How it works
1. Parses timestamps and removes duplicate records.
2. Sets base statistical parameters: `mean = 1.0273`, `std = 0.013782`, `lambda_value = 0.04`, `l = 3`.
3. For each observation:
   - Computes smoothed `z = lambda_value * x + (1 - lambda_value) * prev_z`.
   - Computes dynamic standard deviation: `sigma = std * sqrt((lambda / (2 - lambda)) * (1 - (1 - lambda)**(2 * t)))`.
   - Calculates `UCL = mean + l * sigma` and `LCL = mean - l * sigma`.
   - Flags drift when `z > UCL` or `z < LCL`.
4. Plots raw points with drift anomalies highlighted in red and normal points in blue.

## Important notes or dependencies
- Original calculation parameters:
  - `manual calculation:`
  - `z value`
  - `lambda value`
  - `ucl`
  - `lcl`
  - `drift`
- Requires `pandas`, `matplotlib`, `numpy`, and `scipy`.
