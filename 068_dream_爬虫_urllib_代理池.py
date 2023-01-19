# @Author : huzejun
# @Time : 2023/1/19 21:44

proxies_pool = [
    {'http':'121.13.252.60:41564'},
    {'http':'202.109.157.61:9000'},
    {'http':'120.24.76.81:8123'},
    {'http':'117.41.38.16:9000'},
]

import random
import urllib.request

proxies = random.choice(proxies_pool)

url = 'https://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=headers)

handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

with open('daili_11.html','w',encoding='utf-8')as fp:
    fp.write(content)
