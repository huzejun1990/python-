# @Author : huzejun
# @Time : 2023/1/18 17:50

# post请求
import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

data = {
    'kw':'spider',

}

# post请求的参数 必须要进行编码
data = urllib.parse.urlencode(data).encode('utf-8')
# print(data)

# post的请求参数 是不会拼接在url的后面 而是需要放在请求对象定制的参数中
request = urllib.request.Request(url=url,data=data,headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的数据
content = response.read().decode('utf-8')

# 字符串 --》json对象

import json
obj = json.loads(content)
print(obj)


# post 请求方式的参数 必须编码 data = urllib.parse.urlencode(data)
# 编码之后 必须调用 encode方法 data = urllib.parse.urlencode(data).encode('utf-8')
# 参数是放在请求对象定制的方法中 request = urllib.request.Request(url=url,data=data,headers=headers)
