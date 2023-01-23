# @Author : huzejun
# @Time : 2023/1/24 1:31

from selenium import webdriver

# 创建浏览器对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

# url
url = 'https://www.baidu.com'
browser.get(url)

import time
time.sleep(2)

# 获取文本框的对象
input = browser.find_element(by='id',value='kw')

# 在文本框中输入文本（周杰伦）
input.send_keys('周杰伦')

time.sleep(2)

# 获取百度一下的按钮
button = browser.find_element(by='id',value='su')

# 点击按钮
button.click()

time.sleep(2)

# 滑到底层
js_bottom = 'document.documentElement.scrollTop=10000'
browser.execute_script(js_bottom)

time.sleep(2)

# 获取下一页的按钮
next = browser.find_element(by='xpath',value='//a[@class="n"]')
# print(next)
# 点击下一页
next.click()

time.sleep(2)

# 回到上一页
browser.back()

time.sleep(2)

# 回去
browser.forward()

time.sleep(3)

# 退出
browser.quit()

# next = browser.find_element(By.XPATH,'//a[@class="n"]').click()

# next = browser.find_element(by='xpath',value="//a[@class="n"]")

# find_element(by='xpath',value='//input[@id="su"]')

