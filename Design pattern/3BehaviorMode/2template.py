#模板方法模式

'''
意图：
定义一个操作的算法的骨架，而将一些步骤延迟到子类中。
TemplateMethod使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。

'''

class User:

    def __init__(self,name,shop,times,number):
        self.name=name
        self.shop=shop
        self.times=times
        self.number=number
    
class Handle:

    def __init__(self,user=None):
        self.user=user
    
    def Invoicen(self):
        string="打印小票"\
            "客户:{}"\
            "商品:{}"\
            "数量:{}"\
            "时间:{}".format(self.user.name,self.user.shop,self.user.number,self.user.times)
        print(string)

    def make(self):
        print('制作玩:{}数量：{}'.format(self.user.shop,self.user.number))
    
    def run(self):
        self.Invoicen()
        self.make()
        
if __name__ == "__main__":
    test=Handle()
    xiaoming=User("小明","汉堡","17:50","5")
    test.user=xiaoming
    test.run()