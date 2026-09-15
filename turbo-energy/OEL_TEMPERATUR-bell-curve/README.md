# Oil Temperature Bell Curve Analysis

## Folder Purpose
This directory focuses specifically on normal distribution and bell curve analysis for the oil temperature parameter (`OEL_TEMPERATUR`).

## What this folder does
- Evaluates oil temperature behavior during balancing machine runs.
- Computes mean, standard deviation, min, and max for passed and failed test sets.
- Plots bell curves to determine whether oil temperature abnormalities correlate with failure codes.

## Main files/components and their purpose
- `pass-data.py`: Script analyzing oil temperature distribution for passed test records (status 1001, error 0).
- `fail-data.py`: Script analyzing oil temperature distribution for failed test records (status 1011, error 16).
- `pass-01001-0_merged_CEMB_141E_141C_141A_141B_and_141D.csv`: Pass dataset with oil temperature readings.
- `fail-1011-16_merged_CEMB_141E_141C_141A_141B_and_141D.csv`: Fail dataset with oil temperature readings.

## How it works
1. Scripts load the corresponding CSV dataset.
2. Converts German comma decimal strings in `OEL_TEMPERATUR` to floats (`.str.replace(",", ".").astype(float)`).
3. Calculates `mean` and `standardDeviation` using NumPy.
4. Plots Gaussian bell curves using `scipy.stats.norm.pdf` with Matplotlib.

## Important notes or dependencies
- Requires `matplotlib`, `numpy`, `pandas`, and `scipy`.
