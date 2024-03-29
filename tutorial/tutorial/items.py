# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class NewItem(scrapy.Item):
	# Main Fields
	main_headline = Field()
	headline = Field()

	# Separate Fields
	url = Field()
	project = Field()
	spider = Field()
	server = Field()
	date = Field()

class TestItem(scrapy.Item):
	id = scrapy.Field()
	name = scrapy.Field()
	description = scrapy.Field()

class MovieItem(scrapy.Item):
	title = scrapy.Field()
	crew = scrapy.Field()
	directors = scrapy.Field()
	writers = scrapy.Field()
	stars = scrapy.Field()
	popularity = scrapy.Field()

	


