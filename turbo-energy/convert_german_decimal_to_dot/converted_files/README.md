# Converted Files

## Folder Purpose
This folder stores the standardized CSV files produced after replacing German comma decimals with standard dot decimals.

## What this folder does
- Holds clean, analysis-ready datasets where all numeric columns use standard floating-point formatting (e.g., `12.34`).
- Serves as the output target for `convert_german_decimal_to_dot/main.py`.

## Main files/components and their purpose
- `converted_status_code-1011-err_code-16-merged_CEMB_141E_141C_141A_141B_and_141D.csv`: Cleaned dataset combining CEMB balancing machines for status code 1011 and error code 16, with all numeric sensor values converted to standard floats.

## How it works
- Files in this directory are generated automatically when `main.py` is executed in the parent directory.

## Important notes or dependencies
- These files can be loaded directly into Pandas, NumPy, and SciPy for numerical analysis without further string replacement.
- Do not modify these generated files manually; regenerate them via `main.py` if the source data changes.
