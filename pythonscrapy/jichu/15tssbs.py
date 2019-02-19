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
        


class ParserContent(HTMLParser):
    '''
    爬取唐诗三百首详情信息
    '''

    def __init__(self):
        HTMLParser.__init__(self)
        self.div=False
        self.title_h1=False
        self.translte_h2=False
        self.author_p=False
        self.author_p_num=0
        self.author_list=[]
        self.content_list=[]
        self.content_num=0
        self.content_div=False
        self.contyishang_div=False
        self.content_div_p=False
        self.contyishang_div_p=False
        self.contyishang_num=0
        self.content_detail_list=[]

    
    def handle_starttag(self,tag,attrs):
        if tag=='h1':
            self.title_h1=True
        
        if tag=='h2':
            self.translte_h2=True
        
        if tag=='p' and attr(attrs,'class')=='source':
            self.author_p=True
            self.author_p_num+=1
        
        if tag=='div' and attr(attrs,'class')=='contson':
            self.content_div=True
            self.content_num+=1
        
        if tag=='div' and attr(attrs,'class')=='contyishang':
            self.contyishang_num+=1
            self.contyishang_div=True
            self.contyishang_div_p=True
        
        

    def handle_endtag(self,tag):
        if tag=='h1':
            self.title_h1=False
        
        if tag=='h2':
            self.translte_h2=False
        
        if tag=='p':
            self.author_p=False
            self.contyishang_div_p=False
        
        if tag=='div':
            self.div=False
            self.content_div=False
            self.contyishang_div=False
    
    def handle_data(self,data):
        if self.title_h1:
            print('')

        if self.author_p and self.author_p_num==1:
            if data!='\n':
                self.author_list.append(data.strip())
        
        if self.content_div and self.content_num==1:
            if data!='\n':
                self.content_list.append(data.strip())
        
        if self.contyishang_div_p and self.contyishang_num==1:
            if data!='\n':
                self.content_detail_list.append(data)
    

    



#请求头信息
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Host': 'www.gushiwen.org',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

headers1 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}


def start_request():
    url = 'https://www.gushiwen.org/gushi/tangshi.aspx'
    response = requests.get(url, headers=headers)
    htmlContent = response.content.decode('utf-8')
    parser = MyHtmlParser()
    parser.feed(htmlContent)
    return parser.categorys,parser.categorys_list


def start_content_request():
    url = 'https://so.gushiwen.org/shiwenv_45c396367f59.aspx'
    response = requests.get(url, headers=headers1)
    htmlContent = response.content.decode('utf-8')
    parser = ParserContent()
    parser.feed(htmlContent)
    return parser.author_list,parser.content_list,parser.content_detail_list



if __name__ == '__main__':
    '''
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
    '''
    list1,list2,list3=start_content_request()
    print(list3)

    
