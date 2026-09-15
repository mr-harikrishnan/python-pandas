# Activity Raw Value Visualization

## Folder Purpose
This folder inspects, cleans, and visualizes raw sensor activity measurements over time from telemetry exports.

## What this folder does
- Reads raw time-series CSV data (`output.csv`).
- Converts timestamps to datetime objects and checks for duplicate rows and timestamps.
- Cleans and sorts data chronologically.
- Plots activity raw values against timestamps to visualize signal behavior.

## Main files/components and their purpose
- `main.py`: Python script loading `output.csv`, reporting duplicate counts, sorting records, and rendering time-series plots.
- `main2.py`: Exploration script testing SPC parameters (mean, standard deviation, lambda, L) and drift flags on the dataset.
- `output.csv`: Input CSV file containing `source_timestamp` and `activity_raw_value`.

## How it works
1. Loads `output.csv` using Pandas.
2. Converts `source_timestamp` using `pd.to_datetime`.
3. Detects and removes duplicates via `.drop_duplicates(keep="first")`.
4. Sorts values chronologically.
5. Renders time-series line plots using Matplotlib.

## Important notes or dependencies
- Requires `pandas`, `matplotlib`, `numpy`, and `scipy`.
- Essential preliminary step to inspect raw data quality before applying control limits.
