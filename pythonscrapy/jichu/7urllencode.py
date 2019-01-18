'''
request.urlencode
1.把字典数据转换成URL编码
2.用途
a.对URL参数进行编码
b.对Post上去的form数据进行编码



'''

import urllib
from urllib.request import urlopen,urlparse
from urllib.parse import urlencode,parse_qs

def url_encode():
    params={
        'score':100,
        'name':'爬虫基础',
        'comment':'楼主牛逼！'
    }
    qs=urlencode(params)
    print(qs)

def url_decode(url):
    result=urlparse(url)
    print(result)
    return parse_qs(url)

if __name__=='__main__':
    url='https://www.baidu.com/s?wd=url%20%E7%BC%96%E7%A0%81%E8%A7%84%E5%88%99&rsv_spt=1&rsv_iqid=0x928cf1380000a436&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=16&rsv_sug1=15&rsv_t=1699JwFmhB8a5kfErU33lHHt8KRbsMzqMwqlJ00%2F9fusUM%2Bmx3gc8GLs5In0kVh7s3zU&rsv_sug2=0&inputT=5565&rsv_sug4=6174'
    #url_encode()
    print(url_decode(url))