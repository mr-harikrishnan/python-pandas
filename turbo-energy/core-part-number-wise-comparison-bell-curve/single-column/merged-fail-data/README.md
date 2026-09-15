# Merged Fail Data (Core Part Wise - Single Column)

## Folder Purpose
This folder holds the merged failure test records used for single-column core part distribution comparisons.

## What this folder does
- Provides failed test data (status 1011, error 16) across CEMB machines to `single-column/main.py`.

## Main files/components and their purpose
- `status_code-1011-err_code-16-merged_CEMB_141E_141C_141A_141B_and_141D.csv`: Combined CSV dataset of failed tests.

## How it works
- Filtered by core part number in `single-column/main.py`.

## Important notes or dependencies
- Contains status code 1011 and error code 16 records.
