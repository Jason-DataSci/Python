import requests                     #获取网页内容
from bs4 import BeautifulSoup       #将网页内容提取
import re                           #正则表达式
import json                         #javascript
from datetime import datetime       #日期
#import chardet                      #speed up

# Initialize
index_url = 'http://coolshell.cn/page/68'
ID = 0
dict = {}
class data(object): #ID, title, link, reads
    pass

# Get links
while index_url != 'End':
    index_res = requests.get(index_url)
    index_res.encoding = 'utf-8'
    index_soup = BeautifulSoup(index_res.text, 'html.parser')

    # Get url from index page
    index = index_soup.select('header h2 a')
    for i in index:
        ID = ID + 1
        dict[ID] = data()
        dict[ID].ID = ID
        dict[ID].title = i.text
        dict[ID].link = i['href']
        # dict[ID].reads = get_contents(i['href'])

    # Go to next link page
    try:
        index_url = index_soup.select('nav .wp-pagenavi .nextpostslink')[0]['href']
    except:
        index_url = 'End'

# Get contents
for data_id in range(ID)[1:]:
    page_url = dict[data_id].link
    page_res = requests.get(page_url)
    page_soup = BeautifulSoup(page_res.text, 'html.parser')

    dict[data_id].reads = page_soup.select('.entry-meta .entry-date')[0].text
