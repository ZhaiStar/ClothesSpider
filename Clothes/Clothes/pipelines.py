# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="root",
                     database="clothes")

cursor = db.cursor()


class ClothesPipeline(object):
    def process_item(self, item, spider):
        sql = "insert into customer_fenlei value(fenlei,pinlei_id): "
        cursor.execute(sql)
        cursor.commit()

        return item
