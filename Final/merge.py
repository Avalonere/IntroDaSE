import os

import pandas as pd

import parameters

if not os.path.exists("./train_data"):
    os.makedirs("./train_data")


def merge(type):
    type_data = ["./csv/" + type + "/" + index + ".csv" for index in parameters.indices]
    if not os.path.exists("./year_data/" + type):
        os.makedirs("./year_data/" + type)

    if not os.path.exists("./city_data/" + type):
        os.makedirs("./city_data/" + type)

    # merge by year
    for i in range(1, 11):
        columns = []
        for file in type_data:
            df = pd.read_csv(file)
            columns.append(df.iloc[0:, i])
        merged = pd.concat(columns, axis=1)
        merged.columns = parameters.indices
        merged.index = parameters.city_names[0 : len(parameters.city_codes)]
        merged.to_csv(
            "./year_data/" + type + "/" + str(2023 - i) + ".csv",
            sep=",",
            encoding="utf-8",
        )

    # merge by city
    for i in range(len(parameters.city_codes)):
        rows = []
        for file in type_data:
            df = pd.read_csv(file)
            rows.append(df.iloc[i,])
        merged = pd.concat(rows, axis=1).iloc[1:,]
        merged.columns = parameters.indices
        merged.to_csv(
            "./city_data/"
            + type
            + "/"
            + parameters.city_codes[i]
            + "_"
            + parameters.city_names[i]
            + ".csv",
            sep=",",
            encoding="utf-8",
        )


merge("clean")
merge("normalized")

# data for training
all = []
year_data = [
    "./year_data/" + "normalized" + "/" + str(2023 - i) + ".csv" for i in range(2, 11)
]
for file in year_data:
    df = pd.read_csv(file)
    all.append(df)
train = pd.concat(all, axis=0).iloc[:, 1:]
train.to_csv("./train_data/train.csv", sep=",", encoding="utf-8", index=False)
