# Convert German Decimal to Dot

## Folder Purpose
This folder provides a utility to convert German decimal formatting (using commas `,`) into standard international decimal formatting (using dots `.`) for numeric data.

## What this folder does
- Reads raw CSV files containing test measurements formatted with German comma decimals (e.g., `12,34`).
- Replaces commas with decimal points across 18 critical sensor columns (e.g., `MD1_ANLIEF_MG`, `OEL_TEMPERATUR`, `PF_TORQUE`, etc.).
- Converts the cleaned columns into standard floating-point numbers.
- Writes the converted CSV file to the `converted_files/` directory for downstream analysis.

## Main files/components and their purpose
- `main.py`: Python script that reads the input CSV, converts comma strings to float numbers, and writes the output file.
- `data_files/`: Subfolder holding input CSV datasets with comma decimal formatting.
- `converted_files/`: Subfolder storing output CSV datasets with dot decimal formatting.

## How it works
1. The script loads an input CSV file from `./data_files/`.
2. It iterates through a predefined list of 18 continuous sensor columns.
3. For each column, it executes `.str.replace(",", ".").astype(float)`.
4. It exports the transformed DataFrame to `./converted_files/` using `to_csv(index=False)`.

## Important notes or dependencies
- Requires `pandas` and `os`.
- Always run this conversion before performing mathematical calculations on raw datasets exported from German CEMB balancing equipment.
