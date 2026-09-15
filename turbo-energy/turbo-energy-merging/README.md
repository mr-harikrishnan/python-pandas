# Turbo Energy Merging Pipeline

## Folder Purpose
This directory contains the core data extraction, cleaning, and merging pipeline that processes the raw multi-sheet Excel file into standardized CSV datasets.

## What this folder does
- Reads the master Excel workbook `Core Vs Balancing_Corelation.xlsx`.
- Normalizes and exports each machine sheet to CSV.
- Resolves duplicate column names between joined tables (appending `_2`, `_3`, etc.).
- Merges test records across balancing stations CEMB 141A through 141E and core correlation records.
- Partitions the merged dataset into distinct CSV files based on pass status and error codes.
- Writes an audit log (`report.md`) detailing row counts at each step.

## Main files/components and their purpose
- `main.py`: The ETL pipeline script implementing the extraction, cleaning, merging, and exporting functions.
- `report.md`: Markdown log recording before-and-after row counts for cleaning and merging operations.
- `cleaned_csvs/`: Directory holding individual machine CSV files.
- `merged_csvs/`: Directory holding combined multi-machine CSV datasets.
- `raw_data/`: Directory holding the raw source Excel file.

## How it works
1. Loads sheets `CEMB 141A` through `141E` and `Core`.
2. Cleans records by dropping duplicate rows and filtering valid status and error codes.
3. Merges machine data with core correlation attributes.
4. Splits the combined DataFrame into pass and error-specific subsets.
5. Saves CSV files to `merged_csvs/` and logs row counts in `report.md`.

## Important notes or dependencies
- Requires `pandas`, `tabulate`, and `openpyxl`.
- This is the baseline data preparation step for the entire `turbo-energy` analysis repository.
