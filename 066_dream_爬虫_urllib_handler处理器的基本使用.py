# @Author : huzejun
# @Time : 2023/1/19 20:49

# 需求 使用handler来访问百度 获取网页源码

import urllib.request

url = 'http://www.baidu.com'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=headers)

# handler  build_opener open

# (1)获取hanlder对象
handler = urllib.request.HTTPHandler()

# (2) 获取opener对象
opener = urllib.request.build_opener(handler)

# (3) 调用open方法
response = opener.open(request)
content = response.read().decode('utf-8')

print(content)
# (4)

