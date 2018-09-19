# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.exporters import CsvItemExporter
import csv
class KmmallPipeline(object):
    def process_item(self, item, spider):
        return item






class KmCsvPipeline(object):
    def open_spider(self, spider):
        # 创建文件对象
        self.f = open("km2.csv", "w+")
        # 这种写法还没搞清楚怎么用
        # self.csv_exporter = CsvItemExporter(self.f)
        # 开始进行csv数据读写
        # self.csv_exporter.start_exporting()
        # 创建csv文件读写对象，用来将item数据写入到指定的文件中
        self.csv_writer = csv.writer(self.f, delimiter=',')



    def process_item(self, item, spider):
        # 将item数据通过csv文件读写对象，写入到csv文件中
        # 将item变成字典对象
        item = dict(item)
        # 如果需要保存json就dumps一下
        # item = json.dumps(item, ensure_ascii=False)
        # self.csv_exporter.export_item(item.encode("utf8"))
        print('*******************************************************item:', item)
        print('*******************************************************item:', type(item))
        # print('*******************************************************item:', item['goods_url'])
        # 提取字典对象的数据类型是class:dict   数据格式类似 {item:{"key1":"val1","key2":"val2"...}}
        one=item['one']
        two=item['two']
        two_url=item['two_url']
        three=item['three']
        three_url=item['three_url']
        title=item['title']
        title_two=item['title_two']
        price=item['price']
        goods_url=item['goods_url']
        market_price = item['market_price']
        spec=item['spec']
        count_comment=item['count_comment']
        goods_name=item['goods_name']
        goods_no=item['goods_no']
        goods_pz=item['goods_pz']
        goods_logo=item['goods_logo']
        goods_spec=item['goods_spec']
        goods_jx=item['goods_jx']
        goods_cj=item['goods_cj']
        self.csv_writer.writerow([one,two,two_url,three,three_url,title,title_two,price,market_price,spec, goods_url,count_comment,goods_name,goods_no,goods_pz,goods_logo,goods_spec,goods_jx,goods_cj])
        return item

    def close_spider(self, spider):
        # 结束csv文件读写
        # self.csv_exporter.finish_exporting()
        # 关闭文件，将内存缓冲区的数据写入到磁盘中
        self.f.close()
