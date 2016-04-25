import scrapy
from abroadrecommendscraper.items import AbroadrecommendscraperItem
class BaicaioSpider(scrapy.Spider):
    name = "baicaio"
    allowed_domains = ["baicaio.com"]
    start_urls = [
        "http://www.baicaio.com"
    ]
    def parse(self, response):
        item = AbroadrecommendscraperItem()
        item['title'] = response.xpath('//h1/a/text()').extract()
        item['content'] = response.xpath('//p').extract()
        yield item
