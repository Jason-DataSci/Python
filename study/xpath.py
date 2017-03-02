import requests
from lxml import html


test_html = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

selector = etree.HTML(test_html)
result = etree.tostring(selector)   # 自动补全代码

import requests
from lxml import html
# web page
url = 'http://coolshell.cn/page/69'
page = requests.get(url)
tree = html.fromstring(page.text)
text = '//*[@class="entry-title"]/a/text()'
href = '//*[@class="entry-title"]/a/@href'
next_page = '//*[@id="main"]//*[@class="nextpostslink"]/@href'
tree.xpath(text)

# tree.xpath('//*[@class="entry-title"]/a/text()')
# tree.xpath('//*[@class="entry-title"]/a/@href')
tree.xpath('//*[@id="main"]//*[@class="nextpostslink"]/@href')
# tree.xpath('//*[@class="entry-title"]/a')



from lxml import html
import requests
page = requests.get('http://coolshell.cn/page/69')
tree = html.fromstring(page.text)
tree.xpath('//*[@id="post-7"]/header/h2/a')


import requests
from lxml import html

url = 'http://www.23us.com/class/1_1.html'
page = requests.get(url)
page.encoding = 'gbk'
tree = html.fromstring(page.text)
tree.xpath('//*[@class="L"]/a')
