import requests,re

from html.parser import HTMLParser


#唐诗三百首爬取类
class TangShiParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.in_content_list=False
        self.in_h2=False
        self.in_a=False
        self.in_ul=False
        self.in_li=False
        self.chapter=[] #章节
        self.chapter_tangshi=[] #章节里面的唐诗
        self.pattern=re.compile(r'''
        ^(.*)$ #匹配诗名
        ''',re.VERBOSE)
    
    #处理开始标签
    def handle_starttag(self,tag,attrs):
        #爬取规则
        if tag=='div' and _attr(attrs,'class')=='content-list clearfix':
            self.in_content_list=True
        
        if tag=='h2':
            self.in_h2=True

        if tag=='ul' and _attr(attrs,'class')=='clearfix':
            self.in_ul=True
            self.in_a=True

        if tag=='li' and _attr(attrs,'class')=='col-md-3':
            self.in_li=True

        if tag=='a' and self.in_li:
            ts_url=_attr(attrs,'href')
            ts_title=_attr(attrs,'title')
            tuple1=(ts_title,ts_url)
            self.chapter_tangshi.append(tuple1)

        
    def handle_endtag(self,tag):
        if tag=='div':
            self.in_content_list=False
        
        if tag=='h2':
            self.in_h2=False
        
        if tag=='ul':
            self.in_a=False
            self.in_ul=False
            self.in_li=False

        
    #处理数据
    def handle_data(self,data):
        if self.in_h2:
            self.chapter.append(data)

        '''
        if self.in_ul and self.in_a:
            m=self.pattern.match(data)
            if m:
                self.chapter_tangshi.append(m.group(1))
        '''

class TangShiContentParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.in_article_div=False
        self.in_br=False
        self.in_p=False
        self.in_next_div=False
        self.tsName=None
        self.tangshi_ju=[]
        self.tangshi_other=[]
        self.pattern=re.compile(r'''
        ^(.*)$ #匹配诗名
        ''',re.VERBOSE)
    
    def handle_starttag(self,tag,attrs):

        if tag=='div' and _attr(attrs,'class')=='article':
            self.in_article_div=True
        
        if tag=='br':
            self.in_br=True
        
        if tag=='p':
            self.in_p=True
        
        if tag=='div' and _attr(attrs,'class')=='bottomads':
            self.in_next_div=True
    

    def handle_endtag(self,tag):
        
        if tag=='div':
            self.in_article_div=False
            self.in_br=False
            self.in_p=False
        
    def handle_data(self,data):
        if self.in_br and not self.in_p:
            self.tangshi_ju.append(data)
        
        if self.in_p and self.in_br:
            self.tangshi_other.append(data)

    




    
    #解析标签属性，通过标签属性名获取对应标签属性里面的内容
def _attr(attrlist,attrname):
    for attr in attrlist:
        if attr[0]==attrname:
            return attr[1]
    return None


headers={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Host':'www.300tangshi.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}


def start_request():
    url='http://www.300tangshi.com/'

    response=requests.get(url,headers=headers)
    #返回页面内容
    parserContent=response.content.decode('gbk')
    tsParser=TangShiParser()
    tsParser.feed(parserContent)
    return tsParser.chapter,tsParser.chapter_tangshi

def parser_Content(ts):
    url=ts[1]
    response=requests.get(url,headers=headers)
    parserContent=TangShiContentParser()
    parserContent.tsName=ts[0]
    parserContent.feed(response.content.decode('gbk'))
    tangshi={}
    tangshi['name']=parserContent.tsName
    tangshi['ju']=parserContent.tangshi_ju
    tangshi['other']=parserContent.tangshi_other
    return tangshi





if __name__=='__main__':
    list1,list2=start_request()
    tangshi=parser_Content(list2[0])
    print(tangshi)
    '''
    for li in list2:
        title,url=li
        print('title:%s,url:%s'%(title,url))
    '''

        
