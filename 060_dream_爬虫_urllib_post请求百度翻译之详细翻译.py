# @Author : huzejun
# @Time : 2023/1/18 22:42

import urllib.request

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
# 'Accept': '*/*',
# 'Accept-Encoding': 'gzip, deflate, br',
# 'Accept-Language': 'zh-CN,zh;q=0.9',
# 'Acs-Token': '1674029128306_1674052523482_gNF6xEf4eCcQZnLEAQDq4dA12UqNF/gQddV4G64w+VHdFqNXJWTuTGiPN2mIUfYwJeyEQqETIfTkSq1/gnEuDj6SsEPIZSLS4CFyhwsbR9CuWdJF3OTUwVWSKSTFuI+ojk2YGE72wY0tl72XCQ9iqIaiDmKwQHwN1jHRp0UHm0zKkNd24djmoJhjJ6uCOUcY8vHrBYrSagB7SWEq67fNxsDj0OvvQY144/UWdHS0Z1KuQG5UWCBxmlPt3C7hsBmXZR88++BZdOKipnkS30m7YvyM70iM06758tV9XKIoRqS81kK4mcTWWCcMGpOubeR8',
# 'Connection': 'keep-alive',
# 'Content-Length': '116',
# 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'BIDUPSID=BBCEA4EC9DA1B63ED232D4838937F9EB; PSTM=1671620190; BAIDUID=BBCEA4EC9DA1B63E43C0E2654BB94775:FG=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; MCITY=-131%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=BBCEA4EC9DA1B63E43C0E2654BB94775:FG=1; H_PS_PSSID=36549_37647_38015_36920_37989_37802_37933_26350_38009_37881; BA_HECTOR=ah25212h2001a5al202ka5m01hsfb2i1l; ZFY=A7Thc2ohK2BxXtfMbVDrD9NI1CmlLN2huhkJM2:BzyJI:C; PSINO=2; delPer=0; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1673088772,1673264214,1673865135,1674031915; ab_sr=1.0.1_ZWI1NDg5Y2Q3N2JiMzkxNmM4Mzg2NzhmNzVkNDZkODFiOGViYzhkNmU1OGZhZmE5ODYyMjQ5NTc1MjViNWMyYWIwNWQzM2M0ODBiZTk4YTEyMDVjZDJjZjIyYWI2NzFhOWI1NGNmZDU5MWNmZDVmNDEyYWI4NWM4NGM0NWU0MmZhODBiM2E3MjgwMThlYjRkNGVkZGU1ODZiZjE2ZGQzMQ==; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1674052522',
# 'Host': 'fanyi.baidu.com',
# 'Origin': 'https://fanyi.baidu.com',
# 'Referer': 'https://fanyi.baidu.com/',
# 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
# 'sec-ch-ua-mobile': '?0',
# 'sec-ch-ua-platform': '"Windows"',
# 'Sec-Fetch-Dest': 'empty',
# 'Sec-Fetch-Mode': 'cors',
# 'Sec-Fetch-Site': 'same-origin',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
# 'X-Requested-With': 'XMLHttpRequest',
}


data = {
    'from': 'en',
    'to': 'zh',
    'query': 'love',
    'simple_means_flag': '3',
    'sign': '198772.518981',
    'token': '1132076b337f61413614fa32e61160d9',
    'domain': 'common',
}

# post请求的参数 必须进行编码 并且要调用 encode方法
data = urllib.parse.urlencode(data).encode('utf-8')


# 请求对象的定制
request = urllib.request.Request(url = url, data = data, headers = headers)

# 横扫浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的数据
content = response.read().decode('utf-8')

import json

obj = json.loads(content)

print(obj)