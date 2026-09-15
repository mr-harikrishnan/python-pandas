# Cleaned CSVs (Merging Pipeline)

## Folder Purpose
This folder stores normalized CSV files extracted from individual sheets of the master Excel workbook.

## What this folder does
- Contains per-machine test records cleaned of redundant headers and duplicate rows.

## Main files/components and their purpose
- `cleaned_CEMB_141A.csv`: Cleaned data for balancing machine CEMB 141A.
- `cleaned_CEMB_141B.csv`: Cleaned data for balancing machine CEMB 141B.
- `cleaned_CEMB_141C.csv`: Cleaned data for balancing machine CEMB 141C.
- `cleaned_CEMB_141D.csv`: Cleaned data for balancing machine CEMB 141D.
- `cleaned_CEMB_141E.csv`: Cleaned data for balancing machine CEMB 141E.
- `cleaned_Core.csv`: Cleaned core correlation data.

## How it works
- Output by `turbo-energy-merging/main.py`.

## Important notes or dependencies
- Used as intermediate files to build merged multi-station datasets.
