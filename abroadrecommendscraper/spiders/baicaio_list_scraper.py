
# -*- coding: UTF-8 -*-  
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import time
class BaicaioListSpider(CrawlSpider):
    name = "baicaiolistspider"
    #download_delay = 1
    allowed_domains = ["www.baicaio.com"]
    start_urls = ["http://www.baicaio.com/page/1"] 
    rules = (Rule(LinkExtractor(allow=('page/([\d]+)',)),callback="parse_item",follow = True),)
    def parse_item(self, response):
		sel = scrapy.Selector(response)
		#取出页面中所有文章链接
		links = sel.xpath('//a/@href').re('http://www.baicaio.com/\d{4}/\d{2}/\d{2}/\d{1,6}.html')
		#对list中的元素去重
		links = list(set(links))
		#print links
		#time.sleep(30)
		#打开文件后依次写入
		#fhand = open('/Users/apple/abroadrecommendscraper/links.txt','w')
		with open('/Users/apple/abroadrecommendscraper/links.txt','a') as f:
			for link in links:
		        	f.write(link)
		        	#print link,'written'
		        	#time.sleep(5)
		        	f.write("\n")
		     		links=[]
