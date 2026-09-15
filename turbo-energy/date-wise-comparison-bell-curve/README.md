# Date Wise Bell Curve Comparison

## Folder Purpose
This directory contains tools and data for comparing normal distribution bell curves between pass and fail test records grouped by production date (`DATUM`).

## What this folder does
- Tracks manufacturing quality over time by analyzing parameter distributions on specific dates.
- Detects daily calibration shifts, environmental influences, or day-specific defect spikes.

## Main files/components and their purpose
- `multiple-columns/`: Analyzes multiple sensor columns across dates.
- `single-column/`: Analyzes a single chosen sensor column for an interactively selected date.

## How it works
1. Pass and fail datasets are filtered by date (`DATUM`).
2. Mean, standard deviation, and normal probability density functions are computed.
3. Graphs compare pass vs fail distributions for the selected date.

## Important notes or dependencies
- Requires `pandas`, `numpy`, `scipy`, and `matplotlib`.
