#迭代器Iterator
'''
迭代模式：
对外提供一个接口，实现顺序访问聚合数据，但是不显示该数据的内部机制。
生成器：
对于一个数据集合，生成器并不记住每个元素值，但在循环中记录元素位置并根据元素
生成规则推算出数值，这种边循环边计算的形式是生成器。
迭代器：
是一种访问集合的方式，记住遍历位置，从第一个元素开始访问，
知道最后一个元素，并且只能前进不能后退。
可迭代对象：
list,set,str,dict通过for遍历的类型是可迭代对象。
注意：
凡是通过next()访问的对象都是迭代类型。也就是说生成器就是迭代器的一种；凡是通过
for循环遍历的都是可迭代对象，可迭代对象可以通过iter()转换为迭代器。

'''

def fib(n):
    x=0
    y=1
    i=1
    while(True):
        yield y
        if i==n:
            break
        x,y=y,x+y
        i+=1

'''
if __name__ == "__main__":
    test=fib(7)
    print(next(test))
    print(next(test))
    print(next(test))
    print(next(test))
    print(next(test))
    print(next(test))
    print(next(test))
    print(next(test))
'''


'''
生成器中几个关键词：
yield、yield form,send、next()、__next__()具体作用
'''

def test():
    a=1
    while True:
        yield a
        a=a+a

def test1():
    #yield from是创建一个嵌套的生成器，form后面跟一个生成器，每次执行
    #yield from 后会先把内层的生成器执行完。

    yield from test()


'''
if __name__ == "__main__":
    fn=test()
    #通过next访问内部元素
    print(next(fn))
    #通过__next__()访问内部元素，作用同上
    print(fn.__next__())
    #send有next的作用，同时向生成器内部的yield左边等式赋值 
    fn.send(4)
    fn1=test1()
    print(fn.__next__())
'''

'''
可迭代对象
next() iter() for
'''
a=(i for i in range(50))
b=[1,2,3,4,5,6]
c='string'


if __name__ == "__main__":
    print(next(a))
    #print(next(b))
    #print(next(c))
    d=iter(c)
    print(next(d))

    