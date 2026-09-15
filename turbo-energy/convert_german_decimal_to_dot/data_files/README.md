# Data Files (Input)

## Folder Purpose
This folder contains the raw input CSV files that use German comma decimal formatting.

## What this folder does
- Provides source data files containing German decimal notation (e.g., `10,5` instead of `10.5`) for conversion.
- Feeds into the conversion script in `convert_german_decimal_to_dot/main.py`.

## Main files/components and their purpose
- `status_code-1011-err_code-16-merged_CEMB_141E_141C_141A_141B_and_141D.csv`: Raw merged balancing test data for status code 1011 and error code 16, with sensor readings containing comma decimals.

## How it works
- The conversion script reads files directly from this folder using relative path `./data_files/<filename>.csv`.

## Important notes or dependencies
- These files contain comma-separated decimals in numeric fields, so standard numeric parsing without string replacement will treat them as objects/strings.
- Preserve original files here as reference inputs.
