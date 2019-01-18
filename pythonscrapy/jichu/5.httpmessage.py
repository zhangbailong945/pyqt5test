'''
HTTPMessage
info():返回httplib.HTTPMessage实例
通过httplib.HTTPMessage：可以看到更多应答信息
1.Headers头信息
2.gettype() 获取它的媒体类型
3.getheader() /getheaders() 可以从http头里获取到的头字段
4.Items() /keys() /values() 打印出所有的头出来



['__bytes__', '__class__', '__contains__', '__delattr__', 
'__delitem__', '__dict__', '__dir__', '__doc__',
 '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__gt__', '__hash__',
'__init__', '__init_subclass__', '__iter__', 
'__le__', '__len__', '__lt__', '__module__',
 '__ne__', '__new__', '__reduce__', 
 '__reduce_ex__', '__repr__', '__setattr__', 
 '__setitem__', '__sizeof__',
'__str__', '__subclasshook__', '__weakref__', 
'_charset', '_default_type', '_get_params_preserve',
'_headers', '_payload', '_unixfrom', 'add_header',
 'as_bytes', 'as_string', 'attach', 'defects', 
 'del_param', 'epilogue', 'get', 'get_all', 
 'get_boundary', 'get_charset', 'get_charsets', 
 'get_content_charset', 'get_content_disposition',
  'get_content_maintype', 'get_content_subtype', 
  'get_content_type', 'get_default_type', 'get_filename',
   'get_param', 'get_params', 'get_payload', 
   'get_unixfrom', 'getallmatchingheaders', 'is_multipart', 
   'items', 'keys', 'policy', 'preamble', 'raw_items',
    'replace_header', 'set_boundary', 'set_charset', 
    'set_default_type', 'set_param', 'set_payload', 
    'set_raw', 
'set_type', 'set_unixfrom', 'values', 'walk']

'''

import urllib
from urllib.request import urlopen

def print_list(list):
    for i in list:
        print(i)

def demo1():
    s=urlopen('http://loachblog.com')
    msg=s.info() #获取HTTPMessage对象
    print_list(msg.items())

def demo2():
    s=urlopen('http://loachblog.com')
    msg=s.info()
    print(msg.get('Content-Type'))


if __name__=='__main__':
    demo2()