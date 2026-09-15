# Parquet File to DataFrame & CSV Converter

## Folder Purpose
This folder provides utilities and datasets for converting Apache Parquet telemetry files into Pandas DataFrames and CSV formats, and filtering drift records.

## What this folder does
- Ingests Apache Parquet telemetry files exported from ClickHouse or industrial logging systems.
- Converts Parquet data into CSV format for easy exploration in Pandas or spreadsheet software.
- Filters and extracts subsets of interest, such as records where drift occurred (`drift == 1`).

## Main files/components and their purpose
- `main.py`: Python script converting Parquet files to CSV and filtering drift rows.
- `readme.md`: Documentation note describing the converter purpose.
- Multiple `.parquet` files:
  - `Parquiet-11-09.parquet`: Main telemetry Parquet dataset.
  - `clickhouse_drift_calculation_computed.parquet`: ClickHouse computed drift results.
  - `final_torque-10-9_5-5.parquet`: Torque telemetry data.
  - `final_torque_computed_drifting.parquet`: Torque drift calculations.
  - `result.parquet`, `result (1).parquet`: Query result exports.
- Multiple `.csv` files:
  - `Parquiet-11-09.csv`: Converted telemetry CSV.
  - `Parquiet-11-09-datas-10-drift-true.csv`: Sample subset containing positive drift records.
  - `clickhouse_drift_calculation_computed.csv`: Converted drift calculation CSV.

## How it works
1. Uses `pd.read_parquet("<filename>.parquet")` to load Parquet files.
2. Exports full datasets using `df.to_csv("<filename>.csv", index=False)`.
3. Filters rows where `df["drift"] == 1` and saves targeted sample subsets for verification.

## Important notes or dependencies
- Original note: `parquet to csv dat frame`.
- Requires `pandas` and a parquet engine (`fastparquet` or `pyarrow`).
- Enables cross-tool compatibility between columnar storage and row-oriented analysis tools.
