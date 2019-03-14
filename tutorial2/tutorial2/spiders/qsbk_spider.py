# -*- coding: utf-8 -*-
import scrapy


class QsbkSpiderSpider(scrapy.Spider):
	name = 'qsbk_spider'
	allowed_domains = ['imdb.com']
	start_urls = ['https://www.imdb.com/chart/top/']

	def parse(self, response):
		duanzis = response.xpath('.//div[@id="pagecontent"]')
		# print ("-"*50)
		# print (content)
		# print ("-"*50)
		for duanzi in duanzis:
			content = duanzis.xpath('.//div[@class="lister"]//text()').getall()
			content = ''.join(content).strip()
			print (content)

