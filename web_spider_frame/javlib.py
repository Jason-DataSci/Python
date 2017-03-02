import requests
from bs4 import BeautifulSoup
import re
from lxml import html
from time import time
import pandas as pd


# Get url from index page
# @profile
def get_links(index_url): # title[] link[]
    links = []
    index_res = requests.get(index_url)
    index_res.encoding = 'utf-8'
    index_tree = html.fromstring(index_res.text)

    max = 25

    # 1st page
    link = index_tree.xpath('//*[@class="videotextlist"]//a//@href')
    links = links + link
    # for i in range(max - 1):
    #     i = 0
    #     url = index_url + 'page=' + str(i + 2)
    #     index_res = requests.get(url)
    #     index_res.encoding = 'utf-8'
    #     index_tree = html.fromstring(index_res.text)
    #     link = index_tree.xpath('//*[@class="videotextlist"]//a//@href')
    #     links = links + link
    return links

# Get contents
# @profile
def get_contents(link): # reads[]
    print(link)
    page = []
    page_res = requests.get(link)
    page_res.encoding = 'utf-8'
    page_tree = html.fromstring(page_res.text)

    try:
        video_title = page_tree.xpath('//*[@id="video_title"]/h3/a/text()')[0]
        video_img = page_tree.xpath('//*[@id="video_jacket_img"]/@src')[0]
        video_id = page_tree.xpath('//*[@id="video_id"]//*[@class="text"]/text()')[0]
        video_length = page_tree.xpath('//*[@id="video_length"]//*[@class="text"]/text()')[0]
        video_review = page_tree.xpath('//*[@id="video_review"]//*[@class="score"]/text()')[0]
        video_genres = page_tree.xpath('//*[@id="video_genres"]//a/text()')
        video_cast = page_tree.xpath('//*[@id="video_cast"]//*[@class="star"]/a/text()')[0]
        page = pd.DataFrame({
            'video_title': [video_title], 'video_img': [video_img], 'video_id': [video_id], 'video_length': [video_length], 'video_review': [video_review], 'video_genres': [video_genres], 'video_cast': [video_cast]}, columns=('video_title', 'video_img', 'video_id', 'video_length', 'video_review', 'video_genres', 'video_cast'
            ))
    except:
        lost_page.append(link)
        page = pd.DataFrame({
            'video_title': [], 'video_img': [], 'video_id': [], 'video_length': [], 'video_review': [], 'video_genres': [], 'video_cast ': []}, columns=('video_title', 'video_img', 'video_id', 'video_length', 'video_review', 'video_genres', 'video_cast'
            ))

    return page

# @profile
def muli_get_contents(links):
    data = pd.DataFrame(columns=('video_title', 'video_img', 'video_id', 'video_length', 'video_review', 'video_genres', 'video_cast'))
    page_data = []

    for link in links:
        link = link[-4:]
        link = domain + '?v=javlik' + link
        page = get_contents(link)

        data = pd.concat([data, page], ignore_index=True)

    return data

#output
# @profile
def output(data):
    data.to_csv('/Users/zhengyichen/Downloads/javlib_bestrated_mode' + mode[0] + '.csv', encoding='gb18030')

def main(mode):
    start_time = time()
    index_url = domain + 'vl_bestrated.php?list&mode=' + mode
    lost_page = []

    links = get_links(index_url)
    data = muli_get_contents(links)
    output(data, mode)
    print('mode' + mode[0] + 'cost: ' + str(time() - start_time))
    print(lost_page)

# @profile
if __name__ == '__main__':
    domain = 'http://www.j12lib.com/cn/'
    mode = '1&'
    start_time = time()
    index_url = domain + 'vl_bestrated.php?list&mode=' + mode
    lost_page = []

    links = get_links(index_url)
    data = muli_get_contents(links)
    output(data)
    print('mode' + mode[0] + 'cost: ' + str(time() - start_time))
    print(lost_page)


# domain
# http://www.javlibrary.com/cn/
# http://www.j12lib.com/cn/
