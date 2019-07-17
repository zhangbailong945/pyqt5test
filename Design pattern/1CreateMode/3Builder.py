'''
Builder (建造者模式)
意图：
将一个赋值对象的构造与它的表示分离，使得同样的构建过程可以创建不同的表示
适用性：
当创建复杂对象的算法应该独立该对象的组成部分以及他们的装配方式时
当构造构成必须允许被构造的对象有不同的表示时
'''

class Builder():
    '''
    建造流程
    '''
    def __init__(self):
        self.wheel=None
        self.shell=None
        self.engine=None
    
    def create(self):
        print('造车子，%s,%s,%s.'%(self.wheel,self.shell,self.engine))
    
class A(Builder):
    '''方案A'''
    def get_wheel(self):
        self.wheel='铝合金轮毂'
    
    def get_shell(self):
        self.shell='白色壳子'
    
    def get_engine(self):
        self.engine='FG86'

class B(Builder):
    '''方案B'''
    def get_wheel(self):
        self.wheel='碳纤维轮毂'
    
    def get_shell(self):
        self.shell='红色壳子'
    
    def get_engine(self):
        self.engine='FG88'
    

class Director:
    '''
    调度：轮子壳子引擎
    '''
    def __init__(self):
        self.select = None

    def build(self):
        self.select.get_wheel()
        self.select.get_shell()
        self.select.get_engine()
        self.select.create()


if __name__ == "__main__":
    #造铝合金白色车子
    car1=Director()
    car1.select=A()
    car1.build()

    #早碳纤维红色车子
    car2=Director()
    car2.select=B()
    car2.build()
    

