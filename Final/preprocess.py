import os

import pandas as pd

import parameters

if not os.path.exists("./csv/clean"):
    os.makedirs("./csv/clean")

if not os.path.exists("./csv/normalized"):
    os.makedirs("./csv/normalized")

for file in parameters.original_data:
    df = pd.read_csv(file, index_col=0, header=0)
    df.interpolate(method="linear", axis=1, limit_direction="both", inplace=True)
    df.to_csv(file.replace("original", "clean"))


for file in parameters.clean_data:
    df = pd.read_csv(file, index_col=0)
    for col in df.columns[:]:
        df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    df = df.round(6)
    df.to_csv(file.replace("clean", "normalized"))
