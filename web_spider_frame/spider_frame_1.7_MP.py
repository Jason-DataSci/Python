    import requests
from bs4 import BeautifulSoup
import re
from lxml import html
import json
from datetime import datetime
from time import time
import pandas as pd
from multiprocessing import *
from time import time


# Get url from index page
# @profile
def get_links(index_url): # title[] link[]
    links = []
    index_res = requests.get(index_url)
    index_res.encoding = 'utf-8'
    index_tree = html.fromstring(index_res.text)

    last_url = index_tree.xpath('//*[@id="main"]/nav/div/div/div/span[1]/text()')
    max = int(re.findall(r'/ (\d+)', last_url[0])[0])

    # 1st page
    link = index_tree.xpath('//header/h2/a/@href')
    links = links + link
    max = 2
    for i in range(max - 1):
        url = 'http://coolshell.cn/page/' + str(i + 2)
        index_res = requests.get(url)
        index_res.encoding = 'utf-8'
        index_tree = html.fromstring(index_res.text)
        link = index_tree.xpath('//header/h2/a/@href')
        links = links + link
    return links

# Get contents
# @profile
def get_contents(link): # reads[]
    # print('start one more process')

    page = []
    # link = 'http://coolshell.cn/articles/12206.html'
    page_res = requests.get(link)
    page_res.encoding = 'utf-8'
    page_tree = BeautifulSoup(page_res.text, 'html.parser')
    title = page_tree.select('.entry-title')[0].text
    reads = page_tree.select('.entry-meta .entry-date')[0].text
    page = pd.DataFrame({'title': [title], 'link': [link], 'reads': [reads]}, columns=('title', 'link', 'reads'))
    return page

# @profile
def muli_get_contents(links):
    # print('links got')
    page_data = []
    data = pd.DataFrame(columns=('title', 'link', 'reads'))
    data
    for link in links:
        page_data.append(pool.apply_async(get_contents, (link,)))
    # page = pool.map_async(get_contents, links)
    # page_data.append(page.get())
    pool.close
    pool.join

    for page in page_data:
        data = pd.concat([data, page.get()], ignore_index=True, join_axes=[data.index])
        # data = data.append(page.get(), ignore_index=True)
    return data

#output
# @profile
def output(data):
    data.to_csv('/Users/zhengyichen/Downloads/test.csv', encoding='gb18030')


# @profile
if __name__ == '__main__':
    start_time = time()
    index_url = 'http://coolshell.cn/'
    pool = Pool(processes = cpu_count())

    links = get_links(index_url)
    data = muli_get_contents(links)
    output(data)
    print(time() - start_time)
