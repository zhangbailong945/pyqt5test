
import scrapy

from ..items import GarlandtoolsItem
import time

class Spider3(scrapy.Spider):

    name='en3data'
    allowed_domains=['www.garlandtools.org']
    start_urls=[]

    for i in range(46,16000):
        url='http://www.garlandtools.org/db/doc/item/en/3/{0}.json'.format(str(i))
        start_urls.append(url)

    custom_settings={
        'REQUEST_HEADERS':{
            'Accept':'text/html,application:xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language':'application/json; charset=utf-8',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        },
        "RANDOM_DELAY":2,
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        item=GarlandtoolsItem()
        item['file_urls']=[]
        item['file_urls'].append(response.url)
        yield item

