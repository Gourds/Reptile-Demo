# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json

ret = requests.get('https://dig.chouti.com/',
        headers={
                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
                'Referer': 'https://dig.chouti.com/',
                'Upgrade-Insecure-Requests': '1',
                'Host': 'dig.chouti.com',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1'
                   })
ret.encoding = 'utf-8'
#
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Host': 'dig.chouti.com',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://dig.chouti.com',
    'Sec-Fetch-Mode' : 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
}
ret_cookie = ret.cookies.get_dict()
# ret_cookie['token'] =
print(ret.cookies.get_dict())
# soup = BeautifulSoup(ret.text,'html.parser')
# print(soup)
#https://dig.chouti.com/link/hot?afterTime=1567990799995000&_=1568013317740
url = 'https://dig.chouti.com/link/hot'

ret = requests.get(url=url, headers=headers)
ret_cookie2 = ret.cookies.get_dict()
for i in json.loads(ret.text)['data']:
    print(i)

# res = requests.post('https://dig.chouti.com/login',headers=headers,data=data,cookies=ret_cookie)
