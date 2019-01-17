# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo,sqlite3
from scrapy.item import Item
from .items import Biquge_Books,Biquge_Chapters

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
        if isinstance(item,Biquge_Books):
            self.insert_books(item)
            print('执行books')
            return item
        elif isinstance(item,Biquge_Chapters):
            self.insert_chapters(item)
            return item
        else:
            return item
    
    def insert_books(self,item):
        values=(
            item['bname'],
            item['bauthor'],
            item['bdate'],
            item['bintroduction'],

        )

        query='select * from books where bname=? and bauthor=?'
        rows=self.db_cursor.execute(query,(item['bname'],item['bauthor'])).fetchall()
        if len(rows)<1:
            sql='INSERT INTO books VALUES(null,?,?,?,?)'
            self.db_cursor.execute(sql,values)
            self.db_conn.commit()
    
    def insert_chapters(self,item):
        print('执行chapters')
        query='select * from books where bname=? and bauthor=?'
        row=self.db_cursor.execute(query,(item['bname'],item['bauthor'])).fetchone()
        print('book的编号：%s'%(str(row[0])))
        if row[0]>0:
            values=[]
            for link in item['clinks']:
                value=(row[0],link.text,link.url,'')
                values.append(value)
            sql='INSERT INTO chapters VALUES(null,?,?,?,?)'

            self.db_cursor.executemany(sql,values)
            self.db_conn.commit()
