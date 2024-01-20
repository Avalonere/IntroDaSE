import json
import os
import time

import requests

import parameters


def getTime():
    return int(round(time.time() * 1000))


def scrape(index, city_code):
    url = "https://data.stats.gov.cn/easyquery.htm"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/114.0.0.0"
        "Safari/537.36"
    }
    params = {
        "m": "QueryData",
        "dbcode": "fsnd",
        "rowcode": "zb",
        "colcode": "sj",
        "wds": '[{"wdcode":"reg","valuecode":'
        + '"'
        + str(city_code)
        + "0000"
        + '"'
        + "}]",
        "dfwds": '[{"wdcode":"zb","valuecode":"'
        + parameters.scrape_param.get(index)
        + '"},{"wdcode":"sj","valuecode":"LAST'
        + str(parameters.year)
        + '"}]',
        "k1": str(getTime()),
    }
    r = requests.get(url, headers=headers, params=params, verify=False)
    return json.loads(r.text)


def scrapeAll(index):
    if not os.path.exists("./web_json/" + index + "_json"):
        os.makedirs("./web_json/" + index + "_json")
    for i in range(len(parameters.city_codes)):
        js = scrape(index, parameters.city_codes[i])
        with open(
            "./web_json/"
            + index
            + "_json/"
            + str(parameters.city_codes[i])
            + "_"
            + parameters.city_names[i]
            + ".json",
            "w",
        ) as f:
            json.dump(js, f)


scrapeAll("PILE")
scrapeAll("ILE")
scrapeAll("GDP")
scrapeAll("GDPI")
scrapeAll("Population")
scrapeAll("Life_expectancy")
scrapeAll("Honey")
