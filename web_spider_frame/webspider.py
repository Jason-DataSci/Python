import requests                     #获取网页内容
from bs4 import BeautifulSoup       #将网页内容提取
import re                           #正则表达式
import json                         #javascript
from datetime import datetime       #日期

url = 'http://news.sina.com.cn/c/zs/2016-12-16/doc-ifxytqav9416001.shtml'

def getCommentCounts(url):
    m = re.search('doc-i(.+).shtml',url)                                                    #正则表达式，提取newsurl中在doc-i____.shtml之间的元素
    newsid = m.group(1)                                                                         #提取到每个网页的特征编码
    commentURL = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
    comments = requests.get(commentURL.format((newsid)))                                        #合并评论js的url
    jd = json.loads(comments.text.strip('var data='))                                           #调用json的loads解码
    return jd['result']['count']['total']                                                       #从字典中逐层找出需要的内容

def getNewsDetail(url):
    result = {}                                                                                 #以字典的方式存储网页内容
    res = requests.get(url)                                                                 #从网页上获取Doc
    res.encoding = 'utf-8'                                                                      #说明网页编码格式，网页编码格式为'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')                                               #用BeautifulSoup提取网页内容，为避免警告说明解释器是用html
    result['title'] = soup.select('#artibodyTitle')[0].text                                     #获取网页标题，分析网页element发现可以根据id：artibodyTitle来定位
    result['newssource'] = soup.select('.time-source span a')[0].text                           #分析网页发现可以根据class：time-source来定位，再分析获取的内容，在span a下可以取得
    timesource = soup.select('.time-source')[0].contents[0].strip()                             #获取时间信息，利用contents来将子节点以list的形式输出，利用strip去掉非文本
    result['dt'] = datetime.strptime(timesource, '%Y年%m月%d日%H:%M')                            #利用datetime函数将文本格式的日期转为日期格式
    result['article'] = ' '.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])     #正文由list构成，利用for提取每个元素，用join把处理过的元素拼接。这一句是python特色的"一行文"
    result['editor'] = soup.select('.article-editor')[0].text.rstrip('责任编辑：')
    result['comments'] = getCommentCounts(url)
    return result

print(getNewsDetail(url))
