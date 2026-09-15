# Fail Datasets (Continuous Float Distribution)

## Folder Purpose
This folder holds the failure CSV datasets segmented by status code and error code for continuous float distribution analysis.

## What this folder does
- Provides failure data sources to `main.py` across multiple error conditions.

## Main files/components and their purpose
- `status_code-1002-err_code-503-merged_CEMB_141E_141C_141A_141B_and_141D.csv`: Error 503 fail data.
- `status_code-1002-err_code-513-merged_CEMB_141E_141C_141A_141B_and_141D.csv`: Error 513 fail data.
- `status_code-1002-err_code-555-merged_CEMB_141E_141C_141A_141B_and_141D.csv`: Error 555 fail data.
- `status_code-1011-err_code-16-merged_CEMB_141E_141C_141A_141B_and_141D.csv`: Error 16 fail data.
- Additional merged variants for cross-error comparisons.

## How it works
- Read by `main.py` to evaluate parameter distributions and identify zero-value columns.

## Important notes or dependencies
- Files contain standardized float values ready for statistical processing.
