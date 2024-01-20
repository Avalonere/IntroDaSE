import json
import os

import numpy as np
import pandas as pd

import parameters

if not os.path.exists("./csv/original"):
    os.makedirs("./csv/original")


def parse(item):
    folder_path = "./web_json/" + parameters.original_indices.get(item)[1] + "_json"
    city_num = len(os.listdir(folder_path))
    data = []
    param = parameters.original_indices.get(item)[0]
    year = parameters.year
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r") as f:
            json_data = json.load(f)
        for j in range(year * param, year * (param + 1)):
            try:
                data.append(
                    eval(json_data["returndata"]["datanodes"][j]["data"]["strdata"])
                )
            except:
                data.append(pd.NA)
    array = np.array(data).reshape(city_num, year)
    df = pd.DataFrame(array).drop(labels=0, axis=1)
    df.columns = [str(y) for y in range(2022, 2022 - year + 1, -1)]
    df.index = parameters.city_names[0:city_num]
    df.to_csv("./csv/original/" + item + ".csv", sep=",", encoding="utf-8")


for index in parameters.original_indices:
    parse(index)

# City Population Ratio
dfp = pd.read_csv("./csv/original/Population.csv", index_col=0, header=0)
dfcp = pd.read_csv("./csv/original/City_Population.csv", index_col=0, header=0)
dfcr = dfcp.div(dfp).round(2)
dfcr.to_csv(
    "./csv/original/City_Population_Ratio.csv",
    sep=",",
    index=True,
    header=True,
    encoding="utf-8",
)
