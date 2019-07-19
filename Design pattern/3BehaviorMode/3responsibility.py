'''
责任链 responsibility
意图：
使用多个对象都有机会处理请求，从而避免请求的发送者和接受者之间的耦合关系。
将这些对象连成一条链，并沿着这条链传递该请求，直到有一个对象处理它为止。

责任链要点：
1.一个对象含有另一个对象的引用以此类推形成链条。
2.每个对象中应该有明确的责任划分即处理请求条件
3.链条的最后一节应该设计成通用请求处理，以免出现漏洞。
4.请求应该传入链条的头部


'''

class Bases:

    def __init__(self,obj=None):
        self.obj=obj
    
    def screen(self,number):
        pass
    
class A(Bases):
    
    def screen(self,number):
        if 200>number>100:
            print("{}划入A集合".format(number))
        else:
            self.obj.screen(number)

class B(Bases):
    
    def screen(self,number):
        if number>=200:
            print("{}划入B集合".format(number))
        else:
            self.obj.screen(number)      


class C(Bases):
    
    def screen(self,number):
        if 100>=number:
            print("{}划入C集合".format(number))
        else:
            self.obj.screen(number) 

if __name__ == "__main__":
    test=[10,100,150,200,300,400]
    c=C()
    b=B(c)
    a=A(b)
    for i in test:
        a.screen(i)