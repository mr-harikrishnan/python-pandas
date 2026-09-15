# Merged Fail Data (Core Part Wise - Multiple Columns)

## Folder Purpose
This folder stores merged failure test records used for multi-column core part number distribution analysis.

## What this folder does
- Supplies failed test records across all CEMB balancing stations to `multiple-columns/main.py`.

## Main files/components and their purpose
- `status_code-1011-err_code-16-merged_CEMB_141E_141C_141A_141B_and_141D.csv`: Combined CSV dataset of failed tests with status code 1011 and error code 16 across machines 141A, 141B, 141C, 141D, and 141E.

## How it works
- The parent script reads this CSV to extract fail records for target core part numbers.

## Important notes or dependencies
- Decimal commas are converted to dots dynamically within the analysis script.
- Source data represents machines CEMB 141A through 141E.
