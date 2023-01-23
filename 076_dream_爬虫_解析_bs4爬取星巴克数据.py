# @Author : huzejun
# @Time : 2023/1/23 18:16

import urllib.request

url = 'https://www.starbucks.com.cn/menu/'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

# print(content)

from bs4 import BeautifulSoup

soup = BeautifulSoup(content,'lxml')

# // //ul[@class="grid padded-3 product"]//strong/text()

# name_list = soup.select('.grid padded-3 product')
name_list = soup.select('ul[class="grid padded-3 product"] strong')

for name in name_list:
    print(name.get_text())

# print(name_list)


