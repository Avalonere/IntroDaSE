# dd.py
import scrapy
from dangdang.items import DangdangItem


class DdSpider(scrapy.Spider):
    name = "dd"
    allowed_domains = ["dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.54.00.00.00.00.html"]  # 起始的url

    def parse(self, response):
        books = response.xpath('//ul[@class="bigimg"]/li')
        for book in books:
            item = DangdangItem()
            item["title"] = book.xpath("./a/@title").get()
            item["author"] = book.xpath(
                './p[@class="search_book_author"]/span[1]/a/text()'
            ).get()
            item["price"] = book.xpath('./p[@class="price"]/span[1]/text()').get()
            item["link"] = book.xpath("./a/@href").get()
            yield item

        # 只爬取一页
        # next_page = response.xpath('//li[@class="next"]/a/@href').get()
        # if next_page:  # 如果有下一页
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)
