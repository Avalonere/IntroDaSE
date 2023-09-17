text = "数据科学与工程导论"
length = len(text)
stars = chr(0x2605) * (length + 4)
print("{0}\n{1} {2} {1}\n{0}".format(stars, chr(0x2605), text))
