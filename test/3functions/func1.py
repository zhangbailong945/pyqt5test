'''
 函数
 1、函数代码以def关键词开头，后接函数标识符名称和圆括号
 2、任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于自定义参数
 3、函数的第一行语句可以选择性地使用文档字符串
 4、函数内容以冒号开始，并且缩进
 5、return statements 结束函数，选择性地返回一个值给调用方。不带放回值相当于返回None

'''

def printStr(n):
    print(str(n))
    return

printStr(11)


#函数传值
#1、传不可变对象实例,string,numbers,tuple
def changeInt(a):
    a=10

b=2
changeInt(b)
print(b)


#传可变参数
def changeme(mylist):
    mylist.append([1,2,3,4,5])
    print('函数内取值：',mylist)
    return

a=[10,20,30]
changeme(a)
print('函数外取值：',a)

#参数的种类
#1.必须参数
#2.关键字参数
#3.默认参数
#4.不定长参数

#1.必须参数
def func1(str):
    pass

#2.关键字参数
def func2(name,age):
    pass

#3.默认参数
def func3(name,age=25):
    pass

#4.不定长元组参数*
def func4(name,age=25,*args):
    pass

#5.不定参数字典**
def func5(name,age=25,*args,**kwargs):
    pass


#匿名函数
'''
python使用lambda来创建匿名函数
1.lambda只是一个表达式
2.lambda有自己的命令控件，不能访问全局命名空间的参数


'''

#return 返回值


#变量的作用域
#1.L(local) 局部作用域
#2.E(Enclosing) 闭包函数外的函数中
#3.G(global) 全局函数
#4.B(Built-in) 内建函数

x=int(2.9) #内建作用域
g_count=0 #全局作用域

def outer():
    o_ounter=1 #闭包函数
    def inner():
        i_count=2 #局部作用域


#global和nonlocal 关键字
#如果内部变量为全局变量，用global
#如果修改嵌套作用域中的变量则需要nonlocal关键字