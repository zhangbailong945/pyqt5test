from html.parser import HTMLParser

from htmlbody import Html_Body
from urllib.request import Request,urlopen

class MyHTMLParser(HTMLParser):

    
        

    def __init__(self):
        HTMLParser.__init__(self)
        self.readingtitle=0
        self.title=''
        self.htmls=[]

    def handle_starttag(self,tag,attrs):

        for attr in attrs:
            print(attr)
        if tag=='title':
            self.readingtitle=1
    
    def handle_endtag(self,tag):
        if tag=='title':
            self.readingtitle=0
    
    def handle_startendtag(self,tag,attrs):
        pass
        
    
    def handle_data(self,data):
        if self.readingtitle:
            self.title+=data
    
    def handle_comment(self,data):
        pass
    
    def handle_entityref(self,name):
        pass
    
    def handle_charref(self,name):
        pass
    
    def getTitle(self):
        return self.title


if __name__=='__main__':
    url='https://www.baidu.com'
    headers={
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    }
    req=Request(url,headers=headers)
    response=urlopen(req)
    parser=MyHTMLParser()
    parser.feed(response.read().decode('utf-8'))
    response.close()
    print('title:%s'%(parser.getTitle()))
