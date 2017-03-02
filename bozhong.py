import requests
from lxml import html

index_url = 'http://bbs.bozhong.com/thread-39490570-1-1.html'

page_res = requests.get(index_url)
page_res.encoding = 'utf-8'
page_tree = html.fromstring(page_res.text)

title = page_tree.xpath('//*[@id="ct"]/div[2]/div[1]/h1/text()')[0]
author = page_tree.xpath('//*[@class="theme_box post_list"]/div[1]/div[2]/a/text()')[0]
sex_date = page_tree.xpath('//*[@class="theme_box post_list"]/div[2]/div[4]/div[1]/div[1]/div/table/tbody/tr[1]/td/text()')[0]
moment = page_tree.xpath('//*[@class="theme_box post_list"]/div[2]/div[4]/div[1]/div[1]/div/table/tbody/tr[2]/td/text()')[0]
content_list = page_tree.xpath('//*[@class="t_fsz "]//*[@class="t_f"]/text()')
images = page_tree.xpath('//*[@class="t_f"]/img/@file')

contents = ''
for content in content_list:
    contents = contents + content

print('title: ', title)
print('author: ', author)
print('sex_date: ', sex_date)
print('moment: ', moment)
print('contents: ', contents)
print('images: ', images)
