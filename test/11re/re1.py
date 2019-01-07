'''
正则表达式是一个特殊的字
它能帮助你方便的检查一个字符串是否与某种模式匹配
compile函数根据一个模式字符串和可选的标志参数
生成一个正则表达式对象，该对象拥有一系列方法用于正则表达式匹配和替换
re模块也提供了与这些方法功能完全一致的函数，这些函数使用一个模式字符
串作为他们的第一个参数

'''


#re.match(pattern,string,flags=0)
#re.match尝试从字符串的起始位置匹配一个模式，如果
#不是起始位子匹配成功的话，match()就返回none
#pattern 匹配的正则表达式
#string 要匹配的字符串
#flags 标志位，用于控制正则表达式的匹配方式
'''
re.I 使用匹配对大小写不敏感
re.L 本地化识别匹配
re.M 多行匹配，影响^和$
re.S 使.匹配包括换行在内的字符
re.U 根据Unicode字符集解析字符。这个标志影响\w,\W,\b,\B
re.X 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解

'''
#匹配成功re.match方法返回一个匹配的对象，否则返回None

#group(num)和groups()
'''
group(num=0)匹配的整个表达式的字符串,group()可以一次输入多个组号，在这种情况下
它将返回一个包含那些组所对应值的元组
groups() 返回一个包含所有小组字符串的元组，从1到所含的小组号
'''


import re

print(re.match('www','www.loachblog.com').span()) #起始位置匹配
print(re.match('com','www.loachblog.com')) #不在起始位置



text1="zhang bai long is god!"

matchobj=re.match(r'(.*) bai (.*?) .*',text1,re.M|re.I)

if matchobj:
    print('matchobj.group()',matchobj.group())
    print('matchobj.group(1)',matchobj.group(1))
    print('matchobj.group(2)',matchobj.group(2))
else:
    print('No MATCH!')



#re.search() 扫描整个字符串并返回第一个成功的匹配

#re.match() 与 re.search()的区别
'''
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，
则匹配失败，函数返回None,而re.search匹配整个字符串，直到找到一个匹配。

'''

text2="Cats ar smarter than dogs"
matchobj2=re.match(r'dogs',text2,re.M|re.I)

if matchobj2:
    print("match-->matchobj2.goup():",matchobj2.group())
else:
    print("No Match!")

matchobj3=re.search(r'dogs',text2,re.M|re.I)

if matchobj3:
    print('search-->matchobj.group():',matchobj3.group())
else:
    print("No match!")

#检索和替换
#re模块提供了re.sub用于替换字符串中的匹配项
#re.sub(pattern,repl,sring,count=0)
#pattern:正则中的模式字符串
#repl:替换的字符串，也可为一个函数
#string:要被查找替换的原始字符串
#count：模式匹配后替换的最大次数，默认0匹配全部


phone="2004-987-447 # 这是一个号码"

#删除注释
num=re.sub(r'#.*$',"",phone)
print("phone number:",num)

#移除非数字内容
num=re.sub(r'\D',"",phone)
print('phone number:',num)


#compile函数
'''
compile函数用于编译正则表达式，生成一个正则表达式（Pattern）对象，
提供match()和search()这两个函数使用

'''
pattern1=re.compile(r'\d+')

m=pattern1.match('one123two')
print(m)


#findall
'''
在字符串中找到正则表达式所匹配的所有字符串，并返回一个列表，如果没有匹配，返回空列表。
match和search是匹配一次，findall匹配所有
'''

pattern = re.compile(r'\d+')   # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
 
print(result1)
print(result2)


#re.finditer
'''
在字符串找到正则表大会所匹配的素有字符串，
并把他们当做迭代器返回
'''

it = re.finditer(r"\d+","12a32bc43jf3") 
for match in it: 
    print (match.group() )


#re.split 
'''
split方法安装能够 匹配的字符串将字符串分隔后返回列
'''