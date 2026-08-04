# Data Quality Issues and Handling

## 1. Inconsistent Date Format

**Data Quality Issue**  
Dates are stored as text in different formats.

**What will you do?**  
Convert the `date` column to the `datetime` data type.

**Why?**  
Datetime is required for time-based analysis, sorting, filtering, and visualization.

---

## 2. Service Record in Fuel Data

**Data Quality Issue**  
One row is a service record instead of a petrol refill.

**What will you do?**  
Exclude the service record from all fuel-spending and fuel-consumption analyses.

**Why?**  
It does not represent a fuel purchase and would distort fuel-related calculations.

---

## 3. Missing `price_inr` Value

**Data Quality Issue**  
The `price_inr` value is missing in the service record.

**What will you do?**  
Keep the value as `NaN` and exclude the service record from fuel-related charts and calculations.

**Why?**  
The row is not a petrol refill, so estimating a fuel price would be inaccurate.

---

## 4. Missing Odometer Readings

**Data Quality Issue**  
Some `odometer_km` values are missing.

**What will you do?**  
Keep the missing values as `NaN` and perform odometer-based analyses only on records with available readings.

**Why?**  
The actual odometer readings are unknown and should not be estimated.

---

## 5. Missing Fuel Quantity and Rate

**Data Quality Issue**  
Several `litres` and `rate_inr_per_litre` values are missing.

**What will you do?**  
Keep the missing values as `NaN` and use only records with available values for litre-based analysis.

**Why?**  
The actual values are unknown and should not be estimated.