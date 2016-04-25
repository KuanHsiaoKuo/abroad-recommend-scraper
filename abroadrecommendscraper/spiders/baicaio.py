# -*- coding: UTF-8 -*-  
import sys
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import Selector
from scrapy import Request
from abroadrecommendscraper.items import AbroadrecommendscraperItem 
import logging
class BaicaioSpider(CrawlSpider):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    name = "baicaio_crawler"
    #download_delay = 1
    allowed_domains = ["www.baicaio.com"]
    start_urls = ["http://www.baicaio.com/page/1"] 
    rules =(\
            Rule(LinkExtractor(allow=('page/([\d]+)',)),callback='parse_item'),\
           )
    def parse_item(self, response):
        sel = Selector(response)
        #取出页面中所有文章链接
        links = sel.xpath('//a/@href').re('http://www.baicaio.com/\d{4}/\d{2}/\d{2}/\d{1,6}.html')
        #对list中的元素去重
        #print("this is parse_item  print")
        links = list(set(links))
        for link in links:
             #print link
             yield Request(link,callback=self.parse_detail)
    def parse_detail(self,response):
        detail_sel = Selector(response)
        item = AbroadrecommendscraperItem()
       # print("this is parse_detail")
        #print response.body
        #print response.status
        title = \
        response.xpath('//*[@id="content"]/ul/li/h1/a//text()').extract()
        print type(title)
        print title
        item['title'] = [t.encode('utf-8') for t in title]
        print item['title']
        content =\
        response.xpath('//*[@id="content"]/ul/li/div[3]').re('(?<=<p>).*?(?=</p>)')
        item['content'] = [c.encode('utf-8') for c in content]
        print item['content']
        yield item


