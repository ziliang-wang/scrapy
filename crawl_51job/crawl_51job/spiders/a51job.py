# -*- coding: utf-8 -*-
import re
import scrapy
from crawl_51job.items import Crawl51JobItem


class A51jobSpider(scrapy.Spider):
    name = '51job'
    allowed_domains = ['www.51job.com']

    def start_requests(self):
        print('请输入要查询的关键字: ')
        kw = input()
        url = f'https://search.51job.com/list/000000,000000,0000,00,9,99,{kw},2,1.html'
        yield scrapy.Request(url=url)

    def parse(self, response):
        jobs_dict = Crawl51JobItem()
        records = response.xpath('//div[@id="resultList"]/div[@class="el"]')
        for record in records:
            jobs_dict['job_title'] = record.xpath('./p/span/a/@title').extract_first()
            jobs_dict['company_name'] = record.xpath('./span[1]/a/@title').extract_first()
            jobs_dict['location'] = record.xpath('./span[2]/text()').extract_first()
            jobs_dict['salary'] = record.xpath('./span[3]/text()').extract_first() or '无'
            jobs_dict['pub_date'] = record.xpath('./span[4]/text()').extract_first()
            yield jobs_dict

        if response.xpath('//li[@class="bk"][2]/a/text()'):
            input_kw, page = re.search(r'000000,000000,0000,00,9,99,(.*?),2,(\d+).html',
                                       response.url).groups()
            next_url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,' \
                       '{},2,{}.html'.format(input_kw, int(page)+1)
            yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)








