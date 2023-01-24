# @Author : huzejun
# @Time : 2023/1/24 15:53

import requests

url = 'https://www.baidu.com'

response = requests.get(url=url)

# 一个类型和六个属性
# Response类型
# print(type(response))

# 调转响应的编码格式
response.encoding = 'utf-8'

# 以字符串的形式来返回网页的源码
# print(response.text)

# 返回一个url地址
# print(response.url)

# 返回的是二进制的数据
# print(response.content)

# print(response.status_code)

# 返回各式响应头
print(response.headers)