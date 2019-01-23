
import requests,json,os

from html.parser import HTMLParser


'''
爬虫豆瓣热映电影并下载电影图片

'''

class MyHtmlParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.movies=[]
        self.in_movies=False

    def handle_starttag(self,tag,attrs):

        def _attr(attrlist,attrname):
            for attr in attrlist:
                if attr[0]==attrname:
                    return attr[1]
            return None

        
        if tag=='li' and _attr(attrs,'data-title') and _attr(attrs,'data-category')=='nowplaying':
            movie={}
            movie['title']=_attr(attrs,'data-title')
            movie['score']=_attr(attrs,'data-score')
            movie['director']=_attr(attrs,'data-director')
            movie['actors']=_attr(attrs,'data-actors')
            self.movies.append(movie)
            print('===电影名称:%(title)s====评分:%(score)s====导演:%(director)s====演员阵容:%(actors)s'% movie)
            self.in_movies = True   #表示我们已经解析到了这个电影
        
        if tag=='img' and self.in_movies:
            self.in_movies=False #解析电影的图片
            src=_attr(attrs,'src')
            movie=self.movies[len(self.movies)-1]
            movie['cover-url']=src
            print(movie)
            _download_poster_image(movie)
    

def _download_poster_image(movie):
    url=movie['cover-url']
    response=requests.get(url)
    fname=url.split('/')[-1]
    print(fname)
    fname=os.path.dirname(__file__)+"/"+fname
    print(fname)
    with open(fname,'wb') as f:
        f.write(response.content)
    movie['cover-path']=fname

    

#热映电影
url='https://movie.douban.com/cinema/nowplaying/zhuhai/'
headers={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip',
    'Accept-Language':'zh-CN,zh:q=0.9',
    'Referer':'www.douban.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Host':'movie.douban.com'
}

response=requests.get(url,headers=headers)

def scrapy_Douban_NowPlaying():
    if response.status_code==200:
        parser=MyHtmlParser()
        parser.feed(response.content.decode('utf-8'))
        return parser.movies


if __name__=='__main__':
    list=scrapy_Douban_NowPlaying()
    print(json.dumps(list,sort_keys=True,indent=4,separators=(',',':')))
