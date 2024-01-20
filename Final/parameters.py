year = 10 + 1

original_indices = {
    "PILE": [0, "PILE"],
    "ALE": [1, "ILE"],
    "SLE": [8, "ILE"],
    "GDP": [0, "GDP"],
    "PIGDP": [1, "GDP"],
    "AGDP": [4, "GDP"],
    "SGDP": [7, "GDP"],
    "GDPpc": [13, "GDP"],
    "GDPI": [0, "GDPI"],
    "PIGDPI": [1, "GDPI"],
    "Population": [0, "Population"],
    "City_Population": [1, "Population"],
    "Rural_Population": [2, "Population"],
    "Life_Expectancy": [0, "Life_expectancy"],
    "Life_Expectancy_M": [1, "Life_expectancy"],
    "Life_Expectancy_F": [2, "Life_expectancy"],
    "Honey": [11, "Honey"],
}

indices = (
    ["Demand"]
    + list(original_indices.keys())
    + [
        "City_Population_Ratio",
    ]
)

original_data = ["./csv/original/" + index + ".csv" for index in indices]
clean_data = ["./csv/clean/" + index + ".csv" for index in indices]
normalized_data = ["./csv/normalized/" + index + ".csv" for index in indices]

scrape_param = {
    "Honey": "A0D10",
    "GDP": "A0201",
    "Population": "A0301",
    "PILE": "A010201",
    "ILE": "A010203",
    "GDPI": "A0202",
    "Life_expectancy": "A0303",
}

provinces = {
    "北京市": "11",
    "天津市": "12",
    "河北省": "13",
    "山西省": "14",
    "内蒙古自治区": "15",
    "辽宁省": "21",
    "吉林省": "22",
    "黑龙江省": "23",
    "上海市": "31",
    "江苏省": "32",
    "浙江省": "33",
    "安徽省": "34",
    "福建省": "35",
    "江西省": "36",
    "山东省": "37",
    "河南省": "41",
    "湖北省": "42",
    "湖南省": "43",
    "广东省": "44",
    "广西壮族自治区": "45",
    "海南省": "46",
    "重庆市": "50",
    "四川省": "51",
    "贵州省": "52",
    "云南省": "53",
    "西藏自治区": "54",
    "陕西省": "61",
    "甘肃省": "62",
    "青海省": "63",
    "宁夏回族自治区": "64",
    "新疆维吾尔自治区": "65",
}
city_names = list(provinces.keys())
city_codes = list(provinces.values())
