import numpy as np


def main(value, prevZ, itration):

    # mean = 1.027
    # std = 0.013
    # lambda_ = 0.02
    # l = 3

    mean = 2.6821
    std = 0.3166
    lambda_ = 0.02
    l = 3

    # z = lambda_ * value + (1 - lambda_) * prevZ
    stepone = lambda_ * value

    print(f" = {lambda_} x {value} = {stepone}")

    stepTwo = 1 - lambda_

    print(f" = 1 - {lambda_} = {stepTwo}")

    stepThree = stepTwo * prevZ

    print(f" = {stepTwo} x {prevZ} = {stepThree}")

    stepFour = stepone + stepThree

    print(f" = {stepone} + {stepThree} = {stepFour}")

    print("===================")
    print(f"Z VALUE = {stepFour}")
    print("===================")

    # sigma = std * np.sqrt((lambda_ / 2 - lambda_) * (1 - (1 - lambda_)**2 * t))

    # √

    print(
        f"{std} x √ ( {lambda_} / ( 2 - { lambda_} ) ) x [ 1 - ( 1 - {lambda_} ) ^ {2 * itration}]"
    )

    stepFive = 2 - lambda_  # 2 - 0.02

    print(f" = 2 - {lambda_} = {stepFive}")

    stepSix = 1 - lambda_  # 0.98

    print(f" = 1 - {lambda_} = {stepSix}")

    stepSeven = 2 * (itration)  # 2^4

    print(f"{std} x √ ( {lambda_} / {stepFive} ) x [ 1 - ( {stepSix} ) ^ {stepSeven}]")

    stepTen = lambda_ / stepFive  # 0.01010101

    print(f" = {lambda_} / {stepFive} = {stepTen}")

    stepEight = stepSix**stepSeven  # 0.98^4

    print(f" = {stepSix} ^ {stepSeven} = {stepEight}")

    stepNine = 1 - stepEight

    print(f" = 1 - {stepEight} = {stepNine}")

    stepEleven = stepTen * stepNine

    print(f" = {stepTen} * {stepNine} = {stepEleven}")

    stepTwelve = np.sqrt(stepEleven)

    print(f" = √{stepTwelve} = {stepTwelve}")

    stepThirteeen = std * stepTwelve

    print(f" = {std} * {stepTwelve} = {stepThirteeen}")

    sigma = stepThirteeen

    print("===================")
    print(f"Z SIGMA = {sigma}")
    print("===================")

    # =========================
    # UCL / LCL / DRIFT
    # =========================

    # ==================================================
    # UCL
    # ==================================================

    # UCL = Mean + (L x Sigma)

    stepFourteen = l * sigma

    print(f" = {l} x {sigma} = {stepFourteen}")

    stepFifteen = mean + stepFourteen

    print(f"UCL = {mean} + {stepFourteen} = {stepFifteen}")

    # ==================================================
    # LCL
    # ==================================================

    # LCL = Mean - (L x Sigma)

    stepSixteen = mean - stepFourteen

    print(f"LCL = {mean} - {stepFourteen} = {stepSixteen}")

    # ==================================================
    # DRIFT
    # ==================================================

    # Drift = True if Z is outside UCL or LCL

    drift = stepFour > stepFifteen or stepFour < stepSixteen

    print(
        f"DRIFT = {stepFour} > {stepFifteen} "
        f"or {stepFour} < {stepSixteen} = {drift}"
    )


main(2.24, 2.73068492034218, 1)


