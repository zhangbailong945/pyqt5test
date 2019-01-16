
import scrapy


class LoginSpider(scrapy.Spider):
    name='login'
    allowed_domains=['example.webscraping.com']
    start_urls=['http://example.webscraping.com/places/default/user/profile']

    def parse(self,response):
        keys=response.css('table label::text').re('(.+):')
        values=response.css('table td.w2p_fw::text').extract()
        dict1=dict(zip(keys,values))
        for k,v in dict1.items():
            print('k=%s,v=%s'%(k,v))
        yield dict(zip(keys,values))
    
    #登录页面
    login_url='http://example.webscraping.com/places/default/user/login?_next=/places/default/index'

    def start_requests(self):
        print(11111)
        yield scrapy.Request(self.login_url,callback=self.Login)
    
    def Login(self,response):
        fd={
            'email':'1207549344@qq.com',
            'password':'1234567890',
        }
        print(3333)
        yield scrapy.FormRequest.from_response(response,formdata=fd,callback=self.parse_login)
    
    def parse_login(self,response):
        #登录成功
        if 'bailong' in response.text:
            print(44444)
            yield from super().start_requests()



