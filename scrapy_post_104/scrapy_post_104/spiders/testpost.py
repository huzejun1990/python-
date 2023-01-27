import scrapy

import json




class TestpostSpider(scrapy.Spider):
    # https://fanyi.baidu.com/sug
    name = 'testpost'
    allowed_domains = ['https://fanyi.baidu.com/sug']
    # post请求 如果没有参数 那么这个请求将没有任何意义
    # 所以start_url 也没有用了
    # parse方法也没有用了
    # start_urls = ['http://fanyi.baidu.com/sug']
    #
    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'

        data = {
            'kw': 'final'
        }

        yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse_second)

    def parse_second(self,response):

        content = response.text
        # python3.10 写法
        obj = json.loads(content.encode('utf-8'))

        print(obj)