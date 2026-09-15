# Pass/Fail Distribution Comparison (Selected Columns)

## Folder Purpose
This directory performs comparative normal distribution analysis between pass and fail datasets across selected sensor parameters.

## What this folder does
- Compares distributions of key manufacturing variables between passed tests (status 1001, error 0) and failed tests (status 1011, error 16).
- Highlights differences in parameters such as delivery unbalance (`MD1_ANLIEF_MG`), oil pressure (`OEL_DRUCK`), and oil temperature (`OEL_TEMPERATUR`).

## Main files/components and their purpose
- `pass_fail_distribution_comparison.py`: Script calculating distributions and plotting overlaid bell curves for selected columns.
- `status_code-1001-err_code-0-merged_CEMB_141E_141C_141A_141B_and_141D.csv`: Pass baseline dataset.
- `status_code-1011-err_code-16-merged_CEMB_141E_141C_141A_141B_and_141D.csv`: Target failure dataset.

## How it works
1. Loads pass and fail CSV datasets.
2. Standardizes comma decimals to numeric float values.
3. Computes Gaussian distribution parameters (mean, standard deviation) for each specified column.
4. Overlays pass and fail probability density curves to visualize variance and displacement.

## Important notes or dependencies
- Requires `matplotlib`, `numpy`, `pandas`, and `scipy`.
