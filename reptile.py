# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def get_page(url='https://www.autohome.com.cn/news/'):
    response = requests.get(url)
    response.encoding = 'gbk'
    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_context = soup.find(name='div',attrs={'id':'auto-channel-lazyload-article'})
    # print(news_context)

    for each in news_context.find_all(name='li'):
        # print('-----',each)
        try:
            _url = each.find(name='a').attrs.get('href')
            _title = each.find(name='h3').text
            _img = each.find(name='img').attrs.get('src')
            print('https:' + _url,_title,'https:'+ _img)
        except:
            continue

#href="/news/4/#liststart"
response = requests.get('https://www.autohome.com.cn/news/')
response.encoding = 'gbk'
soup = BeautifulSoup(response.text, 'html.parser')
max_page = 0
for each_page in soup.find(name='div',attrs={'id': 'channelPage'}):
    # try:
    if hasattr(each_page,'attrs'):
        # print(each_page)
        _pgn = each_page.attrs.get('href')
        if not _pgn:
            continue
        if _pgn.startswith('/news/'):
            if int(_pgn.split('/')[2])  > max_page:
                max_page = int(_pgn.split('/')[2])
for page_n in range(1,max_page+1):
    page_url = 'https://www.autohome.com.cn/news/%s/#liststart' % page_n
    get_page(page_url)