'''
单例
一个类只能实例化一次
'''


class Singleton(object):
    '''
    单例模式
    '''

    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'_instance'):
            obj=super(Singleton,cls).__new__(cls,*args,**kwargs)
            cls._instance=obj
        return cls._instance

'''
单例模式共享属性
'''

class Singleton2(object):

    _state={}

    def __new__(cls,*args,**kwargs):
        obj=super(Singleton2,cls).__new__(cls,*args,**kwargs)
        obj.__dict__=cls._state
        return obj


'''
单例模式 装饰器
'''

def singleton(cls,*args,**kwargs):

    instance={}
    def get_instance(*args,**kwargs):
        if cls not in instance:
            instance[cls]=cls(*args,**kwargs)
        return instance[cls]
    return get_instance
    

@singleton
class C(object):
    pass

class A(Singleton):
    name='张三'

class B(Singleton2):
    name='李四'

    def talk(self):
        print('说话')

if __name__ == "__main__":
    obj1=A()
    obj2=A()
    print(obj1.name)
    print(obj2.name)

    obj3=B()
    obj4=B()
    print(obj3.__dict__)
    print(B.__dict__)

    cobj1=C()
    cobj2=C()
    print(cobj1)
    print(cobj2)





