# @Author : huzejun
# @Time : 2023/1/23 20:09

# (1)导入selenium
from selenium import webdriver

# (2) 创建浏览器操作对象

path = 'chromedriver.exe'

broweser = webdriver.Chrome(path)

# （3）访问网站
# url = 'https://www.baidu.com'

# broweser.get(url)

url = 'https://www.jd.com/'
broweser.get(url)

# page_source获取网页源码
content = broweser.page_source
print(content)