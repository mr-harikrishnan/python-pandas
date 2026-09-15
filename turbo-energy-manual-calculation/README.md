# Turbo Energy Manual Calculation

## Folder Purpose
This folder provides step-by-step mathematical demonstration and verification of Statistical Process Control (SPC) drift calculations using Exponentially Weighted Moving Average (EWMA).

## What this folder does
- Breaks down the EWMA formula into explicit arithmetic steps with printed console output.
- Validates the mathematical derivation of the smoothed Z-value, lambda weighting, and control limits.
- Ensures calculation formulas match theoretical SPC equations before applying them to larger datasets.

## Main files/components and their purpose
- `main.py`: Interactive script demonstrating step-by-step calculation of `z = lambda * value + (1 - lambda) * prevZ` with sample parameters.
- `loop/`: Subfolder applying this formula iteratively across rows in a CSV file.

## How it works
1. Given parameters: `mean = 2.148216`, `std = 0.122471`, `lambda_ = 0.02`, `l = 2`.
2. Step 1: Computes `lambda_ * value`.
3. Step 2: Computes `1 - lambda_`.
4. Step 3: Computes `(1 - lambda_) * prevZ`.
5. Step 4: Adds Step 1 and Step 3 to obtain the new Z-value.
6. Prints each step and intermediate result to the console for verification.

## Important notes or dependencies
- Requires `numpy`.
- Useful for validating the logic behind automated drift detection scripts.
