import re


def count_repeats(s):
    repeats = re.findall(r"((\w)\2+)", s)
    for repeat in repeats:
        print(repeat[1] + "连续重复了" + str(len(repeat[0])) + "次")
