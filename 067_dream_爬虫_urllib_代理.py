# @Author : huzejun
# @Time : 2023/1/19 21:15
import urllib.request

# url = 'http://www.baidu.com/s?wd=ip'

url = 'https://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
# }

# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

# 模拟浏览器来访问服务器
# response = urllib.request.urlopen(request)

proxies = {
    'http':'121.13.252.60:41564'
}

# handler build_opener open
handler = urllib.request.ProxyHandler(proxies = proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

# 获取响应的信息
content = response.read().decode('utf-8')

# 保存
with open('daili_22.html','w',encoding='utf-8')as fp:
    fp.write(content)