# Turbo Energy Real Data Analysis

## Folder Purpose
This directory contains tools and workflows for analyzing real-world time-series sensor telemetry, converting Apache Parquet data, detecting SPC drift, and generating visual plots.

## What this folder does
- Converts large Apache Parquet files exported from ClickHouse databases into Pandas DataFrames and CSV files.
- Analyzes time-series activity and torque sensor measurements.
- Implements SPC EWMA drift detection to identify anomalous operational shifts.
- Visualizes time-series activity, control boundaries (UCL/LCL), and compares Python-computed drift against ClickHouse database calculations.

## Main files/components and their purpose
- `activity_raw_value_visualization/`: Visualizes raw time-series sensor values and inspects duplicate timestamps.
- `activity_raw_value_visualization-2/`: Computes EWMA, UCL, and LCL, and visualizes drift points on time-series plots.
- `activity_raw_value_visualization-compare/`: Visualizes and compares precomputed ClickHouse drift classifications against sensor curves.
- `ParquetfiletoDataFrame/`: Utilities and datasets for converting ClickHouse Parquet files to DataFrames and filtered CSVs.

## How it works
1. Telemetry data from ClickHouse is loaded from Parquet files into DataFrames.
2. Timestamps are parsed, sorted chronologically, and deduplicated.
3. Statistical limits (mean, standard deviation, EWMA Z, UCL, LCL) are calculated.
4. Time-series graphs are plotted with drift points highlighted in contrasting colors.

## Important notes or dependencies
- Requires `pandas`, `numpy`, `scipy`, `matplotlib`, and `fastparquet` or `pyarrow`.
