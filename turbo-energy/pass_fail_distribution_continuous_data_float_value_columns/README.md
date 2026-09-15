# Pass/Fail Distribution of Continuous Float Columns

## Folder Purpose
This directory contains an automated analysis suite that inspects continuous float-valued sensor columns across multiple failure modes (error codes).

## What this folder does
- Scans continuous numeric sensor columns across fail datasets for status 1002 (errors 503, 513, 555) and status 1011 (error 16).
- Checks for zero values or unrecorded parameters.
- Generates normal distribution comparison plots comparing pass vs fail for each continuous metric.
- Compiles structured markdown reports summarizing zero-value findings and distribution statistics for each error code.

## Main files/components and their purpose
- `main.py`: Main orchestration script scanning columns, calculating normal distributions, rendering plots, and generating reports.
- `test.txt`: Reference text file listing candidate continuous sensor column names.
- `distribution_plots/`: Directory containing generated PNG bell curve charts organized by error code.
- `fail-datas/`: Directory holding CSV datasets for various failure modes.
- `pass-datas/`: Directory holding baseline pass CSV dataset.
- `report/`: Directory containing generated markdown summary reports.

## How it works
1. Reads candidate sensor columns from the datasets.
2. Evaluates presence of 0 or null values per column for each failure mode.
3. Computes mean and standard deviation for pass and fail groups.
4. Generates visual bell curve plots saved to `distribution_plots/`.
5. Compiles comprehensive markdown findings saved to `report/`.

## Important notes or dependencies
- Requires `pandas`, `numpy`, `scipy`, and `matplotlib`.
