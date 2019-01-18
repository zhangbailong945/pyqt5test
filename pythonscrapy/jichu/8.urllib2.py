'''
HTMLParser 简介
feed:向解析器喂数据，可以分段提供
handler-star他搞：处理html开始的标签
a.tag:标签名称
b.attrs:属性列表

handler_data:处理标签里的数据体
Data:数据文本


'''

import urllib

from HTMLParser import HTMLParser
from prettytable import PrettyTable

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.movies=[]
    
    def handle_startendtag(self,tag,attrs):

        def _attr(attrlist,attrname):
            for attr in attrlist:
                if attr[0]==attrname:
                    return attr[1]
            return None
        
        if tag=='li' and _attr(attrs,'data-title'):
            movie={}
            movie['title']=_attr(attrs,'data-title') #电影名称