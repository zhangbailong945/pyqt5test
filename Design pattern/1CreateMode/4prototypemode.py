
'''
原型模式
'''
'''
意图：
用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象
适用性：
1.当要实例化的类在运行时时刻指定时，例如，通过动态装载
2.为了避免创建一个与产品类层次平行的工厂层次时；
3.当一个类的实例化只能有几个不同状态组合中的一种时，建立相应数目的原型并克隆他们
可能比每次用合适的状态手工实例化该类更方便一些。
'''
import copy

class Prototype:

    def __init__(self,obj):
        self.copy_object=obj()
    
    def clone(self,**attr):
        obj=copy.deepcopy(self.copy_object)
        obj.__dict__.update(attr)
        return obj


class Information:

    def __init__(self):
        self.name=None
        self.age=None
        self.height=None
    
    def run(self):
        print("我叫{}:年龄:{}身高:{}".format(self.name,self.age,self.height))


if __name__ == "__main__":
    mode=Prototype(Information)
    user1=mode.clone(name='张三',age=20,height="178cm")
    user1.run()
    user2=mode.clone(name='李四',age=30,height="198cm")
    user2.run()
    
