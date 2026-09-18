import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

def main():

    final_cohencd_effect_df = pd.read_csv("./welch_ttest_results-with-cohens-d-effect.csv")

    print(final_cohencd_effect_df.coumns)

main()