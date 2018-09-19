# -*- coding: utf-8 -*-
import scrapy
from kmmall.items import KmmallItem
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class KmspiderSpider(scrapy.Spider):
    name = 'kmspider'
    allowed_domains = ['km1818.com']
    base_url = "http://search.km1818.com/"
    start_urls = [base_url]
    def parse(self, response):
        # 提取所有二级url
        print("parse in*****************************")
        two_list = response.xpath("//div[@class='box-lis-item']/dl/dd/em/a/@href").extract()
        for two_url in two_list:
            print("parse out*****************************")
            yield scrapy.Request(two_url, callback=self.parse_two)

    def parse_two(self, response):
        print("parse_two in*****************************")
        # 一级标题
        one_title = response.xpath("/html/body/div[3]/h1/a/text()").extract_first()
        two = response.xpath("/html/body/div[3]/span[1]/a[1]/text()").extract_first()
        two_path = response.xpath("/html/body/div[3]/span[1]/a[1]/@href").extract_first()
        three_path = response.xpath("/html/body/div[3]/span[2]/a[1]/@href").extract_first()
        # 有些Nonetype没数据的url,如果不设置成字符串无法拼接，调度器会忽略这些url不保存
        if two_path or three_path is not str:
            two_path = str(two_path)
            three_path = str(three_path)
        # 拼接url
        two_url = self.base_url+"10/"+two_path
        three_url = self.base_url+"10/"+three_path
        # 三级标题
        three = response.xpath("/html/body/div[3]/span[2]/a[1]/text()").extract_first()
        # 商品url列表
        goods_list = response.xpath("//div[@class='m-prosales-cont']/ul/li/div[2]/a/@href").extract()
        for goods_url in goods_list:
            print("parse_two out*****************************")
            # 传给下个爬虫
            yield scrapy.Request(goods_url, callback=self.parse_three, meta={"two":two,"two_url":two_url,"three":three,"three_url":three_url,"one_title":one_title,"goods_url":goods_url})
        # # 下面是只爬一个页面写法,遍历２级页面，提取字段内容
        # for node in node_list:
        #     item = KmmallItem()
        #     item['one'] = response.xpath("/html/body/div[3]/h1/a/text()").extract_first()
        #     item['two'] = response.xpath("/html/body/div[3]/span[1]/a/text()").extract_first()
        #     item['two_url'] = self.base_url+response.xpath("/html/body/div[3]/span[1]/a/@href").extract_first()
        #     item['three'] = response.xpath("/html/body/div[3]/span[2]/a/text()").extract_first()
        #     item['three_url'] = self.base_url+response.xpath("/html/body/div[3]/span[2]/a/@href").extract_first()
        #     li_list = node.xpath('./li')
        #     for li in li_list:
        #         item['title'] = li.xpath('./div/a/@title').extract_first()
        #         item['goods_url'] = li.xpath('./div[1]/a/@href').extract_first()
        #         item['price'] = li.xpath('./div[3]/strong/text()').extract_first()
        #         # item['head'] = li.xpath("normalize-space(//div[@class='m-prosales-cont']/ul[1]/li[1]/div[2]/a/text())").extract_first()
        #         item['head'] = li.xpath("./div[2]/a/text()").extract_first()

    def parse_three(self, response):
        print("parse_three in*****************************")
        item = KmmallItem()
        # 用selenium爬评论数，scrapy的xpath无法获取
        # 创建Options对象
        options = Options()
        # 设置无界面
        options.set_headless()
        # 创建Chrome的驱动对象
        driver = webdriver.Chrome(options=options)
        driver.get(response.url)
        try:
            item['count_comment']=driver.find_element_by_id("countComment").text
            print("item['count_comment']:", item)
        except Exception as e:
            print(e)
            print("item['count_comment']:", item)
            item['count_comment'] =None
        time.sleep(2)

        # 退出浏览器
        driver.quit()
        # 调用管道Item

        node=response.xpath("//div[@class='product-intro']")
        item['one']=response.meta['one_title']
        item['two'] = response.meta['two']
        item['two_url'] = response.meta['two_url']
        item['three'] = response.meta['three']
        item['three_url'] = response.meta['three_url']
        item['title'] = node.xpath("./div[2]/div[1]/h1/text()").extract_first()
        item['title_two'] = response.xpath("/html/body/div[6]/div[1]/div[2]/div[1]/h1/span/text()").extract_first()
        item['goods_url'] = response.meta['goods_url']
        item['price'] = node.xpath("./div[2]/div[2]/div[1]/ul[1]/li[3]//label/text()").extract_first()
        item['market_price'] = node.xpath("./div[2]/div[2]/div[1]/ul[1]/li[4]//del/text()").extract_first()
        item['spec'] = node.xpath("./div[2]/div[2]/div[1]/ul[1]/li[7]/dd/a/text()").extract_first()
        # item['count_comment'] = response.xpath("//div[contains(@class,'list-info')]/ul/li[6]//label").extract_first()
        item['goods_name'] = response.xpath("//ul[@class='detail-list']/li[1]/text()").extract_first()
        item['goods_no'] = response.xpath("//ul[@class='detail-list']/li[2]/text()").extract_first()
        item['goods_pz'] = response.xpath("//ul[@class='detail-list']/li[3]/text()").extract_first()
        item['goods_logo'] = response.xpath("//ul[@class='detail-list']/li[4]/text()").extract_first()
        item['goods_spec'] = response.xpath("//ul[@class='detail-list']/li[5]/text()").extract_first()
        item['goods_jx'] = response.xpath("//ul[@class='detail-list']/li[6]/text()").extract_first()
        item['goods_cj'] = response.xpath("//ul[@class='detail-list']/li[7]/text()").extract_first()
        print("parse_three out*****************************")
        yield item








