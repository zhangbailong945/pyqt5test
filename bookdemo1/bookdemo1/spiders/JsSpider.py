import scrapy

class JsSpider(scrapy.Spider):

    name='js'
    allowed_domains=['quotes.toscrape.com']
    start_urls=['http://quotes.toscrape.com/js/']

    def parse(self,response):
        tags=response.css('div.tag::text').extract()
        print(tags)
    