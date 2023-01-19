# @Author : huzejun
# @Time : 2023/1/19 19:36

import urllib.request
import urllib.error

# url = 'https://blog.csdn.net/sulixu/article/details/1198189491'

url = 'http://www.abc111.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

try:

    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)
except urllib.error.HTTPError:
    print('系统正在升级。。。')
except urllib.error.URLError:
    print('系统提醒 系统正在升级中。。。')
