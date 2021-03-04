# -*- coding: utf-8 -*-
import random

import scrapy
from ..items import ClothesItem
from copy import deepcopy


class ClothesSpider(scrapy.Spider):
    name = 'clothes'
    allowed_domains = ['taobao.com']
    start_urls = ['https://www.hznzcn.com/gallery-150-grid.html']

    def parse(self, response):
        item = ClothesItem()
        label = response.xpath('//div[@id="productclasslist_div"]//a/text()').extract()
        url = response.xpath('//div[@id="productclasslist_div"]//a/@href').extract()
        for k, v in zip(label, url):
            if k == "全部":
                pass
            else:
                item["fenlei"] = k
                url = "https://www.hznzcn.com" + v
                yield scrapy.Request(url=url, meta={"item": deepcopy(item)}, callback=self.parse_list, dont_filter=True)
        # with open("衣服.html", "w", encoding="utf-8")as f:
        #     f.write(response.body.decode('utf-8'))

    def parse_list(self, response):
        item = response.meta["item"]
        li_list = response.xpath('//div[@id="productList_Div"]/ul/li')
        for i in li_list:
            base = "https://www.hznzcn.com"
            detail_url = base + i.xpath('.//div[@class="rowTitle"]/a/@href').extract()[0]
            print(detail_url)
            item["url"] = detail_url
            yield scrapy.Request(url=detail_url, meta={"item": deepcopy(item)}, callback=self.parse_detail,
                                 dont_filter=True)

    def parse_detail(self, response):
        item = response.meta["item"]
        # 标题
        title = response.xpath('//div[@class="detail-midtitle"]/h1/text()').extract()
        item["title"] = title[0]
        # 价格
        price = response.xpath('//label[@id="productShopPrice"]/text()').extract()
        item["price"] = price[0]

        # 货号
        coodsNo = response.xpath('//div[@class="mid-brand"]/span[1]/label/text()').extract()
        item["coodsNo"] = coodsNo[0]

        # 重量
        weight = response.xpath('//div[@class="mid-brand"]//span[@id="ProductWeight"]/text()').extract()
        item["weight"] = weight[0]

        # 上架时间
        time = response.xpath('//div[@class="mid-brand"]/span[@class="midbrand-2 difWid"]/label/text()').extract()
        item["time"] = time[0]

        # 折扣
        discount = float(price[0]) - random.randrange(0, 20)
        item["discount"] = 0 if discount < 0 else discount
        # 图片
        picture = []
        pictures = response.xpath('//div[@id="imageMenu"]/ul/li/a/img/@src').extract()
        for i in pictures:
            picture.append(i.split("/")[-1])
        item["picture"] = ",".join(picture)

        # 颜色
        color = response.xpath('//div[@id="em0"]/span/img/@alt').extract()
        if len(color) == 0:
            color = response.xpath('//div[@id="em0"]/span/text()').extract()
        item["color"] = ",".join(color)
        # 状态 上架 1 下架 0
        item["state"] = 1
        # 数量
        item["number"] = random.randint(400, 600)
        # 销量
        item["sales"] = item["number"] - random.randint(100, 300)
        print(item)
