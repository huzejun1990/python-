# @Author : huzejun
# @Time : 2023/1/23 23:28

from selenium import webdriver

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

url = 'https://www.baidu.com'
browser.get(url)

# 元素定位

# 根据id来找到对象
# button = browser.find_element_by_id('su')
# button = browser.find_element(by='id',value='su')
# print(button)

# 根据标签属性的属性值来获取对象的
# button = browser.find_element(by='name',value='wd')
# print(button)

# button = browser.find_elements(by='xpath',value='//input[@id="su"]')
# print(button)
# for btn in button:
#     print(btn)

# //a[@class="n"]

# Chrome.find_element(By.XPATH,'//*[@id="s-top-loginbtn"]').click()

# button = browser.find_element(by='xpath',value='//input[@id="su"]')
# print(button)

# 根据标签的名字来获取对象
# button = browser.find_element(by='tag_name',value='input')
# button = browser.find_elements_by_tag_name('input')
# print(button)

# 使用的bs4的语法来获取对象
# button = driver.find_element_by_css_selector('#su')
# print(button)

#

# button = browser.find_element_by_link_text(新闻)
# print(button)