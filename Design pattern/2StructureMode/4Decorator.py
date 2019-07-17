#Decorator 装饰

'''
意图：
动态地给一个对象添加一些额外的职责，新增功能来说，Decorator模式相比生成子类更灵活

适用性：
在不影响其他对象的情况下，以动态、透明的方式给单个对象添加职责。
处理那些可以撤销的职责。

#例子：
一个人类，会说话，能学习。如何在不继承和重写该人类的情况下让人类有开车的功能？


'''

class Person:

    def study(self):
        print('学习')
    
    def speak(self):
        print('说话')


class Decorator:

    def __init__(self,name):
        self._run=name
    
    def drive(self):
        print('开车')
    
    def __getattr__(self,item):
        return getattr(self._run,item)


if __name__ == "__main__":
    person=Person()
    driver=Decorator(person)
    driver.study()
    driver.speak()
    driver.drive()
    