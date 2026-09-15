# Multiple Columns Bell Curve Comparison (Date Wise)

## Folder Purpose
This folder performs multi-parameter normal distribution comparisons between pass and fail data for specific production dates.

## What this folder does
- Filters pass and fail datasets for a specific date (e.g., `12.02.2024`).
- Evaluates multiple balancing parameters: `EB1_AUSLIEF_MG`, `EB2_AUSLIEF_MG`, `MD1_AUSLIEF_MG`, `MD2_AUSLIEF_MG`, and `MD3_AUSLIEF_MG`.
- Outputs comparison bell curve charts saved as PNG images.

## Main files/components and their purpose
- `main.py`: Python script that filters by date, computes Gaussian normal curves, and renders plots.
- `12.02.2024-EB1_AUSLIEF_MG-EB2_AUSLIEF_MG.png`: Plot comparing EB1 and EB2 distributions on 12.02.2024.
- `12.02.2024-MD1_AUSLIEF_MG-MD2_AUSLIEF_MG.png`: Plot comparing MD1 and MD2 distributions on 12.02.2024.
- `12.02.2024-MD3_AUSLIEF_MG.png`: Plot showing MD3 distribution on 12.02.2024.
- `merged-fail-data/`: Holds the merged fail CSV dataset.
- `merged-pass-data/`: Holds the merged pass CSV dataset.

## How it works
1. `main.py` reads pass and fail CSV files.
2. Filters records where `DATUM == inputDate`.
3. Normalizes numeric columns from German comma strings to floats.
4. Computes probability density functions using `scipy.stats.norm.pdf`.
5. Saves visual charts showing pass and fail curves side-by-side.

## Important notes or dependencies
- Requires `matplotlib`, `numpy`, `pandas`, and `scipy`.
- Date format in the dataset matches `DD.MM.YYYY`.
