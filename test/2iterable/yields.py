'''

#生成器
1.使用yield的函数被称为生成器
2.在调用生成器运行的过程中，每次遇到yield时函数会暂停保存当前所有的运行信息，
返回yield的值，并在下一次next()方法时从当前位置继续运行。
3.调用生成器函数，返回的是一个迭代器对象


'''

import sys

def fib(n):
    a,b,counter=0,1,0
    while True:
        if (counter>n):
            return
        yield a
        a,b=b,a+b
        counter+=1

f=fib(10)
while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit() 