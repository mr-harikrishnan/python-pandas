# Single Column Bell Curve Comparison (Core Part Wise)

## Folder Purpose
This folder performs detailed normal distribution analysis for a single chosen sensor column, segmented by core part number.

## What this folder does
- Compares a single metric (e.g., `MD2_AUSLIEF_MG`) between passing parts and failing parts for a specific core part number.
- Isolates individual parameters to avoid visual clutter and provide detailed distribution statistics.

## Main files/components and their purpose
- `main.py`: Python script filtering by core part number and plotting single-parameter bell curves for pass vs fail groups.
- `merged-fail-data/`: Subfolder holding the merged fail CSV data.
- `merged-pass-data/`: Subfolder holding the merged pass CSV data.

## How it works
1. Loads pass and fail datasets from the respective subfolders.
2. Filters records matching the target core part number.
3. Converts the selected column from string to float.
4. Computes mean and standard deviation for pass and fail groups.
5. Plots overlaid bell curves with labeled means and legends using Matplotlib.

## Important notes or dependencies
- Requires `matplotlib`, `numpy`, `pandas`, and `scipy`.
