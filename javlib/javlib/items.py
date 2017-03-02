# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class JavlibItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    video_title = Field() # //*[@id="video_title"]/h3/a/text()
    video_img = Field() # //*[@id="video_jacket_img"]/@src
    video_id = Field() # //*[@id="video_id"]//*[@class="text"]/text()
    video_length = Field() # //*[@id="video_length"]//*[@class="text"]/text()
    video_review = Field() # //*[@id="video_review"]//*[@class="score"]/text()
    video_genres = Field() # //*[@id="video_genres"]//*/a/text()
    video_cast = Field() # //*[@id="video_cast"]//*[@class="star"]/a/text()
    url = Field() # //*[@id="vid_javlikdar4"]/a/@href


#     last = //*[@id="rightcolumn"]//*[@class="page last"]/@href #25
#     start_urls =
#     http://www.javlibrary.com/cn/vl_bestrated.php?list&mode=1& page=2
#     http://www.javlibrary.com/cn/vl_bestrated.php?list&mode=2& page=2
#
# import requests
# from lxml import html
#
# url = 'http://www.javlibrary.com/cn/vl_bestrated.php?list&mode=&page=1'
# page = requests.get(url)
# page.encoding = 'utf-8'
# tree = html.fromstring(page.text)
# tree.xpath('')
