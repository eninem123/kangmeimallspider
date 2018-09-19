# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See docmentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KmmallItem(scrapy.Item):
    # define the fields for your item here like:
    # title2 = scrapy.Field()
    # t2_url = scrapy.Field()
    # title3 = scrapy.Field()
    # t3_url = scrapy.Field()
    # 一级标题
    one = scrapy.Field()
    # ２级标题
    two = scrapy.Field()
    # ２级标题url
    two_url = scrapy.Field()
    # 3级标题
    three = scrapy.Field()
    # 3级标题url
    three_url = scrapy.Field()
    # 商品主标题
    title = scrapy.Field()
    goods_url = scrapy.Field()
    # 售价
    price = scrapy.Field()
    # 商品副标题
    title_two = scrapy.Field()
    # 市场价
    market_price = scrapy.Field()
    # 规格
    spec = scrapy.Field()
    # 评论数
    count_comment = scrapy.Field()
    # 商品简介
    goods_name = scrapy.Field()
    goods_no = scrapy.Field()
    # 批准文号
    goods_pz = scrapy.Field()
    # 商品品牌
    goods_logo = scrapy.Field()
    # 规格
    goods_spec = scrapy.Field()
    # 剂型
    goods_jx = scrapy.Field()
    # 生产厂家
    goods_cj = scrapy.Field()



