import requests                     #获取网页内容
from bs4 import BeautifulSoup       #将网页内容提取
import re                           #正则表达式
import json                         #javascript
from datetime import datetime       #日期
from time import time
import pandas as pd

# Main Program
def get_data(): # title[] link[]
    Initialize()
    get_index_urls(index_url, count, data, index_link, index_next)
    get_contents()
    output(data)

# Initialize
def Initialize():
    global index_url, count, data, index_link, index_next
    index_url = 'http://coolshell.cn/page/68'
    count = 0
    data = pd.DataFrame(columns=('title', 'link', 'reads'))
    index_link = 'header h2 a'
    index_next = 'nav .wp-pagenavi .nextpostslink'

# Get url from index page
def get_index_urls(index_url, count, data, index_link, index_next): # title[] link[]
    while index_url != 'End':
        index_res = requests.get(index_url)
        index_res.encoding = 'utf-8'
        index_soup = BeautifulSoup(index_res.text, 'html.parser')

        # Get url from index page
        index = index_soup.select(index_link)
        for i in index:
            count = count + 1
            data.loc[count] = [i.text, i['href'], '']

        # Go to next link page
        try:
            index_url = index_soup.select(index_next)[0]['href']
        except:
            index_url = 'End'

# Get contents
def get_contents(): # reads[]
    for data_id in list(range(1, count + 1)):
        page_url = data['link'].loc[data_id]
        page_res = requests.get(page_url)
        page_soup = BeautifulSoup(page_res.text, 'html.parser')
        data['reads'].loc[data_id] = page_soup.select('.entry-meta .entry-date')[0].text

#output
def output(data):
    data.to_csv('/Users/zhengyichen/Downloads/test.csv', encoding='gbk')

time_start = time()
get_data()
print(time() - time_start)
