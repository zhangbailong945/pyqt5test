
import scrapy,os

from scrapy.linkextractors import LinkExtractor


class BiqugeSpider(scrapy.Spider):

    name='biquge'
    allowed_domains=['www.biquge5200.cc']
    start_urls=['https://www.biquge5200.cc/']

    custom_settings={
        'DEFAULT_REQUEST_HEADERS':{
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Accept:':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9',

        },
        "RANDOM_DELAY":2,
    }

    #提取分类列表链接
    def parse(self,response):
        title=response.css('title::text').extract_first()
        print(title)
        #根据css提取分类列表
        le=LinkExtractor(restrict_css='div.nav ul li a[href]')
        links=le.extract_links(response)
        print(links[2].url)
        #for link in links[2:]:
        yield scrapy.Request(links[2].url,callback=self.parse_category_book,dont_filter=False)

    
    #提取分类页面好看的书的列表
    def parse_category_book(self,response):
        le=LinkExtractor(restrict_css='#newscontent>div.r>ul>li a[href]')
        links=le.extract_links(response)
        #for link in links:
        yield scrapy.Request(links[0].url,callback=self.parse_category_book_details,dont_filter=False)

    
    #提取分类中书的详情
    def parse_category_book_details(self,response):
        sel=response.css('div#maininfo')
        novel_title=sel.css('#info>h1::text').extract_first()
        #print(novel_title)
        novel_author=sel.css('#info>p:nth-child(2)').re_first('作.*?者：(\w+)')
        #print(novel_author)
        novel_last_update_time=sel.css('#info>p:nth-child(4)').re_first('最后更新：(\d{4}-\d{2}-\d{2})')
        #print(novel_last_update_time)
        novel_last_update_content=response.css('#intro>p::text').extract_first()
        #print(novel_last_update_content)
        #小说的章节链接列表
        le=LinkExtractor(restrict_css='div.box_con>div#list>dl>dd>a[href]')
        links=le.extract_links(response)
        #print(links[9].text)

        for link in links[9:]:
            request=scrapy.Request(link.url,callback=self.parse_book_chapter_content,dont_filter=False)
            request.meta['novel_title']=novel_title
            request.meta['novel_chapter_name']=link.text
            yield request

    
    def parse_book_chapter_content(self,response):
        plist=response.css('div#content>p::text')
        content=''
        for p in plist:
            content+=p.extract()
        novel_title=response.meta['novel_title']
        novel_chapter_name=response.meta['novel_chapter_name']
        new_line='\r\r\n\n'
        content=new_line+novel_chapter_name+new_line+content
        with open(novel_title+'.txt','a+',encoding='utf-8') as f:
            f.write(content)


    

    

