# Raw Data (Error Codes Pipeline)

## Folder Purpose
This folder stores the source Excel workbook used by the error codes row count pipeline.

## What this folder does
- Holds the original raw test log spreadsheet before any extraction or cleaning occurs.

## Main files/components and their purpose
- `Core Vs Balancing_Corelation.xlsx`: Master multi-sheet Excel file containing test data for CEMB machines 141A through 141E and core correlation records.

## How it works
- Read directly by `main.py` via `pandas.ExcelFile`.

## Important notes or dependencies
- Preserve this file as read-only to ensure original test logs remain untouched.
