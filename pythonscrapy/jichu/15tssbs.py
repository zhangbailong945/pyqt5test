import requests
import re
import os

from MySqlite3 import MySqlite3
from html.parser import HTMLParser


#爬取唐诗三百首
#爬取目标地址：https://www.gushiwen.org/gushi/tangshi.aspx


def attr(attrlist, attrname):
    '''
    遍历html标签里的属性，如果属性一致则返回属性内容
    '''
    for attr in attrlist:
        if attr[0] == attrname:
            return attr[1]
    return None


class MyHtmlParser(HTMLParser):
    '''
    爬取首页的分类以及诗集
    '''

    def __init__(self):
        HTMLParser.__init__(self)
        self.categorys = []  # 存放唐诗三百首分类
        self.categorys_list = []  # 分类对应的诗集
        self.category_div = False
        self.category_div_strong = False
        self.category_div_span=False
        self.category_div_a=False

    def handle_starttag(self, tag, attrs):
        '''
        处理html开始标签
        '''
        if tag == 'div' and attr(attrs, 'class') == 'typecont':
            self.category_div = True
            self.category_div_strong = True
            self.category_div_span=True
            self.category_div_a=True
    
        if tag=='a' and self.category_div_span:
            turl=attr(attrs,'href')
            self.categorys_list.append(turl)


            

    def handle_endtag(self, tag):
        '''
        处理html的结束标签
        '''
        if tag == 'div':
            self.category_div = False
            self.category_div_strong = False
            
            self.category_div_a=False
            
            
            

    def handle_data(self, data):
        '''
        处理标签包裹的文本内容
        '''
        if self.category_div_strong:
            if data!='\n':
                self.categorys.append(data)
        


#请求头信息
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Host': 'www.gushiwen.org',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}


def start_request():
    url = 'https://www.gushiwen.org/gushi/tangshi.aspx'
    response = requests.get(url, headers=headers)
    htmlContent = response.content.decode('utf-8')
    parser = MyHtmlParser()
    parser.feed(htmlContent)
    return parser.categorys,parser.categorys_list


if __name__ == '__main__':
    list1,list2=start_request()
    #五言绝句
    wyjjList=list2[0:29]
    #七言绝句
    qyjjList=list2[29:80]
    #五言律诗
    wyysList=list2[80:160]
    #七言律诗
    qyysList=list2[160:213]
    #五言古诗
    wygsList=list2[213:248]
    #七言古诗
    qygsList=list2[248:276]
    #乐府
    yfList=list2[276:320]
    categoryList=[wyjjList,qyjjList,wyysList,qyysList,wygsList,qygsList,yfList]
    sbDict=dict(zip(list1,categoryList))
    print(sbDict)
    
