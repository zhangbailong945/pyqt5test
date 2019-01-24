import requests,re

from html.parser import HTMLParser


#唐诗三百首爬取类
class TangShiParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.in_content_list=False
        self.in_h2=False
        self.chapter=[] #章节
        self.chapter_tangshi=[] #章节里面的唐诗
    
    #处理开始标签
    def handle_starttag(self,tag,attrs):

        #解析标签属性，通过标签属性名获取对应标签属性里面的内容
        def _attr(attrlist,attrname):
            for attr in attrlist:
                if attr[0]==attrname:
                    return attr[1]
            return None
        #爬取规则
        if tag=='div' and _attr(attrs,'class')=='content-list clearfix':
            self.in_content_list=True
        
        if tag=='h2':
            self.in_h2=True
        
    def handle_endtag(self,tag):
        if tag=='div':
            self.in_content_list=False
        
        if tag=='h2':
            self.in_h2=False
        
    #处理数据
    def handle_data(self,data):
        if self.in_h2:
            self.chapter.append(data)





def start_request():
    url='http://www.300tangshi.com/'
    headers={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Host':'www.300tangshi.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    response=requests.get(url,headers=headers)
    #返回页面内容
    parserContent=response.content.decode('gbk')
    tsParser=TangShiParser()
    tsParser.feed(parserContent)
    return tsParser.chapter


if __name__=='__main__':
    list=start_request()[1:]
    print(list)

        
