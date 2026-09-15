# Core Part Number Wise Bell Curve Comparison

## Folder Purpose
This directory contains tools and datasets for comparing normal distribution bell curves between passed and failed parts, categorized by core part numbers (`Part Number_Core`).

## What this folder does
- Segregates balancing test records by specific core part numbers.
- Compares sensor parameter distributions between passed assemblies (status 1001, error 0) and failed assemblies (status 1011, error 16).
- Determines whether specific core part designs exhibit distinct failure characteristics or unbalance patterns.

## Main files/components and their purpose
- `multiple-columns/`: Scripts and plots comparing multiple sensor parameters simultaneously for a given core part number.
- `single-column/`: Scripts comparing a single specific parameter (e.g., `MD2_AUSLIEF_MG`) for a given core part number.

## How it works
1. Merged pass and fail datasets are filtered for matching core part numbers.
2. Numeric values are normalized to floats.
3. Mean and standard deviation are calculated for each group.
4. Bell curve distributions are plotted using Gaussian probability density functions to visualize overlap and divergence.

## Important notes or dependencies
- Relies on `pandas`, `numpy`, `scipy`, and `matplotlib`.
- Data originates from merged CEMB balancing machines (141A through 141E).
