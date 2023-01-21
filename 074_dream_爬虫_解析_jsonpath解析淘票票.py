# @Author : huzejun
# @Time : 2023/1/21 20:33

import urllib.request

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1674305282123_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'


# url = 'https://dianying.taobao.com/cityAction.json?city=&_ksTS=1674304033422_19&jsoncallback=jsonp20&action=cityAction&n_s=new&event_submit_doLocate=true'

headers = {
    # ':authority': 'dianying.taobao.com',
    # ':method': 'GET',
    # ':path': '/cityAction.json?city=&_ksTS=1674304033422_19&jsoncallback=jsonp20&action=cityAction&n_s=new&event_submit_doLocate=true',
    # ':scheme': 'https',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 't=c036667512e54eb85cbe295c1eca4bdc; cookie2=109fa79f62e13002bbb0fa53ad640aa1; v=0; _tb_token_=33e37b18507e3; cna=xS04HESdC1wCAW/E8ftQDcb4; xlly_s=1; isg=BEhIIiTDv6DkWtMkEDLT1Ot4GbZa8az7uQa08AL4k0O63ehHqwDsi8QcVbWtVmTT; l=fBN-VAKqTefZd0zKBO5Bourza77tmIOb4lVzaNbMiIEGa1PfTen9KNCesx627dtjgTCm5eKz_ANlDdLHR3c-wxDDB7kqm0Sj3xv9QaVb5; tfstk=cchGBsjlqAy62lRxAcN6wt1Y_L9RCZbUXmosTe5t3x1I0nvYRR5mW9WPDgJ3x3tNh',
    'referer': 'https://dianying.taobao.com/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

request = urllib.request.Request(url = url,headers = headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# split 切割
content = content.split('(')[1].split(')')[0]

with open('074_dream_爬虫_解析_jsonpath解析淘票票.json','w',encoding='utf-8')as fp:
    fp.write(content)

import json
import jsonpath

obj = json.load(open('074_dream_爬虫_解析_jsonpath解析淘票票.json','r',encoding='utf-8'))

city_list = jsonpath.jsonpath(obj,'$..regionName')

print(city_list)

