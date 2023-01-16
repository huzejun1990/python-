# @Author : huzejun
# @Time : 2023/1/16 21:24

import urllib.request

# 下载网页
# url_page = 'http://www.baidu.com'

# url代表的是下载的路径 filename文件的名字
# 在python中，可以变量的名字 也可以直接写值
# urllib.request.urlretrieve(url_page,'baidu.html')

# 下载图片
# url_img = 'https://img0.baidu.com/it/u=28574317,322636847&fm=253&fmt=auto&app=120&f=JPEG?w=500&h=1927'

# urllib.request.urlretrieve(url = url_img,filename='lisa.jpg')

# 下载视频
# url_video = 'https://haokan.baidu.com/v?vid=13392212293107285933&pd=pcshare&hkRelaunch=p1%3Dpc%26p2%3Dvideoland%26p3%3Dshare_input'

# urllib.request.urlretrieve(url_video,'buypen.mp4')

# url_video = "https://www.ixigua.com/18f978e6-2356-4ed2-ba1b-ed380b5cf8d8"

url_video = 'https://v.qq.com/x/cover/mzc00100mp6td10/f3064srkswu.html'

urllib.request.urlretrieve(url_video,'girl2.mp4')