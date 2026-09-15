# Merged Fail Data (Date Wise - Multiple Columns)

## Folder Purpose
This folder stores merged failure test records used for date-wise multi-column distribution analysis.

## What this folder does
- Provides failed test data (status 1011, error 16) across CEMB machines to `multiple-columns/main.py`.

## Main files/components and their purpose
- `status_code-1011-err_code-16-merged_CEMB_141E_141C_141A_141B_and_141D.csv`: Merged CSV dataset of failed tests.

## How it works
- Filtered by `DATUM` in the parent script.

## Important notes or dependencies
- Contains status code 1011 and error code 16 records across all five CEMB machines.
