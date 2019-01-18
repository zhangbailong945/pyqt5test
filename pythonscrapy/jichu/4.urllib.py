
'''
urllib.urlopen()
打开一个远程的http连接,然后对这个参数进行读取
Url:Scheme(http:/file:)指定远程的服务器读取也支持本地
data:如果有，为POST方法，对服务器POST数据，数据格式必须是
application/X-www-form-urlencoded

返回类文件句柄
read(size) size=-1/None 读字节
readline() 读一行
readlines() 所有的行都会读出来，它返回的是一个链表
close() 把这个文件关闭掉
getcode() 返回http请求应答码，2xx就是正确的应答码

urllib
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
'__name__', '__package__', '__path__', '__spec__', 'error', 'parse',
 'request', 'response']

urllib3

['HTTPConnectionPool', 'HTTPResponse', 'HTTPSConnectionPool', 
'PoolManager', 'ProxyManager', 'Retry', 'Timeout', '__all__', 
'__author__', '__builtins__', '__cached__', '__doc__', 
'__file__', '__license__', '__loader__', '__name__', 
'__package__', '__path__', '__spec__', '__version__',
 '_collections', 'absolute_import', 'add_stderr_logger', 
 'connection', 'connection_from_url', 'connectionpool', 
 'disable_warnings', 'encode_multipart_formdata',
  'exceptions', 'fields', 'filepost', 'get_host', 
  'logging', 'make_headers', 'packages', 
  'poolmanager', 'proxy_from_url', 
  'request', 'response', 'util', 
  'warnings']

'''



import urllib,urllib3

from urllib.request import urlopen

def demo1():
    s=urlopen('http://loachblog.com')
    for i in range(10):
        print('第%d行:%s'%(i+1,s.readline()))

def demo2():
    s=urlopen('http://loachblog.com')
    lines=s.readlines()
    print_list(lines)

def print_list(list):
    for i in list:
        print(i)


def demo3():
    s=urlopen('http://loachblog.com/')
    print(s.getcode())

if __name__=='__main__':
    demo3()
