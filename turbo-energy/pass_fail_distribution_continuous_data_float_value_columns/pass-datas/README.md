# Pass Datasets (Continuous Float Distribution)

## Folder Purpose
This folder holds the baseline pass CSV dataset used for continuous float distribution analysis.

## What this folder does
- Provides normal operation benchmark records (status 1001, error 0) across CEMB machines.

## Main files/components and their purpose
- `status_code-1001-err_code-0-merged_CEMB_141E_141C_141A_141B_and_141D.csv`: Merged pass dataset.

## How it works
- Read by `main.py` to compute benchmark mean and standard deviation curves.

## Important notes or dependencies
- Benchmark dataset against which all failure modes are contrasted.
