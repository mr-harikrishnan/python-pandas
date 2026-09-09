import pandas as pd
import numpy as np
from scipy.stats import t


def findMeanAndStd(df):

    mean = np.mean(df["height"])

    standard_deviation = np.std(df["height"], ddof=1)

    return mean, standard_deviation


def findStandardError(
    classAstandard_deviation,
    classBstandard_deviation,
    classAsample_size,
    classBsample_size,
):

    classAvariance = classAstandard_deviation**2

    classBvariance = classBstandard_deviation**2

    standard_error = np.sqrt(
        (classAvariance / classAsample_size) + (classBvariance / classBsample_size)
    )

    return standard_error


def findTValue(classAmean, classBmean, standard_error):

    t_value = (classAmean - classBmean) / standard_error

    return t_value


def findDegreesOfFreedom(
    classAstandard_deviation,
    classBstandard_deviation,
    classAsample_size,
    classBsample_size,
):

    classAvariance = classAstandard_deviation**2

    classBvariance = classBstandard_deviation**2

    numerator = (
        (classAvariance / classAsample_size) + (classBvariance / classBsample_size)
    ) ** 2

    denominator = (
        ((classAvariance / classAsample_size) ** 2) / (classAsample_size - 1)
    ) + (((classBvariance / classBsample_size) ** 2) / (classBsample_size - 1))

    degrees_of_freedom = numerator / denominator

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

    confidence_level = 95  # %

    df = pd.read_csv("./student_height_data.csv")

    classAstudentdf = df.sample(n=10, random_state=42)

    classBstudentdf = df.sample(n=10, random_state=32)

    # Class A

    classAmean, classAstandard_deviation = findMeanAndStd(classAstudentdf)

    classAsample_size = len(classAstudentdf)

    # Class B

    classBmean, classBstandard_deviation = findMeanAndStd(classBstudentdf)

    classBsample_size = len(classBstudentdf)

    # H0: population mean of Class A = population mean of Class B
    # H1: population mean of Class A != population mean of Class B

    standard_error = findStandardError(
        classAstandard_deviation,
        classBstandard_deviation,
        classAsample_size,
        classBsample_size,
    )

    t_value = findTValue(classAmean, classBmean, standard_error)

    degrees_of_freedom = findDegreesOfFreedom(
        classAstandard_deviation,
        classBstandard_deviation,
        classAsample_size,
        classBsample_size,
    )

    p_value = findPValue(t_value, degrees_of_freedom)

    alpha = findAlpha(confidence_level)

    decision = makeDecision(p_value, alpha)

    print("class_A_mean :", classAmean)

    print("class_A_standard_deviation :", classAstandard_deviation)

    print("class_A_sample_size :", classAsample_size)

    print(" ")

    print("class_B_mean :", classBmean)

    print("class_B_standard_deviation :", classBstandard_deviation)

    print("class_B_sample_size :", classBsample_size)

    print(" ")

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

        print("There is sufficient evidence to reject H0.")

        print(
            "The average heights of Class A and Class B " "are significantly different."
        )

    else:

        print("There is not sufficient evidence to reject H0.")

        print(
            "The average heights of Class A and Class B "
            "are not significantly different."
        )


main()
