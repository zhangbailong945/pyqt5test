'''

标准库

'''

#1.文件管理任务
import shutil


#文件通配符,提供一个函数用于从目录通配符搜索中生成文件列表
import glob


#命令行参数
import sys
print(sys.argv)

#字符串匹配re
import re


#数学
import math


#访问互联网
import urllib


#日期和时间
import datetime

#数据压缩
import zlib,gzip,bz2,zipfile,tarfile


#性能度量
from timeit import Timer

print(Timer('t=a;a=b;b=t;','a=1;b=2').timeit())
print(Timer('a,b=b,a','a=1;b=2').timeit())

#测试模块
import doctest
'''
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # 自动验证嵌入测试
'''

import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)

unittest.main() # Calling from the command line invokes all tests