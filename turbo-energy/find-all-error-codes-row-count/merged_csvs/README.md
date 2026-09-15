# Merged CSVs (Error Codes Pipeline)

## Folder Purpose
This folder stores merged datasets combining test records across all CEMB balancing machines, partitioned by status and error codes.

## What this folder does
- Aggregates multi-machine test runs into dedicated CSV files based on specific status and error codes.
- Serves as the primary data input for statistical and bell curve comparisons.

## Main files/components and their purpose
- `status_code-1001-err_code-0-merged_CEMB_141E_141C_141A_141B_and_141D.csv`: Pass dataset (status 1001, error 0).
- `status_code-1002-err_code-503-merged_CEMB_141E_141C_141A_141B_and_141D.csv`: Fail dataset (status 1002, error 503).
- `status_code-1002-err_code-513-merged_CEMB_141E_141C_141A_141B_and_141D.csv`: Fail dataset (status 1002, error 513).
- `status_code-1002-err_code-555-merged_CEMB_141E_141C_141A_141B_and_141D.csv`: Fail dataset (status 1002, error 555).
- `status_code-1011-err_code-16-merged_CEMB_141E_141C_141A_141B_and_141D.csv`: Fail dataset (status 1011, error 16).

## How it works
- Output by `main.py` after joining individual cleaned CSVs across CEMB stations.

## Important notes or dependencies
- Used by multiple analysis folders across the project.
