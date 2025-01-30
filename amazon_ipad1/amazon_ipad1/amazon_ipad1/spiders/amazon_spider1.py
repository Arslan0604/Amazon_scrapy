import scrapy


class AmazonSpider1Spider(scrapy.Spider):
    name = "amazon_spider1"
    allowed_domains = ["www.amazon.com"]
    start_urls = ["https://www.amazon.com/"]

    def parse(self, response):
        pass
