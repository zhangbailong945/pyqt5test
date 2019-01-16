# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Bookdemo1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    price=scrapy.Field()
    review_rating=scrapy.Field()
    review_num=scrapy.Field()
    upc=scrapy.Field()
    stock=scrapy.Field()

class Biquge_Books(scrapy.Item):
    bname=scrapy.Field()
    bauthor=scrapy.Field()
    bdate=scrapy.Field()
    bintroduction=scrapy.Field()


class Biquge_Chapters(scrapy.Item):
    bid=scrapy.Item()
    chaname=scrapy.Item()
    chalink=scrapy.Item()
    chacontent=scrapy.Item()
