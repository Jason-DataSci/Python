#! usr/bin/env python3
# -*- coding:utf-8 -*-

' WebSpider 1.0 HTML:'

__author__ = 'Jason'

import requests
from bs4 import BeautifulSoup
import re

qiushi = {}
url = 'http://www.qiushibaike.com/article/118228984'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
qiushi['author'] = soup.select('h2')[0].text
qiushi['content'] = soup.select('.content')[0].text.strip()
qiushi['vote'] = soup.select('.stats-vote')[0].contents[0].text
qiushi['comments'] = soup.select('.stats-comments')[0].contents[3].text
qiushi['img-src'] = soup.select('.author img')[0]['src']
qiushi['age'] = soup.select('.author .articleGender')[0].text
gender = soup.select('.author .articleGender')[0]['class'][1]
qiushi['gender'] = re.search(r'(.+)Icon', gender).group(1)


#re.match(r'()Icon',
#qiushi['test'] = soup.select('')[0].text

print(qiushi)
