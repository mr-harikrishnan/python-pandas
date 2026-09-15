# Merged Pass Data (Core Part Wise - Single Column)

## Folder Purpose
This folder holds the merged pass test records used for single-column core part distribution comparisons.

## What this folder does
- Provides benchmark passed test data (status 1001, error 0) across CEMB machines to `single-column/main.py`.

## Main files/components and their purpose
- `status_code-1001-err_code-0-merged_CEMB_141E_141C_141A_141B_and_141D.csv`: Combined CSV dataset of passed tests.

## How it works
- Filtered by core part number in `single-column/main.py` to establish the baseline normal curve.

## Important notes or dependencies
- Represents nominal manufacturing operating conditions.
