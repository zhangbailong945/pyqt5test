#适配器
'''
意图：
将一个类的接口转换成客户希望的另外一个接口。
Adapter模式使得原本由于接口不兼容而不能一起工作的类可以一起工作。
适用性：
使用一个存在的类，而它的接口不符合你的需求
你想创建一个复用的类，该可以与其他不相关的类或不可预见的类协同工作。
你想要使用已经存在的子类，但是不可能对每一个都进行子类化以匹配他们的接口。对象
适配器可以适配它的父类接口。

适配器就是万能接口，各种类可以通过这个接口然后被调用，打到万能转换的效果。

核心：
创建一个适配器类，通过__dict__将需要转换的类的方法注册到适配器，
复写__getattr__使其在适配器函数查无方法的时候，执行getattr魔法方法。


'''

class A:

    def a(self):
        print('我是A类a方法')

class B:

    def b(self):
        print('我是B类b方法')

class C:

    def c(self):
        print('我是C类c方法')


class Adapter:
    '''
    适配器
    '''

    def __init__(self,classname,method):
        self.classname=classname
        self.__dict__.update(method)
    
    def __getattr__(self,attr):
        return getattr(self.classname,attr)

def test():
    objects=[]
    AA=A()
    objects.append(Adapter(AA,dict(test=AA.a)))
    BB=B()
    objects.append(Adapter(BB,dict(test=BB.b)))
    CC=C()
    objects.append(Adapter(CC,dict(test=CC.c)))
    for obj in objects:
        obj.test()

if __name__ == "__main__":
    test()
