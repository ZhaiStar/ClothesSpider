# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ClothesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    # 品类
    pinlei = scrapy.Field()
    # 分类
    fenlei = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 货号
    coodsNo = scrapy.Field()
    # 重量
    weight = scrapy.Field()
    # 上架时间
    time = scrapy.Field()
    # 图片
    picture = scrapy.Field()
    # 折扣
    discount = scrapy.Field()
    # 颜色
    color = scrapy.Field()
    # 状态
    state = scrapy.Field()
    # 数量
    number = scrapy.Field()
    # 销量
    sales = scrapy.Field()