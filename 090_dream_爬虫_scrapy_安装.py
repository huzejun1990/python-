# @Author : huzejun
# @Time : 2023/1/24 22:53

# （1）pip install scrapy
# (2)报错1：building 'twisted,test.raiser' extension
# 解决 1
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
# twisted_iocpsupport-1.0.2-cp310-cp310-win_amd64.whl
# cp是你的python版本
# amd是你的操作系统的版本
# 下载完成之后 使用 pip install twisted的路径 安装
# 切记安装完twisted 再次安装scrapy

# （3）报错2 提示python -m pip install --upgrade pip
#     解决2 运行python -m pip install --upgrade pip

# (4)报错3 win32的错误
#    解决3 pip install pypiwin32

# (5) anaconda
