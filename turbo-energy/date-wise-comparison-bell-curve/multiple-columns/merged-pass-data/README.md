# Merged Pass Data (Date Wise - Multiple Columns)

## Folder Purpose
This folder stores merged pass test records used for date-wise multi-column distribution analysis.

## What this folder does
- Provides benchmark passed test data (status 1001, error 0) across CEMB machines to `multiple-columns/main.py`.

## Main files/components and their purpose
- `status_code-1001-err_code-0-merged_CEMB_141E_141C_141A_141B_and_141D.csv`: Merged CSV dataset of passed tests.

## How it works
- Filtered by `DATUM` in the parent script to establish the pass baseline for that day.

## Important notes or dependencies
- Represents nominal passed test runs.
