import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    # allowed_domains = ['bj.58.com'] # https://bj.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=classify_B
    allowed_domains = ['https://bj.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91'] # https://bj.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=classify_B
    # start_urls = ['http://bj.58.com/']
    start_urls = ['https://bj.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91']

    def parse(self, response):
        # 字符串
        # content = response.text
        # 二进制数据
        # content = response.body
        # print("==============================")
        # print(content)

        span = response.xpath('//div[@id="filter"]//div[@class="tabs"]/a/span')[0]
        print("===============")
        # .extract()
        print(span.extract())
