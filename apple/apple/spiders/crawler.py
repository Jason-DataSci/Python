import scrapy
from bs4 import BeautifulSoup
import requests
from apple.items import AppleItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AppleCrawler(CrawlSpider):
    name = 'apple'
    start_urls = ['http://coolshell.cn/']
    rules = [
        Rule(LinkExtractor(allow=('http://coolshell.cn/page/[1-2]')), callback='parse_list', follow=True)
    ]

    def parse_list(self, response):
        res = BeautifulSoup(response.body)
        for news in res.select('header h2 a'):
            # print news.text
            # print(news['href'])
            yield scrapy.Request(news['href'], self.parse_detail, encoding='utf-8')

    def parse_detail(self, response):
        res = BeautifulSoup(response.body, 'html.parser')
        item = AppleItem()
        item['title'] = res.select('.entry-header h1')[0].text
        item['date'] = res.select('.entry-header time')[0].text
        return item


#
# url = 'http://coolshell.cn/articles/17391.html'
# page = requests.get(url)
# page.encoding = 'utf-8'
# res = BeautifulSoup(page.text, 'html.parser')
# res.select('.entry-header time')[0].text
