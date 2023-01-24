# @Author : huzejun
# @Time : 2023/1/24 18:51

import requests

url = 'http://www.baidu.com/s?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

data = {
    'wd':'ip'
}

proxy = {
    'http':'120.24.76.81:8123'
}

# response = requests.get(url=url,params=data,headers=headers)
response = requests.get(url=url,params=data,headers=headers,proxies=proxy)

content = response.text


with open('daili3.html','w',encoding='utf-8')as fp:
    fp.write(content)


