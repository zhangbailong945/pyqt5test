#代理模式 Proxy

'''
为其他对象提供一种代理以控制这个对象的访问
适用性：
在需要比较通用复杂的对象指针代替简单的指针的时候，使用Proxy模式。
1.远程代理 为一个对象在不同的地址空间提供局部代表
2.虚代理 根据需要创建开销很大的对象
3.保护代理 控制对原始对象的访问。
4.智能指引 取代了简单的指针，它在访问对象时只需一些附加操作。

组成：
抽象角色：通过接口或抽象类声明真实角色的业务方法。
代理角色：实现抽象角色，是真实角色的代理，通过真实角色的业务逻辑方法
来实现抽象方法，并可以附件自己的操作。
真实角色：实现抽象角色，定义真实角色所要实现的业务逻辑，供代理角色调用。
'''


class Jurisdiction:
    '''权限类'''

    def level1(self):
        print('权限等级1')
    
    def level3(self):
        print('权限等级3')
    
    def level2(self):
        print('权限等级2')
    
    def level4(self):
        print('权限等级4')


class Proxy:

    def __init__(self,name):
        self.user=name
        self._jurisdiction=Jurisdiction()
    
    def level(self):
        if self.user=='a':
            return self._jurisdiction.level1()
        elif self.user=='b':
            return self._jurisdiction.level2()
        elif self.user=='c':
            return self._jurisdiction.level3()
        elif self.user=='d':
            return self._jurisdiction.level4()
        else:
            print('你咩有权限。')


if __name__ == "__main__":
    test = Proxy('a')
    test.level()
    test.user = 'b'
    test.level()
    test.user = 'c'
    test.level()
    test.user = 'd'
    test.level()
    test.user = 'e'
    test.level()
    