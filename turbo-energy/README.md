# Turbo Energy Analysis

## Folder Purpose
This is the root directory for the Turbo Energy project, focused on statistical data analysis, process capability studies, and quality control of automotive turbocharger test data from CEMB balancing machines.

## What this folder does
- Ingests raw Excel test logs from balancing machines (CEMB 141A, 141B, 141C, 141D, and 141E) and core correlation files.
- Converts German-style comma decimal notations into standard numeric float decimals.
- Merges multi-station test data and separates records by pass/fail status and specific error codes.
- Conducts normal distribution (bell curve) comparative analysis across core part numbers, test dates, and continuous float sensor parameters.
- Generates visual distribution plots and markdown summary reports to identify process drift and root causes of test failures.

## Main files/components and their purpose
- `convert_german_decimal_to_dot/`: Pipeline to convert German comma decimal numbers to standard dot decimals.
- `core-part-number-wise-comparison-bell-curve/`: Scripts and plots comparing pass vs fail normal distributions grouped by core part numbers.
- `date-wise-comparison-bell-curve/`: Scripts and plots comparing pass vs fail normal distributions grouped by production dates.
- `find-all-error-codes-row-count/`: Extracts all status and error codes from raw Excel sheets and summarizes their row counts and frequency distributions.
- `OEL_TEMPERATUR-bell-curve/`: Focused bell curve analysis on the oil temperature (`OEL_TEMPERATUR`) parameter.
- `pass_fail_distribution_comparison_selected_columns/`: Multi-parameter normal distribution comparison between pass records and failure error codes.
- `pass_fail_distribution_continuous_data_float_value_columns/`: Deep-dive pipeline evaluating continuous float sensor variables across error codes (503, 513, 555, 16).
- `turbo-energy-merging/`: Data preparation pipeline extracting, cleaning, and merging raw Excel sheets into categorized CSV files.

## How it works
1. Raw machine test data is cleaned and merged across balancing stations.
2. Datasets are partitioned into passed tests (STATUS 1001 / DOK 0) and failed tests (such as STATUS 1002, 1011 with various error codes).
3. Statistical metrics (mean, standard deviation, min, max) are calculated using NumPy and SciPy.
4. Normal probability density functions (`norm.pdf`) are plotted over sensor values to visually identify where failed parts diverge from passing parts.

## Important notes or dependencies
- Requires Python 3 with `pandas`, `numpy`, `scipy`, `matplotlib`, and `tabulate`.
- All subfolders contain modular scripts tailored to specific dimensions of the balancing test data.
