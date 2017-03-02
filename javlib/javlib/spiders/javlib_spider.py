#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule, Request
from scrapy.linkextractors import LinkExtractor
from javlib.items import JavlibItem

class JavlibSpider(CrawlSpider):

    name = 'javlib'
    start_urls = ['http://www.j12lib.com/cn/vl_bestrated.php?list&mode=1&/']

    rules = [
        Rule(LinkExtractor(allow=('http://www.j12lib.com/cn/vl_bestrated.php?list&mode=1&page=[1-25]')), callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        print(response.url)
        # item = JavlibItem()
        # item['url'] = response.url
        # item['video_title'] = response.xpath('//*[@id="video_title"]/h3/a/text()')[0]
        # item['video_img'] = response.xpath('//*[@id="video_jacket_img"]/@src')[0]
        # item['video_id'] = response.xpath('//*[@id="video_id"]//*[@class="text"]/text()')[0]
        # item['video_length'] = response.xpath('//*[@id="video_length"]//*[@class="text"]/text()')[0]
        # item['video_review'] = response.xpath('//*[@id="video_review"]//*[@class="score"]/text()')[0]
        # item['video_genres'] = response.xpath('//*[@id="video_genres"]//*/a/text()')[0]
        # item['video_cast'] = response.xpath('//*[@id="video_cast"]//*[@class="star"]/a/text()')[0]
        # return item



        # import pandas as pd
        # data = pd.DataFrame(columns='url')
        # page = pd.DataFrame({'url': [response.url]})
        # data = data.append(page, ignore_index=True)
        # data.to_csv('/Users/zhengyichen/Downloads/jav.csv', encoding='gbk')
