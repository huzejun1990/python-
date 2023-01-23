# @Author : huzejun
# @Time : 2023/1/23 19:49

import urllib.request

url = 'https://www.jd.com/'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

print(content)
