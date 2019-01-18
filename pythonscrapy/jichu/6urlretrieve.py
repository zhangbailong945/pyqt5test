'''
urllib.urlretrieve(提供了一个更便捷的功能，就是直接把远程的文件，下载到本地)
1.url:远程地址
2.filename:要保存到本地的文件
3.reporthook:下载状态报告
4.data:POST的application/x-www-form-urlencoded格式的数据
5.返回(filename,HTTPMessage)

reporthook:看怎么来监控这个当前下载的进度
1.参数1：当前传输的块数
2.参数2:块大小
3.参数3:数据总大小
4.需要注意：content-length不是必须的
实际上参数1，参数2相乘就是当前下载多少个字节，和参数3一除就知道这个百分比


'''

import urllib

from urllib.request import urlopen,urlretrieve

def print_list(list):
    for i in list:
        print(i)

def retrieve():
    fname,msg=urlretrieve('http://loachblog.com','index.html',reporthook=process)
    print(fname)
    print(msg.items())

def process(blk,blk_size,total_size):
    print('%d/%d-%.02f%%'%(blk*blk_size,total_size,(float)(blk*blk_size)*100/total_size))

if __name__=='__main__':
    retrieve()