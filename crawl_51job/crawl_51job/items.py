# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Crawl51JobItem(scrapy.Item):
    job_title = scrapy.Field()
    company_name = scrapy.Field()
    location = scrapy.Field()
    salary = scrapy.Field()
    pub_date = scrapy.Field()

