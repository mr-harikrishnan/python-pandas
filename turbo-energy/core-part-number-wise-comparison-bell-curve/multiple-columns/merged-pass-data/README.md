# Merged Pass Data (Core Part Wise - Multiple Columns)

## Folder Purpose
This folder stores merged pass test records used for multi-column core part number distribution analysis.

## What this folder does
- Provides baseline passed test records across all CEMB balancing stations to `multiple-columns/main.py`.

## Main files/components and their purpose
- `status_code-1001-err_code-0-merged_CEMB_141E_141C_141A_141B_and_141D.csv`: Combined CSV dataset of passed tests with status code 1001 and error code 0 across machines 141A, 141B, 141C, 141D, and 141E.

## How it works
- The parent script reads this CSV to establish baseline normal distributions for comparison against failed parts.

## Important notes or dependencies
- Contains successful balancing runs used as benchmark data.
