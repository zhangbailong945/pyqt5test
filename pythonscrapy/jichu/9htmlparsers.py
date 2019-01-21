from html.parser import HTMLParser

from htmlbody import Html_Body
from urllib.request import Request,urlopen

class MyHTMLParser(HTMLParser):

    def handle_starttag(self,tag,attrs):
        print('%s'%tag)
    
    def handle_endtag(self,tag):
        print('%s'%tag)
    
    def handle_startendtag(self,tag,attrs):
        print('%s'% tag)
    
    def handle_data(self,data):
        print('data:%s'%data)
    
    def handle_comment(self,data):
        print('comment:%s'%data)
    
    def handle_entityref(self,name):
        print('&#%s'% name)
    
    def handle_charref(self,name):
        print('&#%s'% name)


if __name__=='__main__':
    url='http://www.baidu.com'
    headers={
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    }
    req=Request(url,headers=headers)
    response=urlopen(req)
    parser=MyHTMLParser()
    parser.feed(response.read().decode('utf-8'))
    response.close()