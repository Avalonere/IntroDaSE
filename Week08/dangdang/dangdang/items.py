# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


import scrapy


class DangdangItem(scrapy.Item):
    title = scrapy.Field()  # 书名
    author = scrapy.Field()  # 作者
    price = scrapy.Field()  # 价格
    link = scrapy.Field()  # 链接
