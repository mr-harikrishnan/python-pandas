import pandas as pd
import matplotlib.pyplot as plt


def loadCsv():
 
 df=pd.read_csv("./car_petrol_log.csv")

 return df


def dateFomatChange(df):

 df["date"] = df["date"].str.strip()

 df["date"] = pd.to_datetime(df["date"],format="mixed",dayfirst=True)

 return df
 

def main():

 ## Part 1 — Load and prepare


 
# 1. Load the CSV. Parse `date` into a proper datetime column. 
# Note the dates are in mixed text formats ("June 1 2025", "Sept 5 2025", "March 1 2026") — handle this in code, 
# not by editing the CSV.

 df = loadCsv()

 df = dateFomatChange(df)

 # 2. Identify every data quality issue you can find and list them in a markdown cell. 
# For each one, state **what you will do about it and why**.

# 3. Any row you exclude or 
# any value you estimate must be documented with a `# WHY:` comment. A `# WHY:` comment defends a decision — it 
# does not restate the operation.

#completed task 2 and 3 data-quality-issue.md



## Part 2 — Required charts

 


main()