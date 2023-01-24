# @Author : huzejun
# @Time : 2023/1/24 18:08
import encodings

import requests

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

data = {
    'kw': 'eye'
}

# url 请求地址
# data 请求参数
# kwargs 字典

response = requests.post(url=url,data=data,headers=headers)

content = response.text



# obj = unicode(content,'utf-8')
# print(obj)

# content = response.text
#
import json
#
# obj = json.loads(content,encoding='utf-8') # 在不能python版本，可能会出现错误
obj = json.loads(content.encode('utf-8')) # python3.10 写法

print(obj)

# 总结
# （1）post请求 是不需要编解码
# （2）post请求的参数是data
# （3）不需要请求对象的定制
