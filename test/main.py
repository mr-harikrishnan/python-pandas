import pandas as pd

df = pd.read_csv("./Parquiet-11-09-datas-10.csv")

print(
    df[
        [
            "activity_value",
            "mean",
            "stddev",
            "z_prev",
            "L",
            "lambda_",
            "sigma_ewma",
            "ucl",
            "lcl",
            "drift",
        ]
    ]
)
