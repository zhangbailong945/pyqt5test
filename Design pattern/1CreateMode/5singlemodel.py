#单例模式
'''
单例：顾名思义是一个实例，即在一个项目之中，单例的类只实例化一次，它尝尝应用与数据库操作、日志函数。
在一个大象项目中使用到日志和数据库操作的地方有很多，不能每个文件都去单独实例化一，
此时单例模式就显示出他的价值。
单例的核心在类的内部分方法__new__()，每次实例化都是通过执行new函数来返回实例对象。
单例就是在类里面定义一个作用域最高的标志性的属性，如果实例化过一次，那这个属性
为True否则为False,那么返回上次实例化的对象即可。

通过hasattr函数判断实例化时有没有_instance属性
如果不存在，那么继续并返回原始的__new__方法给_instance属性
如果存在则直接返回_instance属性所指的对象
'''

class Nomarl(object):

    def run(self):
        print('11111')

class Singleton(object):

    def __new__(cls,*args,**kwargs):

        if not hasattr(cls,'_instance'):
            '''
            复写内部方法__new__()
            '''
            org=super(Singleton,cls)
            cls._instance=org.__new__(cls,*args,**kwargs)
        return cls._instance


if __name__ == "__main__":
    obj1=Singleton()
    obj2=Singleton()
    print('obj1:{}=====obj2:{}'.format(obj1,obj2))
    obj3=Nomarl()
    obj4=Nomarl()
    print('obj3:{}=====obj4:{}'.format(obj3,obj4))


'''
结果：
obj1:<__main__.Singleton object at 0x00000000038E6198>=====obj2:<__main__.Singleton object at 0x00000000038E6198>
obj3:<__main__.Nomarl object at 0x00000000038E6390>=====obj4:<__main__.Nomarl object at 0x00000000038E6630>
'''