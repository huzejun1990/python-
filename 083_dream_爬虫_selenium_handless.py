# @Author : huzejun
# @Time : 2023/1/24 2:52

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
#  # path是你自己的chrome浏览器的文件路径
# path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
# chrome_options.binary_location = path
#
# browser = webdriver.Chrome(chrome_options=chrome_options)
#
# url = 'https://www.baidu.com'
#
# browser.get(url)
#
# browser.save_screenshot('baidu.png')

# 封装的 handless

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def share_browser():


    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # path是你自己的chrome浏览器的文件路径
    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path

    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser

browser = share_browser()

url = 'https://www.baidu.com'

browser.get(url)