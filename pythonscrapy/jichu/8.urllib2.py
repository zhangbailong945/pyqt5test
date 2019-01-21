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
from urllib.request import Request,urlopen
from html.parser import HTMLParser
from prettytable import PrettyTable

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.movies=[]
    
    def handle_starttag(self,tag,attrs):

        def _attr(attrlist,attrname):
            for attr in attrlist:
                if attr[0]==attrname:
                    return attr[1]
            return None
        
        if tag=='li' and _attr(attrs,'data-title'):
            movie={}
            movie['title']=_attr(attrs,'data-title') #电影名称
            movie['score']=_attr(attrs,'data-score') #电影分数
            movie['director']=_attr(attrs,'data-director') #电影导演
            movie['actors']=_attr(attrs,'data-actors') #电影演员
            self.movies.append(movie)
            print('%(title)s|%(score)s |%(director)s| %(actors)s'% movie)
    
def nowplaying_movies(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'
    }   #模拟一个浏览器的行为
    req =Request(url, headers=headers)  #定制一个http头
    response = urlopen(req)  #获取这个请求
    body=response.read().decode('utf-8')
    parser = MyHTMLParser()  #解析器
    parser.feed(body)
    response.close()
    return parser.movies  #把解析器里面的movies返回给调用者


if __name__=='__main__':
    url='https://movie.douban.com/cinema/nowplaying/beijing'
    movies=nowplaying_movies(url)
    import json
    print('%s'%json.dumps(movies,sort_keys=True,indent=4,separators=(',',':')))