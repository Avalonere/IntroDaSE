import scrapy
from dangdang.items import DangdangItem


class DdSpider(scrapy.Spider):
    name = "dd"
    allowed_domains = ["dangdang.com"]
    start_urls = ["https://book.dangdang.com/01.54.htm"]

    def parse(self, response):
        # 提取每本书的信息
        books = response.xpath('//ul[@class="bigimg"]/li')
        for book in books:
            item = DangdangItem()
            item["title"] = book.xpath(".//a/@title")[0].get()
            item["price"] = book.xpath(
                './/p[@class="price"]/span[@class="search_now_price"]/text()'
            )[0].get()
            item["link"] = book.xpath(".//a/@href")[0].get()
            yield item

        # 提取下一页的链接并继续爬取
        next_page = response.xpath('//li[@class="next"]/a/@href')
        if next_page:
            next_url = next_page[0].get()
            yield scrapy.Request(next_url, callback=self.parse)
