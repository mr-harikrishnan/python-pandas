# Multiple Columns Bell Curve Comparison (Core Part Wise)

## Folder Purpose
This folder performs multi-parameter normal distribution comparisons between pass and fail test data for specific core part numbers.

## What this folder does
- Filters pass and fail datasets for a specific core part number (e.g., `40008447`).
- Analyzes multiple balancing measurements: `EB1_AUSLIEF_MG`, `EB2_AUSLIEF_MG`, `MD1_AUSLIEF_MG`, `MD2_AUSLIEF_MG`, and `MD3_AUSLIEF_MG`.
- Generates side-by-side normal distribution plots to compare pass vs fail distributions on identical scales.

## Main files/components and their purpose
- `main.py`: Python script loading pass/fail data, calculating Gaussian distributions, and plotting multi-column bell curves.
- `40008447-EB1_AUSLIEF_MG-EB2_AUSLIEF_MG.png`: Generated plot comparing distributions for `EB1` and `EB2` delivery unbalance.
- `40008447-MD1_AUSLIEF_MG-MD2_AUSLIEF_MG.png`: Generated plot comparing distributions for `MD1` and `MD2` delivery unbalance.
- `40008447-MD3_AUSLIEF_MG.png`: Generated plot showing distribution for `MD3` delivery unbalance.
- `merged-fail-data/`: Subfolder holding the merged fail CSV data.
- `merged-pass-data/`: Subfolder holding the merged pass CSV data.

## How it works
1. `main.py` loads fail data (status 1011, error 16) and pass data (status 1001, error 0).
2. Filters both datasets for the specified core part number.
3. Computes mean and standard deviation for each column.
4. Generates an x-axis range and computes y-values using `scipy.stats.norm.pdf`.
5. Renders and saves comparative plots with vertical dashed lines marking group means.

## Important notes or dependencies
- Requires `matplotlib`, `numpy`, `pandas`, and `scipy`.
- Column values are converted from comma strings to floats during execution.
