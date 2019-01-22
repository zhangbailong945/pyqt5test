import requests
from html.parser import HTMLParser



class DouBanClient(object):

    def __init__(self):
        object.__init__(self)
        self.headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Origin':'http://www.douban.com',
        }
        self.session=requests.session() #创建一个session
        self.session.headers.update(self.headers)
    
    def login(self,username,password,source="index_nav",redir='http://www.douban.com/',login='登录'):
        url='https://www.douban.com/accounts/login'
        response=self.session.get(url)
        (captcha_id,captcha_url)=_get_captcha(response.content.decode('utf-8'))
        if captcha_id:
            print('验证码url:%s'%captcha_url)
            captcha_solution=input('please input solution for captcha[%s]:'% captcha_url)
        
        data={
            'form_email':username,
            'form_password':password,
            'source':source,
            'redir':redir,
            'login':login
        }

        headers={
            'referer':'https://www.douban.com/accounts/login?source=main',
            'host':'accounts.douban.com'
        }

        if captcha_id:
            data['captcha-id']=captcha_id
            data['captcha-solution']=captcha_solution
        self.session.post(url,data=data,headers=headers)
        print(self.session.cookies.items())
    

    
#这个函数解析登录验证码
def _get_captcha(content):

    class CaptchaParser(HTMLParser):

        def __init__(self):
            HTMLParser.__init__(self)
            self.captcha_id=None
            self.captcha_url=None
        
        
        def handle_starttag(self,tag,attrs):
            if tag=='img' and _attr(attrs,'id')=='captcha_image' and _attr(attrs,'class')=='captcha_image':
                self.captcha_url=_attr(attrs,'src')
                print('self.captcha_url:%s'% self.captcha_url)
            if tag=='input' and _attr(attrs,'type')=='hidden' and _attr(attrs,'name')=='captcha-id':
                self.captcha_id=_attr(attrs,'value')
                print('self.captcha_id:%s'% self.captcha_id)
    p=CaptchaParser()
    p.feed(content)
    return p.captcha_id,p.captcha_url

def _get_ck(content):

    class CKParser(HTMLParser):

        def __init__(self):
            HTMLParser.__init__(self)
        
        def handle_starttag(self,tag,attrs):
            if tag=='input' and _attr(attrs,'type')=='hidden' and _attr(attrs,'name')=='ck':
                self.ck=_attr(attrs,'value')
                
    p=CKParser()
    p.feed(content)
    return p.ck

    
def get_proxy(self):
    return requests.get("http://123.207.35.36:5010/get/").content


def _attr(attrs,attrname):
    for attr in attrs:
        if attr[0]==attrname:
            return attr[1]
    return None


if __name__=='__main__':
    c=DouBanClient()
    c.login('15014927018','123long456')