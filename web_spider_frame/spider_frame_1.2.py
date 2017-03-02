import requests                     #获取网页内容
from bs4 import BeautifulSoup       #将网页内容提取
import re                           #正则表达式
import json                         #javascript
from datetime import datetime       #日期
#import chardet                      #speed up

# Get url from index page
def get_index_urls(index_url, ID, data): # title[] link[]
    index_res = requests.get(index_url)
    index_res.encoding = 'utf-8'
    index_soup = BeautifulSoup(index_res.text, 'html.parser')

    index = index_soup.select('header h2 a')
    for i in index:
        ID = ID + 1
        dict[ID] = data()
        dict[ID].ID = ID
        dict[ID].title = i.text
        dict[ID].link = i['href']
        # dict[ID].reads = get_contents(i['href'])
    return ID

# Go to next link page
def goto_next_link_page(index_url): # index_url
    index_res = requests.get(index_url)
    index_res.encoding = 'utf-8'
    index_soup = BeautifulSoup(index_res.text, 'html.parser')
    index = index_soup.select('nav .wp-pagenavi .nextpostslink')[0]['href']
    return index

# Get contents from the page
def get_contents(data_id): # reads[]
    page_url = dict[data_id].link
    page_res = requests.get(page_url)
    page_soup = BeautifulSoup(page_res.text, 'html.parser')

    dict[data_id].reads = page_soup.select('.entry-meta .entry-date')[0].text
    print(dict[data_id].reads)

# Main Program
def get_data(): # title[] link[]
    # Initialize
    index_url = 'http://coolshell.cn/page/68'
    ID = 0
    dict = {}
    class data(object): #ID, title, link, reads
        pass

    # Get links
    while index_url != '':
        ID = get_index_urls(index_url, ID, data)
        index_url = goto_next_link_page(index_url)

    # Get contents
    for data_id in range(ID)[1:]:
        get_contents(data_id)

get_data()














class test(object): #ID, title, link, reads
    def __init__(self, name):
        self.name = name

class test2(object): #ID, title, link, reads
    pass

a = range(10)
dictionary = {}
dictionary[0] = test('Baa')
dictionary[0].name
dictionary[0].try = 1
dictionary[1] = test2()
dictionary[1].name = 'bob'
dictionary[1].name

def ttt(test2):
    dictionary[2] = test2()
    dictionary[2].name = 'bob'
    return dictionary[2].name

ttt(test2)
