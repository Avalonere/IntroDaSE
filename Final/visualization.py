import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import parameters

matplotlib.rc("font", family="DengXian")

if not os.path.exists("./plot/index_change"):
    os.mkdir("./plot/index_change")


def plot(index):
    data = pd.read_csv("./csv/clean/" + index + ".csv", index_col=0)
    data = data.iloc[:, ::-1]
    data["avg"] = data.mean(axis=1)
    data_sorted = data.sort_values(by="avg").drop(labels="avg", axis=1)
    data = data.drop(labels="avg", axis=1)

    # 划分为四组
    group_size = len(data) // 4
    group1 = data_sorted.iloc[:group_size]
    group2 = data_sorted.iloc[group_size : 2 * group_size]
    group3 = data_sorted.iloc[2 * group_size : 3 * group_size]
    group4 = data_sorted.iloc[3 * group_size :]

    # 创建画布和子图
    fig, axs = plt.subplots(2, 4, figsize=(20, 10))

    # 第一行四列的子图，分别展示四组省份十年变化，并加入图例（放在外面）
    for ax, group in zip(axs[0, :], [group1, group2, group3, group4]):
        for province in group.index:
            if province != "10年均值":
                ax.plot(group.loc[province], label=province, marker="o")
        ax.set_title(f"{group.index[0]} to {group.index[-1]} - 10-Year Change")
        ax.legend()

    # 第二行四列的子图，分别展示均值、总数、标准差和极差
    axs[1, 0].plot(data.mean(), label="Mean", marker="o")
    axs[1, 0].legend()
    axs[1, 0].set_title("Mean Change")

    axs[1, 1].plot(data.sum(), label="Total", marker="o")
    axs[1, 1].legend()
    axs[1, 1].set_title("Total Change")

    axs[1, 2].plot(data.std(), label="Standard Deviation", marker="o")
    axs[1, 2].legend()
    axs[1, 2].set_title("Standard Deviation Change")

    axs[1, 3].plot(data.max() - data.min(), label="Range", marker="o")
    axs[1, 3].legend()
    axs[1, 3].set_title("Range Change")

    years = [
        "2013",
        "2014",
        "2015",
        "2016",
        "2017",
        "2018",
        "2019",
        "2020",
        "2021",
        "2022",
    ]
    for ax in axs.flat:
        ax.set_xticks(np.arange(len(years)))
        ax.set_xticklabels(years)
    plt.suptitle(index, fontsize=16)
    plt.tight_layout()
    plt.savefig("./plot/index_change/" + index + ".png")
    plt.show()


for item in parameters.indices:
    plot(item)
