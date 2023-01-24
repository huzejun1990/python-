# @Author : huzejun
# @Time : 2023/1/24 20:18

# 通过登录 然后进入到页面

# 通过找登陆接口我们发现 登陆的时候需要的参数很多
# __VIEWSTATE:I1pLG4no435SrfA0pv2HyAHAeK3IYH8S7ZbilqXhgrGwSx5rSt4tyt7NvGj+ik89IAXn9e84N8BKFAJ1rQKDimL/MEZ4ULzKu+67sv4nMPTS5G+fBKjf8RBnm6LZdOZw2ZgsSmC3COCT+zJIgmqWaPUBexw=
# __VIEWSTATEGENERATOR:C93BE1AE
# from:http://so.gushiwen.cn/user/collect.aspx
# email:961639130@qq.com
# pwd:123456
# code:ctti
# denglu:登录

# 我们观察到 __VIEWSTATE __VIEWSTATEGENERATOR code是一个可以变化的量

# 难点： （1）__VIEWSTATE __VIEWSTATEGENERATOR 一般情况下看不到的数据 都是在页面的源码中
#         我们观察到这两个数据在页面的源码中 所以我们需要获取页面的源码 然后进行解析就可以获取了
#       （2）验证码

import requests

# 登陆页面的url地址
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

response = requests.get(url=url,headers=headers)
content = response.text

# 解析页面源码 然后获取 __VIEWSTATE __VIEWSTATEGENERATOR

from bs4 import BeautifulSoup

soup = BeautifulSoup(content,'lxml')

# 获取__VIEWSTATE
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')

# 获取 __VIEWSTATEGENERATOR
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

# 获取验证码图片
code = soup.select('#imgCode')[0].attrs.get('src')
code_url = 'https://so.gushiwen.cn' + code

# 有坑
# import urllib.request
# urllib.request.urlretrieve(url=code_url,filename='code.jpg')

# requests里面有一个方法 session() 通过session的返回值 就能使请求变成一个对象

session = requests.session()
# 验证码的url的内容
response_code = session.get(code_url)
# 注意此时要使用进制数据 因为我们要使用的是图片的下载
content_code = response_code.content
# wb的模式就是将二进制写入到文件
with open('code.jpg','wb')as fp:
    fp.write(content_code)


# 获取了验证码的图片之后，下载到本地 然后观察验证码 观察之后 然后在控制台输入这个验证码 就可以将这个值
# code的参数 就可以登录

code_name = input('请输入你的验证码')

# 点击登陆
url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

data_post = {
    '__VIEWSTATE':viewstate,
    '__VIEWSTATEGENERATOR':viewstategenerator,
    'from':'http://so.gushiwen.cn/user/collect.aspx',
    'email':'961639130@qq.com',
    'pwd':'123456',
    'code':code_name,
    'denglu':'登录'
}

response_post = session.post(url=url,headers=headers,data=data_post)

content_post = response_post.text

with open('gushiwen.html','w',encoding='utf-8')as fp:
    fp.write(content_post)

# 难点
# （1）隐藏域
# （2）验证码