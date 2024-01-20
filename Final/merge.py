import os

import pandas as pd

import parameters

if not os.path.exists("./train_data"):
    os.makedirs("./train_data")


def merge(ind):
    type_data = ["./csv/" + ind + "/" + index + ".csv" for index in parameters.indices]
    if not os.path.exists("./year_data/" + ind):
        os.makedirs("./year_data/" + ind)

    if not os.path.exists("./city_data/" + ind):
        os.makedirs("./city_data/" + ind)

    # merge by year
    for i in range(1, 11):
        columns = []
        for item in type_data:
            frame = pd.read_csv(item)
            columns.append(frame.iloc[0:, i])
        merged = pd.concat(columns, axis=1)
        merged.columns = parameters.indices
        merged.index = parameters.city_names[0 : len(parameters.city_codes)]
        merged.to_csv(
            "./year_data/" + ind + "/" + str(2023 - i) + ".csv",
            sep=",",
            encoding="utf-8",
        )

    # merge by city
    for i in range(len(parameters.city_codes)):
        rows = []
        for item in type_data:
            frame = pd.read_csv(item)
            rows.append(frame.iloc[i,])
        merged = pd.concat(rows, axis=1).iloc[1:,]
        merged.columns = parameters.indices
        merged.to_csv(
            "./city_data/"
            + ind
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
total = []
year_data = [
    "./year_data/" + "normalized" + "/" + str(2023 - i) + ".csv" for i in range(2, 11)
]
for file in year_data:
    df = pd.read_csv(file)
    total.append(df)
train = pd.concat(total, axis=0).iloc[:, 1:]
train.to_csv("./train_data/train.csv", sep=",", encoding="utf-8", index=False)
total.append(pd.read_csv("./year_data/normalized/2022.csv"))
train = pd.concat(total, axis=0).iloc[:, 1:]
train.to_csv("./train_data/train_all.csv", sep=",", encoding="utf-8", index=False)
