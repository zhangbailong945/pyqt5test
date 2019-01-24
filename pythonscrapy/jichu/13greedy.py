'''

greedy 贪婪模式
* 是贪婪模式
? 是不贪婪


'''
import re
def re_pattern():
    str1='20.55<h1>This is title!</1>'
    r=re.compile(r'''
    \d+ #正数部分
    \.? #小数点
    \d* #小数点后面的数字，可选
    ''',re.VERBOSE)
    print(re.search(r,str1).group())



if __name__=='__main__':
    re_pattern()