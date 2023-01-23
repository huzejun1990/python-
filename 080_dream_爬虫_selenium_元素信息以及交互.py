# @Author : huzejun
# @Time : 2023/1/24 0:46

from selenium import webdriver

path = 'chromedriver.exe'

browser = webdriver.Chrome(path)

url = 'https://www.baidu.com'

browser.get(url)

input = browser.find_element(by='id',value='su')

# 获取标签的属性
print(input.get_attribute('class'))
# 获取标签的名字
print(input.tag_name)

# 获取元素文本
# a = browser.find_element_link_text('新闻')
# print(a.text)

