#桥接

'''
意图
将抽象部分与它的实现部分分离，使他们都可以独立地变化

适用性
你不希望在抽象和它实现部分之间有一个固定的绑定关系。
类的抽象以及它的实现都应该通过生成子类的方法加以扩充。这时Bridge模式
你可以对不同的抽象接口和实现部分进行组合，并分别对他们进行扩充。

对一个的抽象的实现部分的修改应对客户不产生影响，即客户的代码不必重新编译。

桥接，像一座桥连接两岸，而python程序设计中的桥接是指抽象部分和实体部分的连接。
简单来说就是类和类实例化过程的连接。
核心的思想：
通过封装，将一个抽象类的相关参数和方法分别作为桥接类的属性，这样在实例化桥接
类后通过修改桥接类的属性，便可以实现抽象和实现直接的独立变化。


'''

class A:

    def run(self,name):
        print("my name is :{}".format(name))


class B:

    def run(self,name):
        print("我的名字叫：{}".format(name))


class Bridge:

    def __init__(self,age,classname):
        self.age=age
        self.classname=classname
    
    def bridge_run(self):
        self.classname.run(self.age)
    

if __name__ == "__main__":
    test=Bridge('张三',A())
    test.bridge_run()
    test.age=20
    test.bridge_run()
    test.classname=B()
    test.age='lisi'
    test.bridge_run()
    test.age='李四'
    test.bridge_run()
    