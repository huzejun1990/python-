# @Author : huzejun
# @Time : 2023/1/24 2:10

from selenium import webdriver

# path = 'phantomjs.exe'
path = r'E:\Python\Python310\phantomjs-2.1.1-windows\bin\phantomjs.exe'
browser = webdriver.PhantomJS(path)

url = 'https://www.baidu.com'
browser.get(url)

browser.save_screenshot('baidu1.png')
#
import time
time.sleep(2)
#
input = browser.find_element_by_id('kw')
input.send_keys('昆凌')

time.sleep(3)

browser.save_screenshot('kunling1.png')