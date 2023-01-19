# @Author : huzejun
# @Time : 2023/1/19 19:57

# 适用场景：数据采集的时候需绕过登陆 然后进入到某个页面
# 个人信息页面是utf-8 但是还报错了，编码错误，因为并没有进入到信息页面，而是跳转到了登陆页面
# 登录页面不是 utf-8 所有报错

# 什么情况下访问不成功？
# 因为请求头的解析不够

import urllib.request

url = 'https://weibo.cn/6451491586/info'

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
# }
headers = {
# ':authority': 'weibo.cn',
# ':method': 'GET',
# ':path': '/6451491586/info',
# ':scheme': 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cache-control': 'max-age=0',
# cookie 中携带着你的登陆信息 如果有登陆之后的cookie 那么我们就可以携带着cookie进入到任何页面
'cookie': '_T_WM=4bb7102ecee1d98138c860f98c2b9167; SCF=Apn3WJualV91XNZLJas6aZawJUgLjC3kSvMwoEdFa5v1xLuu3MnP_7ciS4HT9Nd3VEqaoQ4olGzfrwDMxwjGCMs.; SUB=_2A25OzUeGDeRhGedN7FEV-C7EyziIHXVqTmnOrDV6PUNbktAKLWSmkW1NVeXAYyXeMOlofJOn1C70EbyLVMZT81TZ; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhSKGMkVU8P8VzoX6HJJOWT5JpX5KMhUgL.Fo20S0eX1h5RehB2dJLoIERLxK-L12eL1KMLxKBLB.2LB-Ski--RiKn0i-2pi--ci-z0i-i2i--fiKnciKLF; SSOLoginState=1674131414; ALF=1676723414',
# referer 判断当前路径是不是由上一个路径进来的    一般情况下 是做图片的防盗链
'referer': 'https://login.sina.com.cn/',
'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'cross-site',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 获取响应的数据
content = response.read().decode('utf-8')  # gb2312
# content = response.read().decode('gb2312')  # gb2312


# 将数据保存到本地 gb2312
with open('weibo.html','w',encoding='utf-8')as fp:
    fp.write(content)