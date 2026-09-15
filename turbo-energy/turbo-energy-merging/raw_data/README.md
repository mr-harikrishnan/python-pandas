# Raw Data (Merging Pipeline)

## Folder Purpose
This folder holds the original source Excel workbook for the data merging pipeline.

## What this folder does
- Stores the raw multi-sheet Excel file before extraction.

## Main files/components and their purpose
- `Core Vs Balancing_Corelation.xlsx`: Original raw data file containing individual sheets for CEMB balancing machines 141A through 141E and core correlation data.

## How it works
- Read by `turbo-energy-merging/main.py` using `pandas.ExcelFile`.

## Important notes or dependencies
- This file should remain unmodified to preserve the original test logs.
