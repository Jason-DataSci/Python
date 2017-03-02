import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from multiprocessing import *
from time import time

def get_index(q):
    index_res = requests.get(index_url)
    index_res.encoding = 'utf-8'
    index_soup = BeautifulSoup(index_res.text, 'html.parser')

    # # Get url from index page
    # index = index_soup.select('header h2 a')
    # for index_html in index:
    #     result = [index_html.text, index_html['href'], '']
    #     results.append(result)
    # print('Start')
    # Go to next link page

    return results

def get_link(index_url, count_end, results, page):
    while index_url != 'End':
        result = pool.apply(get_index, args(q,))
        print(index_url)
        results.append(result)

    # pool.close()
    # pool.join()

# for result in results:
#     index_url, count_end, result = result.get()
#     print()

# for i in range(count_start, count_end):
#     data.loc[i + 1] = results[i]

# # Get contents
# for data_id in list(range(1, count + 1)):
#     page_url = data['link'].loc[data_id]
#     page_res = requests.get(page_url)
#     page_soup = BeautifulSoup(page_res.text, 'html.parser')
#     data['reads'].loc[data_id] = page_soup.select('.entry-meta .entry-date')[0].text

# data.to_csv('/Users/zhengyichen/Downloads/test.csv', encoding='gbk')
# print(time() - time_start)


if __name__ == '__main__':
    time_start = time()
    index_url = 'http://coolshell.cn/page/69'
    count_end = 0
    data = pd.DataFrame(columns=('title', 'link', 'reads'))
    pool = Pool(processes=cpu_count())
    results = []
    q = Queue()
    get_link(index_url, count_end, results, page)
    # print('Func_End')

# index_url = 'http://coolshell.cn/page/69'
# result = pool.apply_async(get_index)
# print(index_url)
# index_url = 'http://coolshell.cn/page/68'
get_index()
print(index_url)
