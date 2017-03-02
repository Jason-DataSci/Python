import requests                     #获取网页内容
from bs4 import BeautifulSoup       #将网页内容提取
import re                           #正则表达式
import json                         #javascript
from datetime import datetime       #日期

index_url = 'http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/#0'
home = 'http://www.liaoxuefeng.com'

# Initialization
title = []
link = []
page_reads = []
previse_link = []   # can't get the url
next_link = []      # can't get the url

# Get url from index page
def get_index_urls(index_url):
    index_res = requests.get(index_url)
    index_res.encoding = 'utf-8'
    index_soup = BeautifulSoup(index_res.text, 'html.parser')

    index = index_soup.select('.x-sidebar-left-content li a')
    for i in index:
        title.append(i.text)
        link.append(home + i['href'])
        print(i.text)
        print(home + i['href'])
        get_contents(home + i['href'])
        print('/n')

# Get contents from the page
def get_contents(page_url):
    page_res = requests.get(page_url)
    page_soup = BeautifulSoup(page_res.text, 'html.parser')
    reads = page_soup.select('.x-wiki-info span')[0].text
    page_reads.append(reads)
    print(reads)

get_index_urls(index_url)
