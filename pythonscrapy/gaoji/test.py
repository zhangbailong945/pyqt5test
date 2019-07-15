from html.parser import HTMLParser
from urllib.request import Request,urlopen
from urllib import error

import re,os

headers={
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Authorization':' eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTI1MzkwNTEsImlhdCI6MTU1MjQ1MjY1MSwiZGF0YSI6eyJ1c2VybmFtZSI6ImFkbWluIn19.PcFzzIjT7IUi6XiHMagKWZ923Q-gqm8A1DyIsvvx9Pw'
    }

class MyHtmlParser(HTMLParser):
    '''
    爬取器
    '''

    def __init__(self,*args,**kwargs):
        super(MyHtmlParser,self).__init__(*args,**kwargs)
        self.in_list=False
        self.in_th=False
        self.in_td=False


    @classmethod 
    def _attr(cls,attrs,attrname):
        '''
        从属性列表中获取指定的值
        '''
        for attr in attrs:
            if attr[0]==attrname:
                return attr[1]
        return None
    
    
    def handle_starttag(self,tag,attrs):
        '''
        处理开始标签 例如：<div>
        '''
        
        if tag=='div' and self._attr(attrs,'id')=='list':
            self.in_list=True
        
        if tag=='th':
            self.in_th=True
        
        if tag=='td':
            self.in_td=True

    
    def handle_endtag(self,tag):
        '''
        处理结束标签 例如:</div>
        '''
        if tag=='div':
            self.in_list=False
        
        if tag=='th':
            self.in_th=False
        
        if tag=='td':
            self.in_td=False
        

    
    def handle_data(self,data):
        '''
        处理标签中的文本 例如:<div>my data</div>
        '''
        if self.in_list:
            print(data)
        
        if self.in_th:
            print(data)
        
        if self.in_td:
            print(data)
    

if __name__ == "__main__":
    #爬取器
    parser=MyHtmlParser()
    url='https://tools.guardui.net/lifetools/truckplate.html'
    try:
        req=Request(url,headers=headers)
        response=urlopen(req)
        parser.feed(response.read().decode('utf-8'))
        response.close()
    except error.HTTPError as he:
        print(he)
    except error.URLError as ue:
        print(ue)
    except Exception as e:
        print(e)


    
    

