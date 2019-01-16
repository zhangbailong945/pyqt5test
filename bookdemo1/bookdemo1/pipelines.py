# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo,sqlite3
from scrapy.item import Item

class Bookdemo1Pipeline(object):
    def process_item(self, item, spider):
        return item


class MongoDBPipeline(object):

    @classmethod
    def from_crawler(cls,crawler):
        cls.DB_URI=crawler.settings.get('MONGO_DB_URI')
        cls.DB_NAME=crawler.settings.get('MONGO_DB_NAME')

        return cls()
    
    def open_spider(self,spider):
        self.client=pymongo.MongoClient(self.DB_URI)
        self.db=self.client[self.DB_NAME]
    
    def close_spider(self,spider):
        self.client.close()
    
    def process_item(self,item,spider):
        collection=self.db[spider.name]
        post=dict(item) if isinstance(item,Item) else item
        collection.insert_one(post)
        return item
    

class Sqlite3DBPipeline(object):

    def open_spider(self,spider):
        db_name=spider.settings.get('SQLITE3_DB_NAME','novels.db')
        self.db_conn=sqlite3.connect(db_name)
        self.db_cursor=self.db_conn.cursor()
    
    def close_spider(self,spider):
        self.db_conn.close()
    
    def process_item(self,item,spider):
        self.insert_books(item)
        return item
    
    def insert_books(self,item):
        values=(
            item['bname'],
            item['bauthor'],
            item['bdate'],
            item['bintroduction'],

        )
    
        sql='INSERT INTO books VALUES(null,?,?,?,?)'
        self.db_cursor.execute(sql,values)
        self.db_conn.commit()