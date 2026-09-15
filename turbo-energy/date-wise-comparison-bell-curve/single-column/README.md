# Single Column Bell Curve Comparison (Date Wise)

## Folder Purpose
This folder enables single-parameter normal distribution comparisons between pass and fail data for a specific production date.

## What this folder does
- Focuses on a single sensor column for a given date.
- Prompts for or specifies a date and column name, then plots overlaid bell curves comparing passing and failing parts.

## Main files/components and their purpose
- `main.py`: Interactive script for date-wise single-column normal distribution comparison.
- `merged-fail-data/`: Holds the merged fail CSV dataset.
- `merged-pass-data/`: Holds the merged pass CSV dataset.

## How it works
1. Loads pass and fail CSV datasets.
2. Filters by the target `DATUM`.
3. Converts the chosen column to float.
4. Calculates mean and standard deviation.
5. Displays overlaid bell curves using Matplotlib.

## Important notes or dependencies
- Requires `matplotlib`, `numpy`, `pandas`, and `scipy`.
