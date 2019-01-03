'''
1.pyton中单引号和双引号使用完全相同
2.使用三引号，阔以指定一个多行字符串
3.转义符'\'，如果不需要转义则需要在字符串前面加上r
4.字符串可以用+运算符连在一起，用*运算符重复
5.python 中的字符串有两种索引方式，从左到右以0开始，反之-1开始
6.python的字符串不能改变
7.python 没有单独字符类型，一个字符就是长度为1的字符串
8.字符串截取 变量[头下标:尾下标]
9.空行,函数之间或类的方法之前用空行分隔，表示新的一段代码的开始
10. 等待用户输入input()
11.同一行显示多条语句，用分号;隔开，多个语句构成代码组
12.print默认是换行输出的，要想不换行，则需要在变量末尾加上end=""
13.from...import 导入整个模块import module,导入模块某个函数from module import func
14.


'''


str1='zhangbailong'
str2="""这是一个段落，
可以由多行组成
"""

print(str1)
print(str1[0:-1])
print(str1[0:])
print(str1[5:])
print(str1*2,end="")
print(str1+str2,end="")
print(str1[-1])
input('\n\n 按下 Enter 键退出。')