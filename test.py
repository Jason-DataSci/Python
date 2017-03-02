import requests                     #获取网页内容
from bs4 import BeautifulSoup
import pandas as pd
import multiprocessing

index_url = 'http://coolshell.cn/page/69'
data = pd.DataFrame(columns=('title', 'link', 'reads'))
pool = multiprocessing.Pool()
results = []
count = 0


def get_index(index_url, count):
    print(1)
    index_res = requests.get(index_url)
    index_res.encoding = 'utf-8'
    index_soup = BeautifulSoup(index_res.text, 'html.parser')

    # Get url from index page
    index = index_soup.select('header h2 a')


    for index_html in index:
        count = count +1
        result = [index_html.text, index_html['href'], '']
        results.append(result)
    print(results)
    return results

process = pool.apply_async(get_index, args=(index_url, count,))
results = process.get()
pool.close()
pool.join()


import os
import multiprocessing

def task(pid):
    return pid
def main():
    multiprocessing.freeze_support()
    pool = multiprocessing.Pool()
    results = []
    cpus = multiprocessing.cpu_count()

    for i in range(0, cpus):
        result = pool.apply_async(task, args=(i,))
        results.append(result)
    pool.close()
    pool.join()

    for result in results:
        print(result.get())

main()


from multiprocessing import *

def f(x):
    return x*x
pool = Pool(processes=4)
rs = []

for i in range(100):
    r = pool.apply_async(f, args=(i,))
    rs.append(r.get())
pool.close()
pool.join()
print(rs)


from multiprocessing import *

def f():
    rs = []
    for x in range(100):
        rs.append(x * x)
    return rs
pool = Pool(processes=4)

x = pool.apply_async(f)
pool.close()
pool.join()
print(x.get())




import requests
from bs4 import BeautifulSoup
import pandas as pd
from multiprocessing import *

def get_index(index_url, count_end):
    index_res = requests.get(index_url)
    index_res.encoding = 'utf-8'
    index_soup = BeautifulSoup(index_res.text, 'html.parser')

    # Go to next link page
    try:
        index_url = index_soup.select('nav .wp-pagenavi .nextpostslink')[0]['href']
    except:
        index_url = 'End'

    return index_url

if __name__ == '__main__':
    index_url = 'http://coolshell.cn/page/69'
    count_end = 0
    data = pd.DataFrame(columns=('title', 'link', 'reads'))
    pool = Pool(processes=cpu_count())
    results = []
    page = 1
    result = pool.apply_async(get_index, args=(index_url, count_end,))
    result.get()

print(result.get)


def f():
    l = ['foo, foobar, char'] * 10000
    m = [x for x in l if x[:3] == 'foo']

f()

%timeit f()

%prun -l -s cumulative f()

import profile
%prun f()

import cProfile
cProfile.run('f()')

cProfile.run('/Users/zhengyichen/Documents/Python/web_spider_frame/spider_frame_1.5_FINAL.py')

import hotshot
hotshot.Profile(f()).run

def f(n):
    l = ['foo, foobar, char'] * n
    m = [x for x in l if x[:3] == 'foo']

import numpy
def add_and_sum(x, y):
    added = x + y
    summed = added.sum(axis=1)
    return summed

x = numpy.random.randn(3000, 3000)
y = numpy.random.randn(3000, 3000)

add_and_sum(x, y)

%load_ext line_profiler
%prun f(100000)
