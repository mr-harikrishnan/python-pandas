# Activity Raw Value Visualization & ClickHouse Drift Comparison

## Folder Purpose
This folder visualizes and validates sensor activity values against precomputed drift classifications exported directly from ClickHouse.

## What this folder does
- Reads precomputed drift calculation results from ClickHouse (`clickhouse_drift_calculation_computed.csv`).
- Sorts records chronologically and maps drift states to distinct colors (drift = red, normal = blue).
- Plots the activity curve along with a reference mean line to visually verify database calculations.

## Main files/components and their purpose
- `main.py`: Visualization script that loads the dataset, maps drift flags to colors, and renders scatter/line plots.
- `readme.md`: Documentation note on plotting functionality.
- `clickhouse_drift_calculation_computed.csv`: Dataset containing timestamps, `activity_value`, `mean`, and ClickHouse-computed `drift` flags.

## How it works
1. Loads `clickhouse_drift_calculation_computed.csv` with Pandas.
2. Parses `source_timestamp` and removes duplicates.
3. Maps boolean drift flags: `1 -> red`, `0 -> blue`.
4. Plots a continuous time line with overlaid colored scatter points and a horizontal dashed line indicating the mean (`1.027288`).

## Important notes or dependencies
- Original note: `only plot the given data frame`.
- Requires `pandas` and `matplotlib`.
- Used to confirm whether database-computed drift points match expected visual thresholds.
