import scrapy


class Vacuum1Spider(scrapy.Spider):
    name = "vacuum1"
    allowed_domains = ["www.amazon.com"]
    start_urls = ["https://www.amazon.com/"]

    
    def parse(self, response):
        pass
