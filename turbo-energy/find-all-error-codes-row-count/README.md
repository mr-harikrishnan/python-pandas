# Find All Error Codes Row Count

## Folder Purpose
This directory contains an end-to-end data pipeline that ingests raw multi-tab Excel workbooks, extracts and cleans data for each CEMB machine, merges them, and analyzes error code row counts.

## What this folder does
- Reads the multi-sheet workbook `Core Vs Balancing_Corelation.xlsx`.
- Cleans and exports each individual machine sheet (CEMB 141A to 141E, and Core) to CSV.
- Merges data across stations, preventing column name collisions.
- Groups test records by `STATUS` and error code `DOK`.
- Produces a markdown report (`report.md`) detailing row counts per error code and machine.
- Generates a bar plot (`status_1002_error_code_distribution.png`) visualizing error code frequencies.

## Main files/components and their purpose
- `main.py`: Complete pipeline script performing extraction, cleaning, merging, error count aggregation, and reporting.
- `report.md`: Summary markdown report containing row count tables and execution logs.
- `status_1002_error_code_distribution.png`: Bar chart of error code distributions under status code 1002.
- `cleaned_csvs/`: Directory holding individual machine CSV files.
- `merged_csvs/`: Directory holding merged datasets by status and error code.
- `raw_data/`: Directory holding the raw Excel workbook.

## How it works
1. `main.py` opens `Core Vs Balancing_Corelation.xlsx`.
2. Cleans each sheet, removes duplicates, and saves to `cleaned_csvs/`.
3. Merges machine datasets with core correlation data.
4. Tallies row counts for each status and error code.
5. Saves merged CSV datasets and outputs `report.md` and distribution plots.

## Important notes or dependencies
- Requires `pandas`, `openpyxl`, `tabulate`, and `matplotlib`.
