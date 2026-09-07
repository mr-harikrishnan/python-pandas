import pandas as pd
import numpy as np
from scipy.stats import t


def findMeanAndStd(df):

    mean = np.mean(df["height"])

    standard_deviation = np.std(df["height"], ddof=1)

    return mean, standard_deviation


def findStandardError(standard_deviation, sample_size):

    standard_error = standard_deviation / np.sqrt(sample_size)

    return standard_error


def findTValue(mean, claimed_population_mean, standard_error):

    t_value = (mean - claimed_population_mean) / standard_error

    return t_value


def findDegreesOfFreedom(sample_size):

    degrees_of_freedom = sample_size - 1

    return degrees_of_freedom


def findPValue(t_value, degrees_of_freedom):

    # Two-tailed test

    p_value = 2 * t.sf(abs(t_value), df=degrees_of_freedom)

    return p_value


def findAlpha(confidence_level):

    alpha = 1 - (confidence_level / 100)

    return alpha


def makeDecision(p_value, alpha):

    if p_value < alpha:

        return "Reject H0"

    else:

        return "Fail to Reject H0"


def main():

    claimed_population_mean = 170  # cm

    confidence_level = 95  # %

    df = pd.read_csv("./student_height_data.csv")

    df = df.sample(n=10, random_state=42)

    mean, standard_deviation = findMeanAndStd(df)

    sample_size = sample_size = len(df)

    standard_error = findStandardError(standard_deviation, sample_size)

    # H0: population mean = 170
    # H1: population mean != 170

    t_value = findTValue(mean, claimed_population_mean, standard_error)

    degrees_of_freedom = sample_size - 1

    p_value = findPValue(t_value, degrees_of_freedom)

    alpha = findAlpha(confidence_level)

    decision = makeDecision(p_value, alpha)

    print("sample_mean :", mean)

    print("sample_standard_deviation :", standard_deviation)

    print("sample_size :", sample_size)

    print("standard_error :", standard_error)

    print("t_value :", t_value)

    print("degrees_of_freedom :", degrees_of_freedom)

    print("p_value :", p_value)

    print("alpha :", alpha)

    print(" ")

    print("Decision Rule:", decision)

    print(" ")

    print("Final Result")

    if p_value < alpha:

        print("There is sufficient evidence to reject the claim.")

        print("The population mean height is significantly " "different from 170 cm.")

    else:

        print("There is not sufficient evidence to reject the claim.")

        print(
            "The population mean height is not significantly " "different from 170 cm."
        )


main()
