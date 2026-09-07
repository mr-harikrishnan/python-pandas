import pandas as pd
import numpy as np
from scipy.stats import t


def main():

    # A user claims that the average height of students is 170 cm.

    claimed_population_mean = 170  # cm

    confidence_level = 95  # %

    df = pd.read_csv("./student_height_data.csv")

    df = df.sample(n=10, random_state=42)

    mean = np.mean(df["height"])

    print(" ")

    print("claimed_population_mean :", claimed_population_mean)

    print(" ")

    print("calculated_sample_mean :", mean)

    print(" ")

    print("Next step find Standard Deviation")

    print(" ")

    sample_std = np.std(
        df["height"], ddof=1
    )  # this is sample data test so ddof value is 1.#Degrees of Freedom Value

    print("sample_standard_deviation :", sample_std)

    print("")

    print()

    print("Next step: Calculate Standard Error")

    sample_size = len(df)

    standard_error = sample_std / np.sqrt(sample_size)

    print("sample_size :", sample_size)
    print("standard_error :", standard_error)

    print(" ")

    print("Next step: Calculate T Value")

    # H0: population mean = 170
    # H1: population mean != 170

    t_value = (mean - claimed_population_mean) / standard_error

    print("t_value :", t_value)

    print(" ")

    print("Next step: Calculate Degrees of Freedom")

    degrees_of_freedom = sample_size - 1

    print("degrees_of_freedom :", degrees_of_freedom)

    print(" ")

    print("Next step: Calculate P Value")

    # Two-tailed test because H1 is population mean != 170

    p_value = 2 * t.sf(abs(t_value), df=degrees_of_freedom)

    print("p_value :", p_value)

    print(" ")

    print("Next step: Decision Rule")

    alpha = 1 - (confidence_level / 100)

    print("alpha :", alpha)

    print(" ")

    if p_value < alpha:

        print("Decision Rule: p-value < alpha")

        print("Reject H0")

    else:

        print("Decision Rule: p-value >= alpha")

        print("Fail to Reject H0")

    print(" ")

    print("Final Result")

    if p_value < alpha:

        print("There is sufficient evidence to reject the claim.")

        print("The population mean height is significantly different from 170 cm.")

    else:

        print("There is not sufficient evidence to reject the claim.")

        print("The population mean height is not significantly different from 170 cm.")


main()
